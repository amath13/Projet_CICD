import pytest
from calculatrice import addition, soustraction, multiplication, division

def test_add():
    assert addition(3, 2) == 5
    assert addition (-2, 2) == 0
    assert addition (0,0) == 0

def test_soustract():
    assert soustraction(3, 2) == 1
    assert soustraction(-1, 1) == -2
    assert soustraction (0, 0) == 0

def test_mult():
    assert multiplication(2, 3) == 6
    assert multiplication (2, -3) == -6
    assert multiplication (0, 6) == 0

def test_div():
    assert division (6, 3) == 2
    assert division (-6, 2) == -3
    with pytest.raises(ValueError):
        division(1,0)

