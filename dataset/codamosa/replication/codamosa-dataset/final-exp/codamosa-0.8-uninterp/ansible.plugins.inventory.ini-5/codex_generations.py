

# Generated at 2022-06-13 12:55:11.514566
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # For test we have to mock method parse_yaml_from_file() of class BaseFileInventoryPlugin
    BaseFileInventoryPlugin.parse_yaml_from_file = mock.Mock()

    #m = InventoryModule(loader=None, group="all", sources="hosts")
    m = InventoryModule() # FIXME: we are getting default group "all"
    data = """
    a:
      hosts:
        beta:
          ansible_host: 127.0.0.1
        bs:
          ansible_host: 127.0.0.1
    """
    BaseFileInventoryPlugin.parse_yaml_from_file.return_value = yaml.safe_load(data)
    m.parse("")

# Generated at 2022-06-13 12:55:20.666230
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    import os
    import sys
    dl = DataLoader() # used to load the inventory file
    inv = Inventory(loader=dl, variable_manager=VariableManager(), host_list='./test/test_inventory_module/test_file') # this is the inventory object where we will populate
    inv_mod = InventoryModule(dl, inv) # the inventory module we are testing
    path = './test/test_inventory_module/test_file'
    inv_mod.parse(path)

# Generated at 2022-06-13 12:55:28.580780
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test correct path extension if provided path is relative
    a = 'foo/bar/'
    b = os.path.join(os.getcwd(), a)

    m = InventoryModule()
    m.parse(a, None)
    assert m._filename == b
    # Test empty path doesn't raise exception
    m.parse('', None)
    assert m._filename == ''


# Generated at 2022-06-13 12:55:31.396515
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule('/path/to/inventory', loader())
    inv_mod.parse()
    assert False  # TODO: implement your test here


# Generated at 2022-06-13 12:55:46.030383
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Disable pylint complaining about access to protected members of class InventoryModule
    # pylint: disable=protected-access

    # Test 1
    module = InventoryModule()
    test_content = '''
    [webservers]
    foo.example.com

    [dbservers]
    one.example.com
    two.example.com
    three.example.com
    '''
    module._parse('test_inventory', to_bytes(test_content).splitlines(True))

    # Test 1 - verify the result
    assert module.inventory.groups == ['webservers', 'dbservers']
    assert module.inventory.list_hosts('webservers') == ['foo.example.com']

# Generated at 2022-06-13 12:55:56.178911
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:56:04.683409
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    lines = [
        '''
        # A comment
        [group1] ''',
        '''
        host1''',
        '''
        # Another comment
        [group2:vars] ''',
        '''
        foo=bar''',
        '''
        # Yet another comment
        [group3:children] ''',
        '''
        group4'''
    ]
    inventory = InventoryModule()
    inventory.parse('/dev/null', lines)

# Generated at 2022-06-13 12:56:16.887669
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(None, loader=None)

    module = InventoryModule(inventory=inventory)

    module.parse('fixtures/hosts_simple', is_file=True)

    # Test use of evil host/group names

    module.parse('fixtures/hosts_evil', is_file=True)
    assert 'ungrouped' in inventory.groups
    assert 'evil:group' in inventory.groups
    assert inventory.hosts['host:name'] in inventory.groups['ungrouped'].get_hosts()
    assert inventory.hosts['host-name'] in inventory.groups['evil:group'].get_hosts()

    # Test host/group variables

    module.parse('fixtures/hosts_vars', is_file=True)

# Generated at 2022-06-13 12:56:26.787301
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Unit-test the parse method of class InventoryModule.
    fake_inventory = MagicMock()
    fake_InventoryModule = MagicMock(spec=InventoryModule)
    # We define a fake inventory object to use in our test.
    fake_inventory = MagicMock(spec=Inventory)
    # We define a fake InventoryModule object to use in our test.
    fake_InventoryModule = MagicMock(spec=InventoryModule)

    # We define a fake inventory object to use in our test.
    fake_inventory = MagicMock(spec=Inventory)
    
    # We define a fake InventoryModule object to use in our test.
    fake_InventoryModule = MagicMock(spec=InventoryModule)
    fake_InventoryModule._COMMENT_MARKERS ='#'
    fake_InventoryModule._pattern_

