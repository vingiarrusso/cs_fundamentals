"""
leetcode 108
"""

def convert_sorted_array_to_bst(nums):
    if not len(nums):
        return None 

    half = len(nums) // 2
    root = TreeNode(nums[half])
    root.left = convert_sorted_array_to_bst(nums[:half])
    root.right = convert_sorted_array_to_bst(nums[half+1:])

    return root
