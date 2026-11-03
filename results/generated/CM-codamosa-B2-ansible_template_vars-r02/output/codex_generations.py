

# Generated at 2026-11-02 22:50:01.993727
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MockTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}

    templar = MockTemplar(available_variables={'host_var': 'host_value'})
    globals_dict = {'global_var': 'global_value'}
    locals_dict = {
        'l_local_var': 'local_value',
        'plain_var': 'plain_value',
        'context': 'ctx',
        'environment': 'env',
        'template': 'tpl',
        'skipped': missing,
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # local vars with 'l_' prefix have the prefix stripped
    assert 'local_var' in j2vars
    # plain local keys are kept
    assert 'plain_var' in j2vars
    # reserved jinja2 keys are excluded from locals
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars
    # 'missing' sentinel values are excluded
    assert 'skipped' not in j2vars

    # templar available variables
    assert 'host_var' in j2vars

    # globals
    assert 'global_var' in j2vars

    # undefined variables
    assert 'undefined_var' not in j2vars

# Generated at 2026-11-02 22:55:37.873212
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock

    # Build a mock templar with a set of available variables
    templar = MagicMock()
    templar.available_variables = {'host_var': 'host_value'}
    templar.template.return_value = 'templated_host_value'

    globals_dict = {'global_var': 'global_value', 'range': range}
    locals_dict = {'l_local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Local variables are returned directly, without templating
    assert j2vars['local_var'] == 'local_value'
    templar.template.assert_not_called()

    # Variables from the templar's available_variables are templated
    assert j2vars['host_var'] == 'templated_host_value'
    templar.template.assert_called_once_with('host_value')

    # Globals are returned as-is
    assert j2vars['global_var'] == 'global_value'
    assert j2vars['range'] is range

    # Undefined variables raise a KeyError
    try:
        j2vars['undefined_var']
    except KeyError as e:
        assert 'undefined variable: undefined_var' in to_native(e)
    else:
        raise AssertionError("KeyError not raised for undefined variable")

    # The special 'vars' dict is returned as-is, without templating
    templar.template.reset_mock()
    templar.available_variables['vars'] = {'a': 1}
    assert j2vars['vars'] == {'a': 1}
    templar.template.assert_not_called()

    # HostVars instances are returned as-is
    from ansible.vars.hostvars import HostVars
    hostvars_obj = MagicMock(spec=HostVars)
    templar.available_variables['hostvars'] = hostvars_obj
    assert j2vars['hostvars'] is hostvars_obj
    templar.template.assert_not_called()

    # Objects marked with __UNSAFE__ are returned as-is
    class UnsafeString(object):
        __UNSAFE__ = True

    unsafe_obj = UnsafeString()
    templar.available_variables['unsafe_var'] = unsafe_obj
    assert j2vars['unsafe_var'] is unsafe_obj
    templar.template.assert_not_called()