import pytest
from coupon_validator import coupon_discount, best_discount, is_expired

def test_coupon_discount_lines():
    with pytest.raises(ValueError):
        coupon_discount("ANY", 0, True, "mon")
    
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20.0
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0
    
    assert coupon_discount("WEEKEND20", 500, False, "sat") == 100.0
    assert coupon_discount("WEEKEND20", 400, False, "sun") == 50
    
    assert coupon_discount("FLAT100", 400, False, "mon") == 100
    
    assert coupon_discount("INVALID", 100, False, "mon") == 0

def test_best_discount_lines():
    assert best_discount(["FLAT100"], 200, False, "mon") == 80.0
    assert best_discount(["INVALID"], 200, False, "mon") == 0

def test_is_expired_lines():
    # We use integers because the code uses simple subtraction (today - start)
    assert is_expired(10, 5, 0) is True
    assert is_expired(10, 5, 2) is True
    assert is_expired(10, 5, 10) is False
