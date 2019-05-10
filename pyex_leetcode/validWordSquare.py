from symbolic.args import symbolic, concrete
@symbolic(in0="abcdefg")
@symbolic(in1="abcdefg")
def validWordSquare( in0, in1):
    words = [in0, in1]
    """
    :type words: List[str]
    :rtype: bool
    """
    if words is None or len(words) == 0:
        return True
    ls = len(words)
    for i in range(ls):
        for j in range(1, len(words[i])):
            if j >= ls:
                return False
            if i >= len(words[j]):
                return False
            if words[i][j] != words[j][i]:
                return False
    return True
