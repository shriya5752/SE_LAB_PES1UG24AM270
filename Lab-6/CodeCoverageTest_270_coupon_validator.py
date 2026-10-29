import pytest
from coupon_validator import coupon_discount, best_discount, is_expired

def test_coupon_discount_welcome():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20.0
    # Covers the False branch of is_new_user
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0

def test_coupon_discount_weekend():
    # Covers weekend and high cart total
    assert coupon_discount("WEEKEND20", 600, True, "sat") == 120.0
    # Covers weekend and low cart total (< 500)
    assert coupon_discount("WEEKEND20", 300, True, "sun") == 50
    # Covers non-weekend day
    assert coupon_discount("WEEKEND20", 600, True, "mon") == 0

def test_coupon_discount_flat():
    assert coupon_discount("FLAT100", 400, True, "mon") == 100
    # Covers flat discount with cart <= 300
    assert coupon_discount("FLAT100", 200, True, "mon") == 0

def test_cart_total_exception():
    # Covers raising ValueError for empty/invalid cart
    with pytest.raises(ValueError):
        coupon_discount("WELCOME10", 0, True, "mon")

def test_best_discount():
    codes = ["WELCOME10", "FLAT100"]
    assert best_discount(codes, 500, True, "mon") == 100

def test_is_expired():
    assert is_expired(10, 5, 2) is True
    # Covers days_valid <= 0 branch
    assert is_expired(10, 5, 0) is True