from symbolic.args import symbolic, concrete
@symbolic(paragraph="abcdefg")
@symbolic(in0="abcdefg")
@symbolic(in1="abcdefg")
def mostCommonWord( paragraph, in0, in1):
    banned = [in0, in1]
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    banned = set(banned)
    count = collections.Counter(word for word in re.split('[ !?\',;.]',
                                paragraph.lower()) if word)
    return max((item for item in count.items() if item[0] not in banned),
               key=operator.itemgetter(1))[0]
