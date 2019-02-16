"""
leetcode 100
"""

def is_same_tree(t1, t2):
    if t1 and t2:
        if t1.val == t2.val:
            left = is_same_tree(t1.left, t2.left)
            if not left:
                return False
            return is_same_tree(t1.right, t2.right)
        else:
            return False
    if (t1 and not t2) or (t2 and not t1):
        return False
    
    return True
