'''
正如标题所述，你需要使用两个栈来实现队列的一些操作。

队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。

pop和top方法都应该返回第一个元素的值。
'''


class StackQueue:

    def __init__(self, value=None):
        self.push_stack = []
        self.pop_stack = []

    def push(self, value):
        self.push_stack.append(value)

    def pop(self):
        if len(self.pop_stack) == 0:
            if len(self.push_stack) == 0:
                raise Exception("queue empty!")
            else:
                size = len(self.push_stack)
                for i in range(size):
                    self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()


if __name__ == '__main__':
    sq = StackQueue()
    sq.push('1')
    sq.push('2')
    sq.push('3')
    print(sq.pop())
    print(sq.pop())
    print(sq.pop())

