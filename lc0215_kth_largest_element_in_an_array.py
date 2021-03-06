"""Leetcode 215. Kth Largest Element in an Array
Medium

URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 <= k <= array's length.
"""

class SolutionSelectionSort(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(nk).
        Space complexity: O(1).
        """
        n = len(nums)

        # Selection sort from behind: swith max element & last one, and so on.
        for i in range(n - 1, n - k - 1, -1):
            max_i = 0
            for j in range(1, i + 1):
                if nums[max_i] < nums[j]:
                    max_i = j
            nums[max_i], nums[i] = nums[i], nums[max_i]

        return nums[-k]


class SolutionQuickSort(object):
    def _quicksort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]

        small_nums = [x for x in nums if x < pivot]
        mid_nums = [x for x in nums if x == pivot]
        large_nums = [x for x in nums if x > pivot]

        return (self._quicksort(small_nums) +
                mid_nums +
                self._quicksort(large_nums))

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n*logn), where n is the length of nums.
        Space complexity: O(n).
        """
        # Apply quick sort and get the element directly.
        sorted_nums = self._quicksort(nums)
        return sorted_nums[-k]


class SolutionSort(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n*logn), where n is the length of nums.
        Space complexity: O(n).
        """
        nums.sort()
        return nums[-k]


class SolutionMinHeap(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n*logk).
        Space complexity: O(k).
        """
        import heapq

        minheap = []

        for num in nums:
            heapq.heappush(minheap, num)

            # Maintain heap size = k.
            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0]


class SolutionSelection(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Select w/o consider the relative order of other elements.
        pivot = nums[len(nums) // 2]

        small_nums = [x for x in nums if x < pivot]
        mid_nums = [x for x in nums if x == pivot]
        large_nums = [x for x in nums if x > pivot]

        n_larges = len(large_nums)
        n_mids = len(mid_nums)

        if k <= n_larges:
            return self.findKthLargest(large_nums, k)
        elif n_larges < k <= n_mids + n_larges:
            return pivot
        elif k > n_mids + n_larges:
            return self.findKthLargest(small_nums, k - n_larges - n_mids)


def main():
    import random
    import time

    # Input: [3,2,1,5,6,4] and k = 2
    # Output: 5
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    start_time = time.time()
    print 'Selection sort:', SolutionSelectionSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Quick sort:', SolutionQuickSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Sort:', SolutionSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'MinHeap: ', SolutionMinHeap().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Selection: ', SolutionSelection().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    # Input: [3,2,3,1,2,4,5,5,6] and k = 4
    # Output: 4
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 5

    start_time = time.time()
    print 'Selection sort:', SolutionSelectionSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Quick sort:', SolutionQuickSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Sort:', SolutionSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'MinHeap: ', SolutionMinHeap().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Selection: ', SolutionSelection().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    # Input: shuffle([0~999]) and k = 5
    # Output: 995
    nums = list(range(1000))
    random.shuffle(nums)
    k = 5

    start_time = time.time()
    print 'Selection sort:', SolutionSelectionSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Quick sort:', SolutionQuickSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Sort:', SolutionSort().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'MinHeap: ', SolutionMinHeap().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'Selection: ', SolutionSelection().findKthLargest(nums, k)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
