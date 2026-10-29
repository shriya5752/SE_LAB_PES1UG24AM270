import pytest
from coupon_validator import coupon_discount, best_discount, is_expired

# 1. Test cart_total <= 0 exception branch
def test_cart_total_invalid():
    with pytest.raises(ValueError, match="empty cart"):
        coupon_discount("WELCOME10", 0, True, "mon")

# 2. Test WELCOME10 branches (is_new_user True vs False)
def test_welcome_branches():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20.0
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0

# 3. Test WEEKEND20 branches (day matching, cart_total >= 500 vs < 500, non-weekend)
def test_weekend_branches():
    # Sat/Sun with cart >= 500 (True, True)
    assert coupon_discount("WEEKEND20", 600, True, "sat") == 120.0
    # Sat/Sun with cart < 500 (True, False)
    assert coupon_discount("WEEKEND20", 300, True, "sun") == 50
    # Non-weekend day (False)
    assert coupon_discount("WEEKEND20", 600, True, "mon") == 0

# 4. Test FLAT100 branches (cart_total > 300 vs <= 300)
def test_flat_branches():
    assert coupon_discount("FLAT100", 400, True, "mon") == 100
    assert coupon_discount("FLAT100", 200, True, "mon") == 0

# 5. Test unknown coupon fallback branch
def test_unknown_coupon():
    assert coupon_discount("UNKNOWN", 200, True, "mon") == 0

# 6. Test best_discount cap check branches (best > cap vs best <= cap)
def test_best_discount_cap():
    # best exceeds cap (cart_total = 100, weekend discount = 50, cap = 100 * 0.4 = 40)
    codes = ["WEEKEND20"]
    assert best_discount(codes, 100, True, "sat") == 40
# 7. Test is_expired branches (days_valid <= 0 vs > 0)
def test_is_expired_branches():
    assert is_expired(10, 5, 0) is True
    assert is_expired(10, 5, 10) is False
    assert is_expired(10, 5, 3) is True