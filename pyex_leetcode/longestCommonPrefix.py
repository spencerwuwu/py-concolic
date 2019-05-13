from symbolic.args import symbolic, concrete
@symbolic(in0="abcdefg", in1="abcdefg")
def longestCommonPrefix( in0, in1):
    strs = [in0, in1]
    ls = len(strs)
    if ls == 1:
        return strs[0]
    prefix = ''
    pos = 0
    while True:
        try:
            current = strs[0][pos]
        except IndexError:
            break
        index = 1
        while index < ls:
            try:
                if strs[index][pos] != current:
                    break
            except IndexError:
                break
            index += 1
        if index == ls:
            prefix = prefix + current
        else:
            break
        pos += 1
    return prefix
