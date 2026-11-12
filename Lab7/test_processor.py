from datetime import date
from math import isfinite

from hypothesis import given, strategies as st

from processor import expiry_days, most_expensive, split_code


@given(st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1),
       st.integers(min_value=0, max_value=10000))
def test_split_code_normalizes_prefix(prefix, value):
    assert split_code(f" {prefix} - {value} ") == (prefix.upper(), value)


@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_most_expensive_matches_max(prices):
    prices_csv = ", ".join(map(str, prices))
    assert most_expensive(prices_csv) == max(prices)


@given(st.sampled_from(["NaN", "Infinity", "-Infinity"]))
def test_most_expensive_rejects_nonfinite_prices(price):
    assert most_expensive(price) is None


@given(st.dates())
def test_expiry_days_matches_calendar(expiry):
    assert expiry_days(expiry.isoformat()) == (expiry - date(2024, 1, 1)).days


@given(st.text() | st.none() | st.integers())
def test_processors_handle_unexpected_input(value):
    coupon = split_code(value)
    price = most_expensive(value)
    days = expiry_days(value)
    assert coupon is None or (
        isinstance(coupon[0], str) and coupon[0] and isinstance(coupon[1], int)
    )
    assert price is None or (isinstance(price, float) and isfinite(price))
    assert days is None or isinstance(days, int)
