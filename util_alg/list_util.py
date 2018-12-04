
def print_list(single_list_input):
    a = single_list_input
    while a is not None:
        print(a.value, end="->")
        a = a.next
    print()