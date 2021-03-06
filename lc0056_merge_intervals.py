"""Leetcode 56. Merge Intervals
Medium

URL: https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class SolutionBruteForce(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        Time complexity: O(n^2).
        Space complexity: O(1).
        """
        if not intervals:
            return []

        # Sort by interval's start.
        intervals = sorted(intervals)

        # Iterate through intervals to merge them into result.
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            is_merged = False

            for j in range(len(result)):
                if (result[j][0] <= intervals[i][0] <= result[j][1] and 
                    intervals[i][1] > result[j][1]):
                    # interval i's left is in result j, but its right is not.
                    result[j][1] = intervals[i][1]
                    is_merged = True
                    break
                elif (intervals[i][0] < result[j][0] and
                      result[j][0] <= intervals[i][1] <= result[j][1]):
                    # interval i's right is in result j, but its left is not.
                    result[j][0] = intervals[i][0]
                    is_merged = True
                    break
                elif (result[j][0] <= intervals[i][0] <= result[j][1] and
                      result[j][0] <= intervals[i][1] <= result[j][1]):
                    # interval i is in result i.
                    is_merged = True
                    break
                elif (intervals[i][0] < result[j][0] and
                      intervals[i][1] > result[j][1]):
                    # interval i contains result j.
                    result[j] = intervals[i]
                    is_merged = True
                    break

            # If interval is not merged, append to result.
            if not is_merged:
                result.append(intervals[i])

        return result


class SolutionAppendIntervalOrUpdateEnd(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        Time complexity: O(n*logn).
        Space complexity: O(1).
        """
        if not intervals:
            return []

        # Sort by interval's start.
        intervals = sorted(intervals)

        # Iterate through intervals to append them or update end. 
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > result[-1][1]:
                # If interval i is not overlapped with last result, append it.
                result.append(intervals[i])
            else:
                # If overlapped, update result's end.
                result[-1][1] = max(intervals[i][1], result[-1][1])

        return result


def main():
    import time

    print 'By brute force:'
    start_time = time.time()

    # Ans: [[1,6],[8,10],[15,18]]
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    print SolutionBruteForce().merge(intervals)

    # Ans: [[1,5]]
    intervals = [[1,4], [4,5]]
    print SolutionBruteForce().merge(intervals)

    # Ans: [[0,4]]
    intervals = [[1,4], [0,4]]
    print SolutionBruteForce().merge(intervals)

    # Ans: [[0,5]]
    intervals = [[1,4], [0,5]]
    print SolutionBruteForce().merge(intervals)

    # Ans: [[1,10]]
    intervals = [[2,3], [4,5], [6,7], [8,9], [1,10]]
    print SolutionBruteForce().merge(intervals)

    print 'Time: {}'.format(time.time() - start_time)

    print 'By appending interval or updating end:'
    start_time = time.time()

    # Ans: [[1,6],[8,10],[15,18]]
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    print SolutionAppendIntervalOrUpdateEnd().merge(intervals)

    # Ans: [[1,5]]
    intervals = [[1,4], [4,5]]
    print SolutionAppendIntervalOrUpdateEnd().merge(intervals)

    # Ans: [[0,4]]
    intervals = [[1,4], [0,4]]
    print SolutionAppendIntervalOrUpdateEnd().merge(intervals)

    # Ans: [[0,5]]
    intervals = [[1,4], [0,5]]
    print SolutionAppendIntervalOrUpdateEnd().merge(intervals)

    # Ans: [[1,10]]
    intervals = [[2,3], [4,5], [6,7], [8,9], [1,10]]
    print SolutionAppendIntervalOrUpdateEnd().merge(intervals)

    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
