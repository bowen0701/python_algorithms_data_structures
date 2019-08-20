"""Leetcode 79. Word Search
Medium

URL: https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution(object):
    def _dfs(self, i, j, board, word, pos, visited):
        # If there are no letters, return True.
        if pos == len(word):
            return True

        # If visit is out of boundaries, 
        # (i, j) is not the 1st letter of word,
        # or (i, j) was visited.
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or 
            board[i][j] != word[pos] or
            visited.get((i, j))):
            return False

        # Mark (i, j) as visited.
        visited[(i, j)] = True

        # Start DFS visiting, one of DFSs is true, then return True.
        result = (self._dfs(i - 1, j, board, word, pos + 1, visited) or
                  self._dfs(i + 1, j, board, word, pos + 1, visited) or
                  self._dfs(i, j - 1, board, word, pos + 1, visited) or
                  self._dfs(i, j + 1, board, word, pos + 1, visited))

        # Backtrack.
        visited[(i, j)] = False

        return result

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        Time complexity: O(m * n * 4^s), where
          - m is the number of rows,
          - n is the number of cols,
          - s is the length of word.
        Space complexity: O(m * n).
        """
        if not board:
            return False

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                visited = {}
                if self._dfs(i, j, board, word, 0, visited):
                    return True

        return False


def main():
    board = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]

    # Given word = "ABCCED", return true.
    word = 'ABCCED'
    print Solution().exist(board, word)

    # Given word = "SEE", return true.
    word = 'SEE'
    print Solution().exist(board, word)

    # Given word = "ABCB", return false.
    word = 'ABCB'
    print Solution().exist(board, word)

    # Given word = "ABCESEEEFS", return true.
    board = [
              ["A","B","C","E"],
              ["S","F","E","S"],
              ["A","D","E","E"]
            ]
    word = "ABCESEEEFS"
    print Solution().exist(board, word)


if __name__ == '__main__':
    main()