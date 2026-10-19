

# Generated at 2022-06-12 20:26:13.285711
# Unit test for function jdump
def test_jdump():
    jdump([1,2,3])
    jdump({})
    jdump({
        'version_added': '1.0',
        'supports_check_mode': False,
        'foo': ['bar', 1, {'test': 'tree'}],
    })



# Generated at 2022-06-12 20:26:15.824538
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    """
    :avocado: tags=precise
    :avocado: tags=doc
    """
    DocCLI(args=None).run()

# Generated at 2022-06-12 20:26:24.762498
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # Test 1: Test module
    doc = create_semantically_valid_module_doc()
    assert DocCLI.get_man_text(doc, collection_name='test.collection')
    # Test 2: Test playbook
    doc = create_semantically_valid_playbook_doc()
    assert DocCLI.get_man_text(doc, collection_name='test.collection')
    # Test 3: Test cli
    doc = create_semantically_valid_cli_doc()
    assert DocCLI.get_man_text(doc)
    # Test 4: Test role
    doc = create_semantically_valid_role_doc()
    assert DocCLI.get_role_man_text('test_role', doc)
    # Test 5: Test module (ToT)
    doc = create_semantically_valid_module

# Generated at 2022-06-12 20:26:25.862101
# Unit test for method print_paths of class DocCLI
def test_DocCLI_print_paths():
    DocCLI.print_paths()



# Generated at 2022-06-12 20:26:29.235716
# Unit test for method get_man_text of class DocCLI
def test_DocCLI_get_man_text():
    module_name = 'dummy'
    collection_name = 'ansible.builtin'
    doc = {}
    dummy = DocCLI.get_man_text(doc, collection_name, module_name)



# Generated at 2022-06-12 20:26:39.620280
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
  import json

# Generated at 2022-06-12 20:26:45.097092
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    p = DocCLI(None)
    # Set the class variables to valid values
    # Valid values for module_blob, module_blob_ext are all module names listed in the valid list of modules
    # Valid values for lookup_blob, lookup_blob_ext are all lookup modules listed in the valid list of modules
    # Valid values for callback_blob, callback_blob_ext are all callback modules listed in the valid list of modules
    # Valid values for nxos_module_blob, nxos_module_blob_ext are all nxos modules listed in the valid list of modules
    # Valid values for ios_module_blob, ios_module_blob_ext are all ios modules listed in the valid list of modules
    # Valid values for iosxr_module_blob, iosxr_module_

# Generated at 2022-06-12 20:26:55.743600
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    # Create instance to test
    doc_cli = DocCLI()
    # Create a dict of arguments to match call signature of method run
    # instance.run(plugin_type=None, parsed_args=None, search_path=None, index_filter=None, output_file=None)
    kwargs = {}
    kwargs['plugin_type'] = None
    kwargs['parsed_args'] = None
    kwargs['search_path'] = None
    kwargs['index_filter'] = None
    kwargs['output_file'] = None
    # Attempt to run method and verify it runs without raising an exception
    try:
        doc_cli.run(**kwargs)
    except Exception as e:
        assert False

# Generated at 2022-06-12 20:26:57.465637
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    assert DocCLI.namespace_from_plugin_filepath("/path/to/plugins/action/foo.py") == "action"



# Generated at 2022-06-12 20:26:59.311751
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():
    cli = DocCLI()
    cli.get_plugin_metadata()
# test_DocCLI_get_plugin_metadata ends here

################################################################################
# YAML Output
################################################################################

# Generated at 2022-06-12 20:27:54.348066
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    cls = DocCLI()
    plugins = cls.get_all_plugins_of_type()
    assert len(plugins) > 0
    assert isinstance(plugins, dict)

# Generated at 2022-06-12 20:28:04.003542
# Unit test for method get_plugin_metadata of class DocCLI
def test_DocCLI_get_plugin_metadata():

    test_plugin_type = 'module'

    # Test case 1: test valid behavior of method get_plugin_metadata

# Generated at 2022-06-12 20:28:11.084285
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    # DocCLI.add_fields()
    text = []

# Generated at 2022-06-12 20:28:15.652237
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():

    from ansible.cli.doc import DocCLI

    cli = DocCLI()

    for plugin_type in context.CLIARGS['type']:
        assert cli.get_all_plugins_of_type(plugin_type)



