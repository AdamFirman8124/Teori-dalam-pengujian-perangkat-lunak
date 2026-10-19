

# Generated at 2022-06-12 20:25:04.060327
# Unit test for method get_role_man_text of class DocCLI

# Generated at 2022-06-12 20:25:12.882930
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    from ansible.cli.doc import DocCLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import role_loader
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    doc = DocCLI(None)
    collection_loader = AnsibleCollectionLoader()

    test_role_path = os.path.join(os.path.dirname(__file__), 'fixtures/test_roles/doc_display_role')
    test_role_data = collection_loader.load_role_definition(test_role_path)
    display_text = doc.get_role_man_text('doc_display_role', test_role_data)
    assert isinstance(display_text, list)

# Generated at 2022-06-12 20:25:21.854631
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    doc = yaml.safe_load("""
options:
  - a_b_c
    description:
      - abc
  - x_y_z
    description:
      - xyz""")
    cli = DocCLI()
    text = []
    cli.add_fields(text, doc)
    assert text == ["""        A_B_C: abc""", """        X_Y_Z: xyz"""]


# Generated at 2022-06-12 20:25:26.049093
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    cli = DocCLI()
    data = {'setting': 'setting_value', 'setting2': 'setting2_value'}
    result = cli.get_plugin_metadata(**data)
    assert isinstance(result, dict)
    assert result == data


# Generated at 2022-06-12 20:25:34.030750
# Unit test for method get_role_man_text of class DocCLI

# Generated at 2022-06-12 20:25:42.938330
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    from ansible.module_utils.six import string_types
    from ansible.utils.display import Display
    doc = {
        'module': 'test',
        'short_description': 'test module for testing formatting',
        'description': 'test module for testing formatting of modules for ansible -cli',
        'options': {
            'test': {
                'description': 'this is a test',
                'choices': ['hello', 'goodbye', 'hey'],
                'default': 'hello'
            }
        },
        'seealso': [
            'test',
            {'module': 'hello'},
            {'name': 'World', 'ref': 'intro_configuration'}
        ],
        'requirements': ['test']
    }
    res

# Generated at 2022-06-12 20:25:52.978099
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    print('in test_DocCLI_run')


# Generated at 2022-06-12 20:25:57.691416
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugins = {}
    add_collection_plugins(plugins, 'action')
    add_collection_plugins(plugins, 'module', coll_filter='k8s')
    assert 'k8s.yml' in plugins['k8s.core.v1.config_map'].get_doc()



# Generated at 2022-06-12 20:26:04.256710
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    type = 'modules'
    collection_list = [{'name': 'google'}, {'name': 'google.cloud'}]
    cli = DocCLI()
    ans = cli.find_plugins(type, collection_list)

# Generated at 2022-06-12 20:26:07.101608
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    # TODO: implement a mock of the list_collection_dirs and test
    pass



# Generated at 2022-06-12 20:27:35.474948
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    '''Unit test for format_snippet of class DocCLI.'''
    # A simple test to ensure that no exceptions are raised.
    # This test also covers the _format_version_added method
    DocCLI.format_snippet(doc={"version_added": "2.0", "filename": "test.py"})

# Generated at 2022-06-12 20:27:40.287292
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    import os
    import json

    def _test_doc(doc, **kwargs):
        doc_path = os.path.join('test/units/cli/doc/', doc)
        doc_json = json.load(open(doc_path))
        text = DocCLI.get_man_text(doc_json, **kwargs)
        assert all(isinstance(line, string_types) for line in text)
        assert len(text) > 20
        assert text.startswith("> ANSIBLE.COMMUNITY.CLOUD.GCE_ALIAS_MODULE.CLOUD.GCE_ALIAS_MODULE    (lib/ansible/plugins/cloud/gce_alias_module.py)")

    _test_doc('module.json')

# Generated at 2022-06-12 20:27:43.884246
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    args = dict(type='action', module='setup')
    doc = DocCLI(args)
    module.exit_json = Mock(return_value=None)
    module.fail_json = Mock(return_value=None)
    module.params = args
    with pytest.raises(SystemExit):
        doc.run()


# Generated at 2022-06-12 20:27:45.951032
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    path = "library/ntp_facts.py"
    expected = "--name library.ntp_facts"


# Generated at 2022-06-12 20:27:52.149875
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    coll_filter = ["namespace"]
    plugin_list = []
    plugin_type = "modules"
    DocCLI.add_collection_plugins(plugin_list, plugin_type, coll_filter)
    return plugin_list



# Generated at 2022-06-12 20:27:54.445298
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    # Testing if the method exists
    assert callable (getattr(DocCLI, 'get_role_man_text'))

# Generated at 2022-06-12 20:28:04.140715
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible.cli import CLI
    from ansible.module_utils._text import to_text
    from ansible.cli.doc import DocCLI

    cli = CLI(args=[])
    doc = DocCLI(cli)
    # Case 1
    plugin_list = ['test_module1', 'test_module2']
    output = "[test_module1]\n[test_module2]\n"
    assert(to_text(doc.display_plugin_list(plugin_list), errors='surrogate_or_strict') == output)
    # Case 2
    plugin_list = ['test_module1', 'test_module2', 'test_module2']
    output = "[test_module1]\n[test_module2]\n"

# Generated at 2022-06-12 20:28:05.613825
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
  params = DocCLI.format_plugin_doc()
  assert type(params) is str


