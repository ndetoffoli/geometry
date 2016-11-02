################################################################################
# test circle class
# nicolas de toffoli
################################################################################

import pytest
import geometry

def test_circle():
    circle0 = geometry.Circle(0.0)
    assert circle0.perimeter() == 0.0
    assert circle0.area() == 0.0

    circle1 = geometry.Circle(4.0)
    assert round(circle1.perimeter(), 2) == 25.13
    assert round(circle1.area(), 2) == 50.27
