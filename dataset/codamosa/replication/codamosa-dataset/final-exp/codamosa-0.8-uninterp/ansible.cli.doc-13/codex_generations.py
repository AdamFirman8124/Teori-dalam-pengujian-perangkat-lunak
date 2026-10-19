

# Generated at 2022-06-12 20:24:11.429989
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    from ansible.plugins import module_loader
    from ansible.utils.display import Display

    display = Display()
    cli = DocCLI(
        {},
        {'type': 'module', 'verbosity': 0, 'tree': None, 'listt': False}
    )

    # Test that the method does not raise an exception
    cli.display_plugin_list(module_loader, display)

# Generated at 2022-06-12 20:24:14.694287
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    doc_cli = DocCLI()
    # This uses _get_metadata() to call get_plugin_metadata()
    assert doc_cli._get_metadata() is not None

# Generated at 2022-06-12 20:24:25.593188
# Unit test for function jdump
def test_jdump():
    # Test that a simple dictionary can be jdump'd
    assert json.loads(jdump({'a': 1})) == {'a': 1}, 'jdump is not able to convert a simple dictionary to a json.'
    # Test that the jdump function handles a common utility function
    assert json.loads(jdump(to_text({'a': 1}))) == {'a': 1}, 'jdump is not able to convert a simple dictionary to a json.'
"""
[
  {
    "name": "plugin_name",
    "doc": {
      "text": """

# Generated at 2022-06-12 20:24:32.481265
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    test1 = './lib/ansible/plugins/action/copy.py'
    test2 = './lib/ansible/plugins/action/user.py'
    test3 = './lib/ansible/plugins/action/set_fact.py'
    test4 = './lib/ansible/plugins/action/ping.py'
    test5 = './lib/ansible/plugins/action/win_ping.py'

    metatest1 = DocCLI.get_plugin_metadata(test1)
    metatest2 = DocCLI.get_plugin_metadata(test2)
    metatest3 = DocCLI.get_plugin_metadata(test3)
    metatest4 = DocCLI.get_plugin_metadata(test4)
    metatest5 = DocCLI.get_plugin_metadata

# Generated at 2022-06-12 20:24:40.620985
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    import doctest
    # The following test will fail, its purpose is to test the return value
    # of add_fields

# Generated at 2022-06-12 20:24:44.111455
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    connection = Connection('http://localhost:6789')

    for t in C.DOCUMENTABLE:
        d = DocCLI([t])
        d.run()

    for tc in C.DOCUMENTABLE_PLUGIN_CLASSES:
        d = DocCLI([tc])
        d.run()


# Generated at 2022-06-12 20:24:51.710481
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    from collections import namedtuple
    from ansible.cli.doc import DocCLI
    from ansible.utils.display import Display
    display = Display()
    display.columns = 80
    doccli = DocCLI([])
    role = 'myrole'

# Generated at 2022-06-12 20:25:01.989344
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    import textwrap

# Generated at 2022-06-12 20:25:11.496807
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    # setup
    patcher1 = patch('ansible.cli.doc.DocCLI._find_plugin_names', autospec=True)
    mock_find_plugin_names = patcher1.start()
    mock_find_plugin_names.return_value = ['mymodule_name', 'mymodule_name2', 'mymodule_name3']
    patcher2 = patch('ansible.cli.doc.DocCLI.load_plugin_doc', autospec=True)
    mock_load_plugin_doc = patcher2.start()
    mock_load_plugin_doc.return_value = 'mock_load_plugin_doc_return'
    doc = DocCLI()
    # run
    doc.display_plugin_list(None)
    # assert

# Generated at 2022-06-12 20:25:22.280806
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:26:33.686013
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    pass


# Generated at 2022-06-12 20:26:42.219216
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    
    print('Testing method add_fields of class DocCLI')
    cli = DocCLI()
    

# Generated at 2022-06-12 20:26:54.435796
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    from collections import namedtuple
    from refdoc import DocCLI
    import json
    # Mock object for testing 
    class FakeTTY(object):
        def __init__(self):
            self.columns = 80
    display.columns = FakeTTY()

    # Test case 1
    vars = {}
    vars['role'] = "user"
    with open('test/data/role_template_doc_for_user.json') as data_file:
        vars['role_json'] = json.load(data_file) 
    doc_cli_obj = DocCLI()
    resp_text = doc_cli_obj.get_role_man_text(**vars)

