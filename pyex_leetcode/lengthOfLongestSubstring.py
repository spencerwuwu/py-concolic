from symbolic.args import symbolic, concrete
@symbolic(s="abcdefg")
def lengthOfLongestSubstring( s):
    charMap = {}
    for i in range(256):
        charMap[i] = -1
    ls = len(s)
    i = max_len = 0
    for j in range(ls):
        if charMap[ord(s[j])] >= i:
            i = charMap[ord(s[j])] + 1
        charMap[ord(s[j])] = j
        max_len = max(max_len, j - i + 1)
    return max_len
