

# Generated at 2022-06-12 20:25:31.928817
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():

    import sys
    import os
    import inspect


# Generated at 2022-06-12 20:25:38.092745
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    args = DocCLI.get_argument_parser().parse_args([])
    cli = DocCLI(args)
    
    def get_plugin_list(args):
        if args.type == 'module':
            return [{'name': 'ping'}]
        else:
            return [
                {'name': 'ping', 'type': 'module'},
                {'name': 'pong', 'type': 'module'},
                {'name': 'playbook', 'type': 'action'},
            ]
    
    def display_this(what, where):
        pass
    cli.get_plugin_list = get_plugin_list
    cli.display = display_this
    # verify on the surface
    
    def verify(args):
        cli.args = args
        cli.display_

# Generated at 2022-06-12 20:25:39.841006
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    cli = DocCLI()
    # TODO
 

# Generated at 2022-06-12 20:25:46.548590
# Unit test for method print_paths of class DocCLI
def test_DocCLI_print_paths():
    import ansible.plugins.loader
    from ansible.plugins.loader import action_loader, connection_loader, filter_loader, module_finder, module_loader, lookup_loader, test_loader, module_utils_loader, callback_loader

    with mock.patch.dict('ansible.constants.DEFAULT_MODULE_PATH', {'a': 'b'}):
        # Tests the case of all True arguments
        DocCLI.print_paths(True, True, True, True, True, True, True, True, True, True)
        DocCLI.print_paths(True, True, True, True, True, True, True, True, True, False)
        DocCLI.print_paths(True, True, True, True, True, True, True, True, False, True)
        DocCLI.print_path

# Generated at 2022-06-12 20:25:48.956348
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    DocCLI.display_plugin_list(['foo', 'bar'], type='a')


# Generated at 2022-06-12 20:25:57.763176
# Unit test for method add_fields of class DocCLI

# Generated at 2022-06-12 20:26:09.593818
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    global __file__
    __file__ = "library/my_system/firewall.py"
    display.columns = 80

# Generated at 2022-06-12 20:26:10.961913
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    DocCLI.get_all_plugins_of_type('module')


# Generated at 2022-06-12 20:26:20.693871
# Unit test for method print_paths of class DocCLI
def test_DocCLI_print_paths():
    #
    # This test runs DocCLI.print_paths without having run the full
    # DocCLI init
    #
    # DocCLI.__init__ sets self.paths based on the CLI args.  We
    # want to test that method independently of the initialization
    # logic, which is a lot more complicated.  So we call
    # DocCLI._initialize_paths directly.
    #
    paths = []
    DocCLI._initialize_paths(paths)
    text = DocCLI.print_paths(paths)
    assert 'collections/' in text
    assert text.endswith('\n')


# Generated at 2022-06-12 20:26:24.723912
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    args = dict()
    args['p'] = None
    args['listt'] = None
    args['path'] = None
    args['t'] = None
    args['M'] = None
    args['collection'] = None
    # Instantiate class
    doc = DocCLI(args)
    # Execute method run
    res = doc.run()
    assert not res

# Generated at 2022-06-12 20:30:06.558789
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    limit = 100
    opt_indent = ' ' * 8
    options = {'options': {
        'name': {
            'description': 'The name of the object to act on.',
            'required': True,
            'type': 'str'
        },
        'values': {
            'description': 'The values to set on the object.',
            'suboptions': {
                'key1': {
                    'description': 'The first key to set.',
                    'required': True,
                    'type': 'str'
                },
                'key2': {
                    'description': 'The second key to set.',
                    'required': True,
                    'type': 'str'
                }
            },
            'type': 'dict'
        }
    }}
    DocCLI.add_fields

