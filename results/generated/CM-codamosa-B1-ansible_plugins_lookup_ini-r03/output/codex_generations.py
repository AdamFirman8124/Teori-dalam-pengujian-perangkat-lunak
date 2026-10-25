

# Generated at 2026-10-24 22:54:40.340023
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        u"""
[global]
username = alice
user_email = alice@example.com
timeout = 30
"""
    ))

    # Retrieve an existing key.
    assert lookup.get_value('username', 'global', 'default', False) == 'alice'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'global', 'default', False) == 'default'

    # Retrieve all values whose keys match a regular expression.
    values = lookup.get_value(r'^user', 'global', 'default', True)
    assert set(values) == {'alice', 'alice@example.com'}

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing', 'global', 'default', True) == []

# Generated at 2026-10-24 22:54:48.729208
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-24 22:54:57.397259
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_file(StringIO(
        "[global]\n"
        "user=alice\n"
        "user.name=Alice Example\n"
        "host=example.com\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value("user", "global", "default", False) == "alice"

    # Return the supplied default for a missing key.
    assert lookup.get_value("missing", "global", "default", False) == "default"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r"^user", "global", "default", True) == [
        "alice",
        "Alice Example",
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r"^missing$", "global", "default", True) == []

# Generated at 2026-10-24 22:55:07.979238
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        "[global]\n"
        "user = alice\n"
        "user_name = Alice Smith\n"
        "enabled = true\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value("user", "global", "default", False) == "alice"

    # Return the supplied default for a missing key.
    assert lookup.get_value("missing", "global", "default", False) == "default"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r"^user", "global", "default", True) == [
        "alice",
        "Alice Smith",
    ]

# Generated at 2026-10-24 22:55:14.942781
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-24 22:55:27.241779
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        "[global]\n"
        "username=alice\n"
        "user_email=alice@example.com\n"
        "hostname=example.com\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value(
        "username", "global", "default", False
    ) == "alice"

    # Return the supplied default when the key does not exist.
    assert lookup.get_value(
        "missing", "global", "default", False
    ) == "default"

    # Return all matching values when the key is a regular expression.
    assert lookup.get_value(
        r"^user", "global", "default", True
    ) == ["alice", "alice@example.com"]

    # NoSectionError should propagate to the caller.
    try:
        lookup.get_value("username", "missing_section", "default", False)
    except configparser.NoSectionError:
        pass
    else:
        raise AssertionError("Expected configparser.NoSectionError")

# Generated at 2026-10-24 22:55:42.693996
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        "[users]\n"
        "admin = alice\n"
        "guest = bob\n"
        "user.name = charlie\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value("admin", "users", "", False) == "alice"

    # Return the supplied default when the key does not exist.
    assert lookup.get_value("missing", "users", "fallback", False) == "fallback"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r"^(admin|guest)$", "users", "", True) == [
        "alice",
        "bob",
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r"^unknown", "users", "fallback", True) == []

# Generated at 2026-10-24 22:55:54.777977
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    lookup = LookupModule()
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b"[integration]\n"
        b"user=alice\n"
        b"role=developer\n",
        True,
    )

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

    result = lookup.run(["user"], variables={})

    assert result == ["alice"]
    lookup.set_options.assert_called_once_with(var_options={}, direct={})
    lookup.find_file_in_search_path.assert_called_once_with(
        {}, "files", "users.ini"
    )
    lookup._loader._get_file_contents.assert_called_once_with(
        "/tmp/users.ini"
    )

# Generated at 2026-10-24 22:56:05.323447
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[global]\n"
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
        "file": "ansible.ini",
        "re": False,
        "section": "global",
        "type": "ini",
    }

    with patch.object(lookup, "set_options") as set_options, \
            patch.object(lookup, "get_options", return_value=options), \
            patch.object(
                lookup,
                "find_file_in_search_path",
                return_value="/tmp/ansible.ini",
            ) as find_file:

        result = lookup.run(["user"], variables={"inventory_hostname": "test"})

    assert result == ["alice"]
    set_options.assert_called_once_with(
        var_options={"inventory_hostname": "test"},
        direct={},
    )
    find_file.assert_called_once_with(
        {"inventory_hostname": "test"},
        "files",
        "ansible.ini",
    )
    loader._get_file_contents.assert_called_once_with("/tmp/ansible.ini")

# Generated at 2026-10-24 22:56:15.153035
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        "[users]\n"
        "name=alice\n"
        "user.name=Alice Smith\n"
        "user.email=alice@example.com\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value('name', 'users', 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'users', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    values = lookup.get_value(r'^user\.', 'users', 'default', True)
    assert sorted(values) == ['Alice Smith', 'alice@example.com']

