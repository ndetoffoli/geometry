################################################################################
# test rectangle class
# nicolas de toffoli
################################################################################

import pytest
import geometry

def test_rectangle():
    rect0 = geometry.Rectangle(0.0, 0.0)
    assert rect0.perimeter() == 0.0
    assert rect0.area() == 0.0

    rect1 = geometry.Rectangle(10.0, 4.0)
    assert rect1.perimeter() == 28.0
    assert rect1.area() == 40.0
