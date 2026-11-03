

# Generated at 2026-11-02 15:47:46.859669
# Unit test for function compare
def test_compare():
    # Test with all correct guesses
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test with all wrong guesses
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test with mixed results
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert module_0.compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, 0]) == [4, 4, 1, 0, 0, 4]

    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]

    # Test with empty lists
    assert module_0.compare([], []) == []

    # Test with single element
    assert module_0.compare([5], [5]) == [0]
    assert module_0.compare([5], [3]) == [2]

    # Test with floats
    assert module_0.compare([1.5, 2.5], [2.0, 2.0]) == [0.5, 0.5]

    # Test with larger numbers
    assert module_0.compare([100, 200], [50, 250]) == [50, 50]

    print("All tests passed!")


test_compare()

# Generated at 2026-11-02 15:49:13.917739
# Unit test for function compare
def test_compare():
    # nonce:1ab90320
    # Test case 1: basic differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test case 2: exact matches yield zeros
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test case 3: absolute value handles reversed differences
    assert module_0.compare([5, 1, 3], [1, 5, 1]) == [4, 4, 2]

    # Test case 4: empty lists
    assert module_0.compare([], []) == []

    # Test case 5: single elements
    assert module_0.compare([0], [10]) == [10]

    # Test case 6: negative numbers
    assert module_0.compare([-1, -2], [-4, 2]) == [3, 4]

    # Test case 7: mixed values
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

# Generated at 2026-11-02 15:50:49.701767
# Unit test for function compare
def test_compare():
    class TestCompare(unittest.TestCase):

        def test_basic_case(self):
            self.assertEqual(module_0.compare([1, 2, 3], [1, 2, 3]), [0, 0, 0])

        def test_all_different(self):
            self.assertEqual(module_0.compare([1, 2, 3], [3, 2, 1]), [2, 0, 2])

        def test_guess_higher(self):
            self.assertEqual(module_0.compare([1, 2, 3], [4, 5, 6]), [3, 3, 3])

        def test_guess_lower(self):
            self.assertEqual(module_0.compare([4, 5, 6], [1, 2, 3]), [3, 3, 3])

        def test_mixed(self):
            self.assertEqual(module_0.compare([5, 1, 3, 7], [2, 8, 3, 4]), [3, 7, 0, 3])

        def test_empty_lists(self):
            self.assertEqual(module_0.compare([], []), [])

        def test_single_element(self):
            self.assertEqual(module_0.compare([10], [4]), [6])

        def test_negative_numbers(self):
            self.assertEqual(module_0.compare([-1, -5, -3], [-4, -2, -9]), [3, 3, 6])

        def test_zeros(self):
            self.assertEqual(module_0.compare([0, 0, 0], [0, 0, 0]), [0, 0, 0])

        def test_result_always_non_negative(self):
            result = module_0.compare([1, 2, 3], [10, 1, 5])
            self.assertTrue(all(x >= 0 for x in result))

    return TestCompare

if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 15:52:48.296177
# Unit test for function compare
def test_compare():
    # Test case 1: all guesses correct
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0], "Test case 1 failed"
    
    # Test case 2: all guesses wrong
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3], "Test case 2 failed"
    
    # Test case 3: mixed correct and incorrect guesses
    assert module_0.compare([1, 2, 3, 4], [1, 5, 3, 7]) == [0, 3, 0, 3], "Test case 3 failed"
    
    # Test case 4: empty lists
    assert module_0.compare([], []) == [], "Test case 4 failed"
    
    # Test case 5: negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6], "Test case 5 failed"
    
    # Test case 6: guess lower than game values
    assert module_0.compare([5, 10, 15], [3, 7, 10]) == [2, 3, 5], "Test case 6 failed"
    
    # Test case 7: single element lists
    assert module_0.compare([0], [0]) == [0], "Test case 7 failed"
    assert module_0.compare([0], [1]) == [1], "Test case 7b failed"
    
    # Test case 8: absolute difference ordering (game > guess and guess > game)
    assert module_0.compare([10, 1], [1, 10]) == [9, 9], "Test case 8 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_compare()
# nonce:40ac9c4c

# Generated at 2026-11-02 15:55:00.868384
# Unit test for function compare
def test_compare():
    # Test with positive differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    
    # Test with mixed differences
    assert module_0.compare([1, 2, 3, 4], [1, 2, 3, 4]) == [0, 0, 0, 0]
    
    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]
    
    # Test with single element
    assert module_0.compare([5], [10]) == [5]
    
    # Test with empty lists
    assert module_0.compare([], []) == []
    
    # Test with larger values
    assert module_0.compare([100, 200, 300], [50, 250, 350]) == [50, 50, 50]
    
    # Test with random larger arrays
    game = [i for i in range(10)]
    guess = [9 - i for i in range(10)]
    assert module_0.compare(game, guess) == [9 - 2 * i if i < 5 else 2 * i - 9 for i in range(10)]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_compare()