

# Generated at 2026-11-02 06:49:33.888878
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.module_utils.six.moves import configparser

    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('global')
    lookup.cp.set('global', 'key1', 'value1')
    lookup.cp.set('global', 'key2', 'value2')

    # Simple key lookups
    assert lookup.get_value('key1', 'global', 'dflt', False) == 'value1'
    assert lookup.get_value('key2', 'global', 'dflt', False) == 'value2'

    # Missing key returns the default value
    assert lookup.get_value('missing_key', 'global', 'dflt', False) == 'dflt'
    assert lookup.get_value('missing_key', 'global', '', False) == ''

    # Regexp lookup returns all matching values in the section
    assert sorted(lookup.get_value('key.*', 'global', 'dflt', True)) == ['value1', 'value2']

    # Regexp matching a single key
    assert lookup.get_value('key1', 'global', 'dflt', True) == ['value1']

    # Regexp with no matches returns an empty list
    assert lookup.get_value('nomatch.*', 'global', 'dflt', True) == []
# nonce:61bea692

# Generated at 2026-11-02 06:50:04.195577
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from io import StringIO

    from ansible.module_utils.six.moves import configparser
    from ansible.module_utils._text import to_native
    from ansible.plugins.lookup.ini import LookupModule

    lookup = LookupModule()

    # Populate a ConfigParser with sample data (default: keys are lowercased)
    lookup.cp = configparser.ConfigParser()
    config = StringIO(u'[section1]\nkey1 = value1\nkey2 = value2\nKey3 = value3\n'
                      u'[section2]\nother = something\n')
    lookup.cp.readfp(config)

    # Existing keys return their values
    assert lookup.get_value('key1', 'section1', 'default', False) == 'value1'
    assert lookup.get_value('key2', 'section1', 'default', False) == 'value2'

    # Missing key returns the provided default
    assert lookup.get_value('missing', 'section1', 'default_value', False) == 'default_value'
    assert lookup.get_value('missing', 'section1', '', False) == ''

    # Value from a different section
    assert lookup.get_value('other', 'section2', 'default', False) == 'something'

    # Regexp lookups return a list of all matching values
    assert sorted(lookup.get_value('key[12]', 'section1', 'default', True)) == ['value1', 'value2']

    # Regexp matching everything (Key3 was lowercased by default optionxform)
    assert sorted(lookup.get_value('.*', 'section1', 'default', True)) == ['value1', 'value2', 'value3']

    # Regexp with no match returns an empty list (default is ignored for regexp)
    assert lookup.get_value('nomatch', 'section1', 'default', True) == []

    # Missing section raises NoSectionError (run() is responsible for handling it)
    try:
        lookup.get_value('key1', 'nosection', 'default', False)
        assert False, 'expected configparser.NoSectionError'
    except configparser.NoSectionError:
        pass

    try:
        lookup.get_value('key1', 'nosection', 'default', True)
        assert False, 'expected configparser.NoSectionError'
    except configparser.NoSectionError:
        pass

    # Case sensitive parsing preserves original key case
    lookup.cp = configparser.ConfigParser()
    lookup.cp.optionxform = to_native
    config = StringIO(u'[section1]\nKey3 = value3\n')
    lookup.cp.readfp(config)
    assert lookup.get_value('Key3', 'section1', 'default', False) == 'value3'
    assert lookup.get_value('key3', 'section1', 'fallback', False) == 'fallback'

# Generated at 2026-11-02 06:51:33.601224
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import MagicMock, patch

    from ansible.errors import AnsibleLookupError
    from ansible.plugins.lookup.ini import LookupModule

    def _make_lookup(file_content=b'[global]\nkey=value\n', options=None):
        lookup = LookupModule()
        lookup._loader = MagicMock()

        base_options = {
            'type': 'ini',
            'file': 'ansible.ini',
            'section': 'global',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        if options:
            base_options.update(options)

        lookup.set_options = MagicMock()
        lookup.get_options = MagicMock(return_value=dict(base_options))
        lookup.find_file_in_search_path = MagicMock(return_value='/fake/ansible.ini')
        lookup._loader._get_file_contents = MagicMock(return_value=(file_content, False))
        return lookup

    # Simple ini lookup
    lookup = _make_lookup(b'[global]\nkey=value\n')
    assert lookup.run(['key']) == ['value']

    # Multiple terms
    lookup = _make_lookup(b'[global]\nkey=value\nkey2=value2\n')
    assert lookup.run(['key', 'key2']) == ['value', 'value2']

    # Regexp lookup returns all matching keys in the section
    lookup = _make_lookup(b'[global]\nfoo=bar\nfizz=buzz\nother=1\n', options={'re': True})
    assert sorted(lookup.run(['f.*'])) == ['bar', 'buzz']

    # Missing key returns default (empty string by default)
    lookup = _make_lookup(b'[global]\nkey=value\n')
    assert lookup.run(['missing']) == ['']

    # Missing key returns custom default
    lookup = _make_lookup(b'[global]\nkey=value\n', options={'default': 'dflt'})
    assert lookup.run(['missing']) == ['dflt']

    # Java properties type uses implicit [java_properties] section
    lookup = _make_lookup(b'user.name=ansible\n', options={'type': 'properties'})
    assert lookup.run(['user.name']) == ['ansible']

    # Custom section
    lookup = _make_lookup(b'[integration]\nuser=jane\n', options={'section': 'integration'})
    assert lookup.run(['user']) == ['jane']

    # Case sensitive keys
    lookup = _make_lookup(
        b'[global]\nKey=upper\nkey=lower\n',
        options={'case_sensitive': True},
    )
    assert lookup.run(['Key']) == ['upper']
    assert lookup.run(['key']) == ['lower']

    # Missing section raises AnsibleLookupError
    lookup = _make_lookup(b'[other]\nkey=value\n')
    with pytest.raises(AnsibleLookupError) as exc_info:
        lookup.run(['key'])
    assert "No section 'global'" in str(exc_info.value)

    # Duplicate option raises AnsibleLookupError
    lookup = _make_lookup(b'[global]\nkey=value\nkey=other\n')
    with pytest.raises(AnsibleLookupError) as exc_info:
        lookup.run(['key'])
    assert 'Duplicate option' in str(exc_info.value)

    # allow_no_value permits keys without '='
    lookup = _make_lookup(
        b'[global]\nflag\nkey=value\n',
        options={'allow_no_value': True},
    )
    assert lookup.run(['key']) == ['value']
    assert lookup.run(['flag']) == [None]

    # Custom encoding is honored
    lookup = _make_lookup(
        'clé=valeur\n'.encode('latin-1'),
        options={'encoding': 'latin-1'},
    )
    assert lookup.run(['clé']) == ['valeur']

# Generated at 2026-11-02 06:52:08.524699
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupBase)
    assert callable(lookup.run)
    assert callable(lookup.get_value)

