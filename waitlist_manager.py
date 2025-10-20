# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    # Add to front (VIP)
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    # Add to end (general customer)
    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Remove a customer by name
    def remove(self, name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"{name} removed from the waitlist.")
                return True
            prev = current
            current = current.next
        print(f"{name} not found in the waitlist.")
        return False

    # Print current waitlist
    def print_list(self):
        current = self.head
        if not current:
            print("Waitlist is empty.")
            return
        waitlist = []
        while current:
            waitlist.append(current.name)
            current = current.next
        print(" -> ".join(waitlist))


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)

        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Call the waitlist_generator function to start the program
if __name__ == "__main__":
    waitlist_generator()


'''
Design Memo:

This waitlist uses a custom singly linked list to manage customers dynamically. Each Node stores a customer's name and a reference to the next Node in the list. The head node represents the start of the list and acts as the entry point for all operations, such as adding or removing customers. Adding to the front inserts a new Node at the head, while adding to the end traverses the list to append a new Node. Removing a customer requires searching the list for a matching Node and updating the previous Node's reference to skip it. Printing the list traverses from head to tail, showing all current customers.

The head is crucial because it anchors the list; without it, we would have no way to access the linked structure. Custom linked lists like this are valuable when a system requires precise control over insertion and deletion, especially in dynamic, real-time applications where VIPs or priority elements need special handling. Unlike standard lists, a linked list can efficiently insert or remove elements without shifting other items in memory.

Real-world engineers might use this approach in event ticketing, customer support queues, or any situation where priorities change frequently, and the order of processing is important. Implementing this from scratch reinforces understanding of pointers, memory management, and object-oriented programming.
'''
