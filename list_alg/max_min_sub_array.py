class MaxMinSubArray:
    def maxSubArray(self, nums):
        '''
        给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。
        :param nums:
        :return:
        '''
        # write your code here
        n = len(nums)
        maxSum = sum(nums)
        curSum = 0
        for i in range(n):
            # 从i开始求和，如果当前和大于maxSum,则赋值给maxSum
            curSum += nums[i]
            if curSum > maxSum:
                maxSum = curSum
            # 前面的和如果已经小于0了，那么加上下一个元素值，肯定是小于下一个元素值
            # 所以如果前面加起来的值小于0了，则舍弃前面的和，从下一位开始继续求和
            if curSum < 0:
                curSum = 0
        return maxSum

    def minSubArray(self, nums):
        '''
        给定一个整数数组，找到一个具有最小和的子数组，返回其最小和。
        :param nums:
        :return:
        '''
        # write your code here
        n = len(nums)
        minSum = sum(nums)
        curSum = 0
        for i in range(n):
            # 从i开始求和，如果当前和小于于minSum,则赋值给minSum
            curSum += nums[i]
            if curSum < minSum:
                minSum = curSum
            # 前面的和如果已经大于0了，那么加上下一个元素值，肯定是大于下一个元素值
            # 所以如果前面加起来的值大于0了，则舍弃前面的和，从下一位开始继续求和
            if curSum > 0:
                curSum = 0
        return minSum

    def kMaxSubArray(self, nums, k):
        if not nums:
            return 0

        n = len(nums)
        localMax = [[0 for i in range(k + 1)] for i in range(n + 1)]
        globalMax = [[0 for i in range(k + 1)] for i in range(n + 1)]

        # 边界初始化
        for k in range(k + 1):
            localMax[k][0] = globalMax[k][0] = 0

        for i in range(1, n + 1):
            # 边界初始化
            localMax[i][0] = 0
            globalMax[i][0] = 0
            for k in range(1, k + 1):
                localMax[i][k] = max(localMax[i - 1][k] + nums[i - 1], globalMax[i - 1][k - 1] + nums[i - 1])
                globalMax[i][k] = max(globalMax[i - 1][k], localMax[i][k])

        return globalMax[n][k]


if __name__ == '__main__':
    arr = [-1, 4, -2, 3, -2, 3]
    mm = MaxMinSubArray()
    print(mm.kMaxSubArray(arr, 2))
