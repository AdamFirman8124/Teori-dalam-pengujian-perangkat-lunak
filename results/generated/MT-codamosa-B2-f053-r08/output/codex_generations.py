

# Generated at 2026-11-02 07:50:53.834686
# Unit test for function add
def test_add():
    assert module_0.add(2, 3) == 5
    assert module_0.add(-1, 1) == 0
    assert module_0.add(0, 0) == 0
    assert module_0.add(-5, -7) == -12
    assert module_0.add(100, 200) == 300

# Generated at 2026-11-02 07:51:23.041782
# Unit test for function add
def test_add():
    # Basic positive numbers
    assert module_0.add(1, 2) == 3
    assert module_0.add(10, 20) == 30

    # Zero cases
    assert module_0.add(0, 0) == 0
    assert module_0.add(0, 5) == 5
    assert module_0.add(5, 0) == 5

    # Negative numbers
    assert module_0.add(-1, -2) == -3
    assert module_0.add(-1, 1) == 0
    assert module_0.add(1, -1) == 0
    assert module_0.add(-10, 5) == -5

    # Large numbers
    assert module_0.add(1000000, 2000000) == 3000000
    assert module_0.add(2**31 - 1, 1) == 2**31

# Generated at 2026-11-02 07:51:43.904406
# Unit test for function add
def test_add():
    assert module_0.add(2, 3) == 5
    assert module_0.add(0, 0) == 0
    assert module_0.add(-1, 1) == 0
    assert module_0.add(-5, -3) == -8
    assert module_0.add(100, 200) == 300
    assert module_0.add(0, 7) == 7
    assert module_0.add(7, 0) == 7

# Generated at 2026-11-02 07:52:03.984434
# Unit test for function add
def test_add():import unittest


def module_0.add(x: int, y: int):
    return x + y


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(module_0.add(2, 3), 5)
        self.assertEqual(module_0.add(10, 20), 30)

    def test_negative_numbers(self):
        self.assertEqual(module_0.add(-1, -2), -3)
        self.assertEqual(module_0.add(-5, 5), 0)

    def test_zero(self):
        self.assertEqual(module_0.add(0, 0), 0)
        self.assertEqual(module_0.add(0, 7), 7)

    def test_large_numbers(self):
        self.assertEqual(module_0.add(10**18, 10**18), 2 * 10**18)

    def test_return_type(self):
        self.assertIsInstance(module_0.add(1, 2), int)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 07:52:39.142005
# Unit test for function add
def test_add():
    # Basic positive numbers
    assert module_0.add(2, 3) == 5
    assert module_0.add(10, 20) == 30

    # Zero cases
    assert module_0.add(0, 0) == 0
    assert module_0.add(0, 5) == 5
    assert module_0.add(5, 0) == 5

    # Negative numbers
    assert module_0.add(-1, -1) == -2
    assert module_0.add(-5, 3) == -2
    assert module_0.add(5, -3) == 2

    # Large numbers
    assert module_0.add(1_000_000, 2_000_000) == 3_000_000

    # Symmetry check
    assert module_0.add(7, 4) == module_0.add(4, 7)