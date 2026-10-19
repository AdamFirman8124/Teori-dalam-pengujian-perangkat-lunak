

# Generated at 2022-06-12 20:24:17.858673
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    # Setup a test object
    import json
    test_obj = DocCLI()
    # Test variables
    # The expected output

# Generated at 2022-06-12 20:24:28.519197
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    import random
    import string
    from ansible.module_utils.connection import Connection, ConnectionError
    from ansible.module_utils.common import load_platform_subclass
    from ansible.module_utils.common._collections_compat import MutableMapping
    import ansible.module_utils.facts.hardware.realtek
    import ansible.module_utils.facts.network.brocade
    import ansible.module_utils.facts.network.dellos9
    import ansible.module_utils.facts.network.dellos10
    import ansible.module_utils.facts.network.ios
    import ansible.module_utils.facts.network.iosxr
    import ansible.module_utils.facts.network.junos
    import ansible.module_utils.facts.network.nxos
   

# Generated at 2022-06-12 20:24:37.975618
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():

    # Set up mocks for testing by DocCLI
    doc_cli = DocCLI()
    doc_cli.doc = {}
    doc_cli.doc['module_list'] = []
    doc_cli.options.type = 'module'
    doc_cli.get_module_name = lambda a: a
    doc_cli.get_module_files = lambda a: a
    doc_cli.get_module_file_args = lambda a: a
    doc_cli.doc['module_dir'] = '.'
    doc_cli.doc['module_dirs'] = '.'

    # Testing when os.walk returns None in find_plugins
    with patch('os.walk', return_value=None):
        doc_cli.find_plugins()
        assert doc_cli.doc['module_list'] == []

    # Testing when os

# Generated at 2022-06-12 20:24:45.389803
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:24:53.029532
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    limit = 72
    opt_indent = "        "
    doc = dict(
    name = dict(
        default=dict(
            env=['ANSIBLE_ACTION_PLUGINS'],
            ini=['action_plugins'],
            type='pathlist',
            version_added='historical',
            description='colon separated list of directories; DEPRECATED, see ``action_plugins``',
            aliases=[]
        )
    )
    )
    DocCLI.add_fields(text, doc, limit, opt_indent)
    assert text == ['NAME\n', '    DEFAULT: = ansible.builtin.plugins.action_loader:,/home/user/.ansible/plugins/action_plugins:/usr/share/ansible/plugins/action_plugins'], text

    text = []

# Generated at 2022-06-12 20:25:04.484280
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    from ansible.cli import CLI
    from ansible.utils.display import Display
    display = Display()
    context._init_global_context(cli_args=dict(type='role'))
    if os.path.exists('./test/test_plugins/test_roles/role1/meta/main.yml'):
        role_file_path = './test/test_plugins/test_roles/role1/meta/main.yml'
    else:
        role_file_path = os.path.expanduser('~/devel/ansible/test/test_plugins/test_roles/role1/meta/main.yml')
    doc = DocCLI(None, display)._load_file(role_file_path)
    assert isinstance(doc, dict)

# Generated at 2022-06-12 20:25:07.425784
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    plugin_type = 'module'

    with pytest.raises(exceptions.AnsibleError) as e:
        DocCLI.find_plugins(plugin_type=plugin_type)


# Generated at 2022-06-12 20:25:15.446004
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    # check if path to python interpreter is set
    if not cli_tools.check_python_path():
        # skip test
        pytest.skip("python invocation via PATH not working")

    # create a temporary directory
    tmp_dir = tempfile.mkdtemp()

    # write a test plugin in the temporary directory

# Generated at 2022-06-12 20:25:17.164396
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    # check function returns a string
    assert isinstance(DocCLI.namespace_from_plugin_filepath('/tmp/test'), str)


# Generated at 2022-06-12 20:25:18.644524
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    pass

# Generated at 2022-06-12 20:27:28.239070
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # DocCLI.add_fields(text, subdata, limit, opt_indent):
    pass



# Generated at 2022-06-12 20:27:36.521136
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    # Test when filename is present and has dependency is present
    doc = {'has_dependency': True, 'filename': '/usr/lib/python2.7/site-packages/ansible/modules/cloud/amazon/ec2_ami_facts.py'}
    doc_cli = DocCLI()
    doc_cli.get_man_text(doc)

    # Test when filename is not present and has dependency is present
    doc = {'has_dependency': True}
    doc_cli.get_man_text(doc)

    # Test when filename is present and has dependency is not present
    doc = {'has_dependency': False, 'filename': '/usr/lib/python2.7/site-packages/ansible/modules/cloud/amazon/ec2_ami_facts.py'}
    doc_cli.get_man_

# Generated at 2022-06-12 20:27:42.521532
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    collection_name = 'test_collection'
    doc_plugin_name = 'test_doc_plugin'
    plugin_type = 'test_type'
    plugin_name = 'test_plugin_name'
    path = 'test_path'
    plugin_path = os.path.join('test_plugin_path', path)
    req_plugin_name = 'requirements_plugin_name'
    req_plugin_path = os.path.join('test_req_plugin_path', path)

    doc_plugin_meta = {'requirements': [{'collection_name': req_plugin_name}], 'version_added': '2.10'}
    req_plugin_meta = {'version_added': '1.0'}

