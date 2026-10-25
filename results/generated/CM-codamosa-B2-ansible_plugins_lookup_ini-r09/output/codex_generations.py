

# Generated at 2026-10-24 20:01:38.358757
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert lookup._loader is None  # not set until used with a loader

# Generated at 2026-10-24 20:01:39.790819
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert lookup._loader is None  # not set until used with a loader

# Generated at 2026-10-24 20:01:41.116329
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert lookup._loader is None  # not set until used with a loader

# Generated at 2026-10-24 20:01:43.661736
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 20:01:46.184092
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 20:01:48.718659
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 20:01:51.135700
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:01:53.552104
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:01:55.967991
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:02:15.430044
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    variables = {'inventory_hostname': 'localhost'}

    options = {
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'file': 'users.ini',
        'type': 'ini',
        'section': 'integration',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    }

    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options.copy())
    lookup.find_file_in_search_path = MagicMock(
        return_value='/fake/path/users.ini'
    )
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\n'
        b'user=alice\n'
        b'host=example.com\n',
        True,
    )

    result = lookup.run(['user'], variables=variables)

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'users.ini',
    )
    lookup._loader._get_file_contents.assert_called_once_with(
        '/fake/path/users.ini'
    )

# Generated at 2026-10-24 20:02:32.016545
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {}
    options = {
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'file': 'ansible.ini',
        'type': 'ini',
        'section': 'global',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    }

    lookup = LookupModule()
    lookup.set_options = Mock()
    lookup.get_options = Mock(return_value=options)
    lookup.find_file_in_search_path = Mock(
        return_value='/tmp/ansible.ini'
    )
    lookup._loader = Mock()
    lookup._loader._get_file_contents.return_value = (
        b'[global]\nusername=test-user\n',
        True,
    )

    result = lookup.run(['username'], variables=variables)

    assert result == ['test-user']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'ansible.ini',
    )
    lookup._loader._get_file_contents.assert_called_once_with(
        '/tmp/ansible.ini'
    )

# Generated at 2026-10-24 20:02:33.451317
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:02:53.558810
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:02:55.940635
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:02:57.412934
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 20:03:13.692763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[global]\n"
        b"user = alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        "allow_no_value": False,
        "case_sensitive": False,
        "default": "",
        "encoding": "utf-8",
        "file": "users.ini",
        "re": False,
        "section": "global",
        "type": "ini",
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/mock/path/users.ini"
    )

    variables = {"inventory_hostname": "test-host"}
    result = lookup.run(["user"], variables=variables)

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/mock/path/users.ini"
    )

# Generated at 2026-10-24 20:03:15.111587
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:03:24.856588
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:03:26.181171
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 20:03:27.546160
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:03:38.372925
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[integration]\n"
        b"user=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'default': '',
        'encoding': 'utf-8',
        'file': 'users.ini',
        're': False,
        'section': 'integration',
        'type': 'ini',
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )

    variables = {}
    result = lookup.run(['user'], variables=variables)

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'users.ini',
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 20:04:00.798706
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    options = {
        'allow_no_value': False,
        'case_sensitive': False,
        'file': 'users.ini',
        'type': 'ini',
        'section': 'global',
        'encoding': 'utf-8',
        'default': 'not-found',
        're': False,
    }

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b'[global]\n'
        b'user = alice\n'
        b'role = administrator\n',
        True,
    )

    lookup = LookupModule()
    lookup._loader = loader
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )

    variables = {}
    result = lookup.run(['user', 'missing'], variables=variables)

    assert result == ['alice', 'not-found']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    assert lookup.find_file_in_search_path.call_count == 2
    lookup.find_file_in_search_path.assert_any_call(
        variables,
        'files',
        'users.ini',
    )
    assert loader._get_file_contents.call_count == 2

