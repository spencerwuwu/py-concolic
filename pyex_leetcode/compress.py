from symbolic.args import symbolic, concrete
@symbolic(in0="abcdefg", in1="abcdefg")
def compress( in0, in1):
    chars = [in0, in1]
    """
    :type chars: List[str]
    :rtype: int
    """
    anchor = write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    return write
