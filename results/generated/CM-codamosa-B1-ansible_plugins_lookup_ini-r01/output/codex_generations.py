

# Generated at 2026-10-24 22:22:15.749285
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:22:18.169315
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:22:20.584980
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:22:23.004260
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:22:25.602313
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:22:28.021438
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:22:30.438688
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:22:50.374477
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:22:53.028999
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:02.784012
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-24 22:23:13.193722
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    config = StringIO(
        u'[test_section]\n'
        u'username=alice\n'
        u'host_one=server1\n'
        u'host_two=server2\n'
    )
    lookup.cp.readfp(config)

    # Retrieve an existing key.
    assert lookup.get_value(
        'username', 'test_section', 'default_value', False
    ) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value(
        'missing', 'test_section', 'default_value', False
    ) == 'default_value'

    # Retrieve all values whose keys match the regular expression.
    assert sorted(lookup.get_value(
        r'^host_', 'test_section', 'default_value', True
    )) == ['server1', 'server2']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'^missing$', 'test_section', 'default_value', True
    ) == []

# Generated at 2026-10-24 22:23:15.617094
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:18.033210
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:20.451119
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:22.867440
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:25.288405
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:27.707527
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:30.128702
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:32.547519
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:34.969110
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:37.385139
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:39.807839
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:42.221859
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:44.641501
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:47.060204
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:49.479740
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:23:51.896029
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:54.316129
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:56.735513
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:23:59.153238
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:24:01.570826
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:24:04.159532
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:24:13.368907
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'foo', 'bar')
    lookup.cp.set('test', 'foobar', 'baz')
    lookup.cp.set('test', 'other', 'value')

    # Retrieve an existing key.
    assert lookup.get_value('foo', 'test', 'default', False) == 'bar'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all matching values when the key is a regular expression.
    assert lookup.get_value(r'^foo', 'test', 'default', True) == ['bar', 'baz']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'test', 'default', True) == []

# Generated at 2026-10-24 22:24:28.563167
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

    options = {
        "allow_no_value": False,
        "allow_none": False,
        "case_sensitive": False,
        "default": "",
        "encoding": "utf-8",
        "file": "users.ini",
        "re": False,
        "section": "integration",
        "type": "ini",
    }

    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value="/tmp/users.ini"
    )

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

# Generated at 2026-10-24 22:24:52.727295
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    variables = {'inventory_hostname': 'test-host'}
    resolved_path = '/resolved/path/users.ini'


# Generated at 2026-10-24 22:25:01.331536
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'key1', 'value1')
    lookup.cp.set('test', 'key2', 'value2')
    lookup.cp.set('test', 'other', 'value3')

    # Retrieve an existing key.
    assert lookup.get_value('key1', 'test', 'default', False) == 'value1'

    # Return the default when the key does not exist.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all matching values when the key is a regular expression.
    assert lookup.get_value(r'^key\d$', 'test', 'default', True) == [
        'value1',
        'value2',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'test', 'default', True) == []

# Generated at 2026-10-24 22:25:16.688846
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[global]\nusername=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        'type': 'ini',
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/ansible.ini'
    )

    result = lookup.run(['username'], variables={})

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options={},
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {},
        'files',
        'ansible.ini',
    )
    loader._get_file_contents.assert_called_once_with(
        '/tmp/ansible.ini'
    )

# Generated at 2026-10-24 22:25:26.827731
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_file(StringIO(
        "[application]\n"
        "user = alice\n"
        "db_host = localhost\n"
        "db_port = 5432\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value(
        "user", "application", "default", False
    ) == "alice"

    # Return the supplied default when the key does not exist.
    assert lookup.get_value(
        "missing", "application", "default", False
    ) == "default"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(
        r"^db_", "application", "default", True
    ) == ["localhost", "5432"]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r"^cache_", "application", "default", True
    ) == []

# Generated at 2026-10-24 22:25:36.659815
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        "[users]\n"
        "admin = alice\n"
        "user_one = bob\n"
        "user_two = carol\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value("admin", "users", "default", False) == "alice"

    # Return the supplied default when the key does not exist.
    assert lookup.get_value("missing", "users", "default", False) == "default"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r"^user_", "users", "default", True) == [
        "bob",
        "carol",
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r"^unknown_", "users", "default", True) == []

