

# Generated at 2026-11-01 21:19:20.375994
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup_plugin = LookupModule()
    assert lookup_plugin is not None
    assert isinstance(lookup_plugin, LookupModule)

# Generated at 2026-11-01 21:19:24.572303
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupModule)

# Generated at 2026-11-01 21:19:32.558993
# Unit test for constructor of class LookupModule
def test_LookupModule():
    '''
    Test constructor of class LookupModule.
    '''
    # Instantiate the lookup plugin with no arguments
    lookup = LookupModule()

    # Constructor should return a valid instance
    assert lookup is not None
    assert isinstance(lookup, LookupModule)

    # Should also construct successfully when given mocked dependencies
    mock_loader = MagicMock()
    mock_templar = MagicMock()
    lookup_with_deps = LookupModule(loader=mock_loader, templar=mock_templar)
    assert isinstance(lookup_with_deps, LookupModule)
    assert lookup_with_deps._loader == mock_loader
    assert lookup_with_deps._templar == mock_templar

# Generated at 2026-11-01 21:19:37.062178
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupModule)

# Generated at 2026-11-01 21:19:40.462346
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup_plugin = LookupModule()
    assert isinstance(lookup_plugin, LookupModule)

# Generated at 2026-11-01 21:19:54.886659
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Non-empty list: must return a single-element list containing a member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button"]
    result = lookup_module.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Repeated invocations always select one of the provided terms
    for _ in range(25):
        assert lookup_module.run(terms)[0] in terms

    # Empty list is returned unchanged (falsy branch)
    assert lookup_module.run([]) == []

    # None terms is returned unchanged
    assert lookup_module.run(None) is None

    # Tuple input still yields a single-element list
    result = lookup_module.run(("x", "y"))
    assert result == ["x"] or result == ["y"]

    # Mock random.choice to force a deterministic outcome
    with patch("random.choice", return_value="press the red button") as mock_choice:
        assert lookup_module.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # A failure inside random.choice is converted to AnsibleError
    with patch("random.choice", side_effect=Exception("no luck")):
        with pytest.raises(AnsibleError) as excinfo:
            lookup_module.run(terms)
        assert "Unable to choose random term: no luck" in str(excinfo.value)

# Generated at 2026-11-01 21:20:06.148634
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest import mock


# Generated at 2026-11-01 21:20:15.568081
# Unit test for method run of class LookupModule
def test_LookupModule_run():from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.plugins.lookup.random_choice import LookupModule


# Unit test for method run of class LookupModule
def test_LookupModule_run(mocker):
    lookup_module = LookupModule()

    # When terms is empty (falsy), run should return terms unchanged
    assert lookup_module.run([]) == []
    assert lookup_module.run(None) is None

    # When terms is a non-empty list, run should return a single element from it
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup_module.run(terms)
    assert len(result) == 1
    assert result[0] in terms

    # Mock random.choice to control the selected element
    mock_choice = mocker.patch('ansible.plugins.lookup.random_choice.random.choice')
    mock_choice.return_value = 'drink from the goblet'

    result = lookup_module.run(terms)
    assert result == ['drink from the goblet']
    mock_choice.assert_called_once_with(terms)

    # When random.choice raises an exception, an AnsibleError should be raised
    mock_choice.side_effect = Exception('random failure')
    with pytest.raises(AnsibleError) as excinfo:
        lookup_module.run(terms)
    assert 'Unable to choose random term: random failure' in to_native(excinfo.value)

