class Node:
  def __init__(self,data=None):
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
  def search(self,val):
    temp = self.head
    
    while temp.next is not None:
      if temp.next.data==val:
        return "true"
      else:
        temp = temp.next
    return "false"
      

linked = LinkedList()
k= [1,2,3,4,5,6,7]
p=int(input("search the element:"))
for i in k:
  linked.append(i)
print(linked.search(p))