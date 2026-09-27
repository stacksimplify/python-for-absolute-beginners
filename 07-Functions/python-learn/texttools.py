# A small module of our OWN. Other files can import these functions.
# (Step-11 imports make_upper and make_lower from here.)

def make_upper(text):
    """Return the text in capital letters."""
    return text.upper()

def make_lower(text):
    """Return the text in small letters."""
    return text.lower()

if __name__ == "__main__":
    # This guard is explained in full in Section 12. In short: this block runs ONLY
    # when you run texttools.py directly, not when another file imports it.
    print(make_upper("hi"))
    print(make_lower("HI"))
