

# Generated at 2022-06-12 20:24:20.469222
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    doc = DocCLI()
    assert doc.get_plugin_metadata('setup')['category'] == 'GATHERING FACTS'

# Generated at 2022-06-12 20:24:26.049440
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    # Test with an empty name
    with pytest.raises(AnsibleError) as exception:
        DocCLI.get_plugin_metadata('')
    assert exception.typename == 'AnsibleError'
    assert exception.value.args[0] == 'name not provided'

    # Test with a non-existent plugin
    with pytest.raises(AnsibleError) as exception:
        DocCLI.get_plugin_metadata('non_existent_plugin')
    assert exception.typename == 'AnsibleError'
    assert exception.value.args[0] == "plugin non_existent_plugin not found"

    # Test with a valid plugin
    doc, plugin_type = DocCLI.get_plugin_metadata('copy')
    assert plugin_type == 'module'
    assert 'module' in doc


# Generated at 2022-06-12 20:24:36.686583
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    # prepare test data
    import pkg_resources
    import os
    import sys
    import json

    try:
        # Raise exception if the module cannot be imported
        pkg_resources.get_distribution('docutils')
    except Exception as e:
        print("Could not import module docutils in test_DocCLI_get_man_text()")
        return

    try:
        # Raise exception if the module cannot be imported
        from docutils import core
    except Exception as e:
        print("Could not import module docutils.core in test_DocCLI_get_man_text()")
        return

    test_data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_data')

# Generated at 2022-06-12 20:24:38.353425
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    assert(DocCLI.format_snippet('{{ foo }}', 'mustache')) == '``{{ foo }}``'

# Generated at 2022-06-12 20:24:40.557935
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    args = ['-t', 'module']
    args.extend(['-l'])
    args.extend(['copy'])
    doc = DocCLI()
    doc.run(args)

# Generated at 2022-06-12 20:24:47.709989
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    from ansible.utils.collection_loader import ns_collection_name, _parse_collection_to_name_and_version
    def test_namespace_from_plugin_filepath(file, expected_collection, expected_plugin_type, expected_plugin_name):
        collection, plugin_type, plugin_name = ns_collection_name(file)
        assert expected_collection == collection
        assert expected_plugin_type == plugin_type
        assert expected_plugin_name == plugin_name
        collection, version = _parse_collection_to_name_and_version(collection)
        assert expected_collection == collection


# Generated at 2022-06-12 20:24:55.117617
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    import os
    import sys
    import unittest

    PLUGIN_PATH = '/Library/Ansible/plugins'
    SAMPLE_FILENAME = 'my_plugin'
    SAMPLE_FILE_EXTENSION = 'py'
    SAMPLE_FILE_PATH = os.path.join(PLUGIN_PATH, SAMPLE_FILENAME + '.' + SAMPLE_FILE_EXTENSION)

    EXISTING_PLUGIN_PATH = os.path.join(PLUGIN_PATH, 'module_utils/fundamental.py')
    NON_EXISTING_PLUGIN_PATH = os.path.join(PLUGIN_PATH, 'module_utils/not_existing_file.py')


# Generated at 2022-06-12 20:25:07.038517
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    try:
        # Required for testing
        from test.support.import_shims import AnsibleRoleModuleDeprecationWarning
    except ImportError:
        # Fall back to old location
        from ansible.utils.import_shims import AnsibleRoleModuleDeprecationWarning

    # Create a stubbed role to test with
    role_stub = AnsibleRoleModuleDeprecationWarning(
        collections=['some_collection'],
        collection_name='some_collection',
        file_name='some_file_name',
        lineno=12345,
        message='This is a test error message',
    )
    # Get the stubbed role
    role = role_stub.get_role()
    # Instantiate an object of the DocCLI class
    doc_cli = DocCLI()
    # Get the role documentation
    role

# Generated at 2022-06-12 20:25:09.462166
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    docs = DocCLI()
    assert type(DocCLI.get_all_plugins_of_type(docs, 'action')) == dict


