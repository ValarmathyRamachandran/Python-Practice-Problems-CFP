import pytest
import decimal_to_binary


def test_decimal_to_binary():
    assert decimal_to_binary.decimal_to_binary(24) == '11000'

