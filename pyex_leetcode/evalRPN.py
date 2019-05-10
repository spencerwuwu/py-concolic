from symbolic.args import symbolic, concrete
@symbolic(in0="abcdefg")
@symbolic(in1="abcdefg")
def evalRPN( in0, in1):
    tokens = [in0, in1]
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for t in tokens:
        try:
            temp = int(t)
            stack.append(temp)
        except:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                a += b
            elif t == "-":
                a -= b
            elif t == "*":
                a *= b
            else:
                a = int(a * 1.0 / b)
            stack.append(a)
    return stack[-1]