# Generated at 2026-10-24 22:56:25.292773
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'file': 'test.ini',
        'type': 'ini',
        'section': 'global',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    })
    lookup.find_file_in_search_path = MagicMock(return_value='/tmp/test.ini')
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[global]\nusername=alice\n',
        True,
    )

    result = lookup.run(['username'], variables={})

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(var_options={}, direct={})
    lookup.find_file_in_search_path.assert_called_once_with(
        {}, 'files', 'test.ini'
    )
    lookup._loader._get_file_contents.assert_called_once_with('/tmp/test.ini')

# Generated at 2026-10-24 22:56:39.537555
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
        'type': 'ini',
        'file': 'users.ini',
        'section': 'integration',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
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

# Generated at 2026-10-24 22:56:49.867530
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        u"""
[test]
username = alice
user_email = alice@example.com
enabled = true
"""
    ))

    # Retrieve an existing key.
    assert lookup.get_value('username', 'test', 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'^user', 'test', 'default', True) == [
        'alice',
        'alice@example.com',
    ]

# Generated at 2026-10-24 22:57:05.535119
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[integration]\n"
        b"user=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    variables = {"inventory_hostname": "localhost"}
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

    with patch.object(lookup, "set_options") as set_options, \
            patch.object(lookup, "get_options", return_value=options), \
            patch.object(
                lookup,
                "find_file_in_search_path",
                return_value="/tmp/users.ini",
            ) as find_file:

        result = lookup.run(["user"], variables=variables)

    assert result == ["alice"]
    set_options.assert_called_once_with(
        var_options=variables,
        direct={},
    )
    find_file.assert_called_once_with(
        variables,
        "files",
        "users.ini",
    )
    loader._get_file_contents.assert_called_once_with("/tmp/users.ini")

# Generated at 2026-10-24 22:57:15.979681
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    config = StringIO(
        "[example]\n"
        "username=alice\n"
        "service_one=enabled\n"
        "service_two=disabled\n"
    )
    lookup.cp.readfp(config)

    # Retrieve an existing key.
    assert lookup.get_value("username", "example", "default", False) == "alice"

    # Return the default for a missing key.
    assert lookup.get_value("missing", "example", "default", False) == "default"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(
        r"service_.*", "example", "default", True
    ) == ["enabled", "disabled"]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r"unknown_.*", "example", "default", True
    ) == []

# Generated at 2026-10-24 22:57:23.806940
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        "[test]\n"
        "user=alice\n"
        "user_admin=bob\n"
        "enabled=true\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value("user", "test", "default", False) == "alice"

    # Return the default for a missing key.
    assert lookup.get_value("missing", "test", "default", False) == "default"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r"user.*", "test", "default", True) == [
        "alice",
        "bob",
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r"missing.*", "test", "default", True) == []

# Generated at 2026-10-24 22:57:34.501424
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[global]\n"
        b"user=alice\n"
        b"enabled=true\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        "allow_no_value": False,
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

    variables = {"inventory_hostname": "localhost"}
    result = lookup.run(
        ["user", "missing"],
        variables=variables,
        section="global",
    )

    assert result == ["alice", ""]
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={"section": "global"},
    )
    lookup.find_file_in_search_path.assert_any_call(
        variables,
        "files",
        "ansible.ini",
    )
    assert lookup.find_file_in_search_path.call_count == 2
    assert loader._get_file_contents.call_count == 2

# Generated at 2026-10-24 22:57:42.604064
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_string(
        "[test]\n"
        "user=alice\n"
        "user_name=Alice Smith\n"
        "host=localhost\n"
    )

    # Retrieve an existing key.
    assert lookup.get_value("user", "test", "default", False) == "alice"

    # Return the default for a missing key.
    assert lookup.get_value("missing", "test", "default", False) == "default"

    # Retrieve all matching values when the key is a regular expression.
    assert lookup.get_value(r"^user", "test", "default", True) == [
        "alice",
        "Alice Smith",
    ]

# Generated at 2026-10-24 22:57:52.513511
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('integration')
    lookup.cp.set('integration', 'user', 'alice')
    lookup.cp.set('integration', 'user.name', 'Alice Smith')
    lookup.cp.set('integration', 'user.email', 'alice@example.com')
    lookup.cp.set('integration', 'host', 'example.com')

    # Retrieve an existing key.
    assert lookup.get_value('user', 'integration', '', False) == 'alice'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'integration', 'fallback', False) == 'fallback'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(
        r'^user\.', 'integration', '', True
    ) == ['Alice Smith', 'alice@example.com']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'^missing', 'integration', 'fallback', True
    ) == []

