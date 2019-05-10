from symbolic.args import symbolic, concrete
@symbolic(s="abcdefg")
def reverseString( s):
    """
    :type s: str
    :rtype: str
    """
    return s[::-1]
