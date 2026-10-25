

# Generated at 2026-10-25 02:48:02.671743
# Unit test for function parse_music
def test_parse_music():
    assert module_0.parse_music("o") == [4]
    assert module_0.parse_music("o|") == [2]
    assert module_0.parse_music(".|") == [1]
    assert module_0.parse_music("o o| .|") == [4, 2, 1]
    assert module_0.parse_music("o  o|   .|") == [4, 2, 1]
    assert module_0.parse_music("") == []

# Generated at 2026-10-25 02:48:10.127790
# Unit test for function parse_music
def test_parse_music():
    assert module_0.parse_music("o o| .| .| o o o o") == [4, 2, 1, 1, 4, 4, 4, 4]
    assert module_0.parse_music("") == []
    assert module_0.parse_music("o   o|   .|") == [4, 2, 1]

# Generated at 2026-10-25 02:48:15.266119
# Unit test for function parse_music
def test_parse_music():
    assert module_0.parse_music("o o| .| o| o") == [4, 2, 1, 2, 4]
    assert module_0.parse_music("o") == [4]
    assert module_0.parse_music("o|") == [2]
    assert module_0.parse_music(".|") == [1]
    assert module_0.parse_music("") == []
    assert module_0.parse_music("  o   .|  o|  ") == [4, 1, 2]

# Generated at 2026-10-25 02:48:20.521204
# Unit test for function parse_music
def test_parse_music():
    assert module_0.parse_music("o o| .|") == [4, 2, 1]
    assert module_0.parse_music("o o o") == [4, 4, 4]
    assert module_0.parse_music("o| .| o") == [2, 1, 4]
    assert module_0.parse_music("") == []
    assert module_0.parse_music("  o   o|   .|  ") == [4, 2, 1]

# Generated at 2026-10-25 02:48:25.825184
# Unit test for function parse_music
def test_parse_music():
    assert module_0.parse_music("o o| .|") == [4, 2, 1]
    assert module_0.parse_music("o o o") == [4, 4, 4]
    assert module_0.parse_music("o| .| o|") == [2, 1, 2]
    assert module_0.parse_music("") == []
    assert module_0.parse_music("  o   o|   .|  ") == [4, 2, 1]