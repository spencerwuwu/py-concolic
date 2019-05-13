from symbolic.args import symbolic, concrete
@symbolic(in0="abcdefg", in1="abcdefg")
def uniqueMorseRepresentations( in0, in1):
    words = [in0, in1]
    """
    :type words: List[str]
    :rtype: int
    """
    if len(words) == 0:
        return 0
    ans_set = set()
    for word in words:
        morsed = ""
        for c in word:
            morsed += Morse_tab[ord(c) - ord('a')]
        
        ans_set.add(morsed)
    return len(ans_set)
