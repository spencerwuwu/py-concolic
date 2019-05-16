from symbolic.args import symbolic, concrete
@symbolic(in0="test.email+alex@leetcode.com", in1="test.e.mail+bob.cathy@leetcode.com", in2="testemail+david@lee.tcode.com")
def numUniqueEmails( in0, in1, in2):
    emails = [in0, in1, in2]
    """
    :type emails: List[str]
    :rtype: int
    """
    email_set = set()
    for email in emails:
        elements = email.split('@')
        email_set.add(elements[0].split('+')[0].replace('.', '') + elements[1])
    return len(email_set)
