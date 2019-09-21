from nose.tools import assert_equals

def next_smaller(n):
    digits = [int(x) for x in str(n)]
    i = 0

    if all(digits[i] <= digits[i+1] for i in range(len(digits)-1)):
        return -1

    while digits[-1^i] > digits[-1^i+1]:
        i = i + 1

    head = digits[:i]
    tail = digits[i:]

    for i in range(len(tail)):
        if tail[i] < head[-1]:
            try:
                if tail[i] > tail[current_largest]:
                    current_largest = i
            except:
                current_largest = i

    temp = head[-1]
    head[-1] = tail[current_largest]
    tail[current_largest] = temp

    if head[0] == 0:
        return -1
    else:
        result = head + tail[::-1]
        return int(''.join(map(str,result)))


def test_stackexchange():
    assert_equals(next_smaller(1253479), 1249753)

def test_907():
    assert_equals(next_smaller(907), 790)


def test_531():
    assert_equals(next_smaller(531), 513)

def test_135():
    assert_equals(next_smaller(135), -1)

def test_2071():
    assert_equals(next_smaller(2071), 2017)

def test_414():
    assert_equals(next_smaller(414), 144)

def test_123456798():
    assert_equals(next_smaller(123456798), 123456789)

def test_123456789():
    assert_equals(next_smaller(123456789), -1)

def test_1234567908():
    assert_equals(next_smaller(1234567908), 1234567890)

"""
Start from the last digit to the first as long as the digits are decreasing or equal. 12[5]+increasing 3479, 5 > 3.
From the increasing tail pick the element just smaller (4), and reverse the tail. 12(4)+decreasing 97[5]3.

"""