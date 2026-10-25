

# Generated at 2026-10-25 02:15:10.691994
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:15:17.095902
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:15:23.650513
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:15:37.306467
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = _DummyTemplar({'foo': 'bar', 'ansible_host': 'localhost'})
    globals_ = {'range': range, 'lookup': object()}
    locals_ = {'l_item': 'value', 'context': 'ignored'}

    variables = AnsibleJ2Vars(templar, globals_, locals=locals_)

    keys = set(iter(variables))

    # templar vars
    assert 'foo' in keys
    assert 'ansible_host' in keys
    # jinja2 globals
    assert 'range' in keys
    assert 'lookup' in keys
    # locals: 'l_' prefix stripped
    assert 'item' in keys
    assert 'l_item' not in keys
    # 'context' is filtered out by __init__
    assert 'context' not in keys

    assert keys == {'foo', 'ansible_host', 'range', 'lookup', 'item'}
    # __len__ must agree with __iter__
    assert len(variables) == len(keys)

# Generated at 2026-10-25 02:15:39.914744
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:15:42.330920
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:15:44.746606
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:15:47.161619
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:15:49.576973
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:15:51.994690
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:16:00.718990
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MockTemplar(object):
        available_variables = {
            'available_var': 'available value',
        }

    variables = AnsibleJ2Vars(
        templar=MockTemplar(),
        globals={'global_var': 'global value'},
        locals={'local_var': 'local value'},
    )

    assert 'local_var' in variables
    assert 'available_var' in variables
    assert 'global_var' in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:16:11.723475
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = object()
    global_vars = {'global_var': 'global_value'}
    local_vars = {
        'local_var': 'local_value',
        'l_prefixed_var': 'prefixed_value',
        'undefined_var': missing,
        'context': object(),
        'environment': object(),
        'template': object(),
    }

    j2vars = AnsibleJ2Vars(templar, global_vars, local_vars)

    assert j2vars._templar is templar
    assert j2vars._globals is global_vars
    assert j2vars._locals == {
        'local_var': 'local_value',
        'prefixed_var': 'prefixed_value',
    }

    # The constructor must tolerate absent or non-dict locals.
    assert AnsibleJ2Vars(templar, global_vars)._locals == {}
    assert AnsibleJ2Vars(templar, global_vars, ['not', 'a', 'dict'])._locals == {}

# Generated at 2026-10-25 02:16:31.466422
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest

    class DummyTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.templated = []
            self.template_exception = None

        def template(self, value):
            self.templated.append(value)
            if self.template_exception is not None:
                raise self.template_exception
            return ('templated', value)

    class UnsafeValue(object):
        __UNSAFE__ = True

    local_value = object()
    global_value = object()
    available_value = object()
    available_over_global = object()

    templar = DummyTemplar({
        'available': available_value,
        'available_over_global': available_over_global,
    })
    variables = AnsibleJ2Vars(
        templar,
        globals={
            'global': global_value,
            'available_over_global': object(),
        },
        locals={
            'local': local_value,
            'available': object(),
        },
    )

    # Locals have the highest precedence and are returned without templating.
    assert variables['local'] is local_value
    assert variables['available'] is variables._locals['available']
    assert templar.templated == []

    # Available variables take precedence over globals and are templated.
    assert variables['available_over_global'] == (
        'templated',
        available_over_global,
    )
    assert templar.templated == [available_over_global]

    # Globals are returned as-is.
    assert variables['global'] is global_value

    # Unknown variables raise KeyError.
    with pytest.raises(KeyError, match='undefined variable: unknown'):
        variables['unknown']

    # The special "vars" dictionary is returned without templating.
    vars_value = {'answer': 42}
    templar.available_variables = {'vars': vars_value}
    templar.templated = []
    assert variables['vars'] is vars_value
    assert templar.templated == []

    # Unsafe values are returned without templating.
    unsafe_value = UnsafeValue()
    templar.available_variables = {'unsafe': unsafe_value}
    assert variables['unsafe'] is unsafe_value
    assert templar.templated == []

    # Undefined-variable errors are wrapped with the original value.
    templar.available_variables = {'broken': '{{ missing_variable }}'}
    undefined_error = AnsibleUndefinedVariable('missing_variable is undefined')
    if not hasattr(undefined_error, 'message'):
        undefined_error.message = 'missing_variable is undefined'
    templar.template_exception = undefined_error

    with pytest.raises(AnsibleUndefinedVariable) as exc:
        variables['broken']
    assert '{{ missing_variable }}' in to_native(exc.value)
    assert 'missing_variable is undefined' in to_native(exc.value)

    # Other templating exceptions are converted to AnsibleError.
    templar.template_exception = ValueError('template failed')

    with pytest.raises(AnsibleError) as exc:
        variables['broken']
    assert "while templating '{{ missing_variable }}'" in to_native(exc.value)
    assert 'template failed' in to_native(exc.value)

