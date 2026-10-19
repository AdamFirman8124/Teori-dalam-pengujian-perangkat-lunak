

# Generated at 2022-06-13 08:52:11.618838
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_include = RoleInclude()
    role_include.load_data("test1, test2")
    role_include.load_data("test1: test2")
    role_include.load_data({"test1": "test2"})

# Generated at 2022-06-13 08:52:18.068411
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class TestRoleInclude(RoleInclude):
        pass

    class TestPlay:
        variable_manager = None
        loader = None

        def __init__(self):
            self._basedir = None

    play1 = TestPlay()
    role1 = TestRoleInclude(play=play1)
    role1.load_data({'name': 'apache'})

    assert(role1._name == 'apache')

    play2 = TestPlay()
    role2 = TestRoleInclude(play=play2)
    try:
        role2.load_data(None)
        assert False
    except AnsibleParserError:
        pass

    try:
        role2.load_data(123)
        assert False
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 08:52:27.455151
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 08:52:37.666731
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook import Play
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    # create the play and load a test role
    my_play = Play.load({
        'name': 'w00t',
        'hosts': ['localhost'],
        'connection': 'local',
        'gather_facts': 'no',
        'roles': [{
            'name': 'foobar',
            'foo': 'bar',
            'when': 'False',
            'include_role': {
                'name': 'foobar',
                'allow_duplicates': True,
                'bar': 'foo'
            }
        }]
    }, variable_manager=VariableManager(), loader=None)
    # prepare context

# Generated at 2022-06-13 08:52:47.859567
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # Test if load accepts the valid input - string and dict
    role_name = 'ansible-role-some_role'
    dict_data = dict(name=role_name)
    string_data = role_name
    test_data = [dict_data, string_data]
    play = None
    current_role_path=None
    parent_role=None
    loader=None
    collection_list=None
    vars = dict(
        foo = "bar",
        test = dict(
            group_a = 'foo',
            group_b = 'bar'
        )
    )
    from ansible.vars.manager import VariableManager
    vm = VariableManager()
    vm.set_inventory(None)
    vm.set_vars(vars)
    vm.set_fact_cache({})
   

# Generated at 2022-06-13 08:53:00.219213
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager

    data_old_style = "apb.testrole"
    data_new_style = dict(role="apb.testrole")
    data_new_style_nested = dict(role=dict(role="apb.testrole"))
    data_new_style_nested_nested = dict(role=dict(role=dict(role="apb.testrole")))
    data_new_style_nested_dict = dict(role=dict(role="apb.testrole", delegate_to="localhost"))
    data_new_style_nested_dict_nested = dict(role=dict(role=dict(role="apb.testrole", delegate_to="localhost")))
    data_

# Generated at 2022-06-13 08:53:01.293545
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    raise AnsibleParserError("Passed")

# Generated at 2022-06-13 08:53:09.248906
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    role_path = os.path.expanduser("~/ansible/roles")
    role_name = "testRole"
    role_basedir = os.path.join(role_path, role_name)
    play_context = PlayContext()
    play = Play().load({}, variable_manager=None, loader=None)
    ri = RoleInclude(play=play, role_basedir=role_basedir, variable_manager=VariableManager(), loader=TaskQueueManager())

    assert ri.load("../testRole", VariableManager(), TaskQueueManager()) is not None

# Generated at 2022-06-13 08:53:12.157669
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    assert ri.load('role', 'play')
    assert ri.load({'name': 'role', 'role_path': 'play'})


# Generated at 2022-06-13 08:53:14.400427
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # 1. unit test load function with empty string
    # 2. unit test load function with old style
    # 3. unit test load function with correct attributes
    # 4. unit test load function with wrong attributes
    pass

# Generated at 2022-06-13 08:53:22.420580
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: need to refactor to remove use of AnsibleBaseYAMLObject for testing
    #       This is a private class and very tightly bound to Ansible's YAML parser
    # TODO: write unit tests on this method
    pass


# Generated at 2022-06-13 08:53:33.680156
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Sanity check on load method
    """
    # Create a mock object for test.
    import _mock_t_ansible_parsing_yaml_objects
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.module_utils.six.moves import reload_module

    reload_module(_mock_t_ansible_parsing_yaml_objects)
    from _mock_t_ansible_parsing_yaml_objects import AnsibleVaultEncryptedUnicode

    obj = AnsibleBaseYAMLObject()
    obj.__setattr__('object', AnsibleVaultEncryptedUnicode('password'))
    obj.__setattr__('_line_number', '1')

# Generated at 2022-06-13 08:53:44.548001
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.playbook
    import ansible.parsing.yaml.data
    import ansible.parsing.yaml.objects

    p = ansible.playbook.Play()
    yaml_data = ansible.parsing.yaml.data.AnsibleUnicode("""
      roles:
        - role: apache
      """)
    role_basedir = "/etc/ansible/roles"
    d = ansible.parsing.yaml.objects.AnsibleBaseYAMLObject(yaml_data)
    ri = ansible.playbook.role.include.RoleInclude(play=p, role_basedir=role_basedir)

    e = ri.load(d, p)

# Generated at 2022-06-13 08:53:51.550869
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils import context_objects as co

    play_context = PlayContext()
    play_context.become = True

    loader = 'fake loader'
    collection_list = 'fake collection_list'


# Generated at 2022-06-13 08:53:52.261866
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:54:00.971793
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
    Test Case:
    >>> import os
    >>> from ansible.module_utils.six import iteritems, string_types
    >>> from ansible.playbook.role_include import RoleInclude
    >>> # Test for:
    >>> #   RoleInclude.load(data, play, current_role_path=None, parent_role=None,
    >>> #                    variable_manager=None, loader=None, collection_list=None)
    >>> data = '''

# Generated at 2022-06-13 08:54:09.096070
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Passing data of type AnsibleBaseYAMLObject
    data = AnsibleBaseYAMLObject()
    # Variable manager is not used in this case
    variable_manager = None
    # loader is not used in this case
    loader = None
    # collection_list is not used in this case
    collection_list = None
    # Passing play which is not required to create RoleInclude object
    play = None
    # Passing current_role_path which is not required when play is None
    current_role_path = None
    ri = RoleInclude(play=play, role_basedir=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    # Passing data of type AnsibleBaseYAMLObject to load_data method

# Generated at 2022-06-13 08:54:20.133499
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 08:54:25.877790
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement, RoleRequirementSpec
    from ansible.parsing.vault import VaultLib
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # Create a play

# Generated at 2022-06-13 08:54:32.617053
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import sys
    import tempfile
    from ansible.module_utils.six import PY3
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.errors import AnsibleError, AnsibleParserError
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.attribute import Attribute, FieldAttribute

    # Import needed for patching
    from ansible.playbook.base import Base
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager