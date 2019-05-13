from symbolic.args import symbolic, concrete
@symbolic(in0="abcdefg", in1="abcdefg")
def groupAnagrams( in0, in1):
    strs = [in0, in1]
    strs.sort()
    hash = {}
    for s in strs:
        key = hash_key(s)
        try:
            hash[key].append(s)
        except KeyError:
            hash[key] = [s]
    return hash.values()
def hash_key( s):
    table = [0] * 26
    for ch in s:
        index = ord(ch) - ord('a')
        table[index] += 1
    return str(table)
