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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node
# LinkedList class manages the nodes and operations of the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
# Example usage:
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()
