import pytest
import sqrt


def test_sqrt():
    assert sqrt.squareRoot(16, 0.0001) == 4.000000000000051


def test_sqrt_val():
    assert sqrt.squareRoot(25, 0.0001) == 5.000000000053722
