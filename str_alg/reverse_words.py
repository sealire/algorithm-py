'''
给定一个字符串，逐个翻转字符串中的每个单词。
'''


def reverse(str):
    chars = []
    start, end = -1, -1
    for i in range(len(str)):
        if str[i] != ' ':
            if start != -1:
                end = i
            else:
                start = i
        elif start != -1:
            for k in range(start, end + 1)[::-1]:
                chars.append(str[k])
            start = -1
            if end != -1:
                chars.append(' ')
                end = -1
    if start != -1:
        for k in range(start, end + 1)[::-1]:
            chars.append(str[k])
    length = len(chars)
    if chars[length - 1] == ' ':
        chars.pop()
        length -= 1
    for i in range(length // 2):
        chars[i], chars[length - 1 - i] = chars[length - 1 - i], chars[i]
    return '[' + ''.join(chars) + ']'


if __name__ == '__main__':
    print(reverse("  the world   hello me  two "))
