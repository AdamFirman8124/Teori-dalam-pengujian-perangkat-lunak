

# Generated at 2022-06-13 13:52:38.438203
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # test with empty list to return empty list
    assert lookup.run([], {}) == []

    # test with terms which do not exist in the inventory
    assert lookup.run(["localhost"], {"hostvars": {},
                                      "groups": {}}) == []

    # test with terms which do exist in the inventory
    assert lookup.run(["all"], {"hostvars": {},
                                "groups": {"all": ["localhost"]}}) == ["localhost"]

    # test with group pattern which does not exist in the inventory
    assert lookup.run(["group1"], {"hostvars": {},
                                   "groups": {}}) == []

    hostvars = {"test_host1": {"test_var1": "test_value1"}}

# Generated at 2022-06-13 13:52:45.286633
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()
    test.set_loader({'group_names': ['group1']})
    hosts = {
        'group1': [
            'host1',
            'host2',
        ]
    }
    variables = {'groups': hosts}
    # Test with string as input
    assert test.run('', variables) == hosts['group1']
    # Test with list as input
    assert test.run([], variables) == hosts['group1']
    # Test with empty list as input
    assert test.run(['host3'], variables) == []

# Generated at 2022-06-13 13:52:56.918307
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock: loader
    class Mock_loader:
        def get_basedir(self):
            return "basedir"

    # Mock: inventory
    class Mock_inventory:
        def __init__(self):
            self.groups = dict()
            self.hosts = dict()
            self.hosts_patterns = None

    manager = Mock_inventory()
    host1 = Mock_inventory()
    host2 = Mock_inventory()
    host1.name = "localhost.localdomain"
    host2.name = "localhost"
    host1.name_variables = {'inventory_hostname': "localhost.localdomain", 'inventory_hostname_short': "localhost" }

# Generated at 2022-06-13 13:53:05.453540
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.inventory_hostnames
    lookup_module = ansible.plugins.lookup.inventory_hostnames.LookupModule()
    hosts = ["foobar1", "foobar2", "baz", "baz1"]
    variables = {
        "groups": {
            "foobar": [hosts[0], hosts[1]],
            "baz": [hosts[2], hosts[3]]
        },
        "hostvars":{
            "foobar1": {
                "ansible_host": "localhost",
                "ansible_port": 22
            },
            "foobar2": {
                "ansible_host": "127.0.0.1",
                "ansible_port": 22
            }
        }
    }


# Generated at 2022-06-13 13:53:11.876986
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    terms = ['all']
    variables = {'groups':{'group1':['host1', 'host2']}}
    lookup = LookupModule()

    # Act
    actual = lookup.run(terms, variables)

    # Assert
    # "host1", "host2" will be in any order
    assert len(actual) == 2
    assert ('host1' in actual) and ('host2' in actual)



# Generated at 2022-06-13 13:53:16.137989
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run([]) == []

    assert LookupModule().run(['all:!www'], {
        'groups': {
            'all': ['www1', 'www2'],
            'www': ['www1', 'www2']
        }
    }) == ['www1', 'www2']

# Generated at 2022-06-13 13:53:29.165323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Testing with hosts
    hosts = ['127.0.01']
    variables = {
        'groups': {
            'all': hosts
        }
    }

    terms = "all"
    result = lookup_module.run(terms, variables)
    assert result == hosts, "Should get the hosts only"

    # Testing with groups in inventory file
    all = ['127.0.02']
    variables = {
        'groups': {
            'all': all,
            'group1': ['127.0.03', '127.0.04']
        }
    }

    terms = "all"
    result = lookup_module.run(terms, variables)
    assert result == all, "Should get the list of hosts in group all"

    terms = "all:group1"
   

# Generated at 2022-06-13 13:53:43.298045
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    hosts = [
        'test1.example.org',
        'test2.example.org',
        'test3.example.org'
    ]
    groups = {
        'test': hosts,
        'apache': hosts,
        'databases': hosts
    }
    variables = {
        'groups': groups
    }


# Generated at 2022-06-13 13:53:55.785590
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch
    from ansible.vars.hostvars import HostVars

    # Tests on _hosts and _meta keys.
    # Methods not implemented by the InventoryManager classes 
    # should return empty lists.
    class MockInventoryManager(object):
        def __init__(self, loader):
            test_groups = {
                'all': ["A", "B", "C"],
                'webservers': ["A", "B"],
                'dbservers': ["B", "C"],
            }

