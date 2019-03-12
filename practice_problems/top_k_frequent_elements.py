"""
leetcode 347
"""

from collections import Counter

def topKFrequent(nums, k):
    return [item[0] for item in Counter(nums).most_common(k)]
