

# Generated at 2026-10-25 06:56:31.276142
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:33.692390
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:36.105113
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:38.523914
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:40.942370
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:43.357113
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:45.775053
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:48.187694
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:50.601921
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:53.019360
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:55.435089
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:56:57.875921
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:57:00.293209
# Unit test for function parse_nested_parens

# Generated at 2026-10-25 06:57:07.820537
# Unit test for function parse_nested_parens
def test_parse_nested_parens():assert module_0.parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
assert module_0.parse_nested_parens("()") == [1]
assert module_0.parse_nested_parens("") == []
assert module_0.parse_nested_parens("(()())") == [2]