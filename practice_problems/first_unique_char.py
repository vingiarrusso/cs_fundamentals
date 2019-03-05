"""
leetcode 387
"""

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    seen = {} 
    for i, ch in enumerate(s):
      if ch in seen:
	seen[ch] = -1 
      else:
	seen[ch] = i
    
    min_idx = float('inf')
    for k,v in seen.items():
      if v is not -1:
	 min_idx = min(min_idx, v)
	  
    return min_idx if min_idx != float('inf') else -1

firstUniqChar('leetcode')
