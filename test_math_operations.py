import math_operations

def test_add():
    assert math_operations.add(3, 5) == 8
    assert math_operations.add(-1, 1) == 0
    assert math_operations.add(-1, -1) == -2

def test_subtract():
    assert math_operations.subtract(5, 3) == 2
    assert math_operations.subtract(1, -1) == 2
    assert math_operations.subtract(-1, -1) == 0
