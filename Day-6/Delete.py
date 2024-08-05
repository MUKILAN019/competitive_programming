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

    def delete_first(self):
        if self.head.next is None:
            return
        self.head.next = self.head.next.next

    def delete_last(self):
        if self.head.next is None:
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_position(self, pos):
        if pos < 0 or self.head.next is None:
            return
        temp = self.head
        count = 0
        while temp.next is not None and count != pos:
            temp = temp.next
            count += 1
        if temp.next is not None:
            temp.next = temp.next.next

    def delete_value(self, value):
        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    def output(self):
        result = []
        current = self.head.next
        while current is not None:
            result.append(current.data)
            current = current.next
        return result


def delete_option(linked):
    print("Choose the type of deletion:")
    print("1. Delete by value")
    print("2. Delete by position")
    print("3. Delete first element")
    print("4. Delete last element")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        value = int(input("Enter the value to delete: "))
        linked.delete_value(value)
    elif choice == 2:
        pos = int(input("Enter the position to delete: "))
        linked.delete_position(pos)
    elif choice == 3:
        linked.delete_first()
    elif choice == 4:
        linked.delete_last()
    else:
        print("Invalid choice!")


linked = LinkedList()
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for value in values:
    linked.append(value)
delete_option(linked)
print(linked.output())
