

# Generated at 2026-10-24 20:54:03.345368
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:54:13.625234
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():obj = AnsibleJ2Vars.__new__(AnsibleJ2Vars)
obj._locals = {"local_key": "local"}
obj._templar = type("Templar", (), {"available_variables": {"available_key": "available"}})()
obj._globals = {"global_key": "global"}

assert obj.__contains__("local_key") is True
assert obj.__contains__("available_key") is True
assert obj.__contains__("global_key") is True
assert obj.__contains__("missing_key") is False

# Generated at 2026-10-24 20:54:16.269672
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:54:18.858516
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:54:21.275410
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:54:23.881085
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:54:26.297193
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:54:36.346116
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:54:42.089914
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:54:44.824104
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:54:46.147173
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    templar = MagicMock()

    # Empty: 0 distinct keys
    templar.available_variables = {}
    assert len(AnsibleJ2Vars(templar, globals={})) == 0

    # Overlapping keys counted once:
    # available={host, shared, only_var}, globals={shared, global_only},
    # locals={shared, local_only} -> 5 distinct keys
    templar.available_variables = {'host': 'web1', 'shared': 1, 'only_var': 2}
    j2vars = AnsibleJ2Vars(
        templar,
        globals={'shared': 3, 'global_only': 4},
        locals={'shared': 5, 'local_only': 6},
    )
    assert len(j2vars) == 5

    # Locals normalization affects length: 'l_foo' -> 'foo', 'context' excluded
    templar.available_variables = {'host': 'web1'}
    j2vars = AnsibleJ2Vars(
        templar,
        globals={},
        locals={'l_foo': 1, 'context': 2},
    )
    assert len(j2vars) == 2

# Generated at 2026-10-24 20:54:47.620306
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from unittest.mock import MagicMock

    mock_templar = MagicMock()
    mock_templar.available_variables = {}
    test_globals = {'range': range, 'global_var': 'global_value'}

    # 1. locals=None -> empty _locals, stores templar/globals
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=None)
    assert obj._templar is mock_templar
    assert obj._globals is test_globals
    assert obj._locals == {}

    # 2. locals not a dict -> ignored
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals="not-a-dict")
    assert obj._locals == {}
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=['a', 'b'])
    assert obj._locals == {}

    # 3. normal locals are copied
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals={'foo': 'bar', 'num': 42})
    assert obj._locals == {'foo': 'bar', 'num': 42}

    # 4. 'l_' prefix is stripped (jinja2 loop locals)
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'l_foo': 'stripped', 'bar': 'kept'}
    )
    assert obj._locals == {'foo': 'stripped', 'bar': 'kept'}

    # 5. jinja2 internal keys are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'context': 'c',
            'environment': 'e',
            'template': 't',
            'ok': 'kept',
        }
    )
    assert obj._locals == {'ok': 'kept'}

    # 6. jinja2.utils.missing values are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'present': 1, 'absent': missing, 'l_skipped': missing}
    )
    assert obj._locals == {'present': 1}

    # 7. combined case
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'l_x': 1,
            'y': 2,
            'context': 3,
            'z': missing,
        }
    )
    assert obj._locals == {'x': 1, 'y': 2}

# Generated at 2026-10-24 20:54:48.947786
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:01.031231
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from types import SimpleNamespace


# Generated at 2026-10-24 20:55:03.452865
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:05.869122
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:08.286866
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:10.706028
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:13.277939
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:15.694304
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:18.109597
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:20.529077
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:23.120785
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:25.540864
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:27.960089
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:30.377091
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:33.131227
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:55:35.841728
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:55:38.605588
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:55:40.052304
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from unittest.mock import MagicMock

    mock_templar = MagicMock()
    mock_templar.available_variables = {}
    test_globals = {'range': range, 'global_var': 'global_value'}

    # 1. locals=None -> empty _locals, stores templar/globals
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=None)
    assert obj._templar is mock_templar
    assert obj._globals is test_globals
    assert obj._locals == {}

    # 2. locals not a dict -> ignored
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals="not-a-dict")
    assert obj._locals == {}
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=['a', 'b'])
    assert obj._locals == {}

    # 3. normal locals are copied
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals={'foo': 'bar', 'num': 42})
    assert obj._locals == {'foo': 'bar', 'num': 42}

    # 4. 'l_' prefix is stripped (jinja2 loop locals)
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'l_foo': 'stripped', 'bar': 'kept'}
    )
    assert obj._locals == {'foo': 'stripped', 'bar': 'kept'}

    # 5. jinja2 internal keys are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'context': 'c',
            'environment': 'e',
            'template': 't',
            'ok': 'kept',
        }
    )
    assert obj._locals == {'ok': 'kept'}

    # 6. jinja2.utils.missing values are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'present': 1, 'absent': missing, 'l_skipped': missing}
    )
    assert obj._locals == {'present': 1}

    # 7. combined case
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'l_x': 1,
            'y': 2,
            'context': 3,
            'z': missing,
        }
    )
    assert obj._locals == {'x': 1, 'y': 2}