# Generated at 2026-10-24 22:25:44.849143
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('example')
    lookup.cp.set('example', 'user', 'alice')
    lookup.cp.set('example', 'user.name', 'Alice Smith')
    lookup.cp.set('example', 'user.email', 'alice@example.com')

    # Retrieve a single existing value.
    assert lookup.get_value('user', 'example', 'default', False) == 'alice'

    # Return the supplied default when the option does not exist.
    assert lookup.get_value('missing', 'example', 'default', False) == 'default'

    # Retrieve all values whose keys match a regular expression.
    assert lookup.get_value(r'^user\.', 'example', 'default', True) == [
        'Alice Smith',
        'alice@example.com',
    ]

# Generated at 2026-10-24 22:25:54.475390
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
        "type": "ini",
        "file": "users.ini",
        "section": "integration",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
        "allow_none": False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/tmp/users.ini"
    )

    result = lookup.run(["user"], variables={})

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options={},
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {},
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/tmp/users.ini"
    )

# Generated at 2026-10-24 22:26:04.572933
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        u"""
[test_section]
user = alice
user_admin = bob
host = localhost
"""
    ))

    # Retrieve an existing key.
    assert lookup.get_value('user', 'test_section', 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test_section', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'user.*', 'test_section', 'default', True) == [
        'alice',
        'bob',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'database.*', 'test_section', 'default', True) == []

# Generated at 2026-10-24 22:26:14.134955
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
        "allow_no_value": False,
        "allow_none": False,
        "case_sensitive": False,
        "file": "users.ini",
        "type": "ini",
        "section": "global",
        "encoding": "utf-8",
        "default": "",
        "re": False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/mock/path/users.ini"
    )

    result = lookup.run(["user"], variables={})

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(var_options={}, direct={})
    lookup.find_file_in_search_path.assert_called_once_with(
        {}, "files", "users.ini"
    )
    loader._get_file_contents.assert_called_once_with(
        "/mock/path/users.ini"
    )

# Generated at 2026-10-24 22:26:24.685282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

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
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\nuser=alice\n',
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
        '/tmp/users.ini'
    )

# Generated at 2026-10-24 22:26:41.169695
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
        'default': 'not-found',
        're': False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/fake/path/users.ini'
    )

    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\n'
        b'user=alice\n'
        b'role=administrator\n',
        True,
    )

    result = lookup.run(
        ['user', 'missing'],
        variables={'inventory_hostname': 'localhost'},
    )

    assert result == ['alice', 'not-found']
    lookup.set_options.assert_called_once_with(
        var_options={'inventory_hostname': 'localhost'},
        direct={},
    )
    assert lookup.find_file_in_search_path.call_count == 2
    assert lookup._loader._get_file_contents.call_count == 2

# Generated at 2026-10-24 22:26:43.589820
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:26:46.006084
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:26:48.426518
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:26:50.845651
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:26:53.701688
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:26:56.426655
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:27:05.541643
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test_section')
    lookup.cp.set('test_section', 'key1', 'value1')
    lookup.cp.set('test_section', 'key2', 'value2')
    lookup.cp.set('test_section', 'other', 'value3')

    # Retrieve an existing key.
    assert lookup.get_value('key1', 'test_section', 'default', False) == 'value1'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'test_section', 'default', False) == 'default'

    # Retrieve all values whose keys match a regular expression.
    assert lookup.get_value(
        r'^key\d+$', 'test_section', 'default', True
    ) == ['value1', 'value2']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'^missing', 'test_section', 'default', True
    ) == []

# Generated at 2026-10-24 22:27:22.633711
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
        return_value="/tmp/users.ini"
    )

    variables = {"inventory_hostname": "test-host"}

    result = lookup.run(["user"], variables=variables)

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.get_options.assert_called_once_with()
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/tmp/users.ini"
    )

# Generated at 2026-10-24 22:27:32.880607
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    lookup = LookupModule()
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b"[global]\n"
        b"user=alice\n"
        b"role=admin\n",
        True,
    )

    options = {
        "allow_no_value": False,
        "allow_none": False,
        "case_sensitive": False,
        "file": "users.ini",
        "type": "ini",
        "section": "global",
        "encoding": "utf-8",
        "default": "",
        "re": False,
    }

    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value="/mock/path/users.ini"
    )

    result = lookup.run(["user"], variables={})

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options={}, direct={}
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {}, "files", "users.ini"
    )
    lookup._loader._get_file_contents.assert_called_once_with(
        "/mock/path/users.ini"
    )

