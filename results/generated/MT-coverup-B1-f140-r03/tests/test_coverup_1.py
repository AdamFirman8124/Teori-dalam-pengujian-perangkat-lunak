# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

from f140 import fix_spaces


def test_fix_spaces_replaces_internal_space_runs():
    assert fix_spaces("alpha beta  gamma   delta") == "alpha_beta__gamma-delta"


def test_fix_spaces_handles_trailing_spaces():
    assert fix_spaces("word ") == "word_"
    assert fix_spaces("word   ") == "word-"


def test_fix_spaces_handles_text_without_spaces_and_empty_text():
    assert fix_spaces("word") == "word"
    assert fix_spaces("") == ""