# Generated at 2022-06-12 20:28:12.138516
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    import sys
    import ansible.utils.display
    from ansible.utils.display import Display
    display = Display()
    display.columns = 80

    def test_get_versioned_doclink(doc):
        return 'http://docs.ansible.com/ansible/%s' % doc

    def versioned_txt(doc):
        return 'ansible-doc %s' % doc

    import ansible.plugins
    import ansible.modules
    import ansible.module_utils
    mock_plugins = os.path.join(os.path.dirname(__file__), 'mock_plugins')
    ansible.plugins.__path__ = [mock_plugins]
    ansible.modules.__path__ = [mock_plugins]

# Generated at 2022-06-12 20:28:23.885240
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    options = [
        Option({
            'name': 'description',
            'description': ['description'],
            'required': True,
            'choices': ['a', 'b', 'c']
        })
    ]
    env = {
        'name': 'foobar'
    }

    with pytest.raises(ValueError):
        DocCLI.format_snippet('foobar', 'shell', '', {})
    with pytest.raises(ValueError):
        DocCLI.format_snippet('foobar', 'shell', '', env, [])
    assert DocCLI.format_snippet('foobar', 'shell', '', env, options) == "export FOOBAR_DESCRIPTION='description'\n"

# Generated at 2022-06-12 20:30:07.007267
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    class TestDocCLI(DocCLI):
        @staticmethod
        def tty_ify(text):
            return text
    doc = {'options': {'name': {
            'version_added': '2.3',
            'aliases': ['name', 'fqdn'],
            'default': '"jack"',
            'description': 'This is a test'
        }}}
    test_doc = copy.deepcopy(doc)
    test_doc['options']['name']['description'] = 'This is a\ntest'
    output = TestDocCLI.get_man_text(doc)
    assert('\nThis is a test' in output)
    output = TestDocCLI.get_man_text(test_doc)
    assert('\nThis is a\ntest' in output)

# Generated at 2022-06-12 20:30:12.447218
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
  doc = """
  - name: Dump an Ansible module's documentation
    debug: msg="{{ lookup('ansible.builtin.module_docs', 'core.system') }}"
  
  # Print the documentation for a specific module argument/attribute
  - name: Print the documentation for the 'foo' variable of the 'ping'
          module
    debug: msg="{{ lookup('ansible.builtin.module_docs', 'ping', 'foo') }}"
  """


# Generated at 2022-06-12 20:30:18.261765
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():

    doc = {
        "description": "Ansible module for managing network devices",
        "options": {
            "author": "Ansible core team",
            "connection": "local",
            "description": "The connection to use when connecting to the remote device over SSH.  If the value is not specified in the task, the value of environment variable ANSIBLE_NET_CONNECTION will be used instead.",
            "required": False,
            "type": "str",
            "version_added": "2.3"
        },
        "version_added": "2.0"
    }


# Generated at 2022-06-12 20:30:21.639923
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    # TODO: implement test for DocCLI.find_plugins
    # TODO: consider using assert_equal() instead of die()
    die("TODO: implement test for DocCLI.find_plugins")

# Generated at 2022-06-12 20:30:28.273384
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    sample_snippets = [
        dict(
            description='sample snippet',
            options=dict(key='value'),
            playbook='playbook.yml',
        )
    ]
    expected_output = """
- name: sample snippet
  hosts: localhost
  tasks:
    - name: foo
      debug:
        msg: "value"
"""
    assert DocCLI.format_snippet(sample_snippets) == expected_output


# Generated at 2022-06-12 20:30:33.859587
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    # Test with a plugin
    plugin=DocCLI()
    plugin_name='setup'
    result=plugin.get_plugin_metadata(plugin_name)
    assert 'directory' in result
    assert result['directory']=='core'
    assert 'module' in result
    assert result['module']=='ansible.module_utils.basic'
    assert 'type' in result
    assert result['type']=='module'
    assert 'filename' in result
    assert result['filename']=='/usr/lib/python3.6/site-packages/ansible/modules/system/setup.py'
    assert 'docuri' in result
    assert result['docuri']=='setup'
    assert 'name' in result
    assert result['name']=='setup'
    assert 'description' in result

# Generated at 2022-06-12 20:30:43.477761
# Unit test for method get_role_man_text of class DocCLI

# Generated at 2022-06-12 20:30:44.816187
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    assert DocCLI.format_snippet("test") == "test"

# Generated at 2022-06-12 20:30:50.667327
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    null = None
    # Test when the snippet is empty
    snippet = ''
    output = DocCLI.format_snippet(snippet)
    assert output == {'type': 'snippet', 'raw': 'None', 'options': {}, 'examples': []}

    # Test when snippet is none
    output = DocCLI.format_snippet(None)
    assert output == {'type': 'snippet', 'raw': 'None', 'options': {}, 'examples': []}

    # Test when snippet has some content (valid)
    snippet = '- name: Example snippet # do not remove\n  hosts: localhost\n  tasks:\n  - name: hello world\n    action: echo msg="Hello World"'
    output = DocCLI.format_snippet(snippet)

# Generated at 2022-06-12 20:31:00.715983
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible_collections.ansible.builtin.plugins.module_utils.ansible_module_common import AnsibleModule
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible_collections.my.my_collection.plugins.modules import my_module
    import collections
    import sys
    import ansible_collections
    import os

    sys.argv = ["ansible-doc", "--plugins"]
    command_args = DocCLI().parse()
    my_module.main()
    loader_collection = AnsibleCollectionLoader()
    collections_path = ansible_collections.__path__[0]
    loader_collection._load_collections(collections_path)
    col_list = loader_collection._list_collections()
    doc_col_list = DocCLI().display_