class Node:
    def __init__(self, value, nexNode=None, previous = None):
        self.value = value
        self.nexNode = nexNode
        self.previous = previous

class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def insert_end(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return
        current = self.head
        while True:
            if current.nexNode is None:
                current.nexNode = node
                current.previous = current
                break
            current = current.nexNode

    def print_values(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, '--->', end=' ')
            current_node = current_node.nexNode
        print(None)

    def print_rev(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, '--->', end=' ')
            current_node = current_node.previous
        print(None)

l1 = Linked_List()
l1.print_values()
l1.insert_end(3)
l1.print_values()
l1.insert_end(4)
l1.print_values()
# l1.insert_start(34)
l1.print_values()
l1.print_rev()