# Generated at 2026-11-01 21:20:24.067424
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_native

    lookup = LookupModule()

    # Empty terms are returned as-is
    assert lookup.run([]) == []

    # None terms are returned as-is
    assert lookup.run(None) is None

    # Non-empty terms: a single randomly chosen element is returned
    terms = ['go through the door', 'drink from the goblet', 'press the red button', 'do nothing']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Single element list always returns that element
    assert lookup.run(['only choice']) == ['only choice']

    # Repeated runs must always return an element from the original terms
    for _ in range(20):
        assert lookup.run(terms)[0] in terms

    # If random.choice fails, an AnsibleError with a useful message is raised
    with patch('random.choice', side_effect=ValueError('boom')):
        with pytest.raises(AnsibleError) as exc_info:
            lookup.run(['a', 'b'])
    assert 'Unable to choose random term: boom' in to_native(exc_info.value)

# Generated at 2026-11-01 21:20:55.711848
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    return LookupModule()


def test_run_empty_terms(lookup):
    """Empty terms list should be returned unchanged."""
    assert lookup.run([]) == []
    assert lookup.run([], inject={}) == []


def test_run_none_terms(lookup):
    """Falsy terms (None) should be passed through untouched."""
    assert lookup.run(None) is None


def test_run_single_term(lookup):
    assert lookup.run(['only-choice']) == ['only-choice']


def test_run_returns_one_element_from_terms(lookup):
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_does_not_modify_original_terms(lookup):
    terms = ['a', 'b', 'c']
    expected = list(terms)

    lookup.run(terms)

    assert terms == expected


@patch('ansible.plugins.lookup.random_choice.random.choice')
def test_run_delegates_to_random_choice(mock_choice, lookup):
    mock_choice.return_value = 'picked'
    terms = ['a', 'b', 'c']

    result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert result == ['picked']


@patch('ansible.plugins.lookup.random_choice.random.choice')
def test_run_wraps_choice_result_in_list(mock_choice, lookup):
    mock_choice.return_value = 42

    result = lookup.run([1, 2, 3])

    assert result == [42]
    assert isinstance(result, list)


def test_run_invalid_terms_raises_ansible_error(lookup):
    """A non-sequence term (int) makes random.choice fail, which must be wrapped in AnsibleError."""
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(42)

    assert 'Unable to choose random term' in str(excinfo.value)


@patch('ansible.plugins.lookup.random_choice.random.choice', side_effect=ValueError('boom'))
def test_run_exception_is_wrapped_in_ansible_error(mock_choice, lookup):
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])

    assert str(excinfo.value) == 'Unable to choose random term: boom'


def test_run_accepts_extra_kwargs(lookup):
    terms = ['x', 'y', 'z']

    result = lookup.run(terms, variables={}, some_kwarg='ignored')

    assert len(result) == 1
    assert result[0] in terms

# Generated at 2026-11-01 21:21:01.237860
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_LookupModule_run(mocker):
    lookup = LookupModule()

    # Empty/falsy terms are returned as-is
    assert lookup.run([]) == []
    assert lookup.run(None) is None

    # Non-empty terms: returns a single element drawn from terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms

    # Deterministic behavior via mocked random.choice
    mocker.patch('ansible.plugins.lookup.random_choice.random.choice',
                 return_value='drink from the goblet')
    assert lookup.run(terms) == ['drink from the goblet']

    # Exception inside random.choice is wrapped in AnsibleError
    mocker.patch('ansible.plugins.lookup.random_choice.random.choice',
                 side_effect=Exception('boom'))
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(terms)
    assert 'Unable to choose random term: boom' in to_native(excinfo.value)