# Generated at 2022-06-12 20:26:58.179964
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    plugin_type = ''
    collection_name = ''
    docAdapter = DocCLI()
    actual = docAdapter.get_plugin_metadata(plugin_type, collection_name)
    expected = []
    assert expected == actual, "Expected {0} but got {1}".format(expected, actual)

# Generated at 2022-06-12 20:27:04.270247
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    # Create an instance of DocCLI
    cli = DocCLI()
    # This is just a placeholder for the assert.
    arg_value = 'shell'
    # Create a plugin_info (based on return from DocCLI.get_plugin_info)

# Generated at 2022-06-12 20:27:09.193916
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    import collections
    import textwrap
    from six import string_types

    doc = {
        'options': {
            'boolean': {
                'choices': [
                    'yes',
                    'no'
                ],
                'default': 'yes',
                'description': '\n      This is a boolean, it can only be yes or no.\n    ',
                'type': 'bool',
                'version_added': '1.0'
            },
            'string': {
                'choices': [
                    'up',
                    'down'
                ],
                'default': 'up',
                'description': '\n      This is a string, it can only be up or down.\n    ',
                'type': 'str'
            }
        }
    }

    text = []
    opt_indent

# Generated at 2022-06-12 20:27:19.691777
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    # Setting up mocks
    glob_mock = MagicMock(return_value=['/path/to/plugins/foo.py',
                                        '/path/to/plugins/bar.py'])
    open_mock = MagicMock(return_value=MagicMock(spec=file))
    read_mock = MagicMock(side_effect=[
        # Mock first plugin file
        read_mock_helper(PLUGIN_DOCSTRING_1, 'foo/bar', 'FooBar'),
        # Mock second plugin file
        read_mock_helper(PLUGIN_DOCSTRING_1, 'bar/foo', 'BarFoo'),
    ])


# Generated at 2022-06-12 20:27:25.311497
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    doc = {'description': "Brief description describing the module.", 'options': {'msg': {'description': "The message to be sent", 'required': True}}}
    output = DocCLI.get_man_text(doc)
    assert "> UNKNOWN    (unknown)\nBRIEF DESCRIPTION DESCRIBING THE MODULE.\nOPTIONS (= IS MANDATORY):\n        msg:\n            description: The message to be sent\n            required: True" in output
    assert len(output.split("\n")) == 8


# Generated at 2022-06-12 20:27:34.117979
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    plugin_list = []
    plugin = {}
    plugin['module'] = 'ping'
    plugin['name'] = 'ping'
    plugin['path'] = '/ansible/plugins/modules/ping.py'
    plugin['doc'] = '''#!/usr/bin/python\n# This is a docstring'''
    plugin_list.append(plugin)
    
    plugin_list2 = []
    plugin2 = {}
    plugin2['module'] = 'ping'
    plugin2['name'] = 'ping'
    plugin2['path'] = '/ansible/plugins/modules/ping.py'
    plugin2['doc'] = '''#!/usr/bin/python\n# This is a docstring'''
    plugin_list2.append(plugin2)
    
    ansible_doc_cli = DocCLI()


# Generated at 2022-06-12 20:27:38.833251
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    doc_cli = DocCLI()
    plugin_file_path = '/home/user1/ansible/lib/ansible/modules/cloud/amazon/ec2_vpc_route_table.py'
    assert doc_cli.namespace_from_plugin_filepath(plugin_file_path) == 'cloud.amazon'
    plugin_file_path = '/home/user1/ansible/lib/ansible/modules/cloud/amazon/ec2_vpc_route_table'
    assert doc_cli.namespace_from_plugin_filepath(plugin_file_path) == 'cloud.amazon'
    plugin_file_path = '/ansible/lib/ansible/modules/cloud/amazon/ec2_vpc_route_table'

# Generated at 2022-06-12 20:28:25.133763
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    DocCLI.format_plugin_doc(doc=None, collection_name=None, plugin_type=None)



# Generated at 2022-06-12 20:28:33.879971
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    display.columns = 100
    opt_indent = "        "
    pad = display.columns * 0.20
    limit = max(display.columns - int(pad), 70)
    
    class TestArgs(object):
        type = "role"
    context.CLIARGS = TestArgs()
    role = "install"

