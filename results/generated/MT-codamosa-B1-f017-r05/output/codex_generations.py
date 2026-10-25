

# Generated at 2026-10-24 22:24:10.374666
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

# Generated at 2026-10-24 22:24:11.692502
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

# Generated at 2026-10-24 22:24:13.008436
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

# Generated at 2026-10-24 22:24:14.330015
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

# Generated at 2026-10-24 22:24:15.658731
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