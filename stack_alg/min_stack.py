class MinStack:
    def __init__(self, value=None):
        self.__value = []
        self.__min = []
        for v in value:
            self.push(v)

    def push(self, v):
        self.__value.append(v)
        ml = len(self.__min)
        if ml == 0:
            self.__min.append(v)
        elif v <= self.__min[ml - 1]:
            self.__min.append(v)

    def pop(self):
        if len(self.__value) == 0:
            raise Exception("stack empty!")
        v = self.__value.pop()
        ml = len(self.__min)
        if v == self.__min[ml - 1]:
            self.__min.pop()

    def min(self):
        if len(self.__min) == 0:
            raise Exception("stack empty!")
        ml = len(self.__min)
        return self.__min[ml - 1]


if __name__ == '__main__':
    ms = MinStack([4, 2, 4, 6, 9, 1, 1])
    print(ms.min())
    ms.pop()
    print(ms.min())
    ms.pop()
    print(ms.min())
