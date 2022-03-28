import pytest
import monthly_payment


def test_monthly_payment():
    assert monthly_payment.monthly_loan(1000000, 7, 10) == 11610.847921862374


