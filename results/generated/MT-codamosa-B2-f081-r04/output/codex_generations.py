

# Generated at 2026-11-01 20:32:30.388873
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test exact boundary value 4.0 -> A+
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    # Test values just above boundaries
    assert module_0.numerical_letter_grade([3.9, 3.8, 3.75]) == ["A", "A", "A"]
    assert module_0.numerical_letter_grade([3.7, 3.5, 3.4]) == ["A-", "A-", "A-"]
    assert module_0.numerical_letter_grade([3.3, 3.2, 3.1]) == ["B+", "B+", "B+"]
    assert module_0.numerical_letter_grade([3.0, 2.9, 2.8]) == ["B", "B", "B"]
    assert module_0.numerical_letter_grade([2.7, 2.6, 2.4]) == ["B-", "B-", "B-"]
    assert module_0.numerical_letter_grade([2.3, 2.2, 2.1]) == ["C+", "C+", "C+"]
    assert module_0.numerical_letter_grade([2.0, 1.9, 1.8]) == ["C", "C", "C"]
    assert module_0.numerical_letter_grade([1.7, 1.6, 1.4]) == ["C-", "C-", "C-"]
    assert module_0.numerical_letter_grade([1.3, 1.2, 1.1]) == ["D+", "D+", "D+"]
    assert module_0.numerical_letter_grade([1.0, 0.9, 0.8]) == ["D", "D", "D"]
    assert module_0.numerical_letter_grade([0.7, 0.5, 0.1]) == ["D-", "D-", "D-"]
    # Test zero and negative values -> E
    assert module_0.numerical_letter_grade([0.0, -0.2, -1.0]) == ["E", "E", "E"]
    # Test mixed list
    assert module_0.numerical_letter_grade([4.0, 3.0, 1.7, 0.7, 0.0]) == ["A+", "B", "C-", "D", "E"]
    # Test empty list
    assert module_0.numerical_letter_grade([]) == []
    # Test that result length matches input length
    grades = [4.0, 3.5, 2.5, 1.5, 0.5, 0.0]
    result = module_0.numerical_letter_grade(grades)
    assert len(result) == len(grades)
    # Test full grading scale
    assert module_0.numerical_letter_grade([4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.2, 1.9, 1.5, 1.2, 0.9, 0.5, 0.0]) == [
        "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"
    ]
    print("All tests passed!")


test_numerical_letter_grade()

# Generated at 2026-11-01 20:32:52.200931
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test with typical example list
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']

    # Test each exact boundary value
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
    assert module_0.numerical_letter_grade([3.7]) == ["A-"]       # exactly 3.7 -> A-
    assert module_0.numerical_letter_grade([3.4]) == ["A-"]
    assert module_0.numerical_letter_grade([3.3]) == ["B+"]       # exactly 3.3 -> B+
    assert module_0.numerical_letter_grade([3.1]) == ["B+"]
    assert module_0.numerical_letter_grade([3.0]) == ["B"]        # exactly 3.0 -> B
    assert module_0.numerical_letter_grade([2.8]) == ["B"]
    assert module_0.numerical_letter_grade([2.7]) == ["B-"]       # exactly 2.7 -> B-
    assert module_0.numerical_letter_grade([2.4]) == ["B-"]
    assert module_0.numerical_letter_grade([2.3]) == ["C+"]       # exactly 2.3 -> C+
    assert module_0.numerical_letter_grade([2.0]) == ["C"]        # exactly 2.0 -> C
    assert module_0.numerical_letter_grade([1.8]) == ["C"]
    assert module_0.numerical_letter_grade([1.7]) == ["C-"]       # exactly 1.7 -> C-
    assert module_0.numerical_letter_grade([1.4]) == ["C-"]
    assert module_0.numerical_letter_grade([1.3]) == ["D+"]       # exactly 1.3 -> D+
    assert module_0.numerical_letter_grade([1.1]) == ["D+"]
    assert module_0.numerical_letter_grade([1.0]) == ["D"]        # exactly 1.0 -> D
    assert module_0.numerical_letter_grade([0.8]) == ["D"]
    assert module_0.numerical_letter_grade([0.7]) == ["D-"]       # exactly 0.7 -> D-
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]        # zero -> E
    assert module_0.numerical_letter_grade([-0.5]) == ["E"]       # negative -> E

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test mixed list including edge and failing grades
    assert module_0.numerical_letter_grade([0.0, 0.7, 1.0, 2.0, 3.0, 4.0]) == [
        "E", "D-", "D", "C", "B", "A+"
    ]

    print("All tests passed!")


test_numerical_letter_grade()

