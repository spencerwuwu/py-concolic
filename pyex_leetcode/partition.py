from symbolic.args import symbolic, concrete
@symbolic(s="abcdefg")
def partition( s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    result = []
    curr = []
    recurPartition(result, curr, s, 0)
    return result
def recurPartition( result, curr, s, start):
    if start == len(s):
        result.append(list(curr))
    for i in range(start, len(s)):
        if isPalindrome(s, start, i):
            curr.append(s[start:i + 1])
            recurPartition(result, curr, s, i + 1)
            curr.pop()
def isPalindrome( s, begin, end):
    while begin < end:
        if s[begin] != s[end]:
            return False
        begin += 1
        end -= 1
    return True
