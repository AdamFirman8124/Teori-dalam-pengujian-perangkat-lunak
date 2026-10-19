

# Generated at 2022-06-12 20:24:43.144866
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:24:50.600821
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    doc = DocCLI()
    doc.bin_name = "ansible-doc"
    doc.bin_abs_path = "/bin/ansible-doc"
    doc.aliases = {"action": "actions", "module": "modules", "command": "commands", "plugin": "plugins", "inventory": "inventory", "vars": "variables", "facts": "facts", "filter": "filters", "shell": "shell"}
    doc.get_all_plugins_of_type("module")
    doc.get_all_plugins_of_type("action")
    doc.get_all_plugins_of_type("connection")
    doc.get_all_plugins_of_type("cache")
    doc.get_all_plugins_of_type("lookup")

# Generated at 2022-06-12 20:24:54.220774
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    plugin_type = 'action'
    add_collection_plugins(plugin_list, plugin_type, coll_filter=None)
    assert plugin_list == {'core': {'core.ansible_test'}, 'test_other': {'test_other.ansible_test'}, 'test_collection': {'test_collection.ansible_test'}}



# Generated at 2022-06-12 20:24:59.274357
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():

    class MockCLI(object):
        def __init__(self):
            self.tqm = None
            self.inventory = None
            self.variable_manager = None
            self.loader = None
            self.options = None
            self.passwords = None

    class MockOptions(object):
        def __init__(self):
            class MockSubOptions(object):
                def __init__(self):
                    self.tags = []
                    self.skip_tags = []
                def __getattr__(self, key):
                    return None
            self.module = None
            self.module_path = None
            args = None
            self.connection = 'local'

        def __getattr__(self, key):
            return None

    class MockModuleDepRes(object):
        def get_name(self):
            return

# Generated at 2022-06-12 20:25:06.601627
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    args = DocCLI.parse()
    doccli = DocCLI(args)
    modules_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
    plugins = doccli.find_plugins(modules_path)
    assert plugins['modules']
    assert plugins['modules'].get('apt')
    assert plugins['modules'].get('apt').get('name') is not None


# Generated at 2022-06-12 20:25:11.335204
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    module_1 = {
      "elem_1": "value 1",
      "elem_2": "value 2"
    }
    text = [""]
    DocCLI.add_fields(text, module_1, limit=80, opt_indent="        ")
    assert text == ["        elem_1: value 1", "        elem_2: value 2", ""]


# Generated at 2022-06-12 20:25:11.864639
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    pass

# Generated at 2022-06-12 20:25:23.648781
# Unit test for method get_man_text of class DocCLI

# Generated at 2022-06-12 20:25:29.745724
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = {'description': "This is a test of the doc_fragment method in the DocCLI class.\n\nThis module does nothing but return 'pong'."}
    plugin_type = "test"
    assert DocCLI.format_plugin_doc(doc, plugin_type) == "> TEST    ()\nThis is a test of the doc_fragment method in the DocCLI class.\n\nThis module does nothing but return 'pong'.\n"


# Generated at 2022-06-12 20:25:30.384159
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    pass

# Generated at 2022-06-12 20:26:34.882294
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    from ansible.module_utils.six import PY3
    import string
    import random
    import shutil
    import tempfile
    import os

    # test fixture
    def _random_filename(n=16, suffix=''):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(n)) + suffix

    # test fixture
    def _random_content():
        pieces = [''.join(random.choice(string.ascii_lowercase) for i in range(8)) for i in range(random.randint(1, 8))]
        return '\n'.join(pieces)

    # test fixture
    def _touch(path, content=None):
        if content is None:
            content = _random_content()
        if isinstance(content, str):
            content

# Generated at 2022-06-12 20:26:43.103126
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
  from . import collections
  import os
  import shutil
  import tempfile
  # Create a temporary copy of an example collection and prepare module and
  # plugin loader
  collection = collections.installed()['ansible_collections.notstdlib.moveitallout.plugins.modules'].copy()
  collection.module_loader = collections.ModuleLoader(None)
  collection.module_loader.disable_all_modules()

  # Create a temporary copy of the collection because loading it will modify it
  tmp_collection_path = tempfile.mkdtemp()
  tmp_collection = os.path.join(tmp_collection_path, 'ansible_collections')
  shutil.copytree(collection.collection_path, tmp_collection)

  # Load the newly copied collection
  collection.collection_path = tmp_collection
  collection.module_loader

# Generated at 2022-06-12 20:26:54.062976
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    doc = {"options": {"name": {"description": "The name of the movie to add.",
                                "aliases": ["title"],
                                "required": True}}}
    limit = max(display.columns - int(pad), 70)
    opt_indent = "        "
    return_values = False
    try:
        DocCLI.add_fields(text, doc["options"], limit, opt_indent, return_values)
    except Exception:
        assert False, "Error occured in DocCLI_add_fields method"
    assert text[0] == "        name: The name of the movie to add. [aliases: title] [required: True]"

# Generated at 2022-06-12 20:27:00.128436
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    # Using collection for testing
    col_name = 'acme'
    col_path = os.path.join(integration_loader.get_integration_path('module_utils'), col_name)
    role_name = 'new_relic_plugin'
    test_role_path = os.path.join(col_path, 'plugins/modules/new_relic_plugin')
    test_module_utils_path = os.path.join(test_role_path, 'module_utils')
    test_module_utils_file = os.path.join(test_module_utils_path, 'test_module_utils.py')
    # Remove the collection path, so that it gets discovered
    # and cleaned up by get_role_doc() when the test finishes

