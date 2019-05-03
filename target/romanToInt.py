#from symbolic.args import symbolic, concrete

class TheClass:
    def __init__(self, value:str):
        self.value = value

    def __str__(self):
        return self.value


def romanToInt(s:str) -> int:
    num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'E':0 }

    test_class = TheClass(s)
    for val in s:
        if val not in num:
            return -1

    L = len(s)
    s = s + "E"
    sum = 0

    for i in range (0,L):
        if num[s[i]] >= num[s[i+1]]:
            sum = sum + num[s[i]]
        else:
            sum = sum - num[s[i]]

    return sum
