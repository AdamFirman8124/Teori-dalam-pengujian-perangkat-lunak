

# Generated at 2026-11-02 23:40:47.223790
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty terms should be returned as-is
    assert lookup.run([]) == []

    # Falsy terms (None) should be returned as-is
    assert lookup.run(None) is None

    # Single term list should return a list containing that term
    assert lookup.run(['only']) == ['only']

    # Multiple terms: result should be a one-element list containing one of the terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button', 'do nothing']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Repeated runs should always select an element from the given terms
    for _ in range(10):
        picked = lookup.run(terms)
        assert len(picked) == 1
        assert picked[0] in terms

    # Non-sequence truthy terms should cause random.choice to fail and raise AnsibleError
    try:
        lookup.run(42)
    except AnsibleError as e:
        assert 'Unable to choose random term' in to_native(e)
    else:
        raise AssertionError("Expected AnsibleError for non-sequence terms")

    # Terms that random.choice cannot handle (e.g., a dict is a valid sequence of keys, so use an int)
    try:
        lookup.run(1.5)
    except AnsibleError as e:
        assert 'Unable to choose random term' in to_native(e)
    else:
        raise AssertionError("Expected AnsibleError for float terms")

# Generated at 2026-11-02 23:42:10.645398
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup_plugin = LookupModule()
    assert lookup_plugin is not None
    assert isinstance(lookup_plugin, LookupModule)
    assert isinstance(lookup_plugin, LookupBase)

# Generated at 2026-11-02 23:43:58.577832
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Falsy terms are returned unchanged
    assert lookup.run([]) == []
    assert lookup.run(None) is None

    # A random member of terms is returned wrapped in a single-element list
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Single-element list always yields that element
    assert lookup.run(["only-one"]) == ["only-one"]

    # Repeated calls only ever return members of the input
    for _ in range(20):
        assert lookup.run(terms)[0] in terms

    # Failures inside random.choice are converted to AnsibleError
    with patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=Exception("boom")):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(["term"])
    assert "Unable to choose random term" in str(excinfo.value)
    assert "boom" in str(excinfo.value)

    # Non-indexable terms (e.g. a generator) also result in AnsibleError
    with pytest.raises(AnsibleError):
        lookup.run(i for i in [1, 2, 3])

# Generated at 2026-11-02 23:45:17.969739
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_LookupModule_run_returns_member_of_terms():
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]
    lookup = LookupModule()
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(["only-one"]) == ["only-one"]


def test_LookupModule_run_empty_terms():
    lookup = LookupModule()
    assert lookup.run([]) == []


def test_LookupModule_run_none_terms():
    lookup = LookupModule()
    assert lookup.run(None) is None


def test_LookupModule_run_calls_random_choice(mocker):
    mock_choice = mocker.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    )
    terms = ["go through the door", "drink from the goblet", "press the red button"]
    lookup = LookupModule()
    result = lookup.run(terms)
    mock_choice.assert_called_once_with(terms)
    assert result == ["press the red button"]


def test_LookupModule_run_wraps_errors_in_ansible_error(mocker):
    mocker.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom"),
    )
    lookup = LookupModule()
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["a", "b"])
    assert "Unable to choose random term: boom" in to_native_str(excinfo.value)


def to_native_str(exc):
    return str(exc)


def test_LookupModule_run_invalid_terms_raises_ansible_error():
    lookup = LookupModule()
    with pytest.raises(AnsibleError):
        lookup.run(12345)

# Generated at 2026-11-02 23:46:19.892816
# Unit test for constructor of class LookupModule
def test_LookupModule():
    '''
    Test the constructor of LookupModule to ensure the instance is created correctly.
    '''
    lookup_plugin = LookupModule()
    assert lookup_plugin is not None
    assert isinstance(lookup_plugin, LookupModule)