

# Generated at 2026-10-24 20:42:04.786285
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    class DummyTemplar(object):
        available_variables = {'templar_var': 'templar value'}

        def template(self, value):
            return value

    templar = DummyTemplar()
    variables = AnsibleJ2Vars(
        templar,
        {'global_var': 'global value'},
        locals={'existing': 'original value'},
    )

    # No locals returns the same variable proxy.
    assert variables.add_locals(None) is variables

    updated = variables.add_locals({
        'existing': 'updated value',
        'new_local': 'new value',
    })

    # A new proxy is returned and the original remains unchanged.
    assert updated is not variables
    assert variables['existing'] == 'original value'
    assert 'new_local' not in variables

    # Existing locals are overridden and new locals are added.
    assert updated['existing'] == 'updated value'
    assert updated['new_local'] == 'new value'

    # Templar variables and globals remain available.
    assert updated['templar_var'] == 'templar value'
    assert updated['global_var'] == 'global value'

# Generated at 2026-10-24 20:42:06.170864
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:42:21.379395
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():templar = type(
        "Templar",
        (),
        {"available_variables": {"host_var": "value"}},
    )()

# Generated at 2026-10-24 20:42:36.480639
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

# Generated at 2026-10-24 20:42:38.992981
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:42:41.409776
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:42:43.828670
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:42:46.346554
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:42:48.763952
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:42:51.183212
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:43:00.140357
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:43:06.782027
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():templar = type("TemplarStub", (), {"available_variables": {"name": "value"}})()

# Generated at 2026-10-24 20:43:08.101747
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:43:19.372926
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:43:29.808622
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():obj = object.__new__(AnsibleJ2Vars)

# Generated at 2026-10-24 20:43:41.287327
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    class DummyTemplar(object):
        def __init__(self):
            self.available_variables = {'templar_var': 'templar value'}

        def template(self, value):
            return value

    templar = DummyTemplar()
    variables = AnsibleJ2Vars(
        templar,
        {'global_var': 'global value'},
        locals={'existing': 'original value'},
    )

    # No locals should return the existing proxy unchanged.
    assert variables.add_locals(None) is variables

    updated = variables.add_locals({
        'existing': 'updated value',
        'new_var': 'new value',
    })

    # A new proxy is returned and existing locals can be overridden.
    assert updated is not variables
    assert updated['existing'] == 'updated value'
    assert updated['new_var'] == 'new value'

    # The original proxy is not modified.
    assert variables['existing'] == 'original value'
    assert 'new_var' not in variables

    # Templar variables and globals remain available in the new proxy.
    assert updated['templar_var'] == 'templar value'
    assert updated['global_var'] == 'global value'

# Generated at 2026-10-24 20:44:10.106844
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

# Generated at 2026-10-24 20:44:11.433587
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:44:21.311003
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():obj = AnsibleJ2Vars.__new__(AnsibleJ2Vars)

# Generated at 2026-10-24 20:44:33.743889
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from types import SimpleNamespace


# Generated at 2026-10-24 20:44:35.165096
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

# Generated at 2026-10-24 20:44:36.540108
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

# Generated at 2026-10-24 20:45:16.230297
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

# Generated at 2026-10-24 20:45:17.659973
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

# Generated at 2026-10-24 20:45:19.094094
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

# Generated at 2026-10-24 20:45:20.529377
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

# Generated at 2026-10-24 20:45:33.043134
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    class DummyTemplar(object):
        available_variables = {}

        def template(self, value):
            return value

    templar = DummyTemplar()
    globals_ = {'global_var': 'global value'}

    original = AnsibleJ2Vars(
        templar,
        globals_,
        locals={'existing': 'original value'}
    )

    # No locals should return the existing instance.
    assert original.add_locals(None) is original

    updated = original.add_locals({
        'existing': 'updated value',
        'new_var': 'new value',
        'l_scoped_var': 'scoped value',
        'context': 'ignored',
        'undefined_var': missing,
    })

    # A new proxy is returned and the original remains unchanged.
    assert updated is not original
    assert original['existing'] == 'original value'
    assert 'new_var' not in original

    # New locals are merged, with newer values taking precedence.
    assert updated['existing'] == 'updated value'
    assert updated['new_var'] == 'new value'

    # Jinja's local prefix is removed.
    assert updated['scoped_var'] == 'scoped value'
    assert 'l_scoped_var' not in updated

    # Internal and missing Jinja values are excluded.
    assert 'context' not in updated
    assert 'undefined_var' not in updated

    # Existing globals and dependencies are retained.
    assert updated['global_var'] == 'global value'
    assert updated._templar is templar
    assert updated._globals is globals_

