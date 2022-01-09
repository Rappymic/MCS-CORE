class Node:
    '''An object for storing a single node of a linked list
    Models two attributes - data and link to next node in list'''
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<Node data: %s>' % self.data

class Linked_List:
    '''Singly Linked List'''
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    def size(self):
        ''':return No of nodes in list'''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def __repr__(self):
        nodes = []
        current =  self.head

        while current:
            if current is self.head:
                nodes.append(current.data)
            elif current.next_node is None:
                nodes.append(current.data)
            else:
                nodes.append(current.data)
            current = current.next_node
        return '->'.join([str(i) for i in nodes])