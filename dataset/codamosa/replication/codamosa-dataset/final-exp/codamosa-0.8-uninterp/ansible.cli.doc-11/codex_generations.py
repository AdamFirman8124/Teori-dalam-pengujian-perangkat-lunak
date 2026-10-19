

# Generated at 2022-06-12 20:23:37.907979
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    # Asserting that get_plugin_metadata() works as expected
    assert DocCLI.get_plugin_metadata(first=[1, 2], second={'key': 'value'}) == {'first': [1, 2], 'second': {'key': 'value'}}




# Generated at 2022-06-12 20:23:43.480263
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    output = []
    filepath = 'test/unit/plugins/modules/test_module.py'
    doc, plainexamples, returndocs, metadata = get_docstring(filepath)
    output.append(DocCLI.format_plugin_doc(filepath, doc))
    output.append(DocCLI.format_plugin_doc(filepath, doc, plainexamples))
    output.append(DocCLI.format_plugin_doc(filepath, doc, plainexamples, returndocs))
    output.append(DocCLI.format_plugin_doc(filepath, doc, plainexamples, returndocs, metadata))
    output = "\n".join(output)
    #print(output)

# Generated at 2022-06-12 20:23:53.940606
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    doc_ = {
    'description': ['This module provides a basic example of a module with a single parameter.  The parameter '
                    'is named `state` and it can be passed twice, resulting in the module returning `changed`.'],
    'options': {
        'state': {
            'description': ['The state to assert.\n'],
            'required': True,
            'type': 'str',
            'choices': ['present', 'absent', 'changed'],
            'default': 'changed'
        }
    }
}
    doc = dict(doc_)
    opt_indent = "        "
    pad = display.columns * 0.20
    limit = max(display.columns - int(pad), 70)
    text = []

# Generated at 2022-06-12 20:23:59.212958
# Unit test for function jdump
def test_jdump():
    #pylint: disable=missing-docstring
    json_obj = dict(hello=dict(world="it's me!"))
    assert jdump(json_obj) == json.dumps(json_obj, cls=AnsibleJSONEncoder, sort_keys=True, indent=4)



# Generated at 2022-06-12 20:24:00.582945
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    import doctest
    doctest.testmod(DocCLI)


# Generated at 2022-06-12 20:24:07.798839
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    import sys
    import os
    import inspect
    import doctest
    #import imp
    #import DocCLI
    #import importlib
    import unittest
    import ansible.utils
    #print(ansible.utils.__file__)
    from ansible.utils import plugins
    from ansible.module_utils import basic

    print(basic.__file__)
    mypath = os.path.dirname(plugins.__file__)
    #print(mypath)
    discover = unittest.defaultTestLoader.discover(mypath, pattern="*.py") 
    #print(discover)
    runner = unittest.TextTestRunner()
    runner.run(discover)

    #imp.reload(DocCLI)

    #DocCLI.main()

    currentdir = os.path

# Generated at 2022-06-12 20:24:15.925268
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    plugin_name = 'testmod'
    doc = {
        'description': 'Test module',
        'module': plugin_name
    }
    plugin_type = 'module'
    collection_name = 'testcol'
    description = DocCLI.format_plugin_doc(doc, plugin_name, plugin_type, collection_name, 1)
    expected_description = [
        u"TESTMOD    (ansible.builtin.testmod)",
        u"",
        u"  Test module"
    ]
    assert expected_description == textwrap.wrap(description, 70)


# Generated at 2022-06-12 20:24:26.946544
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    c = DocCLI()
    input_parameters = dict(
        text = [],
        options = {
            'foo': {
                'description': """
                    this is a long option
                    that might span multiple lines,
                    and it does!
                    """,
                'type': "str",
                'default': "bar"
            },
            'bar': {
                'description': "this is a short option",
                'type': "bool",
                'default': False
            }
        },
        limit = 70,
        opt_indent = "        ",
        return_values = False,
        module_opts_indent = '    '
    )

# Generated at 2022-06-12 20:24:30.708311
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    mod = DocCLI()
    mod.display_plugin_list(plugins=None, directories=None, collection_name=None, ext_filter=None, version=None)


