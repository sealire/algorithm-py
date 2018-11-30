class SubSet:
    def sub_set(self, input_list):
        ss = []
        length = len(input_list)
        if length == 0:
            ss.append([])
            return ss

        input_copy = input_list[1:length]
        vs = self.sub_set(input_copy)
        for s in vs:
            ss.append(s[:])
            s.insert(0, input_list[0])
            ss.append(s)
        return ss


if __name__ == '__main__':
    subset = SubSet().sub_set([2, 2, 1])
    print(subset)
