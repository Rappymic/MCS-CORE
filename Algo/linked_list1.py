class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_data = Node(data=data, next=self.head)
        self.head = new_data

    def pr(self):
        nodes = []
        while 
