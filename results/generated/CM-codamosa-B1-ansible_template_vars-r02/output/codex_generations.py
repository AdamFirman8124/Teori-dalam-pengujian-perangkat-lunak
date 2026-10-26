

# Generated at 2026-10-25 08:33:03.425633
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

# Generated at 2026-10-25 08:33:17.610429
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

# Generated at 2026-10-25 08:33:20.041953
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:22.726731
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:25.145743
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:27.561448
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:30.096994
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:32.512195
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:34.930436
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:37.347026
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:39.774262
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:42.189444
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:44.606708
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:33:58.637653
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:10.602755
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {'some_var': 'value'}

    globals_dict = {'range': range, 'lookup': None}

    # locals with 'l_' prefix -> stripped; missing -> dropped; reserved names -> dropped
    locals_dict = {
        'l__local_var': 'lvalue',
        'l__missing_var': missing,          # must be excluded
        'l__context': 'should-be-kept',     # 'context' checked AFTER stripping 'l_'
        'context': 'dropped',               # reserved, no prefix -> dropped
        'environment': 'dropped',
        'template': 'dropped',
        'plain': 'kept',                    # no prefix, not reserved -> kept
        'l__some_var': 'local-overrides',   # local shadows templar var
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Constructor behavior
    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict
    assert j2vars._locals == {
        '_local_var': 'lvalue',
        '_missing_var': 'lvalue' if False else j2vars._locals.get('_missing_var'),
        '_context': 'should-be-kept',
        'plain': 'kept',
        'some_var': 'local-overrides',
    } - {'_missing_var'}  # see simplified assertions below

    # Simpler, precise assertions:
    assert '_missing_var' not in j2vars._locals      # missing sentinel dropped
    assert 'context' not in j2vars._locals           # reserved name dropped
    assert 'environment' not in j2vars._locals
    assert 'template' not in j2vars._locals
    assert j2vars._locals['_local_var'] == 'lvalue'  # 'l_' prefix stripped
    assert j2vars._locals['plain'] == 'kept'

    # __contains__
    assert 'some_var' in j2vars
    assert 'range' in j2vars
    assert '_local_var' in j2vars
    assert 'nope' not in j2vars

    # __getitem__ / __len__ / __iter__
    assert j2vars['range'] is range
    assert j2vars['_local_var'] == 'lvalue'
    assert len(j2vars) == len(set(j2vars))           # no duplicate keys
    assert set(j2vars) == {'some_var', 'range', '_local_var', 'plain', 'some_var'} - {'some_var'} | {'some_var'}


def test_AnsibleJ2Vars_locals_none_returns_self():
    templar = MagicMock()
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars.add_locals(None) is j2vars


def test_AnsibleJ2Vars_add_locals_copies():
    templar = MagicMock()
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {}, locals={'a': 1})
    new = j2vars.add_locals({'b': 2})
    assert new is not j2vars
    assert new._locals == {'a': 1, 'b': 2}
    assert j2vars._locals == {'a': 1}                # original untouched

# Generated at 2026-10-25 08:34:12.847546
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:15.266183
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:17.682722
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:20.102779
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:22.520737
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:25.075288
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:27.393931
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:29.823792
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:32.241017
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:34.659229
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:37.180120
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:39.597786
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:42.014577
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:44.432780
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:47.038194
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:49.382357
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:51.797817
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:54.216545
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:56.635097
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:34:59.055138
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:01.468947
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:03.885761
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:06.399092
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:08.739435
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:11.453802
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

# Generated at 2026-10-25 08:35:12.985840
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

# Generated at 2026-10-25 08:35:14.322194
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