# Generated at 2026-10-24 22:58:01.752313
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'username', 'alice')
    lookup.cp.set('test', 'database_host', 'localhost')
    lookup.cp.set('test', 'database_port', '5432')

    # Retrieve an existing key.
    assert lookup.get_value('username', 'test', '', False) == 'alice'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'test', 'fallback', False) == 'fallback'

    # Retrieve all matching values when the key is a regular expression.
    values = lookup.get_value(r'^database_', 'test', '', True)
    assert sorted(values) == ['5432', 'localhost']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing_', 'test', '', True) == []

# Generated at 2026-10-24 22:58:12.095485
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

    variables = {'inventory_hostname': 'localhost'}

    result = lookup.run(
        ['user'],
        variables=variables,
        file='users.ini',
        section='integration',
    )

    assert result == ['alice']
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
    lookup._loader._get_file_contents.assert_called_once_with(
        '/tmp/users.ini'
    )

# Generated at 2026-10-24 22:58:22.027175
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'username', 'alice')
    lookup.cp.set('test', 'user_id', '42')
    lookup.cp.set('test', 'hostname', 'example.com')

    # Retrieve an existing key.
    assert lookup.get_value('username', 'test', 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match a regular expression.
    assert lookup.get_value(r'^user', 'test', 'default', True) == [
        'alice',
        '42',
    ]

# Generated at 2026-10-24 22:58:33.291992
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    config = StringIO(
        u"[global]\n"
        u"user=alice\n"
        u"user.name=Alice Example\n"
        u"host=localhost\n"
    )
    lookup.cp.readfp(config)

    # Retrieve an existing key.
    assert lookup.get_value("user", "global", "default", False) == "alice"

    # Return the supplied default when the key does not exist.
    assert lookup.get_value("missing", "global", "default", False) == "default"

    # Retrieve all values whose keys match a regular expression.
    assert sorted(lookup.get_value(r"^user", "global", "default", True)) == [
        "Alice Example",
        "alice",
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r"^missing$", "global", "default", True) == []

# Generated at 2026-10-24 22:58:42.712473
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:58:52.236017
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 22:59:02.475711
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    config = StringIO(
        u'[test]\n'
        u'key1 = value1\n'
        u'key2 = value2\n'
        u'other = value3\n'
    )
    lookup.cp.readfp(config)

    # Retrieve an existing key.
    assert lookup.get_value('key1', 'test', 'default', False) == 'value1'

    # Return the default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'key\d+', 'test', 'default', True) == [
        'value1',
        'value2',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'unknown.*', 'test', 'default', True) == []

# Generated at 2026-10-24 22:59:12.613372
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    lookup.cp.add_section('users')
    lookup.cp.set('users', 'user1', 'alice')
    lookup.cp.set('users', 'user2', 'bob')
    lookup.cp.set('users', 'admin', 'carol')

    # Retrieve an existing key.
    assert lookup.get_value('user1', 'users', 'default', False) == 'alice'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'users', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert sorted(
        lookup.get_value(r'^user\d+$', 'users', 'default', True)
    ) == ['alice', 'bob']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing', 'users', 'default', True) == []

# Generated at 2026-10-24 22:59:23.057958
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_file(StringIO("""
[global]
user = alice
user_name = Alice Smith
role = admin
"""))

    # Retrieve an existing key.
    assert lookup.get_value('user', 'global', 'default-user', False) == 'alice'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'global', 'default-user', False) == 'default-user'

    # Retrieve all values whose keys match the regular expression.
    values = lookup.get_value(r'^user', 'global', 'default-user', True)
    assert sorted(values) == ['Alice Smith', 'alice']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'global', 'default-user', True) == []

# Generated at 2026-10-24 22:59:45.052155
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    variables = {'inventory_hostname': 'test-host'}
    options = {
        'type': 'ini',
        'file': 'users.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': 'not-found',
        'case_sensitive': False,
        'allow_no_value': False,
    }

    lookup.set_options = Mock()
    lookup.get_options = Mock(return_value=options)
    lookup.find_file_in_search_path = Mock(
        return_value='/fake/path/users.ini'
    )

    lookup._loader = Mock()
    lookup._loader._get_file_contents.return_value = (
        b'[global]\n'
        b'user = alice\n'
        b'role = administrator\n',
        True,
    )

    result = lookup.run(
        terms=['user', 'missing'],
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
        '/fake/path/users.ini'
    )

