from struct_alg.node import TreeNode
import tree_alg.serialize as ts


def convert(input_list):
    length = len(input_list)
    if length == 0:
        return None

    tree = TreeNode(input_list[0])
    for k in range(1, length):
        num = input_list[k]
        node = tree
        while True:
            if num < node.value:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = TreeNode(num)
                    break
            else:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = TreeNode(num)
                    break

    return tree


def search(search_tree, min, max, result):
    if search_tree.left is not None:
        search(search_tree.left, min, max, result)

    if search_tree.value >= min and search_tree.value <= max:
        result.append(search_tree.value)

    if search_tree.right is not None:
        search(search_tree.right, min, max, result)

    return result


if __name__ == '__main__':
    arr = [8, 4, 3, 6, 4, 12, 6, 7, 2]
    tree = convert(arr)

    print(ts.serialize(tree))
    result = []
    search(tree, 5, 18, result)

    print(result)
