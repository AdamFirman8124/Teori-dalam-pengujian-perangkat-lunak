

# Generated at 2026-11-03 03:44:11.715335
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.template import AnsibleJ2Vars

    mock_templar = MagicMock()
    mock_templar.available_variables = dict(templar_var='raw_value')
    mock_templar.template.side_effect = lambda v: 'templated:%s' % v

    mock_globals = dict(global_var='global_value')
    j2vars = AnsibleJ2Vars(mock_templar, mock_globals, locals=dict(local_var='local_value'))

    # locals are returned as-is, without templating
    assert j2vars['local_var'] == 'local_value'
    mock_templar.template.assert_not_called()

    # templar available_variables are templated
    assert j2vars['templar_var'] == 'templated:raw_value'

    # globals are returned as-is
    assert j2vars['global_var'] == 'global_value'

    # unknown variables raise KeyError
    try:
        j2vars['missing_var']
    except KeyError:
        pass
    else:
        raise AssertionError("expected KeyError for 'missing_var'")

    # the special 'vars' dict is returned untemplated
    special_vars = dict(a=1)
    mock_templar.available_variables = dict(vars=special_vars)
    assert j2vars['vars'] is special_vars

    # unsafe variables are returned as-is
    class UnsafeObject(object):
        __UNSAFE__ = True

    unsafe = UnsafeObject()
    mock_templar.available_variables = dict(unsafe_var=unsafe)
    assert j2vars['unsafe_var'] is unsafe

    # AnsibleUndefinedVariable is caught and re-raised with context
    def _raise_undefined(value):
        raise AnsibleUndefinedVariable('undefined')

    mock_templar.template.side_effect = _raise_undefined
    mock_templar.available_variables = dict(undefined_var='undef')
    try:
        j2vars['undefined_var']
    except AnsibleUndefinedVariable:
        pass
    else:
        raise AssertionError('expected AnsibleUndefinedVariable')

    # any other exception is wrapped in AnsibleError
    def _raise_other(value):
        raise Exception('boom')

    mock_templar.template.side_effect = _raise_other
    mock_templar.available_variables = dict(error_var='err')
    try:
        j2vars['error_var']
    except AnsibleError:
        pass
    else:
        raise AssertionError('expected AnsibleError')

    # add_locals returns a copy whose locals are also resolvable via __getitem__
    new_j2vars = j2vars.add_locals(dict(extra='added'))
    assert new_j2vars['extra'] == 'added'
    assert new_j2vars is not j2vars

    # add_locals with None returns the same object
    assert j2vars.add_locals(None) is j2vars

# Generated at 2026-11-03 03:47:13.989404
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    from unittest.mock import MagicMock

    templar = MagicMock()
    templar.available_variables = {'available_var': 'available_value'}
    globals_dict = {'global_var': 'global_value'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Passing None should return the same object
    assert j2vars.add_locals(None) is j2vars

    # Add new locals, including one overriding an existing local
    new_locals = {'new_var': 'new_value', 'local_var': 'overridden_value'}
    result = j2vars.add_locals(new_locals)

    # Result should be a new AnsibleJ2Vars instance sharing templar and globals
    assert isinstance(result, AnsibleJ2Vars)
    assert result is not j2vars
    assert result._templar is templar
    assert result._globals is globals_dict

    # Original object's locals must remain unchanged
    assert j2vars._locals == {'local_var': 'local_value'}
    assert 'new_var' not in j2vars._locals
    assert 'local_var' not in templar.available_variables

    # New object should contain old locals, updated locals, and new locals
    assert result._locals['local_var'] == 'overridden_value'
    assert result._locals['new_var'] == 'new_value'

    # Lookups through the new proxy should reflect the merged locals
    assert result['local_var'] == 'overridden_value'
    assert result['new_var'] == 'new_value'
    assert result['global_var'] == 'global_value'
    assert 'new_var' in result
    assert len(result) == 4  # available_var, global_var, local_var, new_var

# Generated at 2026-11-03 03:51:08.482999
# Unit test for method __getitem__ of class AnsibleJ2Vars