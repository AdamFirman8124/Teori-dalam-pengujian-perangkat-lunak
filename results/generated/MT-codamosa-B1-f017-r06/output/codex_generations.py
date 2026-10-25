

# Generated at 2026-10-24 10:39:57.737066
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

# Generated at 2026-10-24 10:40:00.158067
# Unit test for function parse_music

# Generated at 2026-10-24 10:40:02.577987
# Unit test for function parse_music

# Generated at 2026-10-24 10:40:30.617427
# Unit test for function parse_music
def test_parse_music():
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]
    assert module_0.parse_music('') == []
    assert module_0.parse_music('  o  ') == [4]

# Generated at 2026-10-24 10:40:32.041133
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

# Generated at 2026-10-24 10:40:33.473727
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

# Generated at 2026-10-24 10:40:34.787660
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