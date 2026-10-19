

# Generated at 2022-06-12 20:23:39.167406
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    ModulesDocCLI().run()

if __name__ == "__main__":
    import sys
    import doctest
    for mod in sys.modules.keys():
        if mod.startswith('ansible.module_utils') or mod.startswith('ansible.modules'):
            try:
                doctest.testmod(sys.modules[mod])
            except TypeError:
                # Some modules have issues with doctest on 2.6
                continue

# Generated at 2022-06-12 20:23:42.546729
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    doc=DocCLI()
    doc.main()
    pass


# Generated at 2022-06-12 20:23:51.821933
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    plugin = {
        'name': 'setup',
        'short_description': 'Gathers facts about remote hosts',
        'description': 'This is the message describing the setup module.',
        'version_added': 'historical',
        'options': {
            'gather_timeout': {
                'type': 'int',
                'description': 'Some description'
            }
        }
    }
    plugin_doc = DocCLI._format_plugin_doc(plugin)
    assert plugin_doc.startswith('setup (core)')
    assert plugin_doc.endswith('* gather_timeout: Some description')
    assert plugin_doc.count('\n') == 3


# Generated at 2022-06-12 20:24:02.783008
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    from ansible.plugins.loader import get_all_plugin_loaders
    if os.environ.get('ANSIBLE_NOCOLOR', None) is None:
        os.environ['ANSIBLE_NOCOLOR'] = u'1'
    cli = DocCLI(['-l', 'all'])
    cli.parse()
    assert DocCLI.get_all_plugins_of_type(cli, 'connection') == [u'chroot', u'lxc_container', u'lxd_container', u'paramiko_ssh', u'ssh', u'winrm', u'local']

# Generated at 2022-06-12 20:24:06.286727
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    plugins = [
        ("action", "Example Action Plugin", "./action_plugins/example.py", "./action_plugins/example.py")
    ]
    context.CLIARGS = {'type': 'action'}
    context.CLIARGS['subcommand'] = 'debug'
    DocCLI.display_plugin_list(plugins)



# Generated at 2022-06-12 20:24:17.176875
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    import inisetup
    inisetup._setup()

# Generated at 2022-06-12 20:24:28.040508
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:24:37.672597
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:24:45.029307
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:24:46.332524
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    doc = {}
    assert DocCLI.get_man_text(doc)


# Generated at 2022-06-12 20:25:42.566626
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    pass

# Generated at 2022-06-12 20:25:47.819759
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    # Meta data loading
    meta_data_files = ['meta_data/meta_data.yml']
    # Loading the meta data file
    meta_data = DocCLI.get_plugin_metadata(meta_data_files)
    # Check if meta_data is empty or not
    assert meta_data != {}
    # Check the meta_data file is loaded properly with all plugins

# Generated at 2022-06-12 20:25:56.133610
# Unit test for method get_man_text of class DocCLI

# Generated at 2022-06-12 20:26:03.105646
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    text = []
    text.append('> NAME    (filename)')
    text.append('short description')
    text.append('  * note: This module has a corresponding action plugin.')
    text.append('OPTIONS (= is mandatory):')
    text.append('  name')
    text.append('          Choices: one, two, three')
    text.append('          [Default: one]')
    text.append('  option')
    text.append('          Description')
    text.append('          [Default: abc]')
    text.append('ATTRIBUTES:')
    text.append('{')
    text.append('    attribute: "string"')
    text.append('}')
    text.append('AUTHOR: author')
    text.append('EXAMPLES:')

# Generated at 2022-06-12 20:26:04.728170
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    # FIXME: add tests for this method
    pass

# Generated at 2022-06-12 20:26:12.894342
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    def try_get_man_text_result(doc):
        return DocCLI().get_man_text(doc)

# Generated at 2022-06-12 20:26:22.850310
# Unit test for method add_fields of class DocCLI

# Generated at 2022-06-12 20:26:29.274343
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = {'name': 'test', 'short_description': 'this is a test', 'description': 'This is a test module for unit tests', 'version_added': '2.4'}
    expected_result = '''
This is a test module for unit tests (version_added 2.4)

Summary
=======
this is a test

'''
    result = DocCLI.format_plugin_doc(doc)
    assert result == expected_result

# Generated at 2022-06-12 20:26:31.746649
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    doc_cli = DocCLI()
    assert isinstance(doc_cli.find_plugins(), list)


