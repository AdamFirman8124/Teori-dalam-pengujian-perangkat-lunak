

# Generated at 2026-10-24 12:04:20.433565
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    templar = MagicMock()
    templar.available_variables = {'foo': 'bar'}
    globals_dict = {'range': range, 'lookup': lambda *a, **kw: None}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'local1': 'value1'})

    # 1. module_0.add_locals(None) returns the same object, not a copy
    assert j2vars.add_locals(None) is j2vars

    # 2. add_locals returns a NEW object with merged locals; original untouched
    new_j2vars = j2vars.add_locals({'local2': 'value2'})
    assert new_j2vars is not j2vars
    assert new_j2vars._locals == {'local1': 'value1', 'local2': 'value2'}
    assert j2vars._locals == {'local1': 'value1'}

    # 3. merged locals are visible through the mapping interface
    assert 'local2' in new_j2vars
    assert new_j2vars['local2'] == 'value2'
    assert new_j2vars['local1'] == 'value1'

    # 4. locals shadow templar variables of the same name
    shadowed = j2vars.add_locals({'foo': 'override'})
    assert shadowed['foo'] == 'override'

    # 5. templar vars and globals still reachable on the copy
    assert 'foo' in new_j2vars
    assert 'range' in new_j2vars
    assert new_j2vars['range'] is range

    # 6. add_locals works on an instance created without initial locals
    base = AnsibleJ2Vars(templar, globals_dict)
    merged = base.add_locals({'x': 1})
    assert merged._locals == {'x': 1}


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:04:22.846921
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:25.268284
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:27.693216
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:30.105572
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:32.522736
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:34.943139
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:37.361013
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:39.779475
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:42.195867
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:44.613592
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:47.029618
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:49.446386
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:05:00.457622
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from jinja2.utils import missing, environment

    from ansible.template import Templar

    class FakeTemplar:
        def __init__(self):
            self.available_variables = {'available_var': 'value'}

    templar = FakeTemplar()
    globals_dict = {'global_var': 'gvalue', 'range': range}

    # Case 1: normal dict with 'l_' prefixed keys, plain keys, and reserved names
    locals_dict = {
        'l_stripped': 'stripped_value',      # 'l_' prefix should be stripped
        'plain_var': 'plain_value',          # kept as-is
        'l_context': 'ctx',                  # stripped prefix -> 'context' is NOT reserved after strip
        'context': 'should_be_dropped',      # reserved key, dropped
        'environment': 'should_be_dropped',  # reserved key, dropped
        'template': 'should_be_dropped',     # reserved key, dropped
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict
    assert j2vars._locals['stripped'] == 'stripped_value'
    assert j2vars._locals['plain_var'] == 'plain_value'
    assert j2vars._locals['context'] == 'ctx'  # came from 'l_context'
    assert 'environment' not in j2vars._locals
    assert 'template' not in j2vars._locals

    # Case 2: `missing` sentinel values are excluded
    locals_dict_missing = {
        'l_good': 'yes',
        'l_bad': missing,   # should be skipped
        'also_bad': missing,
    }
    j2vars_missing = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict_missing)
    assert j2vars_missing._locals == {'good': 'yes'}

    # Case 3: locals=None -> empty _locals, no error
    j2vars_none = AnsibleJ2Vars(templar, globals_dict, locals=None)
    assert j2vars_none._locals == {}

    # Case 4: locals is not a dict (e.g. a list) -> ignored, empty _locals
    j2vars_notdict = AnsibleJ2Vars(templar, globals_dict, locals=['l_not_a_dict'])
    assert j2vars_notdict._locals == {}

    # Case 5: locals=None is also the default
    j2vars_default = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars_default._locals == {}
    assert j2vars_default._globals is globals_dict

    print("test_AnsibleJ2Vars passed")

