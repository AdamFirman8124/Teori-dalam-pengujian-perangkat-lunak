

# Generated at 2026-11-02 11:09:52.018365
# Unit test for function parse_music
def test_parse_music():
    # Empty string returns an empty list
    assert module_0.parse_music('') == []

    # Single notes
    assert module_0.parse_music('o') == [4]      # whole note
    assert module_0.parse_music('o|') == [2]     # half note
    assert module_0.parse_music('.|') == [1]     # quarter note

    # All notes of one kind
    assert module_0.parse_music('o o o') == [4, 4, 4]
    assert module_0.parse_music('o| o| o|') == [2, 2, 2]
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]

    # Mixed notes (classic example)
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Repeated pattern with extra spaces between tokens handled via split
    assert module_0.parse_music('o .|') == [4, 1]
    assert module_0.parse_music('.| o| o') == [1, 2, 4]

    # Longer sequence
    assert module_0.parse_music('o o .| .| o| o|') == [4, 4, 1, 1, 2, 2]

    # Ensure result is a list of ints
    result = module_0.parse_music('o o| .|')
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

# Generated at 2026-11-02 11:11:51.775384
# Unit test for function parse_music
def test_parse_music():
    # Test the classic example: whole, half, quarter notes mix
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test a single whole note
    assert module_0.parse_music('o') == [4]

    # Test a single half note
    assert module_0.parse_music('o|') == [2]

    # Test a single quarter note
    assert module_0.parse_music('.|') == [1]

    # Test empty string returns empty list
    assert module_0.parse_music('') == []

    # Test string with only spaces returns empty list
    assert module_0.parse_music('   ') == []

    # Test repeated same notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # Test alternating notes
    assert module_0.parse_music('o| .| o| .|') == [2, 1, 2, 1]

    # Test extra spaces between notes are ignored
    assert module_0.parse_music('o  o|  .|') == [4, 2, 1]

    # Test leading/trailing spaces are ignored
    assert module_0.parse_music(' o .| ') == [4, 1]

    # Test result is a list of integers
    result = module_0.parse_music('o o|')
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 11:14:19.541440
# Unit test for function parse_music
def test_parse_music():
    # Single notes of each type
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Multiple notes of the same type
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]
    assert module_0.parse_music('o| o| o|') == [2, 2, 2]
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]

    # Mixed note types
    assert module_0.parse_music('o o| .|') == [4, 2, 1]
    assert module_0.parse_music('.| o| o') == [1, 2, 4]

    # Canonical example: melody with all note types
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Empty string yields empty list
    assert module_0.parse_music('') == []

    # Extra/leading/trailing whitespace is ignored due to empty-token filter
    assert module_0.parse_music('  o   .|  ') == [4, 1]
    assert module_0.parse_music(' ') == []

    # Alternating pattern
    assert module_0.parse_music('o .| o| o .|') == [4, 1, 2, 4, 1]

    print("All parse_music tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 11:16:41.880053
# Unit test for function parse_music
def test_parse_music():
    # Test with the classic mixed example
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test single notes of each type
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Test empty string returns empty list
    assert module_0.parse_music('') == []

    # Test string with only whitespace returns empty list
    assert module_0.parse_music('   ') == []

    # Test multiple identical notes
    assert module_0.parse_music('o o o') == [4, 4, 4]
    assert module_0.parse_music('o| o|') == [2, 2]
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # Test alternating pattern
    assert module_0.parse_music('o| .| o| .|') == [2, 1, 2, 1]

    # Test long sequence
    assert module_0.parse_music('.| .| o| o o| .| o') == [1, 1, 2, 4, 2, 1, 4]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 11:18:35.440333
# Unit test for function parse_music
def test_parse_music():
    # Test basic whole note
    assert module_0.parse_music('o') == [4]

    # Test basic half note
    assert module_0.parse_music('o|') == [2]

    # Test basic quarter note
    assert module_0.parse_music('.|') == [1]

    # Test multiple notes
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Test repeated notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # Test empty string
    assert module_0.parse_music('') == []

    # Test string with only spaces
    assert module_0.parse_music('   ') == []

    # Test leading/trailing spaces
    assert module_0.parse_music(' o o| ') == [4, 2]

    # Test complex sequence
    assert module_0.parse_music('o .| o| .| o| o| o o') == [4, 1, 2, 1, 2, 2, 4, 4]

    # Test the canonical example
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test result is a list of integers
    result = module_0.parse_music('o o|')
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

    # Test invalid note raises KeyError
    try:
        module_0.parse_music('x')
        assert False, "Expected KeyError for invalid note"
    except KeyError:
        pass

    print("All parse_music tests passed!")


if __name__ == "__main__":
    test_parse_music()