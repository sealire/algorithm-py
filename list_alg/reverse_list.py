from struct_alg.node import Node
import util_alg.list_util as lu


def reverse(list_input):
    '''
    翻转一个链表
    '''
    if list_input is None:
        return None
    nl, first, second = None, list_input, list_input.next
    while second is not None:
        first.next = nl
        nl, first, second = first, second, second.next
    first.next = nl

    return first


def mn_reverse(list_input, m, n):
    '''
    翻转链表中第m个节点到第n个节点的部分
    '''
    if list_input is None:
        return None
    count, ml, nl, first, second, rn, rnl = 1, None, list_input, list_input, list_input.next, None, None
    while second is not None:
        if count >= m:
            if count > n:
                break
            if rnl is None:
                rnl = first
            first.next = rn
            rn, first, second = first, second, second.next
        else:
            ml, first, second = first, second, second.next
        count += 1

    if count <= n:
        first.next = rn
        rn, first = first, second
    if first is not None:
        rnl.next = first
    if ml is not None:
        ml.next = rn
        return list_input
    else:
        return rn


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    lu.print_list(a)

    r = mn_reverse(a, 1, 3)
    lu.print_list(r)
