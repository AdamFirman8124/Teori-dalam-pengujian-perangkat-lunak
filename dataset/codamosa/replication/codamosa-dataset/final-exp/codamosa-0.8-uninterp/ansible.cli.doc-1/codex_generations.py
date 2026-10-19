

# Generated at 2022-06-12 20:23:53.287132
# Unit test for method print_paths of class DocCLI
def test_DocCLI_print_paths():
    from ansible.utils.path import mux_dirs
    from ansible.cli.doc import DocCLI
    import ansible.constants as C
    import os
    # initialize
    C.DEFAULT_MODULE_PATH = os.path.join(os.path.dirname(__file__), 'test_plugins/test_modules')
    # https://github.com/ansible/ansible/issues/37855
    C.DEFAULT_LOCAL_TMP = '/tmp'
    C.DEFAULT_REMOTE_TMP = '/tmp'
    C.DEFAULT_PLUGIN_PATH = os.path.join(os.path.dirname(__file__), 'test_plugins')
    # verify that run_command does what we expect

# Generated at 2022-06-12 20:23:55.534153
# Unit test for function jdump
def test_jdump():
    test_data = {'answer': 42}
    jdump(test_data)


# Generated at 2022-06-12 20:24:05.139491
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    # Test with a negative start value
    result = DocCLI.format_snippet('', start=-5, end=5)
    assert result == '...', 'Expected snippet result to be ...'

    # Test that the start value is used when it's positive
    result = DocCLI.format_snippet('123456', start=3, end=3)
    assert result == '345...', 'Expected snippet result to be 345...'

    # Test that the end value is used when it's positive
    result = DocCLI.format_snippet('123456', start=3, end=3)
    assert result == '345...', 'Expected snippet result to be 345...'

    # Test that the snippet starts at the beginning when the start value is past the end of the string
    result = DocCLI.format_snippet

# Generated at 2022-06-12 20:24:12.551617
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    module_paths = []
    excludes_paths = []
    module_name = []
    display_snippets = False
    verbose = False
    display_extra_paths = False
    display_deprecated = False
    DocCLI.display_plugin_list(module_paths, excludes_paths, module_name, display_snippets, verbose, display_extra_paths, display_deprecated)



# Generated at 2022-06-12 20:24:22.932842
# Unit test for method add_fields of class DocCLI

# Generated at 2022-06-12 20:24:34.039220
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    result = DocCLI().get_role_man_text(role='something',
                                        role_json={
                                            'entry_points': {
                                                'something': {
                                                    'description': 'What a good role',
                                                    'options': {},
                                                    'attributes': {},
                                                },
                                            },
                                            'path': 'a/path',
                                        })

    # This is to ensure we have exactly 4 lines
    if len(result) != 4:
        raise AssertionError("Expected 4 lines of text but got %s: %s" % (len(result), result))
    if result[-1] != "        attributes: {}":
        raise AssertionError("Expected attributes:{} but got %s" % result[-1])

# Generated at 2022-06-12 20:24:35.801164
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    t = DocCLI()
    assert t.get_plugin_metadata('foo.py') == {}

# Generated at 2022-06-12 20:24:36.542086
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    assert 1


# Generated at 2022-06-12 20:24:46.621396
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    #test plugin_type = connection
    plugin_list = {}
    plugin_type = 'connection'
    C.COLLECTION_PTYPE_COMPAT = {'connection': 'connections'}
    coll_filter = 'ansible_collections.nsbl.network'

    add_collection_plugins(plugin_list,plugin_type,coll_filter)
    assert plugin_list['ansible_nsbl.network.amazon.aws_ec2.Connection'] == 'ansible_collections/nsbl/network/plugins/connections/aws_ec2.py'

    #test plugin_type = module
    plugin_list = {}
    plugin_type = 'module'
    C.COLLECTION_PTYPE_COMPAT = {'module': 'modules'}

