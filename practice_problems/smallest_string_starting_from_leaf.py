import string

smallest = ''
def smallestFromLeaf(root: 'TreeNode') -> 'str':
    def dfs(root, path):
      if root is not None:
	if not root.left and not root.right:
	  path_from_here = reconstructPath(path + [root.val])
	  smallest = min(smallest, path_from_here) if smallest else path_from_here
	dfs(root.left, path + [root.val])
	dfs(root.right, path + [root.val])
    
    def reconstructPath(path):
      path.reverse()
      for i, num in enumerate(path):
	path[i] = string.ascii_lowercase[num]
      return ''.join(path)
      
    dfs(root, []) 
    return smallest
