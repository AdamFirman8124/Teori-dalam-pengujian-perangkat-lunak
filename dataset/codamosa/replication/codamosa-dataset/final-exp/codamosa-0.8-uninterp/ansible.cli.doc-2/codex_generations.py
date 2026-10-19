

# Generated at 2022-06-12 20:25:37.465209
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    DocCLI.find_plugins()
    pass

# Generated at 2022-06-12 20:25:45.326325
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    cli = DocCLI()
    cli.display_plugin_list('Module', [
        mock.Mock(name='module1', collection='my_collection',
                  plugin_type='action', description='does stuff'),
        mock.Mock(name='module2',
                  plugin_type='action', description='does stuff'),
        mock.Mock(name='module3', collection='my_collection',
                  plugin_type='not_action', description='does stuff'),
    ])
    expected_calls = [
        ('my_collection.module1 (action)',),
        ('   does stuff',),
        ('module2 (action)',),
        ('   does stuff',),
        ('my_collection.module3',),
        ('   does stuff',)
    ]
    cli._display.display.assert_has_calls

# Generated at 2022-06-12 20:25:54.972593
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    
    doc = {'description': 'here is a description', 'options': {'name': {'description': 'The name of this thing', 'spec': [{'choices': ['a', 'b', 'c'], 'name': 'value'}]}}, 'plainexamples': 'text example', 'requirements': ['package a', 'package b', 'package c'], 'return': {'description': 'desc', 'type': 'bool'}, 'see_also': [{'description': 'this is a link', 'link': 'http://a.com', 'name': 'A'}, {'description': 'this is another link', 'link': 'http://b.com', 'name': 'B'}], 'version_added': '1.2.3', 'version_added_collection': '4.5.6'}
    text = []
   

# Generated at 2022-06-12 20:26:07.518717
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    s = DocCLI()

    doc = {}
    result = DocCLI.get_man_text(doc)
    assert '>\n' == result, result

    assert_equal(DocCLI.get_man_text(dict(description='short'), 'collection'), '> COLLECTION.\n\nshort\n')

    # test optional params
    assert_equal(DocCLI.get_man_text(doc, plugin_type='copy'), '> COPY    \n\n')

    # test ignore param
    doc = dict(description='short', target=True)
    DocCLI.IGNORE = DocCLI.IGNORE + ('target',)
    result = DocCLI.get_man_text(doc)
    assert '>\n\nshort\n' == result, result

    # test short_description

# Generated at 2022-06-12 20:26:19.327334
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    # save a copy for resetting below
    old_plugin_dirs = context.CLIARGS['plugins']

    # Test with collection of one plugin
    context.CLIARGS['plugins'] = ['/tmp/test_collection/']
    assert DocCLI._find_plugins() == set(['/tmp/test_collection/ansible_test_collection/plugins/modules/test_collection.py'])

    # Test with collection with one plugin and normal plugins dir
    with patch.dict(
        'os.path.exists',
        {'/etc/ansible/plugins/modules/': True, '/tmp/test_collection/': True},
        clear=True):
        assert DocCLI._find_plugins() == set(['/tmp/test_collection/ansible_test_collection/plugins/modules/test_collection.py'])

# Generated at 2022-06-12 20:26:26.898492
# Unit test for method get_man_text of class DocCLI

# Generated at 2022-06-12 20:26:28.320227
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    doc = DocCLI()
    doc.find_plugins()



# Generated at 2022-06-12 20:26:32.387254
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Load the module
    doc_obj = DocCLI(module)

    result = doc_obj.run()
    assert result['changed'] is False
    assert result['module_name'] == 'doc'
    assert result['module_path'] == os.path.abspath(__file__)
    assert result.get('msg', None) is not None

# Generated at 2022-06-12 20:26:41.577361
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    # No file in the file system
    with pytest.raises(AnsibleError) as e:
        DocCLI.format_plugin_doc(['/non/existing/file.py'])
    assert str(e.value) in (
        "File /non/existing/file.py not found.",
        "File /non/existing/file.py not found. No such file or directory."
    )

    # A cache file without mandatory keys
    cache_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'lib/ansible/modules/core/network/nxos/nxos_bgp.py'
    )

