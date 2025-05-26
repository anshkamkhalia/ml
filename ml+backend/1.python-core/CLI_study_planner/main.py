# CLI Study Planner
import pandas as pd
import csv
from user import User

# ----------------------------------- authentication --------------------------------

account_df = pd.read_csv("data/accounts.csv")
accounts_empty = account_df.empty
global password

# sign up function
def sign_up():
    global username 
    
    # username
    while True:
        username = input("\nEnter your username: \n")
        if len(username) < 3:
            print("\nToo short\n")
            continue
        else:
            break
    
    def validate_password(password):
        # length of password
        if 6 > len(password) or 12 < len(password):
            return False
        else: 
            pass
        
        # checking if password contains numbers
        has_nums = False
        for num in [n for n in range(9)]:
            if str(num) not in password:
                continue
            else:
                has_nums = True

        if not has_nums:
            return False
        else:
            pass

        # checking if password has uppercase letters
        count_of_uppercase = 0
        for char in password:
            try:
                uppercase_char = char.upper()
                if char == uppercase_char:
                    count_of_uppercase += 1
                else:
                    continue
            except:
                pass

        # final check
        if has_nums and count_of_uppercase >= 2:
            return True
        else:
            return False

    # password
    while True:
        password = input("\nEnter password: \n")
        if validate_password(password=password):
            break
        else:
            print("\nInvalid, at between 6 - 12 characters, at least 2 numbers, and at least 2 uppercase characters\n")
            continue

    # add to csv file
    fields = [username, password]
    with open("data/accounts.csv", 'a') as f:
        try:
            writer = csv.writer(f)
            writer.writerow("")
            writer.writerow(fields)
            print("\nAccount saved successfully\n")
            print(f"\nWelcome {username}!\n")
        except Exception as e:
            print(f"Warning: Account not saved successfully because of {e}\n")




# checks if there are accounts already
if accounts_empty:
    # sign up
    sign_up()
else:
    # login or sign up
    while True:
        try:
            print("\nIt seems as if some accounts were already saved, would you like to log in(1) or sign up(2)?\n")
            choice = int(input())
        except:
            continue

        if choice == 1:
            # login
            valid_username = False
            while True:
                # get username 
                username = input("Enter username: ")
                if account_df["username"].str.contains(username).any():
                    print(f"\nWelcome back {username}, just enter your password\n")
                    valid_username = True
                    break
                else:
                    print("\nUsername not found\n")

            if valid_username:
                # get password
                while True:
                    password = input("Enter password: ")
                    if not account_df[(account_df["username"] == username) & (account_df["password"] == password)].empty:
                        print(f"\nWelcome back {username}!\n")
                        break
                    else:
                        print("\nPassword not found\n")
            break

        elif choice == 2:
            sign_up()
            break

        else:
            print("Invalid")
            
# ----------------------------------------- main loop ---------------------------
user = User(username)

while True:
    print("\n📚 What do you want to do?")
    print("1. Add assignment")
    print("2. Save data")
    print("3. Show assignments")
    print("4. Add subject")
    print("5. Track time")
    print("6. Show subjects")
    print("7. Show time for specific subjects")
    print("8. Modify an assignment")        
    print("9. Mark an assignment as complete")  
    print("q. Quit")

    action = input("Enter your choice: ").strip().lower()

    if action == "1":
        user.create_assignment()

    elif action == "2":
        user.save()

    elif action == "3":
        user.load_assignments()

    elif action == "4":
        user.add_subjects()

    elif action == "5":
        user.track_time()

    elif action == "6":
        user.show_subjects()

    elif action == "7":
        user.show_specific_time()

    elif action == "8":
        user.modify_assignment()

    elif action == "9":
        user.mark_assignment_complete()

    elif action == "q":
        print("👋 Bye!")
        break

    else:
        print("❓ Invalid input, try again.")

