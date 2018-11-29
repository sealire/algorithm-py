from collections import deque
from struct_alg.node import TreeNode

'''
设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”
'''


def serialize(tree):
    ser = []
    queueA = deque()
    queueB = deque()

    queueA.append(tree)
    size = 1
    count = 0
    while size > 0:
        sc = size
        while sc > 0:
            node = queueA.popleft()
            queueB.append(node)
            if node.left is not None:
                count += 1
            if node.right is not None:
                count += 1
            sc -= 1

        sc = size
        size = 0
        while sc > 0:
            node = queueB.popleft()
            ser.append(node.value)
            sc -= 1

            if count > 0:
                if node.left is not None:
                    queueA.append(node.left)
                else:
                    queueA.append(TreeNode("#"))

                if node.right is not None:
                    queueA.append(node.right)
                else:
                    queueA.append(TreeNode("#"))

                size += 2

        count = 0
    return ser


def deserialize(ser):
    queue = deque()
    tree = TreeNode(ser[0])
    queue.append(tree)

    length = len(ser)
    for i in range(0, length // 2):
        parent = queue.popleft()
        il = 2 * i + 1
        if il < length:
            nl = ser[il]
            left = TreeNode(nl)
            queue.append(left)
            if nl != '#':
                parent.left = left
            ir = il + 1
            if ir < length:
                nr = ser[ir]
                right = TreeNode(nr)
                queue.append(right)
                if nr != '#':
                    parent.right = right
            else:
                break
        else:
            break

    return tree


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)

    tree = n1
    n1.left = n2
    n1.right = n3

    n2.right = n4
    n3.left = n5

    n4.left = n6
    n4.right = n7

    n5.left = n8
    n8.right = n9

    ser = serialize(tree)
    print(ser)

    nt = deserialize(ser)
    print(serialize(nt))
