class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                print(f"{key} found in the list")
                return True
            current = current.next
        print(f"{key} not found in the list")
        return False

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

# Example usage:
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()
my_list.search(2)
my_list.search(4)