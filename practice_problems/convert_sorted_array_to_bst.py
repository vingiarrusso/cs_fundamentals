"""
leetcode 108
"""

def convert_sorted_array_to_bst(nums):
    def make_tree(nums, root=None):
        if not len(nums):
            return root

        half = len(nums) // 2
        root = TreeNode(nums[half])
        root.left = make_tree(nums[:half])
        root.right = make_tree(nums[half+1:])
        return root

    return make_tree(nums)
