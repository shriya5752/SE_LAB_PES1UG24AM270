import pytest
from coupon_validator import coupon_discount, best_discount, is_expired

def test_coupon_discount_branches():
    # Branch: cart_total <= 0 (True)
    with pytest.raises(ValueError):
        coupon_discount("ANY", -10, True, "mon")
    
    # Branch: WEEKEND20 -> day in sat/sun (False)
    assert coupon_discount("WEEKEND20", 500, False, "mon") == 0
    
    # Branch: FLAT100 -> cart_total > 300 (False)
    assert coupon_discount("FLAT100", 200, False, "mon") == 0

def test_best_discount_branches():
    # Branch: value > best (True) AND best > cap (True)
    # FLAT100 gives 100. Cap is 200 * 0.4 = 80. Returns 80.
    assert best_discount(["FLAT100"], 200, False, "mon") == 80.0
    
    # Branch: value > best (False) AND best > cap (False)
    assert best_discount(["INVALID"], 200, False, "mon") == 0

def test_is_expired_branches():
    # Branch: days_valid <= 0 (True)
    assert is_expired(10, 5, 0) is True
    # Branch: days_valid <= 0 (False) -> logic False
    assert is_expired(10, 5, 10) is False