# Generated at 2026-11-02 06:53:40.809493
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import pytest
    from ansible.module_utils.six.moves import configparser
    from ansible.plugins.lookup.ini import LookupModule

    lookup = LookupModule()

    # Build a ConfigParser with test data
    cp = configparser.ConfigParser()
    cp.read_string(u"""
[global]
key=value
key with spaces=value with spaces

[integration]
user=yannig
""")
    lookup.cp = cp

    # Simple value retrieval
    assert lookup.get_value('key', 'global', 'dflt', False) == 'value'

    # Key containing spaces
    assert lookup.get_value('key with spaces', 'global', 'dflt', False) == 'value with spaces'

    # Value from a non-default section
    assert lookup.get_value('user', 'integration', 'dflt', False) == 'yannig'

    # Missing key in an existing section -> default value is returned
    assert lookup.get_value('missing_key', 'global', 'dflt', False) == 'dflt'
    assert lookup.get_value('missing_key', 'global', '', False) == ''

    # Missing section -> NoSectionError (handled by run(), not get_value)
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('key', 'unknown_section', 'dflt', False)

    # Regexp based retrieval
    cp2 = configparser.ConfigParser()
    cp2.read_string(u"""
[section1]
foo=1
bar=2
other=3
""")
    lookup.cp = cp2

    # Regexp matching all keys of the section
    assert lookup.get_value('.*', 'section1', 'dflt', True) == ['1', '2', '3']

    # Regexp matching a subset of keys
    assert lookup.get_value('o.*', 'section1', 'dflt', True) == ['3']

    # Regexp matching nothing -> empty list
    assert lookup.get_value('nope.*', 'section1', 'dflt', True) == []

# Generated at 2026-11-02 06:56:19.192605
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.plugins.lookup.ini import LookupModule
    from ansible.module_utils.six.moves import configparser

    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('global')
    lookup.cp.set('global', 'hostname', 'localhost')
    lookup.cp.set('global', 'port', '8080')
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'user', 'admin')
    lookup.cp.set('section1', 'password', 'secret')

    # Simple key lookup returns the value for the given section
    assert lookup.get_value('hostname', 'global', '', False) == 'localhost'
    assert lookup.get_value('user', 'section1', '', False) == 'admin'
    assert lookup.get_value('password', 'section1', '', False) == 'secret'

    # Missing key falls back to the default value
    assert lookup.get_value('unknown', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('unknown', 'global', '', False) == ''

    # Regexp lookup returns all matching values within a section
    values = lookup.get_value('.*', 'section1', '', True)
    assert sorted(values) == ['admin', 'secret']

    values = lookup.get_value('pass.*', 'section1', '', True)
    assert values == ['secret']

    values = lookup.get_value('host', 'global', '', True)
    assert values == ['localhost']

    # Regexp with no matching keys returns an empty list
    values = lookup.get_value('nomatch', 'global', '', True)
    assert values == []

# Generated at 2026-11-02 06:57:43.185213
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    '''Unit test for method get_value of class LookupModule'''
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.readfp(StringIO(u'[global]\nkey1 = value1\nkey2 = value2\n'))

    # Retrieve a single existing value
    assert lookup_module.get_value('key1', 'global', '', False) == 'value1'

    # Missing key in an existing section returns the default value
    assert lookup_module.get_value('missing_key', 'global', 'default_value', False) == 'default_value'

    # Regexp lookup returns every matching value of the section
    assert sorted(lookup_module.get_value('key.', 'global', '', True)) == ['value1', 'value2']

    # Regexp lookup with no match returns an empty list
    assert lookup_module.get_value('nomatch', 'global', '', True) == []

    # A nonexistent section raises configparser.NoSectionError
    with pytest.raises(configparser.NoSectionError):
        lookup_module.get_value('key1', 'nonexistent_section', '', False)