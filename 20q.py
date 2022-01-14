# A -> 0
# Z -> 25
# B.Z = 1 + 25/26
# 2 questions -> 2 answers
# 3 questions -> 4 answers
# 4 questions -> 8 answers
# 26**x == 4**(n-1)
# xlog26 = 19log4

import string

num_frac_bits = 64

scale_factor = 2**num_frac_bits
min_val = 0
max_val = 2**num_frac_bits-1

num_chars = 255

def to_letters(fval):
    letters = []
    while fval is not 0:
        letters.append(string.ascii_uppercase[fval%26])
        fval //= 26
    if len(letters) < num_chars:
        letters += ['A']*(num_chars-len(letters))
    return ''.join(letters)[::-1]

def from_letters(str):
    val = 0
    for i in range(len(str)):
        val += (ord(str[i])-ord('A'))*26**i
    return val

lb = min_val
ub = from_letters('Z'*num_chars)

target = 'THISISADEMONSTRATIONOFATEXTSERIALIZERBASEDONTHECONCEPTOFBINARYSEARCH'

res = []

while True:
    mid = (ub+lb)//2
    midstr = to_letters(mid)
    print(midstr)
    if midstr[:len(target)] == target:
        break
    #choice = input('<? ')
    if midstr[:len(target)] > target:
        res += [0]
        ub = mid
    else:
        res += [1]
        lb = mid
print('Message len (chars): ', len(target))
print('l: ', len(res))
print('L: ', 8*len(target))
print('r: ', (len(res)-8*len(target))/(8*len(target))*100)
print(''.join(str(i) for i in res))
