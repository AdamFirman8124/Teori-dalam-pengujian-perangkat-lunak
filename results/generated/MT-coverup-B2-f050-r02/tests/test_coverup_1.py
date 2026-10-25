# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

def test_encode_shift_wraps_alphabet():
    from f050 import encode_shift

    assert encode_shift("abcxyz") == "fghcde"
    assert encode_shift("") == ""
