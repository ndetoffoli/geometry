################################################################################
# test elipse class
# nicolas de toffoli
################################################################################

import pytest
import geometry

def test_elipse_0():
    elipse_0 = geometry.Elipse(0.0, 0.0)
    assert elipse_0.perimeter() == 0.0
    assert elipse_0.area() == 0.0

def test_elipse_1():
    elipse_1 = geometry.Elipse(4.0, 2.0)
    assert round(elipse_1.perimeter(), 2) == 19.87
    assert round(elipse_1.area(), 2) == 25.13
