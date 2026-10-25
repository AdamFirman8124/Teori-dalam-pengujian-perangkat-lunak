

# Generated at 2026-10-24 12:44:28.603559
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

# Generated at 2026-10-24 12:44:29.913990
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

# Generated at 2026-10-24 12:44:32.532910
# Unit test for function parse_music

# Generated at 2026-10-24 12:44:34.947936
# Unit test for function parse_music

# Generated at 2026-10-24 12:44:37.474983
# Unit test for function parse_music

# Generated at 2026-10-24 12:44:39.885940
# Unit test for function parse_music

# Generated at 2026-10-24 12:44:42.302853
# Unit test for function parse_music

# Generated at 2026-10-24 12:44:44.718832
# Unit test for function parse_music

# Generated at 2026-10-24 12:44:47.136572
# Unit test for function parse_music

# Generated at 2026-10-24 12:44:49.549813
# Unit test for function parse_music

# Generated at 2026-10-24 12:44:51.965058
# Unit test for function parse_music