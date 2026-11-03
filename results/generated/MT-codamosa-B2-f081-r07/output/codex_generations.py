

# Generated at 2026-11-02 21:38:44.720183
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestNumericalLetterGrade)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    test_numerical_letter_grade()

# Generated at 2026-11-02 21:40:06.982553
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Example from specification
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']

    # Boundary checks for each grade tier
    assert module_0.numerical_letter_grade([4.0]) == ['A+']
    assert module_0.numerical_letter_grade([3.9]) == ['A']
    assert module_0.numerical_letter_grade([3.7]) == ['A-']
    assert module_0.numerical_letter_grade([3.8]) == ['A']
    assert module_0.numerical_letter_grade([3.4]) == ['A-']
    assert module_0.numerical_letter_grade([3.3]) == ['B+']
    assert module_0.numerical_letter_grade([3.2]) == ['B+']
    assert module_0.numerical_letter_grade([3.0]) == ['B']
    assert module_0.numerical_letter_grade([3.1]) == ['B+']
    assert module_0.numerical_letter_grade([2.9]) == ['B']
    assert module_0.numerical_letter_grade([2.7]) == ['B-']
    assert module_0.numerical_letter_grade([2.8]) == ['B']
    assert module_0.numerical_letter_grade([2.4]) == ['B-']
    assert module_0.numerical_letter_grade([2.3]) == ['C+']
    assert module_0.numerical_letter_grade([2.1]) == ['C+']
    assert module_0.numerical_letter_grade([2.0]) == ['C']
    assert module_0.numerical_letter_grade([1.9]) == ['C']
    assert module_0.numerical_letter_grade([1.7]) == ['C-']
    assert module_0.numerical_letter_grade([1.8]) == ['C']
    assert module_0.numerical_letter_grade([1.4]) == ['C-']
    assert module_0.numerical_letter_grade([1.3]) == ['D+']
    assert module_0.numerical_letter_grade([1.1]) == ['D+']
    assert module_0.numerical_letter_grade([1.0]) == ['D']
    assert module_0.numerical_letter_grade([0.9]) == ['D']
    assert module_0.numerical_letter_grade([0.7]) == ['D-']
    assert module_0.numerical_letter_grade([0.8]) == ['D']
    assert module_0.numerical_letter_grade([0.5]) == ['D-']
    assert module_0.numerical_letter_grade([0.1]) == ['D-']
    assert module_0.numerical_letter_grade([0.0]) == ['E']
    assert module_0.numerical_letter_grade([-0.2]) == ['E']
    assert module_0.numerical_letter_grade([-3.0]) == ['E']

    # Edge cases: empty list and single values
    assert module_0.numerical_letter_grade([]) == []
    assert module_0.numerical_letter_grade([1.2]) == ['D+']

    # Mixed inputs
    assert module_0.numerical_letter_grade([0.49, 0, 4.0, 3.71, 2.75]) == ['D-', 'E', 'A+', 'A', 'B']
    assert module_0.numerical_letter_grade([2.5, 2.0, 1.5, 1.0, 0.5, 0.0]) == ['B-', 'C', 'C-', 'D', 'D-', 'E']

    print("All tests passed!")


if __name__ == "__main__":
    test_numerical_letter_grade()