# Generated at 2022-06-13 12:56:29.309714
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule('/path/to/inventory_file.yaml')
    assert inv.parse() == None
    

# Generated at 2022-06-13 12:56:40.587956
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    assert True

# Generated at 2022-06-13 12:56:47.310759
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = inventory.Inventory()
    inv.add_host("testhost")

    fd, path = tempfile.mkstemp()
    try:
        os.write(fd, b'[test]\ntesthost\n')
        os.close(fd)

        im = InventoryModule(inv)
        im.parse(path)

        assert "test" in inv.groups
        assert "testhost" in inv.groups["test"].hosts
    finally:
        os.remove(path)

# Generated at 2022-06-13 12:57:03.123990
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.manager import InventoryManager
    inv_data = '''
    #test file
    [all:vars]
    ansible_ssh_user=vagrant
    ansible_ssh_private_key_file=/Users/travishill/.vagrant.d/insecure_private_key

    [nodes]
    node1 ansible_ssh_host=127.0.0.1

    [mon]
    mon1

    [osds]
    osd1
    osd2
    osd3
    osd4

    [rgws]
    rgw1
    rgw2
    '''

    inv_parser = InventoryModule()
    from distutils.version import LooseVersion

# Generated at 2022-06-13 12:57:12.267667
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule()

    # Invalid input
    # Test 1
    try:
        inv_mod._parse(None,None)
        raise Exception('Test 1 failed...')
    except AnsibleParserError:
        pass

    # Test 2
    try:
        inv_mod._parse('',['','','[','','[','','','','','','','','','','','','','','','','','','','','','','','',''])
        raise Exception('Test 2 failed...')
    except AnsibleError:
        pass

    # Test 3

# Generated at 2022-06-13 12:57:19.196410
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = AnsibleModule(
        argument_spec = dict(
            host_list=dict(required=True),
            group_list=dict(required=True),
        ),
        supports_check_mode = True
    )
    _inventory_module = InventoryModule()

    result = _inventory_module.parse(module.params['host_list'], module.params['group_list'], None)
    module.exit_json(**result)


# Generated at 2022-06-13 12:57:25.800745
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # load a trivial inventory
    module = InventoryModule()
    filename = 'trivial.ini'
    path = os.path.join(DATA_PATH, filename)
    module.parse(path, filename)
    # check for one group
    assert(len(module.inventory.groups) == 1)
    # check for the group name
    g = module.inventory.groups[0]
    assert(g.name == 'ungrouped')
    # check for no children
    assert(g.child_groups == [])
    # check for one host with no vars
    assert(list(g.hosts) == ['localhost'])
    assert(list(g.get_host('localhost').vars.keys()) == [])
    # check for nothing more
    assert(len(module.inventory.groups) == 1)

# Generated at 2022-06-13 12:57:34.155337
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    group_name = 'group1'
    port = '22'
    variables = dict(ansible_ssh_user='root', ansible_ssh_pass='pass')
    hosts_data = []
    hosts_data.append ('host1')
    hosts_data.append ('host2')
    hosts_data.append ('host3')
    hosts_data.append ('host4')
    hosts_data.append ('host5')
    try:
        inventory.parse(hosts_data)
    except AnsibleParserError as e:
        print(e)

# Generated at 2022-06-13 12:57:38.872400
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  host_list = []
  new_inventory = InventoryManager(loader=DataLoader()) 
  new_inventory_parser = InventoryModule(loader=None, groups=None, filename=None)
  new_inventory_parser.inventory = new_inventory
  new_inventory_parser._parse(None, host_list)


# Generated at 2022-06-13 12:57:48.853078
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    args = dict(
        host_list=["localhost", "example.com"],
        group_name="test_group"
    )
    args['host_list'].sort()
    module.get_host_list(args)
    module.inventory.get_groups_dict()
    module.get_host_info()

    # Testing InventoryModule._parse
    class TestInventoryModule_parse(object):
        def _parse(self):
            raise AnsibleError("An error message")
    module = TestInventoryModule_parse()
    with pytest.raises(AnsibleParserError) as err:
        module._parse("",[])
    assert "An error message" in str(err.value)