# Generated at 2026-10-25 02:16:41.859298
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    class DummyTemplar(object):
        available_variables = {}

    templar = DummyTemplar()
    global_vars = {'global_var': 'global value'}
    local_vars = {
        'plain_var': 'plain value',
        'l_scoped_var': 'scoped value',
        'missing_var': missing,
        'context': 'ignored',
        'environment': 'ignored',
        'template': 'ignored',
    }

    j2vars = AnsibleJ2Vars(templar, global_vars, local_vars)

    assert j2vars._templar is templar
    assert j2vars._globals is global_vars
    assert j2vars._locals == {
        'plain_var': 'plain value',
        'scoped_var': 'scoped value',
    }

    # Missing or non-dictionary locals should produce an empty local scope.
    assert AnsibleJ2Vars(templar, global_vars)._locals == {}
    assert AnsibleJ2Vars(templar, global_vars, locals=['not', 'a', 'dict'])._locals == {}

# Generated at 2026-10-25 02:16:50.178685
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    class DummyTemplar(object):
        available_variables = {}

    templar = DummyTemplar()
    globals_ = {'global_var': 'global value'}
    locals_ = {
        'normal_var': 'normal value',
        'l_prefixed_var': 'local value',
        'missing_var': missing,
        'context': 'ignored',
        'environment': 'ignored',
        'template': 'ignored',
    }

    variables = AnsibleJ2Vars(templar, globals_, locals_)

    assert variables._templar is templar
    assert variables._globals is globals_
    assert variables._locals == {
        'normal_var': 'normal value',
        'prefixed_var': 'local value',
    }

    # Non-dictionary locals should be ignored.
    variables_without_dict_locals = AnsibleJ2Vars(
        templar, globals_, locals=['not', 'a', 'dict']
    )
    assert variables_without_dict_locals._locals == {}

# Generated at 2026-10-25 02:17:12.092369
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 02:17:22.229587
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class DummyTemplar(object):
        available_variables = {'available_var': 'value'}

    variables = AnsibleJ2Vars(
        templar=DummyTemplar(),
        globals={'global_var': 'value'},
        locals={'local_var': 'value', 'l_scoped_var': 'value'},
    )

    assert 'local_var' in variables
    assert 'scoped_var' in variables
    assert 'l_scoped_var' not in variables
    assert 'available_var' in variables
    assert 'global_var' in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:17:37.999715
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    templar = _FakeTemplar()
    globals_ = {'range': range}

    # Constructor strips 'l_' prefixes and drops jinja-internal keys/missing values
    v = AnsibleJ2Vars(
        templar,
        globals_,
        locals={
            'l_existing': 'old',
            'plain': 1,
            'context': 'ignored',
            'environment': 'ignored',
            'template': 'ignored',
            'missing_var': missing,
        },
    )
    assert v._locals == {'existing': 'old', 'plain': 1}

    # add_locals returns a new proxy, merging and re-filtering locals
    new = v.add_locals({'l_new': 'new', 'plain': 2, 'context': 'ignored'})

    assert new is not v
    assert new._templar is templar
    assert new._globals is globals_
    assert new._locals == {'existing': 'old', 'plain': 2, 'new': 'new'}

    # Original proxy is unchanged
    assert v._locals == {'existing': 'old', 'plain': 1}

    # None is a no-op returning self
    assert v.add_locals(None) is v