# Generated at 2026-11-02 21:41:34.460204
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact boundary: 4.0 -> A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Just above 3.7 -> A; exactly 3.7 -> A-
    assert module_0.numerical_letter_grade([3.9, 3.8, 3.71]) == ["A", "A", "A"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]

    # Just above 3.3 -> A-; exactly 3.3 -> B+
    assert module_0.numerical_letter_grade([3.5, 3.4]) == ["A-", "A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]

    # Just above 3.0 -> B+; exactly 3.0 -> B
    assert module_0.numerical_letter_grade([3.2, 3.1]) == ["B+", "B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]

    # Just above 2.7 -> B; exactly 2.7 -> B-
    assert module_0.numerical_letter_grade([2.9, 2.8]) == ["B", "B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]

    # Just above 2.3 -> B-; exactly 2.3 -> C+
    assert module_0.numerical_letter_grade([2.5, 2.4]) == ["B-", "B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]

    # Just above 2.0 -> C+; exactly 2.0 -> C
    assert module_0.numerical_letter_grade([2.2, 2.1]) == ["C+", "C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C"]

    # Just above 1.7 -> C; exactly 1.7 -> C-
    assert module_0.numerical_letter_grade([1.9, 1.8]) == ["C", "C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]

    # Just above 1.3 -> C-; exactly 1.3 -> D+
    assert module_0.numerical_letter_grade([1.5, 1.4]) == ["C-", "C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]

    # Just above 1.0 -> D+; exactly 1.0 -> D
    assert module_0.numerical_letter_grade([1.2, 1.1]) == ["D+", "D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]

    # Just above 0.7 -> D; exactly 0.7 -> D-
    assert module_0.numerical_letter_grade([0.9, 0.8]) == ["D", "D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]

    # Just above 0.0 -> D-
    assert module_0.numerical_letter_grade([0.3, 0.1]) == ["D-", "D-"]

    # Exactly 0.0 and negative values -> E
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-0.5, -2.0]) == ["E", "E"]

    # Empty list
    assert module_0.numerical_letter_grade([]) == []

    # Mixed list of all boundaries
    assert module_0.numerical_letter_grade([4.0, 3.0, 2.0, 1.0, 0.0]) == ["A+", "B", "C", "D", "E"]

    # Example cases
    assert module_0.numerical_letter_grade([1.5, 0.5]) == ["C-", "D-"]
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ["A+", "B", "C-", "C", "A-"]

    # Verify input list is not modified
    grades = [4.0, 2.0]
    module_0.numerical_letter_grade(grades)
    assert grades == [4.0, 2.0]

    print("All tests passed!")


test_numerical_letter_grade()

# Generated at 2026-11-02 21:42:45.160093
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # nonce:7612c721
    # Exact 4.0 maps to A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Values above 3.7 map to A
    assert module_0.numerical_letter_grade([3.8, 3.9, 3.71]) == ["A", "A", "A"]

    # Exactly 3.7 is NOT > 3.7, falls through to A-
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]

    # Values above 3.3 map to A-
    assert module_0.numerical_letter_grade([3.5, 3.4]) == ["A-", "A-"]

    # Exactly 3.3 -> B+
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]

    # Values above 3.0 map to B+
    assert module_0.numerical_letter_grade([3.2, 3.1]) == ["B+", "B+"]

    # Exactly 3.0 -> B
    assert module_0.numerical_letter_grade([3.0]) == ["B"]

    # Values above 2.7 map to B
    assert module_0.numerical_letter_grade([2.8, 2.9]) == ["B", "B"]

    # Exactly 2.7 -> B-
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]

    # Values above 2.3 map to B-
    assert module_0.numerical_letter_grade([2.5, 2.4]) == ["B-", "B-"]

    # Exactly 2.3 -> C+
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]

    # Values above 2.0 map to C+
    assert module_0.numerical_letter_grade([2.1, 2.2]) == ["C+", "C+"]

    # Exactly 2.0 -> C
    assert module_0.numerical_letter_grade([2.0]) == ["C"]

    # Values above 1.7 map to C
    assert module_0.numerical_letter_grade([1.8, 1.9]) == ["C", "C"]

    # Exactly 1.7 -> C-
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]

    # Values above 1.3 map to C-
    assert module_0.numerical_letter_grade([1.5, 1.4]) == ["C-", "C-"]

    # Exactly 1.3 -> D+
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]

    # Values above 1.0 map to D+
    assert module_0.numerical_letter_grade([1.1, 1.2]) == ["D+", "D+"]

    # Exactly 1.0 -> D
    assert module_0.numerical_letter_grade([1.0]) == ["D"]

    # Values above 0.7 map to D
    assert module_0.numerical_letter_grade([0.8, 0.9]) == ["D", "D"]

    # Exactly 0.7 -> D-
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]

    # Values above 0.0 map to D-
    assert module_0.numerical_letter_grade([0.3, 0.1]) == ["D-", "D-"]

    # Zero and negative values map to E
    assert module_0.numerical_letter_grade([0.0, -0.5, -2.0]) == ["E", "E", "E"]

    # Mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 0.0]) == ["A+", "B", "C-", "E"]

    # Empty input returns empty list
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-11-02 21:44:52.839219
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact boundary values
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]

    # Values just above thresholds
    assert module_0.numerical_letter_grade([3.85]) == ["A"]
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([2.85]) == ["B"]
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    assert module_0.numerical_letter_grade([1.85]) == ["C"]
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([0.85]) == ["D"]
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]

    # Zero and negative GPAs map to "E"
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]
    assert module_0.numerical_letter_grade([0.0, -1.0, -2.5]) == ["E", "E", "E"]

    # Mixed list preserves order
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 0.0]) == ["A+", "B", "C-", "E"]

    # Typical example
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']

    # Empty input
    assert module_0.numerical_letter_grade([]) == []

    print("All tests passed!")


test_numerical_letter_grade()