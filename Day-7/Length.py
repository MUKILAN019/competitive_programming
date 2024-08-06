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
  def length(self):
    temp = self.head
    c=0
    while temp.next is not None:
      temp=temp.next
      c=c+1
    return c

linked = LinkedList()
k= [1,2,3,4,5,6,7]
for i in k:
  linked.append(i)
print(linked.length())