################################################################################
# test ellipse class
# nicolas de toffoli
################################################################################

import pytest
import geometry

# global objects
ellipse_0 = geometry.Elipse(0.0, 0.0)
ellipse_1 = geometry.Elipse(4.0, 2.0)

def test_perimeter_0():
    assert ellipse_0.perimeter() == 0.0

def test_perimeter_1():
    assert round(ellipse_1.perimeter(), 2) == 19.87

def test_area_0():
    assert ellipse_0.area() == 0.0

def test_area_1():
    assert round(ellipse_1.area(), 2) == 25.13
