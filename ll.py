class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")

# Driver code
ll = LinkedList()

user_input = input("Enter numbers separated by space: ")

values = user_input.split()

for v in values:
    v = v.strip()
    if v == '':
        # skip empty strings
        continue
    try:
        num = int(v)
        ll.insert_at_end(num)
    except ValueError:
        print(f"Warning: '{v}' is not a valid integer and will be skipped.")

if ll.head is None:
    print("No valid input values provided.")
else:
    print("Original list:")
    ll.print_list()

    ll.reverse()

    print("Reversed list:")
    ll.print_list()