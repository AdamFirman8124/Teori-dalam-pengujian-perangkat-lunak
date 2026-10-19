

# Generated at 2022-06-13 08:52:18.337878
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test when data is invalid
    data = []
    with pytest.raises(AnsibleParserError):
        ri = RoleInclude()
        ri.load_data(data)

    # test when data is string
    data = 'invalid'
    with pytest.raises(AnsibleError):
        ri = RoleInclude()
        ri.load_data(data)

    # test when data is dict
    data = {}
    ri = RoleInclude()
    ri_new = ri.load_data(data)
    assert ri_new.role_path == None
    assert ri_new.role_name == None
    assert ri_new.role_collections == []
    assert ri_new.role_params == {}

    # test when data is AnsibleBaseY

# Generated at 2022-06-13 08:52:22.415439
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert ri.load(data, play, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)

    # Unit test for class RoleInclude

# Generated at 2022-06-13 08:52:34.781599
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    import os

    ri = RoleInclude.load('tomcat', play='', current_role_path=os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'libcloud'),
                          parent_role=None, variable_manager=None, loader=DataLoader(), collection_list=None)
    play_context = PlayContext()
    loader = DataLoader()
    ri.validate()
    ri.compile(play_context=play_context, loader=loader)

    # FIXME:  this is only checking that the method completes, not that it's actually doing the right thing
    #         so this isn't a great test. 

# Generated at 2022-06-13 08:52:46.363316
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test RoleInclude object with a string value
    data_1 = 'test_role'
    try:
        assert RoleInclude.load(data=data_1) == RoleInclude(test_role=None)
    except Exception as e:
        print('Exception {} in test_RoleInclude_load with data {}'.format(e, data_1))

    # Test RoleInclude object with a AnsibleBaseYAMLObject
    data_2 = RoleInclude(test_role=None)
    try:
        assert RoleInclude.load(data=data_2) == RoleInclude(test_role=None)
    except Exception as e:
        print('Exception {} in test_RoleInclude_load with data {}'.format(e, data_2))

    # Test RoleInclude object with a dictionary

# Generated at 2022-06-13 08:52:52.271573
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_definition = {
        'name': 'test',
        'defaults': {
            'test': 'test',
        }
    }

    # first test with a string, i.e. the 'old style' requirement
    ri = RoleInclude.load('test', None)
    assert ri.get_name() == 'test'
    assert ri.defaults == {}

    # now test with a dict
    ri = RoleInclude.load(role_definition, None)
    assert ri.get_name() == 'test'
    assert ri.defaults == {'test': 'test'}

# Generated at 2022-06-13 08:53:02.960285
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vars import load_extra_vars
    from io import StringIO
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import sys

    # prep

# Generated at 2022-06-13 08:53:12.672258
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
    Test method RoleInclude.load()
    '''
    import os
    import shutil
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleParserError
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import discovery
    import ansible.constants as C
    import six
    import pytest


# Generated at 2022-06-13 08:53:21.478381
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test valid load with a dict
    assert RoleInclude.load({"name": "test"}, play=None) is not None

    # Test valid load with a string
    assert RoleInclude.load("test", play=None) is not None

    # Test valid load with an AnsibleBaseYAMLObject
    assert RoleInclude.load(AnsibleBaseYAMLObject(data={"name": "test"}), play=None) is not None

    # Test invalid load with an integer
    try:
        RoleInclude.load(10, play=None)
    except AnsibleParserError as e:
        assert "Invalid role definition" in to_native(e)

    # Test invalid load with an old style role requirement string

# Generated at 2022-06-13 08:53:34.485872
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class RoleIncludeTestWrapper:

        def __init__(self, play = None, role_basedir = None, variable_manager = None, loader = None, collection_list = None):
            pass

        def load_data(self, data, variable_manager=None, loader=None):
            pass

    assert RoleInclude.load(None, None, None, None, None, None) == None

    class MockAnsibleError:
        def __init__(self, error_message):
            self.error_message = error_message

        def __repr__(self):
            return repr(self.error_message)

        def __str__(self):
            return self.error_message

    class MockAnsibleParserError:
        def __init__(self, error_message, obj=None):
            self.error_

# Generated at 2022-06-13 08:53:45.715941
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing import vault