# Generated at 2026-11-01 21:21:09.839555
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty terms should be returned as-is
    assert lookup.run([]) == []

    # None terms should be returned as-is
    assert lookup.run(None) is None

    # Non-empty terms: should return a list with exactly one element from the input
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Single-element list should return that element
    assert lookup.run(['only-choice']) == ['only-choice']

    # Deterministic behavior when random.choice is mocked
    with mock.patch.object(random, 'choice', return_value='b'):
        assert lookup.run(['a', 'b', 'c']) == ['b']

    # Exception inside random.choice should be wrapped in AnsibleError
    with mock.patch.object(random, 'choice', side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a', 'b'])
    assert 'Unable to choose random term' in to_native(excinfo.value)

# Generated at 2026-11-01 21:21:25.510695
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    return LookupModule()


def test_run_with_empty_terms(lookup):
    assert lookup.run([]) == []


def test_run_with_none_terms(lookup):
    assert lookup.run(None) is None


def test_run_with_single_term(lookup):
    terms = ['only_option']
    assert lookup.run(terms) == ['only_option']


def test_run_returns_one_element_from_terms(lookup):
    terms = ['go through the door', 'drink from the goblet', 'press the red button', 'do nothing']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_with_non_string_items(lookup):
    terms = [1, 2, 3, ('a', 'b')]
    result = lookup.run(terms)
    assert result[0] in terms


def test_run_with_duplicate_items(lookup):
    assert lookup.run(['x', 'x', 'x']) == ['x']


def test_run_delegates_to_random_choice(lookup):
    terms = ['a', 'b', 'c']
    with patch('random.choice', return_value='b') as mock_choice:
        result = lookup.run(terms)
    mock_choice.assert_called_once_with(terms)
    assert result == ['b']


def test_run_wraps_exceptions_in_ansible_error(lookup):
    with patch('random.choice', side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as err:
            lookup.run(['a', 'b'])
    assert 'Unable to choose random term: boom' in str(err.value)


def test_run_with_dict_terms_uses_keys(lookup):
    terms = {'key1': 'val1', 'key2': 'val2'}
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_run_does_not_mutate_terms(lookup):
    terms = ['a', 'b', 'c']
    original = list(terms)
    lookup.run(terms)
    assert terms == original

# Generated at 2026-11-01 21:21:30.219328
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Non-empty terms: should return a list containing one element from terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Empty list should be returned as-is
    assert lookup.run([]) == []

    # None should be returned as-is
    assert lookup.run(None) is None


def test_LookupModule_run_single_term():
    lookup = LookupModule()
    result = lookup.run(['only-choice'])
    assert result == ['only-choice']


def test_LookupModule_run_mocked_choice(monkeypatch):
    lookup = LookupModule()
    terms = ['x', 'y', 'z']
    monkeypatch.setattr(random, 'choice', lambda seq: 'y')
    assert lookup.run(terms) == ['y']


def test_LookupModule_run_error(monkeypatch):
    lookup = LookupModule()

    def fail(seq):
        raise ValueError('boom')

    monkeypatch.setattr(random, 'choice', fail)
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])
    assert 'Unable to choose random term: boom' in to_native(excinfo.value)


def to_native(value):
    return str(value)

# Generated at 2026-11-01 21:21:42.735049
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # No terms / empty list -> returned unchanged (empty list)
    assert lookup.run([]) == []

    # Falsy input (None) -> returned as-is
    assert lookup.run(None) is None

    # Single term -> always that term, wrapped in a list
    assert lookup.run(['only-one']) == ['only-one']

    # Multiple terms -> exactly one element is returned,
    # and it must be one of the original terms
    terms = ['go through the door', 'drink from the goblet',
             'press the red button', 'do nothing']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Original terms list is not mutated by the lookup
    assert terms == ['go through the door', 'drink from the goblet',
                     'press the red button', 'do nothing']


def test_LookupModule_run_deterministic_choice():
    lookup = LookupModule()

    # Force random.choice to always pick the first element
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=lambda seq: seq[0]):
        result = lookup.run(['first', 'second', 'third'])
    assert result == ['first']


def test_LookupModule_run_handles_exception():
    lookup = LookupModule()

    # Make random.choice blow up; module_0.run() must convert it to AnsibleError
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=ValueError('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a', 'b'])

    assert 'Unable to choose random term' in str(excinfo.value)
    assert 'boom' in str(excinfo.value)


def test_LookupModule_run_does_not_raise_on_empty():
    lookup = LookupModule()

    # With falsy terms, random.choice is never invoked,
    # so no error should surface even if choice would fail
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=ValueError('should not be called')):
        assert lookup.run([]) == []

