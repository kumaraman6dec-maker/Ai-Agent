"""Calculator tool definitions for the Claude-powered calculator agent."""

import math
from anthropic import beta_tool


@beta_tool
def add(a: float, b: float) -> str:
    """Add two numbers and return the sum.

    Args:
        a: The first number.
        b: The second number.
    """
    return str(a + b)


@beta_tool
def subtract(a: float, b: float) -> str:
    """Subtract b from a and return the difference.

    Args:
        a: The number to subtract from.
        b: The number to subtract.
    """
    return str(a - b)


@beta_tool
def multiply(a: float, b: float) -> str:
    """Multiply two numbers and return the product.

    Args:
        a: The first number.
        b: The second number.
    """
    return str(a * b)


@beta_tool
def divide(a: float, b: float) -> str:
    """Divide a by b and return the quotient.

    Args:
        a: The dividend.
        b: The divisor (must not be zero).
    """
    if b == 0:
        return "Error: Division by zero is undefined"
    return str(a / b)


@beta_tool
def power(base: float, exponent: float) -> str:
    """Raise base to the power of exponent (base^exponent).

    Args:
        base: The base number.
        exponent: The exponent to raise the base to.
    """
    try:
        result = base ** exponent
        if math.isinf(result):
            return "Error: Result is too large (infinity)"
        return str(result)
    except (OverflowError, ZeroDivisionError) as e:
        return f"Error: {e}"


@beta_tool
def square_root(n: float) -> str:
    """Calculate the square root of n.

    Args:
        n: The number to take the square root of (must be non-negative).
    """
    if n < 0:
        return "Error: Square root of a negative number is not a real number"
    return str(math.sqrt(n))


@beta_tool
def nth_root(n: float, root: float) -> str:
    """Calculate the nth root of a number (equivalent to n^(1/root)).

    Args:
        n: The number to take the root of.
        root: The degree of the root (e.g., 3 for cube root).
    """
    if root == 0:
        return "Error: Root degree cannot be zero"
    if n < 0 and root % 2 == 0:
        return "Error: Even root of a negative number is not a real number"
    try:
        if n < 0:
            return str(-((-n) ** (1 / root)))
        return str(n ** (1 / root))
    except Exception as e:
        return f"Error: {e}"


@beta_tool
def modulo(a: float, b: float) -> str:
    """Calculate the remainder when a is divided by b (a mod b).

    Args:
        a: The dividend.
        b: The divisor (must not be zero).
    """
    if b == 0:
        return "Error: Modulo by zero is undefined"
    return str(a % b)


@beta_tool
def factorial(n: float) -> str:
    """Calculate n! (n factorial) — the product of all positive integers up to n.

    Args:
        n: A non-negative integer to compute the factorial of.
    """
    n_int = int(n)
    if n != n_int:
        return "Error: Factorial is only defined for non-negative integers"
    if n_int < 0:
        return "Error: Factorial is not defined for negative numbers"
    if n_int > 170:
        return "Error: Number too large — factorial exceeds floating-point range"
    return str(math.factorial(n_int))


@beta_tool
def ln(n: float) -> str:
    """Calculate the natural logarithm (base e) of n.

    Args:
        n: The number to take the natural log of (must be positive).
    """
    if n <= 0:
        return "Error: Natural logarithm is undefined for non-positive numbers"
    return str(math.log(n))


@beta_tool
def log10(n: float) -> str:
    """Calculate the base-10 (common) logarithm of n.

    Args:
        n: The number to take the log base 10 of (must be positive).
    """
    if n <= 0:
        return "Error: log10 is undefined for non-positive numbers"
    return str(math.log10(n))


@beta_tool
def log_base(n: float, base: float) -> str:
    """Calculate the logarithm of n with a custom base.

    Args:
        n: The number to take the logarithm of (must be positive).
        base: The base of the logarithm (must be positive and not equal to 1).
    """
    if n <= 0:
        return "Error: Logarithm is undefined for non-positive numbers"
    if base <= 0 or base == 1:
        return "Error: Logarithm base must be positive and not equal to 1"
    return str(math.log(n, base))


@beta_tool
def sine(angle_degrees: float) -> str:
    """Calculate the sine of an angle.

    Args:
        angle_degrees: The angle in degrees.
    """
    return str(math.sin(math.radians(angle_degrees)))


@beta_tool
def cosine(angle_degrees: float) -> str:
    """Calculate the cosine of an angle.

    Args:
        angle_degrees: The angle in degrees.
    """
    return str(math.cos(math.radians(angle_degrees)))


