

# Generated at 2026-10-25 10:54:49.554845
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.templarized = []

        def template(self, variable):
            self.templarized.append(variable)
            if isinstance(variable, str) and variable.startswith('FAIL_UNDEFINED'):
                raise AnsibleUndefinedVariable("'some_undefined_var' is undefined")
            if isinstance(variable, str) and variable.startswith('FAIL_OTHER'):
                raise Exception("boom")
            return 'templated:%s' % variable

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    # 1. var found in available_variables gets templated
    templar = FakeTemplar({'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['foo'] == 'templated:bar'
    assert templar.templarized == ['bar']

    # 2. var found in locals is returned as-is, without templating
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'localvar': 'raw_value'})
    assert j2vars['localvar'] == 'raw_value'
    assert templar.templarized == ['bar']

    # 3. var found only in globals is returned as-is, without templating
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['range'] is range

    # 4. the special variable 'vars' (a dict) is returned as-is
    special_vars = {'a': 1}
    templar = FakeTemplar({'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['vars'] is special_vars
    assert templar.templarized == []

    # 5. objects marked __UNSAFE__ are returned as-is
    class UnsafeStr(str):
        __UNSAFE__ = True

    unsafe = UnsafeStr('unsafe_string')
    templar = FakeTemplar({'unsafe_var': unsafe})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['unsafe_var'] is unsafe
    assert templar.templarized == []

    # 6. undefined variable raises KeyError
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['nope']
    except KeyError as e:
        assert to_native(e) == "'undefined variable: nope'"
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 7. AnsibleUndefinedVariable during templating is wrapped with the variable name
    templar = FakeTemplar({'badvar': 'FAIL_UNDEFINED'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleUndefinedVariable as e:
        assert 'FAIL_UNDEFINED' in to_native(e)
        assert 'some_undefined_var' in to_native(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 8. other exceptions during templating are wrapped in AnsibleError
    templar = FakeTemplar({'badvar': 'FAIL_OTHER'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleError as e:
        assert "An unhandled exception occurred while templating" in to_native(e)
        assert "boom" in to_native(e)
    else:
        raise AssertionError("expected AnsibleError")

# Generated at 2026-10-25 10:55:06.001252
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    templar = pytest.importorskip("unittest.mock").MagicMock()
    templar.available_variables = {'hostvar': 'hv'}
    templar.template.side_effect = lambda v: v  # identity, so values pass through

    v = AnsibleJ2Vars(templar, {'range': range}, locals={'l_foo': 1, 'context': 'x'})

    # 1. None -> returns self, no copy
    assert v.add_locals(None) is v

    # 2. dict -> new instance, original untouched
    v2 = v.add_locals({'bar': 2})
    assert v2 is not v
    assert isinstance(v2, AnsibleJ2Vars)
    assert v2['bar'] == 2
    assert v2['foo'] == 1        # pre-existing locals carried over (l_ prefix stripped)
    assert 'bar' not in v        # source object not mutated

    # 3. templar vars and globals still resolve through the copy
    assert v2['hostvar'] == 'hv'
    assert v2['range'] is range
    assert 'bar' in v2 and 'hostvar' in v2 and 'range' in v2

    # 4. locals take precedence over templar vars of the same name
    templar.available_variables = {'foo': 'from_templar'}
    assert v2['foo'] == 1

    # 5. new locals shadow old locals, old copy unaffected
    v3 = v2.add_locals({'foo': 99})
    assert v3['foo'] == 99
    assert v2['foo'] == 1

    # 6. constructor filtering is applied again to locals passed via add_locals
    assert 'context' not in v.add_locals({'context': 'x'})
    assert v.add_locals({'l_baz': 3})['baz'] == 3

# Generated at 2026-10-25 10:55:08.907460
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.templarized = []

        def template(self, variable):
            self.templarized.append(variable)
            if isinstance(variable, str) and variable.startswith('FAIL_UNDEFINED'):
                raise AnsibleUndefinedVariable("'some_undefined_var' is undefined")
            if isinstance(variable, str) and variable.startswith('FAIL_OTHER'):
                raise Exception("boom")
            return 'templated:%s' % variable

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    # 1. var found in available_variables gets templated
    templar = FakeTemplar({'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['foo'] == 'templated:bar'
    assert templar.templarized == ['bar']

    # 2. var found in locals is returned as-is, without templating
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'localvar': 'raw_value'})
    assert j2vars['localvar'] == 'raw_value'
    assert templar.templarized == ['bar']

    # 3. var found only in globals is returned as-is, without templating
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['range'] is range

    # 4. the special variable 'vars' (a dict) is returned as-is
    special_vars = {'a': 1}
    templar = FakeTemplar({'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['vars'] is special_vars
    assert templar.templarized == []

    # 5. objects marked __UNSAFE__ are returned as-is
    class UnsafeStr(str):
        __UNSAFE__ = True

    unsafe = UnsafeStr('unsafe_string')
    templar = FakeTemplar({'unsafe_var': unsafe})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['unsafe_var'] is unsafe
    assert templar.templarized == []

    # 6. undefined variable raises KeyError
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['nope']
    except KeyError as e:
        assert to_native(e) == "'undefined variable: nope'"
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 7. AnsibleUndefinedVariable during templating is wrapped with the variable name
    templar = FakeTemplar({'badvar': 'FAIL_UNDEFINED'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleUndefinedVariable as e:
        assert 'FAIL_UNDEFINED' in to_native(e)
        assert 'some_undefined_var' in to_native(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 8. other exceptions during templating are wrapped in AnsibleError
    templar = FakeTemplar({'badvar': 'FAIL_OTHER'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleError as e:
        assert "An unhandled exception occurred while templating" in to_native(e)
        assert "boom" in to_native(e)
    else:
        raise AssertionError("expected AnsibleError")

# Generated at 2026-10-25 10:55:26.113772
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    templar = pytest.importorskip("unittest.mock").MagicMock()
    templar.available_variables = {'hostvar': 'hv'}
    templar.template.side_effect = lambda v: v  # identity, so values pass through

    v = AnsibleJ2Vars(templar, {'range': range}, locals={'l_foo': 1, 'context': 'x'})

    # 1. None -> returns self, no copy
    assert v.add_locals(None) is v

    # 2. dict -> new instance, original untouched
    v2 = v.add_locals({'bar': 2})
    assert v2 is not v
    assert isinstance(v2, AnsibleJ2Vars)
    assert v2['bar'] == 2
    assert v2['foo'] == 1        # pre-existing locals carried over (l_ prefix stripped)
    assert 'bar' not in v        # source object not mutated

    # 3. templar vars and globals still resolve through the copy
    assert v2['hostvar'] == 'hv'
    assert v2['range'] is range
    assert 'bar' in v2 and 'hostvar' in v2 and 'range' in v2

    # 4. locals take precedence over templar vars of the same name
    templar.available_variables = {'foo': 'from_templar'}
    assert v2['foo'] == 1

    # 5. new locals shadow old locals, old copy unaffected
    v3 = v2.add_locals({'foo': 99})
    assert v3['foo'] == 99
    assert v2['foo'] == 1

    # 6. constructor filtering is applied again to locals passed via add_locals
    assert 'context' not in v.add_locals({'context': 'x'})
    assert v.add_locals({'l_baz': 3})['baz'] == 3

# Generated at 2026-10-25 10:55:27.486812
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from unittest.mock import MagicMock
    from jinja2.utils import missing
    from ansible.template.vars import AnsibleJ2Vars

    # 1. all empty
    templar = MagicMock()
    templar.available_variables = {}
    assert len(AnsibleJ2Vars(templar, {})) == 0
    assert len(AnsibleJ2Vars(templar, {}, {})) == 0

    # 2. distinct keys are summed
    templar.available_variables = {'a': 1, 'b': 2}
    obj = AnsibleJ2Vars(templar, {'c': 3}, {'d': 4})
    assert len(obj) == 4  # {a,b,c,d}

    # 3. overlapping keys are deduplicated (set union)
    templar.available_variables = {'a': 1, 'b': 2}
    obj = AnsibleJ2Vars(templar, {'b': 20, 'c': 30}, {'c': 300, 'd': 400})
    assert len(obj) == 4  # {a,b,c,d}, not 2+2+2=6
    assert len(obj) == len(list(iter(obj)))
    assert len(obj) == len(set(iter(obj)))

    # 4. locals filtering affects __len__
    # 'l_' prefix stripped, 'context'/'environment'/'template' excluded,
    # 'missing'

# Generated at 2026-10-25 10:55:45.771255
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.templarized = []

        def template(self, variable):
            self.templarized.append(variable)
            if isinstance(variable, str) and variable.startswith('FAIL_UNDEFINED'):
                raise AnsibleUndefinedVariable("'some_undefined_var' is undefined")
            if isinstance(variable, str) and variable.startswith('FAIL_OTHER'):
                raise Exception("boom")
            return 'templated:%s' % variable

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    # 1. var found in available_variables gets templated
    templar = FakeTemplar({'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['foo'] == 'templated:bar'
    assert templar.templarized == ['bar']

    # 2. var found in locals is returned as-is, without templating
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'localvar': 'raw_value'})
    assert j2vars['localvar'] == 'raw_value'
    assert templar.templarized == ['bar']

    # 3. var found only in globals is returned as-is, without templating
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['range'] is range

    # 4. the special variable 'vars' (a dict) is returned as-is
    special_vars = {'a': 1}
    templar = FakeTemplar({'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['vars'] is special_vars
    assert templar.templarized == []

    # 5. objects marked __UNSAFE__ are returned as-is
    class UnsafeStr(str):
        __UNSAFE__ = True

    unsafe = UnsafeStr('unsafe_string')
    templar = FakeTemplar({'unsafe_var': unsafe})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['unsafe_var'] is unsafe
    assert templar.templarized == []

    # 6. undefined variable raises KeyError
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['nope']
    except KeyError as e:
        assert to_native(e) == "'undefined variable: nope'"
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 7. AnsibleUndefinedVariable during templating is wrapped with the variable name
    templar = FakeTemplar({'badvar': 'FAIL_UNDEFINED'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleUndefinedVariable as e:
        assert 'FAIL_UNDEFINED' in to_native(e)
        assert 'some_undefined_var' in to_native(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 8. other exceptions during templating are wrapped in AnsibleError
    templar = FakeTemplar({'badvar': 'FAIL_OTHER'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleError as e:
        assert "An unhandled exception occurred while templating" in to_native(e)
        assert "boom" in to_native(e)
    else:
        raise AssertionError("expected AnsibleError")

# Generated at 2026-10-25 10:55:48.189977
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:55:50.602497
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:55:53.018493
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:55:55.434011
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:55:57.849186
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:56:00.263179
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:56:02.677944
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:56:05.095924
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:56:12.013307
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:56:18.029391
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from unittest.mock import MagicMock
    from ansible.template import AnsibleJ2Vars

    # Mock Templar with a known set of available variables
    templar = MagicMock()
    templar.available_variables = {'available_var': 'value'}

    globals_dict = {'global_var': 'gvalue', 'range': range}

    # Case 1 + 2: locals + globals in one call, then check each scope separately
    j2vars = AnsibleJ2Vars(
        templar,
        globals_dict,
        locals={'l_local_var': 'local_value', 'local_var2': 'v2'}
    )

    # 1. Variable in locals (both 'l_' prefixed and plain) -> True
    assert 'local_var' in j2vars
    assert 'local_var2' in j2vars

    # 2. Variable in templar.available_variables -> True
    assert 'available_var' in j2vars

    # 3. Variable in globals -> True
    assert 'global_var' in j2vars
    assert 'range' in j2vars

    # 4. Variable in none of the scopes -> False
    assert 'missing_var' not in j2vars

    # Edge: 'l_' prefixed key passed directly as locals dict key without prefix handling
    # (constructor strips 'l_' prefix, so original key must not be found)
    assert 'l_local_var' not in j2vars

    # Edge: reserved names in locals are skipped by constructor
    j2vars_reserved = AnsibleJ2Vars(
        templar,
        globals_dict,
        locals={'context': 'ctx', 'environment': 'env', 'template': 'tpl'}
    )
    assert 'context' not in j2vars_reserved
    assert 'environment' not in j2vars_reserved
    assert 'template' not in j2vars_reserved

    # Edge: 'missing' sentinel values are filtered out by constructor
    from jinja2.utils import missing
    j2vars_missing = AnsibleJ2Vars(
        templar,
        globals_dict,
        locals={'l_gone': missing, 'kept': 'yes'}
    )
    assert 'gone' not in j2vars_missing
    assert 'kept' in j2vars_missing

    # Edge: non-dict locals argument is ignored entirely
    j2vars_none = AnsibleJ2Vars(templar, globals_dict, locals=None)
    assert 'local_var' not in j2vars_none
    assert 'global_var' in j2vars_none

# Generated at 2026-10-25 10:56:20.916501
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class FakeTemplar(object):
        def __init__(self, variables):
            self.available_variables = variables

        def template(self, variable):
            return variable

    templar = FakeTemplar({'foo': 'bar', 'vars': {'a': 1}})
    globals_ = {'range': range, 'lookup': object()}
    locals_ = {
        'l_local_var': 'local',
        'other': 'value',
        'context': 'ignored',
        'environment': 'ignored',
        'template': 'ignored',
        'l_missing': missing,
    }

    variables = AnsibleJ2Vars(templar, globals_, locals_)

    assert 'foo' in variables
    assert 'vars' in variables
    assert 'local_var' in variables
    assert 'other' in variables
    assert 'range' in variables
    assert 'lookup' in variables
    assert 'missing_var' not in variables
    assert 'l_local_var' not in variables
    assert 'missing' not in variables
    assert 'context' not in variables
    assert 'environment' not in variables
    assert 'template' not in variables

# Generated at 2026-10-25 10:56:38.772170
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.templarized = []

        def template(self, variable):
            self.templarized.append(variable)
            if isinstance(variable, str) and variable.startswith('FAIL_UNDEFINED'):
                raise AnsibleUndefinedVariable("'some_undefined_var' is undefined")
            if isinstance(variable, str) and variable.startswith('FAIL_OTHER'):
                raise Exception("boom")
            return 'templated:%s' % variable

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    # 1. var found in available_variables gets templated
    templar = FakeTemplar({'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['foo'] == 'templated:bar'
    assert templar.templarized == ['bar']

    # 2. var found in locals is returned as-is, without templating
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'localvar': 'raw_value'})
    assert j2vars['localvar'] == 'raw_value'
    assert templar.templarized == ['bar']

    # 3. var found only in globals is returned as-is, without templating
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['range'] is range

    # 4. the special variable 'vars' (a dict) is returned as-is
    special_vars = {'a': 1}
    templar = FakeTemplar({'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['vars'] is special_vars
    assert templar.templarized == []

    # 5. objects marked __UNSAFE__ are returned as-is
    class UnsafeStr(str):
        __UNSAFE__ = True

    unsafe = UnsafeStr('unsafe_string')
    templar = FakeTemplar({'unsafe_var': unsafe})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['unsafe_var'] is unsafe
    assert templar.templarized == []

    # 6. undefined variable raises KeyError
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['nope']
    except KeyError as e:
        assert to_native(e) == "'undefined variable: nope'"
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 7. AnsibleUndefinedVariable during templating is wrapped with the variable name
    templar = FakeTemplar({'badvar': 'FAIL_UNDEFINED'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleUndefinedVariable as e:
        assert 'FAIL_UNDEFINED' in to_native(e)
        assert 'some_undefined_var' in to_native(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 8. other exceptions during templating are wrapped in AnsibleError
    templar = FakeTemplar({'badvar': 'FAIL_OTHER'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleError as e:
        assert "An unhandled exception occurred while templating" in to_native(e)
        assert "boom" in to_native(e)
    else:
        raise AssertionError("expected AnsibleError")

# Generated at 2026-10-25 10:56:42.912047
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.templarized = []

        def template(self, variable):
            self.templarized.append(variable)
            if isinstance(variable, str) and variable.startswith('FAIL_UNDEFINED'):
                raise AnsibleUndefinedVariable("'some_undefined_var' is undefined")
            if isinstance(variable, str) and variable.startswith('FAIL_OTHER'):
                raise Exception("boom")
            return 'templated:%s' % variable

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    # 1. var found in available_variables gets templated
    templar = FakeTemplar({'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['foo'] == 'templated:bar'
    assert templar.templarized == ['bar']

    # 2. var found in locals is returned as-is, without templating
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'localvar': 'raw_value'})
    assert j2vars['localvar'] == 'raw_value'
    assert templar.templarized == ['bar']

    # 3. var found only in globals is returned as-is, without templating
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['range'] is range

    # 4. the special variable 'vars' (a dict) is returned as-is
    special_vars = {'a': 1}
    templar = FakeTemplar({'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['vars'] is special_vars
    assert templar.templarized == []

    # 5. objects marked __UNSAFE__ are returned as-is
    class UnsafeStr(str):
        __UNSAFE__ = True

    unsafe = UnsafeStr('unsafe_string')
    templar = FakeTemplar({'unsafe_var': unsafe})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['unsafe_var'] is unsafe
    assert templar.templarized == []

    # 6. undefined variable raises KeyError
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['nope']
    except KeyError as e:
        assert to_native(e) == "'undefined variable: nope'"
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 7. AnsibleUndefinedVariable during templating is wrapped with the variable name
    templar = FakeTemplar({'badvar': 'FAIL_UNDEFINED'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleUndefinedVariable as e:
        assert 'FAIL_UNDEFINED' in to_native(e)
        assert 'some_undefined_var' in to_native(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 8. other exceptions during templating are wrapped in AnsibleError
    templar = FakeTemplar({'badvar': 'FAIL_OTHER'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleError as e:
        assert "An unhandled exception occurred while templating" in to_native(e)
        assert "boom" in to_native(e)
    else:
        raise AssertionError("expected AnsibleError")

# Generated at 2026-10-25 10:56:44.546523
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:57:04.106304
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class FakeTemplar(object):
        def __init__(self, variables):
            self.available_variables = variables

        def template(self, variable):
            return variable

    templar = FakeTemplar({'foo': 'bar', 'vars': {'a': 1}})
    globals_ = {'range': range, 'lookup': object()}
    locals_ = {
        'l_local_var': 'local',
        'other': 'value',
        'context': 'ignored',
        'environment': 'ignored',
        'template': 'ignored',
        'l_missing': missing,
    }

    variables = AnsibleJ2Vars(templar, globals_, locals_)

    assert 'foo' in variables
    assert 'vars' in variables
    assert 'local_var' in variables
    assert 'other' in variables
    assert 'range' in variables
    assert 'lookup' in variables
    assert 'missing_var' not in variables
    assert 'l_local_var' not in variables
    assert 'missing' not in variables
    assert 'context' not in variables
    assert 'environment' not in variables
    assert 'template' not in variables

# Generated at 2026-10-25 10:57:06.523763
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:57:08.938924
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:57:11.357357
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:57:28.111521
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    from jinja2.utils import missing
    class FakeTemplar:
        def __init__(self):
            self.available_variables = {'a_var': 'a_value'}
        def template(self, variable):
            return variable
    templar = FakeTemplar()
    globals_dict = {'g_var': 'g_value'}
    proxy = AnsibleJ2Vars(templar, globals_dict, locals={'x': 1, 'y': 2})
    assert proxy._locals == {'x': 1, 'y': 2}
    assert proxy._templar is templar
    assert proxy._globals is globals_dict
    same = proxy.add_locals(None)
    assert same is proxy
    added = proxy.add_locals({'z': 3})
    assert isinstance(added, AnsibleJ2Vars)
    assert added is not proxy
    assert added._templar is templar
    assert added._globals is globals_dict
    assert added._locals == {'x': 1, 'y': 2, 'z': 3}
    assert proxy._locals == {'x': 1, 'y': 2}
    assert 'z' in added
    assert added['z'] == 3
    assert added['x'] == 1
    overwritten = proxy.add_locals({'x': 99})
    assert overwritten._locals == {'x': 99, 'y': 2}
    assert overwritten['x'] == 99
    assert proxy['x'] == 1
    stripped = proxy.add_locals({'l_foo': 'bar'})
    assert stripped._locals.get('foo') == 'bar'
    assert 'l_foo' not in stripped._locals
    assert 'foo' in stripped
    assert stripped['foo'] == 'bar'
    filtered = proxy.add_locals({'context': 'c', 'environment': 'e', 'template': 't', 'ok': 'v'})

# Generated at 2026-10-25 10:57:45.153299
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    templar = pytest.importorskip("unittest.mock").MagicMock()
    templar.available_variables = {'hostvar': 'hv'}
    templar.template.side_effect = lambda v: v  # identity, so values pass through

    v = AnsibleJ2Vars(templar, {'range': range}, locals={'l_foo': 1, 'context': 'x'})

    # 1. None -> returns self, no copy
    assert v.add_locals(None) is v

    # 2. dict -> new instance, original untouched
    v2 = v.add_locals({'bar': 2})
    assert v2 is not v
    assert isinstance(v2, AnsibleJ2Vars)
    assert v2['bar'] == 2
    assert v2['foo'] == 1        # pre-existing locals carried over (l_ prefix stripped)
    assert 'bar' not in v        # source object not mutated

    # 3. templar vars and globals still resolve through the copy
    assert v2['hostvar'] == 'hv'
    assert v2['range'] is range
    assert 'bar' in v2 and 'hostvar' in v2 and 'range' in v2

    # 4. locals take precedence over templar vars of the same name
    templar.available_variables = {'foo': 'from_templar'}
    assert v2['foo'] == 1

    # 5. new locals shadow old locals, old copy unaffected
    v3 = v2.add_locals({'foo': 99})
    assert v3['foo'] == 99
    assert v2['foo'] == 1

    # 6. constructor filtering is applied again to locals passed via add_locals
    assert 'context' not in v.add_locals({'context': 'x'})
    assert v.add_locals({'l_baz': 3})['baz'] == 3

# Generated at 2026-10-25 10:58:03.204743
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.templarized = []

        def template(self, variable):
            self.templarized.append(variable)
            if isinstance(variable, str) and variable.startswith('FAIL_UNDEFINED'):
                raise AnsibleUndefinedVariable("'some_undefined_var' is undefined")
            if isinstance(variable, str) and variable.startswith('FAIL_OTHER'):
                raise Exception("boom")
            return 'templated:%s' % variable

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    # 1. var found in available_variables gets templated
    templar = FakeTemplar({'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['foo'] == 'templated:bar'
    assert templar.templarized == ['bar']

    # 2. var found in locals is returned as-is, without templating
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'localvar': 'raw_value'})
    assert j2vars['localvar'] == 'raw_value'
    assert templar.templarized == ['bar']

    # 3. var found only in globals is returned as-is, without templating
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['range'] is range

    # 4. the special variable 'vars' (a dict) is returned as-is
    special_vars = {'a': 1}
    templar = FakeTemplar({'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['vars'] is special_vars
    assert templar.templarized == []

    # 5. objects marked __UNSAFE__ are returned as-is
    class UnsafeStr(str):
        __UNSAFE__ = True

    unsafe = UnsafeStr('unsafe_string')
    templar = FakeTemplar({'unsafe_var': unsafe})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['unsafe_var'] is unsafe
    assert templar.templarized == []

    # 6. undefined variable raises KeyError
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['nope']
    except KeyError as e:
        assert to_native(e) == "'undefined variable: nope'"
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 7. AnsibleUndefinedVariable during templating is wrapped with the variable name
    templar = FakeTemplar({'badvar': 'FAIL_UNDEFINED'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleUndefinedVariable as e:
        assert 'FAIL_UNDEFINED' in to_native(e)
        assert 'some_undefined_var' in to_native(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 8. other exceptions during templating are wrapped in AnsibleError
    templar = FakeTemplar({'badvar': 'FAIL_OTHER'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleError as e:
        assert "An unhandled exception occurred while templating" in to_native(e)
        assert "boom" in to_native(e)
    else:
        raise AssertionError("expected AnsibleError")

# Generated at 2026-10-25 10:58:05.627142
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:58:08.035920
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:58:10.450588
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:58:12.864682
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:58:15.281877
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:58:17.699210
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:58:20.114515
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:58:22.528430
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:58:25.199373
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:58:28.384485
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.templarized = []

        def template(self, variable):
            self.templarized.append(variable)
            if isinstance(variable, str) and variable.startswith('FAIL_UNDEFINED'):
                raise AnsibleUndefinedVariable("'some_undefined_var' is undefined")
            if isinstance(variable, str) and variable.startswith('FAIL_OTHER'):
                raise Exception("boom")
            return 'templated:%s' % variable

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    # 1. var found in available_variables gets templated
    templar = FakeTemplar({'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['foo'] == 'templated:bar'
    assert templar.templarized == ['bar']

    # 2. var found in locals is returned as-is, without templating
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'localvar': 'raw_value'})
    assert j2vars['localvar'] == 'raw_value'
    assert templar.templarized == ['bar']

    # 3. var found only in globals is returned as-is, without templating
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['range'] is range

    # 4. the special variable 'vars' (a dict) is returned as-is
    special_vars = {'a': 1}
    templar = FakeTemplar({'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['vars'] is special_vars
    assert templar.templarized == []

    # 5. objects marked __UNSAFE__ are returned as-is
    class UnsafeStr(str):
        __UNSAFE__ = True

    unsafe = UnsafeStr('unsafe_string')
    templar = FakeTemplar({'unsafe_var': unsafe})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['unsafe_var'] is unsafe
    assert templar.templarized == []

    # 6. undefined variable raises KeyError
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['nope']
    except KeyError as e:
        assert to_native(e) == "'undefined variable: nope'"
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 7. AnsibleUndefinedVariable during templating is wrapped with the variable name
    templar = FakeTemplar({'badvar': 'FAIL_UNDEFINED'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleUndefinedVariable as e:
        assert 'FAIL_UNDEFINED' in to_native(e)
        assert 'some_undefined_var' in to_native(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 8. other exceptions during templating are wrapped in AnsibleError
    templar = FakeTemplar({'badvar': 'FAIL_OTHER'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleError as e:
        assert "An unhandled exception occurred while templating" in to_native(e)
        assert "boom" in to_native(e)
    else:
        raise AssertionError("expected AnsibleError")

# Generated at 2026-10-25 10:58:44.879799
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    templar = pytest.importorskip("unittest.mock").MagicMock()
    templar.available_variables = {'hostvar': 'hv'}
    templar.template.side_effect = lambda v: v  # identity, so values pass through

    v = AnsibleJ2Vars(templar, {'range': range}, locals={'l_foo': 1, 'context': 'x'})

    # 1. None -> returns self, no copy
    assert v.add_locals(None) is v

    # 2. dict -> new instance, original untouched
    v2 = v.add_locals({'bar': 2})
    assert v2 is not v
    assert isinstance(v2, AnsibleJ2Vars)
    assert v2['bar'] == 2
    assert v2['foo'] == 1        # pre-existing locals carried over (l_ prefix stripped)
    assert 'bar' not in v        # source object not mutated

    # 3. templar vars and globals still resolve through the copy
    assert v2['hostvar'] == 'hv'
    assert v2['range'] is range
    assert 'bar' in v2 and 'hostvar' in v2 and 'range' in v2

    # 4. locals take precedence over templar vars of the same name
    templar.available_variables = {'foo': 'from_templar'}
    assert v2['foo'] == 1

    # 5. new locals shadow old locals, old copy unaffected
    v3 = v2.add_locals({'foo': 99})
    assert v3['foo'] == 99
    assert v2['foo'] == 1

    # 6. constructor filtering is applied again to locals passed via add_locals
    assert 'context' not in v.add_locals({'context': 'x'})
    assert v.add_locals({'l_baz': 3})['baz'] == 3

# Generated at 2026-10-25 10:59:03.001174
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:05.357085
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:07.772298
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:10.470458
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:12.889318
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:15.300444
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:17.714078
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:20.353583
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:22.768608
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:25.185896
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:33.099422
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:59:51.176366
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.common.text.converters import to_native
    from ansible.template import AnsibleJ2Vars

    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
            self.templarized = []

        def template(self, variable):
            self.templarized.append(variable)
            if isinstance(variable, str) and variable.startswith('FAIL_UNDEFINED'):
                raise AnsibleUndefinedVariable("'some_undefined_var' is undefined")
            if isinstance(variable, str) and variable.startswith('FAIL_OTHER'):
                raise Exception("boom")
            return 'templated:%s' % variable

    globals_dict = {'range': range, 'lookup': lambda *a, **kw: 'looked_up'}

    # 1. var found in available_variables gets templated
    templar = FakeTemplar({'foo': 'bar'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['foo'] == 'templated:bar'
    assert templar.templarized == ['bar']

    # 2. var found in locals is returned as-is, without templating
    j2vars = AnsibleJ2Vars(templar, globals_dict, locals={'localvar': 'raw_value'})
    assert j2vars['localvar'] == 'raw_value'
    assert templar.templarized == ['bar']

    # 3. var found only in globals is returned as-is, without templating
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['range'] is range

    # 4. the special variable 'vars' (a dict) is returned as-is
    special_vars = {'a': 1}
    templar = FakeTemplar({'vars': special_vars})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['vars'] is special_vars
    assert templar.templarized == []

    # 5. objects marked __UNSAFE__ are returned as-is
    class UnsafeStr(str):
        __UNSAFE__ = True

    unsafe = UnsafeStr('unsafe_string')
    templar = FakeTemplar({'unsafe_var': unsafe})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    assert j2vars['unsafe_var'] is unsafe
    assert templar.templarized == []

    # 6. undefined variable raises KeyError
    templar = FakeTemplar({})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['nope']
    except KeyError as e:
        assert to_native(e) == "'undefined variable: nope'"
    else:
        raise AssertionError("expected KeyError for undefined variable")

    # 7. AnsibleUndefinedVariable during templating is wrapped with the variable name
    templar = FakeTemplar({'badvar': 'FAIL_UNDEFINED'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleUndefinedVariable as e:
        assert 'FAIL_UNDEFINED' in to_native(e)
        assert 'some_undefined_var' in to_native(e)
    else:
        raise AssertionError("expected AnsibleUndefinedVariable")

    # 8. other exceptions during templating are wrapped in AnsibleError
    templar = FakeTemplar({'badvar': 'FAIL_OTHER'})
    j2vars = AnsibleJ2Vars(templar, globals_dict)
    try:
        j2vars['badvar']
    except AnsibleError as e:
        assert "An unhandled exception occurred while templating" in to_native(e)
        assert "boom" in to_native(e)
    else:
        raise AssertionError("expected AnsibleError")

# Generated at 2026-10-25 10:59:53.592035
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:56.009041
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:59:58.426066
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:00.840314
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:03.287139
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:05.971529
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:08.419618
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:10.805001
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:13.220526
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:15.635448
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:18.050251
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:20.465039
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:23.582731
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:26.002754
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:28.427573
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:30.843038
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:33.259189
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:35.673481
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:38.089242
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:40.505390
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:42.925625
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:45.358410
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:47.754691
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:50.170397
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:52.586298
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:55.003770
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:57.418588
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:00:59.920263
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:02.302891
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:04.717394
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:07.136212
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:09.553197
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:11.966977
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:14.381652
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:16.800465
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:19.211324
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:21.632088
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:24.048170
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:26.458888
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:28.889123
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:31.304576
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:33.722134
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:36.139038
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:38.553690
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:40.968254
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:43.383983
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:45.798458
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:48.214968
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:51.368269
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:53.781201
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:56.196266
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:01:58.611013
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:01.026671
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:03.444549
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:05.861761
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:08.274432
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:10.688426
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:13.102509
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:15.517205
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:17.933819
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:20.350115
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:22.763157
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:25.180928
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:27.591379
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:30.008875
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:32.426222
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:34.886526
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:37.297320
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:39.713907
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:42.127295
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:44.544201
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:46.960441
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:49.374218
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:51.788160
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:54.203495
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:56.618248
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:02:59.034895
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:01.449884
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:04.861300
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:07.274726
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:09.688357
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:12.102744
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:14.519155
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:16.934096
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:19.346186
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:21.764028
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:24.174795
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:26.588347
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:29.002151
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:31.416380
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:33.830229
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:36.244836
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:38.659268
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:41.074690
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:43.488970
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:45.903716
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:48.318942
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:50.736625
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:53.147899
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:55.563783
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:03:57.976554
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:00.391057
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:02.806929
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:05.223120
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:07.636284
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:10.050954
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:12.464045
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:14.879534
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:20.426520
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:22.841918
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:25.289097
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:27.670187
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:30.084388
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:32.499216
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:34.944960
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:04:37.356136
# Unit test for constructor of class AnsibleJ2Vars