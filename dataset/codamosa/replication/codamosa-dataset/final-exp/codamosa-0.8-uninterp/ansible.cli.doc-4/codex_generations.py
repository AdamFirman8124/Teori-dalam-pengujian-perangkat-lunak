

# Generated at 2022-06-12 20:24:30.629914
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:24:32.446460
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    assert callable(DocCLI.get_all_plugins_of_type)


# Generated at 2022-06-12 20:24:39.307873
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    plugin_type_name = 'foo_plugin'
    doc = {
        plugin_type_name: [
            {'filename': './abc.py', 'name': 'baz'},
            {'filename': './xyz.py', 'name': 'bar'},
        ],
    }
    dc = DocCLI()
    dc.display_plugin_list(plugin_type_name, doc)
    output = '''
{0} [-]
    {1}
    {2}
'''.format('foo_plugin', 'bar', 'baz')
    assert display.display(output, log_only=True) == output

# Generated at 2022-06-12 20:24:46.302998
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    #
    # Role only has short description
    #

    # Create a new DocCLI object
    doc = DocCLI()

    # Role JSON
    role_json = {
        "entry_points": {
            "main": {
                "short_description": "This is the role short description."
            }
        }
    }

    # Create text
    text = doc.get_role_man_text("TestRole", role_json)

    # Check that the text is correct
    assert text == [
        '> TESTROLE    ()\n',
        'ENTRY POINT: main - This is the role short description.\n'
    ]

    #
    # Role has long description
    #

    # Create a new DocCLI object
    doc = DocCLI()

    # Role JSON
    role_

# Generated at 2022-06-12 20:24:53.948976
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    """test method get_all_plugins_of_type of class DocCLI"""
    #1. test module names

# Generated at 2022-06-12 20:24:57.148417
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    '''
    Unit test for method find_plugins of class DocCLI
    '''
    # set these environment variables to test this function
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = '/foo/bar'
    output = DocCLI.find_plugins()
    assert output == [('/foo/bar/ansible_collections/test/plugins', [])]


# Generated at 2022-06-12 20:25:00.075031
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    assert DocCLI.find_plugins('modules', 'my_test') == ('my_test', ['my_test'], [])


# Generated at 2022-06-12 20:25:03.118992
# Unit test for function jdump
def test_jdump():
    from .test.test_doc_gen import TestDocGen
    tdg = TestDocGen()
    jdump(tdg.test_data)



# Generated at 2022-06-12 20:25:12.358838
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    plugin = DocCLI()
    plugin.questions = [
        "What is an example of a return value?",
    ]
    plugin.responses = {
        "What is an example of a return value?": "test"
    }

# Generated at 2022-06-12 20:25:18.593274
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    '''Test format_plugin_doc'''
    # create a plugin of type module
    plugin = Plugin(
        name='test_plugin',
        description='test description',
        short_description='test short description',
        version_added='2.1',
        filename='test_plugin_filename',
    )
    # run method format_plugin_doc of class DocCLI
    # expected result is str
    test_result = isinstance(DocCLI.format_plugin_doc(plugin, plugin_type='module'), str)
    assert test_result == True, "result is not a str"
    # expected result is greater than 0
    test_result = len(DocCLI.format_plugin_doc(plugin, plugin_type='module')) > 0
    assert test_result == True, "result is not greater than 0"

#

# Generated at 2022-06-12 20:26:15.719609
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    '''test get_plugin_metadata'''
    fail_json, assertEqual = {'msg': ''}, __builtin__.assertEqual
    plugin_type = 'action_plugin'
    if 'action_plugin' ==  plugin_type:
        get_modules = ACTION_PLUGINS
    elif 'callback' ==  plugin_type:
        get_modules = CALLBACKS
    elif 'become' ==  plugin_type:
        get_modules = BECOME_PLUGINS
    elif 'connection' ==  plugin_type:
        get_modules = CONNECTION_PLUGINS
    elif 'cache' ==  plugin_type:
        get_modules = CACHE_PLUGINS
    else:
        fail_json['msg'] = 'Unsupported plugin type'
        return fail_json
   

