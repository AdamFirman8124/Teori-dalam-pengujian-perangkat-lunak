

# Generated at 2026-11-02 19:05:02.279618
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test exact GPA values and boundaries
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.9]) == ["A"]
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
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
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-1.0]) == ["E"]

    # Test a mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 0.5, 0.3]) == [
        "A+", "B", "C-", "C", "D-", "D-"
    ]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test that the function returns a list
    assert isinstance(module_0.numerical_letter_grade([2.0]), list)

# Generated at 2026-11-02 19:06:02.105066
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test exact boundary: 4.0 gives A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Test just above 3.7 gives A, exactly 3.7 gives A-
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]

    # Test just above 3.3 gives A-, exactly 3.3 gives B+
    assert module_0.numerical_letter_grade([3.4]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]

    # Test just above 3.0 gives B+, exactly 3.0 gives B
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]

    # Test just above 2.7 gives B, exactly 2.7 gives B-
    assert module_0.numerical_letter_grade([2.8]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]

    # Test just above 2.3 gives B-, exactly 2.3 gives C+
    assert module_0.numerical_letter_grade([2.4]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]

    # Test just above 2.0 gives C+, exactly 2.0 gives C
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C"]

    # Test just above 1.7 gives C, exactly 1.7 gives C-
    assert module_0.numerical_letter_grade([1.8]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]

    # Test just above 1.3 gives C-, exactly 1.3 gives D+
    assert module_0.numerical_letter_grade([1.4]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]

    # Test just above 1.0 gives D+, exactly 1.0 gives D
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]

    # Test just above 0.7 gives D, exactly 0.7 gives D-
    assert module_0.numerical_letter_grade([0.8]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]

    # Test just above 0.0 gives D-, exactly 0.0 gives E
    assert module_0.numerical_letter_grade([0.1]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]

    # Test negative GPA gives E
    assert module_0.numerical_letter_grade([-1.0]) == ["E"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test multiple grades at once
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ["A+", "B", "C-", "C", "A-"]

    # Test full range of grades in one call
    assert module_0.numerical_letter_grade(
        [4.0, 3.8, 3.4, 3.1, 2.8, 2.4, 2.1, 1.8, 1.4, 1.1, 0.8, 0.1, 0.0]
    ) == ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]


def test_numerical_letter_grade_empty():
    assert module_0.numerical_letter_grade([]) == []


def test_numerical_letter_grade_single_values():
    assert module_0.numerical_letter_grade([3.95]) == ["A"]
    assert module_0.numerical_letter_grade([2.05]) == ["C+"]
    assert module_0.numerical_letter_grade([0.5]) == ["D-"]
    assert module_0.numerical_letter_grade([-2.5]) == ["E"]

# Generated at 2026-11-02 19:07:42.448912
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test with a typical mix of grades
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']

    # Test exact boundary values
    assert module_0.numerical_letter_grade([4.0]) == ['A+']
    assert module_0.numerical_letter_grade([3.9]) == ['A']
    assert module_0.numerical_letter_grade([3.8]) == ['A']
    assert module_0.numerical_letter_grade([3.7]) == ['A-']
    assert module_0.numerical_letter_grade([3.4]) == ['A-']
    assert module_0.numerical_letter_grade([3.3]) == ['B+']
    assert module_0.numerical_letter_grade([3.1]) == ['B+']
    assert module_0.numerical_letter_grade([3.0]) == ['B']
    assert module_0.numerical_letter_grade([2.8]) == ['B']
    assert module_0.numerical_letter_grade([2.7]) == ['B-']
    assert module_0.numerical_letter_grade([2.4]) == ['B-']
    assert module_0.numerical_letter_grade([2.3]) == ['C+']
    assert module_0.numerical_letter_grade([2.1]) == ['C+']
    assert module_0.numerical_letter_grade([2.0]) == ['C']
    assert module_0.numerical_letter_grade([1.8]) == ['C']
    assert module_0.numerical_letter_grade([1.7]) == ['C-']
    assert module_0.numerical_letter_grade([1.4]) == ['C-']
    assert module_0.numerical_letter_grade([1.3]) == ['D+']
    assert module_0.numerical_letter_grade([1.1]) == ['D+']
    assert module_0.numerical_letter_grade([1.0]) == ['D']
    assert module_0.numerical_letter_grade([0.8]) == ['D']
    assert module_0.numerical_letter_grade([0.7]) == ['D-']
    assert module_0.numerical_letter_grade([0.3]) == ['D-']
    assert module_0.numerical_letter_grade([0.0]) == ['E']

    # Test failing grade
    assert module_0.numerical_letter_grade([0]) == ['E']

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test multiple values at once
    assert module_0.numerical_letter_grade([0.0, 0.5, 1.5, 2.5, 3.5, 4.0]) == [
        'E', 'D-', 'C-', 'B-', 'A-', 'A+'
    ]

# Generated at 2026-11-02 19:10:02.866928
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # nonce:986d9ebf
    # Canonical example from the specification
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']

    # Exact boundary values (a boundary itself falls into the lower grade)
    assert numerical

# Generated at 2026-11-02 19:12:06.912293
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test exact 4.0 -> "A+"
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Test boundary value just above 3.7 -> "A"
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]

    # Test boundary value just above 3.3 -> "A-"
    assert module_0.numerical_letter_grade([3.4]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]

    # Test boundary value just above 3.0 -> "B+"
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]

    # Test boundary value just above 2.7 -> "B"
    assert module_0.numerical_letter_grade([2.8]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]

    # Test boundary value just above 2.3 -> "B-"
    assert module_0.numerical_letter_grade([2.4]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]

    # Test boundary value just above 2.0 -> "C+"
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    assert module_0.numerical_letter_grade([2.0]) == ["C"]

    # Test boundary value just above 1.7 -> "C"
    assert module_0.numerical_letter_grade([1.8]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]

    # Test boundary value just above 1.3 -> "C-"
    assert module_0.numerical_letter_grade([1.4]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]

    # Test boundary value just above 1.0 -> "D+"
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]

    # Test boundary value just above 0.7 -> "D"
    assert module_0.numerical_letter_grade([0.8]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]

    # Test boundary value just above 0.0 -> "D-"
    assert module_0.numerical_letter_grade([0.1]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]

    # Test negative value -> "E"
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]
    assert module_0.numerical_letter_grade([-2.0]) == ["E"]

    # Test multiple values in one call
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 0.0]) == ["A+", "B", "C-", "E"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test typical mixed list (common example)
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ["A+", "B", "C-", "C", "A-"]

    print("All tests passed!")


# Run the tests
test_numerical_letter_grade()