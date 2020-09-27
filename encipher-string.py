"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""
    new_txt = ''
    min_cap = ord('A')
    max_cap = ord('Z')
    min_lower = ord('a')
    max_lower = ord('z')

    # handle out of bounds chars
    for item in txt:
        if item.isupper():
            if ord(item) + shift > max_cap:
                new_txt += chr(ord(item) + shift - 26)
            else:
                new_txt += chr(ord(item) + shift)
        elif item.islower():
            if ord(item) + shift > max_lower:
                new_txt += chr(ord(item) + shift - 26)
            else:
                new_txt += chr(ord(item) + shift)
        elif item.isalpha() == False:
            new_txt += item
    return new_txt


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
