

# Generated at 2026-11-01 22:32:06.850712
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    from unittest.mock import MagicMock

    templar = MagicMock()
    templar.available_variables = {'foo': 'bar'}

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: []}

    # 'l_' prefixed keys are stripped, reserved names excluded, missing values dropped
    locals_dict = {
        'l_local_var': 'local_value',
        'plain_var': 'plain_value',
        'l_missing_var': missing,
        'context': 'should_be_skipped',
    }

    ajv = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)
    assert ajv._locals == {'local_var': 'local_value', 'plain_var': 'plain_value'}

    # Passing None returns the same object
    assert ajv.add_locals(None) is ajv

    # Passing a dict returns a NEW instance with merged locals
    new_ajv = ajv.add_locals({'extra_var': 'extra_value'})
    assert isinstance(new_ajv, AnsibleJ2Vars)
    assert new_ajv is not ajv
    assert new_ajv._locals == {
        'local_var': 'local_value',
        'plain_var': 'plain_value',
        'extra_var': 'extra_value',
    }

    # Original object remains unchanged
    assert ajv._locals == {'local_var': 'local_value', 'plain_var': 'plain_value'}
    assert 'extra_var' not in ajv._locals

    # Templar and globals are carried over to the new instance
    assert new_ajv._templar is templar
    assert new_ajv._globals is globals_dict

    # Chained add_locals accumulates locals across copies
    third_ajv = new_ajv.add_locals({'another': 123})
    assert third_ajv._locals == {
        'local_var': 'local_value',
        'plain_var': 'plain_value',
        'extra_var': 'extra_value',
        'another': 123,
    }

# Generated at 2026-11-01 22:32:20.472679
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from units.mock.loader import DictDataLoader

    fake_loader = DictDataLoader({})
    variable_manager = VariableManager()
    variable_manager.set_loader(fake_loader)

    mock_templar = MagicMock()
    mock_templar.available_variables = {'foo': 'bar', 'num': 1}

    globals_dict = {'range': range, 'lookup': MagicMock()}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(mock_templar, globals_dict, locals=locals_dict)

    # variable in locals
    assert 'local_var' in j2vars
    # variable in templar available_variables
    assert 'foo' in j2vars
    assert 'num' in j2vars
    # variable in globals
    assert 'range' in j2vars
    assert 'lookup' in j2vars
    # variable not defined anywhere
    assert 'missing_var' not in j2vars
    # locals should take precedence over available_variables
    j2vars2 = AnsibleJ2Vars(mock_templar, globals_dict, locals={'foo': 'local_bar'})
    assert 'foo' in j2vars2

# Generated at 2026-11-01 22:32:44.534600
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    class MockTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables

    # Test with no overlapping keys across scopes
    templar = MockTemplar({'var1': 'value1', 'var2': 'value2'})
    j2vars = AnsibleJ2Vars(templar, {'global1': 'gvalue1'}, locals={'local1': 'lvalue1'})
    assert len(j2vars) == 4

    # Test with overlapping keys: union should count each key only once
    templar = MockTemplar({'var1': 'value1'})
    j2vars = AnsibleJ2Vars(templar, {'var1': 'gvalue1', 'var2': 'gvalue2'}, locals={'var1': 'lvalue1'})
    assert len(j2vars) == 2

    # Test with empty variables
    templar = MockTemplar({})
    j2vars = AnsibleJ2Vars(templar, {}, locals=None)
    assert len(j2vars) == 0

    # Test constructor locals processing: 'l_' prefix stripped, 'context' excluded
    templar = MockTemplar({'a': 1})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'l_a': 10, 'context': 'x', 'b': 2})
    # locals become {'a': 10, 'b': 2}; 'a' overlaps with templar vars, 'context' excluded
    assert len(j2vars) == 2

    # Test locals with 'missing' sentinel values are skipped
    templar = MockTemplar({'a': 1})
    j2vars = AnsibleJ2Vars(templar, {'g': 3}, locals={'l_a': missing, 'b': 2})
    # 'l_a' skipped (missing value), locals = {'b': 2}; union = {'a', 'g', 'b'}
    assert len(j2vars) == 3

