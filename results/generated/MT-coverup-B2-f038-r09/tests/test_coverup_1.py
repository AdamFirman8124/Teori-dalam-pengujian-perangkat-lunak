# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

def test_encode_cyclic_full_coverage():
    from f038 import encode_cyclic

    # Empty string: exercises the list comprehension with zero groups (line 4),
    # the second comprehension (line 6), and the join (line 7).
    assert encode_cyclic("") == ""

    # Length 1: single group of size < 3, hits the "else group" branch on line 6.
    assert encode_cyclic("a") == "a"

    # Length 2: group of size 2, again the else branch.
    assert encode_cyclic("ab") == "ab"

    # Length 3: exactly one full group, hits the "group[1:] + group[0]" branch.
    assert encode_cyclic("abc") == "bca"

    # Length 4: one full group (rotated) plus a trailing partial group (kept as-is),
    # covering both branches of the conditional on line 6 in one call.
    assert encode_cyclic("abcd") == "bcad"

    # Length 6: two full groups, both rotated.
    assert encode_cyclic("abcdef") == "bcaefd"
