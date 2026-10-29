def apply_coupon(cart_total, coupon_code, is_member):
    """
    Applies a coupon to the cart total.
    """
    if cart_total <= 0:
        return 0.0

    discount = 0.0

    if coupon_code == "SAVE10":
        discount = cart_total * 0.10
    elif coupon_code == "SAVE20":
        if cart_total > 100:
            discount = cart_total * 0.20
        else:
            discount = 0.0 
    elif coupon_code == "FREESHIP":
        if is_member:
            discount = 5.0
        else:
            discount = 0.0 
    else:
        discount = 0.0 

    final_price = cart_total - discount
    
    if final_price < 0:
        return 0.0
        
    return final_price