# Generated at 2026-11-01 22:34:03.701247
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-11-01 22:34:28.162299
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar:
        def __init__(self, variables):
            self.available_variables = variables

        def template(self, value):
            return 'templated:%s' % value

    available = {'foo': 'bar', 'num': 3, 'vars': {'a': 1}}
    templar = FakeTemplar(available)
    globals_ = {'global_var': 42, 'range': range}
    locals_ = {'l_local_one': 1, 'plain': 'p', 'context': 'ctx', 'environment': 'env', 'template': 'tpl'}

    j2vars = AnsibleJ2Vars(templar, globals_, locals=locals_)

    # locals are returned first, with the 'l_' prefix stripped
    assert j2vars['local_one'] == 1
    assert j2vars['plain'] == 'p'
    # context/environment/template keys are dropped from locals
    assert 'context' not in j2vars._locals
    assert 'environment' not in j2vars._locals
    assert 'template' not in j2vars._locals

    # globals are returned as-is, without templating
    assert j2vars['global_var'] == 42
    assert j2vars['range'] is range

    # regular variables from the templar get templated
    assert j2vars['foo'] == 'templated:bar'
    assert j2vars['num'] == 'templated:3'

    # the special 'vars' dict is returned as-is, not templated
    assert j2vars['vars'] is available['vars']
    assert j2vars['vars'] == {'a': 1}

    # unknown variables raise KeyError
    with pytest.raises(KeyError):
        j2vars['does_not_exist']

