

# Generated at 2026-11-02 12:25:41.563336
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():# Test boundary values for each grade tier
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.7]) == ["A"]
    assert module_0.numerical_letter_grade([3.6]) == ["A"]
    assert module_0.numerical_letter_grade([3.3]) == ["A-"]
    assert module_0.numerical_letter_grade([3.2]) == ["A-"]
    assert module_0.numerical_letter_grade([3.0]) == ["B+"]
    assert module_0.numerical_letter_grade([2.9]) == ["B+"]
    assert module_0.numerical_letter_grade([2.7]) == ["B"]
    assert module_0.numerical_letter_grade([2.6]) == ["B"]
    assert module_0.numerical_letter_grade([2.3]) == ["B-"]
    assert module_0.numerical_letter_grade([2.2]) == ["B-"]
    assert module_0.numerical_letter_grade([2.0]) == ["C+"]
    assert module_0.numerical_letter_grade([1.9]) == ["C+"]
    assert module_0.numerical_letter_grade([1.7]) == ["C"]
    assert module_0.numerical_letter_grade([1.6]) == ["C"]
    assert module_0.numerical_letter_grade([1.3]) == ["C-"]
    assert module_0.numerical_letter_grade([1.2]) == ["C-"]
    assert module_0.numerical_letter_grade([1.0]) == ["D+"]
    assert module_0.numerical_letter_grade([0.9]) == ["D+"]
    assert module_0.numerical_letter_grade([0.7]) == ["D"]
    assert module_0.numerical_letter_grade([0.6]) == ["D"]
    assert module_0.numerical_letter_grade([0.1]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]

    # Test a mixed list of GPAs
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ["A+", "B+", "C", "C+", "A-"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test all grades in one list
    assert module_0.numerical_letter_grade(
        [4.0, 3.8, 3.5, 3.1, 2.8, 2.5, 2.1, 1.8, 1.5, 1.1, 0.8, 0.3, 0.0]
    ) == ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

# Generated at 2026-11-02 12:27:04.047579
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Exact 4.0
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # A range (> 3.7)
    assert module_0.numerical_letter_grade([3.8, 3.9, 3.95]) == ["A", "A", "A"]

    # A- range (> 3.3)
    assert module_0.numerical_letter_grade([3.7, 3.5, 3.4]) == ["A-", "A-", "A-"]

    # B+ range (> 3.0)
    assert module_0.numerical_letter_grade([3.3, 3.1]) == ["B+", "B+"]

    # B range (> 2.7)
    assert module_0.numerical_letter_grade([3.0, 2.8]) == ["B", "B"]

    # B- range (> 2.3)
    assert module_0.numerical_letter_grade([2.7, 2.4]) == ["B-", "B-"]

    # C+ range (> 2.0)
    assert module_0.numerical_letter_grade([2.3, 2.1]) == ["C+", "C+"]

    # C range (> 1.7)
    assert module_0.numerical_letter_grade([2.0, 1.8]) == ["C", "C"]

    # C- range (> 1.3)
    assert module_0.numerical_letter_grade([1.7, 1.4]) == ["C-", "C-"]

    # D+ range (> 1.0)
    assert module_0.numerical_letter_grade([1.3, 1.1]) == ["D+", "D+"]

    # D range (> 0.7)
    assert module_0.numerical_letter_grade([1.0, 0.8]) == ["D", "D"]

    # D- range (> 0.0)
    assert module_0.numerical_letter_grade([0.7, 0.3]) == ["D-", "D-"]

    # E range (<= 0.0)
    assert module_0.numerical_letter_grade([0.0, -1.5]) == ["E", "E"]

    # Mixed input
    assert module_0.numerical_letter_grade([4.0, 3.5, 2.0, 0.0]) == ["A+", "A-", "C", "E"]

    # Empty input
    assert module_0.numerical_letter_grade([]) == []

# Generated at 2026-11-02 12:27:53.670907
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test exact boundary: 4.0 -> A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]

    # Test values just above thresholds
    assert module_0.numerical_letter_grade([3.9]) == ["A"]
    assert module_0.numerical_letter_grade([3.75]) == ["A"]
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
    assert module_0.numerical_letter_grade([0.1]) == ["D-"]

    # Test zero and below -> E
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]

    # Test mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 3.0]) == ["A+", "B", "C-", "B"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test a full range example
    assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.2, 1.9, 1.5, 1.2, 0.9, 0.5, 0.0]) == [
        "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"
    ]

    print("All tests passed!")


# Run tests
if __name__ == "__main__":
    test_numerical_letter_grade()

