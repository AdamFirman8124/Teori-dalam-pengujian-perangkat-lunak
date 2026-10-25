

# Generated at 2026-10-24 22:41:31.335810
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule.__new__(LookupModule)


# Generated at 2026-10-24 22:41:34.000659
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:41:36.654541
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:41:47.837445
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    lookup.set_options = Mock()
    lookup.get_options = Mock(return_value={
        'allow_no_value': False,
        'case_sensitive': False,
        'file': 'users.ini',
        'type': 'ini',
        'section': 'integration',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    })
    lookup.find_file_in_search_path = Mock(return_value='/tmp/users.ini')
    lookup._loader = Mock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\nuser=integration_user\n',
        True,
    )

    result = lookup.run(['user'], variables={'inventory_hostname': 'localhost'})

    assert result == ['integration_user']
    lookup.set_options.assert_called_once_with(
        var_options={'inventory_hostname': 'localhost'},
        direct={},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        {'inventory_hostname': 'localhost'},
        'files',
        'users.ini',
    )
    lookup._loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 22:41:56.321422
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-24 22:42:11.784221
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(
        u"""
[application]
host = localhost
port = 8080
database.name = example
database.user = admin
"""
    ))

    # Retrieve an existing key.
    assert lookup.get_value(
        'host', 'application', 'default', False
    ) == 'localhost'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value(
        'missing', 'application', 'fallback', False
    ) == 'fallback'

    # Retrieve all values whose keys match a regular expression.
    assert sorted(lookup.get_value(
        r'^database\.', 'application', 'unused', True
    )) == ['admin', 'example']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'^missing\.', 'application', 'fallback', True
    ) == []

# Generated at 2026-10-24 22:42:14.205503
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:42:16.626182
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:42:19.044614
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:42:29.007305
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

# Generated at 2026-10-24 22:42:50.706952
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {'inventory_hostname': 'test-host'}

    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b'[global]\n'
        b'user = alice\n',
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
        'section': 'global',
        'type': 'ini',
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/fake/path/users.ini'
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
        '/fake/path/users.ini'
    )

# Generated at 2026-10-24 22:43:04.015307
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:43:12.303281
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 22:43:22.031582
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
        'type': 'ini',
        'file': 'users.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
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
    loader._get_file_contents.assert_called_once_with(
        '/tmp/users.ini'
    )

# Generated at 2026-10-24 22:43:31.535887
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    config = StringIO(
        u"[application]\n"
        u"user=alice\n"
        u"db_host=localhost\n"
        u"db_port=5432\n"
    )
    lookup.cp.readfp(config)

    # Retrieve an existing key.
    assert lookup.get_value("user", "application", "", False) == "alice"

    # Return the supplied default when the key does not exist.
    assert lookup.get_value(
        "missing", "application", "default-value", False
    ) == "default-value"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(
        r"^db_", "application", "", True
    ) == ["localhost", "5432"]

    # A missing section is propagated to the caller.
    try:
        lookup.get_value("user", "missing_section", "", False)
    except configparser.NoSectionError:
        pass
    else:
        raise AssertionError("Expected configparser.NoSectionError")

# Generated at 2026-10-24 22:43:41.281285
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    config = StringIO(
        u"""
[test_section]
username = alice
user_id = 42
enabled = true
"""
    )
    lookup.cp.readfp(config)

    # Retrieve an existing key.
    assert lookup.get_value(
        'username', 'test_section', 'default_value', False
    ) == 'alice'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value(
        'missing_key', 'test_section', 'default_value', False
    ) == 'default_value'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(
        r'^user', 'test_section', 'default_value', True
    ) == ['alice', '42']

    # A missing section should propagate NoSectionError.
    try:
        lookup.get_value('username', 'missing_section', 'default_value', False)
    except configparser.NoSectionError:
        pass
    else:
        raise AssertionError('Expected configparser.NoSectionError')

