

# Generated at 2022-06-12 20:24:10.243039
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Generate manpage sample1 and save it to a file
        with open('sample1_manpage', 'w') as f:
            f.write('\n'.join(DocCLI.run('ping', 'module')))
        # Check if the first line of the manpage (plugin name) is the same
        # in both the sample file and the plugin
        with open('sample1_manpage', 'r') as f:
            assert f.readline() == "> PING    (sample1/ping.py)\n"

        # Generate manpage sample2 and save it to a file
        with open('sample2_manpage', 'w') as f:
            f.write('\n'.join(DocCLI.run('command', 'shell')))

# Generated at 2022-06-12 20:24:13.022223
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    CLIDoc = DocCLI()
    assert CLIDoc.display_plugin_list(None, 'file') == None


# Generated at 2022-06-12 20:24:17.347143
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    test_plist = {}
    test_coll_filter = [ 'acd', 'acm' , 'col' ]
    test_plugin_type = 'action'
    add_collection_plugins(test_plist, test_plugin_type, test_coll_filter)
    assert type(test_plist) == dict


# Generated at 2022-06-12 20:24:28.171162
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:24:32.191982
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    # Setup data for test
    try:
        DocCLI.run()
    except SystemExit as ex:
        # verify that the SystemExit exception is raised with the correct exit code
        assert ex.code == 0


# Generated at 2022-06-12 20:24:37.968632
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    # Generate the arguments for this method
    arg_data = {}
    arg_data['doc'] = {'description': 'The description of the doc', 'options': {}, 'name': 'ansible-doc'}

    # Create object of class DocCLI with required args and kwargs
    obj = DocCLI()

    # Call the method with args and kwargs
    method = DocCLI._get_method_with_args(obj, 'format_plugin_doc')
    method(**arg_data)



# Generated at 2022-06-12 20:24:41.039134
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    documentation = DocCLI()
    assert documentation.format_plugin_doc('my_test_module') == 'Please click on link to see the documentation for this module'
    assert documentation.format_plugin_doc('file') == 'Please click on link to see the documentation for this module'


# Generated at 2022-06-12 20:24:48.292504
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible_collections.testns.testcoll import plugins

    # test empty list
    assert DocCLI.display_plugin_list([]) == 'None\n'

    # test one entry
    assert DocCLI.display_plugin_list([('lookup', 'whooah')]) == 'lookup\t\twhooah\n'

    # test multiple entries
    assert DocCLI.display_plugin_list([('lookup', 'whooah'), ('shell', 'whooah')]) == 'lookup\t\twhooah\nshell\t\twhooah\n'

    # test no collection and collection

# Generated at 2022-06-12 20:24:55.415940
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    # It returns an exited status, if any of its subtest fails
    failed = 0
    # Test if method returns an empty dictionary, if there are no plugins of given type
    if DocCLI.get_all_plugins_of_type('random_type') != {}:
        failed = 1
        print("DocCLI.get_all_plugins_of_type(random_type) failed")
    # Test if method returns a non empty dictionary, if there are plugins of given type
    if len(DocCLI.get_all_plugins_of_type('module')) == 0:
        failed = 1
        print("DocCLI.get_all_plugins_of_type(module) failed")
    # Test if method returns a non empty dictionary, if there are plugins of given type

# Generated at 2022-06-12 20:24:57.018189
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    doc = DocCLI()
    doc.parse()
    doc.run()

# Generated at 2022-06-12 20:26:34.102220
# Unit test for method add_fields of class DocCLI

# Generated at 2022-06-12 20:26:39.771610
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    import mock
    with mock.patch("__builtin__.display") as mock_display:
        DocCLI._display_plugin_list()

# Generated at 2022-06-12 20:26:43.733481
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = {
        "description": "This is the description",
        "options": {
            "key": {
                "description": "A description of what the key is.",
            }
        }
    }
    plugin_type = "foo"
    tty_size = {'height': 40, 'width': 80}
    res = DocCLI.get_man_text(doc, "", plugin_type)
    assert res == DocCLI.format_plugin_doc(doc, plugin_type, tty_size)


# Generated at 2022-06-12 20:26:55.369890
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    @contextmanager
    def chdir(path):
        oldpwd = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(oldpwd)

    # use this role to test
    tmpdir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmpdir, 'library'))
    os.mkdir(os.path.join(tmpdir, 'module_utils'))
    ansible_test_data = os.path.join(os.path.dirname(__file__), 'unit/ansible_test_data')
    shutil.copy(os.path.join(ansible_test_data, 'testfile'), os.path.join(tmpdir, 'library', 'testfile'))