# Generated at 2022-06-13 12:57:58.550009
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # '''
    #   Unit test for method parse of class InventoryModule.
    #   We call function _parse with different input.
    # '''

    inventory = InventoryManager(loader=None, sources=None)
    module = InventoryModule(loader=None, sources=None, inventory=inventory)

    # To test this we need to create files to pass to te module, for each
    # test case we have.
    #
    # Every file created here will be deleted later on.
    #
    # As a temporary dir, we will use /tmp/ansible_test_module_InventoryModule
    tmp_dir = "/tmp/ansible_test_module_InventoryModule"
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.makedirs(tmp_dir)

# Generated at 2022-06-13 12:58:22.021107
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()

# Generated at 2022-06-13 12:58:30.497909
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
    from ansible.inventory.manager import InventoryManager
    m = InventoryManager()
    i = InventoryModule(m)
    input = [
        '# this is a comment',
        '[somename]',
        'alpha',
        'beta',
        '[somename:vars]',
        'spam = eggs',
        'foo = bar',
        '[somename:children]',
        'foo',
        'bar']
    i._parse('/parsertest/example.ini', input)
    print(repr(i.inventory))


# Unit tests for method _parse_value of class InventoryModule

# Generated at 2022-06-13 12:58:37.644183
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class MockInventoryModule(InventoryModule):
        def __init__(self):
            super(InventoryModule, self).__init__()
            self.inventory = Inventory()

    inv_module = MockInventoryModule()
    inv_module._parse('/tmp/inventory', ['[groupname]', '[other:vars]', 'hostname:port'])
    assert inv_module.patterns['section']
    assert inv_module.patterns['groupname']


# Generated at 2022-06-13 12:58:38.845066
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 12:58:50.668597
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inp_contents = """
[ungrouped]
172.31.1.1 user=ansible
172.31.1.2

[group1]
172.31.1.3
172.31.1.4

[group2:vars]
ansible_user=root

[group2:children]
group1
    """

    inventory = InventoryManager(loader=DictDataLoader({}))
    inventory_parser = InventoryModule(loader=DictDataLoader({}), inventory=inventory)
    inventory_parser.parse_inventory(inventory_path=None, inventory_items_posix_path=None, inventory_items_script=None,
                                     inventory_items_script_args=None, inventory_items_script_common_args=None,
                                     inventory_items_script_single_args=None)

# Generated at 2022-06-13 12:58:58.998328
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from os.path import dirname, join, abspath
    path = join(dirname(dirname(dirname(abspath(__file__)))), 'tests', 'inventory.yaml')
    i = Inventory(DataLoader())
    im = InventoryModule()
    im.parse(i, path)
    assert str(i.get_host('foo')) == "<Host foo: ansible_ssh_host=127.0.0.1 ansible_ssh_port=22 ansible_ssh_user=root>"

# Generated at 2022-06-13 12:59:07.147997
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = Inventory(host_list=[])

    # Test1: valid input
    test1_mock_file_path='/tmp/sample_file'
    test1_mock_file_content=['[group1]', 'localhost']
    test1_inventory_module=InventoryModule(filename='sample_file',
                                           inventory=inventory)

    with open(test1_mock_file_path, 'w') as sample_file:
        sample_file.write('\n'.join(test1_mock_file_content))

    test1_inventory_module.parse(test1_mock_file_path)
    group=inventory.get_group('group1')
    assert group.name == 'group1'
    assert len(group.get_hosts()) == 1
    assert group.get_hosts

# Generated at 2022-06-13 12:59:18.179186
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = 'inventory_file'
    path_to_file = '/path/to/file'
    in_data = "Test test"
    in_path = '/path/to/file'
    # Test with no 'lines' argument
    inst = InventoryModule(in_data, in_path, module)
    assert isinstance(inst, InventoryModule)
    inst.parse()
    # Test with 'lines' argument
    inst = InventoryModule(in_data, in_path, module, lines=in_data)
    assert isinstance(inst, InventoryModule)
    inst.parse(lines=in_data)
    # Test with no 'path' argument
    inst = InventoryModule(in_data, in_path, module)
    assert isinstance(inst, InventoryModule)
    inst.parse(path=path_to_file)