# Generated at 2022-06-12 20:27:00.774490
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
	pass

# Generated at 2022-06-12 20:27:04.279932
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    add_collection_plugins(plugin_list, 'module')
    assert isinstance(plugin_list, dict)
    assert len(plugin_list) > 0
    # check plugin
    plugins = plugin_list.keys()
    assert 'na_elementsw_config' in plugins



# Generated at 2022-06-12 20:27:05.188711
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    DocCLI.run()

# Generated at 2022-06-12 20:27:06.728825
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    DocCLI.find_plugins()


# Generated at 2022-06-12 20:27:10.325202
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    assert DocCLI.namespace_from_plugin_filepath('/home/ansible/ansible/lib/ansible/modules/cloud/amazon/ec2_vpc_subnet.py') == 'cloud.amazon'

# Generated at 2022-06-12 20:27:20.870483
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    """
    Verify method DocCLI.get_man_text
    """
    mydoc = {
        'description': [
            "description text 1.",
            "description text 2."
        ],
        'options': {
            'foo': {
                'description': [
                    "description text 1",
                    "description text 2"
                ]
            },
            'bar': {
                'description': "description text."
            }
        },
        'attributes': {
            'baz': {
                'description': "description text"
            }
        },
        'plainexamples': [
            "example 1"
        ],
        'returndocs': {
            'bar': {
                'description': "description text"
            }
        }
    }

# Generated at 2022-06-12 20:29:02.852626
# Unit test for function add_collection_plugins

# Generated at 2022-06-12 20:29:13.160778
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.environ.get("ANSIBLE_CONFIG_DIR", ""), "ansible.cfg"))
    ansible_dir = os.path.dirname(sys.modules['ansible'].__file__)
    ansible_dir = os.path.abspath(os.path.join(ansible_dir, ".."))
    root_dirs = [
        os.path.join(ansible_dir, 'lib', 'ansible', 'playbooks'),
        os.path.join(ansible_dir, 'lib', 'ansible', 'modules', 'extras'),
        os.path.join(ansible_dir, 'lib', 'ansible', 'modules'),
    ]

    d = DocCLI()
    # Testing with valid plugin

# Generated at 2022-06-12 20:29:20.662957
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    """
    Runs all tests for the method run of class DocCLI
    """
    # unit test for method run of class DocCLI
    test_cli_args =  {
        'foo':'nada',
        'version':'nada',
        'version_added':'nada',
        'module':'nada',
        'type':'nada',
        'subtype':'nada',
        'output_format':'nada',
        'width': display.columns,
        'module_path': None,
        'collection': None,
        'role_path': None,
        'metadata': None,
        'is_main': False
    }
    mock_cli_args = mock.Mock(**test_cli_args)

# Generated at 2022-06-12 20:29:24.909638
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    _mock_exit = MagicMock()
    with patch.multiple(DocCLI, exit=_mock_exit):
        # Test missing required options.
        try:
            DocCLI().run()
        except SystemExit as e:
            assert e.code == 1
            pass
        # Test with no valid options.
        try:
            DocCLI(args=['--invalid']).run()
        except SystemExit as e:
            assert e.code == 1
            pass

# ===========================================

# Generated at 2022-06-12 20:29:35.467795
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    collection_loader = CollectionsLoader([])
    collection_resolver = CollectionsPathResolver(collection_loader=collection_loader)

    plugin_loader = PluginLoader(
        '',
        '',
        C.DEFAULT_INTERNAL_PLUGIN_PATH,
        '',
        collection_resolver=collection_resolver
    )

    module_finder = ModuleFinder(collection_resolver=collection_resolver)
    _ = module_finder.find_all()
    module_list = []
    for filename, info in module_finder._collection_filename_to_info.items():
        module_list.append(info['module_name'])

    result = DocCLI.get_all_plugins_of_type('module')(plugin_loader)
    assert isinstance(result, list)

# Generated at 2022-06-12 20:29:37.026049
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    obj = DocCLI()
    print(obj.get_plugin_metadata())



# Generated at 2022-06-12 20:29:44.551107
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    # Test when is_module is true and namespace is provided
    path = './lib/ansible/plugins/action/lwrps_test.yml'
    is_module = True
    namespace = 'testing'
    actual_result = DocCLI.namespace_from_plugin_filepath(path, is_module, namespace)
    expected_result = 'testing'
    assert actual_result == expected_result, "Did not get the expected namespace, got %s" % actual_result

    # Test when is_module is false, namespace is provided and it is a collection
    path = './lib/ansible/plugins/action/lwrps_test.yml'
    is_module = False
    namespace = 'testing'

# Generated at 2022-06-12 20:29:52.873942
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:30:02.648742
# Unit test for method namespace_from_plugin_filepath of class DocCLI

# Generated at 2022-06-12 20:30:09.561337
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    yaml_base = "imaginary.collection.imaginary_plugin"
    plugin_type = "action"
    plugin_list = dict()
    coll_filter = None
    add_collection_plugins(plugin_list, plugin_type, coll_filter)
    assert "imaginary_plugin" in plugin_list, "imaginary_plugin not found in plugin_list"
    assert plugin_list["imaginary_plugin"] == yaml_base, "plugin_list[imaginary_plugin] not found to be equal to yaml_base"

