import pytest
import vending_machine


def test_vending_machine():
    assert vending_machine.count_currency(2000) == 2


def test_vending_machine_2():
    assert vending_machine.count_currency(2500) == 3


