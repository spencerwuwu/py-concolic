from symbolic.args import symbolic, concrete
@symbolic(s="abcdefg")
def validPalindrome( s):
    return validPalindromeHelper(s, 0, len(s) - 1, 1)
def validPalindromeHelper( s, left, right, budget):
    while left < len(s) and right >= 0 and left <= right and s[left] == s[right]:
        left += 1
        right -= 1
    if left >= len(s) or right < 0 or left >= right:
        return True
    if budget == 0:
        return False
    budget -= 1
    return validPalindromeHelper(s, left + 1, right, budget) or validPalindromeHelper(s, left, right - 1, budget)