# Generated at 2022-06-13 13:54:06.796286
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    manager = LookupModule()
    variables = {'groups': {'all': {'srv1', 'srv2'}, 'www': {'srv3'}}}

    # Test with empty host pattern
    assert manager.run([''], variables) == []
    # Test with all:!www host pattern
    assert manager.run(['all:!www'], variables) == ['srv1', 'srv2']
    # Test with invalid host pattern
    assert manager.run(['unknown:host'], variables) == []
    # Test with invalid groups
    assert manager.run(['unknow:host', 'all:!www'], variables) == ['srv1', 'srv2']
    # Test with group_names
    assert manager.run(variables['groups'].keys(), variables) == ['all', 'www']

# Generated at 2022-06-13 13:54:14.595493
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    terms = 'all:!www'
    variables = {
        'groups': {
            'www': ['www-01', 'www-02'],
            'all': ['www-01', 'www-02', 'db-01', 'db-02']
        }
    }
    data = lookup_obj.run(terms, variables=variables)
    assert data == ['db-01', 'db-02']

# Generated at 2022-06-13 13:54:24.836262
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Tests the method run of class LookupModule on:
    """
    lookup = LookupModule()
    assert lookup.run(["host1"]) == ["host1"]
    assert lookup.run(["host*"]) == ["host1"]
    assert lookup.run(["*"]) == ["host1"]
    assert lookup.run(["all"]) == ["host1"]
    assert lookup.run(["all", "!host2"]) == ["host1"]
    assert lookup.run(["all:!host2"]) == ["host1"]
    assert lookup.run(["host1:host2"]) == []
    assert lookup.run(["host2"]) == []
    assert lookup.run(["all:host2"]) == []
    assert lookup.run(["all","host2"]) == []

# Generated at 2022-06-13 13:54:26.094650
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass
    #TODO

# Generated at 2022-06-13 13:54:33.955240
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = "host1"
    variables = {}
    variables['groups'] = {}
    variables['groups']['group1'] = ['host1', 'host2', 'host3']
    variables['groups']['group2'] = ['host2', 'host3', 'host4']
    variables['groups']['group3'] = ['host3']
    result = module.run(terms, variables)
    #assert result[0] == 'host1'
    assert result == ['host1']

# Generated at 2022-06-13 13:54:38.752793
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import pytest

    test_cases = [
        (['', '', 'all:!www'], ['localhost']),
    ]

    for test_case in test_cases:
        args, expected = test_case
        lookup_obj = LookupModule()
        returned = lookup_obj.run(*args, variables={'groups': {'all': ['localhost'], 'www': ['192.168.1.101']}})
        assert returned == expected

# Generated at 2022-06-13 13:54:45.051439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    hosts = [
        'local',
        'dog',
        'cat',
        ]
    groups = {
        'dogs': ['dog']
    }

    terms = [
        '*',
        '%s:dog' % InventoryManager._pattern_tokens['all']
    ]

    variables = {'groups': groups}

    test_llm = LookupModule()
    assert hosts == test_llm.run(terms, variables=variables)

# Generated at 2022-06-13 13:54:49.153239
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    terms = ['all:!www']
    variables = {
        'inventory_dir': 'ansible/inventory',
        'groups': {
            'all': ['localhost'],
            'www': ['localhost'],
            'db': ['localhost'],
            'dev': ['localhost'],
            'prod': ['localhost']
        }
    }
    assert l.run(terms, variables) == ['localhost']

# Generated at 2022-06-13 13:55:00.788657
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_hosts = {'A': ['127.0.0.1'], 'B': ['127.0.0.2']}
    test_variables = {'groups': test_hosts, 'group_names': list(test_hosts.keys())}

    result = LookupModule().run(terms=['A'], variables=test_variables)
    assert result == ['127.0.0.1']

    result = LookupModule().run(terms=['B'], variables=test_variables)
    assert result == ['127.0.0.2']

    result = LookupModule().run(terms=['A:B'], variables=test_variables)
    assert result == ['127.0.0.1', '127.0.0.2']


# Generated at 2022-06-13 13:55:08.211012
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a class object from the lookup module
    from ansible.plugins.lookup import LookupModule
    lookup = LookupModule()

    # Mock variables
    variables = {
        'groups': {
            'all': ['www.example.com', 'www.example.net', 'localhost', 'test.example.com'],
            'www': ['www.example.com', 'www.example.net'],
            'other': ['localhost'],
            'test': ['test.example.com'],
            'example': ['www.example.com', 'www.example.net', 'test.example.com']
        }
    }

    # Pattern 'all'
    # Expected result: ['www.example.com', 'www.example.net', 'localhost', 'test.example.com']

# Generated at 2022-06-13 13:55:08.872305
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(False)

# Generated at 2022-06-13 13:55:18.452650
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    t = [
        ['all:!www']
    ]
    v = {
            "groups": {
                "www": ["www1", "www2"],
                "db": ["db1", "db2"],
                "mon": ["mon1", "mon2"],
                "all": ["www1", "www2", "db1", "db2", "mon1", "mon2"],
                "ungrouped": []
            },
        }

    assert l.run(t, v) == ['db1', 'db2', 'mon1', 'mon2']

# Generated at 2022-06-13 13:55:28.940997
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 13:55:41.120323
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:55:46.973136
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_terms = "all:!www"
    test_variables = {'groups': {'all': ['zeta', 'ypsilon', 'omega'], 'www': ['alpha', 'beta']}}
    expected = ['zeta', 'ypsilon', 'omega']
    lookup_module = LookupModule()
    assert lookup_module.run(test_terms, test_variables) == expected

# Generated at 2022-06-13 13:55:51.297613
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    expected_result = ['host1', 'host2']

    # Creating an object of class LookupModule
    lookup_module = LookupModule()

    # Calling method run of class LookupModule
    result = lookup_module.run(['a'], {'groups': {'testgroup': ['host1', 'host2']}},)

    assert sorted(result) == sorted(expected_result)

# Generated at 2022-06-13 13:56:02.008055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Testing method run of class LookupModule")
    test_class = LookupModule()

    # Test with a list of hosts and a list of terms
    terms = ['a', 'b']
    hosts = ['c', 'd']
    variables = {'groups': {'group1': hosts}}
    assert test_class.run(terms, variables=variables) is None

    # Test with a list of hosts and pattern of hostname
    terms = 'myhost'
    hosts = ['c', 'myhost']
    variables = {'groups': {'group1': hosts}}
    assert test_class.run(terms, variables=variables) == ['myhost']


# Generated at 2022-06-13 13:56:02.888931
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert 1 == 1

# Generated at 2022-06-13 13:56:07.127197
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    result = lookup_module.run([], {}, inventory=["foo", "bar", "baz"])
    assert result == ["foo", "bar", "baz"]

# Generated at 2022-06-13 13:56:16.691803
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.plugins.loader import LookupModule

    _dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
    }
    lookup = LookupModule()
    assert lookup._flatten(dict(_dict), reducer=lambda x, y: x * y) == 720
    assert lookup._flatten(dict(_dict)) == [1, 2, 3, 4, 5, 6]
    assert lookup._flatten(dict(_dict), depth=0) == [1, 2, 3, 4, 5, 6]
    assert lookup._flatten

# Generated at 2022-06-13 13:56:20.126054
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule.run(LookupModule(), ['all'], {'groups':{'all':['test1']}})
    assert result == ['test1'], result

# Generated at 2022-06-13 13:56:36.246704
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['www', 'all']
    variables={'hostvars':
                    [{'ansible_host': '172.16.1.1', 'ansible_port': '22', 'ansible_user': 'root', 'ansible_ssh_pass': 'H4h4h4h4h4!'}],
              'groups':
                    {'all': ['172.16.1.1'],
                     'web': []},
              'inventory_file': '/home/centos/inventory.ini',
              'inventory_dir': '/home/centos',
              'inventory_dirs': []
              }
    #print(dir(LookupModule))
    ret=LookupModule.run(self=None, terms=terms, variables=variables)
    print(ret)



# Generated at 2022-06-13 13:56:49.412582
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(None, terms=None, variables=None, **{}) == []

    assert LookupModule.run(None, terms='ABCDEF', variables={}, **{}) == []

    # Case: groups = {'group1': ['host1']}
    assert LookupModule.run(None, terms=['group1'], variables={'groups': {'group1': ['host1']}}, **{}) == ['host1']

    # Case: groups = {'group1': ['host1', 'host2']}
    assert LookupModule.run(None, terms=['group1'], variables={'groups': {'group1': ['host1', 'host2']}}, **{}) == ['host1', 'host2']

    # Case: groups = {'group1': ['host1'], 'group2': ['

# Generated at 2022-06-13 13:56:50.005545
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:57:01.683854
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # given
    # assert that LookupModule is a class of class LookupBase
    assert issubclass(LookupModule, LookupBase)

    # assert that LookupModule has the method run
    assert callable(getattr(LookupModule, "run", None))

    # when
    # assert that LookupModule is an instance of class LookupBase
    lookup_module = LookupModule()

    # assert that init method of class LookupModule returns None
    assert lookup_module is not None

    # assert that it retruns a list of hosts
    assert lookup_module.run(terms=['all']) == ['test_host_1', 'test_host_2']

    # assert that it returns a list of hosts

# Generated at 2022-06-13 13:57:13.321940
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # check availability of inventory pattern matching and custom inventories
    print('TEST: inventory_hostnames lookup plugin')
    print('TESTSKIP: InventoryManager class is available in ansible>=2.4')
    print('TESTSKIP: get_hosts method is available in ansible>=2.4')

    # create the inventory manager with a custom inventory
    manager = InventoryManager(None, parse=False)
    for group, hosts in { 'test1': ['test1_1'], 'test2': ['test2_1', 'test2_2'] }.items():
        manager.add_group(group)
        for host in hosts:
            manager.add_host(host, group=group)

    # test inventory pattern matching
    print(manager.get_hosts(pattern='test*'))

# Generated at 2022-06-13 13:57:20.988846
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Instance of LookupModule
    lookupM = LookupModule()
    # run method() of LookupModule returns empty list
    assert lookupM.run(terms=None, variables=None, **None) == []
    # run method() of LookupModule returns empty list
    assert lookupM.run(terms=None, variables=dict(groups=dict(group_name=['hostA', 'hostB'])), **None) == []

# Generated at 2022-06-13 13:57:21.840681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:57:30.994322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    data = ['host1', 'host2', 'host3', 'host4']
    # Create an instance of the class LookupModule
    lookup = LookupModule()
    # Create an instance of the class AnsibleLoader with 'data' as the argument
    loader = LookupBase.AnsibleLoader('data', data)
    # Create an instance of the class InventoryManager
    manager = InventoryManager(loader, parse=False)

    # Add a group
    manager.add_group("group1")
    # Add a host to "group1"
    manager.add_host("host1", group="group1")
    # Add an "group2"
    manager.add_group("group2")
    # Add hosts to "group2"

# Generated at 2022-06-13 13:57:41.647664
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule."""
    terms = ''
    variables = None

    lookup_plugin = LookupModule()
    terms = [
        'foo',
        'bar',
        'baz',
        'foo,bar',
        'foo:bar',
        'foo:bar,baz',
        ':bar:baz',
        'all',
        'all,foo',
        'all:foo',
        'all:foo,bar'
    ]
    for term in terms:
        try:
            lookup_plugin.run(terms=term, variables=variables)
        except AnsibleError:
            print("Term '%s' is not a valid host pattern" % term)

