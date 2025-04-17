import calculator as calc


def test_dot_product_2D():
    """Test the dot product function in 2D."""
    a = [1, 2]
    b = [3, 4]
    expected = 11
    assert calc.dot_product(a, b) == expected


def test_dot_product_3D():
    """Test the dot product function in 3D."""
    a = [1, 2, 3]
    b = [4, 5, 6]
    expected = 32
    assert calc.dot_product(a, b) == expected
