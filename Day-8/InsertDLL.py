class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class DoublyLinkedList:
  def __init__(self):
      self.head = None

  def insert_at_end(self, data):
      new_node = Node(data)
      if self.head is None:  
          self.head = new_node
      else:
          current = self.head
          while current.next: 
              current = current.next
          current.next = new_node
          new_node.prev = current

  def insert_at_front(self, data):
      new_node = Node(data)
      if self.head is None: 
          self.head = new_node
      else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node

  def insert_after_node(self, prev_node_data, data):
      current = self.head
      while current and current.data != prev_node_data:  
          current = current.next
      if current is None:
          print(f"Node with data {prev_node_data} not found.")
          return
      new_node = Node(data)
      new_node.next = current.next
      current.next = new_node
      new_node.prev = current

      if new_node.next: 
          new_node.next.prev = new_node

  def insert_before_node(self, next_node_data, data):
      current = self.head
      while current and current.data != next_node_data:  
          current = current.next
      if current is None:
          print(f"Node with data {next_node_data} not found.")
          return
      new_node = Node(data)
      new_node.prev = current.prev
      new_node.next = current
      current.prev = new_node

      if new_node.prev:  
          new_node.prev.next = new_node
      else:
          self.head = new_node 

  def display(self):
      current = self.head
      while current:
          print(current.data, end=" <-> ")
          current = current.next
      print("None")

def populate_dll(dll, array):
  for item in array:
      dll.insert_at_end(item)

def menu():
  dll = DoublyLinkedList()
  array = [1, 2, 3, 4, 5, 6]
  populate_dll(dll, array)

  while True:
      print("Choose an option:")
      print("1. Insert at the front")
      print("2. Insert at the end")
      print("3. Insert after a given node")
      print("4. Insert before a given node")
      print("5. Display the list")
      print("6. Exit")

      choice = int(input("Enter your choice: "))

      if choice == 1:
          data = int(input("Enter the data to insert at the front: "))
          dll.insert_at_front(data)
      elif choice == 2:
          data = int(input("Enter the data to insert at the end: "))
          dll.insert_at_end(data)
      elif choice == 3:
          prev_node_data = int(input("Enter the data of the node after which to insert: "))
          data = int(input("Enter the data to insert: "))
          dll.insert_after_node(prev_node_data, data)
      elif choice == 4:
          next_node_data = int(input("Enter the data of the node before which to insert: "))
          data = int(input("Enter the data to insert: "))
          dll.insert_before_node(next_node_data, data)
      elif choice == 5:
          print("Doubly Linked List:")
          dll.display()
      elif choice == 6:
          print("Exiting...")
          break
      else:
          print("Invalid choice. Please choose again.")

menu()
