class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"{data} inserted at beginning.")

    def display(self):
        if self.head is None:
            print("No elements in the list.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create linked list object
ll = LinkedList()

# Menu loop
while True:
    print("\nLinked List - Insert At Beginning")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            data = int(input("Enter the data: "))
            ll.insert_at_beginning(data)
        except ValueError:
            print("Please enter a valid integer.")
    elif choice == '2':
        ll.display()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
