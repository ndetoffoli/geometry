################################################################################
# test elipse class
# nicolas de toffoli
################################################################################

import pytest
import geometry

def test_elipse():
    eclipse0 = geometry.Elipse(0.0, 0.0)
    assert eclipse0.perimeter() == 0.0
    assert eclipse0.area() == 0.0

    eclipse1 = geometry.Elipse(4.0, 2.0)
    assert round(eclipse1.perimeter(), 2) == 19.87
    assert round(eclipse1.area(), 2) == 25.13