# Generated at 2026-10-24 22:43:52.854499
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('example')
    lookup.cp.set('example', 'username', 'alice')
    lookup.cp.set('example', 'user_id', '42')
    lookup.cp.set('example', 'enabled', 'true')

    # Retrieve an existing key.
    assert lookup.get_value('username', 'example', 'default', False) == 'alice'

    # Return the default for a missing key.
    assert lookup.get_value('missing', 'example', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    values = lookup.get_value(r'^user', 'example', 'default', True)
    assert sorted(values) == ['42', 'alice']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'example', 'default', True) == []

    # A missing section is propagated to the caller.
    try:
        lookup.get_value('username', 'missing_section', 'default', False)
    except configparser.NoSectionError:
        pass
    else:
        raise AssertionError('Expected configparser.NoSectionError')

# Generated at 2026-10-24 22:44:04.222559
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

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all matching values when the key is a regular expression.
    values = lookup.get_value(r'^user', 'test', 'default', True)
    assert sorted(values) == ['42', 'alice']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing', 'test', 'default', True) == []

# Generated at 2026-10-24 22:44:14.562629
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')

    lookup.cp.set('test', 'user', 'alice')
    lookup.cp.set('test', 'user_admin', 'bob')
    lookup.cp.set('test', 'group', 'developers')

    # Retrieve an existing key.
    assert lookup.get_value('user', 'test', 'default', False) == 'alice'

    # Return the default when the key does not exist.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'^user', 'test', 'default', True) == [
        'alice',
        'bob',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'test', 'default', True) == []

# Generated at 2026-10-24 22:44:30.845617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    lookup = LookupModule()
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b"[global]\nusername=ansible\n",
        True,
    )

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

    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(
        return_value="/mock/path/ansible.ini"
    )

    variables = {"inventory_hostname": "localhost"}

    result = lookup.run(
        ["username"],
        variables=variables,
        file="ansible.ini",
        section="global",
    )

    assert result == ["ansible"]

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={"file": "ansible.ini", "section": "global"},
    )
    lookup.find_file_in_search_path.assert_called_once_with(
        variables,
        "files",
        "ansible.ini",
    )
    lookup._loader._get_file_contents.assert_called_once_with(
        "/mock/path/ansible.ini"
    )

# Generated at 2026-10-24 22:44:41.083197
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('integration')
    lookup.cp.set('integration', 'user', 'alice')
    lookup.cp.set('integration', 'username', 'alice_admin')
    lookup.cp.set('integration', 'host', 'example.com')

    # Retrieve an existing key.
    assert lookup.get_value(
        'user', 'integration', 'default-value', False
    ) == 'alice'

    # Return the default when the key does not exist.
    assert lookup.get_value(
        'missing', 'integration', 'default-value', False
    ) == 'default-value'

    # Retrieve all values whose keys match a regular expression.
    assert sorted(lookup.get_value(
        r'^user', 'integration', 'default-value', True
    )) == ['alice', 'alice_admin']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'^missing$', 'integration', 'default-value', True
    ) == []

# Generated at 2026-10-24 22:44:59.312281
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
        'type': 'ini',
        'file': 'users.ini',
        'section': 'integration',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    })
    lookup.find_file_in_search_path = Mock(return_value='/tmp/users.ini')

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

# Generated at 2026-10-24 22:45:09.047604
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    lookup.cp.add_section('test')
    lookup.cp.set('test', 'user', 'alice')
    lookup.cp.set('test', 'user_name', 'Alice Smith')
    lookup.cp.set('test', 'host', 'localhost')

    # Retrieve an existing key.
    assert lookup.get_value('user', 'test', 'default', False) == 'alice'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all matching values when the key is a regular expression.
    assert lookup.get_value(r'^user', 'test', 'default', True) == [
        'alice',
        'Alice Smith',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'^missing$', 'test', 'default', True) == []

# Generated at 2026-10-24 22:45:18.850511
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    config = StringIO(
        u"""
[global]
name = ansible
user1 = alice
user2 = bob
other = value
"""
    )
    lookup.cp.readfp(config)

    # Existing key
    assert lookup.get_value('name', 'global', 'default', False) == 'ansible'

    # Missing key returns the supplied default
    assert lookup.get_value('missing', 'global', 'default', False) == 'default'

    # Regular-expression lookup returns all matching values
    assert sorted(
        lookup.get_value(r'^user\d+$', 'global', 'default', True)
    ) == ['alice', 'bob']

    # A regular expression with no matches returns an empty list
    assert lookup.get_value(r'^missing', 'global', 'default', True) == []

