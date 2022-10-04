from functools import reduce


def sum_arrs(*args):
    result = []
    for i in args:
        print(i)
        result += i
        print(result)
    total = 0
    for num in result:
        total += num
    return total


def sum_arrs2(arr1, arr2):
    return sum(arr1 + arr2)


def sum_arr3(arr1, arr2):
    arr10 = arr1 + arr2
    return (lambda arr1, arr2: sum(arr1) + sum(arr2),sum(arr1) + sum(arr2))


def sum_arr4(arr1, arr2):
    arr0 = arr1 + arr2
    return reduce(lambda x, y: x + y, arr0)
