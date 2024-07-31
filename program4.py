def classify_triangle(side_a, side_b, side_c):
    """
    Classify a triangle based on its sides.
    Args:
        side_a (int): Side A of the triangle
        side_b (int): Side B of the triangle
        side_c (int): Side C of the triangle
    Returns:
        str: The type of triangle (Equilateral, Isosceles, Scalene, or Not a Triangle)
    """
    # Check if the sides form a valid triangle
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        return "Not a Triangle"
    
    # Check for invalid input
    if not (0 < side_a <= 10 and 0 < side_b <= 10 and 0 < side_c <= 10):
        return "Invalid input. Sides must be positive integers no larger than 10."
    
    # Determine the type of triangle
    if side_a == side_b == side_c:
        return "Equilateral triangle"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Test Cases
test_cases = [
    # Boundary Value Analysis
    (0, 0, 0),        # Invalid input
    (1, 1, 1),        # Equilateral triangle
    (1, 1, 10),       # Isosceles triangle
    (1, 10, 1),       # Isosceles triangle
    (10, 10, 10),     # Equilateral triangle
    (10, 10, 11),     # Not a Triangle
    # Equivalence Class Partitioning
    (2, 2, 2),        # Equilateral triangle
    (2, 3, 2),        # Isosceles triangle
    (2, 3, 4),        # Scalene triangle
    (10, 10, 5),      # Isosceles triangle
    (10, 5, 10),      # Isosceles triangle
    # Decision Table
    (3, 3, 3),        # Equilateral triangle
    (3, 4, 3),        # Isosceles triangle
    (3, 4, 5),        # Scalene triangle
    (5, 5, 10),       # Not a Triangle
]

# Execute Test Cases
for test_case in test_cases:
    result = classify_triangle(*test_case)
    print(f"Test Case: {test_case} -> {result}")
