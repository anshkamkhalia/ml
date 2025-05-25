from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def size_of_list(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node  

        return count  
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head  
        self.head = new_node

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return current
            else:
                current = current.next_node
                
        return None
    
    def insert(self, data, index):
        if index == 0:
            self.add(data)
            return

        if index > 0:
            new_node = Node(data)
            current = self.head
            position = index

            while position > 1 and current:
                current = current.next_node
                position -= 1

            if current is None:
                raise IndexError("Index out of bounds")

            new_node.next_node = current.next_node
            current.next_node = new_node


    def remove_node(self, data):
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == data and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == data:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node

        return current
    
    def append(self, data):
        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current:
            if current.next_node is None:
                current.next_node = new_node
                return  
            current = current.next_node

    def reverse(self):
        prev = None              
        current = self.head        

        while current is not None:
            next_node = current.next_node  
            current.next_node = prev       

            prev = current
            current = next_node

        self.head = prev

    def search_at_index(self, index):
        counter = 0
        current = self.head

        while current is not None:
            if counter == index:
                return current
            else:
                counter+=1
                current = current.next_node

        return None
    
    def clear(self):
        self.head = None

    def __repr__(self):
        
        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append(f"[Head: {current.data}]")

            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")

            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return "-> ".join(nodes)