# Generated at 2026-10-24 12:05:01.891124
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from jinja2.utils import missing, environment

    from ansible.template import Templar

    class FakeTemplar:
        def __init__(self):
            self.available_variables = {'available_var': 'value'}

    templar = FakeTemplar()
    globals_dict = {'global_var': 'gvalue', 'range': range}

    # Case 1: normal dict with 'l_' prefixed keys, plain keys, and reserved names
    locals_dict = {
        'l_stripped': 'stripped_value',      # 'l_' prefix should be stripped
        'plain_var': 'plain_value',          # kept as-is
        'l_context': 'ctx',                  # stripped prefix -> 'context' is NOT reserved after strip
        'context': 'should_be_dropped',      # reserved key, dropped
        'environment': 'should_be_dropped',  # reserved key, dropped
        'template': 'should_be_dropped',     # reserved key, dropped
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict
    assert j2vars._locals['stripped'] == 'stripped_value'
    assert j2vars._locals['plain_var'] == 'plain_value'
    assert j2vars._locals['context'] == 'ctx'  # came from 'l_context'
    assert 'environment' not in j2vars._locals
    assert 'template' not in j2vars._locals

    # Case 2: `missing` sentinel values are excluded
    locals_dict_missing = {
        'l_good': 'yes',
        'l_bad': missing,   # should be skipped
        'also_bad': missing,
    }
    j2vars_missing = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict_missing)
    assert j2vars_missing._locals == {'good': 'yes'}

    # Case 3: locals=None -> empty _locals, no error
    j2vars_none = AnsibleJ2Vars(templar, globals_dict, locals=None)
    assert j2vars_none._locals == {}

    # Case 4: locals is not a dict (e.g. a list) -> ignored, empty _locals
    j2vars_notdict = AnsibleJ2Vars(templar, globals_dict, locals=['l_not_a_dict'])
    assert j2vars_notdict._locals == {}

    # Case 5: locals=None is also the default
    j2vars_default = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars_default._locals == {}
    assert j2vars_default._globals is globals_dict

    print("test_AnsibleJ2Vars passed")

# Generated at 2026-10-24 12:05:36.603694
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:06.709005
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:09.579485
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:12.641468
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    g = {'global_var': 'gv'}
    t = object()
    v = AnsibleJ2Vars(t, g)
    assert v._templar is t
    assert v._globals is g
    assert v._locals == {}
    v_none = AnsibleJ2Vars(t, g, locals=None)
    assert v_none._locals == {}
    v_nondict_list = AnsibleJ2Vars(t, g, locals=['a', 'b'])
    assert v_nondict_list._locals == {}
    v_nondict_str = AnsibleJ2Vars(t, g, locals='foo')
    assert v_nondict_str._locals == {}
    v_nondict_int = AnsibleJ2Vars(t, g, locals=42)
    assert v_nondict_int._locals == {}
    locals_dict = {
        'normal': 1,
        'l_stripped': 2,
        'l_': 3,
        'l_context': 4,
        'context': 10,
        'environment': 11,
        'template': 12,
        'skipped_missing': missing,
        'l_keep_missing': missing,
        '': 13,
        'x': 14,
    }
    v2 = AnsibleJ2Vars(t, g, locals=locals_dict)
    assert v2._templar is t
    assert v2._globals is g
    assert v2._locals == {
        'normal': 1,
        'stripped': 2,
        '': 3,
        'context': 4,
        'x': 14,
    }
    assert v2._locals['normal'] == 1
    assert v2._locals['stripped'] == 2
    assert v2._locals[''] == 3
    assert v2._locals['context'] == 4
    assert 'environment' not in v2._locals
    assert 'template' not in v2._locals
    assert 'skipped_missing' not in v2._locals

# Generated at 2026-10-24 12:06:16.337413
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:18.989239
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:21.527651
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:24.090679
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:26.511678
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:28.929002
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:31.348181
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:33.768381
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:36.185512
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:38.780003
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:41.196681
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:43.620444
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:46.042466
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:48.479451
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:50.890929
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:53.312465
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:55.729910
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:58.151918
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:00.566650
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:02.986451
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:05.404818
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:07.826500
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:10.249446
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:13.215408
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:14.529843
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:07:17.257287
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    g = {'global_var': 'gv'}
    t = object()
    v = AnsibleJ2Vars(t, g)
    assert v._templar is t
    assert v._globals is g
    assert v._locals == {}
    v_none = AnsibleJ2Vars(t, g, locals=None)
    assert v_none._locals == {}
    v_nondict_list = AnsibleJ2Vars(t, g, locals=['a', 'b'])
    assert v_nondict_list._locals == {}
    v_nondict_str = AnsibleJ2Vars(t, g, locals='foo')
    assert v_nondict_str._locals == {}
    v_nondict_int = AnsibleJ2Vars(t, g, locals=42)
    assert v_nondict_int._locals == {}
    locals_dict = {
        'normal': 1,
        'l_stripped': 2,
        'l_': 3,
        'l_context': 4,
        'context': 10,
        'environment': 11,
        'template': 12,
        'skipped_missing': missing,
        'l_keep_missing': missing,
        '': 13,
        'x': 14,
    }
    v2 = AnsibleJ2Vars(t, g, locals=locals_dict)
    assert v2._templar is t
    assert v2._globals is g
    assert v2._locals == {
        'normal': 1,
        'stripped': 2,
        '': 3,
        'context': 4,
        'x': 14,
    }
    assert v2._locals['normal'] == 1
    assert v2._locals['stripped'] == 2
    assert v2._locals[''] == 3
    assert v2._locals['context'] == 4
    assert 'environment' not in v2._locals
    assert 'template' not in v2._locals
    assert 'skipped_missing' not in v2._locals

# Generated at 2026-10-24 12:07:20.009598
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    g = {'global_var': 'gv'}
    t = object()
    v = AnsibleJ2Vars(t, g)
    assert v._templar is t
    assert v._globals is g
    assert v._locals == {}
    v_none = AnsibleJ2Vars(t, g, locals=None)
    assert v_none._locals == {}
    v_nondict_list = AnsibleJ2Vars(t, g, locals=['a', 'b'])
    assert v_nondict_list._locals == {}
    v_nondict_str = AnsibleJ2Vars(t, g, locals='foo')
    assert v_nondict_str._locals == {}
    v_nondict_int = AnsibleJ2Vars(t, g, locals=42)
    assert v_nondict_int._locals == {}
    locals_dict = {
        'normal': 1,
        'l_stripped': 2,
        'l_': 3,
        'l_context': 4,
        'context': 10,
        'environment': 11,
        'template': 12,
        'skipped_missing': missing,
        'l_keep_missing': missing,
        '': 13,
        'x': 14,
    }
    v2 = AnsibleJ2Vars(t, g, locals=locals_dict)
    assert v2._templar is t
    assert v2._globals is g
    assert v2._locals == {
        'normal': 1,
        'stripped': 2,
        '': 3,
        'context': 4,
        'x': 14,
    }
    assert v2._locals['normal'] == 1
    assert v2._locals['stripped'] == 2
    assert v2._locals[''] == 3
    assert v2._locals['context'] == 4
    assert 'environment' not in v2._locals
    assert 'template' not in v2._locals
    assert 'skipped_missing' not in v2._locals

# Generated at 2026-10-24 12:07:22.799194
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    g = {'global_var': 'gv'}
    t = object()
    v = AnsibleJ2Vars(t, g)
    assert v._templar is t
    assert v._globals is g
    assert v._locals == {}
    v_none = AnsibleJ2Vars(t, g, locals=None)
    assert v_none._locals == {}
    v_nondict_list = AnsibleJ2Vars(t, g, locals=['a', 'b'])
    assert v_nondict_list._locals == {}
    v_nondict_str = AnsibleJ2Vars(t, g, locals='foo')
    assert v_nondict_str._locals == {}
    v_nondict_int = AnsibleJ2Vars(t, g, locals=42)
    assert v_nondict_int._locals == {}
    locals_dict = {
        'normal': 1,
        'l_stripped': 2,
        'l_': 3,
        'l_context': 4,
        'context': 10,
        'environment': 11,
        'template': 12,
        'skipped_missing': missing,
        'l_keep_missing': missing,
        '': 13,
        'x': 14,
    }
    v2 = AnsibleJ2Vars(t, g, locals=locals_dict)
    assert v2._templar is t
    assert v2._globals is g
    assert v2._locals == {
        'normal': 1,
        'stripped': 2,
        '': 3,
        'context': 4,
        'x': 14,
    }
    assert v2._locals['normal'] == 1
    assert v2._locals['stripped'] == 2
    assert v2._locals[''] == 3
    assert v2._locals['context'] == 4
    assert 'environment' not in v2._locals
    assert 'template' not in v2._locals
    assert 'skipped_missing' not in v2._locals

# Generated at 2026-10-24 12:07:40.419952
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:07:42.838857
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:45.256796
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:47.673822
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:50.093885
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:52.514105
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:54.943494
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:57.541926
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:59.962016
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:02.386340
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:04.804619
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:07.227452
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:09.649208
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:12.067654
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:14.488338
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:16.924464
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:19.343276
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:21.762207
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:24.182764
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:26.600066
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:29.015818
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:31.433978
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:33.853771
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:36.271189
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:38.691907
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:41.105542
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:43.525345
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:45.949532
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:48.365583
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:50.783232
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:53.203967
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:55.621171
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:58.040141
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:00.457484
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:03.367965
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:09:06.145130
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:09:07.653006
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:09:10.401611
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:09:11.718453
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:09:14.362218
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:09:17.044656
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:09:19.738187
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:09:21.052976
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:09:23.770029
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:09:26.462975
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:09:27.828659
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:09:29.495724
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:09:32.131971
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:34.550159
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:36.970621
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:39.391227
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:41.807548
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:44.230611
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:46.650337
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:49.071608
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:51.489622
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:54.110374
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:56.541776
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:58.962954
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:01.383966
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:24.666657
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from jinja2.utils import missing

