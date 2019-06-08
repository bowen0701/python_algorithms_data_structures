"""Leetcode 238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1, return an array output 
such that output[i] is equal to the product of all the elements of nums 
except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of 
space complexity analysis.)
"""

class SolutionLeftRight(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        size = len(nums)

        left_prods = [1] * size
        left_prods[0] = nums[0]
        for i in range(1, size):
            left_prods[i] = left_prods[i - 1] * nums[i]

        right_prods = [1] * size
        right_prods[size - 1] = nums[size - 1]
        for i in range(size - 2, -1, -1):
            right_prods[i] = right_prods[i + 1] * nums[i]

        prods = [1] * size
        for i, n in enumerate(nums):
            if i - 1 < 0:
                prods[i] = right_prods[i + 1]
            elif i + 1 >= size:
                prods[i] = left_prods[i - 1]
            if i - 1 >= 0 and i + 1 < size:
                prods[i] = left_prods[i - 1] * right_prods[i + 1]

        return prods


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)

        


def main():
    # Input:  [2, 3, 4, 5]
    # Output: [60, 40, 30, 24]
    nums = [2, 3, 4, 5]

    print SolutionLeftRight().productExceptSelf(nums)


if __name__ == '__main__':
    main()
