################################################################################
# test circle class
# nicolas de toffoli
################################################################################

import pytest
import geometry

# global objects
circle0 = geometry.Circle(0.0)
circle1 = geometry.Circle(4.0)

def test_perimeter_0():
    assert circle0.perimeter() == 0.0

def test_perimeter_1():
    assert round(circle1.perimeter(), 2) == 25.13

def test_area_0():
    assert circle0.area() == 0.0

def test_area_1():
    assert round(circle1.area(), 2) == 50.27
