

# Generated at 2026-11-02 09:21:11.688205
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test exact boundary: 4.0 -> A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    # Test values just above thresholds
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.2]) == ["B+"]
    assert module_0.numerical_letter_grade([2.9]) == ["B"]
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.2]) == ["C+"]
    assert module_0.numerical_letter_grade([1.9]) == ["C"]
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.2]) == ["D+"]
    assert module_0.numerical_letter_grade([0.8]) == ["D"]
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]
    # Test zero and negative values -> E
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]
    # Test empty list
    assert module_0.numerical_letter_grade([]) == []
    # Test a mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 0.7]) == ["A+", "B", "C", "C+", "D"]
    # Test boundary values just at threshold (should fall to lower tier)
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]
    # Test full range sample
    assert module_0.numerical_letter_grade([2.0, 0.5, 3.5, 4.0, 1.0]) == ["C+", "D-", "A-", "A+", "D"]

# Generated at 2026-11-02 09:23:38.533904
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test boundary values for each grade
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.9]) == ["A"]
    assert module_0.numerical_letter_grade([3.7]) == ["A"]
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["A-"]
    assert module_0.numerical_letter_grade([3.2]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B+"]
    assert module_0.numerical_letter_grade([2.9]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B"]
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["B-"]
    assert module_0.numerical_letter_grade([2.2]) == ["C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C+"]
    assert module_0.numerical_letter_grade([1.9]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C"]
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["C-"]
    assert module_0.numerical_letter_grade([1.2]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D+"]
    assert module_0.numerical_letter_grade([0.9]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D"]
    assert module_0.numerical_letter_grade([0.5]) == ["D-"]
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]

    # Test multiple values at once
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 0.0]) == ["A+", "B+", "C", "C+", "E"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test non-integer GPAs
    assert module_0.numerical_letter_grade([3.85, 2.45, 1.05, 0.75]) == ["A", "B-", "D+", "D"]

    print("All tests passed!")


# Run tests
test_numerical_letter_grade()

# Generated at 2026-11-02 09:26:25.456847
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test all grade boundaries
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.9, 3.85]) == ["A", "A"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]
    assert module_0.numerical_letter_grade([2.9]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C"]
    assert module_0.numerical_letter_grade([1.9]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]
    assert module_0.numerical_letter_grade([0.9]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]
    assert module_0.numerical_letter_grade([0.5]) == ["D-"]
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-1.0]) == ["E"]

    # Test a mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 3.5]) == ["A+", "B", "C-", "C", "A-"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test example from typical spec
    assert module_0.numerical_letter_grade([1.5, 0.5]) == ["C-", "D-"]

    print("All tests passed!")


test_numerical_letter_grade()

# Generated at 2026-11-02 09:28:33.242154
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact boundary: 4.0 -> A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    # Just above 3.7 -> A
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.75]) == ["A"]
    # Just above 3.3 -> A-
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.31]) == ["A-"]
    # Just above 3.0 -> B+
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    # Just above 2.7 -> B
    assert module_0.numerical_letter_grade([2.8]) == ["B"]
    # Just above 2.3 -> B-
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    # Just above 2.0 -> C+
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    # Just above 1.7 -> C
    assert module_0.numerical_letter_grade([1.8]) == ["C"]
    # Just above 1.3 -> C-
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    # Just above 1.0 -> D+
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    # Just above 0.7 -> D
    assert module_0.numerical_letter_grade([0.8]) == ["D"]
    # Just above 0.0 -> D-
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]
    # Zero and below -> E
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]

    # Boundary values that fall into lower bucket (not strictly greater)
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

    # Mixed list preserves order and maps each value correctly
    assert module_0.numerical_letter_grade([4.0, 3.0, 2.0, 1.0, 0.0]) == ["A+", "B", "C", "D", "E"]
    assert module_0.numerical_letter_grade([3.9, 2.5, 1.5, 0.2]) == ["A", "B-", "C-", "D-"]

    # Empty input returns empty list
    assert module_0.numerical_letter_grade([]) == []

    # Result length matches input length
    grades = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
    result = module_0.numerical_letter_grade(grades)
    assert len(result) == len(grades)
    assert result == ["A+", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    print("All tests passed!")


test_numerical_letter_grade()