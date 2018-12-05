from struct.node import Node


class DLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def headappend(self, value):
        node = Node(value)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def tailappend(self, value):
        node = Node(value)
        node.prev = self.tail
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def print(self, reverse):
        node = self.head
        if reverse:
            node = self.tail

        while node is not None:
            print(node.value)
            if reverse:
                node = node.prev
            else:
                node = node.next


dList = DLinkedList()
dList.tailappend(12)
dList.tailappend(8)
dList.tailappend(62)
dList.print(True)
