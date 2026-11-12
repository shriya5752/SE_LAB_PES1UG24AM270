from datetime import date
from math import isfinite


def split_code(code):
    """Return the normalized prefix and integer value, or None."""
    if not isinstance(code, str):
        return None
    prefix, separator, value = code.strip().upper().partition("-")
    prefix = prefix.strip()
    if not separator or not prefix or "-" in value:
        return None
    try:
        return prefix, int(value)
    except ValueError:
        return None


def most_expensive(prices_csv):
    """Return the highest finite price, or None for an invalid list."""
    if not isinstance(prices_csv, str):
        return None
    try:
        prices = [float(price) for price in prices_csv.split(",")]
    except ValueError:
        return None
    if not all(isfinite(price) for price in prices):
        return None
    return max(prices)


def expiry_days(date_text):
    """Return calendar days elapsed since 2024-01-01, or None."""
    if not isinstance(date_text, str):
        return None
    date_text = date_text.strip()
    try:
        expiry = date.fromisoformat(date_text)
    except ValueError:
        return None
    if expiry.isoformat() != date_text:
        return None
    return (expiry - date(2024, 1, 1)).days


def main():
    prompts = [
        ("split_code", "Enter a coupon code (e.g. save-20): ", split_code, "Prefix and Value"),
        ("most_expensive", "Enter item prices as CSV (e.g. 199,49.5,320): ", most_expensive, "Most Expensive Item"),
        ("expiry_days", "Enter an expiry date as YYYY-MM-DD: ", expiry_days, "Days Since 2024"),
    ]
    for name, prompt, processor, label in prompts:
        print(f"==== Running {name} ====")
        result = processor(input(prompt))
        if result is None:
            print("Invalid input.")
        else:
            print(f"{label}: {result}")
        print()


if __name__ == "__main__":
    main()