# Generated at 2026-10-25 02:17:47.319178
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class DummyTemplar(object):
        available_variables = {
            'available_variable': 'available value',
        }

    j2_vars = AnsibleJ2Vars(
        templar=DummyTemplar(),
        globals={
            'global_variable': 'global value',
        },
        locals={
            'local_variable': 'local value',
            'l_prefixed_variable': 'prefixed local value',
            'missing_variable': missing,
        },
    )

    assert 'local_variable' in j2_vars
    assert 'prefixed_variable' in j2_vars
    assert 'available_variable' in j2_vars
    assert 'global_variable' in j2_vars

    assert 'l_prefixed_variable' not in j2_vars
    assert 'missing_variable' not in j2_vars
    assert 'undefined_variable' not in j2_vars

# Generated at 2026-10-25 02:17:55.714281
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class DummyTemplar(object):
        available_variables = {
            'available_variable': 'available value',
        }

    variables = AnsibleJ2Vars(
        templar=DummyTemplar(),
        globals={'global_variable': 'global value'},
        locals={'local_variable': 'local value'},
    )

    assert 'local_variable' in variables
    assert 'available_variable' in variables
    assert 'global_variable' in variables
    assert 'undefined_variable' not in variables

# Generated at 2026-10-25 02:18:05.339736
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MockTemplar(object):
        available_variables = {
            'available_var': 'available value',
        }

    variables = AnsibleJ2Vars(
        templar=MockTemplar(),
        globals={'global_var': 'global value'},
        locals={
            'local_var': 'local value',
            'l_prefixed_var': 'prefixed local value',
            'context': 'ignored',
        },
    )

    assert 'local_var' in variables
    assert 'prefixed_var' in variables
    assert 'available_var' in variables
    assert 'global_var' in variables

    assert 'l_prefixed_var' not in variables
    assert 'context' not in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:18:12.836540
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class DummyTemplar(object):
        available_variables = {
            'templar_var': None,
            'falsey_templar_var': False,
        }

    variables = AnsibleJ2Vars(
        templar=DummyTemplar(),
        globals={'global_var': None},
        locals={
            'local_var': None,
            'l_prefixed_local': 'value',
            'ignored_var': missing,
        },
    )

    assert 'local_var' in variables
    assert 'prefixed_local' in variables
    assert 'templar_var' in variables
    assert 'falsey_templar_var' in variables
    assert 'global_var' in variables

    assert 'l_prefixed_local' not in variables
    assert 'ignored_var' not in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:18:23.565999
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MockTemplar(object):
        available_variables = {
            'available_var': 'available value',
        }

    variables = AnsibleJ2Vars(
        templar=MockTemplar(),
        globals={
            'global_var': 'global value',
        },
        locals={
            'local_var': 'local value',
            'l_prefixed_var': 'prefixed local value',
            'ignored_var': missing,
        },
    )

    assert 'local_var' in variables
    assert 'prefixed_var' in variables
    assert 'available_var' in variables
    assert 'global_var' in variables

    assert 'l_prefixed_var' not in variables
    assert 'ignored_var' not in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:18:30.631975
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class DummyTemplar(object):
        available_variables = {
            'available_var': 'available value',
        }

    variables = AnsibleJ2Vars(
        templar=DummyTemplar(),
        globals={'global_var': 'global value'},
        locals={'local_var': 'local value'},
    )

    assert 'local_var' in variables
    assert 'available_var' in variables
    assert 'global_var' in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:18:39.848490
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = object()
    global_vars = {'global_var': 'global value'}
    local_vars = {
        'local_var': 'local value',
        'l_prefixed_var': 'prefixed value',
        'undefined_var': missing,
        'context': 'ignored',
        'environment': 'ignored',
        'template': 'ignored',
    }

    variables = AnsibleJ2Vars(templar, global_vars, local_vars)

    assert variables._templar is templar
    assert variables._globals is global_vars
    assert variables._locals == {
        'local_var': 'local value',
        'prefixed_var': 'prefixed value',
    }

    variables_without_locals = AnsibleJ2Vars(templar, global_vars)

    assert variables_without_locals._templar is templar
    assert variables_without_locals._globals is global_vars
    assert variables_without_locals._locals == {}