# Generated at 2022-06-12 20:26:58.654680
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = AnsibleModuleDocGen._parse_docstring(read_docstring('cliconf_plugin'))
    txt = DocCLI.get_man_text(doc)
    assert isinstance(txt, string_types)
    assert 'GETTERS={' in txt
    assert 'GETTERS: ' not in txt


# Generated at 2022-06-12 20:26:59.668758
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    test = DocCLI()
    test.find_plugins()


# Generated at 2022-06-12 20:27:05.660329
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    doc = {
        'notes': ['note_1','note_2','note_3'],
        'description': 'description_1',
        'deprecated': 'deprecated_1',
        'short_description': 'short_description_1',
        'seealso': {
        'module': 'module_1'
      },
        'options': {
        'key_1': {
            'default': 'default_1',
            'description': 'description_1'
        }
    },
    'examples': [

    ]
    }
    assert "see also: module_1" in DocCLI.get_man_text(doc)
    assert "add in: description_1" in DocCLI.get_man_text(doc)
    assert "note: note_1, note_2, note_3"

# Generated at 2022-06-12 20:27:07.230023
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    DocCLI.display_plugin_list('filter')


# Generated at 2022-06-12 20:27:17.917589
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    items = {
        "foo": {
            "description": "this is a useful option",
            "required": True,
            "aliases": ["f", "of"],
            "choices": ["one", "two", "three"],
            "default": "one",
        },
        "bar": {
            "description": "this is another useful option",
            "required": False,
            "aliases": ["b", "ab"],
            "choices": ["one", "two", "three"],
        },
    }
    text = []
    DocCLI.add_fields(text, items, 80, "        ")

# Generated at 2022-06-12 20:27:25.137957
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    print('IN: test_DocCLI_get_role_man_text')
    doccli = DocCLI()
    role_json = {
        'path': '/root/ansible/lib/ansible/roles/test1',
        'entry_points': {
            'main': {
                'short_description': 'main',
                'options': {
                    'test1': 'test1',
                    'test2': 'test2'
                }
            }
        },
        'name': 'test1'
    }
    role_text = doccli.get_role_man_text('test1', role_json)
    #print(role_text)


# Generated at 2022-06-12 20:28:24.829154
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    '''test_DocCLI_add_fields
    This unit test covers the functionality of the method add_fields
    of class DocCLI.
    '''
    # Test 1: return_values is False.
    # Write to file.
    text = []
    # Dictionary 1.
    opt_1 = {
        'description': 'The name of the managed host.',
        'aliases': [ 'hostname', 'name' ],
        'required': True,
        'version_added': "2.3"
    }
    # Dictionary 2.
    opt_2 = {
        'description': 'The managed host group.',
        'required': False,
        'type': 'str'
    }
    # Dictionary 3.

# Generated at 2022-06-12 20:28:33.623898
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    doccli = DocCLI()
    code = """
- hosts: myhost
  gather_facts: yes
  tasks:
  - name: Test
    my_command:
    args:
        - 1
        - 2
        - 4

- hosts: myhost
  gather_facts: no
  tasks:
  - name: Test
    my_command:
    args:
        - 1
        - 2
        - 4
"""
    result = doccli.format_snippet(code)

# Generated at 2022-06-12 20:28:39.262007
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    documentation = textwrap.dedent("""
    description:
        - B(Update the current working directory (cwd) to the specified path)
    options:
        chdir:
            description:
                - The path to change into before running the command.
            required: true
            type: path
            aliases: [ cd ]
    """)
    snippet = textwrap.dedent("""
    - name: cd into /usr/src/packages and look for any files
      find:
        paths: /usr/src/packages
        patterns: '*'
        file_type: file
      register: files
    - debug:
        msg: "A file from {{ item.path }}"
      loop: "{{ files.files }}"
      loop_control:
        label: "{{ item.path }}"
    """)

# Generated at 2022-06-12 20:28:47.716342
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():

    from ansible.utils.display import Display
    from ansible.utils.color import colorize
    from ansible.module_utils.six import string_types

    for mode in ('minimal', 'init'):
        display = Display()
        display.verbosity = mode
        display.columns = 120


# Generated at 2022-06-12 20:28:48.554967
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    pass