# Generated at 2022-06-12 20:24:39.110681
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    # Given
    role = 'role'
    role_json = {'path': 'path', 'entry_points': {'module': {'module': 'module', 'options': [{}, {}], 'attributes': [{}, {}], 'description': 'description', 'short_description': 'short'}}}
    # When
    doc = DocCLI()

    # Then
    assert doc.get_role_man_text(role, role_json) == ['> ROLE    (path)\n', 'ENTRY POINT: module - short\n', '        description\n', 'OPTIONS (= is mandatory):\n', 'ATTRIBUTES:\n', "{   \n", '            Key: Key\n', '            Key: Key\n', "}\n"]



# Generated at 2022-06-12 20:27:02.896132
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    # Check if we can get at least the help of the ping module
    assert DocCLI.get_man_text(DocCLI.create_plugin_doc(ping.ActionModule()))
    # Check for a specific case for the augeas module
    assert DocCLI.get_man_text(DocCLI.create_plugin_doc(modules.augeas.ActionModule()))
    # Check for a specific case for the async_status module
    assert DocCLI.get_man_text(DocCLI.create_plugin_doc(async_status.ActionModule()))


# Generated at 2022-06-12 20:27:13.792650
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible.utils.display import Display
    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import get_all_plugin_loaders
    import pytest

    # Create an instance of CLI class
    cli = CLI(['-m', 'setup', '-i', 'test_inventory', 'localhost'])

    # Create an instance of Display class
    display = Display()
    display.verbosity = 4
    display.columns = 80

   

# Generated at 2022-06-12 20:27:23.415698
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():

  # Test with options.
  cli.options = {
      'type' : 'cliconfig',
      'listt' : True,
      'tree' : False,
      'all' : False
  }

  doc = DocCLI()
  doc._collect_plugin_docs(cli.options['type'])
  result = doc.get_all_plugins_of_type(cli.options['type'])

  # Check if the plugin type is cliconfig.
  assert 'cliconfig' in result.keys(), "get_all_plugins_of_type is not working with options"

  # Test without options.
  doc = DocCLI()
  doc._collect_plugin_docs()
  result = doc.get_all_plugins_of_type()

  # Check if the plugin type is not cliconfig.
 

# Generated at 2022-06-12 20:27:31.415273
# Unit test for method run of class DocCLI
def test_DocCLI_run():

    doccli = DocCLI()
    display = Display()
    versioned_doclink = get_versioned_doclink()
    doc_data = {'module': 'example', 'collection': None, 'display': {'versioned_doclink': versioned_doclink}}
    doc_loader = DocLoader()
    data = {'doc': {'files': [{'name': 'example', 'path': '/home/user/ansible/lib/ansible/module_utils/example.py'}]}, 'module_name': None, 'collection_name': None}

# Generated at 2022-06-12 20:27:33.383666
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    obj = DocCLI()
    print(obj.get_man_text({'description': 'description', 'name': 'name', 'options': [{'name': 'options_name', 'description': 'options_description'}]})) # noqa

#Unit test for method organize_docs of class DocCLI

# Generated at 2022-06-12 20:27:38.393331
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():

    os.chdir('../')
    doc = DocCLI('')
    import json
    json_filename = 'test/test_json_half.json'
    with open(json_filename, 'r') as stream:
        plugin_list = json.load(stream)

    display.verbosity = 2
    display.columns = 120
    doc.display_plugin_list(plugin_list, 'action')

    display.columns = 40
    doc.display_plugin_list(plugin_list, 'action')


# Generated at 2022-06-12 20:27:46.098119
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = []
    coll_filter = "*"
    plugin_type = "action"
    b_colldirs = list_collection_dirs(coll_filter=coll_filter)
    for b_path in b_colldirs:
        path = to_text(b_path, errors='surrogate_or_strict')
        collname = _get_collection_name_from_path(b_path)
        ptype = C.COLLECTION_PTYPE_COMPAT.get(plugin_type, plugin_type)
        tmp = DocCLI.find_plugins(os.path.join(path, 'plugins', ptype), False, plugin_type, collection=collname)
    assert len(tmp) > 0
    assert isinstance(plugin_list, list)



