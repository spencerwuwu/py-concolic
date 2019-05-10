from symbolic.args import symbolic, concrete
@symbolic(in0="abcdefg")
@symbolic(in1="abcdefg")
def numUniqueEmails( in0, in1):
    emails = [in0, in1]
    """
    :type emails: List[str]
    :rtype: int
    """
    email_set = set()
    for email in emails:
        elements = email.split('@')
        email_set.add(elements[0].split('+')[0].replace('.', '') + elements[1])
    return len(email_set)
