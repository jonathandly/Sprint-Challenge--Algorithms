'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

txt = 'th'

def count_th(word):
    
    # TBC
    if len(word) <= 1:
        return 0
    # Check first two chars in string
    elif word[:2] == txt:
        return 1 + count_th(word[2:])
    # Check remaining chars incrementing start position by 1
    else:
        return count_th(word[1:])

print(count_th('')) # count == 0
print(count_th('th')) # count == 1
print(count_th('ghhTHthkathl')) # count == 2
print(count_th('ThthwoeEthtlheionth')) # count == 3
print(count_th('thththhhhttttht')) # count == 4