# Generated at 2022-06-12 20:28:22.868984
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    doc={"a":{"a":"b", "b":"c", "c1":"d1", "c2":"d2"}}
    text = []
    DocCLI.add_fields(text, doc, 80, "        ")
    assert "a:" in text
    assert "b" in text
    assert not "c1" in text
    assert not "d1" in text
    assert not "c2" in text
    assert not "d2" in text

# Generated at 2022-06-12 20:28:24.648574
# Unit test for method print_paths of class DocCLI
def test_DocCLI_print_paths():
  DocCLI_object = DocCLI()

# Generated at 2022-06-12 20:28:33.455502
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    doccli = DocCLI()
    text = []
    limit = 90

# Generated at 2022-06-12 20:28:37.807900
# Unit test for method format_snippet of class DocCLI
def test_DocCLI_format_snippet():

    doccli = DocCLI()

    # Case 1:
    # This should return:
    # '       - name: ...'
    snippet = '- name: ...'
    result = doccli.format_snippet(snippet, '        ')
    assert result == '       - name: ...'

    # Case 2:
    # This should return:
    # '- name: ...'
    snippet = '-name: ...'
    result = doccli.format_snippet(snippet, '        ')
    assert result == '-name: ...'



# Generated at 2022-06-12 20:28:43.251118
# Unit test for method namespace_from_plugin_filepath of class DocCLI
def test_DocCLI_namespace_from_plugin_filepath():
    l = DocCLI.namespace_from_plugin_filepath(['/some/path/plugins', 'module_utils'])
    assert l == ['module_utils', '_text'], 'DocCLI.namespace_from_plugin_filepath() returned '+str(l)+' instead of ["module_utils", "_text"]!'


# Generated at 2022-06-12 20:28:50.844196
# Unit test for method add_fields of class DocCLI
def test_DocCLI_add_fields():
    text = []
    ref_text = ["> COMMAND    (command.py)\n",
                "OPTIONS (= is mandatory):\n",
                "        --param3\n",
                "                option description\n",
                "        --param2\n",
                "                option description\n",
                "        --param1\n",
                "                option description\n",
                "\n"]

# Generated at 2022-06-12 20:31:18.409495
# Unit test for method get_all_plugins_of_type of class DocCLI
def test_DocCLI_get_all_plugins_of_type():
    import os
    from ansible.module_utils.six import StringIO
    from ansible.utils.display import Display
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.utils.path import module_finder, plugins_paths

    display_stringio = StringIO()
    display_out = Display(verbosity=4, log_file=display_stringio)


# Generated at 2022-06-12 20:31:25.250520
# Unit test for method format_plugin_doc of class DocCLI
def test_DocCLI_format_plugin_doc():
    cli = DocCLI()
    # see if we can get it to not throw an exception on its own
    cli.find_plugin_docs('')
    cli.find_plugin_docs('copy')
    # see if we can add/remove some bogus directories and get it to not throw an exception
    cli.directories.insert(0, 'does_not_exist')
    cli.directories.insert(0, 'does_not_exist_either')
    cli.directories.pop()
    cli.directories.pop()

# Generated at 2022-06-12 20:31:27.059248
# Unit test for method run of class DocCLI
def test_DocCLI_run():
    doc_cli = DocCLI()

    assert doc_cli.run() is None, 'Basic DocCLI failed to run'


# Generated at 2022-06-12 20:31:34.262796
# Unit test for method format_plugin_doc of class DocCLI

# Generated at 2022-06-12 20:31:43.573650
# Unit test for method get_man_text of class DocCLI

# Generated at 2022-06-12 20:31:56.218683
# Unit test for method find_plugins of class DocCLI
def test_DocCLI_find_plugins():
    # Test setting up a plugin.
    plugin1 = {
        'test1': 'test plugin'
    }
    plugin2 = {
        'test2': 'test plugin'
    }
    plugin_dir = 'test_dir'
    libdir = getattr(builtins, '__xonsh_env__', {}).get('ANSIBLE_LIBRARY')
    # Test finding plugins without any input.
    _ = DocCLI.find_plugins()
    # Test finding plugins with a plugin dir.
    _ = DocCLI.find_plugins(plugin_dir=plugin_dir)
    # Test finding plugins with a plugin list.
    _ = DocCLI.find_plugins(plugins=[plugin1])
    # Test finding plugins with a plugin dir and plugin list.