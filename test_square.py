################################################################################
# test square class
# nicolas de toffoli
################################################################################

import pytest
import geometry

# global objects
square_0 = geometry.Square(0.0)
square_1 = geometry.Square(10.0)

def test_perimeter_0():
    assert square_0.perimeter() == 0.0

def test_perimeter_1():
    assert square_1.perimeter() == 40.0

def test_area_0():
    assert square_0.area() == 0.0

def test_area_1():
    assert square_1.area() == 100.0