# Generated at 2022-06-12 20:26:24.726811
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    opt_indent = "        "
    text = []
    limit = 70
    myoptions = dict()
    myoptions["name1"] = dict()
    myoptions["name1"]["description"] = "description1"
    myoptions["name1"]["choices"] = ("a","b","c")
    myoptions["name1"]["default"] = "b"
    myoptions["name1"]["version_added"] = "2.5"
    DocCLI.add_fields(text, myoptions, limit, opt_indent)
    assert('        NAME1: description1' in text)
    assert('        choices: a, b, c' in text)
    assert('        [Default: b]' in text)
    assert('        added in: 2.5' in text)
    text = []
    my

# Generated at 2022-06-12 20:26:30.171161
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    yaml_text =""
    yaml_text +='---'
    yaml_text += '- name: This is test'
    yaml_text += '  hosts: localhost'
    yaml_text += '  tasks:'
    yaml_text += '    - include_tasks: tasks/main.yml'
    host_list = None
    if yaml_text is not None:
        host_list = yaml.load(yaml_text,Loader=yaml.BaseLoader)
    for i in host_list:
        for j in i:
            print(j)
            print("")
test_DocCLI_add_fields()

# Generated at 2022-06-12 20:26:40.382888
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    from ansible.cli.doc import DocCLI
    from ansible.module_utils._text import to_text
    import ansible.utils.data
    import ansible.utils.plugin_docs
    import ansible.plugins.action.copy
    import ansible.plugins.action.command
    import ansible.plugins.action.script
    import ansible.plugins.action.debug
    import ansible.plugins.action.pause
    import ansible.plugins.action.ping
    import ansible.plugins.action.setup
    import ansible.plugins.action.wait_for
    import ansible.modules.system
    import ansible.modules.system.sysctl
    import ansible.modules.cloud
    import ansible.modules.cloud.amazon.ec2_asg
    import ansible.modules.cloud.amazon.ec2_

# Generated at 2022-06-12 20:26:53.446098
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    doc = DocCLI()
    fake_module_name = 'AnsibleFakeModule'

    def get_module_path_patch(module_name, prepend_basedir=True):
        module_path = '{0}/{1}'.format('./lib/ansible/modules', 'fake_module.py')
        return module_path

    with patch.object(doc, 'get_plugin_list') as mock_plugin_list:
        mock_plugin_list.return_value = ['fake_module']
        with patch.object(utils, 'module_finder') as mock_module_finder:
            with patch.object(ansible.utils.module_finder, 'get_module_path') as mock_mod_path:
                mock_mod_path.side_effect = get_module_path_patch

# Generated at 2022-06-12 20:26:59.790358
# Unit test for method get_man_text of class DocCLI

# Generated at 2022-06-12 20:27:05.423105
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # Arrange
    lines = []
    opts = {
        'key1': 'value1',
        'key2': {
            'choices': ['foo', 'bar'],
            'default': 'foo',
            'description': 'choice between foo and bar'
        }
    }

    # Act
    DocCLI.add_fields(lines, opts, 100, "    ")
    result = "".join(lines)

    # Assert
    assert 'key1: value1' in result
    assert 'key2:' in result
    assert 'choices: [foo, bar]' in result
    assert 'default: [Default: foo]' in result
    assert 'description: choice between foo and bar' in result


# Generated at 2022-06-12 20:27:15.998659
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    C = collections.namedtuple('C', 'display')
    C.display = Mock()
    C.display.colums = 80

# Generated at 2022-06-12 20:27:25.176566
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    test_args = {
        '_ansible_remote_tmp': tempfile.mkdtemp(suffix='.ansible_test'),
    }

    for key in ['ANSIBLE_MODULE_ARGS', 'ANSIBLE_MODULE_CONSTANTS']:
        if key in os.environ:
            del os.environ[key]

    if PY2:
        test_args['ANSIBLE_MODULE_ARGS'] = json.dumps(test_args)
    else:
        test_args['ANSIBLE_MODULE_ARGS'] = json.dumps(test_args, ensure_ascii=False)