# Generated at 2022-06-12 20:26:50.343267
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    # Patch AnsibleModule
    set_module_args({
        'paths': ['Test/data/modules'],
        'type': 'module',
    })
    module = AnsibleModule(
        argument_spec=dict(
            paths=dict(required=True, type='list'),
            type=dict(required=True, type='str', choices=['module']),
        )
    )

    # Create class object
    doc_obj = DocCLI()

    # run function test
    with pytest.raises(SystemExit):
        doc_obj.run()

# Generated at 2022-06-12 20:27:56.445716
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    list_plugins = [{"path": "plugins/lookup/apt.py", "plugin_type": "lookup"}, {"path": "plugins/module_utils/netaddr.py", "plugin_type": "module_utils"}, {"path": "plugins/modules/apt.py", "plugin_type": "modules"}, {"path": "plugins/modules/apt_key.py", "plugin_type": "modules"}, {"path": "plugins/modules/apt_repository.py", "plugin_type": "modules"}, {"path": "plugins/modules/apt_rpm.py", "plugin_type": "modules"}, {"path": "plugins/modules/apt_state.py", "plugin_type": "modules"}]

# Generated at 2022-06-12 20:28:04.380783
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    """Unit test for method get_plugin_metadata in class DocCLI"""
    doc = {
        'action': {
            'description': 'Ansible action plugin',
            'filename': 'action.py'
        },
        'connection': {
            'description': 'Ansible connection plugin',
            'filename': 'connection.py'
        }
    }
    plugin_type = 'action'
    actual_result = DocCLI.get_plugin_metadata(doc, plugin_type)
    expected_result = {
        'description': 'Ansible action plugin',
        'filename': 'action.py'
    }
    assert expected_result == actual_result



# Generated at 2022-06-12 20:28:11.313039
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    doc = """
    NAME:

        one
    SHORT DESCRIPTION:

        A short description
    DESCRIPTION:

        Long description
    VERSION_ADDED:

        1.1
    MODULE:

        mod
    """
    with patch('__builtin__.open', create=True) as mock_open:
        mock_open.return_value = MagicMock(spec=file)
        handle = mock_open.return_value.__enter__.return_value
        handle.read.return_value = doc

        # Patch the prettytable
        with patch.multiple(DocCLI, display_plugin=DEFAULT, display_plugin_list=DEFAULT):
            DocCLI.display_plugin_list('', '', '', '')
            assert DocCLI.display_plugin_list.call_count == 1

            # Check

# Generated at 2022-06-12 20:28:19.563848
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    """Test if we correctly get all plugins of given type"""
    # GIVEN: mocking a plugin type
    plugin_type = 'module'
    # WHEN: invoking method get_all_plugins_of_type of class DocCLI
    output = DocCLI.get_all_plugins_of_type(plugin_type)
    # THEN: we get all plugins
    assert len(output) > 0, "It is expected that we get all plugins."



# Generated at 2022-06-12 20:28:22.309486
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    plugin = {"version_added": "2.4"}
    rc = DocCLI(args=["", "-t", "test"])
    rc.create_docs(plugin, "test")



# Generated at 2022-06-12 20:28:31.722420
# Unit test for method get_man_text of class DocCLI

# Generated at 2022-06-12 20:28:32.466987
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    assert 1 == 1


# Generated at 2022-06-12 20:28:34.525360
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    plugins = DocCLI.get_all_plugins_of_type('module')
    plugin_list = []
    for plugin in plugins:
        plugin_list.append(plugin)
    assert 'zfs' in plugin_list


# Generated at 2022-06-12 20:28:37.962228
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = {'hello':'world'}
    assert DocCLI.format_plugin_doc(doc) == '{\n    hello: world\n}'
    doc = 'hello world'
    assert DocCLI.format_plugin_doc(doc) == 'hello world'
    doc = ['hello', 'world']
    assert DocCLI.format_plugin_doc(doc) == '- hello\n- world'


# Generated at 2022-06-12 20:28:38.678166
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():

    # Unimplemented
    pass