# Generated at 2022-06-12 20:24:48.386036
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    """
    Test for method DocCLI.get_role_man_text
    """
    pass


# Generated at 2022-06-12 20:25:40.976016
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    from ansible.module_utils._text import to_text
    from collections import namedtuple
    from ansible.cli import CLI
    from ansible.utils.display import Display
    from ansible.utils.color import stringc
    from ansible.utils.path import get_distribution_version

    # initialize some settings
    context.CLIARGS = namedtuple('CLIARGS', 'listtags listtasks listhosts syntax check diff module_path')
    context.CLIARGS.syntax = False
    context.CLIARGS.check = False
    context.CLIARGS.diff = False
    context.CLIARGS.type = 'module'
    context.CLIARGS.module_path = '.'
    display = Display()
    display.verbosity = 3
    DocCLI.tty_ify

# Generated at 2022-06-12 20:25:47.637243
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    from ansible.utils.display import Display
    import ansible.plugins.loader
    display = Display()
    display.columns = 100
    for plugin_type in ansible.plugins.loader.all():
        for plugin in ansible.plugins.loader.all()[plugin_type]:
            if '__doc__' in plugin._annotation_attributes:
                text = DocCLI.get_role_man_text(plugin_type, plugin._annotation_attributes)
                assert isinstance(text, list)


# Generated at 2022-06-12 20:25:51.794730
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    module_name = 'systemd'
    output_type = 'json'
    doc = DocCLI.format_plugin_doc(module_name, output_type, get_versioned_json_docs=False)
    assert isinstance(doc, dict)


# Generated at 2022-06-12 20:25:55.485855
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    add_collection_plugins(plugin_list, 'action', coll_filter=['ansible_collections.fortinet.fortios'])
    assert 'ansible_collections.fortinet.fortios.plugins.modules.fortios_system_vdom_netflow' in plugin_list



# Generated at 2022-06-12 20:25:56.182638
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    pass

# Generated at 2022-06-12 20:26:02.234500
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    module = "network_cli"
    snippet = "- name: get facts for all devices\n  nxos_facts:\n    gather_subset: all\n"
    args = "name: get facts for all devices\nnxos_facts:\n  gather_subset: all\n"
    res = DocCLI.format_snippet(module, snippet, args)
    print(res)

# Generated at 2022-06-12 20:26:03.515110
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
  pass

# Generated at 2022-06-12 20:26:07.144876
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    doc = DocCLI()
    doc.get_all_plugins_of_type('connection_plugins')

# Testing for method print_manpage of class DocCLI

# Generated at 2022-06-12 20:26:13.757810
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = {}
    plugin_name = 'os_flavor'
    plugin_type = 'module'
    collection_name = 'openstack.cloud'
    (options, notes, examples) = DocCLI.format_plugin_doc(doc, plugin_name, plugin_type, collection_name)
    assert(options == {})
    assert(notes == {})
    assert(examples == [])


# Generated at 2022-06-12 20:26:23.546706
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    from ansible.module_utils._text import to_text
    from ansible.utils.display import Display
    display = Display()
    display.columns = 160

    json_data = {
        'options': {
            'foo': {
                'choices': ['1', '2', '3'],
                'default': '2',
                'description': 'foo',
                'required': True
            },
            'bar': {
                'description': ['baz', 'bam'],
                'required': False
            }
        }
    }
    text = []
    DocCLI.add_fields(text, json_data['options'], limit=display.columns, opt_indent='', return_values=True)
    text = to_text("\n".join(text))

# Generated at 2022-06-12 20:28:02.059308
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    import tempfile

    # temporary filename
    fileobj = tempfile.NamedTemporaryFile(mode='wt', delete=False)
    filename = fileobj.name
    fileobj.close()

    # Create a playbook doc
    playbook_data = {
        'name': 'my playbook',
        'author': 'my name',
        'description': 'my description',
        'filename': filename,
        'plainexamples': 'some plain examples'
    }
    playbook_data_display = DocCLI.get_man_text(playbook_data, plugin_type='playbook')
    assert playbook_data_display == '''> MY PLAYBOOK    (%s)
my description

EXAMPLES:

some plain examples
''' % filename

    # Create a module doc

