from symbolic.args import symbolic, concrete
@symbolic(secret="abcdefg")
@symbolic(guess="abcdefg")
def getHint( secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    check = {}
    ls = len(secret)
    bull, cow = 0, 0
    different = []
    for i in range(ls):
        if guess[i] == secret[i]:
            bull += 1
        else:
            different.append(i)
            try:
                check[secret[i]] += 1
            except KeyError:
                check[secret[i]] = 1
    for i in different:
        try:
            if check[guess[i]] > 0:
                cow += 1
                check[guess[i]] -= 1
        except:
            pass
    return "%dA%dB" % (bull, cow)
