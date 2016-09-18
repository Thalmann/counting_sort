def counting_sort(l):
    k = max(l) + 1
    n = len(l)
    count = [0] * k

    for x in l:
        count[x] += 1

    total = 0
    for x in range(k):
        old = count[x]
        count[x] = total
        total += old

    result = [0] * n
    for x in l:
        result[count[x]] = x
        count[x] += 1

    return result


def print_list(l):
    for i, x in enumerate(l):
        print(i, x)


def counting_sort_print(l):
    k = max(l) + 1
    n = len(l)
    count = [0] * k

    print('Input:')
    print_list(l)

    for x in l:
        count[x] += 1

    print('After counting:')
    print_list(count)

    total = 0
    for x in range(k):
        old = count[x]
        count[x] = total
        total += old

    print('Starting key:')
    print_list(count)

    result = [0] * n
    for x in l:
        result[count[x]] = x
        count[x] += 1

    print('Result:')
    print_list(result)

    return result

if __name__ == '__main__':
    """Example"""

    l1 = [5, 4, 3, 2, 1, 0]
    l2 = [5, 5, 4, 3, 3, 0, 1, 1]

    counting_sort_print(l1)
    counting_sort_print(l2)