# Generated at 2026-11-01 21:21:53.157822
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Non-empty terms: returns a single-element list drawn from terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    for _ in range(10):
        result = lookup_module.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms

    # Single-element list is deterministic
    assert lookup_module.run(["only-choice"]) == ["only-choice"]

    # Empty / falsy terms are returned as-is
    assert lookup_module.run([]) == []
    assert lookup_module.run(None) is None

    # Exceptions from random.choice are wrapped in AnsibleError
    with patch("random.choice", side_effect=Exception("boom")):
        try:
            lookup_module.run(["a", "b"])
        except AnsibleError as e:
            assert "Unable to choose random term" in to_native(e)
            assert "boom" in to_native(e)
        else:
            raise AssertionError("AnsibleError was not raised")

# Generated at 2026-11-01 21:22:29.715629
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.random_choice import LookupModule

    # Test with empty terms (falsy) - should return terms as-is
    lookup_plugin = LookupModule()
    assert lookup_plugin.run([]) == []

    # Test with None terms - should return None as-is
    assert lookup_plugin.run(None) is None

    # Test with non-empty terms - should return a list with one element
    terms = ['go through the door', 'drink from the goblet', 'press the red button', 'do nothing']
    result = lookup_plugin.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Test with single-element list
    result = lookup_plugin.run(['only_choice'])
    assert result == ['only_choice']

    # Test that random.choice is called with the terms
    with patch('ansible.plugins.lookup.random_choice.random.choice', return_value=['picked']) as mock_choice:
        result = lookup_plugin.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ['picked']

# Generated at 2026-11-01 21:22:50.400285
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Non-empty list should return a list containing a single element from the input
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Empty (falsy) terms should be returned unchanged
    assert lookup.run([]) == []

    # Single element list should return that element
    assert lookup.run(["only choice"]) == ["only choice"]


def test_LookupModule_run_error(monkeypatch):
    lookup = LookupModule()

    def fake_choice(seq):
        raise ValueError("boom")

    monkeypatch.setattr(random, "choice", fake_choice)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["a", "b"])
    assert "Unable to choose random term: boom" in to_native(excinfo.value)

# Generated at 2026-11-01 21:23:07.193052
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty / falsy terms are returned as-is
    assert lookup.run([]) == []
    assert lookup.run(None) is None

    # Single term - must return a list containing that term
    assert lookup.run(['only_choice']) == ['only_choice']

    # Multiple terms - must return exactly one of the given terms
    terms = [
        'go through the door',
        'drink from the goblet',
        'press the red button',
        'do nothing',
    ]
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms

    # Exception during random.choice is wrapped in AnsibleError
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as exc_info:
            lookup.run(['a', 'b'])
    assert 'Unable to choose random term: boom' in str(exc_info.value)

