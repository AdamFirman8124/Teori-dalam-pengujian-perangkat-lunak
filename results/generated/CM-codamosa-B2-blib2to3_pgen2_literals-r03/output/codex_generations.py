

# Generated at 2026-11-03 02:54:06.380894
# Unit test for function test
def test_test():
    from unittest.mock import patch

    # module_0.test() prints only when a round-trip fails; a silent run means success.
    with patch('builtins.print') as mock_print:
        module_0.test()

    mock_print.assert_not_called()

    # Verify the same invariant directly: evalString(repr(c)) == c for all chars.
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, "mismatch for %r: repr=%r, got=%r" % (i, s, e)

    # Spot-check simple escapes.
    assert evalString("'a'") == "a"
    assert evalString('"hello\\nworld"') == "hello\nworld"
    assert evalString("'tab:\\t end'") == "tab:\t end"
    assert evalString("'''triple\\rquoted'''") == "triple\rquoted"

    # Hex and octal escapes.
    assert evalString("'\\x41\\x42'") == "AB"
    assert evalString("'\\101\\102'") == "AB"
    assert evalString('"\\0"') == "\0"

    # Quotes and backslashes.
    assert evalString("'\\'quoted\\''") == "'quoted'"
    assert evalString('"back\\\\slash"') == "back\\slash"

# Generated at 2026-11-03 02:59:18.576975
# Unit test for function evalString

# Generated at 2026-11-03 03:00:51.253681
# Unit test for function evalString
def test_evalString():assert module_0.evalString("'hello'") == "hello"