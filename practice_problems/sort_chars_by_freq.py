"""
leetcode 451
"""

from collections import Counter
from heapq import heapify, heappop

def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    c = Counter(s)
    st = []
    
    max_heap = [(-v, k) for k,v in c.items()]
    heapify(max_heap) 
    
    while max_heap:
      v, k = heappop(max_heap)
      st.append(k * -v)
    
    return ''.join(st)
