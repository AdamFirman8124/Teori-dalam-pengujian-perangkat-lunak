

# Generated at 2026-10-25 05:25:52.473775
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact 4.0 is the only A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Boundary values fall into the LOWER bucket (strict > comparisons)
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

    # Just above each boundary goes to the higher letter
    assert module_0.numerical_letter_grade([3.71]) == ["A"]
    assert module_0.numerical_letter_grade([3.69]) == ["A-"]
    assert module_0.numerical_letter_grade([0.01]) == ["D-"]
    assert module_0.numerical_letter_grade([-1.0]) == ["E"]  # negatives -> E

    # Order preserved, one output per input
    assert module_0.numerical_letter_grade([4.0, 3.5, 2.5, 1.5, 0.5]) == [
        "A+", "A-", "B-", "D+", "D-",
    ]

    # Empty input
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-25 05:25:53.876795
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact 4.0 is the only A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Boundary values fall into the LOWER bucket (strict > comparisons)
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

    # Just above each boundary goes to the higher letter
    assert module_0.numerical_letter_grade([3.71]) == ["A"]
    assert module_0.numerical_letter_grade([3.69]) == ["A-"]
    assert module_0.numerical_letter_grade([0.01]) == ["D-"]
    assert module_0.numerical_letter_grade([-1.0]) == ["E"]  # negatives -> E

    # Order preserved, one output per input
    assert module_0.numerical_letter_grade([4.0, 3.5, 2.5, 1.5, 0.5]) == [
        "A+", "A-", "B-", "D+", "D-",
    ]

    # Empty input
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-25 05:25:55.341803
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact 4.0 is the only A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Boundary values fall into the LOWER bucket (strict > comparisons)
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

    # Just above each boundary goes to the higher letter
    assert module_0.numerical_letter_grade([3.71]) == ["A"]
    assert module_0.numerical_letter_grade([3.69]) == ["A-"]
    assert module_0.numerical_letter_grade([0.01]) == ["D-"]
    assert module_0.numerical_letter_grade([-1.0]) == ["E"]  # negatives -> E

    # Order preserved, one output per input
    assert module_0.numerical_letter_grade([4.0, 3.5, 2.5, 1.5, 0.5]) == [
        "A+", "A-", "B-", "D+", "D-",
    ]

    # Empty input
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-25 05:25:56.781659
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact 4.0 is the only A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Boundary values fall into the LOWER bucket (strict > comparisons)
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

    # Just above each boundary goes to the higher letter
    assert module_0.numerical_letter_grade([3.71]) == ["A"]
    assert module_0.numerical_letter_grade([3.69]) == ["A-"]
    assert module_0.numerical_letter_grade([0.01]) == ["D-"]
    assert module_0.numerical_letter_grade([-1.0]) == ["E"]  # negatives -> E

    # Order preserved, one output per input
    assert module_0.numerical_letter_grade([4.0, 3.5, 2.5, 1.5, 0.5]) == [
        "A+", "A-", "B-", "D+", "D-",
    ]

    # Empty input
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-25 05:25:58.134414
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact 4.0 is the only A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Boundary values fall into the LOWER bucket (strict > comparisons)
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

    # Just above each boundary goes to the higher letter
    assert module_0.numerical_letter_grade([3.71]) == ["A"]
    assert module_0.numerical_letter_grade([3.69]) == ["A-"]
    assert module_0.numerical_letter_grade([0.01]) == ["D-"]
    assert module_0.numerical_letter_grade([-1.0]) == ["E"]  # negatives -> E

    # Order preserved, one output per input
    assert module_0.numerical_letter_grade([4.0, 3.5, 2.5, 1.5, 0.5]) == [
        "A+", "A-", "B-", "D+", "D-",
    ]

    # Empty input
    assert module_0.numerical_letter_grade([]) == []