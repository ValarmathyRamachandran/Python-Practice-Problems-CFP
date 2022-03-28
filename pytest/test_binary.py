import pytest
import binary


def test_binary():
    assert binary.swap_nibbles(100) == 70