# Generated at 2026-11-01 22:35:01.376235
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from unittest.mock import MagicMock

    # Mock templar with available variables
    templar = MagicMock()
    templar.available_variables = {'available_var': 'value', 'host_var': 'hvalue'}

    globals_dict = {'global_var': 'gvalue', 'range': range}

    locals_dict = {
        'l_local_var': 'lvalue',       # jinja2-style local with l_ prefix
        'plain_local': 'pvalue',       # plain local without prefix
        'context': 'ctx',              # excluded special key
        'environment': 'env',          # excluded special key
        'template': 'tmpl',            # excluded special key
        'missing_local': missing,      # value is jinja2 missing sentinel, should be skipped
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Variables stored in locals (l_ prefix stripped) should be found
    assert 'local_var' in j2vars
    assert 'plain_local' in j2vars

    # Special jinja2 keys should not have been stored in locals
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars

    # Locals whose value is the jinja2 `missing` sentinel are skipped
    assert 'missing_local' not in j2vars

    # Variables from templar.available_variables should be found
    assert 'available_var' in j2vars
    assert 'host_var' in j2vars

    # Variables from globals should be found
    assert 'global_var' in j2vars
    assert 'range' in j2vars

    # Undefined variables should not be found
    assert 'undefined_var' not in j2vars
    assert '' not in j2vars

    # Verify precedence: local shadows available variable and global
    templar2 = MagicMock()
    templar2.available_variables = {'shared': 'from_available'}
    globals2 = {'shared': 'from_globals'}
    j2vars2 = AnsibleJ2Vars(templar2, globals2, locals={'l_shared': 'from_locals'})
    assert 'shared' in j2vars2
    assert j2vars2['shared'] == 'from_locals'

# Generated at 2026-11-01 22:36:00.695401
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest
    from unittest.mock import MagicMock, Mock
    from ansible.template import AnsibleJ2Vars
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class UnsafeValue(object):
        __UNSAFE__ = True

    templar = MagicMock()
    templar.available_variables = {
        'simple': 'value',
        'vars': {'inner': 'var'},
        'unsafe_var': UnsafeValue(),
        'hostvars': Mock(spec=HostVars),
    }
    templar.template.side_effect = lambda v: 'templated:%s' % v

    globals_dict = {'range': range, 'global_var': 'global_value'}
    locals_dict = {
        'l_local_var': 'local_value',
        'l_context': 'ctx',
        'l_environment': 'env',
        'l_template': 'tmpl',
        'plain': 'kept',
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # locals are checked first and have the 'l_' prefix stripped
    assert j2vars['local_var'] == 'local_value'

    # non 'l_' prefixed local keys are preserved as-is
    assert j2vars['plain'] == 'kept'

    # special local keys (context, environment, template) are filtered out
    with pytest.raises(KeyError):
        j2vars['context']

    # templar variables are templated before being returned
    assert j2vars['simple'] == 'templated:value'

    # the special 'vars' variable is returned as-is without templating
    assert j2vars['vars'] == {'inner': 'var'}

    # unsafe values are returned as-is without templating
    unsafe_value = j2vars['unsafe_var']
    assert hasattr(unsafe_value, '__UNSAFE__')

    # HostVars instances are returned as-is without templating
    assert isinstance(j2vars['hostvars'], HostVars)

    # globals are returned directly, without templating
    assert j2vars['global_var'] == 'global_value'
    assert j2vars['range'] is range

    # a variable found nowhere raises KeyError
    with pytest.raises(KeyError):
        j2vars['does_not_exist']

    # an AnsibleUndefinedVariable during templating is re-raised with context
    templar.template.side_effect = AnsibleUndefinedVariable('inner boom')
    with pytest.raises(AnsibleUndefinedVariable):
        j2vars['simple']

    # any other error during templating is wrapped in an AnsibleError
    templar.template.side_effect = Exception('kaboom')
    with pytest.raises(AnsibleError):
        j2vars['simple']

# Generated at 2026-11-01 22:36:44.964071
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    # Mock templar with available variables
    mock_templar = MagicMock()
    mock_templar.available_variables = {'some_var': 'some_value'}

    globals_dict = {'range': range, 'lookup': MagicMock()}

    # Build an instance carrying some pre-existing locals
    ajv = AnsibleJ2Vars(mock_templar, globals_dict, locals={'existing': 'local_value'})

    # module_0.add_locals(None) must return the very same object
    assert ajv.add_locals(None) is ajv

    # Adding locals returns a NEW AnsibleJ2Vars instance
    new_ajv = ajv.add_locals({'added': 'new_value'})
    assert isinstance(new_ajv, AnsibleJ2Vars)
    assert new_ajv is not ajv

    # New instance combines pre-existing locals with the newly supplied ones
    assert new_ajv._locals['existing'] == 'local_value'
    assert new_ajv._locals['added'] == 'new_value'

    # Newly supplied locals override conflicting older ones
    overridden = ajv.add_locals({'existing': 'updated'})
    assert overridden._locals['existing'] == 'updated'

    # The original instance remains untouched
    assert ajv._locals == {'existing': 'local_value'}

    # Templar and globals are carried over to the new instance
    assert new_ajv._templar is mock_templar
    assert new_ajv._globals is globals_dict

    # Constructor filtering applies to locals flowing through add_locals:
    # 'l_'-prefixed keys are stripped, missing values dropped, and
    # context/environment/template keys excluded
    filtered = ajv.add_locals({
        'l_stripped': 'yes',
        'dropped': missing,
        'context': 'nope',
        'environment': 'nope',
        'template': 'nope',
        'kept': 'yes',
    })
    assert filtered._locals.get('stripped') == 'yes'
    assert 'dropped' not in filtered._locals
    assert 'context' not in filtered._locals
    assert 'environment' not in filtered._locals
    assert 'template' not in filtered._locals
    assert filtered._locals.get('kept') == 'yes'
    assert filtered._locals.get('existing') == 'local_value'


if __name__ == '__main__':
    test_AnsibleJ2Vars_add_locals()
    print("test_AnsibleJ2Vars_add_locals passed")

# Generated at 2026-11-01 22:37:16.002536
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    from unittest import mock

    # Mock templar with available variables; make template() an identity op
    mock_templar = mock.MagicMock()
    mock_templar.available_variables = {'foo': 'bar', 'num': 123}
    mock_templar.template.side_effect = lambda v: v

    globals_dict = {'range': range, 'lookup': mock.Mock()}
    locals_dict = {'host': 'localhost'}

    ajv = AnsibleJ2Vars(mock_templar, globals_dict, locals=locals_dict)

    # Passing None returns the exact same object
    assert ajv.add_locals(None) is ajv

    # Passing new locals returns a NEW AnsibleJ2Vars instance
    new_ajv = ajv.add_locals({'port': 22})
    assert isinstance(new_ajv, AnsibleJ2Vars)
    assert new_ajv is not ajv

    # Old locals preserved, new locals added, original object untouched
    assert new_ajv['host'] == 'localhost'
    assert new_ajv['port'] == 22
    assert 'port' not in ajv._locals
    assert 'port' not in ajv

    # Templar variables and globals remain reachable through the new object
    assert new_ajv['foo'] == 'bar'
    assert new_ajv['range'] is range
    assert 'num' in new_ajv

    # Subsequent calls merge over previously accumulated locals
    updated = new_ajv.add_locals({'host': 'otherhost'})
    assert isinstance(updated, AnsibleJ2Vars)
    assert updated['host'] == 'otherhost'
    assert updated['port'] == 22
    assert updated['foo'] == 'bar'

    # An empty dict still produces a fresh copy carrying existing locals
    copied = ajv.add_locals({})
    assert copied is not ajv
    assert copied['host'] == 'localhost'
    assert dict(copied._locals) == {'host': 'localhost'}

# Generated at 2026-11-01 22:37:48.167234
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    '''Verify the AnsibleJ2Vars constructor stores the templar/globals and
    preprocesses jinja2 locals correctly.'''

    templar = MagicMock()
    templar.available_variables = {'foo': 'bar', 'num': 42}
    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: None}

    locals_dict = {
        'l_localvar': 'local_value',   # 'l_' prefix should be stripped
        'plainvar': 'plain_value',     # plain keys kept as-is
        'l_skipme': missing,           # values equal to the missing sentinel are dropped
        'skipme_too': missing,
        'context': 'dropped',          # reserved jinja2 names are dropped
        'environment': 'dropped',
        'template': 'dropped',
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # attributes are stored correctly
    assert j2vars._templar is templar
    assert j2vars._globals == globals_dict

    # l_ prefixes stripped, missing values skipped,
    # context/environment/template keys excluded
    assert j2vars._locals == {'localvar': 'local_value', 'plainvar': 'plain_value'}

    # locals=None results in an empty locals mapping
    no_locals = AnsibleJ2Vars(templar, globals_dict, locals=None)
    assert no_locals._locals == {}
    assert no_locals._templar is templar
    assert no_locals._globals == globals_dict

# Generated at 2026-11-01 22:38:08.737583
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import Mock, MagicMock
    from ansible.template import Templar
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable

    # --- variable found in locals ---
    templar = Mock()
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {}, locals={'l_localvar': 'local_value'})
    assert j2vars['localvar'] == 'local_value'

    # --- variable found in templar.available_variables, gets templated ---
    templar.available_variables = {'myvar': 'value'}
    templar.template = Mock(return_value='templated_value')
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['myvar'] == 'templated_value'
    templar.template.assert_called_once_with('value')

    # --- variable found in globals, returned as-is without templating ---
    templar.available_variables = {}
    templar.template = Mock()
    j2vars = AnsibleJ2Vars(templar, {'globalvar': 'global_value'})
    assert j2vars['globalvar'] == 'global_value'
    assert templar.template.called is False

    # --- undefined variable raises KeyError ---
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['nonexistent']
        assert False, "Expected KeyError"
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)

    # --- 'vars' special variable returned as-is (not templated) ---
    templar.available_variables = {'vars': {'a': 1, 'b': 2}}
    templar.template = Mock()
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result == {'a': 1, 'b': 2}
    assert templar.template.called is False

    # --- HostVars instance returned as-is ---
    from ansible.vars.hostvars import HostVars
    hostvars = Mock(spec=HostVars)
    templar.available_variables = {'hostvars': hostvars}
    templar.template = Mock()
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars
    assert templar.template.called is False

    # --- unsafe variable (has __UNSAFE__ attr) returned as-is ---
    class UnsafeVar(str):
        __UNSAFE__ = True
    unsafe = UnsafeVar('unsafe_value')
    templar.available_variables = {'unsafevar': unsafe}
    templar.template = Mock()
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafevar'] is unsafe
    assert templar.template.called is False

    # --- AnsibleUndefinedVariable during templating is wrapped ---
    templar.available_variables = {'badvar': 'bad_value'}
    templar.template = Mock(side_effect=AnsibleUndefinedVariable("undefined"))
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['badvar']
        assert False, "Expected AnsibleUndefinedVariable"
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in str(e)

    # --- generic exception during templating wrapped in AnsibleError ---
    templar.available_variables = {'errvar': 'err_value'}
    templar.template = Mock(side_effect=Exception("boom"))
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['errvar']
        assert False, "Expected AnsibleError"
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)

    # --- locals take precedence over available_variables ---
    templar.available_variables = {'x': 'from_available'}
    templar.template = Mock(return_value='templated')
    j2vars = AnsibleJ2Vars(templar, {}, locals={'l_x': 'from_locals'})
    assert j2vars['x'] == 'from_locals'
    assert templar.template.called is False

    # --- available_variables take precedence over globals ---
    templar.available_variables = {'y': 'from_available'}
    templar.template = Mock(return_value='templated_y')
    j2vars = AnsibleJ2Vars(templar, {'y': 'from_globals'})
    assert j2vars['y'] == 'templated_y'

    # --- locals filtering: 'context', 'environment', 'template' keys skipped ---
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {}, locals={'context': 'ctx', 'environment': 'env', 'template': 'tmpl', 'ok': 'kept'})
    assert 'context' not in j2vars._locals
    assert 'environment' not in j2vars._locals
    assert 'template' not in j2vars._locals
    assert j2vars['ok'] == 'kept'

    # --- locals filtering: keys without 'l_' prefix kept, missing values skipped ---
    from jinja2.utils import missing
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {}, locals={'plain': 'v1', 'noprefix': missing})
    assert j2vars['plain'] == 'v1'
    assert 'noprefix' not in j2vars._locals

