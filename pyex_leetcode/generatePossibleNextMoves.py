from symbolic.args import symbolic, concrete
@symbolic(s="abcdefg")
def generatePossibleNextMoves( s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = []
    if s is None or len(s) == 0:
        return res
    ls = len(s)
    for i in range(ls - 1):
        if s[i] == '+' and s[i + 1] == '+':
            res.append(s[:i] + '--' + s[i + 2:])
    return res
