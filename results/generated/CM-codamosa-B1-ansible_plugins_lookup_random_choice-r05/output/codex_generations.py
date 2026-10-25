

# Generated at 2026-10-24 02:11:35.203155
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    # Empty terms -> empty result (no call to random.choice)
    assert lookup.run([]) == []

    # Non-empty terms -> exactly one element, and it came from the input
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_LookupModule_returns_selected_term(monkeypatch):
    """Make the choice deterministic so we can assert on the exact return value."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    monkeypatch.setattr(
        "ansible.plugins.lookup.random_choice.random.choice",
        lambda seq: seq[1],
    )
    assert lookup.run(terms) == ["b"]



# Generated at 2026-10-24 02:12:30.262281
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:31.686703
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:32.986758
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:34.655504
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:36.103483
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:37.413050
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:38.721722
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:40.020067
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:41.339889
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:42.658896
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:43.963336
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:45.287018
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:46.630201
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:48.172892
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:49.605922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:50.936046
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:52.233037
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:53.533028
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:54.838258
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:56.181663
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:57.508744
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:12:58.832750
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:00.145286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:01.462612
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:02.767399
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:04.073749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:05.380695
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:06.696956
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:07.985441
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:09.571959
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:10.884163
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:12.179530
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:13.487610
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:14.806732
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:16.472601
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:17.733231
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:19.074814
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:20.392699
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:21.714555
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:23.015638
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:24.336029
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:25.646025
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:27.084633
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:28.403637
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:29.712565
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:31.019974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:32.360614
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:33.669158
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:35.001545
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:36.310819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:37.635622
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:38.940774
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:40.240715
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:41.541368
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:42.844552
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:44.494019
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:45.800158
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:47.260233
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:48.689501
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:50.124375
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:51.444115
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:52.890162
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:54.199969
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:55.523781
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:57.312704
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:13:58.930745
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:00.238035
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:01.546542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:02.924832
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:04.257289
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:05.571839
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:06.870145
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:08.202596
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:09.506157
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:12.923008
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:14.249656
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:15.554402
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:16.862964
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:18.187048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:19.821330
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:21.147581
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:22.451286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:23.770233
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:25.078267
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:32.209977
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:33.645748
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:34.958433
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:36.262086
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:37.637759
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:38.953807
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:40.267096
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:41.578257
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:42.874616
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:44.173649
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:14:59.082543
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:00.693911
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:02.112328
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:03.562058
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:04.885356
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:06.223573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:07.550234
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:08.972790
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:10.277137
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:11.603372
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:41.946397
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:43.254093
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:44.587324
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:46.246831
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:47.698356
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:49.037111
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:50.367732
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:51.722221
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:53.050508
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:15:54.382485
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:16:54.861762
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:16:56.172541
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:16:57.504166
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:16:58.951265
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:17:00.272743
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:17:01.582818
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:17:02.902159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:17:04.209450
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:17:05.521716
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:17:06.876884
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:08.090087
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:09.393689
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:10.700141
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:12.005539
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:13.353127
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:14.658118
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:15.958724
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:17.263211
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:18.622888
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]

# Generated at 2026-10-24 02:19:20.264517
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """module_0.run() returns a one-element list holding the randomly chosen term."""
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet",
             "press the red button", "do nothing"]

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="drink from the goblet") as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert isinstance(result, list)
    assert result == ["drink from the goblet"]


def test_LookupModule_run_returns_a_real_term():
    """Whatever is returned is always one of the supplied terms."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]

    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only"]) == ["only"]


def test_LookupModule_run_empty_terms():
    """Falsy terms are returned untouched and random.choice is not called."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice") as mock_choice:
        assert lookup.run([]) == []
        assert lookup.run(None) is None

    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_exceptions():
    """Any failure from random.choice is re-raised as AnsibleError."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError,
                           match="Unable to choose random term: boom"):
            lookup.run(["a", "b"])


def test_LookupModule_run_ignores_extra_args():
    """inject/extra kwargs are accepted and don't affect the result."""
    lookup = LookupModule()

    with patch("ansible.plugins.lookup.random_choice.random.choice",
               return_value="b"):
        assert lookup.run(["a", "b"], inject={"x": 1}, wantlist=True) == ["b"]