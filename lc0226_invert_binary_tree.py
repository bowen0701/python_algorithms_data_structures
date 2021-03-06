"""Leetcode 226. Invert Binary Tree
Easy

URL: https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply postorder traversal to invert tree.
        if not root:
            return None

        # Recursively invert left subtree and right subtree.
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Invert tree by interchanging left and right trees.
        root.left = right
        root.right = left
        return root


class SolutionBFS(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        from collections import deque

        if not root:
            return root

        # Apply BFS w/ queue to iteratively visit and invert tree.
        queue = deque([root])

        while queue:
            # Invert tree by swapping current's left and right subtrees.
            current = queue.pop()
            current.left, current.right = current.right, current.left
 
            # Insert left/right child into queue if exists.
            if current.left:
                queue.appendleft(current.left)
            if current.right:
                queue.appendleft(current.right)

        return root


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # root = SolutionRecur().invertTree(root)
    root = SolutionBFS().invertTree(root)
    print root.val              # Should be 4.
    print root.left.val         # Should be 7.
    print root.right.val        # Should be 2.
    print root.left.left.val    # Should be 9.
    print root.left.right.val   # Should be 6.
    print root.right.left.val   # Should be 3.
    print root.right.right.val  # Should be 1.


if __name__ == '__main__':
    main()

