from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def selection_sort(nums):
    """Selection sort algortihm.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Start from pos=n-1,..1, select next max num to swap with its num.  
    for i in reversed(range(1, len(nums))):
        i_max = 0
        for j in range(1, i + 1):
            if nums[j] > nums[i_max]:
                i_max = j
        nums[i_max], nums[i] = nums[i], nums[i_max]


def main():
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('By selection sort: ')
    selection_sort(nums)
    print(nums)


if __name__ == '__main__':
    main()