# Generated at 2026-11-01 21:23:39.808886
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Empty terms are returned as-is
    assert lookup_module.run([]) == []

    # None (falsy) is returned as-is
    assert lookup_module.run(None) is None

    # Single term list returns that term wrapped in a list
    assert lookup_module.run(['only-one']) == ['only-one']

    # Multiple terms: result is a one-element list containing a member of terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button', 'do nothing']
    result = lookup_module.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # inject and kwargs are accepted and ignored
    result = lookup_module.run(terms, inject={'some': 'vars'}, variables=None)
    assert result[0] in terms

    # random.choice is used and its result is wrapped in a list
    with patch('random.choice', return_value='press the red button') as mock_choice:
        result = lookup_module.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ['press the red button']

    # Exceptions from random.choice are converted to AnsibleError
    with patch('random.choice', side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup_module.run(terms)
        assert 'Unable to choose random term: boom' in to_native(excinfo.value)

# Generated at 2026-11-01 21:23:51.438289
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_run_empty_terms():
    """Empty list should be returned as-is without invoking random.choice."""
    lookup = LookupModule()
    result = lookup.run([])
    assert result == []


def test_run_none_terms():
    """None should be returned as-is."""
    lookup = LookupModule()
    result = lookup.run(None)
    assert result is None


def test_run_single_term():
    """A single-element list should return that element in a list."""
    lookup = LookupModule()
    result = lookup.run(['only_choice'])
    assert result == ['only_choice']


def test_run_multiple_terms():
    """Result should be a list containing exactly one element from the input terms."""
    lookup = LookupModule()
    terms = ['go through the door', 'drink from the goblet', 'press the red button', 'do nothing']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


@patch('ansible.plugins.lookup.random_choice.random.choice', side_effect=Exception('boom'))
def test_run_exception_raises_ansible_error(mock_choice):
    """If random.choice raises, an AnsibleError should be raised with the message."""
    lookup = LookupModule()
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])
    assert 'Unable to choose random term: boom' in str(excinfo.value)
    mock_choice.assert_called_once_with(['a', 'b'])


@patch('ansible.plugins.lookup.random_choice.random.choice', return_value='red button')
def test_run_uses_random_choice(mock_choice):
    """run should delegate to random.choice and wrap its return value in a list."""
    lookup = LookupModule()
    terms = ['go through the door', 'press the red button']
    result = lookup.run(terms)
    mock_choice.assert_called_once_with(terms)
    assert result == ['red button']

# Generated at 2026-11-01 21:24:04.539115
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_LookupModule_run_empty_list():
    lookup = LookupModule()
    result = lookup.run([])
    assert result == []


def test_LookupModule_run_none():
    lookup = LookupModule()
    result = lookup.run(None)
    assert result is None


def test_LookupModule_run_single_element():
    lookup = LookupModule()
    result = lookup.run(["only_option"])
    assert result == ["only_option"]


def test_LookupModule_run_returns_one_element_from_terms():
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_LookupModule_run_uses_random_choice():
    lookup = LookupModule()
    with patch('ansible.plugins.lookup.random_choice.random.choice', return_value="picked") as mock_choice:
        result = lookup.run(["a", "b", "c"])
    mock_choice.assert_called_once_with(["a", "b", "c"])
    assert result == ["picked"]


def test_LookupModule_run_accepts_inject_and_kwargs():
    lookup = LookupModule()
    terms = ["a", "b", "c"]
    result = lookup.run(terms, inject={"foo": "bar"}, variables={"baz": "qux"})
    assert len(result) == 1
    assert result[0] in terms


def test_LookupModule_run_raises_ansible_error_on_failure():
    lookup = LookupModule()
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=Exception("boom")):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(["term1", "term2"])
    assert "Unable to choose random term: boom" in str(excinfo.value)


def test_LookupModule_run_non_list_terms():
    lookup = LookupModule()
    # non-list truthy sequence still goes through random.choice
    result = lookup.run(("a", "b"))
    assert len(result) == 1
    assert result[0] in ("a", "b")

# Generated at 2026-11-01 21:24:25.634264
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest

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
    result = lookup.run(['only-choice'])
    assert result == ['only-choice']


def test_LookupModule_run_multiple_terms():
    lookup = LookupModule()
    terms = ['go through the door', 'drink from the goblet',
             'press the red button', 'do nothing']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_LookupModule_run_returns_element_from_original_list(mocker):
    mocker.patch('ansible.plugins.lookup.random_choice.random.choice',
                 return_value='drink from the goblet')
    lookup = LookupModule()
    result = lookup.run(['go through the door', 'drink from the goblet'])
    assert result == ['drink from the goblet']


def test_LookupModule_run_error_wrapped_in_ansible_error(mocker):
    mocker.patch('ansible.plugins.lookup.random_choice.random.choice',
                 side_effect=TypeError('boom'))
    lookup = LookupModule()
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['term'])
    assert 'Unable to choose random term: boom' in str(excinfo.value)