# Generated at 2022-06-12 20:28:57.029281
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    '''Testing DocCLI.add_fields()'''
    text = []
    doc_data = {'options': {
            'myopt': {'choices': ['one', 'two'], 'default': 'three', 'default_aliases': ['four'], 'description': 'foo bar this is my option'}}}
    limit = 100
    DocCLI._dump_yaml = lambda x, y: yaml_dump(x, indent=0, default_flow_style=False)
    DocCLI.add_fields(text, doc_data, limit, opt_indent='    ')
    result = '\n'.join(text)
    #print result
    assert re.search(r'MYOPT: foo bar this is my option', result)
    assert re.search(r'choices: one, two', result)

# Generated at 2022-06-12 20:29:07.141628
# Unit test for method get_all_plugins_of_type of class DocCLI

# Generated at 2022-06-12 20:29:08.937925
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    mydoc = DocCLI()
    mydoc._display = display
    assert mydoc.run.__name__ == 'run'

# Generated at 2022-06-12 20:29:11.354454
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    doccli = DocCLI()
    doccli.display_plugin_list(["1", "2", "3"], "test")


# Generated at 2022-06-12 20:29:19.517370
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    import tempfile, os
    # Create a temporary file and write a yaml spec to it
    module_spec_path = tempfile.mktemp()
    with open(module_spec_path, 'w') as f:
        f.write(
            '''name: mymodule
description: My module's description goes here.
version_added: "2.4"
options:
    myoption:
        description:
            - A description of myoption.
        required: true
        type: str
'''
        )

    doc = DocCLI.get_man_text(module_spec_path, collection_name='mycollection')

    # Ensure the module name and version were properly inserted

# Generated at 2022-06-12 20:30:30.797372
# Unit test for method display_plugin_list of class DocCLI

# Generated at 2022-06-12 20:30:41.649473
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    from ansible.plugins import action
    from ansible.modules.system import apt
    from ansible.utils.display import Display
    from ansible.cli import CLI
    display = Display()
    cli = CLI(args=[], display=display)
    cli.add_options()
    options, _ = cli.parser.parse_args()
    options.tree = None

    # import one file
    doc = DocCLI(args=['ansible-doc', apt.__file__], options=options)
    assert doc.namespace_from_plugin_filepath(apt.__file__) == "system"

    # import dir
    doc = DocCLI(args=['ansible-doc', action.__path__[0]], options=options)

# Generated at 2022-06-12 20:30:42.722464
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    assert True == False

# Generated at 2022-06-12 20:30:44.198887
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():

    # return output of display_plugin_list
    return DocCLI.display_plugin_list()

# Generated at 2022-06-12 20:30:50.073383
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    # Setup
    import json
    import tempfile
    DebugCLI.options['module'] = False
    DebugCLI.options['role'] = False
    DebugCLI.options['collection'] = False
    DebugCLI.options['filter'] = 'setup'
    DebugCLI.options['unsafe'] = True
    DebugCLI.options['no_log'] = True
    DebugCLI._write_stdout = lambda x: None
    DebugCLI._write_stderr = lambda x: None
    DebugCLI.options['document'] = False
    DocCLI.options['module'] = False
    DocCLI.options['role'] = False
    DocCLI.options['collection'] = False
    DocCLI.options['filter'] = 'setup'
    DocCLI.options['unsafe'] = True
    DocCL

# Generated at 2022-06-12 20:30:54.393349
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
  module_dir = './library/'

  assert DocCLI.namespace_from_plugin_filepath(
    path=module_dir) == 'ansible.builtin'


# unit test for method namespace_from_plugin_name of class DocCLI

# Generated at 2022-06-12 20:31:03.271151
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
        cli = DocCLI()

# Generated at 2022-06-12 20:31:04.914595
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    instance = DocCLI()
    instance.add_fields(text, doc.pop('options'), limit, opt_indent)

# Generated at 2022-06-12 20:31:06.973097
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    doc = DocCLI() 
    actual = doc.display_plugin_list()
    expected = 0 
    assert actual == expected


# Generated at 2022-06-12 20:31:11.784548
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    argspec = Mock()
    argspec.args = []
    argspec.kwargs = {'no_files_ignore': True,}
    cli_plugin_paths = ( 'test1', 'test2')
    cli_src = 'test3'
    cli_type = 'test4'
    user_collection_paths = ['test5']
    plugin_type = 'test6'