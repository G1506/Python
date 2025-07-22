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
    print("3. Exit")

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
        print("Exit the operation...")
        break
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
