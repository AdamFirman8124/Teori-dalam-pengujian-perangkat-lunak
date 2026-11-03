

# Generated at 2026-11-01 23:50:02.079475
# Unit test for method run of class LookupModule

# Generated at 2026-11-01 23:51:10.472722
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.ini import LookupModule

    ini_content = u"[global]\nkey1 = value1\nkey2 = value2\n[section1]\nuser = alice\n"

    class FakeLoader(object):
        def _get_file_contents(self, path):
            return (ini_content.encode('utf-8'), False)

    lookup = LookupModule()
    lookup._loader = FakeLoader()
    lookup.set_options = lambda var_options=None, direct=None: None

    options = {
        'type': 'ini',
        'file': 'test.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    }
    lookup.get_options = lambda: options
    lookup.find_file_in_search_path = lambda variables, subdir, fname: '/fake/path/test.ini'

    result = lookup.run(['key1'], variables=None)
    assert result == ['value1']

    result = lookup.run(['nonexistent'], variables=None)
    assert result == ['']

    options['re'] = True
    result = lookup.run(['key.*'], variables=None)
    assert sorted(result) == ['value1', 'value2']

# Generated at 2026-11-01 23:52:18.776400
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.plugins.lookup.ini import LookupModule
    from ansible.errors import AnsibleLookupError

    # Sample ini content
    ini_content = u"""
[global]
key1=value1
key2=value2

[integration]
user=yannig
password=secret

[section1]
foo=bar
baz=qux
"""

    def _create_lookup(ini_data=ini_content, options_overrides=None):
        """Helper to create a mocked LookupModule."""
        lookup = LookupModule()
        lookup._loader = MagicMock()
        lookup._loader._get_file_contents.return_value = (
            ini_data.encode('utf-8'), False)

        mock_get_options = {
            'file': 'ansible.ini',
            'section': 'global',
            'type': 'ini',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        if options_overrides:
            mock_get_options.update(options_overrides)

        lookup.set_options = MagicMock()
        lookup.get_options = MagicMock(return_value=mock_get_options)
        lookup.find_file_in_search_path = MagicMock(
            return_value='/fake/path/ansible.ini')
        return lookup

    # Test simple lookup in default section
    lookup = _create_lookup()
    result = lookup.run(['key1'])
    assert result == ['value1']

    # Test lookup with specific section
    lookup = _create_lookup()
    result = lookup.run(['user'], variables={},
                        section='integration', file='users.ini')
    assert result == ['yannig']

    # Test non-existent key returns default
    lookup = _create_lookup()
    result = lookup.run(['nonexistent'])
    assert result == ['']

    # Test non-existent key with custom default
    lookup = _create_lookup(
        options_overrides={'default': 'my_default'})
    result = lookup.run(['nonexistent'])
    assert result == ['my_default']

    # Test regexp lookup
    lookup = _create_lookup(
        options_overrides={'section': 'section1', 're': True})
    result = lookup.run(['f.*'])
    assert result == ['bar']

    # Test regexp matching all keys in section
    lookup = _create_lookup(
        options_overrides={'section': 'section1', 're': True})
    result = lookup.run(['.*'])
    assert sorted(result) == ['bar', 'qux']

    # Test multiple terms
    lookup = _create_lookup()
    result = lookup.run(['key1', 'key2'])
    assert result == ['value1', 'value2']

    # Test missing section raises error
    lookup = _create_lookup(
        options_overrides={'section': 'no_such_section'})
    try:
        lookup.run(['key1'])
    except AnsibleLookupError as e:
        assert "No section 'no_such_section'" in str(e)
    else:
        raise AssertionError("Expected AnsibleLookupError")

    # Test properties type
    props_content = u"user.name=john\ndb.port=3306\n"
    lookup = _create_lookup(ini_data=props_content,
                            options_overrides={
                                'type': 'properties',
                                'section': 'java_properties'})
    result = lookup.run(['user.name'])
    assert result == ['john']

    # Test inline key-value style parameters
    lookup = _create_lookup()
    result = lookup.run(['user section=integration file=users.ini'])
    assert result == ['yannig']

    # Test case sensitive option
    cs_content = u"[global]\nKey1=value_lower\nkey1=value_upper\n"
    lookup = _create_lookup(ini_data=cs_content,
                            options_overrides={'case_sensitive': True})
    result = lookup.run(['Key1'])
    assert result == ['value_lower']

    # Test duplicate option raises AnsibleLookupError
    dup_content = u"[global]\nkey1=a\nkey1=b\n"
    lookup = _create_lookup(ini_data=dup_content)
    try:
        lookup.run(['key1'])
    except AnsibleLookupError as e:
        assert 'Duplicate option' in str(e)
    else:
        raise AssertionError("Expected AnsibleLookupError")

    # Test allow_no_value
    novalue_content = u"[mysqld]\nuser\nport=3306\n"
    lookup = _create_lookup(
        ini_data=novalue_content,
        options_overrides={'section': 'mysqld',
                           'allow_no_value': True})
    result = lookup.run(['port'])
    assert result == ['3306']

# Generated at 2026-11-01 23:56:02.214730
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock

    lookup = LookupModule()

    options = {
        '_terms': 'hostname',
        'type': 'ini',
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    }

    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=options)
    lookup.find_file_in_search_path = MagicMock(return_value='/fake/path/ansible.ini')

    fake_loader = MagicMock()
    fake_loader._get_file_contents.return_value = (
        b'[global]\nhostname = localhost\nport = 8080\n', False)
    lookup._loader = fake_loader

    # Simple ini lookup
    result = lookup.run(['hostname'], variables=None)
    assert result == ['localhost']
    lookup.find_file_in_search_path.assert_called_once_with(None, 'files', 'ansible.ini')
    fake_loader._get_file_contents.assert_called_once_with('/fake/path/ansible.ini')

    # Missing key falls back to default value
    result = lookup.run(['nonexistent'], variables=None)
    assert result == ['']

    # Key present in another section raises AnsibleLookupError
    options['section'] = 'does_not_exist'
    try:
        lookup.run(['hostname'], variables=None)
        raised = False
    except Exception:
        raised = True
    assert raised
    options['section'] = 'global'

    # Java properties style file
    options['type'] = 'properties'
    options['file'] = 'app.properties'
    options['_terms'] = 'key.name'
    lookup.find_file_in_search_path.reset_mock()
    fake_loader._get_file_contents.return_value = (b'key.name=value.name\n', False)

    result = lookup.run(['key.name'], variables=None)
    assert result == ['value.name']
    lookup.find_file_in_search_path.assert_called_once_with(None, 'files', 'app.properties')

    # Multiple keys retrieved via regexp
    options['type'] = 'ini'
    options['re'] = True
    options['_terms'] = 'host.*'
    fake_loader._get_file_contents.return_value = (
        b'[global]\nhostname = localhost\nhosts = all\nother = x\n', False)

    result = lookup.run(['host.*'], variables=None)
    assert result == ['localhost', 'all']