# Generated at 2026-10-24 22:45:21.274073
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:45:23.694556
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:45:26.416109
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 22:45:36.791396
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

    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(return_value='/tmp/users.ini')
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[integration]\nuser=alice\n',
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

# Generated at 2026-10-24 22:45:52.765377
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    loader = MagicMock()
    loader._get_file_contents.return_value = (
        b"""
[integration]
user=alice
enabled=true
""",
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
        return_value='/fake/path/users.ini'
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
    loader._get_file_contents.assert_called_once_with(
        '/fake/path/users.ini'
    )

# Generated at 2026-10-24 22:46:03.505990
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
        return_value="/tmp/users.ini"
    )

    result = lookup.run(["username"], variables={})

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

# Generated at 2026-10-24 22:46:25.430247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    options = {
        'type': 'ini',
        'file': 'test.ini',
        'section': 'application',
        're': False,
        'encoding': 'utf-8',
        'default': 'fallback',
        'case_sensitive': False,
        'allow_no_value': False,
    }

    ini_contents = b"""
[application]
user = alice
db_host = localhost
db_port = 5432
"""

    loader = MagicMock()
    loader._get_file_contents.return_value = (ini_contents, True)

    lookup = LookupModule(loader=loader)
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(side_effect=lambda: options.copy())
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/test.ini'
    )

    # Regular key lookup and missing-key default.
    result = lookup.run(
        ['user', 'missing'],
        variables={'inventory_hostname': 'test-host'},
    )

    assert result == ['alice', 'fallback']

    # Regular-expression lookup returns every matching value.
    options['re'] = True
    result = lookup.run(
        [r'^db_'],
        variables={'inventory_hostname': 'test-host'},
    )

    assert result == ['localhost', '5432']

    lookup.find_file_in_search_path.assert_called_with(
        {'inventory_hostname': 'test-host'},
        'files',
        'test.ini',
    )

# Generated at 2026-10-24 22:46:35.669816
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:46:44.783070
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 22:47:22.017390
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch


# Generated at 2026-10-24 22:47:33.388765
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test_section')
    lookup.cp.set('test_section', 'key1', 'value1')
    lookup.cp.set('test_section', 'user_admin', 'admin')
    lookup.cp.set('test_section', 'user_guest', 'guest')

    # Retrieve an existing key.
    assert lookup.get_value(
        'key1', 'test_section', 'default', False
    ) == 'value1'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value(
        'missing_key', 'test_section', 'default', False
    ) == 'default'

    # Retrieve all matching values when the key is a regular expression.
    assert sorted(lookup.get_value(
        r'user_.*', 'test_section', 'default', True
    )) == ['admin', 'guest']

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(
        r'unknown_.*', 'test_section', 'default', True
    ) == []

# Generated at 2026-10-24 22:47:44.384062
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    section = 'test_section'
    lookup.cp.add_section(section)
    lookup.cp.set(section, 'username', 'alice')
    lookup.cp.set(section, 'user_id', '42')
    lookup.cp.set(section, 'hostname', 'example.com')

    # Retrieve an existing key.
    assert lookup.get_value('username', section, 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', section, 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'user.*', section, 'default', True) == [
        'alice',
        '42',
    ]

    # A regular expression with no matches returns an empty list.
    assert lookup.get_value(r'database.*', section, 'default', True) == []

# Generated at 2026-10-24 22:47:55.133263
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    config = StringIO(
        "[global]\n"
        "username=alice\n"
        "user_email=alice@example.com\n"
        "server=localhost\n"
    )
    lookup.cp.readfp(config)

    # Retrieve an existing key.
    assert lookup.get_value("username", "global", "default", False) == "alice"

    # Return the supplied default when the key does not exist.
    assert lookup.get_value("missing", "global", "default", False) == "default"

    # Retrieve all matching values when the key is a regular expression.
    assert lookup.get_value(r"user.*", "global", "default", True) == [
        "alice",
        "alice@example.com",
    ]

