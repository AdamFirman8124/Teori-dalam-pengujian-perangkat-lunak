

# Generated at 2026-11-02 15:37:35.201095
# Unit test for function parse_music
def test_parse_music():
    # Single notes
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Empty string
    assert module_0.parse_music('') == []

    # Multiple spaces / extra whitespace handled
    assert module_0.parse_music('  ') == []
    assert module_0.parse_music(' o   o|  .| ') == [4, 2, 1]

    # Mixed notes
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]
    assert module_0.parse_music('o| o| o|') == [2, 2, 2]

    # Repeated whole notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 15:39:42.551719
# Unit test for function parse_music
def test_parse_music():
    # Test basic example: whole, half, quarter notes
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Test single whole note
    assert module_0.parse_music('o') == [4]

    # Test single half note
    assert module_0.parse_music('o|') == [2]

    # Test single quarter note
    assert module_0.parse_music('.|') == [1]

    # Test multiple whole notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # Test multiple half notes
    assert module_0.parse_music('o| o| o|') == [2, 2, 2]

    # Test multiple quarter notes
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]

    # Test empty string returns empty list
    assert module_0.parse_music('') == []

    # Test string with only spaces returns empty list
    assert module_0.parse_music('   ') == []

    # Test mixed sequence with repeated notes
    assert module_0.parse_music('o| .| o .| o|') == [2, 1, 4, 1, 2]

    # Test complex sequence
    assert module_0.parse_music('o o| o| .| .| o') == [4, 2, 2, 1, 1, 4]

    # Test that extra spaces between notes are handled
    assert module_0.parse_music('  o   o|  .| ') == [4, 2, 1]

    # Test long sequence
    assert module_0.parse_music('.| .| .| .| .| .| .| .|') == [1] * 8

    # Test alternating pattern
    assert module_0.parse_music('o .| o .| o .|') == [4, 1, 4, 1, 4, 1]

    # Test result is a list of integers
    result = module_0.parse_music('o o| .|')
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

    # Test length of result matches number of notes
    assert len(module_0.parse_music('o o| .| o| o')) == 5


if __name__ == '__main__':
    test_parse_music()
    print("All tests passed!")

# Generated at 2026-11-02 15:41:41.034040
# Unit test for function parse_music
def test_parse_music():
    # Standard example: whole, half, and quarter notes mixed
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Empty string returns an empty list
    assert module_0.parse_music('') == []

    # Single whole note
    assert module_0.parse_music('o') == [4]

    # Single half note
    assert module_0.parse_music('o|') == [2]

    # Single quarter note
    assert module_0.parse_music('.|') == [1]

    # Repeated same notes
    assert module_0.parse_music('o o o') == [4, 4, 4]
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # String with only spaces returns empty list
    assert module_0.parse_music('   ') == []

    # Leading/trailing spaces are ignored
    assert module_0.parse_music('  o o|  ') == [4, 2]

    # Alternating notes
    assert module_0.parse_music('o| .| o| .| o|') == [2, 1, 2, 1, 2]

    # Long sequence of quarter notes
    assert module_0.parse_music('.| .| .| .| .| .|') == [1, 1, 1, 1, 1, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 15:44:42.399711
# Unit test for function parse_music
def test_parse_music():
    # Basic example
    assert module_0.parse_music('o .| .| .| o o o o') == [4, 1, 1, 1, 4, 4, 4, 4]
    # Empty string
    assert module_0.parse_music('') == []
    # Single notes
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]
    # Mixed notes
    assert module_0.parse_music('o| o| .| .| o| o| o| .|') == [2, 2, 1, 1, 2, 2, 2, 1]
    assert module_0.parse_music('o| .| o| .| o o| o') == [2, 1, 2, 1, 4, 2, 4]
    # Extra spaces are ignored
    assert module_0.parse_music('  o  .|  ') == [4, 1]
    # Repeated identical notes
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]
    assert module_0.parse_music('o| o|') == [2, 2]
    assert module_0.parse_music('o o') == [4, 4]

# Generated at 2026-11-02 15:47:12.167741
# Unit test for function parse_music
def test_parse_music():
    # Test with empty string
    assert module_0.parse_music('') == []

    # Test with single whole note
    assert module_0.parse_music('o') == [4]

    # Test with single half note
    assert module_0.parse_music('o|') == [2]

    # Test with single quarter note
    assert module_0.parse_music('.|') == [1]

    # Test with multiple whole notes
    assert module_0.parse_music('o o o') == [4, 4, 4]

    # Test with mixed note types
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Test with a longer sequence
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test with repeated quarter notes
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]

    # Test with extra whitespace (should be handled by filtering empty strings)
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    print("All tests passed!")