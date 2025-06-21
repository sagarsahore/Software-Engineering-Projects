import pytest
from pytest import approx
from mypackage.calculator import (
    add, subtract, multiply, divide,
    power, root,
    sine, cosine, tangent
)

# ----- Arithmetic Tests -----

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 2) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 99) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# ----- Power and Root Tests -----

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_root():
    assert root(9, 2) == 3
    assert root(27, 3) == 3
    with pytest.raises(ValueError, match="Cannot take even root of negative number"):
        root(-16, 2)

# ----- Trigonometric Function Tests -----

def test_sine():
    assert sine(0) == approx(0.0)
    assert sine(90) == approx(1.0, rel=1e-3)

def test_cosine():
    assert cosine(0) == approx(1.0)
    assert cosine(180) == approx(-1.0, rel=1e-3)

def test_tangent():
    assert tangent(45) == approx(1.0, rel=1e-3)
    with pytest.raises(ValueError, match="Tangent undefined at 90 degrees"):
        tangent(90)
