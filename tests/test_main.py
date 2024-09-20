''' My Calculator Test'''
import pytest
from app.main import addition, division, subtraction, multiplcation

def test_addition():
    '''Addition funtion'''
    assert addition(1,1)  == 2

def test_subtraction():
    '''Subtraction funtion'''
    assert subtraction(1,1)  == 0

def test_multiplcation():
    '''Multiplcation funtion'''
    assert multiplcation(2,2)  == 4

def test_division():
    '''Division funtion'''
    assert division(2,2)  == 1

def test_division_by_zero_exception():
    '''Division funtion testing for exception divide by zero'''
    with pytest.raises(ZeroDivisionError):
        division(2,0)
