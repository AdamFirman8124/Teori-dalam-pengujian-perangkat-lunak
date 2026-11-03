

# Generated at 2026-11-02 08:25:01.807597
# Unit test for function parse_music
def test_parse_music():
    # Empty string returns empty list
    assert module_0.parse_music('') == []

    # Single whole note
    assert module_0.parse_music('o') == [4]

    # Single half note
    assert module_0.parse_music('o|') == [2]

    # Single quarter note
    assert module_0.parse_music('.|') == [1]

    # Mixed notes
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Whitespace-only string returns empty list
    assert module_0.parse_music('   ') == []

    # Multiple spaces between notes are handled
    assert module_0.parse_music('o  .|') == [4, 1]

    # Repeated same note
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    print("All tests passed!")


test_parse_music()

# Generated at 2026-11-02 08:25:08.125990
# Unit test for function parse_music
def test_parse_music():
    # Test basic whole notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # Test basic half notes
    assert module_0.parse_music('o| o| o|') == [2, 2, 2]

    # Test basic quarter notes
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # Test mixed notes (classic example)
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test empty string
    assert module_0.parse_music('') == []

    # Test string with only spaces
    assert module_0.parse_music('   ') == []

    # Test single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Test that result is a list of ints
    result = module_0.parse_music('o .|')
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 08:25:22.263580
# Unit test for function parse_music
def test_parse_music():
    # Empty string yields an empty list
    assert module_0.parse_music('') == []

    # Single notes
    assert module_0.parse_music('o') == [4]       # whole note
    assert module_0.parse_music('o|') == [2]      # half note
    assert module_0.parse_music('.|') == [1]      # quarter note

    # Mixed sequence
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Repeated notes
    assert module_0.parse_music('o| o| .| .| .| .| .| .|') == [2, 2, 1, 1, 1, 1, 1, 1]

    # Longer example
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Multiple spaces are ignored (split handles them, empty tokens filtered out)
    assert module_0.parse_music('  o   .|  ') == [4, 1]


test_parse_music()

# Generated at 2026-11-02 08:25:39.869221
# Unit test for function parse_music
def test_parse_music():
    # Canonical example: whole, half, and quarter notes
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Empty string returns empty list
    assert module_0.parse_music('') == []

    # String with only spaces returns empty list
    assert module_0.parse_music('   ') == []

    # Single whole note
    assert module_0.parse_music('o') == [4]

    # Single half note
    assert module_0.parse_music('o|') == [2]

    # Single quarter note
    assert module_0.parse_music('.|') == [1]

    # Repeated same notes
    assert module_0.parse_music('o o o') == [4, 4, 4]
    assert module_0.parse_music('o| o|') == [2, 2]
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # Mixed notes in various orders
    assert module_0.parse_music('.| o| o') == [1, 2, 4]
    assert module_0.parse_music('o .| o| .|') == [4, 1, 2, 1]

    # Long sequence
    assert module_0.parse_music('o| .| o| .| o| .| o| .|') == [2, 1, 2, 1, 2, 1, 2, 1]

    # Leading/trailing spaces are ignored (empty tokens filtered)
    assert module_0.parse_music(' o o| ') == [4, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-02 08:25:47.012512
# Unit test for function parse_music
def test_parse_music():
    # Test with a single whole note
    assert module_0.parse_music('o') == [4]

    # Test with a single half note
    assert module_0.parse_music('o|') == [2]

    # Test with a single quarter note
    assert module_0.parse_music('.|') == [1]

    # Test with empty string
    assert module_0.parse_music('') == []

    # Test with multiple whole notes
    assert module_0.parse_music('o o') == [4, 4]

    # Test with mixed notes
    assert module_0.parse_music('o .| o|') == [4, 1, 2]

    # Test with the canonical example
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]

    # Test with extra spaces (empty tokens are filtered out)
    assert module_0.parse_music('  o   .|  ') == [4, 1]

    # Test long sequence
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]

    print("All tests passed!")


test_parse_music()