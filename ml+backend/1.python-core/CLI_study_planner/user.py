from datetime import datetime
from assignment import Assignment
import json
import os
import time

class User:
# --------------------------------- initialize ----------------------------------

    def __init__(self, username):
        self.username = username

        # subject_list format:
        # {
        #     <subject_name>:<hours_studied>
        # }

        self.subject_list = {}

        # assignment list format:
        # [{
        #     "assignment_name":<assignment_name>,
        #     "subject_name":<subject_name>,
        #     "topic":<topic_name>,
        #     "deadline":<date>,
        #     "urgency":<urgency> (either unimportant, important, or very important)  
        #     "difficulty":<difficulty> (scale of 1-10) 
        # }]

        self.assignment_list = []

# --------------------------------- save assignments ----------------------------------
    def save(self):
        os.makedirs("data", exist_ok=True)  # ensure directory exists

        filename = f"data/{self.username}_assignments.json"

        try:
            with open(filename, 'r') as f:
                existing_data = json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):  # handle missing file also
            existing_data = []

        # combine old + new
        all_assignments = existing_data + self.assignment_list

        try:
            with open(filename, 'w') as f:
                json.dump(all_assignments, f, indent=4)
            print(f"✅ Assignments saved successfully to {filename}")

        except Exception as e:
            print(f"⚠️ Error saving assignments: {e}")

# --------------------------------- create assignments ----------------------------------
    def create_assignment(self):

        assignment_name = input("\nEnter name of assignment: ").lower()
        subject_name = input("\nEnter name of subject: ").lower()
        topic_name = input("\nEnter name of topic: ").lower()

        self.subject_list[subject_name] = self.subject_list.get(subject_name, 0)

        # validate deadline format
        while True:
            deadline = input("\nEnter deadline in YYYY-MM-DD: ")

            try:
                datetime.strptime(deadline, "%Y-%m-%d")
                break

            except ValueError:
                print("⚠️ Invalid date format. Please use YYYY-MM-DD.")

        # validate urgency
        urgency = ""

        while urgency not in ["unimportant", "important", "very important"]:

            urgency = input("\nEnter urgency of assignment (unimportant, important, very important): ").lower()
            if urgency not in ["unimportant", "important", "very important"]:
                print("⚠️ Invalid urgency. Please enter one of: unimportant, important, very important.")

        # validate difficulty
        while True:

            try:
                difficulty = float(input("\nEnter difficulty from scale of 1-10, decimals allowed: "))
                if 1 <= difficulty <= 10:
                    break
                else:
                    print("⚠️ Difficulty must be between 1 and 10.")
            except ValueError:
                print("⚠️ Please enter a valid number for difficulty.")

        new_assignment = Assignment(
            assignment_name,
            subject_name,
            topic_name,
            deadline,
            urgency,
            difficulty
        )

        self.assignment_list.append({
            "assignment_name": new_assignment.name,
            "subject_name": new_assignment.subject,
            "topic": new_assignment.topic,
            "deadline": new_assignment.deadline,
            "urgency": new_assignment.urgency,
            "difficulty": new_assignment.difficulty
        })

        print("\n✅ Assignment created and added successfully!")
        self.save()

# --------------------------------- load assignments ----------------------------------
    def load_assignments(self):

        filename = f"data/{self.username}_assignments.json"
        try:

            with open(filename, 'r') as f:

                self.assignment_list = json.load(f)
            print(f"✅ Assignments loaded successfully from {filename}\n")

            if not self.assignment_list:

                print("No assignments found.")

            else:

                print("Here are your assignments:")
                for i, assignment in enumerate(self.assignment_list, 1):

                    print(f"\nAssignment {i}:")
                    print(f"  Name: {assignment['assignment_name']}")
                    time.sleep(0.7)
                    print(f"  Subject: {assignment['subject_name']}")
                    time.sleep(0.7)
                    print(f"  Topic: {assignment['topic']}")
                    time.sleep(0.7)
                    print(f"  Deadline: {assignment['deadline']}")
                    time.sleep(0.7)
                    print(f"  Urgency: {assignment['urgency']}")
                    time.sleep(0.7)
                    print(f"  Difficulty: {assignment['difficulty']}")
                    time.sleep(0.7)

        except (FileNotFoundError, json.JSONDecodeError):

            self.assignment_list = []
            print(f"⚠️ No existing assignments found, starting fresh.")

