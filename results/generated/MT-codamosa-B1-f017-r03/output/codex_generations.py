

# Generated at 2026-10-24 20:25:19.671159
# Unit test for function parse_music

# Generated at 2026-10-24 20:25:22.182439
# Unit test for function parse_music

# Generated at 2026-10-24 20:25:27.767377
# Unit test for function parse_music
def test_parse_music():
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]
    assert module_0.parse_music('o| .| o| .|') == [2, 1, 2, 1]
    assert module_0.parse_music('') == []
    assert module_0.parse_music('  o  .| ') == [4, 1]

# Generated at 2026-10-24 20:25:35.551198
# Unit test for function parse_music
def test_parse_music():
    # 1. Basic notes: whole, half, quarter
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # 2. Empty string -> empty list
    assert module_0.parse_music('') == []

    # 3. Whitespace-only string -> empty list
    assert module_0.parse_music('   ') == []

    # 4. Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # 5. Repeated notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # 6. Mixed sequence (typical example)
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # 7. Extra spaces between notes are tolerated
    assert module_0.parse_music('o  o|   .|') == [4, 2, 1]

    # 8. Leading/trailing spaces
    assert module_0.parse_music('  o o|  ') == [4, 2]

    # 9. Result type is a list of ints
    result = module_0.parse_music('o| .|')
    assert isinstance(result, list) and all(isinstance(x, int) for x in result)

    # 10. Unknown token raises KeyError (documents current behavior)
    try:
        module_0.parse_music('o x')
        assert False, 'Expected KeyError'
    except KeyError:
        pass

    print('All tests passed!')


if __name__ == '__main__':
    test_parse_music()

# Generated at 2026-10-24 20:25:36.865862
# Unit test for function parse_music
def test_parse_music():
    # 1. Basic notes: whole, half, quarter
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # 2. Empty string -> empty list
    assert module_0.parse_music('') == []

    # 3. Whitespace-only string -> empty list
    assert module_0.parse_music('   ') == []

    # 4. Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # 5. Repeated notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # 6. Mixed sequence (typical example)
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # 7. Extra spaces between notes are tolerated
    assert module_0.parse_music('o  o|   .|') == [4, 2, 1]

    # 8. Leading/trailing spaces
    assert module_0.parse_music('  o o|  ') == [4, 2]

    # 9. Result type is a list of ints
    result = module_0.parse_music('o| .|')
    assert isinstance(result, list) and all(isinstance(x, int) for x in result)

    # 10. Unknown token raises KeyError (documents current behavior)
    try:
        module_0.parse_music('o x')
        assert False, 'Expected KeyError'
    except KeyError:
        pass

    print('All tests passed!')


if __name__ == '__main__':
    test_parse_music()

# Generated at 2026-10-24 20:25:38.202742
# Unit test for function parse_music
def test_parse_music():
    # 1. Basic notes: whole, half, quarter
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # 2. Empty string -> empty list
    assert module_0.parse_music('') == []

    # 3. Whitespace-only string -> empty list
    assert module_0.parse_music('   ') == []

    # 4. Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # 5. Repeated notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # 6. Mixed sequence (typical example)
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # 7. Extra spaces between notes are tolerated
    assert module_0.parse_music('o  o|   .|') == [4, 2, 1]

    # 8. Leading/trailing spaces
    assert module_0.parse_music('  o o|  ') == [4, 2]

    # 9. Result type is a list of ints
    result = module_0.parse_music('o| .|')
    assert isinstance(result, list) and all(isinstance(x, int) for x in result)

    # 10. Unknown token raises KeyError (documents current behavior)
    try:
        module_0.parse_music('o x')
        assert False, 'Expected KeyError'
    except KeyError:
        pass

    print('All tests passed!')


if __name__ == '__main__':
    test_parse_music()

# Generated at 2026-10-24 20:25:39.524067
# Unit test for function parse_music
def test_parse_music():
    # 1. Basic notes: whole, half, quarter
    assert module_0.parse_music('o o| .|') == [4, 2, 1]

    # 2. Empty string -> empty list
    assert module_0.parse_music('') == []

    # 3. Whitespace-only string -> empty list
    assert module_0.parse_music('   ') == []

    # 4. Single note
    assert module_0.parse_music('o') == [4]
    assert module_0.parse_music('o|') == [2]
    assert module_0.parse_music('.|') == [1]

    # 5. Repeated notes
    assert module_0.parse_music('o o o o') == [4, 4, 4, 4]

    # 6. Mixed sequence (typical example)
    assert module_0.parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

    # 7. Extra spaces between notes are tolerated
    assert module_0.parse_music('o  o|   .|') == [4, 2, 1]

    # 8. Leading/trailing spaces
    assert module_0.parse_music('  o o|  ') == [4, 2]

    # 9. Result type is a list of ints
    result = module_0.parse_music('o| .|')
    assert isinstance(result, list) and all(isinstance(x, int) for x in result)

    # 10. Unknown token raises KeyError (documents current behavior)
    try:
        module_0.parse_music('o x')
        assert False, 'Expected KeyError'
    except KeyError:
        pass

    print('All tests passed!')


if __name__ == '__main__':
    test_parse_music()