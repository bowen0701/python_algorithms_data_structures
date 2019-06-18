from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def binary_search_iter(a_list, target):
    """Binary search for ordered list by iteration.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    first = 0
    last = len(a_list) - 1
    is_found = False

    while first <= last and not is_found:
        mid = first + (last - first) // 2
        if a_list[mid] == target:
            is_found = True
        else:
            if a_list[mid] > target:
                last = mid - 1
            else:
                first = mid + 1

    return is_found


def binary_search_recur(a_list, target):
    """Binary search for ordered list by recursion.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    if len(a_list) == 0:
        return False
    else:
        mid = len(a_list) // 2
        if a_list[mid] == target:
            return True
        else:
            if a_list[mid] > target:
                return binary_search_recur(a_list[:mid], target)
            else:
                return binary_search_recur(a_list[(mid + 1):], target)


def binary_search_recur_fast(a_list, target, first, last):
    """Binary search for ordered list by recursion w/o slicing.

    Note: It performs faster than binary_search_recur().
    Time complexity: O(logn).
    Space complexity: O(1).
    """
    if first > last:
        return False

    mid = first + (last - first) // 2
    if a_list[mid] == target:
        return True
    else:
        if a_list[mid] > target:
            return binary_search_recur_fast(a_list, target, first, mid - 1)
        else:
            return binary_search_recur_fast(a_list, target, mid + 1, last)


def main():
    import time

    a_list = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93, 100]
    target = 65
    print('In sorted list {0}: search {1}'.format(a_list, target))

    # Binary search by binary_search().
    start_time = time.time()
    print('Binary search by iteration: {}'
          .format(binary_search_iter(a_list, target)))
    print('Time for binary_search_iter(): {}'
          .format(time.time() - start_time))

    # Binary search by binary_search_recur().
    start_time = time.time()
    print('Binary search by recursion: {}'
          .format(binary_search_recur(a_list, target)))
    print('Time for binary_search_recur(): {}'
          .format(time.time() - start_time))

    # Binary search by binary_search_recur_fast().
    start_time = time.time()
    print('Binary search by fast recursion: {}'.format(
            binary_search_recur_fast(a_list, target, 0, len(a_list) - 1)))
    print('Time for binary_search_recur_fast(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
