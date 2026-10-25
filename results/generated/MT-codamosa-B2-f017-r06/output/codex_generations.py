

# Generated at 2026-10-24 11:27:06.540084
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

# Generated at 2026-10-24 11:27:07.857573
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

# Generated at 2026-10-24 11:27:09.169920
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

# Generated at 2026-10-24 11:27:10.502432
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

# Generated at 2026-10-24 11:27:11.817092
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