def test_LookupModule_run_unindexable_terms_raises_ansible_error():
    lookup = LookupModule()
    with pytest.raises(AnsibleError):
        lookup.run(42)

# Generated at 2026-11-01 21:24:48.365953
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_LookupModule_run_returns_terms_when_empty():
    lookup = LookupModule()

    # Empty list should be returned as-is
    assert lookup.run([]) == []

    # None should be returned as-is (falsy)
    assert lookup.run(None) is None


def test_LookupModule_run_returns_single_element_from_list():
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet", "press the red button"]

    result = lookup.run(terms)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_LookupModule_run_with_single_term():
    lookup = LookupModule()

    result = lookup.run(["only-choice"])

    assert result == ["only-choice"]


@patch('ansible.plugins.lookup.random_choice.random.choice')
def test_LookupModule_run_uses_random_choice(mock_choice):
    mock_choice.return_value = "picked"

    lookup = LookupModule()
    result = lookup.run(["a", "b", "c"])

    mock_choice.assert_called_once_with(["a", "b", "c"])
    assert result == ["picked"]


@patch('ansible.plugins.lookup.random_choice.random.choice')
def test_LookupModule_run_wraps_exceptions_in_ansible_error(mock_choice):
    mock_choice.side_effect = Exception("boom")

    lookup = LookupModule()

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["some-term"])

    assert "Unable to choose random term: boom" in to_native_error(excinfo.value)


def to_native_error(error):
    from ansible.module_utils._text import to_native
    return to_native(error)

# Generated at 2026-11-01 21:25:18.781498
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    return LookupModule()


def test_lookup_module_run_empty_terms(lookup):
    """Empty list should be returned unchanged."""
    assert lookup.run([]) == []


def test_lookup_module_run_none_terms(lookup):
    """None is falsy, so it should be returned unchanged."""
    assert lookup.run(None) is None


def test_lookup_module_run_single_term(lookup):
    """A single-item list must always yield that item."""
    assert lookup.run(['only_choice']) == ['only_choice']


def test_lookup_module_run_multiple_terms(lookup):
    """Result must be a list containing exactly one of the given terms."""
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_lookup_module_run_with_inject(lookup):
    """inject argument is accepted and does not affect the outcome."""
    terms = ['x', 'y', 'z']
    result = lookup.run(terms, inject={'foo': 'bar'})

    assert len(result) == 1
    assert result[0] in terms


def test_lookup_module_run_uses_random_choice(lookup):
    """Ensure random.choice's return value is wrapped in a list."""
    terms = ['a', 'b', 'c']
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               return_value='b') as mock_choice:
        result = lookup.run(terms)

    mock_choice.assert_called_once_with(terms)
    assert result == ['b']


def test_lookup_module_run_string_terms(lookup):
    """A non-empty string is truthy; choice picks a character from it."""
    result = lookup.run('abc')

    assert len(result) == 1
    assert result[0] in 'abc'


def test_lookup_module_run_unchoosable_terms_raises_ansible_error(lookup):
    """An object that random.choice cannot handle should raise AnsibleError."""
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(42)

    assert 'Unable to choose random term' in str(excinfo.value)


def test_lookup_module_run_wraps_underlying_exception_message(lookup):
    """The original exception message should be included in the AnsibleError."""
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=ValueError('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a'])

    assert 'boom' in str(excinfo.value)

# Generated at 2026-11-01 21:25:41.002893
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_LookupModule_run_empty_list():
    """An empty terms list should be returned unchanged."""
    lookup = LookupModule()
    assert lookup.run([]) == []


def test_LookupModule_run_none():
    """None terms should be returned unchanged (falsy branch)."""
    lookup = LookupModule()
    assert lookup.run(None) is None


def test_LookupModule_run_single_term():
    """With one term, that term must always be the result."""
    lookup = LookupModule()
    assert lookup.run(["only_option"]) == ["only_option"]


