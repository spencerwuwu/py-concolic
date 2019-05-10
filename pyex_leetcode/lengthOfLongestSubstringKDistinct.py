from symbolic.args import symbolic, concrete
@symbolic(s="abcdefg")
def lengthOfLongestSubstringKDistinct( s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    count = [0] * 256
    i, numDistinct, maxLen = 0, 0, 0
    for j in range(len(s)):
        if count[ord(s[j])] == 0:
            numDistinct += 1
        count[ord(s[j])] += 1
        while numDistinct > k:
            count[ord(s[i])] -= 1
            if count[ord(s[i])] == 0:
                numDistinct -= 1
            i += 1
        maxLen =  max(j - i + 1, maxLen)
    return maxLen
