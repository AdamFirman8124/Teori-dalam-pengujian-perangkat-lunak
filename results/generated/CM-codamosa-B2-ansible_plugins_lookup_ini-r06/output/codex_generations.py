

# Generated at 2026-11-02 18:30:37.993994
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Basic ini content with two sections
    lookup = _make_lookup(
        u"[integration]\n"
        u"user = alice\n"
        u"password = secret\n"
        u"[production]\n"
        u"user = bob\n"
    )

    # Simple key lookup within a section
    assert lookup.get_value('user', 'integration', '', False) == 'alice'
    assert lookup.get_value('password', 'integration', '', False) == 'secret'

    # Same key name in a different section yields that section's value
    assert lookup.get_value('user', 'production', '', False) == 'bob'

    # Missing key falls back to the provided default
    assert lookup.get_value('missing', 'integration', 'fallback', False) == 'fallback'

    # Missing key with empty default returns ''
    assert lookup.get_value('missing', 'integration', '', False) == ''

    # Regexp lookup returns a list of all matching values in the section
    lookup_multi = _make_lookup(
        u"[section1]\n"
        u"key1 = value1\n"
        u"key2 = value2\n"
        u"other = value3\n"
    )
    assert lookup_multi.get_value('key.*', 'section1', '', True) == ['value1', 'value2']
    assert lookup_multi.get_value('.*', 'section1', '', True) == ['value1', 'value2', 'value3']

    # Regexp matching nothing returns an empty list
    assert lookup_multi.get_value('nomatch.*', 'section1', '', True) == []

    # Regexp anchored at the start of the key
    assert lookup_multi.get_value('other', 'section1', '', True) == ['value3']

    # Case-sensitive keys are distinguished when optionxform is disabled
    lookup_cs = _make_lookup(
        u"[sect]\n"
        u"Key = upper\n"
        u"key = lower\n",
        case_sensitive=True
    )
    assert lookup_cs.get_value('Key', 'sect', '', False) == 'upper'
    assert lookup_cs.get_value('key', 'sect', '', False) == 'lower'

    # Case-insensitive (default configparser behavior) collapses duplicates,
    # so only use distinct keys here
    lookup_ci = _make_lookup(
        u"[sect]\n"
        u"Key = upper\n"
    )
    assert lookup_ci.get_value('key', 'sect', '', False) == 'upper'
    assert lookup_ci.get_value('KEY', 'sect', '', False) == 'upper'

    # allow_no_value: key without '=' yields None from cp.get
    lookup_nv = _make_lookup(
        u"[mysqld]\n"
        u"user\n",
        allow_no_value=True
    )
    assert lookup_nv.get_value('user', 'mysqld', 'dflt', False) is None

    # allow_no_value with regexp lookup includes the None value
    assert lookup_nv.get_value('.*', 'mysqld', 'dflt', True) == [None]

# Generated at 2026-11-02 18:33:26.451665
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(u'[global]\nkey=value1\nanother=second value\n'))

    # Simple key lookup in existing section
    assert lookup.get_value('key', 'global', '', False) == 'value1'
    assert lookup.get_value('another', 'global', '', False) == 'second value'

    # Missing key in existing section returns the default
    assert lookup.get_value('missing', 'global', 'default_value', False) == 'default_value'
    assert lookup.get_value('missing', 'global', '', False) == ''

    # Regexp lookups return a list of matching values
    assert lookup.get_value('k.*', 'global', '', True) == ['value1']
    assert lookup.get_value('another', 'global', '', True) == ['second value']
    assert lookup.get_value('.*', 'global', '', True) == ['value1', 'second value']

    # Regexp with no matches returns an empty list
    assert lookup.get_value('nomatch', 'global', '', True) == []

# Generated at 2026-11-02 18:35:32.336777
# Unit test for constructor of class LookupModule
def test_LookupModule():
    '''Test the LookupModule constructor'''
    from ansible.plugins.lookup.ini import LookupModule

    # Instantiate the lookup module
    lookup = LookupModule()

    # Verify the instance is created properly
    assert lookup is not None
    assert isinstance(lookup, LookupModule)

    # Verify default attributes from LookupBase
    assert lookup._loader is not None
    assert lookup._templar is not None
    assert lookup._basedir is not None

    # The configparser should not exist before run() is called
    assert not hasattr(lookup, 'cp')

    # Verify the lookup has the expected methods
    assert callable(lookup.run)
    assert callable(lookup.get_value)