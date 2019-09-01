from nose.tools import assert_equals

def next_smaller(n):
    return int("".join(sorted(str(n))))

def test_smaller_numbers():
    assert_equals(next_smaller(907), 790)

def test_further_numbers():
    assert_equals(next_smaller(531), 513)
    assert_equals(next_smaller(135), -1)
    assert_equals(next_smaller(2071), 2017)
    assert_equals(next_smaller(414), 144)
    assert_equals(next_smaller(123456798), 123456789)
    assert_equals(next_smaller(123456789), -1)
    assert_equals(next_smaller(1234567908), 1234567890)