# Generated at 2022-06-12 20:28:39.640957
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    '''Test for method get_plugin_metadata'''
    def _mock_collect_fqcn(loader, name, path, *args, **kwargs):
        fqcns = ["module.fqcn"]
        return fqcns

    def _mock_collect_plugin_meta(loader, name, path, *args, **kwargs):
        module_metadata = {
            "doc": "module doc",
            "name": name
        }
        return module_metadata

    class MockedPathEntry(object):
        def __init__(self, *args, **kwargs):
            pass

    class MockedEntryPoint(object):
        def __init__(self, *args, **kwargs):
            self.resolve = lambda x: [MockedPathEntry()]


# Generated at 2022-06-12 20:28:43.402049
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():

    doc_cli = DocCLI()

    module = 'ping'
    collection_name = None
    plugin_type = 'module'
    rval = doc_cli.get_plugin_metadata(module, collection_name, plugin_type)

    assert isinstance(rval, dict)


# Generated at 2022-06-12 20:28:45.552277
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    assert DocCLI.namespace_from_plugin_filepath('/path/to/library/network_acl_facts.py') == "network.network_acl_facts"


# Generated at 2022-06-12 20:28:52.650239
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():

    text_list = []
    DocCLI.add_fields(text_list, {'test': 'a'}, 80, '    ', True)
    assert text_list == ['    TEST:', '        a']

    text_list = []
    DocCLI.add_fields(text_list, {'test': ['a', 'b']}, 80, '    ', True)
    assert text_list == ['    TEST:', '        a, b']

    text_list = []
    DocCLI.add_fields(text_list, {'test': {'a': 'b'}}, 80, '    ', True)
    assert text_list == ['    TEST:', '        a: b']

    text_list = []

# Generated at 2022-06-12 20:29:00.991238
# Unit test for method get_role_man_text of class DocCLI

# Generated at 2022-06-12 20:29:11.356424
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    from ansible.module_utils._text import to_bytes, to_text
    text = []
    options = {'become': {'type': 'bool', 'aliases': ['become_method', 'become_user', 'become_pass'], 'default': 'true'}}
    DocCLI.add_fields(text, options, limit=80, opt_indent="    ", return_values=False)

    expect = ("    BECOME (B):\n"
              "        become: true\n"
              "        type: bool\n"
              "        aliases: [become_method, become_user, become_pass]")
    assert '\n'.join(text) == expect

    text = []
    options = {"_ansible_diff": {'type': 'bool'}}

# Generated at 2022-06-12 20:29:19.457596
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():

    doc = {
        'description': 'This is a sample module',
        'filename': 'samplefile.py',
        'options': [
            {
                'required': True,
                'choices': ['present', 'absent'],
                'description': [
                    'If set to I(present), the specified objects should be present.',
                    'If set to I(absent), the specified objects should be absent.',
                ],
                'type': 'str',
                'name': 'state',
                'defaul': 'present'
            },
            {
                'description': 'The string to use in the new file.',
                'type': 'str',
                'name': 'dest'
            }
        ],
        'author': 'Ansible, Inc',
        'deprecated': 'This module is deprecated'
    }

# Generated at 2022-06-12 20:29:25.595614
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.utils.display import Display
    from ansible.module_utils.six import string_types

    # This tests assumes an output with a width of 80 characters
    display = Display()
    display.columns = 80

    # Ensure assertions are used
    # pylint: disable=W0702
    try:
        assert 0
    except AssertionError:
        pass
    else:
        raise Exception("Assertions must be enabled")
    # pylint: enable=W0702


# Generated at 2022-06-12 20:31:44.254321
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    """Unit test case for testing DocCLI.get_man_text() """

    #################################################################################################
    # Test case: Normal execution.
    #################################################################################################

    print ("Executing test case: Normal execution.")

    display.columns = 120
    display.verbosity = 0

# Generated at 2022-06-12 20:31:57.172047
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    import ansible.plugins.doc_fragments.doc_fragments

    # This is the fake plugin
    doc = {
        'description': ['Create an I(EC2) instance.'],
        'options': {
            'count': {
                'description': 'How many instances to launch.',
                'required': True
            },
            'name': {
                'description': 'Name of the instances to launch.',
                'required': True
            },
            'instance_type': {
                'description': 'Instance type to use for the instances.',
                'default': 'm3.medium'
            },
            'key_name': {
                'description': 'SSH keypair to install on the instance(s).'
            }
        },
        'requirements': [
            'boto'
        ]
    }

# Generated at 2022-06-12 20:31:58.972329
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    # Calling get_plugin_metadata from on class DocCLI
    # DocCLI.get_plugin_metadata()
    pass