

# Generated at 2026-11-02 18:12:32.286415
# Unit test for function parse_music
def test_parse_music():
    # Test single whole note
    assert module_0.parse_music('o') == [4]

    # Test single half note
    assert module_0.parse_music('o|') == [2]

    # Test single quarter note
    assert module_0.parse_music('.|') == [1]

    # Test empty string
    assert module_0.parse_music('') == []

    # Test string with only spaces
    assert module_0.parse_music('   ') == []

    # Test multiple whole notes
    assert module_0.parse_music('o o o') == [4, 4, 4]

    # Test multiple half notes
    assert module_0.parse_music('o| o| o|') == [2, 2, 2]

    # Test multiple quarter notes
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # Test mixed notes
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Test the canonical example
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test string with leading/trailing spaces
    assert module_0.parse_music(' o .| ') == [4, 1]

    # Test string with consecutive spaces
    assert module_0.parse_music('o  .|') == [4, 1]

    # Test long sequence of alternating notes
    assert module_0.parse_music('o| .| o| .| o|') == [2, 1, 2, 1, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 18:13:12.087692
# Unit test for function parse_music
def test_parse_music():
    # Empty string returns empty list
    assert module_0.parse_music('') == []

    # Single notes
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Mixed notes
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Longer sequence
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Repeated identical notes
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]
    assert module_0.parse_music('o o o') == [4, 4, 4]

    # Extra whitespace is ignored (empty tokens filtered out)
    assert module_0.parse_music('o  o|') == [4, 2]
    assert module_0.parse_music('   o   ') == [4]

    # Leading/trailing whitespace only
    assert module_0.parse_music(' ') == []

    print("All parse_music tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 18:13:56.917847
# Unit test for function parse_music
def test_parse_music():
    # Test single note types
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Test multiple notes
    assert module_0.parse_music('o o| .|') == [4, 2, 1]
    assert module_0.parse_music('o| o| .| .|') == [2, 2, 1, 1]
    assert module_0.parse_music('o| .| o| .| o o o o') == [2, 1, 2, 1, 4, 4, 4, 4]

    # Test example sequence
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test empty string
    assert module_0.parse_music('') == []

    # Test string with extra spaces (should be ignored)
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    # Test repeated identical notes
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

# Generated at 2026-11-02 18:14:12.452701
# Unit test for function parse_music
def test_parse_music():
    from typing import List

    # Test with the classic example: whole, half, quarter notes mixed
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test with a single whole note
    assert module_0.parse_music('o') == [4]

    # Test with a single half note
    assert module_0.parse_music('o|') == [2]

    # Test with a single quarter note
    assert module_0.parse_music('.|') == [1]

    # Test with an empty string
    assert module_0.parse_music('') == []

    # Test with only spaces (should be treated as empty)
    assert module_0.parse_music('   ') == []

    # Test with multiple whole notes
    assert module_0.parse_music('o o o') == [4, 4, 4]

    # Test with multiple half notes
    assert module_0.parse_music('o| o| o|') == [2, 2, 2]

    # Test with multiple quarter notes
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]

    # Test with mixed notes in different order
    assert module_0.parse_music('.| o| o') == [1, 2, 4]

    # Test with trailing/leading spaces
    assert module_0.parse_music('  o  .|  ') == [4, 1]

    # Verify return type is a list
    assert isinstance(module_0.parse_music('o o|'), list)

    # Verify all elements are integers
    result = module_0.parse_music('o o| .|')
    assert all(isinstance(x, int) for x in result)

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 18:14:26.753372
# Unit test for function parse_music
def test_parse_music():
    # Test with a single whole note
    assert module_0.parse_music('o') == [4]

    # Test with a single half note
    assert module_0.parse_music('o|') == [2]

    # Test with a single quarter note
    assert module_0.parse_music('.|') == [1]

    # Test with a mixed sequence of notes
    assert module_0.parse_music('o o| .| o| o') == [4, 2, 1, 2, 4]

    # Test with multiple identical notes
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # Test with empty string
    assert module_0.parse_music('') == []

    # Test with string containing only spaces
    assert module_0.parse_music('   ') == []

    # Test with leading/trailing spaces
    assert module_0.parse_music(' o .| ') == [4, 1]

    # Test with a long mixed sequence
    assert module_0.parse_music('o o| o .| .| o|') == [4, 2, 4, 1, 1, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()