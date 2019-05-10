from symbolic.args import symbolic, concrete
@symbolic(s1="abcdefg")
@symbolic(s2="abcdefg")
def isScramble( s1, s2, memo={}):
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False
    if len(s1) <= len(s2) <= 1:
        return s1 == s2
    if s1 == s2:
        return True
    if (s1, s2) in memo:
        return memo[s1, s2]
    n = len(s1)
    for i in range(1, n):
        a = isScramble(s1[:i], s2[:i], memo) and isScramble(s1[i:], s2[i:], memo)
        if not a:
            b = isScramble(s1[:i], s2[-i:], memo) and isScramble(s1[i:], s2[:-i], memo)
        if a or b:
            memo[s1, s2] = True
            return True
    memo[s1, s2] = False
    return False