# Generated at 2026-11-02 12:28:53.563076
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test A+ (exactly 4.0)
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([4.0, 4.0]) == ["A+", "A+"]

    # Test A (gpa > 3.7, but not 4.0)
    assert module_0.numerical_letter_grade([3.9]) == ["A"]
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.75]) == ["A"]
    assert module_0.numerical_letter_grade([3.71]) == ["A"]

    # Test A- (gpa > 3.3, up to and including 3.7)
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]
    assert module_0.numerical_letter_grade([3.5]) == ["A-"]
    assert module_0.numerical_letter_grade([3.31]) == ["A-"]

    # Test B+ (gpa > 3.0, up to and including 3.3)
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([3.01]) == ["B+"]

    # Test B (gpa > 2.7, up to and including 3.0)
    assert module_0.numerical_letter_grade([3.0]) == ["B"]
    assert module_0.numerical_letter_grade([2.8]) == ["B"]
    assert module_0.numerical_letter_grade([2.71]) == ["B"]

    # Test B- (gpa > 2.3, up to and including 2.7)
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]
    assert module_0.numerical_letter_grade([2.5]) == ["B-"]
    assert module_0.numerical_letter_grade([2.31]) == ["B-"]

    # Test C+ (gpa > 2.0, up to and including 2.3)
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]
    assert module_0.numerical_letter_grade([2.1]) == ["C+"]
    assert module_0.numerical_letter_grade([2.01]) == ["C+"]

    # Test C (gpa > 1.7, up to and including 2.0)
    assert module_0.numerical_letter_grade([2.0]) == ["C"]
    assert module_0.numerical_letter_grade([1.8]) == ["C"]
    assert module_0.numerical_letter_grade([1.71]) == ["C"]

    # Test C- (gpa > 1.3, up to and including 1.7)
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]
    assert module_0.numerical_letter_grade([1.5]) == ["C-"]
    assert module_0.numerical_letter_grade([1.31]) == ["C-"]

    # Test D+ (gpa > 1.0, up to and including 1.3)
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([1.01]) == ["D+"]

    # Test D (gpa > 0.7, up to and including 1.0)
    assert module_0.numerical_letter_grade([1.0]) == ["D"]
    assert module_0.numerical_letter_grade([0.8]) == ["D"]
    assert module_0.numerical_letter_grade([0.71]) == ["D"]

    # Test D- (gpa > 0.0, up to and including 0.7)
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]
    assert module_0.numerical_letter_grade([0.5]) == ["D-"]
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]
    assert module_0.numerical_letter_grade([0.01]) == ["D-"]

    # Test E (gpa == 0.0 or negative)
    assert module_0.numerical_letter_grade([0.0]) == ["E"]
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]
    assert module_0.numerical_letter_grade([-2.0]) == ["E"]

    # Test mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 3.5]) == ["A+", "B", "C-", "A-"]
    assert module_0.numerical_letter_grade([1.0, 0.7, 0.0, 2.0]) == ["D", "D-", "E", "C"]
    assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.2, 1.9, 1.5, 1.2, 0.9, 0.5, 0.0]) == \
        ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test that boundary values are strictly exclusive (e.g., 3.7 is A-, not A)
    assert module_0.numerical_letter_grade([3.7, 2.7, 1.7, 0.7]) == ["A-", "B-", "C-", "D-"]

    print("All tests passed!")


# Run tests
if __name__ == "__main__":
    test_numerical_letter_grade()

# Generated at 2026-11-02 12:30:20.787497
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():import unittest


class TestNumericalLetterGrade(unittest.TestCase):

    def test_typical_values(self):
        self.assertEqual(module_0.numerical_letter_grade([4.0, 3.0, 1.7, 2.0, 0.5]),
                         ["A+", "B-", "C-", "C", "D-"])

    def test_exact_boundaries(self):
        self.assertEqual(module_0.numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7, 2.3,
                                                 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]),
                         ["A+", "A-", "B", "B-", "C+", "C",
                          "C-", "D+", "D", "D-", "E", "E"])

    def test_just_above_boundaries(self):
        self.assertEqual(module_0.numerical_letter_grade([3.85, 3.5, 3.1, 2.85, 2.5,
                                                 2.1, 1.85, 1.5, 1.1, 0.85, 0.3]),
                         ["A", "A-", "B+", "B", "B-", "C+",
                          "C", "C-", "D+", "D", "D-"])

    def test_zero_and_negative(self):
        self.assertEqual(module_0.numerical_letter_grade([0.0, -0.2, -1.0]),
                         ["E", "E", "E"])

    def test_empty_list(self):
        self.assertEqual(module_0.numerical_letter_grade([]), [])

    def test_single_value(self):
        self.assertEqual(module_0.numerical_letter_grade([4.0]), ["A+"])
        self.assertEqual(module_0.numerical_letter_grade([2.5]), ["B-"])

    def test_result_length_matches_input(self):
        grades = [4.0, 3.9, 3.5, 3.2, 2.9, 2.4, 1.9, 1.4, 0.9, 0.4, 0.0]
        result = module_0.numerical_letter_grade(grades)
        self.assertEqual(len(result), len(grades))


if __name__ == "__main__":
    unittest.main()