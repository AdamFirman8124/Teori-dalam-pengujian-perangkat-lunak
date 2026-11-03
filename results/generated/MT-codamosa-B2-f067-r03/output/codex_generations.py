

# Generated at 2026-11-02 12:42:58.175936
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases with two numbers in the string
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 20) == 9
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Single number in the string
    assert module_0.fruit_distribution("10 apples", 15) == 5
    assert module_0.fruit_distribution("0 apples", 5) == 5

    # No digits in the string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 7) == 7

    # Numbers with multiple digits
    assert module_0.fruit_distribution("123 mangoes and 456 guavas", 1000) == 421

    # Result can be zero
    assert module_0.fruit_distribution("3 apples and 4 oranges", 7) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-02 12:46:38.798138
# Unit test for function fruit_distribution
def test_fruit_distribution():import unittest


def module_0.fruit_distribution(s, n):
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


class TestFruitDistribution(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(module_0.fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_zero_apples(self):
        self.assertEqual(module_0.fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_large_total(self):
        self.assertEqual(module_0.fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_multi_digit(self):
        self.assertEqual(module_0.fruit_distribution("100 apples and 1 oranges", 120), 19)

    def test_single_number(self):
        self.assertEqual(module_0.fruit_distribution("10 apples", 15), 5)

    def test_no_digits(self):
        self.assertEqual(module_0.fruit_distribution("apples and oranges", 7), 7)

    def test_all_digits(self):
        self.assertEqual(module_0.fruit_distribution("3 4", 10), 3)

    def test_result_zero(self):
        self.assertEqual(module_0.fruit_distribution("4 apples and 5 oranges", 9), 0)

    def test_mixed_text(self):
        self.assertEqual(module_0.fruit_distribution("apples 12 oranges 8 mangoes", 30), 10)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 12:49:21.636807
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic cases with typical fruit descriptions
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 oranges", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19

    # String with no digits - all fruits are mangoes
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 7) == 7

    # Single digit fruit count
    assert module_0.fruit_distribution("1 apple", 1) == 0
    assert module_0.fruit_distribution("3 apples", 3) == 0

    # Multi-digit numbers
    assert module_0.fruit_distribution("12 apples and 34 oranges", 50) == 4
    assert module_0.fruit_distribution("999 apples", 1000) == 1

    # Numbers embedded in longer text
    assert module_0.fruit_distribution("there are 4 apples and 5 oranges in the basket", 15) == 6

    # All fruits accounted for by described fruits
    assert module_0.fruit_distribution("10 apples and 10 oranges", 20) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_fruit_distribution()

# Generated at 2026-11-02 12:50:29.703610
# Unit test for function fruit_distribution
def test_fruit_distribution():
    # Basic test cases
    assert module_0.fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert module_0.fruit_distribution("5 apples and 6 apples", 21) == 10
    assert module_0.fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert module_0.fruit_distribution("1 apples and 0 oranges", 3) == 2
    assert module_0.fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert module_0.fruit_distribution("2 apples and 3 oranges", 5) == 0
    assert module_0.fruit_distribution("1 apples and 1 oranges", 10) == 8
    
    # Test with multi-digit numbers
    assert module_0.fruit_distribution("100 apples and 1 oranges", 120) == 19
    assert module_0.fruit_distribution("10 apples and 20 oranges", 40) == 10
    
    # Test with no digits in the string
    assert module_0.fruit_distribution("apples and oranges", 10) == 10
    assert module_0.fruit_distribution("", 5) == 5
    
    # Test with all fruits accounted for
    assert module_0.fruit_distribution("3 apples and 4 oranges", 7) == 0
    
    # Test with large numbers
    assert module_0.fruit_distribution("1000 apples and 2000 oranges", 5000) == 2000
    
    # Test with single digit total
    assert module_0.fruit_distribution("1 apples and 2 oranges", 5) == 2
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_fruit_distribution()