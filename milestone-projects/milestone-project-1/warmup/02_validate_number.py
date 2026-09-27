"""
Warm-up 2: Validate a Positive Amount Using String Methods (No try/except)

Write a program that checks whether text entered by the user is a valid positive
amount by using string methods instead of try/except. Valid examples include
"12" and "12.50". Reject invalid values such as "-5", "abc", "1.2.3", "0",
"0.0", and "0.00".

Task-1:
Validate a positive whole number using .isdecimal().
Examples:
- Valid   : "12", "007"
- Invalid : "-5", "abc", "1.5"

Task-2:
Build a complete amount validation function that accepts either:
- A positive whole number (12)
- A positive decimal number (12.50)

Reject:
- Invalid formats ("abc", "1.2.3", "-5")
- Zero values ("0", "0.0", "0.00")

Python concepts practiced:
1. String methods:
   - .strip()
   - .split(".")
   - .isdecimal()
2. len() to determine whether the input is a whole number or a decimal.
3. if / elif / else to validate different input formats.
4. Functions for reusable validation logic.
5. return to send a result back to the caller.
6. Boolean values (True and False) and the and operator.
7. float() to turn validated digits into a number.
8. for loops to test the functions with multiple sample values.
9. f-strings to create readable output.

Project connection:
The Task-2 function IS f1_is_valid_amount.py in the project, character for
character. Write it here, then copy it straight across. It does no printing,
because a helper never prints; the test loop below prints the verdict instead.
It validates the amount before calling float(amount_text), making that
conversion safe without using try/except (covered later in Section 09).
"""


# ===== Task-1: Validate a Whole Number =====
# Accepts a positive whole number (12, 007).
# Rejects decimal numbers (1.5), negative numbers (-5), and non-numeric text (abc).
#
# Note:
# .isdecimal() returns True only when every character is a digit.
# A minus sign (-), decimal point (.), or letters cause it to return False.
# Section 03 taught .isdigit(); .isdecimal() is its stricter sibling. .isdigit()
# also accepts characters like a superscript two, which float() then cannot read.
def is_whole_number(amount_text):
    return amount_text.strip().isdecimal()


print("\n===== Task-1: Validate a Whole Number =====")

# Test the function with different sample inputs.
for amount_text in ["12", "007", "-5", "abc", "1.5"]:
    print(f"\nInput : {amount_text}")
    print(f"Result is_whole_number: {is_whole_number(amount_text)}")


# ===== Task-2: Validate an Amount (Function-1) =====
# Accepts a positive whole number (12) or a positive decimal number (12.50).
# Rejects invalid formats (abc, 1.2.3, -5) and zero values (0, 0.0, 0.00).
# This function becomes f1_is_valid_amount.py in the project, unchanged. It never
# prints: a helper hands back True or False and lets the caller do the talking.
def is_valid_amount(amount_text):
    """True if amount_text is a positive number like '12' or '12.50' (rejects 0 and negatives).

    Uses string methods and float(). No try/except (that is Section 09).
    """
    amount_text = amount_text.strip()
    decimal_parts = amount_text.split(".")
    if len(decimal_parts) == 1:
        is_valid_format = decimal_parts[0].isdecimal()
    elif len(decimal_parts) == 2:
        is_valid_format = (
            decimal_parts[0].isdecimal() and
            decimal_parts[1].isdecimal()
        )
    else:
        is_valid_format = False
    if not is_valid_format:
        return False
    # every character is a digit now, so float() is safe: a real amount is above zero
    return float(amount_text) > 0


print("\n===== Task-2: Validate an Amount =====")

# Test the function with different sample inputs.
for amount_text in ["12", "12.50", "0", "-5", "abc", "1.2.3", " 7 "]:
    print(f"\nInput : {amount_text}")
    print(f"Result is_valid_amount: {is_valid_amount(amount_text)}")
