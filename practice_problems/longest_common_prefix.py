import pudb
pu.db

def longestCommonPrefix(strs):
    prefix = []
    if not strs:
      return ''

    minLen = float('inf')
    for word in strs:
      if len(word) < minLen:
        minLen = len(word)

    for i in range(minLen):
      current = strs[0][i]
      for j in range(1, len(strs)):
        if current != strs[j][i]:
          return ''.join(prefix)
          
      prefix.append(current)
    return ''.join(prefix)

# a cool way using zip
def longestCommonPrefixZ(strs):
    prefix = []
    if not strs:
        return ''

    for letters in zip(*strs):
        if len(set(letters)) > 1:
            return ''.join(prefix)

        prefix.append(letters[0])

longestCommonPrefixZ(['corgi', 'corgin', 'corgbutt'])
