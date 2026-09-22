def is_right_angled(a, b, c):
    """
    Check whether a triangle with sides a, b, c is right-angled.
    Uses the Pythagorean theorem: for a right triangle, the square of the
    longest side equals the sum of squares of the other two sides.
    Returns True if right-angled, False otherwise.
    """
    sides = sorted([a, b, c])
    x, y, z = sides  # z is the longest side

    # Basic validity check: sides must form a triangle
    if x <= 0 or y <= 0 or z <= 0 or (x + y <= z):
        return False

    # Use a small tolerance to handle floating-point inputs
    return abs((x ** 2 + y ** 2) - z ** 2) < 1e-9


def main():
    print("Enter the lengths of the three sides of the triangle:")
    try:
        a = float(input("Side 1: "))
        b = float(input("Side 2: "))
        c = float(input("Side 3: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("These side lengths do not form a valid triangle.")
        return

    if is_right_angled(a, b, c):
        print(f"The triangle with sides {a}, {b}, {c} IS a right-angled triangle.")
    else:
        print(f"The triangle with sides {a}, {b}, {c} is NOT a right-angled triangle.")


if __name__ == "__main__":
    main()
