import pytest
import day_of_week


@pytest.mark.parametrize("date, result",
                         [
                             ('30 04 1995', 'Sunday'),
                             ('27 11 1192', 'Friday')

                         ])
def test_vending_machine(date, result):
    assert day_of_week.findDay(date) == result
