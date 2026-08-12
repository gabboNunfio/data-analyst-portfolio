def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference between a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

def modulo(a, b):
    """Return the modulus or remainder of the division of a by b."""
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a % b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