# Generated at 2026-10-24 20:55:43.222168
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:45.640833
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:56.333290
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:55:59.083238
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:56:00.411320
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:02.840889
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:05.252280
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:07.672248
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:10.094154
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:12.661746
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:15.078026
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:17.496362
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:19.913850
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:22.329693
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:24.748625
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:27.168284
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:29.585030
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:32.000805
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:34.418394
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:36.837395
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:39.255709
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:41.672025
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:44.088161
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:46.502699
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:48.919086
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:51.337014
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:53.750497
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:56.166045
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:56:58.581186
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:00.999377
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:03.415378
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:06.146453
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:57:08.930426
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:57:10.366266
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from unittest.mock import MagicMock

    mock_templar = MagicMock()
    mock_templar.available_variables = {}
    test_globals = {'range': range, 'global_var': 'global_value'}

    # 1. locals=None -> empty _locals, stores templar/globals
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=None)
    assert obj._templar is mock_templar
    assert obj._globals is test_globals
    assert obj._locals == {}

    # 2. locals not a dict -> ignored
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals="not-a-dict")
    assert obj._locals == {}
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=['a', 'b'])
    assert obj._locals == {}

    # 3. normal locals are copied
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals={'foo': 'bar', 'num': 42})
    assert obj._locals == {'foo': 'bar', 'num': 42}

    # 4. 'l_' prefix is stripped (jinja2 loop locals)
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'l_foo': 'stripped', 'bar': 'kept'}
    )
    assert obj._locals == {'foo': 'stripped', 'bar': 'kept'}

    # 5. jinja2 internal keys are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'context': 'c',
            'environment': 'e',
            'template': 't',
            'ok': 'kept',
        }
    )
    assert obj._locals == {'ok': 'kept'}

    # 6. jinja2.utils.missing values are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'present': 1, 'absent': missing, 'l_skipped': missing}
    )
    assert obj._locals == {'present': 1}

    # 7. combined case
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'l_x': 1,
            'y': 2,
            'context': 3,
            'z': missing,
        }
    )
    assert obj._locals == {'x': 1, 'y': 2}

# Generated at 2026-10-24 20:57:13.141670
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:57:15.885682
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:57:18.659275
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:57:21.187949
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:23.708067
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:26.127266
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:28.643735
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:31.061765
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:33.482307
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:35.899625
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:38.322247
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:40.746222
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:43.592608
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:57:44.923219
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:57:56.619244
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from types import SimpleNamespace


# Generated at 2026-10-24 20:57:57.996420
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from unittest.mock import MagicMock

    mock_templar = MagicMock()
    mock_templar.available_variables = {}
    test_globals = {'range': range, 'global_var': 'global_value'}

    # 1. locals=None -> empty _locals, stores templar/globals
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=None)
    assert obj._templar is mock_templar
    assert obj._globals is test_globals
    assert obj._locals == {}

    # 2. locals not a dict -> ignored
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals="not-a-dict")
    assert obj._locals == {}
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=['a', 'b'])
    assert obj._locals == {}

    # 3. normal locals are copied
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals={'foo': 'bar', 'num': 42})
    assert obj._locals == {'foo': 'bar', 'num': 42}

    # 4. 'l_' prefix is stripped (jinja2 loop locals)
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'l_foo': 'stripped', 'bar': 'kept'}
    )
    assert obj._locals == {'foo': 'stripped', 'bar': 'kept'}

    # 5. jinja2 internal keys are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'context': 'c',
            'environment': 'e',
            'template': 't',
            'ok': 'kept',
        }
    )
    assert obj._locals == {'ok': 'kept'}

    # 6. jinja2.utils.missing values are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'present': 1, 'absent': missing, 'l_skipped': missing}
    )
    assert obj._locals == {'present': 1}

    # 7. combined case
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'l_x': 1,
            'y': 2,
            'context': 3,
            'z': missing,
        }
    )
    assert obj._locals == {'x': 1, 'y': 2}

