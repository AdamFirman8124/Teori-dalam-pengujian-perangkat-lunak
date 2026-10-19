

# Generated at 2022-06-12 20:24:24.740225
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    snippet_data1 = dict(
        platform='test_platform',
        snippet='test_snippet',
        options={'inventory': 'test_inventory',
                 'become_method': 'test_become_method',
                 'diff': 'test_diff',
                 'check': 'test_check',
                 'listhosts': 'test_listhosts',
                 'listtasks': 'test_listtasks',
                 'listtags': 'test_listtags',
                 'syntax': 'test_syntax'})


# Generated at 2022-06-12 20:24:30.337436
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    from ansible.module_utils._text import to_bytes

    i = DocCLI()
    meta = i.get_plugin_metadata()

    assert isinstance(meta, dict)
    assert meta[context.CLIARGS['type']] is not None
    assert meta['name'] is not None



# Generated at 2022-06-12 20:24:36.965745
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    from ansible.module_utils.common.text.converters import to_text as _to_text

    for plugin_filepath in [
        'foo/bar/bigip_monitor_dns.py',
        'foo/bar/bigip_monitor_http.py',
        'foo/bar/bigip_monitor_tcp.py',
        'foo/bar/bigip_monitor_udp.py',
    ]:
        assert DocCLI.namespace_from_plugin_filepath(plugin_filepath) == 'bigip_monitor'


# Generated at 2022-06-12 20:24:43.883775
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    s = """
    doc_plugin_list:
        foo:
            description: bar
        baz:
            path: /a/b/c/d.py
    """
    args = {'type': 'doc_plugin_list'}
    display = Display()
    display.columns = 80
    cli = DocCLI(args, display)
    cli._create_doc_dict(yaml.safe_load(s))
    cli.display_plugin_list()

    args['type'] = 'doc_plugin_list0'
    cli = DocCLI(args, display)
    cli._create_doc_dict(yaml.safe_load(s))
    cli.display_plugin_list()


# Generated at 2022-06-12 20:24:51.517955
# Unit test for method add_fields of class DocCLI

# Generated at 2022-06-12 20:25:00.618088
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    doc = {'description': 'This is a description of the module',
           'short_description': 'This is a short description of the module',
           'plainexamples': '> Show module output here.',
           'options': {'opt1':
                       {'description': 'description\nthat\ncontinues\nfor multiple lines.',
                        'default': 'value',
                        'choices': ['one', 'two', 'three'],
                        'aliases': ['answers_to_alias']}
                       }
           }
    DocCLI.IGNORE = []
    opt_indent = "        "
    text = []
    limit = 70
    pad = display.columns * 0.20
    limit = max(display.columns - int(pad), 70)
    assert limit == 70

    DocCLI.add_

# Generated at 2022-06-12 20:25:02.934527
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    c = DocCLI()
    c.run()
    return True

# Generated at 2022-06-12 20:25:05.409220
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    add_collection_plugins(plugin_list, 'lookup')
    assert 'unarchive' in plugin_list

# Generated at 2022-06-12 20:25:09.277156
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    plugin_type = 'action'
    context.CLIARGS = {'type':plugin_type}
    result = DocCLI().get_all_plugins_of_type()
    assert result
    assert isinstance(result, list)
    assert isinstance(result[0], string_types)

# Generated at 2022-06-12 20:25:16.760916
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    doctext = DocCLI()
    text = []
    limit = 70
    opt_indent = "        "

# Generated at 2022-06-12 20:26:31.224269
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    add_collection_plugins(plugin_list, 'module')
    assert 'ansible.posix.copy' in plugin_list
    assert 'copy' in plugin_list
    assert len(plugin_list) > 0



# Generated at 2022-06-12 20:26:40.639128
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    # Arrange
    DocCLI.base_dir = os.path.join("test", "unit", "utils", "doc-files", "collection")
    DocCLI.src_dir = os.path.join("test", "unit", "utils", "doc-files", "src")
    DocCLI.template_dir = os.path.join("test", "unit", "utils", "doc-files", "template")
    DocCLI.pdk_version = "0.0.15"
    DocCLI.collection_artifacts = []
    DocCLI.collection_name = "test"
    DocCLI.modules = []

    # Act
    plugins = DocCLI.get_all_plugins_of_type()

    # Assert
    assert len(plugins) == 1

# Generated at 2022-06-12 20:26:44.542677
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    plugin_type = 'module'
    coll_filter = []
    add_collection_plugins(plugin_list, plugin_type, coll_filter=coll_filter)
    return plugin_list

# Generated at 2022-06-12 20:26:49.900447
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    a = {'action': {'short_description': 'Action plugins', 'description': ''}, 'module': {'short_description': 'Core modules', 'description': ''}}
    assert DocCLI.get_plugin_metadata(a) == ('{action: Action plugins, module: Core modules}', 0)

# Generated at 2022-06-12 20:26:58.364719
# Unit test for method print_paths of class DocCLI
def test_DocCLI_print_paths():
    from ansible.utils.display import Display
    from ansible.cli import CLI
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils._text import to_bytes
    from ansible.collections.collection_loader import AnsibleCollectionLoader