# Generated at 2026-10-24 22:59:54.501208
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'user', 'alice')
    lookup.cp.set('test', 'user_admin', 'bob')
    lookup.cp.set('test', 'host', 'localhost')

    # Retrieve an existing key.
    assert lookup.get_value('user', 'test', 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'^user', 'test', 'default', True) == [
        'alice',
        'bob',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'test', 'default', True) == []

# Generated at 2026-10-24 23:00:13.338479
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

import pytest

from ansible.errors import AnsibleLookupError


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"""
[integration]
user=alice
user.name=Alice Example
""",
        True,
    )

    lookup = LookupModule()
    lookup._loader = loader

    options = {
        "type": "ini",
        "file": "users.ini",
        "section": "integration",
        "re": False,
        "encoding": "utf-8",
        "default": "not-found",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    # Isolate module_0.run() from Ansible's option and file-search infrastructure.
    monkeypatch.setattr(lookup, "set_options", lambda **kwargs: None)
    monkeypatch.setattr(lookup, "get_options", lambda: options.copy())
    monkeypatch.setattr(
        lookup,
        "find_file_in_search_path",
        lambda variables, subdir, filename: "/mock/path/" + filename,
    )

    assert lookup.run(["user"], variables={}) == ["alice"]
    assert lookup.run(["missing"], variables={}) == ["not-found"]

    loader._get_file_contents.assert_called_with("/mock/path/users.ini")


def test_LookupModule_run_regexp(monkeypatch):
    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"""
[integration]
user=alice
user.name=Alice Example
group=developers
""",
        True,
    )

    lookup = LookupModule()
    lookup._loader = loader

    options = {
        "type": "ini",
        "file": "users.ini",
        "section": "integration",
        "re": True,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    monkeypatch.setattr(lookup, "set_options", lambda **kwargs: None)
    monkeypatch.setattr(lookup, "get_options", lambda: options.copy())
    monkeypatch.setattr(
        lookup,
        "find_file_in_search_path",
        lambda variables, subdir, filename: "/mock/path/" + filename,
    )

    assert lookup.run([r"^user"], variables={}) == [
        "alice",
        "Alice Example",
    ]


def test_LookupModule_run_missing_section(monkeypatch):
    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"""
[integration]
user=alice
""",
        True,
    )

    lookup = LookupModule()
    lookup._loader = loader

    options = {
        "type": "ini",
        "file": "users.ini",
        "section": "production",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    monkeypatch.setattr(lookup, "set_options", lambda **kwargs: None)
    monkeypatch.setattr(lookup, "get_options", lambda: options.copy())
    monkeypatch.setattr(
        lookup,
        "find_file_in_search_path",
        lambda variables, subdir, filename: "/mock/path/" + filename,
    )

    with pytest.raises(
        AnsibleLookupError,
        match=r"No section 'production' in users\.ini",
    ):
        lookup.run(["user"], variables={})

# Generated at 2026-10-24 23:00:28.032238
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import Mock

    variables = {'inventory_hostname': 'test-host'}
    loader = Mock()
    loader._get_file_contents.return_value = (
        b'[integration]\nuser=alice\n',
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = Mock()
    lookup.get_options = Mock(return_value={
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
    lookup.find_file_in_search_path = Mock(
        return_value='/tmp/users.ini'
    )

    result = lookup.run(
        ['user'],
        variables=variables,
        section='integration',
    )

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={'section': 'integration'},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        'files',
        'users.ini',
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 23:00:43.980575
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class DummyLoader:
        def __init__(self):
            self.requested_path = None

        def _get_file_contents(self, path):
            self.requested_path = path
            return b"[global]\nusername=test_user\n", True

    options = {
        "allow_no_value": False,
        "allow_none": False,
        "case_sensitive": False,
        "file": "ansible.ini",
        "type": "ini",
        "section": "global",
        "encoding": "utf-8",
        "default": "",
        "re": False,
    }

    loader = DummyLoader()
    lookup = LookupModule(loader=loader)

    # Isolate module_0.run() from Ansible's plugin option and file-discovery machinery.
    lookup.set_options = lambda **kwargs: None
    lookup.get_options = lambda: options.copy()
    lookup.find_file_in_search_path = (
        lambda variables, subdir, filename: "/tmp/ansible.ini"
    )

    result = lookup.run(["username"], variables={})

    assert result == ["test_user"]
    assert loader.requested_path == "/tmp/ansible.ini"

# Generated at 2026-10-24 23:00:53.786158
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('example')
    lookup.cp.set('example', 'user', 'alice')
    lookup.cp.set('example', 'user_name', 'Alice Smith')
    lookup.cp.set('example', 'role', 'admin')

    # Retrieve an existing key.
    assert lookup.get_value('user', 'example', '', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'example', 'fallback', False) == 'fallback'

    # Retrieve all values whose keys match a regular expression.
    assert lookup.get_value(r'^user', 'example', '', True) == [
        'alice',
        'Alice Smith',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'example', '', True) == []

# Generated at 2026-10-24 23:01:03.616111
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

    result = lookup.run(['user'], variables={})

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(
        var_options={},
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {},
        'files',
        'users.ini',
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 23:01:24.711425
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[integration]\n"
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
        "section": "integration",
        "type": "ini",
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/mock/files/users.ini"
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
    loader._get_file_contents.assert_called_once_with(
        "/mock/files/users.ini"
    )

# Generated at 2026-10-24 23:01:34.336027
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:01:44.677789
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:01:54.303709
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 23:02:14.478256
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    variables = {'inventory_hostname': 'test-host'}
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

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b'[integration]\n'
        b'user = alice\n',
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value='/virtual/files/users.ini'
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
    loader._get_file_contents.assert_called_once_with(
        '/virtual/files/users.ini'
    )

# Generated at 2026-10-24 23:02:22.977576
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        u"""
[test_section]
username=alice
user_id=42
hostname=example.com
"""
    ))

    # Retrieve an existing key.
    assert lookup.get_value(
        'username', 'test_section', 'default', False
    ) == 'alice'

    # Return the default when the key does not exist.
    assert lookup.get_value(
        'missing_key', 'test_section', 'default', False
    ) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(
        r'^user', 'test_section', 'default', True
    ) == ['alice', '42']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'^missing', 'test_section', 'default', True
    ) == []

# Generated at 2026-10-24 23:02:32.500135
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'foo', 'bar')
    lookup.cp.set('test', 'foobar', 'baz')

    # Retrieve an existing key.
    assert lookup.get_value('foo', 'test', 'default', False) == 'bar'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all matching values when the key is a regular expression.
    values = lookup.get_value(r'^foo', 'test', 'default', True)
    assert sorted(values) == ['bar', 'baz']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'test', 'default', True) == []

