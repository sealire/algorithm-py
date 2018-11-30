'''
给定一个数字列表，返回其所有可能的排列。
'''

class Permutation:
    def full_permutation(self, input_list):
        permutation = []
        temp = []
        for item in input_list:
            if len(permutation) == 0:
                permutation.append([item])
            else:
                for ip in permutation:
                    ipl = len(ip)
                    for k in range(ipl + 1):
                        nip = ip[:]
                        nip.append(item)
                        for ik in range(k, ipl)[::-1]:
                            nip[ik + 1] = nip[ik]
                        nip[k] = item
                        temp.append(nip)
                permutation = temp[:]
                temp = []
        return permutation


    def unique_permutation(self, nums):
        result = []
        if nums is None:
            return result
        n = len(nums)
        if n == 0:
            result.append([])
        nums.sort()
        i = 0

        # 遍历整个数组
        while i < n:
            # while循环筛除重复
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            # 抽取元素，记为x
            x = nums[i]
            # 复制列表，并将列表中去除x
            temp_nums = nums[:]
            temp_nums.remove(x)
            # 剩余元素全排列后，在所有排列的首位添加之前抽取的元素
            for ele in self.unique_permutation(temp_nums):
                ele.insert(0, x)
                result.append(ele)
            i += 1
        return result


if __name__ == '__main__':
    permutation = Permutation().unique_permutation([1, 2, 1])

    print(len(permutation))
    print(permutation)