# Generated at 2026-10-25 02:19:04.323481
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest

    class UnsafeValue(object):
        __UNSAFE__ = True

    class DummyTemplar(object):
        def __init__(self):
            self.calls = []
            self.available_variables = {
                'normal': 'normal-source',
                'shadowed': 'shadowed-source',
                'available_wins': 'normal-source',
                'vars': {'answer': 42},
                'unsafe': UnsafeValue(),
                'undefined': 'undefined-source',
                'failure': 'failure-source',
            }

        def template(self, value):
            self.calls.append(value)

            if value == 'undefined-source':
                raise AnsibleUndefinedVariable('nested variable is undefined')
            if value == 'failure-source':
                raise ValueError('templating failed')

            return 'rendered-value'

    templar = DummyTemplar()
    local_value = object()
    global_value = object()
    ignored_local_value = object()

    variables = AnsibleJ2Vars(
        templar,
        globals={
            'global_only': global_value,
            'available_wins': object(),
            'shadowed': object(),
        },
        locals={
            'shadowed': local_value,
            'context': ignored_local_value,
            'not_present': missing,
        },
    )

    # Locals have the highest precedence and are returned without templating.
    assert variables['shadowed'] is local_value
    assert 'shadowed-source' not in templar.calls

    # Available variables take precedence over globals and are templated.
    assert variables['normal'] == 'rendered-value'
    assert variables['available_wins'] == 'rendered-value'

    # Globals are returned without templating.
    assert variables['global_only'] is global_value

    # The special "vars" dictionary and unsafe values are returned unchanged.
    assert variables['vars'] is templar.available_variables['vars']
    assert variables['unsafe'] is templar.available_variables['unsafe']

    # Unknown variables raise KeyError.
    with pytest.raises(KeyError) as exc:
        variables['absent']
    assert 'undefined variable: absent' in str(exc.value)

    # Undefined-variable errors retain the source value as context.
    with pytest.raises(AnsibleUndefinedVariable) as exc:
        variables['undefined']

# Generated at 2026-10-25 02:19:21.495077
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest

    class FakeTemplar(object):
        def __init__(self):
            self.available_variables = {
                'templated': '{{ value }}',
                'vars': {'value': 42},
                'shared': 'from_available_variables',
            }
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            return 'rendered-value'

    templar = FakeTemplar()
    variables = AnsibleJ2Vars(
        templar,
        globals={
            'global_only': 'global-value',
            'shared': 'from_globals',
        },
        locals={
            'local_only': 'local-value',
            'shared': 'from_locals',
        },
    )

    # Locals have the highest precedence and are returned without templating.
    assert variables['local_only'] == 'local-value'
    assert variables['shared'] == 'from_locals'

    # Available variables are templated before being returned.
    assert variables['templated'] == 'rendered-value'
    assert templar.template_calls == ['{{ value }}']

    # The special "vars" dictionary is returned unchanged.
    assert variables['vars'] is templar.available_variables['vars']
    assert templar.template_calls == ['{{ value }}']

    # Globals are used when the variable is not local or otherwise available.
    assert variables['global_only'] == 'global-value'

    # Unknown variables behave like missing mapping keys.
    with pytest.raises(KeyError, match='undefined variable: unknown'):
        variables['unknown']

