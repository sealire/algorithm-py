def majorityNumber(arr):
    '''
    给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。
    :param arr:
    :return:
    '''
    ele = arr[0]
    count = 0
    for i in arr:
        if ele == i:
            count += 1
        else:
            count -= 1
            if count <= 0:
                ele = i
    return ele


def kMajorityNumber(nums, k):
    '''
    首先，先要搞清楚这个问题在数学上的原理。既然主元素的判定标准是个数大于数组长度的1/k，那换句话说，就是满足如下的公式：
    x/n > 1/k
    其中，我假设x为主元素的个数，n为数组长度。然后，将这个公式化简，得到下面这个式子：
    x - 1 > n/k - 1  ->  (x - 1) / (n - k) > 1/ k
    这个式子说明了一个很重要的问题：当主元素的个数减1后，如果整个数组的长度也减去k，是不会影响主元素的“地位”的。
    :param nums:
    :param k:
    :return:
    '''
    hash_table = {}

    for i in nums:
        if i not in hash_table:
            hash_table[i] = 1
        else:
            hash_table[i] += 1

        if len(hash_table) == k:
            for key in hash_table:
                hash_table[key] -= 1
            temp = {}
            for key in hash_table:
                if hash_table[key] != 0:
                    temp[key] = hash_table[key]
            hash_table = temp

    for key in hash_table:
        hash_table[key] = 0

    for i in nums:
        if i in hash_table:
            hash_table[i] += 1

    return max(hash_table.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 5, 16, 17, 18, 19, 1]
    print(kMajorityNumber(arr, 10))
