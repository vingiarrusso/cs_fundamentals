"""
leetcode 654
O(n log n)
"""


def constructMaximumBinaryTree(nums: 'List[int]') -> 'TreeNode':
    if len(nums) == 0:
      return
    
    i = nums.index(max(nums))
    root = TreeNode(nums[i])
    root.left = constructMaximumBinaryTree(nums[:i])
    root.right = constructMaximumBinaryTree(nums[i+1:])

    return root
    
