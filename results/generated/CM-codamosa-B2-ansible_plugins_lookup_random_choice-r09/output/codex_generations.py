

# Generated at 2026-11-01 21:53:35.563196
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.errors import AnsibleError


def test_LookupModule_run(mocker):
    lookup_plugin = LookupModule()
    mocker.patch.object(random, 'choice', side_effect=Exception("mocked error"))

    with pytest.raises(AnsibleError) as e:
        lookup_plugin.run(['a', 'b'])
    assert "Unable to choose random term: mocked error" in to_native(e.value)

    mocker.stopall()
    result = lookup_plugin.run(['a', 'b'])
    assert result in [['a'], ['b']]

    result = lookup_plugin.run([])
    assert result == []

# Generated at 2026-11-01 21:54:14.225723
# Unit test for constructor of class LookupModule
def test_LookupModule():
    """
    Test the constructor of class LookupModule.
    """
    # Instantiate the lookup module without any arguments
    lookup_module = LookupModule()

    # Verify that the instance was created successfully
    assert lookup_module is not None
    assert isinstance(lookup_module, LookupModule)

    # Verify inherited attributes/methods exist from LookupBase
    assert hasattr(lookup_module, 'run')
    assert callable(lookup_module.run)
    assert hasattr(lookup_module, 'get_options')

    # Verify instantiation with explicit keyword arguments
    lookup_module_kwargs = LookupModule(loader=None, templar=None, variable_params={})
    assert lookup_module_kwargs is not None
    assert isinstance(lookup_module_kwargs, LookupModule)

    # Verify run() is callable on the new instance
    assert callable(lookup_module_kwargs.run)

# Generated at 2026-11-01 21:55:08.635996
# Unit test for constructor of class LookupModule
def test_LookupModule():
    '''
    Test the constructor of LookupModule
    '''
    lookup_plugin = LookupModule()
    assert isinstance(lookup_plugin, LookupModule)
    assert isinstance(lookup_plugin, LookupBase)
    assert lookup_plugin._loader is None
    assert lookup_plugin._templar is None
    assert lookup_plugin._basedir == '.'

# Generated at 2026-11-01 21:55:52.059643
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    return LookupModule()


def test_empty_terms(lookup):
    """An empty list returns an empty list unchanged."""
    assert lookup.run([]) == []


def test_none_terms(lookup):
    """Falsy (None) terms return None unchanged."""
    assert lookup.run(None) is None


def test_single_term(lookup):
    """A single-item list always yields that item."""
    assert lookup.run(["only"]) == ["only"]


def test_multiple_terms_returns_one_of_them(lookup):
    """Result must be a single-element list containing one of the input terms."""
    terms = ["a", "b", "c", "d"]
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_all_choices_eventually_selected(lookup):
    """Repeated runs eventually exercise every possible choice."""
    terms = ["x", "y", "z"]
    seen = set()
    for _ in range(200):
        seen.add(lookup.run(terms)[0])
    assert seen == set(terms)


def test_non_string_terms(lookup):
    """Works with arbitrary object types."""
    terms = [1, {"key": "value"}, ("t",), None]
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_error_raised_on_failure(lookup, monkeypatch):
    """Exceptions from random.choice are wrapped in AnsibleError."""

    def boom(seq):
        raise ValueError("boom")

    monkeypatch.setattr(
        "ansible.plugins.lookup.random_choice.random.choice", boom
    )
    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        lookup.run(["a"])

# Generated at 2026-11-01 21:56:41.829328
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    return LookupModule()


def test_run_empty_terms(lookup):
    # Falsy terms should be returned as-is (empty list)
    assert lookup.run([]) == []


def test_run_none_terms(lookup):
    # None terms should be returned as-is
    assert lookup.run(None) is None


def test_run_single_term(lookup):
    result = lookup.run(["only"])
    assert result == ["only"]


