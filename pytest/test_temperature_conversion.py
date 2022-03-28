import pytest
import temperature_conversion


def test_temperature_conversion():
    assert temperature_conversion.temperature_conversion_celsius(30) == 86


def test_temperature_conversion2():
    assert temperature_conversion.temperature_conversion_fahrenheit(86) == 30