# Generated at 2026-10-24 22:27:42.517295
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
        "type": "ini",
        "file": "users.ini",
        "section": "integration",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
        "allow_none": False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/tmp/users.ini"
    )

    result = lookup.run(["user"], variables={})

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(
        var_options={},
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {},
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/tmp/users.ini"
    )

# Generated at 2026-10-24 22:27:44.935680
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:27:47.371274
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:27:49.786919
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:27:52.202206
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:27:54.797660
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:27:57.511939
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:28:34.235006
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock


# Generated at 2026-10-24 22:28:49.886319
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    variables = {'inventory_hostname': 'localhost'}
    options = {
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'default': '',
        'encoding': 'utf-8',
        'file': 'users.ini',
        're': False,
        'section': 'integration',
        'type': 'ini',
    }

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b'[integration]\n'
        b'user=alice\n',
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

# Generated at 2026-10-24 22:28:52.415214
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:28:55.006155
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:28:57.820525
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:29:14.770498
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {'inventory_hostname': 'test-host'}
    options = {
        'allow_no_value': False,
        'case_sensitive': False,
        'default': '',
        'encoding': 'utf-8',
        'file': 'users.ini',
        're': False,
        'section': 'integration',
        'type': 'ini',
    }

    loader = Mock()
    loader._get_file_contents.return_value = (
        b'[integration]\n'
        b'user = test-user\n',
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = Mock()
    lookup.get_options = Mock(return_value=options)
    lookup.find_file_in_search_path = Mock(return_value='/tmp/users.ini')

    result = lookup.run(
        ['user'],
        variables=variables,
        file='users.ini',
        section='integration',
    )

    assert result == ['test-user']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={
            'file': 'users.ini',
            'section': 'integration',
        },
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'users.ini',
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 22:29:31.631457
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
        'default': 'not-found',
        're': False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/mock/path/users.ini'
    )

    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\n'
        b'user=alice\n'
        b'role=administrator\n',
        True,
    )

    variables = {'inventory_hostname': 'localhost'}

    result = lookup.run(
        ['user', 'missing'],
        variables=variables,
        section='integration',
    )

    assert result == ['alice', 'not-found']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={'section': 'integration'},
    )
    assert lookup.find_file_in_search_path.call_count == 2
    lookup.find_file_in_search_path.assert_any_call(
        variables,
        'files',
        'users.ini',
    )
    assert lookup._loader._get_file_contents.call_count == 2
    lookup._loader._get_file_contents.assert_any_call(
        '/mock/path/users.ini'
    )

# Generated at 2026-10-24 22:29:41.819001
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule.__new__(LookupModule)
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'username', 'alice')
    lookup.cp.set('test', 'url_one', 'https://one.example.com')
    lookup.cp.set('test', 'url_two', 'https://two.example.com')

    # Retrieve an existing key.
    assert lookup.get_value('username', 'test', 'default', False) == 'alice'

    # Return the default when the key does not exist.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'^url_', 'test', 'default', True) == [
        'https://one.example.com',
        'https://two.example.com',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'test', 'default', True) == []

# Generated at 2026-10-24 22:29:44.239247
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:29:46.658752
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:29:49.078426
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:29:51.647715
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:29:54.175908
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:29:56.593948
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:30:25.744546
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest

# Generated at 2026-10-24 22:30:43.243894
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[global]\n"
        b"username=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)

    options = {
        "type": "ini",
        "file": "ansible.ini",
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value="/tmp/ansible.ini"
    )

    variables = {"inventory_hostname": "localhost"}

    result = lookup.run(
        terms=["username"],
        variables=variables,
    )

    assert result == ["alice"]

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        "files",
        "ansible.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/tmp/ansible.ini"
    )

