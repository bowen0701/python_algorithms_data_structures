from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def quick_sort(a_list):
    """Quick sort algortihm with list comprehension recursion."""
    if len(a_list) <= 1:
        return a_list
    pivot_value = a_list[len(a_list) // 2]
    left_list = [x for x in a_list if x < pivot_value]
    middle_list = [x for x in a_list if x == pivot_value]
    right_list = [x for x in a_list if x > pivot_value]
    return quick_sort(left_list) + middle_list + quick_sort(right_list)


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('Quick sort with list comprehension: ')
    print(quick_sort(a_list))


if __name__ == '__main__':
    main()