@beta_tool
def tangent(angle_degrees: float) -> str:
    """Calculate the tangent of an angle.

    Args:
        angle_degrees: The angle in degrees (undefined at 90°, 270°, etc.).
    """
    angle_rad = math.radians(angle_degrees)
    if abs(math.cos(angle_rad)) < 1e-10:
        return "Error: Tangent is undefined at this angle (90°, 270°, etc.)"
    return str(math.tan(angle_rad))


@beta_tool
def arc_sine(value: float) -> str:
    """Calculate the inverse sine (arcsin) and return the angle in degrees.

    Args:
        value: A number between -1 and 1.
    """
    if value < -1 or value > 1:
        return "Error: arcsin input must be between -1 and 1"
    return str(math.degrees(math.asin(value)))


@beta_tool
def arc_cosine(value: float) -> str:
    """Calculate the inverse cosine (arccos) and return the angle in degrees.

    Args:
        value: A number between -1 and 1.
    """
    if value < -1 or value > 1:
        return "Error: arccos input must be between -1 and 1"
    return str(math.degrees(math.acos(value)))


@beta_tool
def arc_tangent(value: float) -> str:
    """Calculate the inverse tangent (arctan) and return the angle in degrees.

    Args:
        value: Any real number.
    """
    return str(math.degrees(math.atan(value)))


@beta_tool
def absolute_value(n: float) -> str:
    """Calculate the absolute value (magnitude/distance from zero) of n.

    Args:
        n: Any real number.
    """
    return str(abs(n))


@beta_tool
def percentage(part: float, whole: float) -> str:
    """Calculate what percentage 'part' is of 'whole'.

    Args:
        part: The portion value.
        whole: The total/reference value (must not be zero).
    """
    if whole == 0:
        return "Error: Cannot calculate percentage — 'whole' cannot be zero"
    return str((part / whole) * 100)


@beta_tool
def percent_of(percent: float, number: float) -> str:
    """Calculate a given percentage of a number (e.g., 20% of 150 = 30).

    Args:
        percent: The percentage value (e.g., 20 for 20%).
        number: The number to calculate the percentage of.
    """
    return str((percent / 100) * number)


@beta_tool
def ceil(n: float) -> str:
    """Round n up to the nearest integer (ceiling function).

    Args:
        n: The number to round up.
    """
    return str(math.ceil(n))


@beta_tool
def floor(n: float) -> str:
    """Round n down to the nearest integer (floor function).

    Args:
        n: The number to round down.
    """
    return str(math.floor(n))


@beta_tool
def round_number(n: float, decimal_places: float = 0) -> str:
    """Round n to the specified number of decimal places.

    Args:
        n: The number to round.
        decimal_places: Number of decimal places to round to (default: 0 for nearest integer).
    """
    return str(round(n, int(decimal_places)))


@beta_tool
def gcd(a: float, b: float) -> str:
    """Calculate the Greatest Common Divisor (GCD) of two integers.

    Args:
        a: The first integer.
        b: The second integer.
    """
    return str(math.gcd(int(a), int(b)))


@beta_tool
def lcm(a: float, b: float) -> str:
    """Calculate the Least Common Multiple (LCM) of two integers.

    Args:
        a: The first positive integer.
        b: The second positive integer.
    """
    a_int, b_int = int(a), int(b)
    if a_int == 0 or b_int == 0:
        return "0"
    return str(abs(a_int * b_int) // math.gcd(a_int, b_int))


@beta_tool
def is_prime(n: float) -> str:
    """Check whether a number is prime.

    Args:
        n: A positive integer to test for primality.
    """
    n_int = int(n)
    if n_int < 2:
        return f"{n_int} is not prime"
    if n_int == 2:
        return f"{n_int} is prime"
    if n_int % 2 == 0:
        return f"{n_int} is not prime"
    for i in range(3, int(math.sqrt(n_int)) + 1, 2):
        if n_int % i == 0:
            return f"{n_int} is not prime"
    return f"{n_int} is prime"


# All tools collected for use by the agent
ALL_TOOLS = [
    add, subtract, multiply, divide,
    power, square_root, nth_root, modulo,
    factorial, ln, log10, log_base,
    sine, cosine, tangent,
    arc_sine, arc_cosine, arc_tangent,
    absolute_value, percentage, percent_of,
    ceil, floor, round_number,
    gcd, lcm, is_prime,
]