# Generated at 2022-06-13 13:57:50.357384
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert list(run(None, [ 'all:!www' ])) == [h.name for h in manager.get_hosts(pattern=terms)]
    assert list(run(None, [ 'all:!www' ])) == []
    assert list(run(None, [ 'all:!www' ])) == [h.name for h in manager.get_hosts(pattern=terms)]
    assert list(run(None, [ 'all:!www' ])) == [h.name for h in manager.get_hosts(pattern=terms)]

# Generated at 2022-06-13 13:58:04.541673
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = 'test'
    variables = {'groups': {'www': ['www1', 'www2', 'www3'], 'db': ['db1', 'db2', 'db3']}}
    manager = InventoryManager(LookupBase._loader, parse=False)
    # expected_result = ['www1', 'www2', 'www3']
    expected_result = ['www1', 'www2', 'www3', 'db1', 'db2', 'db3']
    assert sorted(expected_result) == sorted(LookupModule(manager, terms, variables).run())


# Generated at 2022-06-13 13:58:18.410573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a fake inventory object and variables object to use
    def run_unrequired(self, terms, variables=None, **kwargs):
        return []
    
    manager = InventoryManager(loader=None, parser=None, sources=None,
                               whitelist=None, Host=None, Group=None)

    lookup_base = LookupBase()
    lookup_base.run = run_unrequired

    lookup_module = LookupModule()
    lookup_module._loader = None
    lookup_module._templar = None

    # create a test host and group objects
    class Host():
        def __init__(self, hostname):
            self.name = hostname


    class Group():
        def __init__(self, groupname, hostnames):
            self.name = groupname
            self.hosts = hostnames



