class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, pos):
        new_node = Node(data)

        if pos <= 0:
            print("Position must be >= 1.")
            return

        # Insert at beginning
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"{data} inserted at position {pos}")
            return

        current = self.head
        count = 1

        # Traverse to the node before the target position
        while current is not None and count < pos - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds.")
            return

        new_node.next = current.next
        current.next = new_node
        print(f"{data} inserted at position {pos}")

    def delete(self, key):
        current = self.head
        # Case 1: Deleting the head node
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            print(f"{key} deleted from the list")
            return

        # Case 42: Deleting a node other than the head
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        # If key was not present in the list
        if current is None:
            print(f"{key} not found in the list")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None
        print(f"{key} deleted from the list")


    def display(self):
        if self.head is None:
            print("No elements in the list.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Driver code
ll = LinkedList()

while True:
    print("\nLinked List Operations")
    print("1. Insert at Position")
    print("2. Display")
    print("3. Delete by Value")
    print("4. Exit")


    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            data = int(input("Enter a value to insert: "))
            pos = int(input("Enter position: "))
            ll.insert_at_position(data, pos)
        except ValueError:
            print("Please enter valid integer values.")
    elif choice == '2':
        ll.display()
    elif choice == '3':
        try:
            key = int(input("Enter the value to delete: "))
            ll.delete(key)
        except ValueError:
            print("Please enter a valid integer value.")
    elif choice == '4':
        print("Exit the operation...")
        break
    else:
        print("Invalid choice. Please pick 1, 2, 3 or 4.")