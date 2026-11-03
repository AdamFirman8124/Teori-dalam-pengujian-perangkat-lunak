

# Generated at 2026-11-03 02:35:27.822265
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases with two numbers in the string
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 19 - (5 + 6)
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 1 oranges", 3) == 1
    assert module_0.fruit_distribution("1 apples and 1 oranges", 4) == 2

    # Single number in the string
    assert module_0.fruit_distribution("5 apples", 10) == 5
    assert module_0.fruit_distribution("10 apples", 10) == 0

    # No numbers in the string
    assert module_0.fruit_distribution("apples and oranges", 7) == 7

    # Multi-digit numbers
    assert module_0.fruit_distribution("100 apples and 200 oranges", 500) == 200
    assert module_0.fruit_distribution("12 apples and 34 oranges", 100) == 54

    # Multiple numbers (three or more)
    assert module_0.fruit_distribution("2 apples and 3 oranges and 4 mangoes", 20) == 11

    # Zero remaining
    assert module_0.fruit_distribution("3 apples and 4 oranges", 7) == 0

    # Counted fruits exceed total (negative result)
    assert module_0.fruit_distribution("10 apples", 5) == -5

    # All fruits are mangoes
    assert module_0.fruit_distribution("0 apples and 0 oranges", 9) == 9

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-03 02:36:31.004092
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Test with typical cases
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Test with numbers appearing in different positions
    assert module_0.fruit_distribution("apples 7 and oranges 3", 25) == 15
    assert module_0.fruit_distribution("3 mangoes 4 apples 5 oranges", 30) == 18

    # Test with zero counts
    assert module_0.fruit_distribution("0 apples and 0 oranges", 10) == 10

    # Test with no numeric words at all
    assert module_0.fruit_distribution("only fruits here", 12) == 12

    # Test with empty string
    assert module_0.fruit_distribution("", 7) == 7

    # Test with multi-digit numbers
    assert module_0.fruit_distribution("15 apples and 20 oranges", 100) == 65

    print("All tests passed!")

# Generated at 2026-11-03 02:37:11.142039
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 1 oranges", 3) == 1
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19
    assert module_0.fruit_distribution("apples and oranges", 10) == 10  # no numbers present
    assert module_0.fruit_distribution("10 apples", 10) == 0  # all accounted for

# Generated at 2026-11-03 02:37:53.999585
# Unit test for function fruit_distribution
def test_fruit_distribution():
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19
    assert module_0.fruit_distribution("5 apples and 6 oranges and 10 mangoes", 30) == 9
    assert module_0.fruit_distribution("1 apples", 10) == 9
    assert module_0.fruit_distribution("0 apples and 0 oranges", 0) == 0
    assert module_0.fruit_distribution("3 apples and 4 oranges", 7) == 0

# Generated at 2026-11-03 02:38:44.129125
# Unit test for function fruit_distribution
def test_fruit_distribution():import unittest


def module_0.fruit_distribution(s, n):
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


class TestFruitDistribution(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(module_0.fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_basic_case_2(self):
        self.assertEqual(module_0.fruit_distribution("5 apples and 6 oranges", 21), 10)

    def test_zero_apples(self):
        self.assertEqual(module_0.fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_zero_oranges(self):
        self.assertEqual(module_0.fruit_distribution("1 apples and 0 oranges", 3), 2)

    def test_large_total(self):
        self.assertEqual(module_0.fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_multi_digit_numbers(self):
        self.assertEqual(module_0.fruit_distribution("100 apples and 1 oranges", 120), 19)

    def test_no_digits_in_string(self):
        self.assertEqual(module_0.fruit_distribution("apples and oranges", 10), 10)

    def test_single_fruit(self):
        self.assertEqual(module_0.fruit_distribution("0 apples and 0 oranges", 1), 1)

    def test_numbers_only(self):
        self.assertEqual(module_0.fruit_distribution("3 4", 10), 3)

    def test_negative_result(self):
        self.assertEqual(module_0.fruit_distribution("5 apples and 6 oranges", 5), -6)


if __name__ == "__main__":
    unittest.main()