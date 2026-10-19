

# Generated at 2022-06-12 20:24:31.446640
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():

    # remove the key from the context structure (if present)
    context_copy = dict(context={})
    context_copy['display'] = ''  # TODO: implement this test

    # Test 1: passing invalid plugin type
    data = {'type': 'INVALID'}
    assert DocCLI(context_copy=context_copy).display_plugin_list(data) == 'Invalid Plugin Type'

    # Test 2: passing module and not passing display_type
    data = {'type': 'modules'}
    assert 'TestModule' not in DocCLI(context_copy=context_copy).display_plugin_list(data)

    # Test 3: passing module and passing display_type
    data = {'type': 'modules'}
    assert 'TestModule' in DocCLI(context_copy=context_copy).display_plugin_

# Generated at 2022-06-12 20:24:39.928353
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    # simple test case
    if DocCLI.format_snippet(u'module: test', False) == ("module: test", 0, 0):
        return

    # module is not found
    if DocCLI.format_snippet(u'module: test', False) == ("    module: test", 4, 0):
        return

    # comment is not in the snippet
    if DocCLI.format_snippet(u'# this is a comment\nmodule: test', False) == ("    module: test", 4, 1):
        return

    # comment is in the snippet
    if DocCLI.format_snippet(u'# this is a comment\nmodule: test', True) == ("    # this is a comment\n    module: test", 4, 1):
        return

    # comment and changed indent


# Generated at 2022-06-12 20:24:46.839669
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    # Function to convert bytes type to str type
    # Necessary for Python 3.4
    # https://bugs.python.org/issue24368
    if sys.version_info < (3, 5):
        import codecs
        utf8_reader = codecs.getreader('utf-8')
        def u(x):
            return x if isinstance(x, text_type) else utf8_reader(x)[0]
    else:
        def u(x):
            return x


    # Create mock objects

# Generated at 2022-06-12 20:24:47.895184
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    DocCLI.get_plugin_metadata()



# Generated at 2022-06-12 20:24:49.672373
# Unit test for function jdump
def test_jdump():
    assert jdump("{ 'test': 'string' }") == json.dumps("{ 'test': 'string' }")



# Generated at 2022-06-12 20:24:56.336536
# Unit test for method get_role_man_text of class DocCLI

# Generated at 2022-06-12 20:24:59.500566
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    assert DocCLI._get_plugin_metadata()
    assert all([bool(item) for item in DocCLI._get_plugin_metadata()])


# Generated at 2022-06-12 20:25:04.581530
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    res = DocCLI.get_plugin_metadata('system', 'setup')
    assert res is not None
    assert isinstance(res, dict)
    assert 'module' in res
    assert 'module_utils' in res
    assert 'docuri' in res


# Generated at 2022-06-12 20:25:07.172052
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    string = "  4 attr: 4"
    # test 1
    assert DocCLI.format_snippet(string) == "   attr: 4"



# Generated at 2022-06-12 20:25:15.352614
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    """
    Test method
    """
    # Testobject

# Generated at 2022-06-12 20:26:13.266327
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():

    def test_add_fields(description, fields, expected):
        text = []
        DocCLI.add_fields(text, fields, 80, "       ", False)
        assert "\n".join(text) == expected, description


# Generated at 2022-06-12 20:26:17.955511
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    mock_loader = MagicMock()
    mock_loader.get_docs.return_value = [{'metadata': 'metadata', 'doc': 'doc'}]
    cli = DocCLI(mock_loader)
    assert cli.get_plugin_metadata('name') == 'metadata'



# Generated at 2022-06-12 20:26:29.465163
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = {
        'short_description': 'Test short description',
        'description': 'This is a test description.\nThis should be a wrapped description.',
        'options': {'test1': {'description': 'Test description'},
                    'test2': {'description': 'Test description 2'},
                    },
        }
    result = DocCLI.format_plugin_doc(doc, tty=False)
    print(result)

    test = """
    NAME
        test.py

    SYNOPSIS
        Test short description

    DESCRIPTION
        This is a test description. This should be a wrapped description.

    OPTIONS (= is mandatory):
        test1 (str) - Test description

        test2 (str) - Test description 2"""

    assert result == test



# Generated at 2022-06-12 20:26:39.852293
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    import sys
    import doctest
    import textwrap
    import ruamel.yaml

    yaml = ruamel.yaml.YAML()
    yaml.width = 80
    yaml.indent = 2
    yaml.default_flow_style = False
    sys.modules['ansible.utils.yaml'] = ruamel.yaml
    sys.modules['ansible.utils.yaml_loader'] = ruamel.yaml
    sys.modules['ansible.utils.yaml_dumper'] = ruamel.yaml
    sys.modules['ansible.utils.plugin_docs'] = ruamel.yaml

    module_name = 'ruamel.yaml'
    module_name_0 = 'ansible.utils.yaml'

