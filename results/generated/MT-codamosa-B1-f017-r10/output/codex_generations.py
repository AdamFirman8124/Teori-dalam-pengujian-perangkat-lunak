

# Generated at 2026-10-24 14:52:17.654581
# Unit test for function parse_music
def test_parse_music():
    # Basic: each note type maps correctly
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Empty string returns empty list
    assert module_0.parse_music('') == []

    # Extra spaces are ignored (the `if x` filter)
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    # Longer sequence
    assert module_0.parse_music('o o| o .| o| .| o') == [4, 2, 4, 1, 2, 1, 4]

    # Sum check: beats add up
    assert sum(module_0.parse_music('o o| .| .|')) == 8

    print("All tests passed!")


test_parse_music()

# Generated at 2026-10-24 14:52:19.186488
# Unit test for function parse_music
def test_parse_music():
    # Basic: each note type maps correctly
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Empty string returns empty list
    assert module_0.parse_music('') == []

    # Extra spaces are ignored (the `if x` filter)
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    # Longer sequence
    assert module_0.parse_music('o o| o .| o| .| o') == [4, 2, 4, 1, 2, 1, 4]

    # Sum check: beats add up
    assert sum(module_0.parse_music('o o| .| .|')) == 8

    print("All tests passed!")


test_parse_music()

# Generated at 2026-10-24 14:52:20.513123
# Unit test for function parse_music
def test_parse_music():
    # Basic: each note type maps correctly
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Empty string returns empty list
    assert module_0.parse_music('') == []

    # Extra spaces are ignored (the `if x` filter)
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    # Longer sequence
    assert module_0.parse_music('o o| o .| o| .| o') == [4, 2, 4, 1, 2, 1, 4]

    # Sum check: beats add up
    assert sum(module_0.parse_music('o o| .| .|')) == 8

    print("All tests passed!")


test_parse_music()

# Generated at 2026-10-24 14:52:21.835182
# Unit test for function parse_music
def test_parse_music():
    # Basic: each note type maps correctly
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Empty string returns empty list
    assert module_0.parse_music('') == []

    # Extra spaces are ignored (the `if x` filter)
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    # Longer sequence
    assert module_0.parse_music('o o| o .| o| .| o') == [4, 2, 4, 1, 2, 1, 4]

    # Sum check: beats add up
    assert sum(module_0.parse_music('o o| .| .|')) == 8

    print("All tests passed!")


test_parse_music()

# Generated at 2026-10-24 14:52:23.283231
# Unit test for function parse_music
def test_parse_music():
    # Basic: each note type maps correctly
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # Empty string returns empty list
    assert module_0.parse_music('') == []

    # Extra spaces are ignored (the `if x` filter)
    assert module_0.parse_music('  o   o|  ') == [4, 2]

    # Longer sequence
    assert module_0.parse_music('o o| o .| o| .| o') == [4, 2, 4, 1, 2, 1, 4]

    # Sum check: beats add up
    assert sum(module_0.parse_music('o o| .| .|')) == 8

    print("All tests passed!")


test_parse_music()