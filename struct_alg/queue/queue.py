class Queue:

    def __init__(self):
        self.queue = list()

    def push(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False

    def size(self):
        return len(self.queue)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in Queue!"


queue = Queue()
queue.push("Mon")
queue.push("Tue")
queue.push("Wed")
print(queue.size())
print(queue.pop())
