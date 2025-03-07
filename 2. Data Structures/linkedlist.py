class Node():
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

class linkedList():
  def __init__(self):
    self.head = None

n1, n2, n3, n4 = Node(1), Node(3), Node(5), Node(7)
LL = linkedList()

LL.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
