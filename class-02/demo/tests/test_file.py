import pytest
from fizz_buzz.fizz_buzz import fizz_buzz
'''
fizz_buzz
n%3=0 --> "fizz"
n%5=0 --> "buzz"
n%3 and n%5 ==0 --> "fizzbuzz"
n%3 and n%5 !=0 => "n"
1 => "1"
2=> "2"
3=> "fizz"
'''

def test_one():
    actual = fizz_buzz(1)
    expected = "1"
    assert actual == expected  #true or false 

def test_two():
    actual = fizz_buzz(2)
    expected = "2"
    assert actual == expected 

def test_three():
    actual = fizz_buzz(3)
    expected = "fizz"
    assert actual == expected 

def test_four():
    actual = fizz_buzz(4)
    expected = "4"
    assert actual == expected 

def test_five():
    actual = fizz_buzz(5)
    expected = "buzz"
    assert actual == expected 

def test_fifteen():
    actual = fizz_buzz(15)
    expected = "fizz buzz"
    assert actual == expected 

    











