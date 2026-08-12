import pytest

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulo,
    power,
)

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2

def test_modulo():
    assert modulo(5, 3) == 2

def test_power():
    assert power(2, 3) == 8

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Denominator cannot be zero."):
        divide(5, 0)

def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Denominator cannot be zero."):
        modulo(5, 0)
