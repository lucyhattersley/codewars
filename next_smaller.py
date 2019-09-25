from nose.tools import assert_equals

# Code from geeksforgeeks

# This code finds the next larger number with the same set of digits

# Given number as int array, this function finds the  
# greatest number and returns the number as integer
# n = length of number 
def next_smaller(n):

    # create number and n_length from n

    number = [int(x) for x in str(n)]
    n_length = len(number)  

    # Start from the right most digit and find the first 
    # digit that is greater than the digit next to it 
    for i in range(n_length-1,0,-1): 
        if number[i] > number[i-1]: 
            break
            
    # If no such digit found,then all numbers are in  
    # ascending order, no lower number is possible 
    if i == 0: 
        print("Next number not possible")
        return
        
    # Find the smallest digit on the right side of  
    # (i-1)'th digit that is lower than number[i-1] 
    x = number[i-1] 
    largest = i 
    for j in range(i+1,n_length): 
        if number[j] < x and number[j] > number[largest]: 
            largest = j 
        
    # Swapping the above found smallest digit with (i-1)'th 
    number[largest],number[i-1] = number[i-1], number[largest] 
    
    # X is the final number, in integer datatype  
    x = 0
    # Converting list upto i-1 into number 
    for j in range(i): 
        x = x * 10 + number[j] 
    
    # Sort the digits after i-1 in descending order 
    number = sorted(number[i:], reverse=True) 
    # converting the remaining sorted digits into number 
    for j in range(n_length-i): 
        x = x * 10 + number[j] 
    
    print("Next number with set of digits is",x)

next_smaller(123)


# def next_smaller(n):
#     digits = [int(x) for x in str(n)]

#     if all(digits[i] <= digits[i+1] for i in range(len(digits)-1)):
#         return -1

#     i = 0
#     try:
#         while digits[i + 1] < digits[i]:
#             i = i + 1
#     except:
#         pass

#     # i = 1
#     # while digits[i] > digits[i-1]:
#     #     i = i + 1

#     head = digits[:i]
#     tail = digits[i:]

#     i = 0
#     for i in range(len(tail)):
#         if tail[i] < head[-1]:
#             try:
#                 if tail[i] > tail[current_largest]:
#                     current_largest = i
#             except:
#                 current_largest = i

#     temp = head[-1]
#     head[-1] = tail[current_largest]
#     tail[current_largest] = temp

#     if head[0] == 0:
#         return -1
#     else:
#         result = head + tail[::-1]
#         return int(''.join(map(str,result)))

# next_smaller(531)


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