# Generated at 2026-11-01 22:38:25.058865
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from unittest import TestCase
    from unittest.mock import MagicMock

    class TestAnsibleJ2VarsContains(TestCase):

        def _make_templar(self, available_variables=None):
            templar = MagicMock()
            templar.available_variables = available_variables if available_variables is not None else {}
            return templar

        def test_in_locals(self):
            templar = self._make_templar({'foo': 'bar'})
            ajv = AnsibleJ2Vars(templar, globals={})
            ajv._locals['localvar'] = 'value'
            assert 'localvar' in ajv
            assert 'foo' in ajv

        def test_in_available_variables(self):
            templar = self._make_templar({'host_var': 'value'})
            ajv = AnsibleJ2Vars(templar, globals={})
            assert 'host_var' in ajv

        def test_in_globals(self):
            templar = self._make_templar({})
            ajv = AnsibleJ2Vars(templar, globals={'range': range, 'lookup': lambda *a, **kw: None})
            assert 'range' in ajv
            assert 'lookup' in ajv

        def test_not_present(self):
            templar = self._make_templar({})
            ajv = AnsibleJ2Vars(templar, globals={})
            assert 'nonexistent' not in ajv

        def test_locals_take_precedence(self):
            templar = self._make_templar({'var': 'from_available'})
            ajv = AnsibleJ2Vars(templar, globals={})
            ajv._locals['var'] = 'from_locals'
            assert 'var' in ajv
            assert ajv['var'] == 'from_locals'

        def test_locals_from_constructor(self):
            templar = self._make_templar({})
            ajv = AnsibleJ2Vars(templar, globals={}, locals={'l_myvar': 'myvalue', 'other': 42})
            assert 'myvar' in ajv
            assert 'other' in ajv
            assert ajv['myvar'] == 'myvalue'
            assert ajv['other'] == 42

        def test_missing_sentinel_filtered_from_locals(self):
            templar = self._make_templar({})
            ajv = AnsibleJ2Vars(templar, globals={}, locals={'l_undefined': missing})
            assert 'undefined' not in ajv

        def test_special_keys_filtered_from_locals(self):
            templar = self._make_templar({})
            ajv = AnsibleJ2Vars(templar, globals={}, locals={'context': 1, 'environment': 2, 'template': 3})
            assert 'context' not in ajv
            assert 'environment' not in ajv
            assert 'template' not in ajv

    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(TestAnsibleJ2VarsContains))
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2026-11-01 22:38:54.201714
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from unittest.mock import MagicMock

    # Set up a mock templar with available variables
    templar = MagicMock()
    templar.available_variables = {'available_var': 'value', 'hostvars': MagicMock()}

    globals_dict = {'global_var': 'global_value', 'range': range}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Variable in locals should be found
    assert 'local_var' in j2vars

    # Variable in templar.available_variables should be found
    assert 'available_var' in j2vars

    # Variable in globals should be found
    assert 'global_var' in j2vars

    # Nonexistent variable should not be found
    assert 'nonexistent_var' not in j2vars

    # Test without locals
    j2vars_no_locals = AnsibleJ2Vars(templar, globals_dict)
    assert 'local_var' not in j2vars_no_locals
    assert 'available_var' in j2vars_no_locals
    assert 'global_var' in j2vars_no_locals

# Generated at 2026-11-01 22:40:13.048878
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-11-01 22:41:33.982776
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template import AnsibleJ2Vars