# Generated at 2022-06-13 13:58:22.487815
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    inventory = ["all:", "  hosts:", "    test:", "    test2:"]
    return_value = [h.name for h in manager.get_hosts(pattern=terms)]
    # Placeholder for test


# Generated at 2022-06-13 13:58:35.794773
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ## test setup
    def _inject(obj, attr, val):
        setattr(obj, attr, val)

    class FakeInventory(object):
        def __init__(self, host, groups):
            self._host = host
            self._groups = groups

        def get_host(self, host):
            return self

        def get_hosts(self, pattern):
            return self

        def get_hosts_by_pattern(self):
            return self

        def get_groups(self, group):
            if group in self._groups:
                return [self._groups[group]]
            return []

        def list_hosts(self):
            return self._host

        def list_groups(self):
            return self._groups.keys()

        def list_all_groups(self):
            return self._

# Generated at 2022-06-13 13:58:41.124388
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["all"]
    # vars is a dict to be used as a fake inventory
    vars = {'groups': {'all': ['host1', 'host2']}}
    lm = LookupModule()
    result = lm.run(terms, variables=vars)
    assert result == ['host1', 'host2']

# Generated at 2022-06-13 13:58:50.228054
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TEST 1
    # pylint: disable=undefined-variable
    # variables['groups'] = {'group1': {'host1', 'host2'}, 'group2': {'host3', 'host4'}}
    # mock ansible.errors.AnsibleError = None
    # mock ansible.inventory.manager.InventoryManager = None
    # mock ansible.plugins.lookup.LookupBase = InventoryManager
    # assert LookupModule.run('all', variables) == {'host1', 'host2', 'host3', 'host4'}
    pass

