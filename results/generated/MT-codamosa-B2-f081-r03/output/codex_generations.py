

# Generated at 2026-11-02 21:04:22.282188
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Standard examples covering every grade bucket
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 3.5]) == ["A+", "B-", "C-", "C", "A-"]

    # Boundary checks around each threshold
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]          # exactly 4.0
    assert module_0.numerical_letter_grade([3.8]) == ["A"]           # > 3.7
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]          # not > 3.7
    assert module_0.numerical_letter_grade([3.4]) == ["A-"]          # > 3.3
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]          # not > 3.3
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]          # > 3.0
    assert module_0.numerical_letter_grade([3.0]) == ["B-"]          # not > 3.0
    assert module_0.numerical_letter_grade([2.8]) == ["B"]           # > 2.7
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]          # not > 2.7
    assert module_0.numerical_letter_grade([2.4]) == ["B-"]          # > 2.3
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]          # not > 2.3
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]          # > 2.0
    assert module_0.numerical_letter_grade([2.0]) == ["C"]           # not > 2.0
    assert module_0.numerical_letter_grade([1.8]) == ["C"]           # > 1.7
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]          # not > 1.7
    assert module_0.numerical_letter_grade([1.4]) == ["C-"]          # > 1.3
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]          # not > 1.3
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]          # > 1.0
    assert module_0.numerical_letter_grade([1.0]) == ["D"]           # not > 1.0
    assert module_0.numerical_letter_grade([0.8]) == ["D"]           # > 0.7
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]          # not > 0.7
    assert module_0.numerical_letter_grade([0.1]) == ["D-"]          # > 0.0
    assert module_0.numerical_letter_grade([0.0]) == ["E"]           # zero
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]          # negative

    # Empty input
    assert module_0.numerical_letter_grade([]) == []

    # Mixed list with repeated values preserves order
    assert module_0.numerical_letter_grade([0.0, 3.9, 2.5, 3.9]) == ["E", "A", "B-", "A"]

    print("All tests passed!")

# Generated at 2026-11-02 21:04:57.327802
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test individual grade boundaries
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.9]) == ["A"]
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]  # exactly 3.7 is not > 3.7
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]  # exactly 3.3 is not > 3.3
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]   # exactly 3.0 is not > 3.0
    assert module_0.numerical_letter_grade([2.9]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]  # exactly 2.7 is not > 2.7
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]  # exactly 2.3 is not > 2.3
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C"]   # exactly 2.0 is not > 2.0
    assert module_0.numerical_letter_grade([1.9]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]  # exactly 1.7 is not > 1.7
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]  # exactly 1.3 is not > 1.3
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]   # exactly 1.0 is not > 1.0
    assert module_0.numerical_letter_grade([0.9]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]  # exactly 0.7 is not > 0.7
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]

    # Test multiple grades in one call
    assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.0, 2.5, 1.5, 0.0]) == \
        ["A+", "A", "A-", "B", "B-", "C-", "E"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test all grades at once
    grades = [4.0, 3.9, 3.7, 3.5, 3.3, 3.1, 3.0, 2.9, 2.7, 2.5,
              2.3, 2.1, 2.0, 1.9, 1.7, 1.5, 1.3, 1.1, 1.0, 0.9, 0.7, 0.3, 0.0]
    expected = ["A+", "A", "A-", "A-", "B+", "B+", "B", "B", "B-", "B-",
                "C+", "C+", "C", "C", "C-", "C-", "D+", "D+", "D", "D", "D-", "D-", "E"]
    assert module_0.numerical_letter_grade(grades) == expected

    # Verify result is a list
    assert isinstance(module_0.numerical_letter_grade([3.0]), list)

    print("All tests passed!")


test_numerical_letter_grade()

# Generated at 2026-11-02 21:06:13.863658
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # nonce:9fa67afa

    # Test each grade boundary and category
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.9]) == ["A"]
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.75]) == ["A"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.4]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]
    assert module_0.numerical_letter_grade([3.2]) == ["B+"]
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]
    assert module_0.numerical_letter_grade([2.9]) == ["B"]
    assert module_0.numerical_letter_grade([2.8]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.4]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]
    assert module_0.numerical_letter_grade([2.2]) == ["C+"]
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C"]
    assert module_0.numerical_letter_grade([1.9]) == ["C"]
    assert module_0.numerical_letter_grade([1.8]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.4]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]
    assert module_0.numerical_letter_grade([1.2]) == ["D+"]
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]
    assert module_0.numerical_letter_grade([0.9]) == ["D"]
    assert module_0.numerical_letter_grade([0.8]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]
    assert module_0.numerical_letter_grade([0.5]) == ["D-"]
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]
    assert module_0.numerical_letter_grade([0.1]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]
    assert module_0.numerical_letter_grade([-2.0]) == ["E"]

    # Test multiple values in a single call (order preserved)
    assert module_0.numerical_letter_grade([4.0, 3.0, 2.0, 1.0, 0.0]) == ["A+", "B", "C", "D", "E"]
    assert module_0.numerical_letter_grade([3.8, 3.4, 2.9, 2.4, 1.9, 1.4, 0.9, 0.4]) == \
        ["A", "A-", "B", "B-", "C", "C-", "D", "D-"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test floating point precision edge cases
    assert module_0.numerical_letter_grade([3.7000001]) == ["A"]
    assert module_0.numerical_letter_grade([2.7000001]) == ["B"]
    assert module_0.numerical_letter_grade([0.0000001]) == ["D-"]

    print("All tests passed!")

# Generated at 2026-11-02 21:07:24.679353
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    unittest.main(argv=["first-arg-is-ignored"], exit=False)


if __name__ == "__main__":
    test_numerical_letter_grade()

# Generated at 2026-11-02 21:08:37.809032
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test exact 4.0 -> A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Test values just above each threshold
    assert module_0.numerical_letter_grade([3.9]) == ["A"]
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([2.9]) == ["B"]
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    assert module_0.numerical_letter_grade([1.9]) == ["C"]
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([0.9]) == ["D"]
    assert module_0.numerical_letter_grade([0.5]) == ["D-"]

    # Test boundary values (exactly on threshold, not strictly greater)
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

    # Test zero and below -> E
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]

    # Test a mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 3.5]) == ["A+", "B", "C-", "C", "A-"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test all grade levels in one list
    assert module_0.numerical_letter_grade(
        [4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.5, 0.0]
    ) == ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    print("All tests passed!")


if __name__ == "__main__":
    test_numerical_letter_grade()