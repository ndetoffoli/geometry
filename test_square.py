################################################################################
# test square class
# nicolas de toffoli
################################################################################

import pytest
import geometry

def test_square():
    square0 = geometry.Square(0.0)
    assert square0.perimeter() == 0.0
    assert square0.area() == 0.0

    square1 = geometry.Square(10.0)
    assert square1.perimeter() == 40.0
    assert square1.area() == 100.0