# Generated at 2026-10-24 22:48:05.270159
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:48:07.690309
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:48:19.883129
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:48:39.985348
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:48:49.507181
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:48:58.109463
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:49:08.048350
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:49:20.919043
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:49:29.954699
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:49:39.888035
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
    lookup._loader._get_file_contents.assert_called_once_with(
        '/tmp/users.ini'
    )

# Generated at 2026-10-24 22:49:55.760956
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    loader = Mock()
    loader._get_file_contents.return_value = (
        b"[global]\n"
        b"user=alice\n",
        True,
    )

    lookup = LookupModule(loader=loader)
    lookup.set_options = Mock()
    lookup.get_options = Mock(return_value={
        "allow_no_value": False,
        "case_sensitive": False,
        "default": "",
        "encoding": "utf-8",
        "file": "users.ini",
        "re": False,
        "section": "global",
        "type": "ini",
    })
    lookup.find_file_in_search_path = Mock(
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

# Generated at 2026-10-24 22:50:05.938237
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'first_key', 'first_value')
    lookup.cp.set('test', 'second_key', 'second_value')

    assert lookup.get_value('first_key', 'test', 'default', False) == 'first_value'
    assert lookup.get_value('missing_key', 'test', 'default', False) == 'default'
    assert lookup.get_value(r'.*_key$', 'test', 'default', True) == [
        'first_value',
        'second_value',
    ]
    assert lookup.get_value(r'^missing', 'test', 'default', True) == []

# Generated at 2026-10-24 22:50:14.294587
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'username', 'alice')
    lookup.cp.set('test', 'user_email', 'alice@example.com')
    lookup.cp.set('test', 'hostname', 'example.com')

    # Retrieve an existing key.
    assert lookup.get_value('username', 'test', 'default', False) == 'alice'

    # Return the supplied default when the key does not exist.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r'^user', 'test', 'default', True) == [
        'alice',
        'alice@example.com',
    ]

# Generated at 2026-10-24 22:50:22.691424
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('test')
    lookup.cp.set('test', 'user', 'alice')
    lookup.cp.set('test', 'user_name', 'Alice Smith')
    lookup.cp.set('test', 'group', 'admins')

    # Retrieve an existing key.
    assert lookup.get_value('user', 'test', 'default', False) == 'alice'

    # Return the supplied default for a missing key.
    assert lookup.get_value('missing', 'test', 'default', False) == 'default'

    # Retrieve all values whose keys match a regular expression.
    values = lookup.get_value(r'^user', 'test', 'default', True)
    assert sorted(values) == ['Alice Smith', 'alice']

# Generated at 2026-10-24 22:50:37.949099
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value={
        'allow_no_value': False,
        'case_sensitive': False,
        'file': 'ansible.ini',
        'type': 'ini',
        'section': 'global',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    })
    lookup.find_file_in_search_path = MagicMock(
        return_value='/tmp/ansible.ini'
    )
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (
        b'[global]\nusername=alice\n',
        True,
    )

    variables = {'inventory_hostname': 'localhost'}

    result = lookup.run(['username'], variables=variables)

    assert result == ['alice']
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

# Generated at 2026-10-24 22:50:49.930088
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
        'allow_no_value': False,
        'case_sensitive': False,
        'file': 'users.ini',
        'type': 'ini',
        'section': 'integration',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    })
    lookup.find_file_in_search_path = Mock(return_value='/tmp/users.ini')

    result = lookup.run(['user'], variables={})

    assert result == ['alice']
    lookup.set_options.assert_called_once_with(var_options={}, direct={})
    lookup.find_file_in_search_path.assert_called_once_with(
        {}, 'files', 'users.ini'
    )
    loader._get_file_contents.assert_called_once_with('/tmp/users.ini')

# Generated at 2026-10-24 22:51:05.597192
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:51:15.222568
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock


# Generated at 2026-10-24 22:51:17.745183
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:51:20.163037
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 22:51:22.676592
# Unit test for method run of class LookupModule