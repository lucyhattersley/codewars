from nose.tools import assert_equals

import itertools

def next_smaller(n):
    numbers = []
    
    digits = [int(x) for x in str(n)]
    possibles_as_set = set(itertools.permutations(digits))

    for i in possibles_as_set:
        numbers.append(int(''.join(str(x) for x in i)))

    possibles = [i for i in numbers if i < n]
        
    if possibles != [] and len(str(max(possibles))) == len(str(n)):
        return(max(possibles))
    else:
        return(-1)

result = next_smaller(135)
print(result)

def test_smaller_numbers():
    assert_equals(next_smaller(907), 790)
    assert_equals(next_smaller(531), 513)
    assert_equals(next_smaller(135), -1)
    assert_equals(next_smaller(2071), 2017)
    assert_equals(next_smaller(414), 144)
    assert_equals(next_smaller(123456798), 123456789)
    assert_equals(next_smaller(123456789), -1)
    assert_equals(next_smaller(1234567908), 1234567890)

"""
Step 1: remove tail. Index through number to find first instance of lower-than previous digit
# 12345679 08
1234567 98

Step 2: locate tail of head
# 9
7

THIS MAY BE WRONG! SORT VALUES (STEP 4) AND SEE IF NUMBER IS GREATER THEN SWAP LOWEST VALUE IN HEAD (STEP 3)
Step 3: is value in tail lower than head? If so swap greatest lower value in tail with head
# 8 <> 9
7 # tail remains 7

Head is now
# 12345678
1234567

Tail is now:
# 09
98

Step 4
# Sort tail numbers smallest to greatest  (0 is high)
# 90
89

Step 5
Add head and tail
#1234567890
123456789

"""