# Generated at 2026-11-01 20:33:22.718382
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test exact boundary values
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

    # Test values just above boundaries
    assert module_0.numerical_letter_grade([3.8]) == ["A"]
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

    # Test multiple grades at once
    assert module_0.numerical_letter_grade([4.0, 3.0, 2.0, 1.0, 0.0]) == ["A+", "B", "C", "D", "E"]

    # Test empty list
    assert module_0.numerical_letter_grade([]) == []

    # Test full range example
    assert module_0.numerical_letter_grade([3.9, 3.5, 3.1, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.5, 0.0]) == [
        "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"
    ]

    print("All tests passed!")


test_numerical_letter_grade()

# Generated at 2026-11-01 20:33:49.036237
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
# nonce:35ad96ec
    # Test A+ (exactly 4.0)
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    
    # Test A (> 3.7 but not 4.0)
    assert module_0.numerical_letter_grade([3.9, 3.8, 3.71]) == ["A", "A", "A"]
    
    # Test A- (> 3.3 but <= 3.7)
    assert module_0.numerical_letter_grade([3.7, 3.5, 3.31]) == ["A-", "A-", "A-"]
    
    # Test B+ (> 3.0 but <= 3.3)
    assert module_0.numerical_letter_grade([3.3, 3.1, 3.01]) == ["B+", "B+", "B+"]
    
    # Test B (> 2.7 but <= 3.0)
    assert module_0.numerical_letter_grade([3.0, 2.9, 2.71]) == ["B", "B", "B"]
    
    # Test B- (> 2.3 but <= 2.7)
    assert module_0.numerical_letter_grade([2.7, 2.5, 2.31]) == ["B-", "B-", "B-"]
    
    # Test C+ (> 2.0 but <= 2.3)
    assert module_0.numerical_letter_grade([2.3, 2.1, 2.01]) == ["C+", "C+", "C+"]
    
    # Test C (> 1.7 but <= 2.0)
    assert module_0.numerical_letter_grade([2.0, 1.9, 1.71]) == ["C", "C", "C"]
    
    # Test C- (> 1.3 but <= 1.7)
    assert module_0.numerical_letter_grade([1.7, 1.5, 1.31]) == ["C-", "C-", "C-"]
    
    # Test D+ (> 1.0 but <= 1.3)
    assert module_0.numerical_letter_grade([1.3, 1.1, 1.01]) == ["D+", "D+", "D+"]
    
    # Test D (> 0.7 but <= 1.0)
    assert module_0.numerical_letter_grade([1.0, 0.9, 0.71]) == ["D", "D", "D"]
    
    # Test D- (> 0.0 but <= 0.7)
    assert module_0.numerical_letter_grade([0.7, 0.5, 0.1]) == ["D-", "D-", "D-"]
    
    # Test E (0.0 or below)
    assert module_0.numerical_letter_grade([0.0, -0.5]) == ["E", "E"]
    
    # Test mixed list of all grades
    assert module_0.numerical_letter_grade(
        [4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.5, 0.0]
    ) == ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    
    # Test empty list
    assert module_0.numerical_letter_grade([]) == []
    
    print("All tests passed!")


if __name__ == "__main__":
    test_numerical_letter_grade()

# Generated at 2026-11-01 20:34:11.354456
# Unit test for function numerical_letter_grade
def test_numerical_letter_grade():
    # Test case 1: Exact grade values matching the 4.0 scale
    assert module_0.numerical_letter_grade([4.0]) == ["A+"]
    assert module_0.numerical_letter_grade([3.7]) == ["A"]
    assert module_0.numerical_letter_grade([3.3]) == ["A-"]
    assert module_0.numerical_letter_grade([3.0]) == ["B+"]
    assert module_0.numerical_letter_grade([2.7]) == ["B"]
    assert module_0.numerical_letter_grade([2.3]) == ["B-"]
    assert module_0.numerical_letter_grade([2.0]) == ["C+"]
    assert module_0.numerical_letter_grade([1.7]) == ["C"]
    assert module_0.numerical_letter_grade([1.3]) == ["C-"]
    assert module_0.numerical_letter_grade([1.0]) == ["D+"]
    assert module_0.numerical_letter_grade([0.7]) == ["D"]
    assert module_0.numerical_letter_grade([0.0]) == ["E"]

    # Test case 2: Values just above the boundary thresholds
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
    assert module_0.numerical_letter_grade([0.3]) == ["D-"]

    # Test case 3: Failing/zero GPA
    assert module_0.numerical_letter_grade([0.0, -1.0]) == ["E", "E"]

    # Test case 4: Mixed list of grades
    assert module_0.numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ["A+", "B+", "C", "C+", "A-"]

    # Test case 5: Empty input
    assert module_0.numerical_letter_grade([]) == []

    # Test case 6: All grades at once
    input_grades = [4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.1, 1.9, 1.5, 1.1, 0.9, 0.5, 0.0]
    expected = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    assert module_0.numerical_letter_grade(input_grades) == expected

    print("All test cases passed!")


# Run the test
test_numerical_letter_grade()