

# Generated at 2026-10-25 10:18:44.604614
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:18:47.020645
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:04.873845
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:22.975596
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

# Generated at 2026-10-25 10:19:41.226023
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:43.641903
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:46.055651
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:48.638504
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:51.052644
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:53.467077
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:55.882759
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:19:57.405387
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:20:27.820053
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

# Generated at 2026-10-25 10:21:00.592161
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

# Generated at 2026-10-25 10:21:02.020370
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:21:23.320611
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

# Generated at 2026-10-25 10:21:42.781533
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:21:45.544125
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:21:47.959338
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:21:50.373186
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:21:52.787678
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:21:55.201195
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:21:57.616848
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:22:00.031913
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:22:02.447470
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:22:04.860380
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:22:06.286891
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:22:07.713625
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:22:09.200788
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:22:27.161347
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

# Generated at 2026-10-25 10:22:58.962932
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

# Generated at 2026-10-25 10:23:01.382351
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:23:03.796787
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:23:06.211339
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:23:08.624063
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:23:11.040299
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:23:29.788055
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:23:31.219791
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:23:32.656896
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:23:41.987286
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

# Generated at 2026-10-25 10:23:43.516715
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:23:44.807945
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:23:47.616184
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

# Generated at 2026-10-25 10:23:52.931619
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

# Generated at 2026-10-25 10:23:55.574679
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:23:58.210851
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:00.624350
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:03.040770
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:05.454248
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:07.873482
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:10.290473
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:12.705460
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:15.118571
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:17.532616
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:19.964484
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:22.376115
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:24.794647
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:27.207424
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:29.621575
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:32.036341
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:34.453393
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:36.870260
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:39.289607
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:24:40.850603
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:24:42.284913
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:24:46.179098
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

# Generated at 2026-10-25 10:24:48.891560
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

# Generated at 2026-10-25 10:25:06.861451
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

# Generated at 2026-10-25 10:25:16.354567
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

# Generated at 2026-10-25 10:25:18.947861
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:21.494934
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:23.910181
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:26.327406
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:28.741001
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:31.154245
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:33.572961
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:35.984789
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:38.399405
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:40.812473
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:43.225986
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:25:45.843542
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:25:48.743608
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

# Generated at 2026-10-25 10:26:11.987809
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

# Generated at 2026-10-25 10:26:36.789828
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

# Generated at 2026-10-25 10:26:39.362222
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:26:41.774600
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:26:44.216473
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:26:46.643514
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:26:49.054189
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:26:50.496201
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:26:54.276534
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:26:55.712435
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:27:00.324555
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

# Generated at 2026-10-25 10:27:19.982947
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

# Generated at 2026-10-25 10:27:39.438090
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

# Generated at 2026-10-25 10:27:41.855147
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:27:44.272311
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:27:46.685374
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:27:49.132256
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:27:51.768738
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:27:53.162399
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:28:16.308403
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

# Generated at 2026-10-25 10:28:38.524836
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