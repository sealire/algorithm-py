class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False

    def peek(self):
        return self.stack[0]

    def pop(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()


stack = Stack()
stack.push("Mon")
stack.push("Tue")
stack.peek()
print(stack.peek())
stack.push("Wed")
stack.push("Thu")
print(stack.peek())

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