# Generated at 2026-10-25 08:35:15.665596
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {'some_var': 'value'}

    globals_dict = {'range': range, 'lookup': None}

    # locals with 'l_' prefix -> stripped; missing -> dropped; reserved names -> dropped
    locals_dict = {
        'l__local_var': 'lvalue',
        'l__missing_var': missing,          # must be excluded
        'l__context': 'should-be-kept',     # 'context' checked AFTER stripping 'l_'
        'context': 'dropped',               # reserved, no prefix -> dropped
        'environment': 'dropped',
        'template': 'dropped',
        'plain': 'kept',                    # no prefix, not reserved -> kept
        'l__some_var': 'local-overrides',   # local shadows templar var
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Constructor behavior
    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict
    assert j2vars._locals == {
        '_local_var': 'lvalue',
        '_missing_var': 'lvalue' if False else j2vars._locals.get('_missing_var'),
        '_context': 'should-be-kept',
        'plain': 'kept',
        'some_var': 'local-overrides',
    } - {'_missing_var'}  # see simplified assertions below

    # Simpler, precise assertions:
    assert '_missing_var' not in j2vars._locals      # missing sentinel dropped
    assert 'context' not in j2vars._locals           # reserved name dropped
    assert 'environment' not in j2vars._locals
    assert 'template' not in j2vars._locals
    assert j2vars._locals['_local_var'] == 'lvalue'  # 'l_' prefix stripped
    assert j2vars._locals['plain'] == 'kept'

    # __contains__
    assert 'some_var' in j2vars
    assert 'range' in j2vars
    assert '_local_var' in j2vars
    assert 'nope' not in j2vars

    # __getitem__ / __len__ / __iter__
    assert j2vars['range'] is range
    assert j2vars['_local_var'] == 'lvalue'
    assert len(j2vars) == len(set(j2vars))           # no duplicate keys
    assert set(j2vars) == {'some_var', 'range', '_local_var', 'plain', 'some_var'} - {'some_var'} | {'some_var'}


def test_AnsibleJ2Vars_locals_none_returns_self():
    templar = MagicMock()
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars.add_locals(None) is j2vars


def test_AnsibleJ2Vars_add_locals_copies():
    templar = MagicMock()
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {}, locals={'a': 1})
    new = j2vars.add_locals({'b': 2})
    assert new is not j2vars
    assert new._locals == {'a': 1, 'b': 2}
    assert j2vars._locals == {'a': 1}                # original untouched

# Generated at 2026-10-25 08:35:17.018522
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {'some_var': 'value'}

    globals_dict = {'range': range, 'lookup': None}

    # locals with 'l_' prefix -> stripped; missing -> dropped; reserved names -> dropped
    locals_dict = {
        'l__local_var': 'lvalue',
        'l__missing_var': missing,          # must be excluded
        'l__context': 'should-be-kept',     # 'context' checked AFTER stripping 'l_'
        'context': 'dropped',               # reserved, no prefix -> dropped
        'environment': 'dropped',
        'template': 'dropped',
        'plain': 'kept',                    # no prefix, not reserved -> kept
        'l__some_var': 'local-overrides',   # local shadows templar var
    }

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # Constructor behavior
    assert j2vars._templar is templar
    assert j2vars._globals is globals_dict
    assert j2vars._locals == {
        '_local_var': 'lvalue',
        '_missing_var': 'lvalue' if False else j2vars._locals.get('_missing_var'),
        '_context': 'should-be-kept',
        'plain': 'kept',
        'some_var': 'local-overrides',
    } - {'_missing_var'}  # see simplified assertions below

    # Simpler, precise assertions:
    assert '_missing_var' not in j2vars._locals      # missing sentinel dropped
    assert 'context' not in j2vars._locals           # reserved name dropped
    assert 'environment' not in j2vars._locals
    assert 'template' not in j2vars._locals
    assert j2vars._locals['_local_var'] == 'lvalue'  # 'l_' prefix stripped
    assert j2vars._locals['plain'] == 'kept'

    # __contains__
    assert 'some_var' in j2vars
    assert 'range' in j2vars
    assert '_local_var' in j2vars
    assert 'nope' not in j2vars

    # __getitem__ / __len__ / __iter__
    assert j2vars['range'] is range
    assert j2vars['_local_var'] == 'lvalue'
    assert len(j2vars) == len(set(j2vars))           # no duplicate keys
    assert set(j2vars) == {'some_var', 'range', '_local_var', 'plain', 'some_var'} - {'some_var'} | {'some_var'}


def test_AnsibleJ2Vars_locals_none_returns_self():
    templar = MagicMock()
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars.add_locals(None) is j2vars


