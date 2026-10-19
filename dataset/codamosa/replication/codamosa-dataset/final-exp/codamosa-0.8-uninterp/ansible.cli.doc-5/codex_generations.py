

# Generated at 2022-06-12 20:26:15.372405
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    d = DocCLI("foo", "bar")
    try:
        d.namespace_from_plugin_filepath("/path/to/my/ansible_my_module.py")
    except Exception as e:
        print("unable to find namespace_from_plugin_filepath: %s" % to_native(e))
    else:
        if d.namespace_from_plugin_filepath("/path/to/my/ansible_my_module.py") != "modules.my":
            print("Namespace not correct")
        else:
            print("Namespace correct")

# Generated at 2022-06-12 20:26:19.678763
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    # Inits with list of plugins
    d = DocCLI(['module', 'module_build'])
    # Call display_plugin_list
    d.display_plugin_list()
    # Check it is string
    assert isinstance(d.plugin_list_txt, string_types)

# Generated at 2022-06-12 20:26:27.126477
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    filename = '/home/arista/ansible/lib/ansible/plugins/action/cloudengine_rest.py'
    assert DocCLI.namespace_from_plugin_filepath(filename) == 'cloudengine_rest'
    filename = '/home/arista/ansible/lib/ansible/plugins/test/test_cloudengine.py'
    assert DocCLI.namespace_from_plugin_filepath(filename) == 'test_cloudengine'
    filename = '/home/arista/ansible/lib/ansible/plugins/command/command.py'
    assert DocCLI.namespace_from_plugin_filepath(filename) == 'command'
    filename = '/home/arista/ansible/lib/ansible/plugins/inventory/azure_rm/__init__.py'
    assert DocCLI.names

# Generated at 2022-06-12 20:26:29.580566
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    mydoc = DocCLI()
    mydoc.run()
    assert True

if __name__ == '__main__':
    test_DocCLI_run()

# Generated at 2022-06-12 20:26:36.021439
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    # We don't have any specific tests yet, but at least make sure we can parse each parser plugin without error (we tested the 'docs' parser in test_plugins.py)
    for name in (n.split('.')[0] for n in os.listdir(C.DOCUMENTATION_PARSER_PLUGINS) if n.endswith('.py')):
        DocCLI._get_doc(name, verbose=False)


# Generated at 2022-06-12 20:26:43.895402
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    text_empty = []
    limit = 70
    opt_indent = "        "

    # Test 1
    opt = {
        'default': 'localhost',
        'description': 'Hostname or IP address of the target host.',
        'type': 'str',
        'version_added': '2.0'
    }
    DocCLI.add_fields(text, opt, limit, opt_indent, False)
    text_expected = """
        host: Hostname or IP address of the target host. [Default: localhost]
              added in: 2.0"""
    assert text == text_expected.split("\n"), "DocCLI.add_fields() failed"
    text = []

    # Test 2
    opt = {
        'version_added': '2.0'
    }


# Generated at 2022-06-12 20:26:55.442515
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    # try to get the actual function to test by instantiating the class first
    doc_instance = DocCLI()

    # test with name not in the list
    doc_list = [{}]
    plugin_name = 'sample_plugin'
    plugin_type = 'sample_plugin_type'
    module_name = 'sample_module'

# Generated at 2022-06-12 20:26:59.370565
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    plugin_filepath = './lib/ansible/plugins/modules/test.py'
    cli_instance = DocCLI()
    expected_result = 'test'
    real_result = cli_instance.namespace_from_plugin_filepath(plugin_filepath)

    assert expected_result == real_result, "The result is not as expected: %s != %s" % (real_result, expected_result)

# Generated at 2022-06-12 20:27:05.346798
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []

# Generated at 2022-06-12 20:27:15.955491
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    config = {'filter': lambda x, y: True}
    doc = {
        'description': 'sometext',
        'options': {'arg1': {'description': 'test1', 'choices': ['test', 'testtest'], 'type': 'string'},
                    'arg2': {'description': 'test2', 'choices': ['test', 'testtest'], 'type': 'string'}}
    }


# Generated at 2022-06-12 20:28:11.356917
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    # Run doc.py with '---' as argument
    cli = DocCLI(['---'])
    # Check if OutStream is StringIO
    assert isinstance(cli.pager, StringIO)
    # Run doc.py
    cli.run()
    # Check if PAGER_ENV is set to cat
    assert os.environ.get('PAGER') == "cat"


