"""Leetcode 256. Paint House (Premium)
Easy

URL: https://leetcode.com/problems/paint-house

There are a row of n houses, each house can be painted with one of the three colors:
red, blue or green. The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost
matrix. For example, costs[0][0] is the cost of painting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green, and so on.
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:
Input: [[17,2,17],
        [16,16,5],
        [14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
"""

class SolutionMinTheOtherTwoDp(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not costs:
            return 0

        n_houses = len(costs)

        # Start from house 1 to accumulate costs of the other two houses.
        for i in range(1, n_houses):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[-1])


def main():
    # Output: 10
    costs = [[17,2,17],
             [16,16,5],
             [14,3,19]]
    print SolutionMinTheOtherTwoDp().minCost(costs)


if __name__ == '__main__':
    main()
