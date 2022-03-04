class Element:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Linked_List():
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next