# Generated at 2026-10-25 02:19:43.606382
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest

    class UnsafeValue(object):
        __UNSAFE__ = True

    class DummyTemplar(object):
        def __init__(self):
            self.available_variables = {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == "broken":
                raise ValueError("template failure")
            return "templated:%s" % value

    templar = DummyTemplar()
    vars_value = {"answer": 42}
    unsafe_value = UnsafeValue()

    templar.available_variables.update({
        "regular": "{{ value }}",
        "shadowed": "available value",
        "vars": vars_value,
        "unsafe": unsafe_value,
        "broken": "broken",
    })

    j2vars = AnsibleJ2Vars(
        templar,
        globals={
            "global_only": "global value",
            "shadowed": "global value",
        },
        locals={
            "l_shadowed": "local value",
        },
    )

    # Locals take precedence over available variables and globals.
    assert j2vars["shadowed"] == "local value"

    # Globals are returned without templating.
    assert j2vars["global_only"] == "global value"

    # Ordinary available variables are templated.
    assert j2vars["regular"] == "templated:{{ value }}"
    assert templar.template_calls == ["{{ value }}"]

    # Special values are returned unchanged.
    assert j2vars["vars"] is vars_value
    assert j2vars["unsafe"] is unsafe_value
    assert templar.template_calls == ["{{ value }}"]

    # Unknown variables raise KeyError.
    with pytest.raises(KeyError) as exc:
        j2vars["unknown"]
    assert exc.value.args == ("undefined variable: unknown",)

    # Unexpected templating errors are wrapped in AnsibleError.
    with pytest.raises(AnsibleError) as exc:
        j2vars["broken"]
    assert "template failure" in str(exc.value)

# Generated at 2026-10-25 02:19:46.247174
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:19:48.664508
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:19:51.259901
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:19:53.674422
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:19:56.090369
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:19:58.507346
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:20:10.371041
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class FakeTemplar(object):
        def __init__(self):
            self.available_variables = {
                'templated': '{{ value }}',
                'vars': {'value': 42},
                'unsafe': UnsafeValue(),
            }
            self.calls = []

        def template(self, value):
            self.calls.append(value)
            return 'rendered: %s' % value

    class UnsafeValue(object):
        __UNSAFE__ = True

    templar = FakeTemplar()
    j2vars = AnsibleJ2Vars(
        templar,
        globals={'global_var': 'global value'},
        locals={
            'local_var': 'local value',
            'l_prefixed': 'prefixed local value',
        },
    )

    # Locals take precedence and l_ prefixes are removed.
    assert j2vars['local_var'] == 'local value'
    assert j2vars['prefixed'] == 'prefixed local value'

    # Available variables are templated.
    assert j2vars['templated'] == 'rendered: {{ value }}'
    assert templar.calls == ['{{ value }}']

    # Globals are returned without templating.
    assert j2vars['global_var'] == 'global value'
    assert templar.calls == ['{{ value }}']

    # The special "vars" dictionary is returned as-is.
    assert j2vars['vars'] is templar.available_variables['vars']

    # Unsafe values are also returned as-is.
    assert j2vars['unsafe'] is templar.available_variables['unsafe']

    try:
        j2vars['undefined']
    except KeyError as exc:
        assert 'undefined variable: undefined' in to_native(exc)
    else:
        raise AssertionError('Accessing an undefined variable did not raise KeyError')

# Generated at 2026-10-25 02:20:21.224606
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest
    from unittest.mock import Mock

    templar = Mock()
    templar.available_variables = {
        'templated_var': '{{ value }}',
        'precedence_var': 'from_available_variables',
    }
    templar.template.side_effect = lambda value: 'rendered' if value == '{{ value }}' else value

    variables = AnsibleJ2Vars(
        templar=templar,
        globals={
            'global_var': 'from_globals',
            'precedence_var': 'from_globals',
        },
        locals={
            'local_var': 'from_locals',
            'precedence_var': 'from_locals',
        },
    )

    # Locals are returned directly and have the highest precedence.
    assert variables['local_var'] == 'from_locals'
    assert variables['precedence_var'] == 'from_locals'

    # Available variables are templated before being returned.
    assert variables['templated_var'] == 'rendered'
    templar.template.assert_called_once_with('{{ value }}')

    # Globals are returned directly when no local or available variable exists.
    assert variables['global_var'] == 'from_globals'

    # Unknown variables raise KeyError.
    with pytest.raises(KeyError, match='undefined variable: unknown_var'):
        variables['unknown_var']

# Generated at 2026-10-25 02:20:48.983517
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:20:51.398925
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:20:53.814239
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:20:56.229970
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:20:58.645249
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:21:01.060034
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:21:10.898561
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():from unittest.mock import Mock

# Generated at 2026-10-25 02:21:35.987360
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest

    class UnsafeValue(object):
        __UNSAFE__ = True

    class FakeTemplar(object):
        def __init__(self):
            self.calls = []
            self.available_variables = {
                'regular': '{{ answer }}',
                'vars': {'untemplated': '{{ value }}'},
                'unsafe': UnsafeValue(),
                'available_wins': 'available value',
                'undefined': 'undefined value',
                'broken': 'broken value',
            }

        def template(self, value):
            self.calls.append(value)

            if value == 'undefined value':
                raise AnsibleUndefinedVariable('nested variable is undefined')
            if value == 'broken value':
                raise ValueError('templating failed')

            return 'templated: %s' % value

    templar = FakeTemplar()
    global_value = object()

# Generated at 2026-10-25 02:21:54.210539
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class DummyTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            return "templated:%s" % value

    class UnsafeValue(object):
        __UNSAFE__ = True

    vars_value = {"answer": 42}
    unsafe_value = UnsafeValue()

    templar = DummyTemplar({
        "value": "raw-value",
        "local": "available-value",
        "vars": vars_value,
        "unsafe": unsafe_value,
    })

    variables = AnsibleJ2Vars(
        templar,
        globals={
            "global_value": "from-globals",
            "value": "global-value",
        },
        locals={
            "l_local": "from-locals",
            "context": "ignored",
            "missing_value": missing,
        },
    )

    # Locals have the highest precedence and l_ is stripped.
    assert variables["local"] == "from-locals"

    # Available variables are templated and take precedence over globals.
    assert variables["value"] == "templated:raw-value"
    assert templar.template_calls == ["raw-value"]

    # Globals are returned directly rather than templated.
    assert variables["global_value"] == "from-globals"
    assert templar.template_calls == ["raw-value"]

    # The special "vars" dictionary and unsafe values are returned unchanged.
    assert variables["vars"] is vars_value
    assert variables["unsafe"] is unsafe_value
    assert templar.template_calls == ["raw-value"]

    # Ignored and undefined variables raise KeyError.
    for key in ("context", "missing_value", "undefined"):
        try:
            variables[key]
        except KeyError as exc:
            assert key in to_native(exc)
        else:
            raise AssertionError("Expected KeyError for %r" % key)

    # Unexpected templating errors are wrapped in AnsibleError.
    class FailingTemplar(object):
        available_variables = {"broken": "bad-value"}

        def template(self, value):
            raise ValueError("template failed")

    failing_variables = AnsibleJ2Vars(FailingTemplar(), {})

    try:
        failing_variables["broken"]
    except AnsibleError as exc:
        message = to_native(exc)
        assert "bad-value" in message
        assert "ValueError" in message
        assert "template failed" in message
    else:
        raise AssertionError("Expected AnsibleError")

# Generated at 2026-10-25 02:21:56.623614
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:21:59.038914
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:22:01.457106
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:22:04.110027
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 02:22:13.774417
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = object()
    globals_vars = {'global_var': 'global_value'}
    local_vars = {
        'normal_var': 'normal_value',
        'l_scoped_var': 'scoped_value',
        'missing_var': missing,
        'context': 'ignored',
        'environment': 'ignored',
        'template': 'ignored',
    }

    j2_vars = AnsibleJ2Vars(templar, globals_vars, locals=local_vars)

    assert j2_vars._templar is templar
    assert j2_vars._globals is globals_vars
    assert j2_vars._locals == {
        'normal_var': 'normal_value',
        'scoped_var': 'scoped_value',
    }

    # None and non-dictionary locals should be ignored.
    assert AnsibleJ2Vars(templar, globals_vars)._locals == {}
    assert AnsibleJ2Vars(templar, globals_vars, locals=[])._locals == {}

# Generated at 2026-10-25 02:22:26.772611
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest

    class UnsafeValue(object):
        __UNSAFE__ = True

    class FakeTemplar(object):
        def __init__(self):
            self.available_variables = {
                'templated': '{{ value }}',
                'precedence': 'from available variables',
                'vars': {'raw': '{{ value }}'},
                'unsafe': UnsafeValue(),
                'undefined': '{{ missing_variable }}',
                'failure': '{{ broken }}',
            }
            self.calls = []

        def template(self, value):
            self.calls.append(value)

            if value == '{{ missing_variable }}':
                raise AnsibleUndefinedVariable('missing_variable is undefined')
            if value == '{{ broken }}':
                raise ValueError('templating failed')
            if value == '{{ value }}':
                return 'rendered value'

            return 'templated: %s' % value

    templar = FakeTemplar()
    globals_ = {
        'global_only': 'global value',
        'precedence': 'from globals',
    }
    locals_ = {
        'local_only': 'local value',
        'precedence': 'from locals',
    }

    variables = AnsibleJ2Vars(templar, globals_, locals_)

    # Locals have the highest precedence and are returned without templating.
    assert variables['local_only'] == 'local value'
    assert variables['precedence'] == 'from locals'

    # Available variables are templated before being returned.
    assert variables['templated'] == 'rendered value'
    assert '{{ value }}' in templar.calls

    # Globals are returned directly.
    assert variables['global_only'] == 'global value'

    # The special "vars" dictionary and unsafe values are returned unchanged.
    assert variables['vars'] is templar.available_variables['vars']
    assert variables['unsafe'] is templar.available_variables['unsafe']

    # Unknown variables raise KeyError.
    with pytest.raises(KeyError, match='undefined variable: unknown'):
        variables['unknown']

    # AnsibleUndefinedVariable is preserved with additional context.
    with pytest.raises(AnsibleUndefinedVariable) as exc_info:
        variables['undefined']
    assert 'missing_variable is undefined' in to_native(exc_info.value)

    # Other templating exceptions are wrapped in AnsibleError.
    with pytest.raises(AnsibleError) as exc_info:
        variables['failure']
    assert 'templating failed' in to_native(exc_info.value)
    assert 'ValueError' in to_native(exc_info.value)

# Generated at 2026-10-25 02:22:36.306272
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MockTemplar(object):
        available_variables = {
            'available_var': 'available value',
        }

    variables = AnsibleJ2Vars(
        templar=MockTemplar(),
        globals={'global_var': 'global value'},
        locals={'local_var': 'local value'},
    )

    assert 'local_var' in variables
    assert 'available_var' in variables
    assert 'global_var' in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:22:55.649374
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest

    class UnsafeValue(object):
        __UNSAFE__ = True

    class DummyTemplar(object):
        def __init__(self):
            self.available_variables = {
                'normal': 'normal-value',
                'shared': 'available-value',
                'available_over_global': 'available-value',
                'vars': {'answer': 42},
                'unsafe': UnsafeValue(),
                'undefined': 'undefined-value',
                'broken': 'broken-value',
            }
            self.templated = []

        def template(self, value):
            self.templated.append(value)

            if value == 'undefined-value':
                raise AnsibleUndefinedVariable('referenced variable is undefined')
            if value == 'broken-value':
                raise ValueError('templating failed')

            return 'templated:%s' % value

    templar = DummyTemplar()
    globals_ = {
        'global_only': 'global-value',
        'shared': 'global-value',
        'available_over_global': 'global-value',
    }
    locals_ = {
        'local_only': 'local-value',
        'shared': 'local-value',
    }

    variables = AnsibleJ2Vars(templar, globals_, locals_)

    # Locals have the highest precedence and are returned without templating.
    assert variables['local_only'] == 'local-value'
    assert variables['shared'] == 'local-value'
    assert templar.templated == []

    # Available variables take precedence over globals and are templated.
    assert variables['normal'] == 'templated:normal-value'
    assert variables['available_over_global'] == 'templated:available-value'

    # Globals are returned without templating.
    assert variables['global_only'] == 'global-value'

    # The special "vars" dictionary and unsafe values must be returned as-is.
    vars_value = templar.available_variables['vars']
    unsafe_value = templar.available_variables['unsafe']

    assert variables['vars'] is vars_value
    assert variables['unsafe'] is unsafe_value
    assert vars_value not in templar.templated
    assert unsafe_value not in templar.templated

    # Unknown variables raise KeyError.
    with pytest.raises(KeyError, match='undefined variable: unknown'):
        variables['unknown']

    # Undefined-variable errors retain their type and include context.
    with pytest.raises(AnsibleUndefinedVariable) as exc_info:
        variables['undefined']

    assert 'undefined-value' in str(exc_info.value)
    assert 'referenced variable is undefined' in str(exc_info.value)

    # Other templating exceptions are wrapped in AnsibleError.
    with pytest.raises(AnsibleError) as exc_info:
        variables['broken']

    message = str(exc_info.value)
    assert 'broken-value' in message
    assert 'ValueError' in message
    assert 'templating failed' in message

# Generated at 2026-10-25 02:22:58.064963
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:00.481506
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:02.894884
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:05.308840
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:07.723151
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:10.139298
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:17.705763
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class DummyTemplar(object):
        available_variables = {'available_var': 'available_value'}

    variables = AnsibleJ2Vars(
        templar=DummyTemplar(),
        globals={'global_var': 'global_value'},
        locals={'local_var': 'local_value'},
    )

    assert 'local_var' in variables
    assert 'available_var' in variables
    assert 'global_var' in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:23:25.035704
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class DummyTemplar(object):
        available_variables = {
            'available_var': 'available value',
        }

    variables = AnsibleJ2Vars(
        templar=DummyTemplar(),
        globals={'global_var': 'global value'},
        locals={'local_var': 'local value'},
    )

    assert 'local_var' in variables
    assert 'available_var' in variables
    assert 'global_var' in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:23:33.895537
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MockTemplar(object):
        available_variables = {
            'templar_var': 'templar value',
            'templar_none': None,
        }

    variables = AnsibleJ2Vars(
        templar=MockTemplar(),
        globals={
            'global_var': 'global value',
            'global_none': None,
        },
        locals={
            'local_var': 'local value',
            'local_none': None,
        },
    )

    assert 'local_var' in variables
    assert 'local_none' in variables
    assert 'templar_var' in variables
    assert 'templar_none' in variables
    assert 'global_var' in variables
    assert 'global_none' in variables
    assert 'undefined_var' not in variables

# Generated at 2026-10-25 02:23:41.316010
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class DummyTemplar(object):
        available_variables = {
            'available_var': 'available value',
        }

    j2vars = AnsibleJ2Vars(
        DummyTemplar(),
        globals={'global_var': 'global value'},
        locals={
            'local_var': 'local value',
            'l_prefixed_var': 'prefixed local value',
            'context': 'ignored',
            'environment': 'ignored',
            'template': 'ignored',
        },
    )

    assert 'local_var' in j2vars
    assert 'prefixed_var' in j2vars
    assert 'available_var' in j2vars
    assert 'global_var' in j2vars

    assert 'l_prefixed_var' not in j2vars
    assert 'context' not in j2vars
    assert 'environment' not in j2vars
    assert 'template' not in j2vars
    assert 'undefined_var' not in j2vars

# Generated at 2026-10-25 02:23:43.735450
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:46.264443
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:48.681877
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:51.103048
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:53.707924
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:56.125520
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:23:59.817439
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:24:02.231809
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:24:04.645905
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:24:07.061681
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:24:09.477157
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:24:11.893156
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 02:24:14.536264
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 02:24:26.886145
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class DummyTemplar(object):
        def __init__(self):
            self.available_variables = {
                'templated': '{{ value }}',
                'shared': 'available value',
                'vars': {'unmodified': '{{ value }}'},
            }
            self.calls = []

        def template(self, value):
            self.calls.append(value)
            return 'rendered: %s' % value

    templar = DummyTemplar()
    variables = AnsibleJ2Vars(
        templar,
        globals={
            'global_only': 'global value',
            'shared': 'global value',
        },
        locals={
            'local_only': 'local value',
            'shared': 'local value',
        },
    )

    # Locals take precedence and are returned without templating.
    assert variables['local_only'] == 'local value'
    assert variables['shared'] == 'local value'

    # Available variables are templated before being returned.
    assert variables['templated'] == 'rendered: {{ value }}'
    assert templar.calls == ['{{ value }}']

    # Globals are returned directly.
    assert variables['global_only'] == 'global value'

    # The special "vars" mapping must not be templated.
    assert variables['vars'] == {'unmodified': '{{ value }}'}
    assert templar.calls == ['{{ value }}']

    # Unknown variables raise KeyError.
    try:
        variables['undefined']
    except KeyError as exc:
        assert 'undefined variable: undefined' in str(exc)
    else:
        raise AssertionError('Expected KeyError for an undefined variable')