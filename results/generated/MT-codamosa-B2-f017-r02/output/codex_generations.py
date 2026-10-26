

# Generated at 2026-10-25 06:52:44.446202
# Unit test for function parse_music
def test_parse_music():
    assert module_0.parse_music("o o| .|") == [4, 2, 1]
    assert module_0.parse_music("o| o| .| .| o o") == [2, 2, 1, 1, 4, 4]
    assert module_0.parse_music("") == []
    assert module_0.parse_music("  o   o|  ") == [4, 2]

# Generated at 2026-10-25 06:52:46.863599
# Unit test for function parse_music

# Generated at 2026-10-25 06:52:49.567432
# Unit test for function parse_music

# Generated at 2026-10-25 06:52:52.205419
# Unit test for function parse_music

# Generated at 2026-10-25 06:52:54.619530
# Unit test for function parse_music

# Generated at 2026-10-25 06:52:57.036017
# Unit test for function parse_music

# Generated at 2026-10-25 06:52:59.453585
# Unit test for function parse_music

# Generated at 2026-10-25 06:53:28.612510
# Unit test for function parse_music
def test_parse_music():
    # whole notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # half notes
    assert module_0.parse_music('o| o| o| o|') == [2, 2, 2, 2]

    # quarter notes
    assert module_0.parse_music('.| .| .| .|') == [1, 1, 1, 1]

    # mixed notes - example from docstring
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # single notes
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # empty / blank input
    assert module_0.parse_music('') == []
    assert module_0.parse_music('   ') == []

    # extra spaces should be ignored
    assert module_0.parse_music('o  o|   .|') == [4, 2, 1]

# Generated at 2026-10-25 06:53:31.140730
# Unit test for function parse_music

# Generated at 2026-10-25 06:53:33.674591
# Unit test for function parse_music

# Generated at 2026-10-25 06:53:36.091670
# Unit test for function parse_music