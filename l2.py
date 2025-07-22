class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        # If the list is empty
        if self.head is None:
            self.head = new_node
            print(f"{data} inserted at end (first node).")
            return

        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"{data} inserted at end.")

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
    print("\nLinked List - Insert At End")
    print("1. Insert at End")
    print("2. Display")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            data = int(input("Enter the data: "))
            ll.insert_at_end(data)
        except ValueError:
            print("Please enter a valid integer.")
    elif choice == '2':
        ll.display()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
