

# Generated at 2026-11-02 18:00:12.788068
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from unittest.mock import Mock
    from ansible.template import AnsibleJ2Vars

    # Setup templar mock with available variables
    templar = Mock()
    templar.available_variables = {'var1': 'value1', 'var2': 'value2'}

    # Globals include a jinja2 builtin and a key shadowing an available variable
    globals_dict = {'global1': 'gvalue1', 'range': range, 'var1': 'shadowed'}

    # Locals: 'l_' prefixed keys get stripped, reserved names and missing values are dropped
    locals_dict = {
        'l_local1': 'lvalue1',
        'local2': 'lvalue2',
        'context': 'ctx',
        'environment': 'env',
        'template': 'tpl',
        'skipped': missing,
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    keys = set(j2vars)

    # Union of templar variables, processed locals and globals, deduplicated
    assert keys == {'var1', 'var2', 'global1', 'range', 'local1', 'local2'}

    # __iter__ must return a real iterator
    it = j2vars.__iter__()
    assert hasattr(it, '__next__')
    assert set(it) == keys

    # Empty case: no variables anywhere yields an empty iteration
    empty_templar = Mock()
    empty_templar.available_variables = {}
    empty_vars = AnsibleJ2Vars(empty_templar, {})
    assert list(empty_vars) == []
    assert len(empty_vars) == 0

# Generated at 2026-11-02 18:01:38.366482
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import AnsibleJ2Vars
    from jinja2.utils import missing

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables

    # Keys should come from templar available_variables, globals, and locals
    templar = FakeTemplar({'var_a': 1, 'var_b': 2, 'shared': 'from_available'})
    globals_dict = {'range': range, 'shared': 'from_globals'}
    locals_dict = {
        'l_var_c': 3,            # 'l_' prefix is stripped -> 'var_c'
        'context': 'ctx',        # special name, excluded
        'environment': 'env',    # special name, excluded
        'template': 'tpl',       # special name, excluded
        'missing_var': missing,  # missing sentinel value, excluded
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    result = j2vars.__iter__()
    keys = set(result)

    assert keys == {'var_a', 'var_b', 'shared', 'range', 'var_c'}

    # __iter__ must return an iterator object
    it = j2vars.__iter__()
    assert iter(it) is it

    # duplicates across scopes are deduplicated (set semantics)
    assert len(list(j2vars.__iter__())) == len(keys)

    # empty scopes yield no keys
    empty = AnsibleJ2Vars(FakeTemplar({}), {})
    assert set(empty.__iter__()) == set()
    assert len(list(empty.__iter__())) == 0

# Generated at 2026-11-02 18:04:05.573537
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from jinja2.utils import missing

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables

    templar = FakeTemplar({'available_var': 1, 'vars': {}})
    globals_dict = {'global_var': 2, 'range': range, 'lookup': lookup_stub}
    locals_dict = {
        'l__underscore_local': 'a',
        'l_plain_local': 'b',
        'context': 'should be skipped',
        'environment': 'should be skipped',
        'template': 'should be skipped',
    }

    def lookup_stub(*args, **kwargs):
        return None

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # locals with 'l_' prefix are stripped and stored without prefix
    assert '_underscore_local' in j2vars
    assert 'plain_local' in j2vars

    # special keys are excluded from locals
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars

    # available_variables from templar
    assert 'available_var' in j2vars

    # globals
    assert 'global_var' in j2vars
    assert 'range' in j2vars
    assert 'lookup' in j2vars

    # missing keys
    assert 'undefined_var' not in j2vars
    assert 'l_plain_local' not in j2vars  # prefix stripped, raw key not present

    # locals with the missing sentinel value are skipped
    j2vars_missing = AnsibleJ2Vars(templar, globals_dict, locals={'l_sentinel': missing, 'l_kept': 1})
    assert 'sentinel' not in j2vars_missing
    assert 'kept' in j2vars_missing

    # no locals provided
    j2vars_no_locals = AnsibleJ2Vars(templar, globals_dict, locals=None)
    assert 'available_var' in j2vars_no_locals
    assert 'global_var' in j2vars_no_locals
    assert 'plain_local' not in j2vars_no_locals

    # locals not passed at all
    j2vars_default = AnsibleJ2Vars(templar, globals_dict)
    assert 'global_var' in j2vars_default
    assert 'plain_local' not in j2vars_default

# Generated at 2026-11-02 18:05:49.951087
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    class MockTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}

    templar = MockTemplar({'host_var': 'value'})

    # Test with no locals
    globals_dict = {'range': range, 'global_var': 123}
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict
    assert j2vars._locals == {}

    # Test with a locals dict: l_ prefix stripped, missing values skipped,
    # and reserved jinja2 context keys excluded
    locals_dict = {
        'l__locals': {'a': 1},
        'l__simple': 42,
        'l__undefined': missing,
        'l__context': 'should still be included',
        'context': 'ctx',
        'environment': 'env',
        'template': 'tpl',
        'plain_var': 'plain',
    }
    j2vars = AnsibleJ2Vars(templar, {}, locals=locals_dict)
    assert j2vars._locals == {
        '_locals': {'a': 1},
        '_simple': 42,
        '_context': 'should still be included',
        'plain_var': 'plain',
    }

    # Test with non-dict locals (should be ignored entirely)
    j2vars = AnsibleJ2Vars(templar, {}, locals='not a dict')
    assert j2vars._locals == {}

    j2vars = AnsibleJ2Vars(templar, {}, locals=None)
    assert j2vars._locals == {}

    # Test with empty locals dict
    j2vars = AnsibleJ2Vars(templar, {}, locals={})
    assert j2vars._locals == {}
# nonce:989d0409

# Generated at 2026-11-02 18:07:55.688228
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    mock_templar = MagicMock()
    mock_templar.available_variables = {'available_var': 'available_value'}

    globals_dict = {'global_var': 'global_value'}

    # locals with an 'l_' prefix get stripped, special jinja2 keys are
    # excluded, and values equal to jinja2's `missing` sentinel are dropped
    locals_dict = {
        'l_local_var': 'local_value',
        'bare_local': 'bare_value',
        'context': 'ctx',
        'environment': 'env',
        'template': 'tpl',
        'l_dropped': missing,
    }

    j2vars = AnsibleJ2Vars(mock_templar, globals_dict, locals=locals_dict)

    # variables from locals are found
    assert 'local_var' in j2vars
    assert 'bare_local' in j2vars

    # special jinja2 keys are not exposed
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars

    # jinja2 `missing` values are not exposed
    assert 'dropped' not in j2vars

    # variables from the templar's available_variables are found
    assert 'available_var' in j2vars

    # variables from globals are found
    assert 'global_var' in j2vars

    # unknown variables are not found
    assert 'undefined_var' not in j2vars