# Generated at 2022-06-12 20:27:04.426975
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    ansible_collection_name = 'cloud.vmware.nsxt'
    ansible_module_type = 'module'
    # doc_cli is a DocCLI object of class DocCLI
    doc_cli = DocCLI(ansible_collection_name, ansible_module_type)
    plugins = doc_cli.get_all_plugins_of_type()
    if len(plugins) == 0:
        raise Exception("Test case 1: test_DocCLI_get_all_plugins_of_type() failed")

    # calling the base class constructor explicitly
    DocCLI.__init__(doc_cli, C.DEFAULT_COLLECTION_NAME, 'module')
    plugins = doc_cli.get_all_plugins_of_type()

# Generated at 2022-06-12 20:27:14.596340
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    basic_args = {'type': 'module', 'output': 'yaml'}
    assert DocCLI.run(basic_args)
    basic_args['output'] = 'json'
    assert DocCLI.run(basic_args)
    basic_args['output'] = 'txt'
    assert DocCLI.run(basic_args)
    basic_args['output'] = 'md'
    assert DocCLI.run(basic_args)
    basic_args['output'] = 'persist'
    assert DocCLI.run(basic_args)
    basic_args['output'] = 'name_only'
    assert DocCLI.run(basic_args)
    basic_args['listt'] = True
    assert DocCLI.run(basic_args)
    basic_args['listt'] = False
    basic

# Generated at 2022-06-12 20:27:19.142470
# Unit test for function jdump
def test_jdump():
    jdump('{"test":1}')
    jdump([1,2,3])
    jdump([1,[2,3,4],5])
    jdump({'a':{'b':1,'c':2,'d':[1,2,3,4]}})
# end of unit test


# Generated at 2022-06-12 20:27:26.957587
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
  # create an instance of DocCLI
  dcli = DocCLI()
  # declara a variable of type dict
  plugins = dict()
  # add an entry to plugins dict
  plugins['foo'] = dict()
  # set the description of plugins['foo']
  plugins['foo']['description'] = "Foo is a thing"
  # set the version_added of plugins['foo']
  plugins['foo']['version_added'] = "1.2"
  # set the filename of plugins['foo']
  plugins['foo']['filename'] = "Foo"
  # set the has_action of plugins['foo']
  plugins['foo']['has_action'] = False
  # call the function display_plugin_list with parameters plugin and plugins
  dcli.display_plugin_list('plugin', plugins)

#

# Generated at 2022-06-12 20:27:36.010844
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
  # No args
  assert DocCLI._find_plugins('action') == []

  # Good args
  assert DocCLI._find_plugins('action', {'_ansible_base': './lib/ansible'}, '../lib/ansible/plugins/action') != []

  # Bad path
  assert DocCLI._find_plugins('action', {'_ansible_base': './lib/ansible'}, './lib/ansible/plugins/action_fakes') == []

  # Bad collection
  assert DocCLI._find_plugins('action', {'_ansible_collection_base': './lib/ansible'}, './lib/ansible/plugins/action') == []

  # Good collection

# Generated at 2022-06-12 20:29:11.036418
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():

    # set up context
    iris_obj = {}
    iris_obj['type'] = 'module'
    iris_obj['filename'] = './lib/ansible/modules/cloud/amazon/ec2_ami_find.py'
    iris_obj['description'] = ['This module is used to find AMI images which match the supplied search criteria.']
    iris_obj['requirements'] = ['botocore']
    iris_obj['author'] = 'Will Thames <will@thames.id.au>'
    iris_obj['version_added'] = '2.2'
    iris_obj['options'] = {}
    iris_obj['options']['release'] = {}
    iris_obj['options']['release']['type'] = 'str'

# Generated at 2022-06-12 20:29:19.182591
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    '''
    unit test for DocCLI.add_fields()
    '''
    # Set up test input
    text = []
    limit = 120
    opt_indent = "    "
    opt = {
        "required": False,
        "description": "description text",
        "default": "test string",
        "version_added": "2.4",
        "options": [
            "option1",
            "option2",
            "option3"
        ]
    }
    return_values = []

    # Invoke class method and check results
    DocCLI.add_fields(text, opt, limit, opt_indent, return_values, opt_indent)


# Generated at 2022-06-12 20:29:20.782764
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    doc = dict()
    text = DocCLI.get_man_text(doc)
    assert len(text) == 0


# Generated at 2022-06-12 20:29:22.524512
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    pass

# Generated at 2022-06-12 20:29:23.432283
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    # No test yet
    assert True

# Generated at 2022-06-12 20:29:27.488305
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    expected = 'test_namespace'
    cli = DocCLI()
    actual = cli.namespace_from_plugin_filepath('/test/test/test_namespace/test.py')
    assert expected == actual


