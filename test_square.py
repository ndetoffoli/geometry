################################################################################
# test square class
# nicolas de toffoli
################################################################################

import pytest
import geometry

def test_square_0():
    square_0 = geometry.Square(0.0)
    assert square_0.perimeter() == 0.0
    assert square_0.area() == 0.0

def test_square_1():
    square_1 = geometry.Square(10.0)
    assert square_1.perimeter() == 40.0
    assert square_1.area() == 100.0
