

# Generated at 2026-11-02 22:26:29.427691
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    class FakeTemplar(object):
        def __init__(self):
            self.available_variables = {}

    templar = FakeTemplar()
    globals_dict = {'range': range, 'undefined': AnsibleUndefinedVariable}

    # Constructor without locals
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict
    assert j2vars._locals == {}

    # Constructor with locals=None
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=None)
    assert j2vars._locals == {}

    # Constructor with locals: 'l_' prefixed keys are stripped,
    # special jinja2 keys and missing values are skipped
    locals_dict = {
        'l_local_var': 'local_value',
        'plain_var': 'plain_value',
        'context': 'should_be_skipped',
        'environment': 'should_be_skipped',
        'template': 'should_be_skipped',
        'missing_var': missing,
    }
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)
    assert j2vars._locals == {
        'local_var': 'local_value',
        'plain_var': 'plain_value',
    }
    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict

# Generated at 2026-11-02 22:28:08.545540
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables

    templar = FakeTemplar({'templar_var': 'value1', 'another_var': 'value2'})

    globals_dict = {'global_var': 'gvalue', 'hostvars': {}}
    locals_dict = {
        'l_local_var': 'lvalue',
        'plain_local': 'pvalue',
        'l_missing_var': missing,
        'context': 'ctx',
        'environment': 'env',
        'template': 'tpl',
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Variables available through templar.available_variables
    assert 'templar_var' in j2vars
    assert 'another_var' in j2vars

    # Variables available through globals
    assert 'global_var' in j2vars
    assert 'hostvars' in j2vars

    # Variables available through locals (with l_ prefix stripped)
    assert 'local_var' in j2vars
    assert 'plain_local' in j2vars

    # Locals with `missing` values should be dropped
    assert 'missing_var' not in j2vars
    assert 'l_missing_var' not in j2vars

    # Special local keys should be filtered out
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars

    # Undefined variables
    assert 'undefined_var' not in j2vars
    assert 'l_undefined_var' not in j2vars

    # No locals provided
    j2vars_no_locals = AnsibleJ2Vars(templar, globals_dict)
    assert 'global_var' in j2vars_no_locals
    assert 'local_var' not in j2vars_no_locals

    # Explicit __contains__ calls
    assert j2vars.__contains__('templar_var') is True
    assert j2vars.__contains__('undefined_var') is False

# Generated at 2026-11-02 22:29:14.097659
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    mock_templar = MagicMock()
    mock_templar.available_variables = {
        'templar_var': 'templar_value',
        'another_var': 'another_value',
    }

    globals_dict = {'global_var': 'global_value'}

    # No locals provided
    j2vars = AnsibleJ2Vars(mock_templar, globals_dict)

    # Variables available via the templar should be found
    assert 'templar_var' in j2vars
    assert 'another_var' in j2vars
    assert j2vars.__contains__('templar_var') is True

    # Variables in globals should be found
    assert 'global_var' in j2vars
    assert j2vars.__contains__('global_var') is True

    # Unknown variables should not be found
    assert 'missing_var' not in j2vars
    assert j2vars.__contains__('missing_var') is False

    # With locals provided (including jinja2 'l_' prefixed keys)
    locals_dict = {
        'l_local_var': 'local_value',
        'plain_local': 'plain_value',
        'context': 'should_be_skipped',
    }
    j2vars_with_locals = AnsibleJ2Vars(mock_templar, globals_dict, locals=locals_dict)

    # 'l_' prefixed locals have the prefix stripped
    assert 'local_var' in j2vars_with_locals
    assert j2vars_with_locals.__contains__('local_var') is True

    # Non-prefixed locals are kept as-is (except reserved names)
    assert 'plain_local' in j2vars_with_locals

    # Reserved name 'context' without 'l_' prefix is filtered out of locals
    assert 'context' not in j2vars_with_locals

    # Locals take precedence but all sources are still consulted
    assert 'templar_var' in j2vars_with_locals
    assert 'global_var' in j2vars_with_locals
    assert 'missing_var' not in j2vars_with_locals

# Generated at 2026-11-02 22:30:56.043241
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            if available_variables is None:
                available_variables = {}
            self.available_variables = available_variables

    # available_variables: 2 keys, globals: 2 keys (1 overlap), locals: 2 keys (1 overlap)
    templar = FakeTemplar({'foo': 'bar', 'baz': 'qux'})
    globals_dict = {'global_var': 'gv', 'foo': 'global_foo'}
    locals_dict = {'l_foo': 'local_foo', 'local_var': 'lv'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Unique keys: foo, baz, global_var, local_var == 4
    assert len(j2vars) == 4

    # locals entries whose values are the jinja2 'missing' sentinel are skipped
    locals_with_missing = {'l_foo': missing, 'local_var': 'lv'}
    j2vars_missing = AnsibleJ2Vars(templar, globals_dict, locals=locals_with_missing)
    # Unique keys: foo, baz, global_var, local_var == 4
    assert len(j2vars_missing) == 4

    # no variables in any scope
    empty_vars = AnsibleJ2Vars(FakeTemplar(), {})
    assert len(empty_vars) == 0

    # only globals defined
    only_globals = AnsibleJ2Vars(FakeTemplar(), {'g1': 'v1', 'g2': 'v2', 'g3': 'v3'})
    assert len(only_globals) == 3

# Generated at 2026-11-02 22:32:16.411314
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''Unit test for method __contains__ of class AnsibleJ2Vars'''

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables

    templar = FakeTemplar({'available_var': 'available_value', 'shared_var': 'shared_value'})
    globals_dict = {'global_var': 'global_value', 'shared_var': 'shared_global_value'}
    locals_dict = {
        'l_local_var': 'local_value',
        'plain_local': 'plain_value',
        'context': 'ctx',
        'environment': 'env',
        'template': 'tmpl',
        'skipped_var': missing,
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Variables stored in locals (l_ prefix is stripped during init)
    assert 'local_var' in j2vars
    assert 'plain_local' in j2vars
    assert j2vars.__contains__('local_var') is True

    # Keys filtered out during initialization should not be contained
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars
    assert 'skipped_var' not in j2vars

    # Variables available on the templar
    assert 'available_var' in j2vars
    assert j2vars.__contains__('available_var') is True

    # Variables available in globals
    assert 'global_var' in j2vars
    assert j2vars.__contains__('global_var') is True

    # Variable present in multiple scopes is still contained
    assert 'shared_var' in j2vars

    # Variables defined nowhere
    assert 'undefined_var' not in j2vars
    assert j2vars.__contains__('undefined_var') is False

    # Construction without locals
    j2vars_no_locals = AnsibleJ2Vars(templar, globals_dict)
    assert 'available_var' in j2vars_no_locals
    assert 'global_var' in j2vars_no_locals
    assert 'undefined_var' not in j2vars_no_locals

    # Construction with a non-dict locals argument is ignored
    j2vars_bad_locals = AnsibleJ2Vars(templar, globals_dict, locals='not-a-dict')
    assert 'available_var' in j2vars_bad_locals
    assert 'global_var' in j2vars_bad_locals
    assert 'undefined_var' not in j2vars_bad_locals