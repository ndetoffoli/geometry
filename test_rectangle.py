################################################################################
# test rectangle class
# nicolas de toffoli
################################################################################

import pytest
import geometry

# global objects
rectangle_0 = geometry.Rectangle(0.0, 0.0)
rectangle_1 = geometry.Rectangle(10.0, 4.0)

def test_perimeter_0():
    assert rectangle_0.perimeter() == 0.0

def test_perimeter_1():
    assert rectangle_1.perimeter() == 28.0

def test_area_0():
    assert rectangle_0.area() == 0.0

def test_area_1():
    assert rectangle_1.area() == 40.0
