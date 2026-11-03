

# Generated at 2026-11-02 00:10:06.517057
# Unit test for method get_value of class LookupModule

# Generated at 2026-11-02 00:11:11.374039
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():from ansible.module_utils.six.moves import configparser


# Generated at 2026-11-02 00:13:06.533509
# Unit test for method run of class LookupModule

# Generated at 2026-11-02 00:13:58.347141
# Unit test for method run of class LookupModule
def test_LookupModule_run():
# nonce:18506ada
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    fd, path = tempfile.mkstemp(suffix='.ini')
    with os.fdopen(fd, 'w') as f:
        f.write('[global]\nkey1=value1\nkey2=value2\n[other]\nfoo=bar\n')

    lookup = LookupModule()
    lookup._loader = type('FakeLoader', (), {})()
    lookup._loader._get_file_contents = lambda p: (open(p, 'rb').read(), False)
    lookup.find_file_in_search_path = lambda variables, kind, fname: path

    options = {'file': path, 'type': 'ini', 'section': 'global', 're': False,
               'encoding': 'utf-8', 'default': '', 'case_sensitive': False,
               'allow_no_value': False, 'allow_none': False}
    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: options

    assert lookup.run(['key1', 'key2'], variables=None) == ['value1', 'value2']
    assert lookup.run(['missing'], variables=None) == ['']

    options['re'] = True
    assert lookup.run(['key.'], variables=None) == ['value1', 'value2']
    options['re'] = False

    options['section'] = 'other'
    assert lookup.run(['foo'], variables=None) == ['bar']
    options['section'] = 'global'

    os.remove(path)

# Generated at 2026-11-02 00:16:00.587638
# Unit test for method run of class LookupModule
def test_LookupModule_run():import os