# Generated at 2026-10-24 20:04:02.234794
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:04:03.608366
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:04:05.001996
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:04:21.163943
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import Mock

    loader = Mock()
    loader._get_file_contents.return_value = (
        b"[integration]\n"
        b"user=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = Mock()
    lookup.get_options = Mock(return_value={
        "type": "ini",
        "file": "users.ini",
        "section": "integration",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    })
    lookup.find_file_in_search_path = Mock(return_value="/tmp/users.ini")

    variables = {}
    result = lookup.run(["user"], variables=variables)

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with("/tmp/users.ini")

# Generated at 2026-10-24 20:04:31.620339
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:04:32.943709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 20:04:48.925325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[integration]\nuser=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        "allow_no_value": False,
        "allow_none": False,
        "case_sensitive": False,
        "default": "",
        "encoding": "utf-8",
        "file": "users.ini",
        "re": False,
        "section": "integration",
        "type": "ini",
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/resolved/users.ini"
    )

    variables = {"inventory_hostname": "localhost"}
    result = lookup.run(["user"], variables=variables)

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/resolved/users.ini"
    )

# Generated at 2026-10-24 20:04:51.347574
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:04:53.756000
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:04:56.334782
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:04:58.756033
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:05:01.169184
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:05:03.586210
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:05:06.001887
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:05:08.419480
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:05:10.832289
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:05:22.395194
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = object.__new__(LookupModule)

# Generated at 2026-10-24 20:05:27.954282
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-24 20:05:44.528935
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[integration]\n"
        b"user=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'default': '',
        'encoding': 'utf-8',
        'file': 'users.ini',
        're': False,
        'section': 'integration',
        'type': 'ini',
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )

    variables = {'inventory_hostname': 'localhost'}
    result = lookup.run(['user'], variables=variables)

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'users.ini',
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 20:05:45.961638
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:06:01.836396
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[integration]\nuser=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        "allow_no_value": False,
        "case_sensitive": False,
        "file": "users.ini",
        "type": "ini",
        "section": "integration",
        "encoding": "utf-8",
        "default": "",
        "re": False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/fake/path/users.ini"
    )

    variables = {"inventory_hostname": "testhost"}

    result = lookup.run(["user"], variables=variables)

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/fake/path/users.ini"
    )

# Generated at 2026-10-24 20:06:04.255715
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:06:06.674553
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:06:09.089089
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:06:11.506515
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:06:13.924160
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:06:16.341239
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:06:18.757494
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:06:21.176286
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:06:28.766486
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule.__new__(LookupModule)

# Generated at 2026-10-24 20:06:44.847480
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    variables = {'inventory_hostname': 'test-host'}
    options = {
        'type': 'ini',
        'file': 'users.ini',
        'section': 'integration',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    }

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b'[integration]\nuser=alice\n',
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )

    result = lookup.run(['user'], variables=variables)

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'users.ini',
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 20:06:46.276898
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:06:56.928014
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    lookup = LookupModule()

    options = {
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'file': 'test.ini',
        'type': 'ini',
        'section': 'global',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    }

    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/test.ini'
    )

    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[global]\nusername=test-user\n',
        True,
    )

    result = lookup.run(['username'], variables={})

    assert result == ['test-user']
    lookup.set_options.assert_called_once_with(
        var_options={},
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {},
        'files',
        'test.ini',
    )
    lookup._loader._get_file_contents.assert_called_once_with(
        '/tmp/test.ini'
    )

# Generated at 2026-10-24 20:06:58.358769
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:07:15.051095
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    variables = {'inventory_hostname': 'localhost'}
    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b'[users]\nusername=alice\n',
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        'type': 'ini',
        'file': 'users.ini',
        'section': 'users',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )

    result = lookup.run(
        ['username'],
        variables=variables,
        section='users',
        file='users.ini',
    )

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={'section': 'users', 'file': 'users.ini'},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'users.ini',
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 20:07:17.471673
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:07:19.889750
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:07:22.314793
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:07:24.731156
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:27.145032
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:29.561450
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:31.977844
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:34.396438
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:36.813465
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:39.261113
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:41.645311
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:44.061416
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:46.478159
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:48.897879
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:07:59.911615
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:16.286198
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[global]\n"
        b"user=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        "type": "ini",
        "file": "users.ini",
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/tmp/users.ini"
    )

    result = lookup.run(["user"])

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options=None,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        None,
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/tmp/users.ini"
    )

