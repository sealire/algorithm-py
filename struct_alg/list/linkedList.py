from struct.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def headappend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def tailappend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def remove(self, value):
        head = self.head

        if head is None:
            return

        if head.value == value:
            self.head = head.next
            return

        node = head
        while node.next is not None:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next


linkedList = LinkedList()
linkedList.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
linkedList.head.next = e2
e2.next = e3

linkedList.headappend("Sun")
linkedList.tailappend("Thu")
linkedList.tailappend("Wed")

linkedList.print()

linkedList.remove("Wed")
print("after remove Wed:")
linkedList.print()

linkedList.remove("Sun")
print("after remove Sun:")
linkedList.print()

linkedList.remove("Wed")
print("after remove Wed:")
linkedList.print()

linkedList.remove("Wed")
print("after remove Wed:")
linkedList.print()
