

# Generated at 2026-11-02 11:59:02.364511
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test with a typical mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.6]) == ['A+', 'B', 'C-', 'C', 'A-']

    # Test boundary and representative values
    assert module_0.numerical_letter_grade([4.0]) == ['A+']
    assert module_0.numerical_letter_grade([3.8]) == ['A']
    assert module_0.numerical_letter_grade([3.7]) == ['A-']
    assert module_0.numerical_letter_grade([3.4]) == ['A-']
    assert module_0.numerical_letter_grade([3.3]) == ['B+']
    assert module_0.numerical_letter_grade([3.0]) == ['B']
    assert module_0.numerical_letter_grade([2.7]) == ['B-']
    assert module_0.numerical_letter_grade([2.0]) == ['C']
    assert module_0.numerical_letter_grade([1.7]) == ['C-']
    assert module_0.numerical_letter_grade([1.0]) == ['D']
    assert module_0.numerical_letter_grade([0.7]) == ['D-']
    assert module_0.numerical_letter_grade([0.3]) == ['D-']
    assert module_0.numerical_letter_grade([0.0]) == ['E']

    # Test negative GPA falls into 'E'
    assert module_0.numerical_letter_grade([-0.5]) == ['E']

    # Test empty input
    assert module_0.numerical_letter_grade([]) == []

    # Test multiple values at once
    assert module_0.numerical_letter_grade([1.0, 0.7]) == ['D', 'D-']
    assert module_0.numerical_letter_grade([4.0, 3.8, 3.3, 2.7, 1.0, 0.0]) == ['A+', 'A', 'B+', 'B-', 'D', 'E']

# Generated at 2026-11-02 12:03:46.836457
# Unit test for function numerical_letter_grade

# Generated at 2026-11-02 12:04:53.168435
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.1, 1.9, 1.5, 1.2, 0.9, 0.5, 0.0]) == [
        "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"
    ]
    assert module_0.numerical_letter_grade([]) == []
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
    assert module_0.numerical_letter_grade([3.85, 2.45, 1.05]) == ["A", "B-", "D+"]
    assert module_0.numerical_letter_grade([0.0, 0.3, 4.0]) == ["E", "D-", "A+"]

# Generated at 2026-11-02 12:05:58.618540
# Unit test for function numerical_letter_grade

# Generated at 2026-11-02 12:06:27.217786
# Unit test for function numerical_letter_grade