def test_AnsibleJ2Vars_add_locals_copies():
    templar = MagicMock()
    templar.available_variables = {}
    j2vars = AnsibleJ2Vars(templar, {}, locals={'a': 1})
    new = j2vars.add_locals({'b': 2})
    assert new is not j2vars
    assert new._locals == {'a': 1, 'b': 2}
    assert j2vars._locals == {'a': 1}                # original untouched

# Generated at 2026-10-25 08:35:18.463335
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

# Generated at 2026-10-25 08:35:21.463135
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

# Generated at 2026-10-25 08:35:24.213019
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

# Generated at 2026-10-25 08:35:25.548113
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

# Generated at 2026-10-25 08:35:28.150655
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:30.587967
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:33.004092
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:35.616054
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:38.035357
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:40.576326
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:42.944369
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:45.358439
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:47.774875
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:50.191983
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:52.613359
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:55.030106
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:57.461125
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:35:59.875552
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:02.292569
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:04.708888
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:07.130821
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:09.547862
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:12.041408
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:14.407243
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:16.822652
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:19.239470
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:21.685823
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:24.103194
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:26.524094
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:28.939265
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:31.357045
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:33.839138
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:36.255026
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:38.671772
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:41.088951
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:43.508061
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:45.922581
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:48.507313
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:50.925266
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:53.497550
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:55.775077
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:36:58.669545
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:04.648306
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:06.142816
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

# Generated at 2026-10-25 08:37:07.543924
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

# Generated at 2026-10-25 08:37:10.371737
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

# Generated at 2026-10-25 08:37:13.103982
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

# Generated at 2026-10-25 08:37:15.697571
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:18.115674
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:20.648013
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:23.066378
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:25.647821
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:28.070819
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:30.480212
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:32.897691
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:35.313268
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:37.731109
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:40.146008
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:42.564208
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:45.577633
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:47.993640
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:50.409296
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:52.825617
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:55.242877
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:37:57.661058
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:00.074810
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:02.490617
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:04.907456
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:07.325546
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:09.745531
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:12.159403
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:14.577782
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:16.993090
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:19.409219
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:21.824283
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:24.240826
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:26.660592
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:29.073128
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:31.492234
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:33.914510
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:36.330109
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:38.747838
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:41.164320
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:43.580774
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:45.999522
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:48.419655
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:50.839739
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:53.255775
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:38:55.673698
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:00.517420
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:02.932578
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:05.348435
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:07.767810
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:10.184857
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:12.604633
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:15.019822
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:17.440360
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:19.855704
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:22.274967
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:24.690307
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:27.107106
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:29.521078
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:31.982024
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:34.401184
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:36.815603
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:39.238273
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:41.656438
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:44.071182
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:46.489112
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:48.906410
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:51.325719
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:39:53.743468
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:21.835225
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():from jinja2.utils import missing

# Generated at 2026-10-25 08:40:24.436647
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:26.852846
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:29.270860
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:31.841429
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:34.463351
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:36.878118
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:40.871178
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:43.291100
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:45.706619
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:48.125940
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:50.541807
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:52.960525
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:55.376001
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:40:57.791263
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:00.207076
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:02.625735
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:05.042496
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:07.457839
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:09.873187
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:12.289477
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:14.707409
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:17.123749
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:19.541199
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:21.957004
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:24.377620
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:26.792097
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:29.208721
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:31.626092
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:34.041415
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:36.458883
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:38.875583
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:41.292141
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:43.708914
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:46.128286
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:49.074301
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:41:52.175089
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:04.928744
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

# Generated at 2026-10-25 08:42:07.732229
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

# Generated at 2026-10-25 08:42:09.149557
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

# Generated at 2026-10-25 08:42:10.787049
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

# Generated at 2026-10-25 08:42:13.362652
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:15.928771
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:18.346814
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:21.017991
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:23.433677
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:25.850315
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:28.269893
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:30.689625
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:33.107472
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:35.523793
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:37.940420
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:40.358186
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:42.801424
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:45.214178
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:47.632540
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:50.049859
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:52.466675
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 08:42:54.886187
# Unit test for method __contains__ of class AnsibleJ2Vars