# Function to get options

# Generated at 2022-06-12 20:28:18.950178
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    d = {'ansible_ssh_host': 'inventory_hostname', 'ansible_ssh_port': 22}
    list_string = []
    DocCLI.add_fields(list_string, d, 30, '        ')
    assert "        " in list_string[0]
    assert "        " in list_string[1]



# Generated at 2022-06-12 20:28:26.696940
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    plugin_type = 'module'
    plugins = {
        'empty_module': {'name': 'empty_module', 'module_name': 'empty_module', 'path': '/path/to/empty_module.py', 'filename': 'empty_module.py'},
        'sample_module': {'name': 'sample_module', 'module_name': 'sample_module', 'path': '/path/to/sample_module.py', 'filename': 'sample_module.py'}
    }
    monkeypatch.setattr(DocCLI, 'get_default_config', lambda self, component='', verify_docs=False, plugin_type='': {'module_dir': '/path/to', 'search_path': '/path'})

# Generated at 2022-06-12 20:28:34.500302
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # Test 1
    test_dict = {'test': {'default': '1', 'description': 'Description'},
                 'keyboard': {'suboptions': 'subopt'}}
    test_list = ["        TEST: [Default: 1]", "        DESCRIPTION: Description", "", "        KEYBOARD:",
                 "            SUBOPTIONS:"]
    test_list_subopt = ["                SUBOPTIONS: [Default: (null)]", "                DESCRIPTION: Description", "", "                KEYBOARD:",
                        "                    SUBOPTIONS:"]
    text, opt_ty = list(), list()
    DocCLI.add_fields(text, test_dict['test'], 80, '        ', False, opt_ty)
    assert test_list == text

    # Test 2
    text, opt_ty = list

# Generated at 2022-06-12 20:28:37.833525
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    # creating an object of class DocCLI
    doccli = DocCLI()
    #creating mock data for get_role_man_text
    role = {'name':'test'}
    role_json = {'path':'test_path','plugins':'test_plugins','entry_points':'test_entry_point'}
    doccli.get_role_man_text(role,role_json)


# Generated at 2022-06-12 20:28:47.647381
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    # Assumes tty of width 80
    # Assumes this is the first test called in the module
    plugins_docs = DocCLI._generate_plugin_docs()

    # Test the formatter of a module (no collection)
    plugin_doc = plugins_docs['apt']
    assert plugin_doc.startswith("> APT    (plugins/modules/apt.py)")
    assert "\nEXAMPLES:\n" in plugin_doc
    assert "\nDEPRECATED: \n\tReason: superseded by the `apt_key` module" in plugin_doc
    assert "\nADDED IN: Ansible 2.6" in plugin_doc

# Generated at 2022-06-12 20:28:48.874217
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    assert get_plugin_metadata.__doc__ is not None


# Generated at 2022-06-12 20:28:51.049018
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    DocCLI_instance = DocCLI().find_plugins('/home/mmistroni/ansible/ansible/modules')


# Generated at 2022-06-12 20:28:59.326218
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    import yaml
    from ansible.module_utils._text import to_bytes

# Generated at 2022-06-12 20:29:03.915556
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    test_object = DocCLI()
    test_object.IGNORE = tuple(set(test_object.IGNORE) & set(context.CLIARGS['type']))
    test_object.IGNORE = tuple(set(test_object.IGNORE) & set(context.CLIARGS['type']))
    text = []
    add_fields__options = {"foo": "bar"}
    add_fields__limit = 123
    add_fields__opt_indent = "  "
    add_fields__opt_indent_nest = "    "
    add_fields__return_values = True
    test_object.add_fields(text, add_fields__options, add_fields__limit, add_fields__opt_indent, add_fields__opt_indent_nest, add_fields__return_values)


# Generated at 2022-06-12 20:30:22.136341
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    DocCLI_obj = DocCLI()

    def test_assertion(text, doc, limit, opt_indent, return_values, indent):
        assert text[0] == "        test: This is a test"

    DocCLI_obj.add_fields.func_code = test_assertion.func_code
    DocCLI_obj.add_fields([], {"test": "This is a test"}, 80, "        ", False, "        ")



