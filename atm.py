class Node:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.next = None

class TransactionHistory:
    def __init__(self):
        self.head = None
        self.balance = 0

    def add_transaction(self, transaction_type, amount):
        new_node = Node(transaction_type, amount)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        if transaction_type == "Deposit":
            self.balance += amount
        elif transaction_type == "Withdrawal":
            self.balance -= amount

        print(f"{transaction_type} of Rs.{amount} recorded. Current balance: Rs.{self.balance}")


    def show_history(self):
        if not self.head:
            print("No transactions recorded yet.")
            return

        print("\n--- Transaction History ---")
        current = self.head
        while current:
            print(f"{current.transaction_type}: Rs.{current.amount}")
            current = current.next
        print("--------------------------")
        print(f"Current balance: Rs.{self.balance}")


# Driver code
history = TransactionHistory()

while True:
    print("\nATM Transaction Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. History")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                history.add_transaction("Deposit", amount)
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '2':
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0 and amount <= history.balance:
                history.add_transaction("Withdrawal", amount)
            elif amount > history.balance:
                print("Insufficient balance.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '3':
        history.show_history()
    elif choice == '4':
        print("Exiting ATM.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        