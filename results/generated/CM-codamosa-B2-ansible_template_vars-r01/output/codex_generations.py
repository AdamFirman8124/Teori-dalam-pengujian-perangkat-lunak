

# Generated at 2026-11-03 01:17:50.019541
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    """Test the constructor of AnsibleJ2Vars"""

    class FakeTemplar(object):
        def __init__(self):
            self.available_variables = {}

    templar = FakeTemplar()
    globals_dict = {'global_var': 'global_value', 'range': range}

    # Test with locals=None (default), which should result in empty _locals
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict
    assert j2vars._locals == {}

    # Test with a locals dict:
    # - 'l_' prefixed keys should have the prefix stripped
    # - 'context', 'environment', 'template' keys should be skipped
    locals_dict = {
        'l_local_var': 'local_value',
        'plain_var': 'plain_value',
        'context': 'ctx',
        'environment': 'env',
        'template': 'tmpl',
    }
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)
    assert j2vars._locals == {
        'local_var': 'local_value',
        'plain_var': 'plain_value',
    }

    # Test that entries whose value is the jinja2 'missing' sentinel are skipped
    locals_dict = {
        'l_missing_var': missing,
        'l_present_var': 'present',
    }
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)
    assert j2vars._locals == {'present_var': 'present'}

    # Test that non-dict locals are ignored entirely
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=[('l_x', 1)])
    assert j2vars._locals == {}

# Generated at 2026-11-03 01:20:21.175302
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-11-03 01:21:41.140511
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            return 'templated:%s' % value

    templar = FakeTemplar({'foo': 'bar', 'vars': {'a': 1}})
    globals_ = {'range': range, 'globalvar': 'gval'}
    locals_ = {'l_localvar': 'lval', 'l_skipped_missing': missing}
    j2vars = AnsibleJ2Vars(templar, globals_, locals=locals_)

    # local variable (stripped of 'l_' prefix) is returned as-is
    assert j2vars['localvar'] == 'lval'
    # templar variable gets templated through the templar
    assert j2vars['foo'] == 'templated:bar'
    # global is returned as-is without templating
    assert j2vars['globalvar'] == 'gval'
    # special 'vars' dict is returned as-is without templating
    assert j2vars['vars'] == {'a': 1}
    # only 'foo' was sent through the templar
    assert templar.template_calls == ['bar']

# Generated at 2026-11-03 01:23:04.177842
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader

    fake_loader = DictDataLoader({})
    variable_manager = type('VariableManager', (object,), {'available_variables': {}})()
    templar = Templar(loader=fake_loader, variables={})
    templar.available_variables = {'foo': 'bar', 'num': 1}

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: None}

    # create initial instance with some locals
    ajv = AnsibleJ2Vars(templar, globals_dict, locals={'l_x': 'local_x', 'context': 'skipme', 'template': 'skipme'})

    # locals should be stripped of l_ prefix, and special keys excluded
    assert ajv._locals == {'x': 'local_x'}
    assert 'foo' in ajv
    assert 'x' in ajv
    assert 'range' in ajv
    assert ajv['x'] == 'local_x'
    assert ajv['foo'] == 'bar'

    # add_locals with None returns the same object
    result = ajv.add_locals(None)
    assert result is ajv

    # add_locals with a dict returns a new object with merged locals
    result = ajv.add_locals({'y': 'local_y', 'x': 'updated_x'})
    assert result is not ajv
    assert isinstance(result, AnsibleJ2Vars)
    assert result._locals == {'x': 'updated_x', 'y': 'local_y'}
    # original is unchanged
    assert ajv._locals == {'x': 'local_x'}
    # new instance shares templar and globals
    assert result._templar is ajv._templar
    assert result._globals is ajv._globals
    # lookups through the new instance
    assert result['x'] == 'updated_x'
    assert result['y'] == 'local_y'
    assert result['foo'] == 'bar'
    assert 'y' in result
    assert len(result) == len(set(templar.available_variables) | set(result._locals) | set(globals_dict))

    # locals passed via constructor as jinja2 locals with l_ prefix and missing values
    from jinja2.utils import missing as j2_missing
    ajv2 = AnsibleJ2Vars(templar, globals_dict, locals={'l_a': j2_missing, 'l_b': 'val_b'})
    assert ajv2._locals == {'b': 'val_b'}

# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars_constructor():
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader

    fake_loader = DictDataLoader({})
    templar = Templar(loader=fake_loader, variables={})
    templar.available_variables = {'hostvars': object(), 'vars': {'a': 1}}

    globals_dict = {'range': range}
    ajv = AnsibleJ2Vars(templar, globals_dict)

    assert ajv._templar is templar
    assert ajv._globals is globals_dict
    assert ajv._locals == {}
    assert len(ajv) == 2
    assert 'hostvars' in ajv
    assert 'vars' in ajv
    assert 'nonexistent' not in ajv

    try:
        ajv['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("KeyError not raised for undefined variable")

# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars_getitem():
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader

    fake_loader = DictDataLoader({})
    templar = Templar(loader=fake_loader, variables={})
    templar.available_variables = {
        'plain': 'value',
        'vars': {'inner': 'special'},
        'hostvars': {'localhost': {}},
    }

    class Unsafe(object):
        __UNSAFE__ = True

    templar.available_variables['unsafe'] = Unsafe()

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    ajv = AnsibleJ2Vars(templar, globals_dict, locals={'l_local': 'localval'})

    # templated variable
    assert ajv['plain'] == 'value'
    # locals take precedence
    assert ajv['local'] == 'localval'
    # special 'vars' returned as-is
    assert ajv['vars'] == {'inner': 'special'}
    # globals returned as-is
    assert ajv['range'] is range
    assert ajv['lookup']() == 'looked_up'
    # unsafe variables returned as-is
    assert isinstance(ajv['unsafe'], Unsafe)

# Unit test for method __contains__/__iter__/__len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars_dunder_methods():
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader

    fake_loader = DictDataLoader({})
    templar = Templar(loader=fake_loader, variables={})
    templar.available_variables = {'a': 1, 'b': 2}

    globals_dict = {'g1': 1, 'g2': 2}
    ajv = AnsibleJ2Vars(templar, globals_dict, locals={'l_c': 3})

    keys = set(ajv)
    assert keys == {'a', 'b', 'g1', 'g2', 'c'}
    assert len(ajv) == 5
    assert 'a' in ajv
    assert 'b' in ajv
    assert 'c' in ajv
    assert 'g1' in ajv
    assert 'g2' in ajv
    assert 'missing' not in ajv

# Unit test for error handling in __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars_getitem_errors():
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader

    fake_loader = DictDataLoader({})

    templar = Templar(loader=fake_loader, variables={})
    templar.available_variables = {'bad_var': '{{ undefined_var }}'}

    globals_dict = {}
    ajv = AnsibleJ2Vars(templar, globals_dict)

    try:
        ajv['bad_var']
    except AnsibleUndefinedVariable as e:
        assert 'bad_var' in str(e)
    except Exception as e:
        raise AssertionError("Unexpected exception type: %s" % type(e))
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable not raised")

# Generated at 2026-11-03 01:25:10.344467
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Mock templar with available variables
    templar = MagicMock()
    templar.available_variables = {
        'templar_var': 'templar_value',
        'another_templar_var': {'nested': 'data'},
    }

    globals_dict = {
        'range': range,
        'lookup': None,
        'global_var': 'global_value',
    }

    locals_dict = {
        'l_local_var': 'local_value',
        'bare_local': 'bare_value',
        'context': 'ignored',
        'environment': 'ignored',
        'template': 'ignored',
        'l_missing_var': missing,
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Locals (with l_ prefix stripped) are contained
    assert 'local_var' in j2vars
    assert 'bare_local' in j2vars

    # Templar available variables are contained
    assert 'templar_var' in j2vars
    assert 'another_templar_var' in j2vars

    # Globals are contained
    assert 'global_var' in j2vars
    assert 'range' in j2vars
    assert 'lookup' in j2vars

    # Special jinja2 context keys are excluded from locals
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars

    # Values equal to jinja2's missing sentinel are excluded from locals
    assert 'missing_var' not in j2vars

    # Undefined variables are not contained
    assert 'undefined_var' not in j2vars


def test_AnsibleJ2Vars___contains___no_locals():
    templar = MagicMock()
    templar.available_variables = {'templar_var': 'templar_value'}

    j2vars = AnsibleJ2Vars(templar, {'global_var': 1}, locals=None)

    assert 'templar_var' in j2vars
    assert 'global_var' in j2vars
    assert 'nothing' not in j2vars


def test_AnsibleJ2Vars___contains___precedence():
    # Locals shadow templar variables and globals
    templar = MagicMock()
    templar.available_variables = {'shared_var': 'from_templar'}

    globals_dict = {'shared_var': 'from_globals'}
    locals_dict = {'l_shared_var': 'from_locals'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    assert 'shared_var' in j2vars

# Generated at 2026-11-03 01:26:22.014692
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from unittest.mock import MagicMock

    # Set up a mock templar with available variables
    templar = MagicMock()
    templar.available_variables = {'available_var': 'value', 'another_var': 42}

    globals_dict = {'global_var': 'global_value', 'range': range}

    # locals with 'l_' prefix keys and regular keys, plus excluded keys
    locals_dict = {
        'l_local_var': 'local_value',
        'plain_local': 'plain_value',
        'l__context': 'should_be_kept_as_context',
        'context': 'should_be_skipped',
        'environment': 'should_be_skipped',
        'template': 'should_be_skipped',
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Keys found in locals (prefix stripped from l_ keys)
    assert 'local_var' in j2vars
    assert 'plain_local' in j2vars
    # Excluded keys were not stored in locals
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars

    # Keys found in templar.available_variables
    assert 'available_var' in j2vars
    assert 'another_var' in j2vars

    # Keys found in globals
    assert 'global_var' in j2vars
    assert 'range' in j2vars

    # Keys not found anywhere
    assert 'nonexistent_var' not in j2vars
    assert '' not in j2vars

    # Constructed without locals - only templar and globals available
    j2vars_no_locals = AnsibleJ2Vars(templar, globals_dict)
    assert 'available_var' in j2vars_no_locals
    assert 'global_var' in j2vars_no_locals
    assert 'local_var' not in j2vars_no_locals