def test_LookupModule_run_picks_exactly_one_from_terms():
    """Result must be a single-element list containing a member of terms."""
    lookup = LookupModule()
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


def test_LookupModule_run_delegates_to_random_choice():
    """module_0.run() should delegate selection to random.choice over the terms."""
    lookup = LookupModule()
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice", return_value="picked"
    ) as mock_choice:
        result = lookup.run(["a", "b", "c"])
    mock_choice.assert_called_once_with(["a", "b", "c"])
    assert result == ["picked"]


def test_LookupModule_run_wraps_errors_in_ansible_error():
    """Exceptions raised while choosing must surface as AnsibleError."""
    lookup = LookupModule()
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=ValueError("boom"),
    ):
        with pytest.raises(AnsibleError) as exc_info:
            lookup.run(["a", "b"])
    assert "Unable to choose random term: boom" in str(exc_info.value)


def test_LookupModule_run_does_not_mutate_terms():
    """The original terms collection must remain unmodified."""
    lookup = LookupModule()
    terms = ["x", "y", "z"]
    lookup.run(terms)
    assert terms == ["x", "y", "z"]


def test_LookupModule_run_accepts_extra_kwargs():
    """Additional keyword arguments should be tolerated."""
    lookup = LookupModule()
    result = lookup.run(["term1", "term2"], inject={}, variables={"foo": "bar"})
    assert len(result) == 1
    assert result[0] in ("term1", "term2")


def test_LookupModule_run_results_are_repeatable_shape():
    """Repeated calls always yield a one-item list of original members."""
    lookup = LookupModule()
    terms = ["a", "b", "c"]
    for _ in range(10):
        result = lookup.run(terms)
        assert result == [result[0]]
        assert result[0] in terms

# Generated at 2026-11-01 21:25:58.613916
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_run_empty_terms():
    lookup = LookupModule()
    assert lookup.run([]) == []


def test_run_none_terms():
    lookup = LookupModule()
    assert lookup.run(None) is None


def test_run_single_term():
    lookup = LookupModule()
    result = lookup.run(['only_choice'])
    assert result == ['only_choice']


def test_run_multiple_terms_returns_one_member():
    lookup = LookupModule()
    terms = ['go through the door', 'drink from the goblet', 'press the red button']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_exception_wrapped_in_ansible_error():
    lookup = LookupModule()
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a', 'b'])
    assert 'Unable to choose random term: boom' in str(excinfo.value)


def test_run_falsy_terms_returned_unchanged():
    lookup = LookupModule()
    assert lookup.run('') == ''
    assert lookup.run(0) == 0