def test_run_returns_element_from_terms(lookup):
    terms = ["go through the door", "drink from the goblet", "press the red button"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_multiple_calls_valid(lookup):
    terms = [1, 2, 3, 4, 5]
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms


def test_run_with_inject_and_kwargs(lookup):
    terms = ["a", "b"]
    result = lookup.run(terms, inject={"some": "var"}, variables=None)
    assert len(result) == 1
    assert result[0] in terms


@patch("ansible.plugins.lookup.random_choice.random.choice")
def test_run_calls_random_choice(mock_choice, lookup):
    mock_choice.return_value = "b"
    terms = ["a", "b", "c"]
    result = lookup.run(terms)
    mock_choice.assert_called_once_with(terms)
    assert result == ["b"]


@patch("ansible.plugins.lookup.random_choice.random.choice")
def test_run_wraps_exception_in_ansible_error(mock_choice, lookup):
    mock_choice.side_effect = ValueError("boom")
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["a", "b"])

# Generated at 2026-11-01 21:57:17.155226
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_LookupModule_run_empty_terms():
    lookup = LookupModule()
    assert lookup.run([]) == []


def test_LookupModule_run_none_terms():
    lookup = LookupModule()
    assert lookup.run(None) is None


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    assert lookup.run(['only_choice']) == ['only_choice']


def test_LookupModule_run_multiple_terms():
    lookup = LookupModule()
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_LookupModule_run_returns_list_even_with_tuple():
    lookup = LookupModule()
    terms = ('a', 'b', 'c')
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_LookupModule_run_error_wrapped_in_ansible_error():
    lookup = LookupModule()
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=ValueError('boom')):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(['x', 'y'])

# Generated at 2026-11-01 21:57:56.785112
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import random
    from unittest.mock import patch

    from ansible.errors import AnsibleError
    from ansible.plugins.lookup.random_choice import LookupModule

    lookup = LookupModule()

    # Empty (falsy) terms are returned as-is
    assert lookup.run([]) == []
    assert lookup.run(None) is None

    # Non-empty terms return a single-element list containing a member of terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Deterministic behavior: random.choice is called once with the terms
    with patch('random.choice', return_value='drink from the goblet') as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ['drink from the goblet']

    # inject and extra kwargs are accepted and ignored
    result = lookup.run(terms, inject={'some': 'var'}, arbitrary_kwarg=True)
    assert len(result) == 1
    assert result[0] in terms

    # Exceptions raised by random.choice are wrapped in AnsibleError
    with patch('random.choice', side_effect=ValueError('boom')):
        try:
            lookup.run(terms)
        except AnsibleError as e:
            assert 'Unable to choose random term' in str(e)
            assert 'boom' in str(e)
        else:
            raise AssertionError("AnsibleError was not raised")