# Generated at 2022-06-12 20:25:16.560779
# Unit test for function jdump
def test_jdump():
    json_str = '{"key": "value"}'
    json_str_expect = '''{
    "key": "value"
}
'''
    assert json_str_expect == jdump(json.loads(json_str))

    p = {'a': 1, 'b': {'c': 3.0, 'd': True, 'e': [1, 2, 3], 'f': None}}
    p_expect = '''{
    "a": 1,
    "b": {
        "c": 3.0,
        "d": true,
        "e": [
            1,
            2,
            3
        ],
        "f": null
    }
}
'''
    assert p_expect == jdump(p)



# Generated at 2022-06-12 20:27:36.792133
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    # DocCLI.run(args)
    pass


# Generated at 2022-06-12 20:27:37.680385
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    # DocCLI.run(self)
    pass

# Generated at 2022-06-12 20:27:41.899259
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    doc = {
            'filename': 'cloud-tools/roles/role1',
            'entry_points': {
                'main': {
                    'description': ['This role has a main entry point',
                                    'which is invoked by default'],
                    'options': {
                        'role_option': {
                            'description': 'This is a description of my option'
                        }
                    }
                }
            }
    }
    ansible_cli = DocCLI(doc)
    ansible_cli.get_role_man_text('role1', doc)
    return True # no error


# Generated at 2022-06-12 20:27:54.089428
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    '''Test for method get_role_man_text of class DocCLI'''

    # Define input parameters

# Generated at 2022-06-12 20:27:58.414835
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    import ansible.utils.unsafe_proxy
    ansible_DocCLI = DocCLI()
    real_ansible_utils_unsafe_proxy_wrap = ansible.utils.unsafe_proxy.wrap
    def fake_ansible_utils_unsafe_proxy_wrap(name, value, only_strings=False, unsafe_proxy=None):
        return value
    ansible.utils.unsafe_proxy.wrap = fake_ansible_utils_unsafe_proxy_wrap
    args = dict()
    args['type'] = None
    args['path'] = None
    args['version'] = False
    args['help'] = False
    args['formatter'] = 'json'
    args['verbosity'] = 0
    args['force_colored'] = False
    args['no_log'] = False
    args['debug']

# Generated at 2022-06-12 20:28:07.413098
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    test = DocCLI()

# Generated at 2022-06-12 20:28:16.489754
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    def check(result, arg):
        assert DocCLI.format_snippet(arg) == result

    check('\x1b[1;32m$ echo hello\x1b[0m', 'echo hello')
    check('\x1b[1;32m$ echo hello\x1b[0m', 'echo {hello}')
    check('\x1b[1;32m$ echo hello\x1b[0m', 'echo {hello')
    check('\x1b[1;32m$ echo hello\x1b[0m', 'echo hello}')
    check('\x1b[1;32m$ echo hello\x1b[0m', 'echo hello')

# Generated at 2022-06-12 20:28:23.702946
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
	assert DocCLI.namespace_from_plugin_filepath('/bla/bla/bla/windows/powershell/test.ps1') == 'windows.powershell'
	assert DocCLI.namespace_from_plugin_filepath('/bla/bla/bla/windows/ansible_test.ps1') == 'windows'
	assert DocCLI.namespace_from_plugin_filepath('/bla/bla/bla/ansible_test.ps1') == ''


# Generated at 2022-06-12 20:28:29.870767
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    pattern = '^.*_module\.py$'
    if path.exists('/usr/share/ansible'):
        filter_path = ['/usr/share/ansible']
    elif path.exists('/usr/local/share/ansible'):
        filter_path = ['/usr/local/share/ansible']
    else:
        filter_path = None
    DocCLI.find_plugins(BASE_MODULE_PATH, pattern, filter_path=filter_path)

# Generated at 2022-06-12 20:28:34.377422
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    doc = {
        'a': 1,
        'b': ['foo', 'bar'],
        'c': dict(foo=1, bar='baz')
    }

    text = []

    DocCLI.add_fields(text, doc, limit=70, opt_indent=' ' * 4)
    assert text == ['    A: 1', '    B: foo, bar', '    C:\n        BAR: baz\n        FOO: 1']