# Generated at 2022-06-12 20:27:45.350790
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    add_collection_plugins(plugin_list, 'module')
    assert plugin_list is not None
    assert len(plugin_list) > 0
    assert 'copy' in plugin_list 


# Generated at 2022-06-12 20:27:46.352225
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    # No need to test this
    pass

# Generated at 2022-06-12 20:27:48.949222
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    DocCLI.format_plugin_doc()

# Generated at 2022-06-12 20:28:01.087978
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    doc_cli = DocCLI()

# Generated at 2022-06-12 20:28:06.566204
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    """
    Test format_plugin_doc()
    """

    test_DocCLI = DocCLI()

    DocCLI.format_plugin_doc('test_name', {"foo": "test_foo"}, '', 'test_type')

    # Successfully raise exception. This block will not execute.
    try:
        DocCLI.format_plugin_doc('test_name', {}, '', 'test_type')
    except:
        assert True
    else:
        assert False


# Generated at 2022-06-12 20:28:14.379256
# Unit test for function add_collection_plugins
def test_add_collection_plugins():

    def mock_list_collection_dirs(coll_filter=None):
        if coll_filter:
            assert coll_filter == 'jpt'
            return ['coll1', 'coll2']
        else:
            return ['coll1', 'coll2', 'jpt']

    # TODO: test with runtime.yml once implemented
    def mock_find_plugins(path, show_dupes, plugin_type, collection=None):
        assert show_dupes is False
        assert plugin_type == 'action'
        assert path == 'path/collection/plugins/action'
        assert collection
        plugin_list = {'%s/%s' % (collection, plugin): 'path/%s/%s' % (collection, plugin) for plugin in
                       ['col_plugin1', 'col_plugin2']}
        return plugin_list

# Generated at 2022-06-12 20:28:24.894731
# Unit test for method namespace_from_plugin_filepath of class DocCLI

# Generated at 2022-06-12 20:31:12.468636
# Unit test for method get_role_man_text of class DocCLI

# Generated at 2022-06-12 20:31:23.861786
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():

    # test 1 - type_check: str

    my_obj = DocCLI()  

    # args
    (text, data, limit, opt_indent, return_values, opt_indent) = ("Test for text", "Test for data", "Test for limit", "Test for opt_indent", "Test for return_values", "Test for opt_indent") #args
    # expectation
    expected_output1 = "Test for text"

    # test
    assert expected_output1 == my_obj.add_fields(text, data, limit, opt_indent, return_values, opt_indent)

    # test 2 - type_check: int

    my_obj = DocCLI()  

    # args

# Generated at 2022-06-12 20:31:24.866955
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    pass



# Generated at 2022-06-12 20:31:28.333481
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    plugin_list = DocCLI().find_plugins()
    assert(isinstance(plugin_list, list))
    assert(len(plugin_list) > 0)

    # Calling find_plugins() again should return the same list
    plugin_list2 = DocCLI().find_plugins()
    assert(plugin_list == plugin_list2)

# Generated at 2022-06-12 20:31:35.292488
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    opt = {'choices': ['80', '443']}
    opt_indent = "        "
    opt2 = {'a': 'b', 'version_added': '1.8'}
    choices = 'choices: 80, 443'
    version_added = 'added in: 1.8'
    DocCLI.add_fields(text, opt, 80, opt_indent)
    assert choices in text
    text.clear()
    DocCLI.add_fields(text, opt2, 80, opt_indent)
    assert version_added in text
    text.clear()
    assert 'default' not in opt2
    opt2 = {'a': 'b', 'version_added': '1.8', 'default': '23'}

# Generated at 2022-06-12 20:31:43.840580
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    opt_indent = "        "
    pad = display.columns * 0.20
    limit = max(display.columns - int(pad), 70)
    opt = {}
    opt['name'] = {}
    opt['name']['default'] = 'localhost'
    opt['name']['description'] = 'Sets the hostname or IP address of the remote device. The value of host can either be a host name or an IP address.'
    x = DocCLI.add_fields(text, opt, limit, opt_indent)
    assert text[1] == "        name: Sets the hostname or IP address of the remote device. The value of host can either be a host name or an IP address. [Default: localhost]"

# Generated at 2022-06-12 20:31:46.126163
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    doc = DocCLI()
    result = doc.get_all_plugins_of_type('action')
    assert result


# Generated at 2022-06-12 20:31:49.040514
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    # Dummy values for testing
    DocCLI.format = 'json'
    sys.argv = ['ansible-doc', '-t', 'module', 'apt', '-M', '../test/units/modules/extras']

    # Run the method under test
    DocCLI.find_plugins()

    assert True


# Generated at 2022-06-12 20:32:00.742115
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    from ansible.utils.color import stringc

    # Test handling of doc/man options
    args = DocCLI._parse_args(['ansible-doc', '-M', 'our/path', 'acmecafe.example_module', '--doc-type=man'])
    assert args['doc_type'] == 'man'
    assert args['target'] == 'acmecafe.example_module'
    assert args['paths'] == ['/usr/share/ansible', '/etc/ansible', '~/.ansible/plugins/modules', './library', './module_utils', './modules']
    args = DocCLI._parse_args(['ansible-doc', '-M', 'our/path', 'acmecafe.example_module', '--doc-type=doc'])