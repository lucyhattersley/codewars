from nose.tools import assert_equals

def snail(array):
    
    # pop first list from array to return_list
    if array:
        return_list = array.pop(0)

        # pop end list from array in holding
    if array:
        holding = array.pop()
        holding.reverse()

        # walk array forward and pop last element of each list to return_list
    if array:
        for l in array:
            return_list.append(l.pop())

    if array:
        # reverse holding and add to return_list
        return_list = return_list + holding
        # walk array backward and pop first element of each to return list
        for l in array:
            return_list.append(l.pop(0))
       
    else:
        return return_list 

array = [[1,2,3],
        [4,5,6],
        [7,8,9]]

print(snail(array))

#TESTS
def test_order():
    array = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    assert_equals(snail(array), expected)

def test_unorder():
    array = [[1,2,3],
            [8,9,4],
            [7,6,5]]
    expected = [1,2,3,4,5,6,7,8,9]
    assert_equals(snail(array), expected)

def test_four_by_four():
    array = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]
    expected = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
    assert_equals(snail(array), expected)

def test_two_by_two():
    array = [[1,2],
             [3,4]]
    expected = [1,2,4,3]
    assert_equals(snail(array), expected)

def test_four_by_two():
    array = [[1,2,3,4],
             [5,6,7,8]]
    expected = [1,2,3,4,8,7,6,5]
    assert_equals(snail(array), expected)

