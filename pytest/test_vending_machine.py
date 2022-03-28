import pytest
import vending_machine


def test_vending_machine():
    assert vending_machine.count_currency(1000) == 1


def test_vending_machine2():
    assert vending_machine.count_currency(2000) == 2


def test_vending_machine3():
    assert vending_machine.count_currency(3000) == 3
