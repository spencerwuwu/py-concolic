from symbolic.args import symbolic, concrete
@symbolic(in0="gin", in1="zen", in2="gig", in3="msg")
def uniqueMorseRepresentations( in0, in1, in2, in3):
    Morse_tab = [".-","-...","-.-.",
                 "-..",".","..-.","--.","....",
                 "..",".---","-.-",".-..","--",
                 "-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--",
                 "-..-","-.--","--.."]
    words = [in0, in1, in2, in3]
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
