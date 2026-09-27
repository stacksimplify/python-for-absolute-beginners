# A module inside the "store" package. It holds two small pricing functions.

def line_total(price, quantity):
    return price * quantity


def apply_discount(total, percent):
    discount = total * percent / 100
    return total - discount