# Generated at 2022-06-13 13:58:59.608501
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    manager = InventoryManager(None, parse=False)

    for group, hosts in {'group1': ['host1'], 'group2': ['host1', 'host2'],
                         'group3': ['host3'], 'group4': ['host4', 'host5'],
                         'group5': ['host2'], 'group6': ['host2', 'host4']}.items():
        manager.add_group(group)
        for host in hosts:
            manager.add_host(host, group=group)

    assert LookupModule(None, None).run(terms='all', variables={'groups': manager.list_groups()}) ==\
        ['host1', 'host2', 'host3', 'host4', 'host5']

# Generated at 2022-06-13 13:59:05.330060
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    hostnames = ['test1.example.com', 'test2.example.com']
    terms = 'test?'
    variables = {'groups': {'test': ['test1.example.com', 'test2.example.com']}}
    lookup = LookupModule()
    assert lookup.run(terms, variables) == hostnames

# Generated at 2022-06-13 13:59:18.210836
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create class instance
    inventory_hostnames = LookupModule()

    # Create test dictionaries
    terms_test = ['pattern_1', 'pattern_2']
    variables_test = {
        'groups': {
            'test_group': ['host_1', 'host_2'],
            'other_group': ['host_3', 'host_4']
        }
    }
    kwargs_test = {}

    # Run method
    result = inventory_hostnames.run(terms=terms_test, variables=variables_test, **kwargs_test)

    expected_result = {
        "host_1": ["test_group"],
        "host_2": ["test_group"],
        "host_3": ["other_group"],
        "host_4": ["other_group"],
    }

    assert result

# Generated at 2022-06-13 13:59:28.808227
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from fixture_loader import path
    from yaml_fixtures import load_fixtures
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[path("hosts.yml")])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    context = PlayContext()
    context._variable_manager = variable_manager

    fixtures = load_fixtures("fixture_inventory_hostnames.yml")
    for fixture in fixtures:
        lookup_module = LookupModule()