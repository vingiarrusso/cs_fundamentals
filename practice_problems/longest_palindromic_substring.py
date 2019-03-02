"""
leetcode 5
"""
def longestPalindromicSubstring(s):
    isPalindrome = [[False] * len(s) for i in range(len(s))] 
    
    for i in range(len(s)):
        isPalindrome[i][i] = True
    
    start = 0
    end = 0

    for i in range(1, len(s)):
        for j in range(i):
            
            thisRangeIsPalindrome = s[i] == s[j] and (isPalindrome[j+1][i-1] or i - j == 1)

            if thisRangeIsPalindrome:
                isPalindrome[j][i] = True
                
                if i - j > end - start:
                    start = j
                    end = i
    
    return s[start:end + 1]

longestPalindromicSubstring('hahahaaaa')
