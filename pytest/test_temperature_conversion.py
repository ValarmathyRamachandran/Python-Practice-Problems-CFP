import pytest
import temperature_conversion


@pytest.mark.parametrize('celsius, result',
                         [(30, 86),
                          (86, 186.80)
                          ])
def test_temperature_conversion(celsius, result):

    assert temperature_conversion.temperature_conversion_celsius(30) == result
