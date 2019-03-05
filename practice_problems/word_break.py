"""
leetcode 139
"""

# dp is an array where index value is true or false if the word starting from the previous True (the last dict word)
# until that index is in the dict.  ex: 'leet' => [T, F, F, F, T]

def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
    return dp[-1]            

wordBreak('leetcode', ['leet', 'code'])

