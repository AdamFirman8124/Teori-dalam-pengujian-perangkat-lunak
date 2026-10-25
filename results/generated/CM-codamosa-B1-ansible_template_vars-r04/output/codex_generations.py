

# Generated at 2026-10-24 21:09:24.190271
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:26.607098
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:29.023677
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:31.438322
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:33.853006
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:36.269947
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:38.694018
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:41.109334
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:43.524374
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:45.940899
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:48.357796
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:50.776321
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:53.191002
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:55.608576
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:09:58.025804
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:00.441911
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:02.862946
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:05.278324
# Unit test for method __len__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:07.694753
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:10.111420
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:12.528746
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:14.947582
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:17.363682
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:26.015309
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:10:28.709828
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

# Generated at 2026-10-24 21:10:37.595555
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    templar = object()
    globals_ = {'global_var': 'global_value'}
    original = AnsibleJ2Vars(
        templar,
        globals_,
        locals={'existing': 'original'},
    )

    # No additional locals should return the existing proxy.
    assert original.add_locals(None) is original

    result = original.add_locals({
        'existing': 'overridden',
        'new_var': 'new_value',
    })

    # A new proxy is returned without mutating the original.
    assert result is not original
    assert result._templar is templar
    assert result._globals is globals_
    assert original._locals == {'existing': 'original'}
    assert result._locals == {
        'existing': 'overridden',
        'new_var': 'new_value',
    }

# Generated at 2026-10-24 21:10:40.568516
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

# Generated at 2026-10-24 21:10:41.932716
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

# Generated at 2026-10-24 21:10:43.322306
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

# Generated at 2026-10-24 21:10:46.088694
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

# Generated at 2026-10-24 21:10:48.829036
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

# Generated at 2026-10-24 21:10:50.187838
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:03.721631
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template import AnsibleJ2Vars

templar = type(
    "Templar",
    (),
    {"available_variables": {"available_var": "available value"}},
)()

variables = AnsibleJ2Vars(
    templar,
    {"global_var": "global value"},
    {"l_local_var": "local value"},
)

assert variables.__contains__("local_var") is True
assert variables.__contains__("available_var") is True
assert variables.__contains__("global_var") is True
assert variables.__contains__("missing_var") is False

# Generated at 2026-10-24 21:11:05.040722
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:07.561796
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:10.080331
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:12.496701
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:14.913260
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:17.329562
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:19.747433
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:22.164517
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:24.579816
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:26.997990
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:29.414057
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:31.830025
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:34.394551
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:36.812660
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:39.230117
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:41.642863
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:44.059425
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:50.297447
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:11:53.049471
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

# Generated at 2026-10-24 21:11:54.378681
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:10.569171
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template import AnsibleJ2Vars

class FakeTemplar:
    available_variables = {"available_var": "value"}

templar = FakeTemplar()
variables = AnsibleJ2Vars(
    templar,
    globals={"global_var": "value"},
    locals={"local_var": "value"},
)

assert variables.__contains__("local_var") is True
assert variables.__contains__("available_var") is True
assert variables.__contains__("global_var") is True
assert variables.__contains__("missing_var") is False

# Generated at 2026-10-24 21:12:13.438024
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

# Generated at 2026-10-24 21:12:16.201115
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

# Generated at 2026-10-24 21:12:18.624629
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:21.042254
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:23.556800
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:25.973785
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:28.391918
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:30.807554
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:33.225729
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:35.644544
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:38.060407
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:40.476913
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:42.893415
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:45.309604
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:47.729586
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:50.144303
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:52.562842
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:54.978304
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:57.396376
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:12:59.816959
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:13:02.232105
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:13:04.652854
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:13:07.065298
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:13:27.180413
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from jinja2.utils import missing
    _cls = globals().get("AnsibleJ2Vars")
    if _cls is None:
        from ansible.template.vars import AnsibleJ2Vars as _cls

    class _Templar:
        def __init__(self, available):
            self.available_variables = available

    templar = _Templar({"templated_var": 1, "shared": "from_templar"})
    obj = _cls(
        templar,
        {"global_var": 2, "shared_global": 3},
        locals={
            "local_var": 4,
            "l_prefixed": 5,
            "context": "x",
            "environment": "y",
            "template": "z",
            "missing_var": missing,
        },
    )
    assert "local_var" in obj
    assert "prefixed" in obj
    assert "l_prefixed" not in obj
    assert "templated_var" in obj
    assert "shared" in obj
    assert "global_var" in obj
    assert "shared_global" in obj
    assert "missing_var" not in obj
    assert "context" not in obj
    assert "environment" not in obj
    assert "template" not in obj
    assert "nonexistent" not in obj
    assert "" not in obj
    empty = _cls(_Templar({}), {})
    assert "anything" not in empty
    no_locals = _cls(_Templar({"a": 1}), {"b": 2}, locals=None)
    assert "a" in no_locals
    assert "b" in no_locals
    assert "c" not in no_locals

# Generated at 2026-10-24 21:13:29.922086
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

# Generated at 2026-10-24 21:13:32.586937
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

# Generated at 2026-10-24 21:13:35.286013
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

# Generated at 2026-10-24 21:13:36.612930
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:13:53.144427
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-24 21:13:54.541324
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:05.078753
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:21.642385
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:23.074373
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

# Generated at 2026-10-24 21:14:25.856107
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

# Generated at 2026-10-24 21:14:27.190497
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:29.706834
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:32.260434
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:34.679847
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:37.192213
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:39.612254
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:42.033039
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:44.597097
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:47.012628
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:49.431814
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:51.849909
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:14:59.326437
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:02.192346
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

# Generated at 2026-10-24 21:15:04.956873
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

# Generated at 2026-10-24 21:15:06.389780
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

# Generated at 2026-10-24 21:15:07.722713
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:20.519770
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:36.700071
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from types import SimpleNamespace

# Generated at 2026-10-24 21:15:39.121205
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:41.537850
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:43.956214
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:46.376191
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:48.791069
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:51.207962
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:53.626519
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:56.046080
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:15:58.463788
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:00.881690
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:03.298571
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:12.144829
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:13.474775
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:27.798309
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:42.854630
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:45.273202
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:47.690423
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:50.106100
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:52.982838
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:55.401205
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:16:57.816604
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:00.234277
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:02.651857
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:05.069267
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:07.805046
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

# Generated at 2026-10-24 21:17:10.704372
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

# Generated at 2026-10-24 21:17:12.146672
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:26.371122
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:42.959542
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-24 21:17:45.528137
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:47.945279
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:50.363661
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:52.781597
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:55.200290
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:17:57.614693
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:00.030788
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:02.446803
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:04.865144
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:07.279737
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:30.165211
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():from jinja2.utils import missing


# Generated at 2026-10-24 21:18:32.854718
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

# Generated at 2026-10-24 21:18:38.135554
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:40.653181
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:43.170619
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:45.689392
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:48.106429
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:50.526923
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:52.944693
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:55.361433
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:18:57.779765
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:00.196341
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:02.615556
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:05.030389
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:07.452179
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:09.873199
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:12.291336
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:14.706183
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:17.122557
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:19.539229
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:21.956062
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:24.373531
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 21:19:26.789784
# Unit test for method __getitem__ of class AnsibleJ2Vars