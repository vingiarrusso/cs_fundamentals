"""
leetcode 107
"""
def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
  def helper(roots, levels):
    if not roots:
      return
    this_level = []
    next_level = []
    for root in roots:
      if root:
	this_level.append(root.val)
	next_level.append(root.left)
	next_level.append(root.right)
    
    if len(this_level):
      levels.append(this_level)
    helper(next_level, levels)
  
  levels = []
  helper([root], levels)
  return levels[::-1]

