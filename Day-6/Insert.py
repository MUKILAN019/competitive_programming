class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_first(self, val):
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert_last(self, val):
        if self.head.next is None:
            self.append(val)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(val)

    def insert_position(self, pos, ele):
        if pos < 0:
            print("Position cannot be negative")
            return
        temp = self.head
        count = 0
        while temp.next is not None and count < pos:
            temp = temp.next
            count += 1
        if count == pos:
            new_node = Node(ele)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print("Position out of range")

    def insert_value(self, value, i):
        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                new_node = Node(i)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("Value not found in the list")

    def output(self):
        result = []
        current = self.head.next
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

def insert_option(linked):
    print("Choose the type of insertion:")
    print("1. Insert at the beginning")
    print("2. Insert at the end")
    print("3. Insert at a specific position")
    print("4. Insert before a specific value")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        val = int(input("Enter the value to insert at the beginning: "))
        linked.insert_first(val)
    elif choice == 2:
        val = int(input("Enter the value to insert at the end: "))
        linked.insert_last(val)
    elif choice == 3:
        pos = int(input("Enter the position to insert at: "))
        ele = int(input("Enter the value to insert: "))
        linked.insert_position(pos, ele)
    elif choice == 4:
        value = int(input("Enter the value before which to insert: "))
        i = int(input("Enter the value to insert: "))
        linked.insert_value(value, i)
    else:
        print("Invalid choice!")


linked = LinkedList()
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for value in values:
    linked.append(value)

insert_option(linked)
print(linked.output())  
