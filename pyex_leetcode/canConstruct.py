from symbolic.args import symbolic, concrete
@symbolic(ransomNote="abcdefg")
@symbolic(magazine="abcdefg")
def canConstruct( ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    letter_map = {}
    for letter in magazine:
        letter_map[letter] = letter_map.get(letter, 0) + 1
    for letter in ransomNote:
        letter_map[letter] = letter_map.get(letter, 0) - 1
        if letter_map[letter] < 0:
            return False
    return True