# Generated at 2022-06-12 20:28:08.897712
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    doc = DocCLI()
    items = [
        {'name': 'test1', 'path': '/path/to/test1', 'collection': 'collection1'},
        {'name': 'test1', 'path': '/path/to/test2', 'collection': 'collection2'},
        {'name': 'test2', 'path': '/path/to/test3', 'collection': 'collection3'},
        {'name': 'test3', 'path': '/path/to/test4', 'collection': 'collection4'}
    ]
    output = doc.display_plugin_list(items, 'PLUGIN_TYPE')
    assert len(output.splitlines()) == len(items) + 4



# Generated at 2022-06-12 20:28:10.626556
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    my_DocCLI = DocCLI()
    assert(my_DocCLI.get_man_text(None, '', '') == None)


# Generated at 2022-06-12 20:28:22.598888
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    module = MockModule()
    module.params = dict(
        type='module',
        name='setup',
        paths=[],
    )
    result = DocCLI._run(module)
    assert result['name'] == 'setup'
    assert result['description'] == 'Gather facts about remote hosts'

    module.params = dict(
        type='module',
        name='rip',
        paths=[],
    )
    result = DocCLI._run(module)
    assert result is None

    module.params = dict(
        type='module',
        name='setup',
        paths=['/path/to/doc/'],
    )
    result = DocCLI._run(module)
    assert result['name'] == 'setup'
    assert result['description'] == 'Gather facts about remote hosts'


# Generated at 2022-06-12 20:28:28.343451
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    plugin_paths = (os.path.join(os.path.dirname(__file__), 'plugins'),)
    plugins = DocCLI._load_plugins(plugin_paths)
    category = 'action'
    data = DocCLI.display_plugin_list(plugins, category, short=False)
    assert data == ['action', 'debug', 'pause', 'setup', 'wait_for']

# Generated at 2022-06-12 20:28:35.405918
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    doc_obj = DocCLI()

    doc_obj.display_plugin_list(['ansible.builtin.command_module', 'ansible.builtin.copy_module'],
            'module', 'Core modules', 'Modules shipped with ansible')

    doc_obj.display_plugin_list(['setup', 'gather_facts', 'shell'],
            'module', 'Core modules', 'Modules shipped with ansible')

    doc_obj.display_plugin_list(['setup', 'gather_facts', 'shell'],
            'module', 'Core modules', 'Modules shipped with ansible', aliases=['setup', 'gather_facts'])


# Generated at 2022-06-12 20:28:41.005201
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    plugin_type = "ANSIBLE"
    test_path = '../lib/ansible/plugins/modules'
    plugin_name = 'firewalld'
    search_paths = [test_path]
    cli_args = {'type': plugin_type, 'show_snippet': False, 'output': 'text'}
    context.CLIARGS = cli_args

# Generated at 2022-06-12 20:28:49.233844
# Unit test for method get_plugin_metadata of class DocCLI

# Generated at 2022-06-12 20:28:55.389278
# Unit test for method get_plugin_metadata of class DocCLI

# Generated at 2022-06-12 20:29:03.784866
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    from ansible.cli.doc import DocCLI
    from ansible.module_utils._text import to_bytes
    import ansible.constants as C
    import os
    import sys

    # Create a DocCLI object
    # Test parsing method parse()
    # Test parsing method parse() with no arguments
    args = dict(
        all=False,
        module=None,
        exclude_module=None,
        exclude_dir=None,
        requester=None,
        subdir=None,
        versioned=False
    )
    doc = DocCLI(args, display=None)
    doc.parse()
    assert doc.args.all == False
    assert doc.args.module == None
    assert doc.args.exclude_module == None
    assert doc.args.exclude_dir == None