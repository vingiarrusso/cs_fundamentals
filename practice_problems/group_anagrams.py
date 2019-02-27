"""
leetcode 49
"""

from collections import defaultdict

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    sorted_strs = defaultdict(list)

    for s in strs:
      sorted_strs[''.join(sorted(s))].append(s)

    return list(sorted_strs.values())

groupAnagrams(["eat","tea","tan","ate","nat","bat"]) #[["tan","nat"],["bat"],["eat","tea","ate"]]
