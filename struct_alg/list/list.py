list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

# 第1个元素，返回的是字符串
print("list1[0]: ", list1[0])

# 第2到5个元素，返回的是一个列表
print("list2[1:5]: ", list2[1:5])

list1[2] = 2001
print("list1: ", list1)

del list1[2]
print("list1: ", list1)

print(len(list1))
print(list1 * 2)

print(list1 + list2)