# Generated at 2022-06-12 20:29:36.385372
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    # Find plugins of type module
    plugin_dirs = (
        os.path.join(os.path.dirname(__file__), "../../plugins/modules"),
        os.path.join(os.path.dirname(__file__), "../../test/units/plugins/modules"),
    )

    plugins = DocCLI.find_plugins(os.path.sep.join(plugin_dirs), subdirs=('.',))
    # As DocCLI is not a AnsibleModule() class, we cannot use the find_plugins method
    # directly, but the result of the method is used in an another method. This is
    # only a test to make sure that the list of plugins found is not empty.
    assert len(plugins) > 0



# Generated at 2022-06-12 20:29:43.928007
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    from ansible.cli.doc import DocCLI
    from test.mock.loader import DictDataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-12 20:29:46.498361
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    from ansible.plugins import module_loader
    # Assuming that tempfile.mkdtemp returns '/tmp/tmp123'
    mod_path = module_loader._get_paths(directories=['/tmp/tmp123'])
    assert mod_path == ['/tmp/tmp123']

# Generated at 2022-06-12 20:29:56.933673
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    ansible_collection_loader = importlib.import_module('ansible.utils.collection_loader')
    from ansible.utils.collection_loader import find_collections, find_collection_roles, find_collection_plugins
    ansible_collection_loader.find_collections = find_collections
    ansible_collection_loader.find_collection_roles = find_collection_roles
    ansible_collection_loader.find_collection_plugins = find_collection_plugins
    test_collections = 'ansible.module_utils.common.collections_compat.module_collection_name'
    module_collection_name = lambda: 'include_role'
    plugin_list = dict()
    curpath = os.path.abspath(os.path.dirname(__file__))

# Generated at 2022-06-12 20:31:03.085539
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    assert DocCLI.namespace_from_plugin_filepath("/a/b/c/d/e/f/g/h/i") == "h.i"


# Generated at 2022-06-12 20:31:09.593265
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    doccli = DocCLI

    # test module snippet with connection
    snippet = '''#!/usr/bin/python

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'version': '1.0'}

DOCUMENTATION = ''' + "'''" + '''
---
module: test
short_description: test
description:
  - test
version_added: "2.4"
author:
  - test (@test)
options:
  name:
    description:
      - test
    required: false
''' + "'''" + '\n'

# Generated at 2022-06-12 20:31:19.520639
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    from ansible.module_utils.six import StringIO
    from ansible.utils.display import Display
    from ansible.utils.vars import AnsibleVars
    from ansible.plugins.loader import plugin_loader
    from ansible.parsing.plugin_docs import read_docstring

    display = Display()
    display.columns = 1000

    filename = '%s/plugins/doc_fragments/action_plugins/copy.py' % os.path.dirname(ansible.__file__)
    filename_yaml = '%s.yaml' % os.path.splitext(filename)[0]
    collection_name = None
    fake_vars = AnsibleVars(loader=None)

    # load the docfragment

# Generated at 2022-06-12 20:31:24.034626
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    docCLI = DocCLI()
    assert docCLI.get_man_text([{'name': 'test_module'}], collection_name='test_collection', plugin_type='test_type') == '''
> TEST_COLLECTION.TEST_MODULE    (unknown)
'''


# Generated at 2022-06-12 20:31:31.177005
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # Test Case 1
    my_dict = {
        "ansible_facts": "Dictionary containing modules return values",
        "_ansible_verbosity": "The verbosity level",
        "examples": "show_how_to_use_the_module",
        "aliases": [
            "a",
            "b"
        ],
        "version_added": "2.3",
        "disp": "value",
        "kwarg2": "value2"
    }
    opt_indent = "        "
    limit = 70
    text = []
    DocCLI.add_fields(text, my_dict, limit, opt_indent)
    fields = len(text)
    assert fields == 7


# Generated at 2022-06-12 20:31:34.262306
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    assert '\n'.join(DocCLI.format_snippet(['- name: ping', '  ping:', '    data: pong'], indent=2))  == '\n'.join([
        '- name: ping',
        '  ping:',
        '    data: pong'
    ])

# Generated at 2022-06-12 20:31:43.506871
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    print("starting test_DocCLI_get_role_man_text")
    test_DocCLI = DocCLI()
    try:
        test_DocCLI.get_role_man_text("role", {"entry_points":{"test":{"short_description":"test"}}})
    except Exception as e:
        print("Failed to run test_DocCLI_get_role_man_text with error:")
        print(str(e))
        traceback.print_exc()
        print("Reloading collection_loader")
        importlib.reload(collection_loader)
        print("Reloading command")
        importlib.reload(command)
        print("Reloading constants")
        importlib.reload(constants)
        print("Reloading data_loader")

# Generated at 2022-06-12 20:31:44.944929
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    doc = DocCLI(type='module')
    doc.display_plugin_list('module', 'core')

# Generated at 2022-06-12 20:31:53.053944
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    assert to_text(b_path, errors='surrogate_or_strict') == 'collection_dir/name'
    assert _get_collection_name_from_path(b_path) == 'collection_dir/name'
    assert C.COLLECTION_PTYPE_COMPAT.get(plugin_type, plugin_type) == 'lookup'
    assert os.path.join(path, 'plugins', ptype) == 'collection_dir/name/plugins/lookup'


# Generated at 2022-06-12 20:31:54.775202
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    assert False