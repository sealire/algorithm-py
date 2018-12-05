class Solution:
    def nextPermutation(self, nums):
        '''
        给定一个若干整数的排列，给出按正数大小进行字典序从小到大排序后的下一个排列。如果没有下一个排列，则输出字典序最小的序列。

        1. 先找到需要改变的高位：从右向左扫描排列，若一直满足nums[i] > nums[i - 1]，则说明这些元素是满足高位大于低位的，不需操作，直到找到nums[i] < nums[i - 1]，
            找到高位比低位小的了，而且是“最低”的高位，这个位置就是我们需要做交换操作的。比如：6, 8, 7, 4, 3, 2 当中的8（发现6 < 8）
        2.第二步找要和这个高位交换的低位：原则是尽量寻找只比这个高位“大一点”的低位，因为只是下一个排列。
            因为在这个高位右边的数组满足从右往左递增，所以，我们重新从右边起扫描，找到第一个比这个高位大的元素。比如：6, 8, 7, 4, 3, 2 中的7.
        3. 交换高位与低位，使得高位变大：比如6, 8, 7, 4, 3, 2 -> 7, 8, 6, 4, 3, 2
        4.此时，不论交换后的高位后面的元素是如何排列的，都肯定比之前的排列靠后了。因为只是下一个排列，所以我们现在尽量要现在的这个排列“靠前”，
            怎么做呢，就是按升序排列高位后面的元素，比如：按升序排列此时7后面的元素。因为此时高位后面的元素一定是从左往右，从大到小，所以，也相当于是翻转这一部分的数组。
            比如：7, 8, 6, 4, 3, 2 -> 7, 2, 3, 4, 6, 8
        :param nums:
        :return:
        '''
        n = len(nums)
        if n == 0 or n == 1:
            return
        right_index = n - 1
        pivot = 0
        # 从右边起找第一个（i - 1, i），使得nums[i] > nums[i - 1]
        while right_index >= 0:
            if right_index - 1 >= 0 and nums[right_index] > nums[right_index - 1]:
                # 将找到的i - 1记为pivot
                pivot = right_index - 1
                break
            elif right_index == 0:
                pivot = right_index - 1
                break
            else:
                right_index -= 1
        # 若pivot < 0，则说明这是最后一个排列了，就需要将nums改为最小的排列
        if pivot < 0:
            nums.sort()
        else:
            right_index = n - 1
            # 从右边起，找第一个大于nums[pivot]的数，并将这个数与nums[pivot]交换
            while right_index >= 0:
                if nums[right_index] > nums[pivot]:
                    nums[right_index], nums[pivot] = nums[pivot], nums[right_index]
                    break
                else:
                    right_index -= 1
            # 将此时pivot之后的部分数组翻转（其实也就是重新排序）
            left = pivot + 1
            right = n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

    def prevPermuation(self, num):
        n = len(num)
        right = n - 1
        # 从右往左，找第一个升序
        while right > 0:
            if num[right] < num[right - 1]:
                break
            else:
                right -= 1
        # 如果整个数组是降序排列，颠倒过来
        if right == 0:
            num.reverse()
            return num
        # 定位需要交换的高位
        right -= 1
        index = n - 1
        # 从右往左，找第一个比这个高位小的低位
        while index > right:
            # 交换高地位
            if num[index] < num[right]:
                num[index], num[right] = num[right], num[index]
                break
            else:
                index -= 1
        # 将被交换的高位之后的部分数组按逆序排列，因为只是上1个
        return num[:right + 1] + sorted(num[right + 1:], reverse=True)


if __name__ == '__main__':
    arr = [2, 1, 3]
    Solution().nextPermutation(arr)
    print(arr)

    arr = [2, 1, 3]
    Solution().prevPermuation(arr)
    print(arr)