# Generated at 2026-10-24 20:58:00.853368
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:58:03.717465
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:58:06.783842
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:58:08.111496
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:24.606730
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:27.029395
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:29.618750
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:32.035958
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:34.452974
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:36.869543
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:39.286377
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:41.706002
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:58:44.487221
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:58:47.342027
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:58:50.054374
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:58:51.408461
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from unittest.mock import MagicMock

    mock_templar = MagicMock()
    mock_templar.available_variables = {}
    test_globals = {'range': range, 'global_var': 'global_value'}

    # 1. locals=None -> empty _locals, stores templar/globals
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=None)
    assert obj._templar is mock_templar
    assert obj._globals is test_globals
    assert obj._locals == {}

    # 2. locals not a dict -> ignored
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals="not-a-dict")
    assert obj._locals == {}
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=['a', 'b'])
    assert obj._locals == {}

    # 3. normal locals are copied
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals={'foo': 'bar', 'num': 42})
    assert obj._locals == {'foo': 'bar', 'num': 42}

    # 4. 'l_' prefix is stripped (jinja2 loop locals)
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'l_foo': 'stripped', 'bar': 'kept'}
    )
    assert obj._locals == {'foo': 'stripped', 'bar': 'kept'}

    # 5. jinja2 internal keys are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'context': 'c',
            'environment': 'e',
            'template': 't',
            'ok': 'kept',
        }
    )
    assert obj._locals == {'ok': 'kept'}

    # 6. jinja2.utils.missing values are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'present': 1, 'absent': missing, 'l_skipped': missing}
    )
    assert obj._locals == {'present': 1}

    # 7. combined case
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'l_x': 1,
            'y': 2,
            'context': 3,
            'z': missing,
        }
    )
    assert obj._locals == {'x': 1, 'y': 2}

# Generated at 2026-10-24 20:58:52.770188
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from unittest.mock import MagicMock

    mock_templar = MagicMock()
    mock_templar.available_variables = {}
    test_globals = {'range': range, 'global_var': 'global_value'}

    # 1. locals=None -> empty _locals, stores templar/globals
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=None)
    assert obj._templar is mock_templar
    assert obj._globals is test_globals
    assert obj._locals == {}

    # 2. locals not a dict -> ignored
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals="not-a-dict")
    assert obj._locals == {}
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=['a', 'b'])
    assert obj._locals == {}

    # 3. normal locals are copied
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals={'foo': 'bar', 'num': 42})
    assert obj._locals == {'foo': 'bar', 'num': 42}

    # 4. 'l_' prefix is stripped (jinja2 loop locals)
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'l_foo': 'stripped', 'bar': 'kept'}
    )
    assert obj._locals == {'foo': 'stripped', 'bar': 'kept'}

    # 5. jinja2 internal keys are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'context': 'c',
            'environment': 'e',
            'template': 't',
            'ok': 'kept',
        }
    )
    assert obj._locals == {'ok': 'kept'}

    # 6. jinja2.utils.missing values are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'present': 1, 'absent': missing, 'l_skipped': missing}
    )
    assert obj._locals == {'present': 1}

    # 7. combined case
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'l_x': 1,
            'y': 2,
            'context': 3,
            'z': missing,
        }
    )
    assert obj._locals == {'x': 1, 'y': 2}

# Generated at 2026-10-24 20:58:55.637031
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:58:58.381365
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:59:01.152831
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars

    class FakeTemplar(object):
        def __init__(self, available_variables=None):
            self.available_variables = available_variables or {}
            self.template_calls = []

        def template(self, value):
            self.template_calls.append(value)
            if value == '{{ fail_undefined }}':
                raise AnsibleUndefinedVariable("'fail_undefined' is undefined")
            if value == '{{ fail_other }}':
                raise Exception("boom")
            return "templated:%s" % value

    class FakeHostVars(object):
        pass

    # Setup templar with a mix of variables
    templar = FakeTemplar({
        'plain': 'hello',
        'needs_templating': '{{ some_var }}',
        'vars': {'a': 1},
        'hostvars': FakeHostVars(),
    })

    globals_dict = {'range': range, 'lookup': lambda *args, **kwargs: 'global_lookup_result'}
    locals_dict = {'local_var': 'local_value'}

    j2vars = AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

    # 1. Local variable is returned as-is
    assert j2vars['local_var'] == 'local_value'

    # 2. Global variable is returned as-is
    assert j2vars['range'] is range

    # 3. Available variable that needs templating gets templated
    assert j2vars['needs_templating'] == 'templated:{{ some_var }}'
    assert templar.template_calls == ['{{ some_var }}']

    # 4. Special 'vars' dict is returned as-is without templating
    special_vars = j2vars['vars']
    assert special_vars == {'a': 1}
    # templating should not have been invoked again for 'vars'
    assert templar.template_calls == ['{{ some_var }}']

    # 5. HostVars-like object is returned as-is
    hv = j2vars['hostvars']
    assert isinstance(hv, FakeHostVars)

    # 6. Missing variable raises KeyError
    try:
        j2vars['nonexistent']
    except KeyError as e:
        assert 'undefined variable: nonexistent' in str(e)
    else:
        raise AssertionError("Expected KeyError for 'nonexistent'")

    # 7. AnsibleUndefinedVariable during templating is re-raised with context
    templar.available_variables['fail_undefined'] = '{{ fail_undefined }}'
    try:
        j2vars['fail_undefined']
    except AnsibleUndefinedVariable as e:
        assert 'fail_undefined' in str(e)
    else:
        raise AssertionError("Expected AnsibleUndefinedVariable for 'fail_undefined'")

    # 8. Generic exception during templating is wrapped in AnsibleError
    templar.available_variables['fail_other'] = '{{ fail_other }}'
    try:
        j2vars['fail_other']
    except AnsibleError as e:
        assert 'unhandled exception' in str(e)
        assert 'boom' in str(e)
    else:
        raise AssertionError("Expected AnsibleError for 'fail_other'")