# Generated at 2022-06-12 20:29:44.845312
# Unit test for function add_collection_plugins
def test_add_collection_plugins():
    plugin_list = {}
    add_collection_plugins(plugin_list, 'action')
    plugin_list = plugin_list.keys()
    # Expected list of ansible.builtin plugins
    ansible_builtin_plugins = ['ansible.builtin.debug', 'ansible.builtin.meta']
    # Expected list of ansible.netcommon plugins
    ansible_netcommon_plugins = ['ansible.netcommon.network_cli']
    # Expected list of ansible.posix plugins
    ansible_posix_plugins = ['ansible.posix.argspec']
    # Expected list of community.general plugins
    community_general_plugins = ['community.general.backup_file']
    # Expected list of ansible.windows plugins

# Generated at 2022-06-12 20:29:54.340553
# Unit test for method run of class DocCLI

# Generated at 2022-06-12 20:30:01.852961
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    mock_plugins = [
        'action',
        'become',
        'cache',
        'callback',
        'cliconf',
        'connection',
        'httpapi',
        'inventory',
        'lookup',
        'netconf',
        'strategy'
    ]

    doc_cli = DocCLI()
    plugins = doc_cli.get_all_plugins_of_type('action')

    for plugin in plugins:
        assert plugin in mock_plugins

    plugins = doc_cli.get_all_plugins_of_type('actions')

    for plugin in plugins:
        assert plugin in mock_plugins


# Generated at 2022-06-12 20:30:04.708225
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    ''' test_DocCLI_get_plugin_metadata '''
    cli = DocCLI()
    cmd = {}
    plugins = []
    plugins.append({'plugin_type': '', 'filename': '', 'name': '', 'doc': {}})
    result = cli.get_plugin_metadata(cmd, plugins)

# Generated at 2022-06-12 20:30:06.832236
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    '''Unit test for add_fields method of DocCLI class'''
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)



# Generated at 2022-06-12 20:30:15.540390
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:30:26.552409
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    filename = './test_plugins/action/test_action_plugin.py'
    category = 'action'
    plugin_type='action'
    try:
        metadata = DocCLI.get_plugin_metadata(filename, category, plugin_type)
    except:
        pytest.fail("test_DocCLI_get_plugin_metadata failed to get metadata for plugin %s"%filename)
    assert metadata['filename'] == filename
    assert metadata['name'] == 'test_action_plugin'
    assert metadata['author'] == 'me'
    assert metadata['version'] == 0.1
    assert metadata['description'] == 'this is my description'

    assert metadata['module'] == 'test_action_plugin'
    assert metadata['short_description'] == 'test short_description'

# Generated at 2022-06-12 20:30:37.080367
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    '''
    Unit test for method find_plugins of class DocCLI
    '''
    # Create an instance of class DocCLI
    doc = DocCLI()

    # simple test
    plugins = doc._find_plugins(None, ['/usr/local/lib/python2.7/dist-packages/ansible/modules'], 'action')

# Generated at 2022-06-12 20:30:46.113490
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    text = DocCLI.add_fields(
        text = text,
        field = [
            {
                "name": "src",
                "description": "Files to copy to the remote server",
                "required": True,
                "default": None,
                "choices": None
            },
            {
                "name": "dest",
                "description": "location to copy the files to",
                "required": True,
                "default": None,
                "choices": None
            }
        ],
        limit = 80,
        indent = "        ",
        return_values = False,
        parent_indent = "    "
    )

# Generated at 2022-06-12 20:30:51.581919
# Unit test for method format_snippet of class DocCLI

# Generated at 2022-06-12 20:32:01.373018
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    context._init_global_context(CLIArgs())
    docs = DocCLI.load_docs(force=True, refresh_cache=True, verbosity=0)
    all_module_names = docs[0].keys()
    if not all_module_names:
        # No plugins loaded, restore defaults, try again
        context.CLIARGS = CLIArgs()
        docs = DocCLI.load_docs(force=True, refresh_cache=False, verbosity=0)
        all_module_names = docs[0].keys()

    modules_of_type = docs[1]
    if not modules_of_type:
        # No plugins of type, restore defaults, try again
        context.CLIARGS = CLIArgs()