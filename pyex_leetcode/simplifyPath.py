from symbolic.args import symbolic, concrete
@symbolic(path="abcdefg")
def simplifyPath( path):
    """
    :type path: str
    :rtype: str
    """
    result = []
    plist = path.split('/')
    for pos in plist:
        if pos:
            if pos == '..':
                try:
                    result.pop()
                except:
                    result = []
            elif pos != '.':
                result.append(pos)
    return '/'+'/'.join(result)
