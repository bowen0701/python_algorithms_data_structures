"""Leetcode 39. Combination Sum
Medium

URL: https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a
target number (target), find all unique combinations in candidates where
the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def _backtrack(self, result, temps, target, start, candidates):
        if target < 0:
            return None

        if target == 0:
            result.append(temps[:])
            return None

        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                temps.append(candidates[i])
                self._backtrack(result, temps, target - candidates[i], i, candidates)
                temps.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self._backtrack(result, [], target, 0, candidates)
        return result


def main():
    candidates = [2,3,6,7]
    target = 7
    print Solution().combinationSum(candidates, target)

    candidates = [2,3,5]
    target = 8
    print Solution().combinationSum(candidates, target)


if __name__ == '__main__':
    main()
