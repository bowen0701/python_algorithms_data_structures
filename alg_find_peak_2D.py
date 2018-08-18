from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

"""Find a peak in 2D array.

Support a is an array of length (m, n).
If a is an array of length (1, 1), a[0][0] is a peak.
In general, a[i][j] is a peak iff 
  a[i][j] >= a[i][j - 1] and a[i][j] >= a[i][j + 1] and
  a[i][j] >= a[i + 1][j] and a[i][j] >= a[i - 1][j] 
Similarly for corner cases, a[i][j], i = 0 or m - 1, or j = 0 or n -1.
"""

def find_peak_naive(arr):
    """Find peak by naive algorithm.

    Time complexity: O(nm).
    """
    nrow, ncol = len(arr), len(arr[0])

    for (i, j) in itertools.product(range(nrow), range(ncol)):
        if (i, j) == (0, 0):
            # Upper left.
            if (arr[i][j] >= arr[i][j + 1] and 
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        elif (i, j) == (0, ncol - 1):
            # Upper right.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        elif (i, j) == (nrow - 1, 0):
            # Lower left.
            if (arr[i][j] >= arr[i][j + 1] and 
                arr[i][j] >= arr[i - 1][j]):
                return arr[i][j]
        elif (i, j) == (nrow - 1, ncol - 1):
            # Lower right.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i - 1][j]):
                return arr[i][j]
        elif i == 0 and 0 < j < ncol - 1:
            # On the 0th row.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i][j + 1] and
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        elif i == nrow - 1 and 0 < j < ncol - 1:
            # On the last row.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i][j + 1] and
                arr[i][j] >= arr[i - 1][j]):
                return arr[i][j]
        elif 0 < i < nrow - 1 and j == 0:
            # On the 0th col.
            if (arr[i][j] >= arr[i][j + 1] and
                arr[i][j] >= arr[i - 1][j] and
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        elif 0 < i < nrow - 1 and j == ncol - 1:
            # On the last col.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i - 1][j] and
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        else:
            # Other center entries.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i][j + 1] and
                arr[i][j] >= arr[i - 1][j] and
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]


def find_peak(arr):
    pass


def main():
    import time

    # 2D array with peak 21.
    arr = [[10, 8, 10, 10, 7], 
           [14, 13, 12, 11, 9], 
           [15, 9, 11, 21, 22], 
           [16, 17, 19, 20, 18]]

    time_start = time.time()
    peak = find_peak_naive(arr)
    time_run = time.time() - time_start
    print('Peak: {}'.format(peak))
    print('Time for naive alg: {}'.format(time_run))


if __name__ == '__main__':
    main()
