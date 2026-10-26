

# Generated at 2026-10-25 12:15:12.421153
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:16:30.449190
# Unit test for constructor of class LookupModule
def test_LookupModule():lookup = LookupModule()

# Generated at 2026-10-25 12:17:18.108978
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:17:34.446499
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-25 12:18:14.963363
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:19:04.671843
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:19:06.193876
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:19:08.096787
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:19:49.106966
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:20:18.993876
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:20:20.431556
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:21:08.164755
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:21:27.001933
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-25 12:22:03.850916
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:22:38.682429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:22:59.061203
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:23:03.775401
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 12:24:07.567483
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch
    mod = LookupModule()
    assert mod.run([]) == []
    assert mod.run([], inject={}) == []
    assert mod.run(['only']) == ['only']
    assert mod.run(['only'], inject=None) == ['only']
    terms = ['a', 'b', 'c', 'd']
    orig = list(terms)
    res = mod.run(terms)
    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0] in orig
    assert terms == orig

# Generated at 2026-10-25 12:24:51.740370
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)