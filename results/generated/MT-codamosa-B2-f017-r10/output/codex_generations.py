

# Generated at 2026-11-01 19:31:36.095459
# Unit test for function parse_music
def test_parse_music():
    # Test with empty string
    assert module_0.parse_music('') == []

    # Test with a single whole note
    assert module_0.parse_music('o') == [4]

    # Test with a single half note
    assert module_0.parse_music('o|') == [2]

    # Test with a single quarter note
    assert module_0.parse_music('.|') == [1]

    # Test with multiple whole notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # Test with mixed note types
    assert module_0.parse_music('o .| o| .| o| o| O O'.replace('O', 'o')) == [4, 1, 2, 1, 2, 2, 4, 4]

    # Test with the classic example pattern
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Test that extra spaces are handled gracefully
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-01 19:32:13.618156
# Unit test for function parse_music
def test_parse_music():
    # Test with whole notes ('o' = 4)
    assert module_0.parse_music('o o o') == [4, 4, 4]

    # Test with half notes ('o|' = 2)
    assert module_0.parse_music('o| o|') == [2, 2]

    # Test with quarter notes ('.|' = 1)
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # Test with mixed notes
    assert module_0.parse_music('o .| o| o| .|') == [4, 1, 2, 2, 1]

    # Test with a single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('.|') == [1]

    # Test with empty string
    assert module_0.parse_music('') == []

    # Test with extra spaces
    assert module_0.parse_music('  o  o|  ') == [4, 2]

    print("All parse_music tests passed!")


test_parse_music()

# Generated at 2026-11-01 19:33:06.107690
# Unit test for function parse_music
def test_parse_music():
    # Empty string yields no beats
    assert module_0.parse_music("") == []

    # Single whole note
    assert module_0.parse_music("o") == [4]

    # Single half note
    assert module_0.parse_music("o|") == [2]

    # Single quarter note
    assert module_0.parse_music(".|") == [1]

    # Mixed notes, one of each type
    assert module_0.parse_music("o o| .|") == [4, 2, 1]

    # Classic example: sequence of varying lengths
    assert module_0.parse_music("o o| .| o| o| .| .| .| .| o o") == [
        4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4
    ]

    # Repeated quarter notes
    assert module_0.parse_music(".| .| .| .|") == [1, 1, 1, 1]

    # Extra whitespace between notes is ignored
    assert module_0.parse_music("  o   o|  ") == [4, 2]

    # Result length matches number of tokens
    result = module_0.parse_music("o o o o| .|")
    assert len(result) == 5

    # Sum of beats for a known melody
    melody = "o .| o| .|"
    assert sum(module_0.parse_music(melody)) == 8

    print("All tests passed!")


if __name__ == "__main__":
    test_parse_music()

# Generated at 2026-11-01 19:33:58.539256
# Unit test for function parse_music
def test_parse_music():
    # Empty string should return an empty list
    assert module_0.parse_music('') == []

    # Single whole note
    assert module_0.parse_music('o') == [4]

    # Single half note
    assert module_0.parse_music('o|') == [2]

    # Single quarter note
    assert module_0.parse_music('.|') == [1]

    # Example from the docstring: whole, half, quarter, whole, half, quarter, quarter
    assert module_0.parse_music('o o| .| o o| .| .|') == [4, 2, 1, 4, 2, 1, 1]

    # Repeated whole notes
    assert module_0.parse_music('o o o') == [4, 4, 4]

    # Repeated half notes
    assert module_0.parse_music('o| o|') == [2, 2]

    # Repeated quarter notes
    assert module_0.parse_music('.| .| .|') == [1, 1, 1]

    # Mixed notes in a different order
    assert module_0.parse_music('.| o| o') == [1, 2, 4]

    # Extra whitespace should be ignored
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    # Verify return type is a list
    assert isinstance(module_0.parse_music('o o|'), list)

    # Verify all elements are integers
    assert all(isinstance(x, int) for x in module_0.parse_music('o o| .|'))

# Generated at 2026-11-01 19:34:54.244779
# Unit test for function parse_music
def test_parse_music():
    # Single notes
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Mixed notes
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Classic example sequence
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # Empty string yields empty list
    assert module_0.parse_music('') == []

    # Extra spaces are ignored
    assert module_0.parse_music('o  o|') == [4, 2]
    assert module_0.parse_music(' o ') == [4]
    assert module_0.parse_music('   ') == []

    # Repeated notes
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]
    assert module_0.parse_music('o| o| o|') == [2, 2, 2]
    assert module_0.parse_music('o o o') == [4, 4, 4]

    # Alternating pattern
    assert module_0.parse_music('o .| o .|') == [4, 1, 4, 1]

    # Long sequence
    assert module_0.parse_music('o| .| o .| o| .| o') == [2, 1, 4, 1, 2, 1, 4]