# Generated at 2026-10-24 23:02:42.189337
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:02:51.237319
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:03:00.658921
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 23:03:07.110452
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_file(StringIO(
        "[example]\n"
        "username=alice\n"
        "user_id=42\n"
        "enabled=true\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value("username", "example", "", False) == "alice"

    # Return the supplied default for a missing key.
    assert lookup.get_value("missing", "example", "fallback", False) == "fallback"

    # Retrieve all values whose keys match a regular expression.
    assert lookup.get_value(r"^user", "example", "", True) == ["alice", "42"]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r"^missing$", "example", "", True) == []

# Generated at 2026-10-24 23:03:21.551056
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"[integration]\n"
        b"user=alice\n"
        b"host=example.com\n",
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
        "section": "integration",
        "encoding": "utf-8",
        "default": "",
        "re": False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value="/mock/path/users.ini"
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
        "/mock/path/users.ini"
    )

# Generated at 2026-10-24 23:03:31.276265
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'username', 'alice')
    lookup.cp.set('test', 'user_id', '42')
    lookup.cp.set('test', 'enabled', 'true')

    # Retrieve an existing key.
    assert lookup.get_value('username', 'test', 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'^user', 'test', 'default', True) == ['alice', '42']

# Generated at 2026-10-24 23:03:41.619844
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'username', 'alice')
    lookup.cp.set('test', 'user_id', '42')
    lookup.cp.set('test', 'enabled', 'true')

    # Retrieve an existing key.
    assert lookup.get_value('username', 'test', 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'^user', 'test', 'default', True) == ['alice', '42']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing', 'test', 'default', True) == []

# Generated at 2026-10-24 23:03:54.220728
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

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

    lookup.set_options = Mock()
    lookup.get_options = Mock(return_value=options)
    lookup.find_file_in_search_path = Mock(return_value='/tmp/users.ini')

    lookup._loader = Mock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\n'
        b'user=alice\n',
        True,
    )

    result = lookup.run(['user'], variables={})

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(var_options={}, direct={})
    lookup.find_file_in_search_path.assert_called_once_with(
        {}, 'files', 'users.ini'
    )
    lookup._loader._get_file_contents.assert_called_once_with(
        '/tmp/users.ini'
    )

# Generated at 2026-10-24 23:03:57.661454
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:04:00.078379
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:04:02.495593
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:04:04.914760
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:04:22.376183
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:04:32.003812
# Unit test for method run of class LookupModule