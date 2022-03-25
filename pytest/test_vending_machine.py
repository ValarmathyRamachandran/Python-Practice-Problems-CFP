import pytest
import vending_machine


@pytest.mark.parametrize("amount, result",
                         [
                             ('1000', 1)
                         ])
def test_vending_machine(amount, result):
    assert vending_machine.count_currency(1000) == result