# Generated at 2026-10-24 20:08:26.938246
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'file': 'users.ini',
        'type': 'ini',
        'section': 'integration',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\nuser=alice\n',
        True,
    )

    result = lookup.run(
        ['user'],
        variables={'inventory_hostname': 'localhost'},
    )

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options={'inventory_hostname': 'localhost'},
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {'inventory_hostname': 'localhost'},
        'files',
        'users.ini',
    )
    lookup._loader._get_file_contents.assert_called_once_with(
        '/tmp/users.ini'
    )

# Generated at 2026-10-24 20:08:29.358637
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:08:31.776537
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:08:34.192522
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:08:36.609994
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:39.193985
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:41.609247
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:44.965662
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:47.382135
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:49.798596
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:52.215219
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:54.633464
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:57.049037
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:08:59.468022
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:09:01.884726
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:09:04.301800
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:09:06.717799
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:09.135593
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:17.741448
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:19.160956
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:09:36.263826
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {'inventory_hostname': 'localhost'}
    options = {
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'file': 'users.ini',
        'type': 'ini',
        'section': 'integration',
        'encoding': 'utf-8',
        'default': 'not-found',
        're': False,
    }

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\nuser=alice\n',
        True,
    )

    result = lookup.run(
        ['user', 'missing_user'],
        variables=variables,
    )

    assert result == ['alice', 'not-found']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    assert lookup.find_file_in_search_path.call_count == 2
    lookup.find_file_in_search_path.assert_called_with(
        variables,
        'files',
        'users.ini',
    )
    assert lookup._loader._get_file_contents.call_count == 2
    lookup._loader._get_file_contents.assert_called_with(
        '/tmp/users.ini'
    )

# Generated at 2026-10-24 20:09:38.685074
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:41.100490
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:43.517104
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:45.939331
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:48.357332
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:50.779526
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:09:53.313664
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:09:55.730001
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:10:04.325538
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule.__new__(LookupModule)

# Generated at 2026-10-24 20:10:22.754316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class FakeLoader:
        def __init__(self):
            self.requested_paths = []

        def _get_file_contents(self, path):
            self.requested_paths.append(path)
            return b"[global]\nuser = alice\n", True

    lookup = LookupModule()
    lookup._loader = FakeLoader()

    options = {
        'allow_no_value': False,
        'case_sensitive': False,
        'file': 'ansible.ini',
        'type': 'ini',
        'section': 'global',
        'encoding': 'utf-8',
        'default': 'not-found',
        're': False,
    }

    lookup.set_options = lambda **kwargs: None
    lookup.get_options = lambda: options.copy()
    lookup.find_file_in_search_path = (
        lambda variables, subdir, filename: '/tmp/ansible.ini'
    )

    result = lookup.run(['user'], variables={})

    assert result == ['alice']
    assert lookup._loader.requested_paths == ['/tmp/ansible.ini']

# Generated at 2026-10-24 20:10:28.170439
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:30.762786
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:33.180575
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:35.598909
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:38.150760
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:40.566761
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:42.984237
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:45.399156
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:47.814624
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:50.232829
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:10:52.653535
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:10:55.067166
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 20:10:57.482904
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:10:59.899999
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:11:02.315287
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:11:03.718812
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:11:05.149791
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.add_section('empty')

    # exact match returns single value
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    assert lookup.get_value('key2', 'section1', '', False) == 'value2'

    # missing option returns dflt
    assert lookup.get_value('missing', 'section1', 'mydefault', False) == 'mydefault'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # regexp returns list of matching values
    assert sorted(lookup.get_value('key.*', 'section1', '', True)) == ['value1', 'value2']
    assert lookup.get_value('^key1$', 'section1', '', True) == ['value1']

    # regexp with no match returns empty list (not dflt)
    assert lookup.get_value('nomatch.*', 'section1', 'mydefault', True) == []

    # missing section propagates NoSectionError
    try:
        lookup.get_value('key1', 'nosection', '', False)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key.*', 'nosection', '', True)
        assert False, 'expected NoSectionError'
    except configparser.NoSectionError:
        pass

# Generated at 2026-10-24 20:11:21.528928
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {}
    options = {
        'type': 'ini',
        'file': 'users.ini',
        'section': 'integration',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    }

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b'[integration]\nuser=alice\n',
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )

    result = lookup.run(['user'], variables=variables)

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'users.ini',
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 20:11:32.137623
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:11:34.561390
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:11:36.977432
# Unit test for method run of class LookupModule