# Generated at 2026-10-24 12:10:25.982205
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:10:28.616750
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:31.033678
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:33.453939
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:35.868388
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:38.285483
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:40.703023
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:43.248733
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:45.670369
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:48.087819
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:51.435080
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:53.852918
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:56.272473
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:58.691725
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:01.109041
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:03.719450
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:06.154766
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:08.565854
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:10.987652
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:13.400003
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:15.819834
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:18.238080
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:20.656814
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:23.076520
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:25.498281
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:27.917350
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:30.339348
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:32.758993
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:35.304427
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:11:38.284205
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    g = {'global_var': 'gv'}
    t = object()
    v = AnsibleJ2Vars(t, g)
    assert v._templar is t
    assert v._globals is g
    assert v._locals == {}
    v_none = AnsibleJ2Vars(t, g, locals=None)
    assert v_none._locals == {}
    v_nondict_list = AnsibleJ2Vars(t, g, locals=['a', 'b'])
    assert v_nondict_list._locals == {}
    v_nondict_str = AnsibleJ2Vars(t, g, locals='foo')
    assert v_nondict_str._locals == {}
    v_nondict_int = AnsibleJ2Vars(t, g, locals=42)
    assert v_nondict_int._locals == {}
    locals_dict = {
        'normal': 1,
        'l_stripped': 2,
        'l_': 3,
        'l_context': 4,
        'context': 10,
        'environment': 11,
        'template': 12,
        'skipped_missing': missing,
        'l_keep_missing': missing,
        '': 13,
        'x': 14,
    }
    v2 = AnsibleJ2Vars(t, g, locals=locals_dict)
    assert v2._templar is t
    assert v2._globals is g
    assert v2._locals == {
        'normal': 1,
        'stripped': 2,
        '': 3,
        'context': 4,
        'x': 14,
    }
    assert v2._locals['normal'] == 1
    assert v2._locals['stripped'] == 2
    assert v2._locals[''] == 3
    assert v2._locals['context'] == 4
    assert 'environment' not in v2._locals
    assert 'template' not in v2._locals
    assert 'skipped_missing' not in v2._locals

# Generated at 2026-10-24 12:11:39.607065
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:11:42.248011
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:11:47.379972
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:11:48.694573
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:11:50.008829
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:11:52.430697
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:54.845509
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:57.264756
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:59.685539
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:02.101883
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:04.640163
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:07.061980
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:09.482220
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:12.045412
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:14.464861
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:16.885437
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:19.304464
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:21.719906
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:24.135790
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:26.563537
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:28.980998
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:31.400717
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:33.816109
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:36.230015
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:38.645969
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:41.063437
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:47.944037
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:50.361443
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:52.777004
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:55.192977
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:57.609224
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:00.028807
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:02.448187
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:04.864905
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:07.282002
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:09.697957
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:12.115240
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:14.535596
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:16.951062
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:19.407056
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:21.804810
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:24.227469
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:25.653570
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from jinja2.utils import missing