# Generated at 2026-10-24 22:30:51.947143
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test_section')
    lookup.cp.set('test_section', 'first_key', 'first_value')
    lookup.cp.set('test_section', 'second_key', 'second_value')
    lookup.cp.set('test_section', 'other_key', 'other_value')

    # Retrieve an existing key.
    assert lookup.get_value(
        'first_key', 'test_section', 'default_value', False
    ) == 'first_value'

    # Return the default for a missing key.
    assert lookup.get_value(
        'missing_key', 'test_section', 'default_value', False
    ) == 'default_value'

    # Retrieve all keys matching a regular expression.
    assert lookup.get_value(
        r'^(first|second)_key$', 'test_section', 'default_value', True
    ) == ['first_value', 'second_value']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'^missing_', 'test_section', 'default_value', True
    ) == []

# Generated at 2026-10-24 22:31:03.047955
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser(allow_no_value=True)
    lookup.cp.readfp(StringIO(
        u"""
[test_section]
user = alice
user_role = admin
host = localhost
empty_key
"""
    ))

    # Retrieve an existing key.
    assert lookup.get_value(
        'user', 'test_section', 'default', False
    ) == 'alice'

    # Return the default when the key does not exist.
    assert lookup.get_value(
        'missing', 'test_section', 'default', False
    ) == 'default'

    # Retrieve all values whose keys match a regular expression.
    assert lookup.get_value(
        r'^user', 'test_section', 'default', True
    ) == ['alice', 'admin']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'^missing', 'test_section', 'default', True
    ) == []

    # Keys without values return None when allow_no_value is enabled.
    assert lookup.get_value(
        'empty_key', 'test_section', 'default', False
    ) is None

    # Missing sections are intentionally propagated to the caller.
    try:
        lookup.get_value('user', 'missing_section', 'default', False)
    except configparser.NoSectionError:
        pass
    else:
        raise AssertionError('Expected configparser.NoSectionError')

# Generated at 2026-10-24 22:31:13.248094
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

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
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/users.ini'
    )
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\nuser=alice\n',
        True,
    )

    result = lookup.run(['user'], variables={'inventory_hostname': 'localhost'})

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

# Generated at 2026-10-24 22:31:23.281360
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[global]\n"
        b"user=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        "allow_no_value": False,
        "allow_none": False,
        "case_sensitive": False,
        "file": "ansible.ini",
        "type": "ini",
        "section": "global",
        "encoding": "utf-8",
        "default": "",
        "re": False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/tmp/ansible.ini"
    )

    result = lookup.run(
        terms=["user"],
        variables={"inventory_hostname": "localhost"},
    )

    assert result == ["alice"]

    lookup.set_options.assert_called_once_with(
        var_options={"inventory_hostname": "localhost"},
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {"inventory_hostname": "localhost"},
        "files",
        "ansible.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/tmp/ansible.ini"
    )

# Generated at 2026-10-24 22:31:40.486672
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[global]\n"
        b"user = test-user\n",
        True,
    )

    lookup = LookupModule(loader=loader)

    options = {
        "allow_no_value": False,
        "allow_none": False,
        "case_sensitive": False,
        "file": "users.ini",
        "type": "ini",
        "section": "global",
        "encoding": "utf-8",
        "default": "",
        "re": False,
    }

    variables = {"inventory_hostname": "localhost"}

    with patch.object(lookup, "set_options") as set_options, \
            patch.object(lookup, "get_options", return_value=options), \
            patch.object(
                lookup,
                "find_file_in_search_path",
                return_value="/tmp/users.ini",
            ) as find_file:

        result = lookup.run(["user"], variables=variables)

    assert result == ["test-user"]

    set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    find_file.assert_called_once_with(
        variables,
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with(
        "/tmp/users.ini",
    )

# Generated at 2026-10-24 22:31:48.371751
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        u"[global]\n"
        u"user = alice\n"
        u"user_name = Alice Smith\n"
        u"host = example.com\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value('user', 'global', '', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'global', 'default-value', False) == 'default-value'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'^user', 'global', '', True) == [
        'alice',
        'Alice Smith',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing', 'global', '', True) == []

# Generated at 2026-10-24 22:31:50.952653
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:31:53.477046
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:31:56.009238
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:31:58.646913
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:32:01.375925
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:32:04.449596
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:32:19.602281
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    variables = {'inventory_hostname': 'localhost'}
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
        b'[integration]\nuser = alice\n',
        True,
    )

    lookup = LookupModule(loader=loader, templar=MagicMock())
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