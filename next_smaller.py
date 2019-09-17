from nose.tools import assert_equals

import itertools

def next_smaller(n):
    n_list = [int(x) for x in str(n)]
    print(n_list[::-1])

# def next_smaller(n):
#     numbers = []
    
#     digits = [int(x) for x in str(n)]
#     possibles_as_set = set(itertools.permutations(digits))

#     for i in possibles_as_set:
#         numbers.append(int(''.join(str(x) for x in i)))

#     possibles = [i for i in numbers if i < n]
        
#     if possibles != [] and len(str(max(possibles))) == len(str(n)):
#         return(max(possibles))
#     else:
#         return(-1)

result = next_smaller(907)
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
Start from the last digit to the first as long as the digits are decreasing or equal. 12[5]+increasing 3479, 5 > 3.
From the increasing tail pick the element just smaller (4), and reverse the tail. 12(4)+decreasing 97[5]3.

"""