# Generated at 2026-11-01 21:26:14.077847
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Test LookupModule.run'''
    lookup = LookupModule()

    # Empty or falsy terms are returned as-is
    assert lookup.run([]) == []
    assert lookup.run(None) is None

    # A single term is always chosen
    assert lookup.run(['only']) == ['only']

    # Multiple terms: exactly one element, and it must be one of the given terms
    terms = ['go through the door', 'drink from the goblet', 'press the red button', 'do nothing']
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # Non-sequence terms cause random.choice to fail -> AnsibleError
    with pytest.raises(AnsibleError):
        lookup.run(42)

# Generated at 2026-11-01 21:26:38.300076
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-11-01 21:27:10.389547
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty/falsy terms are returned unchanged
    assert lookup.run([]) == []
    assert lookup.run(None) is None

    # Non-empty terms yield exactly one randomly selected element
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

    # Deterministic behavior when random.choice is patched
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               return_value='press the red button'):
        assert lookup.run(terms) == ['press the red button']

    # Exceptions from random.choice are wrapped in AnsibleError
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=ValueError('boom')):
        with pytest.raises(AnsibleError,
                           match='Unable to choose random term: boom'):
            lookup.run(terms)

# Generated at 2026-11-01 21:27:48.590608
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_run_empty_terms():
    lookup = LookupModule()
    assert lookup.run([]) == []


def test_run_none_terms():
    lookup = LookupModule()
    assert lookup.run(None) is None


def test_run_single_term():
    lookup = LookupModule()
    assert lookup.run(['only']) == ['only']


def test_run_multiple_terms():
    lookup = LookupModule()
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


def test_run_with_kwargs():
    lookup = LookupModule()
    terms = ['a', 'b', 'c']
    result = lookup.run(terms, inject=None, variables={'foo': 'bar'})
    assert len(result) == 1
    assert result[0] in terms


def test_run_error_raises_ansible_error():
    lookup = LookupModule()
    with patch('random.choice', side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a', 'b'])
    assert 'Unable to choose random term: boom' in to_native(excinfo.value)


def from_ansible_module_utils_text_import():
    pass


# helper import placed after tests to mirror source usage
from ansible.module_utils._text import to_native  # noqa: E402

# Generated at 2026-11-01 21:28:20.233259
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Test LookupModule.run returns a single random element from terms.'''
    lookup = LookupModule()

    # Non-empty list: should return a list with exactly one member of terms
    terms = ['go through the door', 'drink from the goblet',
             'press the red button', 'do nothing']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Single-element list: returns that element
    assert lookup.run(['only-option']) == ['only-option']

    # Empty list is returned as-is
    assert lookup.run([]) == []

    # None is returned as-is (falsy terms short-circuit)
    assert lookup.run(None) is None


# Unit test for error handling in run of class LookupModule
def test_LookupModule_run_error():
    '''Test that exceptions from random.choice are wrapped in AnsibleError.'''
    lookup = LookupModule()

    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=Exception('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a', 'b'])

    assert 'Unable to choose random term' in to_native(excinfo.value)
    assert 'boom' in to_native(excinfo.value)

# Generated at 2026-11-01 21:28:53.616118
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    return LookupModule()


def test_empty_terms_returns_empty_list(lookup):
    """An empty terms list should be returned unchanged."""
    assert lookup.run([]) == []


def test_none_terms_returned_unchanged(lookup):
    """Falsy terms (None) bypass random.choice entirely."""
    assert lookup.run(None) is None


def test_single_term_list(lookup):
    """A single-element list must always yield that element."""
    assert lookup.run(['only']) == ['only']


def test_result_contains_exactly_one_item_from_terms(lookup):
    terms = ['a', 'b', 'c']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_input_terms_not_mutated(lookup):
    terms = ['a', 'b', 'c']
    original = list(terms)
    lookup.run(terms)
    assert terms == original


def test_random_choice_called_and_result_used(lookup):
    """Mock random.choice to verify its return value is wrapped in a list."""
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               return_value='b') as mock_choice:
        result = lookup.run(['a', 'b', 'c'])
    mock_choice.assert_called_once_with(['a', 'b', 'c'])
    assert result == ['b']


def test_exception_wrapped_in_ansible_error(lookup):
    """Any exception from random.choice is converted to AnsibleError."""
    with patch('ansible.plugins.lookup.random_choice.random.choice',
               side_effect=ValueError('boom')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['a', 'b'])
    assert 'Unable to choose random term' in str(excinfo.value)
    assert 'boom' in str(excinfo.value)


def test_unhashable_terms_do_not_crash_lookup_logic(lookup):
    """random.choice works fine on lists containing unhashable items."""
    terms = [{'k': 1}, {'k': 2}]
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_tuple_terms_supported(lookup):
    """Sequences like tuples work as terms input."""
    result = lookup.run(('a', 'b', 'c'))
    assert len(result) == 1
    assert result[0] in ('a', 'b', 'c')


def test_repeated_runs_stay_within_terms(lookup):
    """Statistical sanity check: many runs only ever select known terms."""
    terms = ['x', 'y', 'z']
    for _ in range(100):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms