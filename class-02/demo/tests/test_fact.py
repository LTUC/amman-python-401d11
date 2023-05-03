import pytest
from fizz_buzz.factorial import fact
# import fizz_buzz.factorial

def test_one():
    actual= fact(1)
    expected = 1
    assert actual == expected

def test_zero():
    actual= fact(0)
    expected = 1
    assert actual == expected    

def test_two():
    actual= fact(2)
    expected = 2
    assert actual == expected     

def test_five():
    actual= fact(5)
    expected = 120
    assert actual == expected      

def test_string():
    actual= fact("7")
    expected = "please enter a number"
    assert actual == expected 