# --------------------------------- add subjects ---------------------------------
    def add_subjects(self):

        new_subject = input("Enter new subject name: ")
        hours_studied = float(input("Enter hours studied (decimal works): "))

        self.subject_list[new_subject] = hours_studied

# --------------------------------- track time ------------------------------------
    def track_time(self):

        subject = ""

        while subject not in self.subject_list.keys():

            subject = input("Enter subject: ")

        time_spent = float(input("How many hours did you study: "))
        self.subject_list[subject] += time_spent

# ------------------------------- show time -----------------------------------
    def show_time(self):

        for subject, hours in self.subject_list.items():
            print(f"Hours studied for {subject}: {hours}")

# ------------------------------ show subjects ------------------------------
    def show_subjects(self):

        print("Current subject:")

        for subject in self.subject_list.keys():
            print(f"\t {subject}")
            print("\n")

# -------------------------------- display time for specific subjects -------------------
    def show_specific_time(self):

        subject = input("Enter subject name: ").lower()

        try:
            time = self.subject_list[subject]
            print(f"Time spent: {time} hours")
        
        except:
            print("\nSubject not found\n")
            print("Here are your current subjects:\n")
            self.show_subjects()

# ------------------------------ modify task ----------------------------------
    def modify_assignment(self):

        if not self.assignment_list:

            print("⚠️ No assignments to modify.")
            return

        print("\nWhich assignment would you like to modify?")
        for i, assignment in enumerate(self.assignment_list, 1):

            print(f"{i}. {assignment['assignment_name']} (Subject: {assignment['subject_name']})")

        try:
            choice = int(input("Enter the number of the assignment: "))
            if not (1 <= choice <= len(self.assignment_list)):
                print("⚠️ Invalid selection.")
                return

            assignment = self.assignment_list[choice - 1]

            print("\nWhat do you want to modify?")
            print("1. Name")
            print("2. Subject")
            print("3. Topic")
            print("4. Deadline")
            print("5. Urgency")
            print("6. Difficulty")
            field_choice = input("Enter choice (1-6): ")

            if field_choice == "1":

                assignment["assignment_name"] = input("Enter new name: ").lower()

            elif field_choice == "2":

                assignment["subject_name"] = input("Enter new subject: ").lower()

            elif field_choice == "3":

                assignment["topic"] = input("Enter new topic: ").lower()

            elif field_choice == "4":

                while True:
                    new_deadline = input("Enter new deadline (YYYY-MM-DD): ")
                    try:
                        datetime.strptime(new_deadline, "%Y-%m-%d")
                        assignment["deadline"] = new_deadline
                        break
                    except ValueError:
                        print("⚠️ Invalid date format.")

            elif field_choice == "5":

                while True:
                    urgency = input("Enter new urgency (unimportant, important, very important): ").lower()
                    if urgency in ["unimportant", "important", "very important"]:
                        assignment["urgency"] = urgency
                        break
                    else:
                        print("⚠️ Invalid urgency level.")

            elif field_choice == "6":

                while True:
                    try:
                        difficulty = float(input("Enter new difficulty (1-10): "))
                        if 1 <= difficulty <= 10:
                            assignment["difficulty"] = difficulty
                            break
                        else:
                            print("⚠️ Must be between 1 and 10.")
                    except ValueError:
                        print("⚠️ Please enter a number.")

            else:
                print("⚠️ Invalid field choice.")
                return

            print("✅ Assignment modified successfully.")
            self.save()

        except ValueError:
            print("⚠️ Please enter a valid number.")

# ---------------------------------------- complete task ----------------------------------------
    def mark_assignment_complete(self):
        
        if not self.assignment_list:
            print("⚠️ No assignments to mark as complete.")
            return

        print("\nWhich assignment did you complete?")
        for i, assignment in enumerate(self.assignment_list, 1):
            print(f"{i}. {assignment['assignment_name']} (Subject: {assignment['subject_name']})")

        try:
            choice = int(input("Enter the number of the completed assignment: "))
            if not (1 <= choice <= len(self.assignment_list)):
                print("⚠️ Invalid selection.")
                return

            completed = self.assignment_list.pop(choice - 1)
            print(f"✅ '{completed['assignment_name']}' marked as complete and removed.")
            self.save()

        except ValueError:
            print("⚠️ Please enter a valid number.")