# Generated at 2022-06-12 20:27:54.001380
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    test_plugin_list = {}
    test_coll_filter = 'test-collection'
    test_plugin_type = 'action'
    add_collection_plugins(test_plugin_list, test_plugin_type, test_coll_filter)
    assert isinstance(test_plugin_list, dict)
    assert (len(test_plugin_list.keys()) > 0)



# Generated at 2022-06-12 20:28:03.782916
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    assert DocCLI().namespace_from_plugin_filepath('/usr/lib/python2.7/dist-packages/ansible/plugins/action/test.py') == 'action'
    assert DocCLI().namespace_from_plugin_filepath('/usr/lib/python2.7/dist-packages/ansible/plugins/connection/test.py') == 'connection'
    assert DocCLI().namespace_from_plugin_filepath('/usr/lib/python2.7/dist-packages/ansible/plugins/doc_fragments/test.py') == 'doc_fragments'
    assert DocCLI().namespace_from_plugin_filepath('/usr/lib/python2.7/dist-packages/ansible/plugins/filter/test.py') == 'filter'
    assert DocCLI().names

# Generated at 2022-06-12 20:28:10.897065
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from unittest import TestCase
    # Stub display.columns
    display.columns = 100

    class TestDocCLI_display_plugin_list(TestCase):
        @mock.patch('ansible.cli.doc.DocCLI.get_man_text')
        @mock.patch('ansible.cli.doc.DocCLI.get_role_man_text')
        @mock.patch('ansible.cli.doc.AnsiblePluginLoader')
        def test_display_plugin_list(self, plugin_loader, get_role_man_text, get_man_text):
            command = DocCLI(['ansible-doc', '--version'])
            # stub out items in plugin_loader.all that we will test

# Generated at 2022-06-12 20:29:13.456111
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    names = ['module', 'shell', 'lookup']
    dirs = [os.path.join(os.getcwd(), 'lib'), os.path.join(os.getcwd(), 'plugins')]

    plugins = DocCLI.find_plugins(names, dirs)

    assert plugins

# Generated at 2022-06-12 20:29:16.603274
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    class_instance = DocCLI()
    class_instance.find_plugins(
            plugin_type = '',
            pattern = '',
            search_path = '',
            collection_name = ''
            )

# Generated at 2022-06-12 20:29:18.274341
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    plugin_reader = DocCLI._PluginReader()
    result = plugin_reader.get_all_plugins_of_type('callback')
    assert len(result) > 0


# Generated at 2022-06-12 20:29:27.530791
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    DocCLI.add_fields(text, {'test': 'hello'}, 20, '  ')
    assert text == ['  test: hello']
    DocCLI.add_fields(text, {'test': ['hello', 'world']}, 20, '  ')
    assert text == ['  test: hello, world']
    text = []
    DocCLI.add_fields(text, {'test': 'hello', 'test2': 'world'}, 20, '  ')
    assert text == ['  test: hello', '  test2: world']
    DocCLI.add_fields(text, {'test': {'new': 'hello'}}, 20, '  ')
    assert text == ['  test:', '    new: hello']

# Generated at 2022-06-12 20:29:30.657021
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list, plugin_type = {}, 'module'
    coll_filter = None
    add_collection_plugins(plugin_list, plugin_type, coll_filter)


# Generated at 2022-06-12 20:29:31.982401
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    doc = DocCLI()
    doc.display_plugin_list()



# Generated at 2022-06-12 20:29:37.564937
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    options = [{'name': 'jonas', 'version_added': '2.4'}, {'name': 'joe'}]
    text = []
    DocCLI.add_fields(text, options, limit=100, opt_indent='    ')
    assert len(text) == 4
    assert text[0] == '    JONAS: [Introduced in Ansible 2.4] (string)'
    assert text[1] == ''
    assert text[2] == '    JOE: (string)'
    assert text[3] == ''