# Generated at 2026-10-24 20:45:35.724241
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

# Generated at 2026-10-24 20:45:38.422188
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

# Generated at 2026-10-24 20:45:50.324252
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    class DummyTemplar(object):
        available_variables = {}

    templar = DummyTemplar()
    globals_vars = {'global_var': 'global'}
    variables = AnsibleJ2Vars(
        templar,
        globals_vars,
        locals={'existing': 'original'}
    )

    # No additional locals should return the original proxy.
    assert variables.add_locals(None) is variables

    updated = variables.add_locals({
        'existing': 'overridden',
        'added': 'new',
    })

    # A new proxy is returned with merged locals.
    assert updated is not variables
    assert updated._templar is templar
    assert updated._globals is globals_vars
    assert updated._locals == {
        'existing': 'overridden',
        'added': 'new',
    }

    # The original proxy must remain unchanged.
    assert variables._locals == {'existing': 'original'}

# Generated at 2026-10-24 20:45:52.867149
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:45:55.391425
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:46:06.197400
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:46:09.070029
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

# Generated at 2026-10-24 20:46:11.830623
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

# Generated at 2026-10-24 20:46:14.514649
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

# Generated at 2026-10-24 20:46:15.849345
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:46:38.454411
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():templar = type('Templar', (), {'available_variables': {'templar_var': 1}})()

# Generated at 2026-10-24 20:46:39.993178
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

# Generated at 2026-10-24 20:46:41.428265
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

# Generated at 2026-10-24 20:46:42.856454
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

# Generated at 2026-10-24 20:46:44.291611
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

# Generated at 2026-10-24 20:46:45.715880
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:47:06.408333
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():templar = type("Templar", (), {"available_variables": {"available_var": 1}})()

# Generated at 2026-10-24 20:47:07.742724
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:47:24.225597
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:47:39.073972
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from types import SimpleNamespace


# Generated at 2026-10-24 20:47:41.829800
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

# Generated at 2026-10-24 20:47:44.605362
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

# Generated at 2026-10-24 20:47:47.421130
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

# Generated at 2026-10-24 20:47:50.138292
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

# Generated at 2026-10-24 20:47:52.897865
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:47:55.535226
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:48:02.120757
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:48:05.013807
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

# Generated at 2026-10-24 20:48:07.849383
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

# Generated at 2026-10-24 20:48:09.248013
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:48:23.108549
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():obj = object.__new__(AnsibleJ2Vars)

# Generated at 2026-10-24 20:48:38.056588
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from types import SimpleNamespace
from ansible.template.vars import AnsibleJ2Vars

templar = SimpleNamespace(available_variables={"host_name": "web01"})
variables = AnsibleJ2Vars(
    templar,
    {"global_name": "all_hosts"},
    {"l_local_name": "local_value"},
)

assert variables.__contains__("local_name") is True
assert variables.__contains__("host_name") is True
assert variables.__contains__("global_name") is True
assert variables.__contains__("missing_name") is False

# Generated at 2026-10-24 20:48:40.815221
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

# Generated at 2026-10-24 20:48:42.153658
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:49:03.962252
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:49:20.484797
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:49:23.221508
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

# Generated at 2026-10-24 20:49:24.651046
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

# Generated at 2026-10-24 20:49:26.031973
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:49:47.278970
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:49:49.800768
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:49:52.326247
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:49:54.739894
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:49:57.155696
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:00.295439
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:02.713032
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:05.129783
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:07.550173
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:09.966345
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:12.381555
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:14.799995
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:17.213125
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:19.631192
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:22.049313
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:24.465251
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:26.882714
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:29.298576
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:31.714486
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:34.130980
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:36.548205
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:38.964573
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:41.381308
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:43.800707
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:46.216349
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:48.635236
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:51.051816
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:50:53.469884
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:51:00.802378
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:51:02.237509
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:51:16.644385
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:51:28.450817
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from types import SimpleNamespace


# Generated at 2026-10-24 20:51:31.205487
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

# Generated at 2026-10-24 20:51:35.311513
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

# Generated at 2026-10-24 20:51:38.060618
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

# Generated at 2026-10-24 20:51:39.390766
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-24 20:51:55.806680
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars