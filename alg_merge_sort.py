from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def merge_recur(x_list, y_list):
    """Merge two sorted lists by Recusions."""
    if len(x_list) == 0:
        return y_list
    if len(y_list) == 0:
        return x_list
    if x_list[0] <= y_list[0]:
        return [x_list[0]] + merge_recur(x_list[1:], y_list)
    else:
        return [y_list[0]] + merge_recur(x_list, y_list[1:])


def merge_iter(x_list, y_list):
    """Merge two sorted lists by Iteration (i.e. Two Fingers Algorithm)."""
    z_list = []
    x_pos = 0
    y_pos = 0
    for z_pos in range(len(x_list) + len(y_list)):
        if x_pos < len(x_list) and y_pos < len(y_list):
            if x_list[x_pos] <= y_list[y_pos]:
                z_list.append(x_list[x_pos])
                x_pos += 1
            else:
                z_list.append(y_list[y_pos])
                y_pos += 1      
        elif x_pos < len(x_list) and y_pos >= len(y_list):
            z_list.append(x_list[x_pos])
            x_pos += 1
        elif x_pos >= len(x_list) and y_pos < len(y_list):
            z_list.append(y_list[y_pos])
            y_pos += 1
        else:
            pass
    return z_list


def merge_sort(a_list, merge):
    """Merge sort by Divide and Conquer Algorithm.

    Time complexity: O(n*logn).
    """
    if len(a_list) == 1:
        return a_list
    else:
        mid = len(a_list) // 2
        return merge(merge_sort(a_list[:mid], merge), 
                     merge_sort(a_list[mid:], merge))


def main():
    import time

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    start_time = time.time()
    print(merge_sort(a_list, merge_recur))
    print('Run time of merge sort with recusions: {}'
          .format(time.time() - start_time))

    start_time = time.time()
    print(merge_sort(a_list, merge_iter))
    print('Run time of merge sort with iterations: {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