# Generated at 2026-10-24 12:13:26.967340
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:13:29.632436
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from unittest.mock import MagicMock
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_text
    from ansible.vars.hostvars import HostVars

    try:
        from jinja2.utils import missing
    except ImportError:
        from jinja2.runtime import missing

    class FakeTemplar(object):
        def __init__(self, available_variables=None, fail=False):
            self.available_variables = available_variables if available_variables is not None else {}
            self.fail = fail

        def template(self, variable):
            if self.fail:
                raise AnsibleUndefinedVariable("templating failed")
            if isinstance(variable, str):
                return variable + "_templated"
            return variable

    # 1. Variable found in locals is returned as-is (no templating)
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'local_var': 'local_value'})
    assert j2vars['local_var'] == 'local_value'

    # 2. Variable found in available_variables gets templated
    templar = FakeTemplar(available_variables={'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 'bar_templated'

    # 3. Variable found in globals is returned as-is
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {'global_var': 'global_value'})
    assert j2vars['global_var'] == 'global_value'

    # 4. Missing variable raises KeyError
    templar = FakeTemplar(available_variables={})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['no_such_var']
    except KeyError as e:
        assert 'no_such_var' in to_text(e)
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 5. The special 'vars' dict is returned as-is without templating
    special_vars = {'a': 1}
    templar = FakeTemplar(available_variables={'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, {})
    result = j2vars['vars']
    assert result is special_vars

    # 6. HostVars instance is returned as-is without templating
    hostvars = MagicMock(spec=HostVars)
    templar = FakeTemplar(available_variables={'hostvars': hostvars})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['hostvars'] is hostvars

    # 7. Variable marked __UNSAFE__ is returned as-is without templating
    unsafe_var = 'unsafe_value'
    unsafe_var.__UNSAFE__ = True
    templar = FakeTemplar(available_variables={'unsafe': unsafe_var})
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['unsafe'] is unsafe_var

    # 8. AnsibleUndefinedVariable during templating is re-raised with context
    templar = FakeTemplar(available_variables={'bad': 'bad_value'}, fail=True)
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['bad']
    except AnsibleUndefinedVariable as e:
        assert 'bad_value' in to_text(e)
        assert 'templating failed' in to_text(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 9. Generic exception during templating is wrapped in AnsibleError
    class ExplodingTemplar(FakeTemplar):
        def template(self, variable):
            raise Exception("boom")

    templar = ExplodingTemplar(available_variables={'exploding': 'value'})
    j2vars = AnsibleJ2Vars(templar, {})
    try:
        j2vars['exploding']
    except AnsibleError as e:
        assert 'boom' in to_text(e)
    else:
        raise AssertionError("expected AnsibleError")

    # 10. Locals shadow available_variables
    templar = FakeTemplar(available_variables={'foo': 'from_available'})
    j2vars = AnsibleJ2Vars(templar, {}, locals={'foo': 'from_locals'})
    assert j2vars['foo'] == 'from_locals'

# Generated at 2026-10-24 12:13:30.959801
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Build jinja2-style locals: keys prefixed with 'l_', plus reserved names
    jinja_locals = {
        'l_my_local': 1,
        'l_skip_undefined': missing,  # sentinel for undefined jinja2 locals
        'context': 'should be ignored',
        'environment': 'should be ignored',
        'template': 'should be ignored',
        'raw_dict': {'a': 1},  # no 'l_' prefix -> kept as-is
    }

    j2vars = make_j2vars(
        available_variables={'host_var': 'value', 'other_var': 42},
        globals_={'lookup': MagicMock(), 'range': range, 'global_var': True},
        locals_=jinja_locals,
    )

    # In locals (via 'l_' prefix stripping)
    assert j2vars.__contains__('my_local') is True

    # In templar.available_variables
    assert j2vars.__contains__('host_var') is True

    # In globals
    assert j2vars.__contains__('lookup') is True
    assert j2vars.__contains__('global_var') is True

    # Not defined anywhere
    assert j2vars.__contains__('nonexistent') is False

    # jinja2 sentinel `missing` value must be dropped from locals
    assert j2vars.__contains__('skip_undefined') is False

    # Reserved names without 'l_' prefix must be excluded from locals
    assert j2vars.__contains__('context') is False
    assert j2vars.__contains__('environment') is False
    assert j2vars.__contains__('template') is False

    # Non-prefixed, non-reserved locals are kept verbatim
    assert j2vars.__contains__('raw_dict') is True


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 12:13:33.704976
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    g = {'global_var': 'gv'}
    t = object()
    v = AnsibleJ2Vars(t, g)
    assert v._templar is t
    assert v._globals is g
    assert v._locals == {}
    v_none = AnsibleJ2Vars(t, g, locals=None)
    assert v_none._locals == {}
    v_nondict_list = AnsibleJ2Vars(t, g, locals=['a', 'b'])
    assert v_nondict_list._locals == {}
    v_nondict_str = AnsibleJ2Vars(t, g, locals='foo')
    assert v_nondict_str._locals == {}
    v_nondict_int = AnsibleJ2Vars(t, g, locals=42)
    assert v_nondict_int._locals == {}
    locals_dict = {
        'normal': 1,
        'l_stripped': 2,
        'l_': 3,
        'l_context': 4,
        'context': 10,
        'environment': 11,
        'template': 12,
        'skipped_missing': missing,
        'l_keep_missing': missing,
        '': 13,
        'x': 14,
    }
    v2 = AnsibleJ2Vars(t, g, locals=locals_dict)
    assert v2._templar is t
    assert v2._globals is g
    assert v2._locals == {
        'normal': 1,
        'stripped': 2,
        '': 3,
        'context': 4,
        'x': 14,
    }
    assert v2._locals['normal'] == 1
    assert v2._locals['stripped'] == 2
    assert v2._locals[''] == 3
    assert v2._locals['context'] == 4
    assert 'environment' not in v2._locals
    assert 'template' not in v2._locals
    assert 'skipped_missing' not in v2._locals

# Generated at 2026-10-24 12:13:53.442147
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:55.865218
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:58.284135
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:14:00.706138
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:14:03.129483
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:14:05.556668
# Unit test for method __contains__ of class AnsibleJ2Vars