# Generated at 2022-06-12 20:30:15.338417
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible.cli import CLI

    cli = CLI()
    cli.options = lambda noop: None
    cli.options.list_dirs = False
    cli.options.list_files = False
    cli.settings = lambda noop: None
    cli.settings.loose_loader = False
    cli.settings.loose_loader_package = None
    cli.options.tree = None
    cli.options.type = 'action'
    cli.options.name = None
    cli.options.path = "/Users/simon/projects/ansible/lib/ansible/plugins/action"
    cli.args = []
    cli.options.verbosity = 0

    assert DocCLI.display_plugin_list(cli, []) == (0, '')

# Unit

# Generated at 2022-06-12 20:30:18.339077
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    """
    This function returns the result of DocCLI.find_plugins('')
    """
    return DocCLI.find_plugins('')

# Generated at 2022-06-12 20:30:28.765470
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    from ansible.cli.doc import DocCLI
    from ansible.utils.display import Display
    from ansible.utils.yaml import AnsibleUnsafeLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from datetime import date

    with open('test/testdata/doc/ping.txt', 'r') as f:
        expected_output = f.readlines()
    with open('test/testdata/doc/ping_json.txt', 'r') as f:
        json_data = f.read()
    display = Display()
    display.columns = 80
    doc = (AnsibleUnsafeLoader(json_data).get_single_data())
    assert DocCLI.get_man_text(doc) == ''.join(expected_output)


# Generated at 2022-06-12 20:30:40.245946
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    # Test with a small negative number of available columns
    with pytest.raises(AssertionError):
        DocCLI().find_plugins(plugins=(), name='', status=None, paths=(), desc='',
                              verbose=False, extra_paths=(), collection_name='',
                              min_columns=-1)
    # Test with a small positive number of available columns
    with pytest.raises(AssertionError):
        DocCLI().find_plugins(plugins=(), name='', status=None, paths=(), desc='',
                              verbose=False, extra_paths=(), collection_name='',
                              min_columns=1)
    # Test with a large negative number of available columns

# Generated at 2022-06-12 20:30:48.066072
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    from ansible.cli import CLI
    from ansible.module_utils._text import to_bytes
    import ansible.constants as C

    args = [ 'ansible-doc', '--version' ]
    cli = CLI(args)
    cli.parse()

    config = ConfigParser()
    config.read(C.DEFAULT_CONFIG_FILE)

    tmp_config = os.path.join(C.DEFAULT_LOCAL_TMP, 'config_file_%s' % uuid.uuid4().hex)
    display.display("Using temporary config file: %s" % tmp_config)
    config.write(open(tmp_config, 'w'))
    os.environ[C.CONFIG_ENV] = tmp_config

    display.verbosity = cli.options.verbosity
   

# Generated at 2022-06-12 20:30:58.244784
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    plugins = {
        'action': ['setup', 'debug'],
        'aggregate': ['setup', 'debug'],
        'become': [],
        'cache': [],
        'callback': [],
        'cliconf': [],
        'connection': [],
        'httpapi': ['http.get', 'http.post'],
        'inventory': ['dynamic', 'hostgroup'],
        'lookup': [],
        'module': ['setup', 'debug'],
        'strategy': [],
        'terminal': [],
        'test': [],
        'vars': [],
        'vars_prompt': []
    }
    plugin_type = "action"
    category = None
    get_subcommand_list = []

# Generated at 2022-06-12 20:31:01.006427
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    _docs = DocCLI(type='module')
    item = 'ansible.module_utils.facts.linux.distribution.distribution'
    assert item in _docs.get_all_plugins_of_type(type="module")

# Generated at 2022-06-12 20:31:07.528682
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    doc = DocCLI()
    doc.load()
    filter_path = set()
    filter_path.add(os.path.join(os.getcwd(),'test/test_utils/test_plugins/_test_plugin.py'))
    plugin_list = doc.get_all_plugins_of_type('modules', filter_path)
    assert len(plugin_list) == 1, 'Incorrect number of plugins of type modules were retrieved.'

# Generated at 2022-06-12 20:31:17.724097
# Unit test for method get_role_man_text of class DocCLI