#

# Generated at 2022-06-13 12:59:30.144350
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:59:41.106870
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule(loader=DictDataLoader({}))

    # Test with comments
    inv.parse({}, '# Basic group with a variable\n\n[group1]\nfoo=bar\n\n# A group with hosts, children, and a variable\n[group2]\nhost1\nhost2  # comment\n\n[group2:children]\nchild1\nchild2\nchild3\n\n[group2:vars]\nansible_connection=local')
    assert len(inv.groups) == 3, 'should have 3 groups'
    assert inv.groups['group1'].vars == {'foo': 'bar'}, 'should have 1 variable in group1'
    assert len(inv.groups['group2'].hosts) == 2, 'should have 2 hosts in group2'

# Generated at 2022-06-13 13:00:02.435978
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 13:00:09.026209
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:00:19.616858
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:00:24.164310
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_source = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inventory_source.ini')
    with open(inventory_source) as f:
        text = f.read()

    InventoryModule._parse(inventory_source, text)


# Generated at 2022-06-13 13:00:33.840981
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()

# Generated at 2022-06-13 13:00:40.996804
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for method parse of class InventoryModule
    '''
    import StringIO

    def obj_to_safe_group_name(obj):
        if isinstance(obj, str): return obj
        elif isinstance(obj, unicode): return obj.encode('utf8')
        elif isinstance(obj, list): return [obj_to_safe_group_name(e) for e in obj]
        elif isinstance(obj, dict):
            o = {}
            for k, v in obj.iteritems():
                o[obj_to_safe_group_name(k)] = obj_to_safe_group_name(v)
            return o
        raise Exception("Undetermined type: " + str(obj) + " " + str(type(obj)))


# Generated at 2022-06-13 13:00:45.385791
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    path = './hosts'
    module.parse(path, 'hosts')
    assert type(module.inventory) == Inventory
    assert len(module.inventory.groups) == 0
    assert len(module.inventory.hosts) == 0


# Tests for method parse_group of class InventoryModule

# Generated at 2022-06-13 13:00:47.288849
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    inventory_module._parse('test', ['[test]', 'test'])
# Test for method _parse_host_definition

# Generated at 2022-06-13 13:00:58.585261
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    im = InventoryModule()
    im.parse(b'---\none: 1')
    im.parse(b'---\none: 2')
    assert im.get_hosts('all') == ['one']
    assert im.get_hosts('all') == ['one']
    assert im.get_hosts('all') == ['one']
    assert im.get_host('one').get_vars() == {'one': 1}
    im.parse(b'---\none: 2')
    assert im.get_host('one').get_vars() == {'one': 2}
    im.parse(b'[all]\none: 3')
    assert im.get_host('one').get_vars() == {'one': 3}
    assert im.get_host(b'one').get_vars()

# Generated at 2022-06-13 13:01:03.271976
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    parser = InventoryModule()
    with pytest.raises(AnsibleParserError):
        parser.parse('', {}, {}, {})


# Generated at 2022-06-13 13:01:52.707329
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    current_dir = os.path.dirname(__file__)
    inventory_path = os.path.join(current_dir, '../../lib/ansible/inventory')
    sys.path.append(inventory_path)
    try:
        import InventoryModule
    except ImportError:
        raise AssertionError("Unable to import InventoryModule")
    test_case_list = [{'in': (b'''
        [test]
        host ansible_connection=ssh ansible_ssh_user=root ansible_ssh_pass=foobar
    '''), 'out': {'test': {'hosts': {'host': {'ansible_connection': 'ssh', 'ansible_ssh_user': 'root', 'ansible_ssh_pass': 'foobar'}}}}}]

# Generated at 2022-06-13 13:02:04.195586
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # init
    inventory_module_parse = InventoryModule()

    # test with a non-existent file
    with pytest.raises(AnsibleParserError):
        inventory_module_parse._parse('/non-existent.yml', ['hello', 'world'])

    # test with a non-supported content type
    with pytest.raises(AnsibleParserError):
        inventory_module_parse._parse('/none-existent.yml', ['hello', 'world'])

    # test with an empty file
    with pytest.raises(AnsibleParserError):
        inventory_module_parse._parse('/empty.yml', [])

    # test with a valid file (gathered from different sources)

# Generated at 2022-06-13 13:02:08.618632
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
# INITIALIZATION
    inventory = InventoryManager(c.get_config_data())
    filename = 'test/test_all/test_inventory/test_hosts'


# Generated at 2022-06-13 13:02:19.801253
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    #
    # The following parameters will be passed to the constructor:
    #
    # path:
    # filename:
    # loader:
    # host_list:
    # cache:
    #
    # The following instance variables need to be initialized:
    #
    # inventory:
    # parser:
    #
    inventory_module = InventoryModule(
        path=None,
        filename=None,
        loader=None,
        host_list=[],
        cache=False)
    inventory_module.inventory = InventoryManager(
        loader=None,
        sources=C.INVENTORY_ENABLED,
    )

# Generated at 2022-06-13 13:02:31.409676
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule()

# Generated at 2022-06-13 13:02:41.941912
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Helper funtion that verifies that the inventory module correctly reads the given input and generates the given
    # output.
    def verify(args, expected):
        InventoryModule.inventory_parser(args)
        assertInventory(args, expected)

    # Test the parsing of a single group with one host, no variables or children.
    verify(dict(path=dict(key='test'),
                data='''
                    [groupname]
                    alpha
                '''),
           dict(groups=['groupname'],
                hosts=dict(alpha=[]),
                vars=dict(groupname={})))

    # Test the parsing of multiple groups, hosts, and variables, with a variety of groups appearing in different
    # orders.

# Generated at 2022-06-13 13:02:43.830718
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print(InventoryModule.parse)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 13:02:55.311230
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    arguments = dict(
        inv='inventory_hosts',
    )

    module = AnsibleModule(
        argument_spec=dict(
            inv=dict(required=True, type='str'),
        ),
        supports_check_mode=False,
    )

    inv = InventoryModule(module)
    inv.parse(arguments['inv'])
    hosts = inv.list_hosts()
    assert hosts == ['agroup', 'bgroup', 'agroup', 'bgroup', 'agroup', 'bgroup', 'agroup', 'bgroup']
    groups = inv.list_groups()
    assert groups == ['agroup', 'bgroup', 'all', 'ungrouped']
    keys = inv.get_host(hosts[0]).get_vars().keys()
    assert 'ansible_host' in keys

# Generated at 2022-06-13 13:03:02.752799
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    inventory_path = 'inventory_hosts'
    print(os.path.realpath(os.getcwd()))
    print(os.path.realpath(os.path.join(skeletondir,inventory_path)))

    # Create inventory_hosts
    with open(inventory_path,'w+') as hostfile:
        hostfile.writelines([
            "[all]\n",
            "127.0.0.1\n",
            "localhost\n",
            "\n",
            "[all:vars]\n",
            'ansible_connection=local\n'
        ])

    hostfile.close()

    print(InventoryModule.__load__)
    inventory_mod = InventoryModule(inventory_path)
    print(inventory_mod)

    ## No need to create inventory file each time


# Generated at 2022-06-13 13:03:09.318724
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    group_name = 'test_parse_group'
    child_name = 'test_parse_child:children'
    vars_name = 'test_parse_vars:vars'
    var = 'test_var'
    var_value = 'test_var_value'
    path = 'test_path'
    data = '[%s]\n[%s]\n[%s]\n%s=%s' % (group_name, child_name, vars_name, var, var_value)

    m = InventoryModule()
    m.inventory = Inventory()
    m.parse(path, data.splitlines(True))

    group_exists = group_name in m.inventory.groups
    assert group_exists, 'Group %s exists in inventory' % group_name
    assert m.inventory.groups

# Generated at 2022-06-13 13:04:51.167950
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    inv.parse('')

if __name__ == '__main__':
    test_InventoryModule_parse()

from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.inventory.manager import InventoryManager
from ansible.inventory.vars import VariableManager
from ansible.module_utils._text import to_text, to_bytes
from ansible.parsing.vault import VaultLib
from ansible.parsing.vault import VaultSecret
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.six import string_types, iteritems, with_metaclass
import os
import re
import shlex
import ast
import json
