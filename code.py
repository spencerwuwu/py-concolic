
s = "IV"
num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'E':0 }

for val in s:
    if val not in num:
        print(-1)
        exit

L = len(s)
s = s + "E"
sum = 0

for i in range (0,L):
    if num[s[i]] >= num[s[i+1]]:
        sum = sum + num[s[i]]
    else:
        sum = sum - num[s[i]]

print(sum)
