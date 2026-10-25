

# Generated at 2026-10-24 12:03:28.703279
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:03:31.116222
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:03:33.532618
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:03:36.063012
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:03:38.484177
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:03:41.004980
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:03:43.526989
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:03:45.948645
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:03:48.368184
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:01.107716
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:08.902305
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:10.217563
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:44.940919
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:47.539053
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:04:49.956136
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:05:23.969368
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

# Generated at 2026-10-24 12:05:34.662652
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

# Generated at 2026-10-24 12:05:35.984556
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

# Generated at 2026-10-24 12:05:37.303251
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

# Generated at 2026-10-24 12:05:39.818650
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:05:42.241940
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:05:44.825975
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:05:47.248858
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:05:49.666765
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:05:52.089249
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:05:54.507774
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:14.809638
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:17.469444
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:18.881773
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

# Generated at 2026-10-24 12:06:20.205544
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

# Generated at 2026-10-24 12:06:22.732539
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:25.241184
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:27.759186
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:30.175866
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:32.594161
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:35.012802
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:37.431235
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:39.991422
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:42.412196
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:44.837358
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:47.257217
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:49.683247
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:52.101947
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:54.528079
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:56.945107
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:06:59.362837
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:01.783717
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:04.201592
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:06.617200
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:09.043557
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:11.863146
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:30.497186
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.template.vars import AnsibleJ2Vars
    from ansible.vars.hostvars import HostVars

    class FakeTemplar:
        def __init__(self, available=None, template_func=None):
            self.available_variables = dict(available or {})
            self._template_func = template_func
            self.template_calls = []

        def template(self, variable):
            self.template_calls.append(variable)
            if self._template_func is not None:
                return self._template_func(variable)
            return "templated:%s" % (variable,)

    # locals take precedence and are returned without templating
    templar = FakeTemplar({"x": "available", "y": "available-y"})
    j2vars = AnsibleJ2Vars(templar, {"x": "global", "g": "global-g"}, locals={"x": "local-x", "l_stripped": "stripped-val"})
    assert j2vars["x"] == "local-x"

# Generated at 2026-10-24 12:07:33.101784
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:35.700066
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:38.290667
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:40.816313
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:43.236188
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:45.651498
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:48.071632
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:50.500408
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:52.922262
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:55.582785
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:07:58.007729
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:00.422484
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:02.843926
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:05.264314
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:07.684355
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:10.106531
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:12.527402
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:14.953343
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:17.369378
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:19.785285
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:22.204338
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:24.626016
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:27.041824
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:29.458130
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:31.873870
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:34.293212
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:36.724691
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:39.146234
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:41.557925
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:43.979187
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:46.395349
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:48.812633
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:51.234369
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:53.655822
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:56.068999
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:08:58.486112
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:00.902654
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:31.511257
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-24 12:09:33.936375
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:36.354962
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:38.777152
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:41.199236
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:43.624657
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:46.056175
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:48.620041
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:51.045391
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:53.475639
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:55.905273
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:09:58.325635
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:00.750125
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:03.379081
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

# Generated at 2026-10-24 12:10:04.692338
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

# Generated at 2026-10-24 12:10:07.378780
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

# Generated at 2026-10-24 12:10:10.036300
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

# Generated at 2026-10-24 12:10:12.887868
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

# Generated at 2026-10-24 12:10:15.594868
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

# Generated at 2026-10-24 12:10:17.693645
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

# Generated at 2026-10-24 12:10:19.007177
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

# Generated at 2026-10-24 12:10:21.743800
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

# Generated at 2026-10-24 12:10:24.383208
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

# Generated at 2026-10-24 12:10:27.115916
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

# Generated at 2026-10-24 12:10:29.697114
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:32.213881
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:34.631591
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:37.061695
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:39.477774
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:42.048924
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:44.470234
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:46.888005
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:49.307379
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:51.726314
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:54.146082
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:56.567480
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:10:58.987055
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:01.404251
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:03.824503
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:08.297328
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:10.717934
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:13.131637
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:15.561554
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:17.978638
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:20.400114
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:22.817845
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:25.232689
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:27.654935
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:30.074455
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:32.497135
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:35.132896
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:11:36.476157
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

# Generated at 2026-10-24 12:11:39.267368
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

# Generated at 2026-10-24 12:11:40.651481
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

# Generated at 2026-10-24 12:11:43.711129
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

# Generated at 2026-10-24 12:11:45.026284
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

# Generated at 2026-10-24 12:11:47.914492
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

# Generated at 2026-10-24 12:12:02.436545
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:04.855731
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:07.279855
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:09.829760
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:12.250725
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:14.669880
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:17.087544
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:19.507313
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:21.921508
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:24.338108
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:26.756544
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:29.173077
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:31.591092
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:34.008092
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:36.423115
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:38.840110
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:41.268434
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:43.709190
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:46.127989
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:48.545428
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:50.961512
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:53.377040
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:55.793208
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:12:58.212780
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:00.633450
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:03.047610
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:05.467999
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:07.883757
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:10.300931
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:12.720718
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 12:13:28.505539
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