'''
给定一个字符串source和一个目标字符串target，在字符串source中找到包括所有目标字符串字母的子串。

算法流程如下：
1. 先将target中所有的字符出现的次数保存到td数组中。
2. 遍历source数组，开始时start=0，i=0；
   start记录当前字串的起点，i相当于当前字串的终点。
   用found表示当前字串中包含target中字符的数目，如果found=target.length()则表明当前字串包含了target中所有字符，如果满足，进入下一步。
3. 将start后移，取出start前面多余的元素，已达到字串最小的目标。
4.判断，如果当前字串小于历史搜到的最小字串，则将当前字串的长度，起始点，结束点都记录，更新。
5.将start后移，寻找下一个字串。
'''


def minWindow(source, target):
    if source is None or len(source) == 0:
        return ""

    if target is None or len(target) == 0:
        return ""

    td = [0] * 256
    for tc in target:
        td[ord(tc)] += 1

    sd = [0] * 256
    minLen = len(source)
    start, first, end = 0, -1, 0
    found = 0  # 在source中发现了target中元素的数目

    for i in range(len(source)):
        osc = ord(source[i])
        sd[osc] += 1
        if sd[osc] <= td[osc]:
            found += 1

        if found == len(target):
            # 满足条件
            # 处理1：start后移，删除无用元素
            while start <= i and sd[ord(source[start])] > td[ord(source[start])]:
                sd[ord(source[start])] -= 1
                start += 1
            # 处理2：如果比当前最小子串小，则更新
            if i + 1 - start <= minLen:
                minLen = i + 1 - start
                first = start
                end = i + 1

            sd[ord(source[start])] -= 1
            start += 1
            found -= 1

    if first == -1:
        return ""
    else:
        return source[first:end]


if __name__ == '__main__':
    print(minWindow("ADOBECODEBANC", "ABC"))