# Generated at 2022-06-12 20:30:29.920982
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    # Verify that roles can be displayed with the DocCLI.get_role_man_text() method
    rf = C.data_loader.load_from_file
    for role in rf.items():
        if role[0].startswith('.'):
            continue
        if not os.path.isdir(role[1]):
            continue
        p = C.data_loader.find_plugin_file(role[1], 'meta/main.yml')
        if p is not None:

            DocCLI._create_role_doc(p)
            DocCLI._create_role_doc()



# Generated at 2022-06-12 20:30:41.209129
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    doccli = DocCLI()
    text1 = doccli.get_plugin_metadata('service', 'action')
    text2 = doccli.get_plugin_metadata('service', 'become')
    text3 = doccli.get_plugin_metadata('service', 'cache')
    text4 = doccli.get_plugin_metadata('service', 'connection')
    text5 = doccli.get_plugin_metadata('service', 'httpapi')
    text6 = doccli.get_plugin_metadata('service', 'logger')
    text7 = doccli.get_plugin_metadata('service', 'shell')
    text8 = doccli.get_plugin_metadata('service', 'strategy')
    text9 = doccli.get_plugin_metadata('service', 'terminal')

# Generated at 2022-06-12 20:30:48.725586
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    from ansible.errors import AnsibleOptionsError

    # Arrange
    cli = DocCLI(['--help'])
    cli.parser = Mock()

    cli.all = False
    cli.listt = False
    cli.extensions = False
    cli.version = False
    cli.man = False
    cli.json = False
    cli.expand_vars = None
    cli.paths = []
    cli.type = 'module'
    cli.subtype = None
    cli.parse_version = LooseVersion("2.10")
    cli.parse_collection = None
    cli.parse_index_info = {'indexed_collections': [], 'modules': [], 'plugins': []}
    cli.name = None

    # Act

# Generated at 2022-06-12 20:30:59.027760
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    from ansible import module_utils

    # set context to a specific type
    context.CLIARGS['type'] = 'module'

    # use the module_utils.common.normalize_module_utils_path method
    # to get the right path depending of the system
    module_utils_path = module_utils.common.normalize_module_utils_path('lib/ansible/utils/cache.py')

    # read its content as yaml
    data = read_content_if_exists(module_utils_path, ignore_errors=False, content_type='yaml')

    # remove IGNORED keys
    if 'version_added_collection' in data:
        data.pop('version_added_collection')

    data.pop('version_added')

    # get text with tty format
    text = DocCLI.get

# Generated at 2022-06-12 20:31:06.286769
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    loader, inventory, variable_manager = DocCLI._init_loader()
    collection_finder = CollectionFinder(loader=loader, variable_manager=variable_manager)
    collection_name = 'my_collection'
    collection_path = '/path/to/my_collection'
    module_name = 'my_module'
    collection = collections.namedtuple('Collection', ['name', 'path'])
    collection.name = collection_name
    collection.path = collection_path

    # Patching of method _find_collections_in_paths of class CollectionFinder
    with patch.object(CollectionFinder, '_find_collections_in_paths') as mock_find_collections_in_paths:
        mock_find_collections_in_paths.return_value = [collection]
        # Patching of method

# Generated at 2022-06-12 20:31:12.358365
# Unit test for method add_fields of class DocCLI

# Generated at 2022-06-12 20:31:23.732828
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    filename = 'plugins/modules/cloud/rackspace/rax.py'
    module_name = 'rax'
    args = ['-t', 'module']
    plugin_type = 'module'
    run_method = 'module_docs'
    doc_or_plugin = 'plugin'
    doc = {'filename': filename, 'docuri': 'rax', 'name': module_name, 'module': 'rax', 'doc': 'rax', '_terms': {}, 'options': {}, 'defaults': {}}
    doccli = DocCLI(['rax'], args, plugin_type, {}, run_method, doc_or_plugin)

# Generated at 2022-06-12 20:31:31.376901
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    import ansible
    from ansible.utils.display import Display
    display = Display()


# Generated at 2022-06-12 20:31:37.235112
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    # Class setup
    plugin_name = 'ping'
    collection_name = 'community.general'
    display_args = dict(type='module', collection_name=collection_name)
    context.CLIARGS = {'type': 'module', 'collection_name': collection_name}

    # Create some sample data