

# Generated at 2026-10-25 11:52:17.425153
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:22.222164
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 11:52:25.049843
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:27.494199
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:29.881875
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:32.298782
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:34.933118
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:37.349024
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:39.762211
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:42.177874
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:44.640530
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:47.032141
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:49.446327
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:51.860048
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:54.272743
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:56.683637
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:52:59.096281
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:01.511175
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:03.925802
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:06.339688
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:08.755305
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:11.173108
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:13.585831
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:15.997618
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:18.411862
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:20.828058
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:23.745013
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

# Generated at 2026-10-25 11:53:47.102074
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

# Generated at 2026-10-25 11:53:50.019700
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:52.434702
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:55.066063
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:57.482799
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:53:59.898174
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:02.312283
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:04.732616
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:07.146275
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:09.562758
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:11.982701
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:14.944479
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:17.357803
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:19.771823
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:22.189201
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:24.606856
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:27.017706
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:29.430691
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:31.848795
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:34.261580
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:36.676601
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:39.089667
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:41.504868
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:43.922273
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:46.332588
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:48.750708
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:51.167009
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:53.576892
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:55.993861
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:54:58.405282
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:00.822012
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:03.235753
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:05.649996
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:08.064889
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:10.479392
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:12.911924
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:15.326417
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:17.741972
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:20.157914
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:22.572141
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:24.986981
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:27.400948
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:29.820747
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:32.233088
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:34.646822
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:37.062239
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:39.476544
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:41.894483
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:44.308992
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:46.722645
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:49.136707
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:51.551145
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:53.966358
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:56.381383
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:55:58.795563
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:01.357868
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:03.641693
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:06.067872
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:08.472840
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:10.886871
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:13.302414
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:15.715865
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:18.129385
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:20.544631
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:22.958364
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:25.372713
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:27.785252
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:30.198552
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:32.612526
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:35.028091
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:37.446147
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:39.862169
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:42.272664
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:44.689149
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:47.100634
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:49.515018
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:51.931539
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:54.344679
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:56.759135
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:56:59.173073
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:01.586348
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:03.998741
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:06.413820
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:08.827906
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:11.242125
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:13.655480
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:16.069297
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:18.481797
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:20.896110
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:23.310743
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:25.724507
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:28.139130
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:30.554083
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:32.967296
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:35.380694
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:37.795298
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:40.209686
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:42.624416
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:45.041365
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:47.451316
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:49.866222
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:52.278860
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:54.693445
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:57:59.298904
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:01.713821
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:04.127792
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:06.540254
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:08.953628
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:11.367514
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:13.840124
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:16.226079
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:18.638483
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:21.053873
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:23.465603
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:25.878022
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:28.291523
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:30.706810
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:58:32.311431
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 11:58:35.278514
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

# Generated at 2026-10-25 11:58:38.359269
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

# Generated at 2026-10-25 11:58:39.779595
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 11:58:57.668198
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

# Generated at 2026-10-25 11:59:15.729696
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

# Generated at 2026-10-25 11:59:29.656533
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:59:32.079780
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:59:56.204067
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 11:59:57.684440
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 11:59:59.210867
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 12:00:17.252393
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

# Generated at 2026-10-25 12:00:19.670118
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:22.085263
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:24.498132
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:26.912420
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:29.325287
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:31.739953
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:34.198751
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:36.613489
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:39.027972
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:41.441602
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:43.855487
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:46.268236
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:48.682433
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:51.335724
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:00:54.404594
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:01:28.009689
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

# Generated at 2026-10-25 12:01:40.156965
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 12:01:42.800724
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 12:01:45.218270
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 12:01:47.631066
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:01:50.286964
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:01:52.998461
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:02:11.001122
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

# Generated at 2026-10-25 12:02:13.734613
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

# Generated at 2026-10-25 12:02:15.091143
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

# Generated at 2026-10-25 12:02:17.641808
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:02:20.304277
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 12:02:22.837598
# Unit test for method __getitem__ of class AnsibleJ2Vars