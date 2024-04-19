"""Module to test fileio.py
"""

import fileio


def test_sort_ascending1():
    my_nums = [10, 9, 0. - 6]
    fileio.sortListInAscendingOrder(my_nums)
    assert (my_nums == [-6, 0, 9, 10])

# add 3 more test cases in separate test functions
def test_sort_ascending2():
    my_nums = [1,6,4,7,2]
    fileio.sortListInAscendingOrder(my_nums)
    assert (my_nums == [1,2,4,6,7])

def test_sort_ascending3():
    my_nums = [1,-6,4,7,20]
    fileio.sortListInAscendingOrder(my_nums)
    assert (my_nums == [-6,1,4,7,20])

def test_sort_descending1():
    my_nums = [0, -10, -1, 5, 100]
    fileio.sortListInDescendingOrder(my_nums)
    my_nums == [100, 5, 0, -1, -10]

def test_sort_descending2():
    my_nums = [20, -9, -1, 5, 100]
    fileio.sortListInDescendingOrder(my_nums)
    my_nums == [100, 20, 5, -1, -9]