# Generated at 2022-06-12 20:26:41.078016
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    cli = DocCLI()

    assert isinstance(cli.get_all_plugins_of_type('lookup'), list)
    assert isinstance(cli.get_all_plugins_of_type('module'), list)
    assert isinstance(cli.get_all_plugins_of_type('callback'), list)
    assert isinstance(cli.get_all_plugins_of_type('filter'), list)
    assert isinstance(cli.get_all_plugins_of_type('test'), list)
    assert isinstance(cli.get_all_plugins_of_type('connection'), list)
    assert isinstance(cli.get_all_plugins_of_type('shell'), list)
    assert isinstance(cli.get_all_plugins_of_type('strategy'), list)

# Generated at 2022-06-12 20:27:45.952669
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    plugin_list = ['uri']
    type_ = 'modules'
    filtered_plugin_list = DocCLI.get_all_plugins_of_type(plugin_list, type_)
    assert filtered_plugin_list != []
    assert filtered_plugin_list == ['uri']

# Generated at 2022-06-12 20:27:58.881745
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():
    """Unit test for method format_snippet of class DocCLI"""
    # Test case 1
    print("Test Case 1")
    print("Solution:")
    print("    Module documentation for command module")
    print("    ----------------------------------------\n")
    print("    :author: Tim Bielawa <tbielawa@redhat.com>")
    print("    :copyright: 2016, Tim Bielawa <tbielawa@redhat.com>")
    print("    :license: GPLv3+")
    print("")
    print("    EXAMPLES:")
    print("")
    print("    # Print the current date and time.")
    print("    - command: date")
    print("      register: result")
    print("")
    print("    # Run the command if the specified file does not exist.")


# Generated at 2022-06-12 20:28:07.753350
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():

    import json


# Generated at 2022-06-12 20:28:16.578440
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    from ansible import constants as C
    from ansible.module_utils.common.collections import ImmutableDict

    display = DocCLI.Display()
    display.columns = 80
    DocCLI.IGNORE = DocCLI.IGNORE + ('type',)


# Generated at 2022-06-12 20:28:26.070036
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    doc = [{
        'filename': '/path/to/file.py',
        'description': 'some description',
        'options': {
            'some_option': {'description': 'some description', 'required': True},
        }
    }]
    format_plugin_doc(doc, 'module')
    assert doc[0] == {
        'filename': '/path/to/file.py',
        'description': 'some description',
        'options': {
            'some_option': {'description': 'some description', 'required': True},
        },
        'module': 'file',
        'version_added': None,
        'version_added_collection': None,
    }


# Generated at 2022-06-12 20:28:31.631057
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():

    ###################################################################################################################
    # Test case no:01
    # Testing with valid input
    ###################################################################################################################

    doc_cli = DocCLI()
    _filter = ''
    plugin_type = 'module'
    # Case 1:
    # When subdir_filter is provided

    # Expected output:
    # all the available modules in the subdir

    # Actual output:
    # all the available modules in the subdir

    output1 = doc_cli.get_all_plugins_of_type(plugin_type, subdir_filter='block')
    assert len(output1) > 1
    for plugin in output1:
        assert plugin.split('/')[-3] == 'block'

    # Case 2:
    # When subdir_filter is not provide

    # Expected output:
    # all

# Generated at 2022-06-12 20:28:34.818459
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    dc = DocCLI()
    plugin_name = "ubuntu"
    plugin_type = "distros"
    plugin_metadata = dc.get_plugin_metadata(plugin_name, plugin_type)
    # The assertion below is a simple placeholder
    assert plugin_metadata[0]["name"] == "ubuntu"


# Generated at 2022-06-12 20:28:40.337375
# Unit test for method display_plugin_list of class DocCLI
def test_DocCLI_display_plugin_list():
    import sys
    import tempfile
    from os import path
    from unittest import TestCase
    from unittest.mock import patch

    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import cache_loader
    from ansible.plugins.loader import callback_loader
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import filter_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import module_utils_loader
    from ansible.plugins.loader import test_loader

    class DocCLITestCase(TestCase):
        def setUp(self):
            self.mock_stderr = tempfile.TemporaryFile()
            self.mock_std

# Generated at 2022-06-12 20:28:48.734952
# Unit test for method get_role_man_text of class DocCLI
def test_DocCLI_get_role_man_text():
    import json
    import os

    test_directory = os.path.join('unit', 'clilib', 'test_docs')
    test_glob = 'test_docs_*.json'
    test_files = [(os.path.join(basedir, f), os.path.join(test_directory, f),) for (basedir, dirs, files) in os.walk(test_directory) for f in fnmatch.filter(files, test_glob)]

    test_count = 0

    for (test_file, test_results_file) in test_files:
        test_count += 1

        temp_cli_args = dict()

        module_name = os.path.splitext(os.path.basename(test_file))[0].split('_')[2]

# Generated at 2022-06-12 20:28:50.210945
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    DocCLI.get_all_plugins_of_type()