# Generated at 2022-06-12 20:29:45.472881
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible.utils.display import Display
    display = Display()
    display.columns = 80

    def _create_cache_entry(plugin_name, collection_name, version_added=None, version_added_collection=None, filename=None):
        cache_entry = Mock()
        cache_entry.plugin_name = plugin_name
        cache_entry.collection_name = collection_name
        cache_entry.module_name = plugin_name
        cache_entry.api_version = '2.0'
        cache_entry.short_description = 'short description'
        cache_entry.version_added = version_added
        cache_entry.version_added_collection = version_added_collection
        cache_entry.filename = filename
        return cache_entry


# Generated at 2022-06-12 20:29:48.178776
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    # test that find_plugins finds something
    plugins = DocCLI.find_plugins()
    assert plugins is not None
    assert isinstance(plugins, list)
    assert len(plugins) > 0


# Generated at 2022-06-12 20:29:58.904950
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible import constants as C
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import fragment_loader
    from ansible.plugins.callback import callback_loader
    from ansible.utils.display import Display
    from ansible.cli.arguments import option_helpers as opt_help

    display = Display()
    doc = DocCLI(
        doc_fragment=fragment_loader,
        doc_module=module_loader,
        doc_callback=callback_loader,
        display=display,
        verbosity=3,
        type='module',
        subtype='',
    )

    # testing with empty plugin list
    plugin_list = []
    assert doc.display_plugin_list(plugin_list) is None
    # testing with valid plugin list

# Generated at 2022-06-12 20:31:05.309287
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    from ansible.utils import vars_load_yaml
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.module_utils.six import iteritems, string_types
    from ansible.module_utils._text import to_text

    results = DocCLI.get_man_text(vars_load_yaml(to_text(DocCLI.get_man_text.__doc__)))

    assert isinstance(results, string_types)
    assert isinstance(vars_load_yaml(results), AnsibleBaseYAMLObject)



# Generated at 2022-06-12 20:31:14.356195
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = {
        'description':
            'Test module.\n'
            'This module does nothing really.',
        'options':
            {
                'name':
                    {
                        'description': 'The name of the thing',
                        'required': True
                    },
                'type':
                    {
                        'description': 'The type of the thing',
                        'required': True,
                        'choices': ['A', 'B', 'C']
                    },
                'file':
                    {
                        'description': 'The type of the thing',
                        'required': True,
                        'choices': ['A', 'B', 'C'],
                        'aliases': ['dest', 'destfile']
                    }
            },
        'filename': "./test/file.py"
    }

# Generated at 2022-06-12 20:31:25.043638
# Unit test for method add_fields of class DocCLI

# Generated at 2022-06-12 20:31:32.575172
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_text
    md = {
        "name": "example_module",
        "filename": "example_module.py",
        "description": "This module does something",
        "version_added": "2.2",
        "options": {
            "name": {
                "description": "The C(name) argument controls something.",
                "required": True,
                "type": "str",
                "default": "default.name"
            },
            "age": {
                "description": "The C(age) option does something else.",
                "required": False,
                "type": "int",
                "default": 42
            }
        }
    }

# Generated at 2022-06-12 20:31:41.902399
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # Inject a fixture
    text = []

# Generated at 2022-06-12 20:31:48.572514
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # Test all possible cases of fields

    options = {
        'test1': 'test_value1',
        'test2': {
            'test1': 'test_value1',
            'test2': ['test_value1', 'test_value2'],
            'test3': {
                'test1': 'test_value1',
            }
        },
        'test3': [
            {'name': 'test_value1'},
            {'name': 'test_value2'}
        ],
        'test4': [
            'test_value1'
        ],
        'test5': '',
        'test6': None
    }
    
    text = []
    limit = 70
    opt_indent = '        '
    return_values = False

# Generated at 2022-06-12 20:31:51.792742
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    """Unit test for method get_plugin_metadata of class DocCLI"""
    pass

# Generated at 2022-06-12 20:31:53.906810
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    # No need to test, as this method is a simple wrapper around get_man_text
    pass