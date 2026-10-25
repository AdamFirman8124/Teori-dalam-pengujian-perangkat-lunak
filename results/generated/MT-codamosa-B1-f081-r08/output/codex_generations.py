

# Generated at 2026-10-24 11:04:08.758567
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 11:04:11.506565
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 11:04:13.923149
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 11:04:16.344112
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 11:04:18.768441
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 11:04:21.191671
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 11:04:23.614186
# Unit test for function numerical_letter_grade

# Generated at 2026-10-24 11:04:52.666817
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 3.5]) == ['A+', 'B-', 'C-', 'C', 'A-']
    assert module_0.numerical_letter_grade([1.5]) == ['C-']
    assert module_0.numerical_letter_grade([0.0]) == ['E']
    assert module_0.numerical_letter_grade([0.7]) == ['D-']
    assert module_0.numerical_letter_grade([3.6]) == ['A-']
    assert module_0.numerical_letter_grade([3.7]) == ['A-']
    assert module_0.numerical_letter_grade([2.5]) == ['B-']
    assert module_0.numerical_letter_grade([1.0]) == ['D-']
    assert module_0.numerical_letter_grade([2.0]) == ['C-']
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 11:04:53.992689
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Top grade
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # One value in each band
    assert module_0.numerical_letter_grade(
        [3.9, 3.5, 3.1, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.5]
    ) == ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]

    # Boundaries fall into the lower band
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
    ) == ["A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    # Failing and empty input
    assert module_0.numerical_letter_grade([0.0, -1.0]) == ["E", "E"]
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-10-24 11:05:10.412626
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Top grade
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # One value in each band
    assert module_0.numerical_letter_grade(
        [3.9, 3.5, 3.1, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.5]
    ) == ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]

    # Boundaries fall into the lower band
    assert module_0.numerical_letter_grade(
        [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
    ) == ["A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    # Failing and empty input
    assert module_0.numerical_letter_grade([0.0, -1.0]) == ["E", "E"]
    assert module_0.numerical_letter_grade([]) == []