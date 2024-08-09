class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_from_front(self):
        if self.head is None: 
            print("List is empty. No nodes to delete.")
            return
        if self.head.next is None: 
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_from_end(self):
        if self.head is None:
            print("List is empty. No nodes to delete.")
            return
        if self.head.next is None:  
            self.head = None
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.prev.next = None

    def delete_node(self, value):
        if self.head is None:  
            print("List is empty. No nodes to delete.")
            return

        current = self.head

        if current.data == value:
            self.delete_from_front()
            return

  
        while current and current.data != value:
            current = current.next

        if current is None:
            print(f"Node with value {value} not found.")
            return

      
        if current.next is None:
            self.delete_from_end()
            return

    
        current.prev.next = current.next
        current.next.prev = current.prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

def populate_dll(dll, array):
    for item in array:
        new_node = Node(item)
        if dll.head is None:
            dll.head = new_node
        else:
            current = dll.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

def menu():
    dll = DoublyLinkedList()
    array = [1, 2, 3, 4, 5, 6]
    populate_dll(dll, array)

    while True:
        print("Choose an option:")
        print("1. Delete from the front")
        print("2. Delete from the end")
        print("3. Delete a specific node by value")
        print("4. Display the list")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            dll.delete_from_front()
        elif choice == 2:
            dll.delete_from_end()
        elif choice == 3:
            value = int(input("Enter the value of the node to delete: "))
            dll.delete_node(value)
        elif choice == 4:
            print("Doubly Linked List:")
            dll.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

menu()
