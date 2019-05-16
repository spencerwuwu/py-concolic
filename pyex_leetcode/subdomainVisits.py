from symbolic.args import symbolic, concrete
@symbolic(in0="9001 discuss.leetcode.com", in1="9001 leetcode.com", in2="9001 com")
def subdomainVisits( in0, in1, in2):
    cpdomains = [in0, in1, in2]
    """
    :type cpdomains: List[str]
    :rtype: List[str]
    """
    domain_count = {}
    for cpdomain in cpdomains:
        count, domain = cpdomain.split(' ')
        sub_domain = domain.split('.')
        for i in range(len(sub_domain)):
            curr = '.'.join(sub_domain[i:])
            domain_count[curr] = domain_count.get(curr, 0) + int(count)
    return [str(v) + ' ' + k for k, v in domain_count.items()]
