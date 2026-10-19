# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from script_1 import separate_paren_groups

# WIN: covers lines 6-22 - try: pytest --cov=script_1 (1 min)
# Status: step 1 of 1 done
# 1. empty covers loop-zero + return
def test_empty_string():
    assert separate_paren_groups("") == []

# 2. single covers ( / ) / depth==0-true
def test_single_group():
    assert separate_paren_groups("()") == ["()"]

# 3. nested covers depth==0-false
def test_nested_single_group():
    assert separate_paren_groups("(())") == ["(())"]

# 4. multiple covers non-paren elif-false + clear/reuse
def test_multiple_groups_with_spaces_and_ignored_chars():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]
    assert separate_paren_groups("(a) b (c(d))") == ["()", "((()))".replace("((()))", "(())")]
# NEXT (under 2 min): run pytest --cov=script_1 --cov-branch