# Generated at 2026-10-24 20:59:02.607328
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from unittest.mock import MagicMock

    mock_templar = MagicMock()
    mock_templar.available_variables = {}
    test_globals = {'range': range, 'global_var': 'global_value'}

    # 1. locals=None -> empty _locals, stores templar/globals
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=None)
    assert obj._templar is mock_templar
    assert obj._globals is test_globals
    assert obj._locals == {}

    # 2. locals not a dict -> ignored
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals="not-a-dict")
    assert obj._locals == {}
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals=['a', 'b'])
    assert obj._locals == {}

    # 3. normal locals are copied
    obj = AnsibleJ2Vars(mock_templar, test_globals, locals={'foo': 'bar', 'num': 42})
    assert obj._locals == {'foo': 'bar', 'num': 42}

    # 4. 'l_' prefix is stripped (jinja2 loop locals)
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'l_foo': 'stripped', 'bar': 'kept'}
    )
    assert obj._locals == {'foo': 'stripped', 'bar': 'kept'}

    # 5. jinja2 internal keys are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'context': 'c',
            'environment': 'e',
            'template': 't',
            'ok': 'kept',
        }
    )
    assert obj._locals == {'ok': 'kept'}

    # 6. jinja2.utils.missing values are filtered out
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={'present': 1, 'absent': missing, 'l_skipped': missing}
    )
    assert obj._locals == {'present': 1}

    # 7. combined case
    obj = AnsibleJ2Vars(
        mock_templar, test_globals,
        locals={
            'l_x': 1,
            'y': 2,
            'context': 3,
            'z': missing,
        }
    )
    assert obj._locals == {'x': 1, 'y': 2}

# Generated at 2026-10-24 20:59:05.274871
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:07.693414
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:10.111735
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:12.529783
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:14.947881
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:17.368761
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:21.868994
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:24.287038
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:26.706610
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:29.122598
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:31.542909
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:33.959052
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:36.376802
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:38.793222
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:41.211727
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:43.630218
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:46.047882
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:48.464242
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:50.881825
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:53.299451
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:55.715517
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:59:58.131387
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:00.550349
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:02.967693
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:05.382621
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:07.803397
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:10.219937
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:11.595254
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:32.915228
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:53.805123
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():templar = type("Templar", (), {"available_variables": {"templar_var": 1}})()

# Generated at 2026-10-24 21:00:56.563464
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:00:59.105286
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:01.524544
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:04.217414
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:06.631469
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:09.051246
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:12.420209
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:26.353993
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from types import SimpleNamespace

# Generated at 2026-10-24 21:01:27.796217
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:44.290386
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:46.811005
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:49.333087
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:51.863333
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:54.277974
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:56.694624
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:01:59.115263
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:01.533484
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:03.950491
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:06.369404
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:08.785754
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:11.202121
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:13.621156
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:16.040642
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:18.458236
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:20.873387
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:23.292765
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:25.710867
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:28.127529
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:30.576292
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:32.962891
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:35.379553
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:37.795035
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:40.211917
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:42.628076
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:45.046443
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:52.563978
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:54.982050
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:57.398505
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:02:59.814994
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:02.232253
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:04.648819
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:07.067133
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:09.483250
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:11.903546
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:14.318375
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:16.735606
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:19.154002
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:21.570960
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:23.986368
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:26.402754
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:28.854199
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:31.244384
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:33.660650
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:36.077886
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:38.495166
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:40.910956
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:43.328295
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:45.743573
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:48.161693
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:50.579984
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:53.000217
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:55.420084
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:03:57.841932
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:04:00.264518
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:04:02.685486
# Unit test for constructor of class AnsibleJ2Vars