# Generated at 2022-06-12 20:26:44.670994
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    import os
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.removed import removed
    from ansible.module_utils.common.removed import removed_module
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY3


# Generated at 2022-06-12 20:26:56.736398
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    test_doc_format = DocCLI()

    # Assert that method format_plugin_doc output is of type str
    test_data = {'version_added': '2.3', 'description': ['description'], 'options': {'options1': {'description': ['description']},
        'options2': {'description': ['description']}, 'options3': {'description': ['description']}}}
    assert isinstance(test_doc_format.format_plugin_doc(test_data), str)
    assert isinstance(test_doc_format.format_plugin_doc(test_data, 'collection_name'), str)
    assert isinstance(test_doc_format.format_plugin_doc(test_data, plugin_type='plugin_type'), str)


# Generated at 2022-06-12 20:27:02.692533
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # Test with missing test file (test_ansible_doc_fragments_syntax.txt)
    # Would not be possible to run this test in not existing directory
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-12 20:27:04.885566
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    '''Unit test for get_plugin_metadata of class DocCLI'''
    pass

# Generated at 2022-06-12 20:27:07.714524
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    with pytest.raises(AnsibleOptionsError):
        doc = DocCLI(None, context={'foo': 'bar'})
        doc.get_plugin_metadata()



# Generated at 2022-06-12 20:27:10.037443
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    doc_cli = DocCLI()
    assert isinstance(doc_cli, DocCLI)


# Generated at 2022-06-12 20:30:24.479352
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    dc = DocCLI()
    doc = dc.find_plugins()
    assert doc is None


# Generated at 2022-06-12 20:30:31.126778
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    doc_obj = DocCLI()
    doc_obj._create_role_doc = MagicMock(return_value={'entry_points':{'main':{'short_description':'test'},'test':{'short_description':'blah'}}})
    result = doc_obj.get_role_man_text('test',{'entry_points':{'main':{'short_description':'test'},'test':{'short_description':'blah'}}})
    assert result[0].startswith('> TEST    (')
    assert result[1] == 'ENTRY POINT: main - test'
    assert result[2] == 'ENTRY POINT: test - blah'


# Generated at 2022-06-12 20:30:33.391686
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    DocCLI.get_all_plugins_of_type()



# Generated at 2022-06-12 20:30:42.990881
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    doc_cli = DocCLI()
    doc_cli.IGNORE =  ['name', 'filename', 'platform', 'seealso', 'requirements', 'author', 'version_added', 'deprecated', 'version_added_collection']
    role =  'role1'

# Generated at 2022-06-12 20:30:46.861078
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    clear_known_hosts() # workaround for https://github.com/ansible/ansible/issues/30991
    runner = TestRunner()
    # Test code here
    cliargs = context.CLIARGS
    args = DocCLI.parse()
    runner.run_module('doc', args)

# need to ensure we can read the output of multiple command invocations

# Generated at 2022-06-12 20:30:52.109371
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    from ansible.utils.display import Display
    from ansible.utils.unicode import to_text
    display = Display()
    display.columns = 80

    DocCLI.IGNORE = DocCLI.IGNORE + (context.CLIARGS['type'],)
    opt_indent = "        "
    text = []
    pad = display.columns * 0.20
    limit = max(display.columns - int(pad), 70)
    options = []
    return_values = False

# Generated at 2022-06-12 20:31:01.504108
# Unit test for method get_role_man_text of class DocCLI

# Generated at 2022-06-12 20:31:10.969133
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    # Verify single module
    file_name = 'win_group'
    results = DocCLI._get_all_plugins_of_type(module_finder, file_name, 'module')
    assert len(results) == 1
    assert results[0].get('filename').endswith('lib/ansible/modules/windows/%s.ps1' % file_name)
    assert results[0].get('module_name') == file_name

    # Verify single lookup
    file_name = 'vars_prompt'
    results = DocCLI._get_all_plugins_of_type(lookup_finder, file_name, 'lookup')
    assert len(results) == 1

# Generated at 2022-06-12 20:31:13.090169
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    assert DocCLI.add_fields("", {"name" : "foo", "type" : "string", "description" : "This is foo"}) == ""


# Generated at 2022-06-12 20:31:24.252361
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible.plugins import module_loader
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves import StringIO