# Generated at 2026-11-01 21:58:48.189660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty list is returned unchanged
    assert lookup.run([]) == []

    # Falsy terms (None) are returned unchanged
    assert lookup.run(None) is None

    # Single term returns a list with that term
    assert lookup.run(['only']) == ['only']

    # Multiple terms: result contains exactly one element from terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Repeated runs always pick one of the provided terms
    for _ in range(50):
        assert lookup.run(terms)[0] in terms

    # Terms of various types are handled
    mixed_terms = [1, 'two', 3.0, None]
    result = lookup.run(mixed_terms)
    assert len(result) == 1
    assert result[0] in mixed_terms

    # Exception during random.choice is wrapped in an AnsibleError
    with patch('random.choice', side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as exc_info:
            lookup.run(['a', 'b'])
        assert 'Unable to choose random term' in str(exc_info.value)
        assert 'boom' in str(exc_info.value)

# Generated at 2026-11-01 21:59:39.084913
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty input returns empty list
    assert lookup.run([]) == []

    # None input is returned as-is
    assert lookup.run(None) is None

    # Non-empty input returns exactly one element chosen from the terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button', 'do nothing']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Single-element input deterministically returns that element
    assert lookup.run(['only']) == ['only']

    # Failure inside random.choice is wrapped in AnsibleError
    with mock.patch('random.choice', side_effect=ValueError('boom')):
        try:
            lookup.run(['a', 'b'])
            assert False, 'AnsibleError was not raised'
        except AnsibleError as e:
            assert 'Unable to choose random term: boom' in str(e)


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-01 22:00:26.396263
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty or missing terms are returned unchanged
    assert lookup.run([]) == []
    assert lookup.run(None) is None

    # Non-empty terms: result must be a single-element list drawn from terms
    terms = ["go through the door", "drink from the goblet", "press the red button"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Deterministic behavior when random.choice is patched
    with patch('random.choice', return_value="drink from the goblet"):
        assert lookup.run(["a", "b"]) == ["drink from the goblet"]

    # Errors raised by random.choice are wrapped in AnsibleError
    with patch('random.choice', side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(["a", "b"])
    assert "Unable to choose random term" in str(excinfo.value)
    assert "boom" in str(excinfo.value)

    # Extra kwargs (like inject/variables) are accepted without breaking behavior
    with patch('random.choice', return_value=42):
        assert lookup.run([1, 2, 3], inject={"foo": "bar"}, some_kwarg=True) == [42]

# Generated at 2026-11-01 22:01:04.484686
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_run_with_empty_terms():
    lookup = LookupModule()
    assert lookup.run([]) == []


def test_run_with_none_terms():
    lookup = LookupModule()
    assert lookup.run(None) is None


def test_run_with_single_term():
    lookup = LookupModule()
    terms = ['only_option']
    assert lookup.run(terms) == ['only_option']


def test_run_with_multiple_terms_returns_one():
    lookup = LookupModule()
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_run_returns_list_of_one():
    lookup = LookupModule()
    terms = ['a', 'b', 'c', 'd']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1


def test_run_wraps_exception_in_ansible_error():
    lookup = LookupModule()
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as exc_info:
            lookup.run(['a', 'b'])
    assert 'Unable to choose random term' in to_text(exc_info.value)
    assert 'boom' in to_text(exc_info.value)


def test_run_with_unhashable_terms():
    lookup = LookupModule()
    terms = [{'key': 'value1'}, {'key': 'value2'}]
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms


def to_text(value):
    return str(value)

# Generated at 2026-11-01 22:02:00.090824
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Non-empty terms: result must be a single-element list containing one of the terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Single-element list
    assert lookup.run(['only']) == ['only']

    # Empty list is returned as-is (falsy short-circuit)
    assert lookup.run([]) == []

    # None terms are returned as-is
    assert lookup.run(None) is None

    # inject kwarg is accepted and ignored
    assert lookup.run(['a', 'b'], inject={'foo': 'bar'})[0] in ['a', 'b']

    # Deterministic behavior via mocked random.choice
    with patch('ansible.plugins.lookup.random_choice.random.choice', return_value='b') as m_choice:
        assert lookup.run(['a', 'b', 'c']) == ['b']
        m_choice.assert_called_once_with(['a', 'b', 'c'])

    # Any exception from random.choice is wrapped in AnsibleError
    with patch('ansible.plugins.lookup.random_choice.random.choice', side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a', 'b'])
        assert 'Unable to choose random term: boom' in str(excinfo.value)

# Generated at 2026-11-01 22:02:53.542645
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    from ansible.errors import AnsibleError
    from ansible.plugins.lookup.random_choice import LookupModule

    lookup = LookupModule()

    # Empty terms are returned as-is
    assert lookup.run([]) == []

    # None terms are returned as-is
    assert lookup.run(None) is None

    # Single term list returns that single term
    assert lookup.run(['only']) == ['only']

    # Multiple terms: result is a list containing exactly one element
    # chosen from the input terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms

    # If random.choice raises, an AnsibleError is raised with a message
    with patch('random.choice', side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(terms)
        assert 'Unable to choose random term' in str(excinfo.value)
        assert 'boom' in str(excinfo.value)