# Generated at 2022-06-12 20:27:33.886104
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    modules = DocCLI().find_plugins('action', 'lib/ansible/plugins/action')
    assert modules
    modules = DocCLI().find_plugins('doc_fragments', 'lib/ansible/plugins/doc_fragments')
    assert modules
    modules = DocCLI().find_plugins('filter', 'lib/ansible/plugins/filter')
    assert modules
    modules = DocCLI().find_plugins('inventory', 'lib/ansible/plugins/inventory')
    assert modules
    modules = DocCLI().find_plugins('lookup', 'lib/ansible/plugins/lookup')
    assert modules
    modules = DocCLI().find_plugins('module_utils', 'lib/ansible/module_utils')
    assert modules

# Generated at 2022-06-12 20:29:56.933335
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    """Unit test for function add_collection_plugins"""
    # TODO: This needs a better mock, one that returns appropriate values for the supported_os of each plugin
    def _mock_list_collection_dirs(coll_filter=None):
        return ['collection_path']

    DocCLI.list_collection_dirs = _mock_list_collection_dirs

    plugin_list = dict()
    add_collection_plugins(plugin_list, 'action')
    # Using magical literal string rather than the value of the variable(s) this came from
    # to avoid later constant changes breaking this test
    assert plugin_list['collection_path:modules/action/test.py'] == 'test'



# Generated at 2022-06-12 20:30:03.543866
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:30:11.013875
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    # basics
    isinstance(DocCLI.get_plugin_metadata('action', 'ec2_vpc_route_facts'), dict)
    isinstance(DocCLI.get_plugin_metadata('action', 'win_ping', collection_name='ansible.windows'), dict)
    isinstance(DocCLI.get_plugin_metadata('become', 'win_ping'), dict)
    isinstance(DocCLI.get_plugin_metadata('cache', 'test'), dict)
    isinstance(DocCLI.get_plugin_metadata('callback', 'test'), dict)
    isinstance(DocCLI.get_plugin_metadata('connection', 'test'), dict)
    isinstance(DocCLI.get_plugin_metadata('filter', 'test'), dict)

# Generated at 2022-06-12 20:30:17.713311
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    from ansible.utils.color import stringc
    plugins = get_docstring_plugin_generator()

    display = Display()
    display.columns = 80

    # Using the json output, we can regenerate the text output used by Ansible
    text = []
    for plugin_type, plugin_names in plugins.items():
        for plugin_name in sorted(plugin_names):
            DocCLI.IGNORE = DocCLI.IGNORE + (plugin_type,)
            opt_indent = "        "
            text = []
            if plugin_type == 'module':
                doc, plainexamples, returndocs, metadata = get_docstring(plugins, plugin_type, plugin_name)

# Generated at 2022-06-12 20:30:18.916244
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    DocCLI.display_plugin_list('modules')

# Generated at 2022-06-12 20:30:23.169934
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    DocCLI.find_plugins = lambda *args, **kwargs: ('plugin1', 'plugin2')
    plugin_list = {}
    coll_filter = ['ansible_namespace.collection']
    add_collection_plugins(plugin_list, 'lookup', coll_filter)
    assert plugin_list == {'ansible_namespace.collection': {'lookup': ['plugin1', 'plugin2']}}
# end unit test


# Generated at 2022-06-12 20:30:27.313353
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    from ansible.cli import CLI
    plugin = CLI.get_cli_argparser().subparsers.choices.pop('DocCLI')
    # Test the xxx method using
    # ansible-doc DocCLI -t core -s xxx



# Generated at 2022-06-12 20:30:33.267360
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    doc_cli = DocCLI()

    role = "sasl"

# Generated at 2022-06-12 20:30:35.470177
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    cli = DocCLI()
    assert isinstance(cli.get_man_text(dict(description='test description',name = 'test name')), str)



# Generated at 2022-06-12 20:30:45.193648
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():

    import json
    import pytest

    cli = DocCLI()
    assert cli.format_snippet(['key1=value1', 'key2=value2']) == [u'key1="value1"', u'key2="value2"']
    assert cli.format_snippet(['key1="value1"', 'key2="value2"']) == [u'key1="value1"', u'key2="value2"']
    assert cli.format_snippet(['key1=\'value1\'', 'key2=\'value2\'']) == [u'key1=\'value1\'', u'key2=\'value2\'']