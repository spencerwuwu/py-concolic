from symbolic.args import symbolic, concrete
@symbolic(digits="abcdefg")
def letterCombinations( digits):
    result = []
    ls = len(digits)
    if ls == 0:
        return result
    current = digits[0]
    posfix = letterCombinations(digits[1:])
    for t in dmap[current]:
        if len(posfix) > 0:
            for p in posfix:
                temp = t + p
                result.append(temp)
        else:
            result.append(t)
    return result
