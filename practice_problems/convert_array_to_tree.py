class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def convertArrayToTree(lst):
    lst_len = len(lst)
    def helper(lst, node_index):
        node = TreeNode(lst[node_index])
        l_index = node_index * 2 + 1
        r_index = l_index + 1

        if l_index <= lst_len - 1:
            node.left = helper(lst, l_index)

        if r_index <= lst_len - 1:
            node.right = helper(lst, r_index)

        return node

    return helper(lst, 0)

convertArrayToTree([7,5,6,3,1,9])
