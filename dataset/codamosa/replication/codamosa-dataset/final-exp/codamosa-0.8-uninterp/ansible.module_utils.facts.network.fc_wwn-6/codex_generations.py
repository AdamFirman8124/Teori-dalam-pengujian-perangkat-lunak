

# Generated at 2022-06-13 01:27:37.277811
# Unit test for method collect of class FcWwnInitiatorFactCollector

# Generated at 2022-06-13 01:27:38.443997
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector() is not None


# Generated at 2022-06-13 01:27:48.272493
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModuleMock()
    fc = FcWwnInitiatorFactCollector(module)
    facts = fc.collect()
    assert fc.name in facts
    assert not facts['fibre_channel_wwn']
    module.run_command = AnsibleModuleMock.run_command_osx
    facts = fc.collect()
    assert 'fc_wwn_initiator' in facts
    assert facts['fc_wwn_initiator'][0] == '0x50060b00006975ec'
    module.run_command = AnsibleModuleMock.run_command_linux
    facts = fc.collect()
    assert 'fibre_channel_wwn' in facts

# Generated at 2022-06-13 01:27:50.015706
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn = FcWwnInitiatorFactCollector()
    assert fcwwn.name == 'fibre_channel_wwn'
    assert fcwwn._fact_ids == set()

# Generated at 2022-06-13 01:27:52.469776
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import Collector
    obj = FcWwnInitiatorFactCollector()
    assert isinstance(obj, Collector)

# Generated at 2022-06-13 01:27:56.918030
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import Collector

    collector = Collector(None, None)
    collector.collect_device_facts = lambda module: None
    fact_collector = FcWwnInitiatorFactCollector(collector, None)
    facts = fact_collector.collect()
    assert facts['fibre_channel_wwn'][0] == '21000024ff52a9bb'

# Generated at 2022-06-13 01:28:01.941819
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """

    test_module = AnsibleModule(argument_spec={})
    res = FcWwnInitiatorFactCollector().collect(module=test_module, collected_facts=None)
    assert res is not None

# Generated at 2022-06-13 01:28:05.365647
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fact_collector._fact_ids

# Generated at 2022-06-13 01:28:09.504320
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_initiator = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator.name == 'fibre_channel_wwn'
    assert fc_wwn_initiator.collect() == {}


# Generated at 2022-06-13 01:28:13.250678
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcObj = FcWwnInitiatorFactCollector()
    assert fcObj.name == 'fibre_channel_wwn'
    assert fcObj._fact_ids == set()

# Generated at 2022-06-13 01:28:32.022422
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'

    # empty fact collection
    fact_list = fc_facts.collect()
    assert 'fibre_channel_wwn' in fact_list
    assert len(fact_list['fibre_channel_wwn']) == 0

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 01:28:36.183592
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    checks if return of collect method is a dict with a single entry:
    'fibre_channel_wwn' = []
    """
    test_obj = FcWwnInitiatorFactCollector()
    result = test_obj.collect()
    assert isinstance(result, dict)
    assert len(result) == 1
    assert 'fibre_channel_wwn' in result
    assert isinstance(result['fibre_channel_wwn'], list)

# Generated at 2022-06-13 01:28:40.624115
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:28:52.700559
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = {'fibre_channel_wwn': ['10000090fa1658de', '10000090fa551509']}
    # set sys.platform to linux
    sys.platform = 'linux'
    # create a temporary facts.d directory and add 2 test files
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmp_dirname:
        # create test files
        lines = ['0x21000014ff52a9bb']
        fcfile1 = tmp_dirname + '/sys/class/fc_host/1/port_name'
        fcfile2 = tmp_dirname + '/sys/class/fc_host/2/port_name'

# Generated at 2022-06-13 01:29:00.282956
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Unit test for method collect of class FcWwnInitiatorFactCollector"""

    class MockModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, executable, opt_dirs=[]):
            if executable == 'lsdev':
                return 'lsdev'
            elif executable == 'lscfg':
                return 'lscfg'
            elif executable == 'fcinfo':
                return 'fcinfo'
            elif executable == 'ioscan':
                return 'ioscan'
            elif executable == 'fcmsutil':
                return 'fcmsutil'
            return None


# Generated at 2022-06-13 01:29:11.865382
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    - include_mounts
      - False
    """
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.fibre_channel_wwn import FcWwnInitiatorFactCollector
    class MockModule():
        def __init__(self):
            self.params = {}
        def get_bin_path(self, *args, **kwargs):
            return '/bin/fctest'
        def run_command(self, *args, **kwargs):
            return 0, '0x21000014ff52a9bb\n0x21000014ff52a9bc', None


    fc_facts_collector = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:29:15.880483
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts is not None
    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts.collect() == {}

# Generated at 2022-06-13 01:29:26.686440
# Unit test for method collect of class FcWwnInitiatorFactCollector

# Generated at 2022-06-13 01:29:28.618056
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    # TODO: write unit test
    pass

# Generated at 2022-06-13 01:29:30.566988
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.collect() is None

# Generated at 2022-06-13 01:29:45.724206
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:48.505983
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    f = FcWwnInitiatorFactCollector()
    f.collect()
    assert isinstance(f.data, dict)
    assert 'fibre_channel_wwn' in f.data



# Generated at 2022-06-13 01:29:53.445130
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import Collector

    facts = ansible_collector.get_facts()
    facts['ansible_collector'] = Collector

    collector = FcWwnInitiatorFactCollector()
    result = collector.collect(None, facts)
    # this particular fact depends on the test platform, only check
    # if it's empty
    assert not result['fibre_channel_wwn']

# Generated at 2022-06-13 01:29:56.257530
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector().collect()
    assert 'fibre_channel_wwn' in fc_facts.keys()

# Generated at 2022-06-13 01:30:01.036385
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids == set()
    assert fc_collector._platform == 'Generic'
    assert fc_collector._is_platform_supported() is False

# Generated at 2022-06-13 01:30:04.289543
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fact_collector._fact_ids

# Generated at 2022-06-13 01:30:07.844969
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts_collector = FcWwnInitiatorFactCollector()
    assert facts_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:12.571840
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn = FcWwnInitiatorFactCollector()
    assert fc_wwn.name == 'fibre_channel_wwn'
    assert isinstance(fc_wwn.collect(), dict)
    assert isinstance(fc_wwn._fact_ids, set)

# Unit test to validate collection of facts

# Generated at 2022-06-13 01:30:17.223333
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    if fc.name is not 'fibre_channel_wwn':
        raise Exception("Constructor of class FcWwnInitiatorFactCollector() failed")


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:20.111478
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert obj.collect() == {}

# Generated at 2022-06-13 01:30:36.774210
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact = FcWwnInitiatorFactCollector()
    assert fact.name == 'fibre_channel_wwn'
    assert set(fact.collect().keys()) == set(['fibre_channel_wwn'])

# Generated at 2022-06-13 01:30:38.337797
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:48.322477
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    def get_bin_path_mock(path, opt_dirs=[]):
        if path == "lsdev":
            return "/usr/sbin/lsdev"
        if path == "lscfg":
            return "/usr/sbin/lscfg"
        if path == "ioscan":
            return "/usr/sbin/ioscan"
        if path == "fcmsutil":
            return "/opt/fcms/bin/fcmsutil"
        return None

    def run_command_mock(cmd):
        output = ""

# Generated at 2022-06-13 01:30:52.142942
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Check if constructor raises an exception without argument(s) provided
    try:
        FcWwnInitiatorFactCollector()
    except Exception as my_exception:
        assert(type(my_exception) == TypeError)

# Generated at 2022-06-13 01:30:59.533871
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import collectors
    my_collector = FcWwnInitiatorFactCollector()
    assert my_collector.name == 'fibre_channel_wwn', \
        'Incorrect collector name returned'
    assert my_collector.priority == Collector.DEFAULT_PRIORITY, \
        'Invalid priority returned'
    assert my_collector.fact_ids == set(), \
        'Invalid fact_ids returned'
    
test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:31:10.286070
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Creating object FcWwnInitiatorFactCollector
    fc_collector_obj = FcWwnInitiatorFactCollector()
    # Creating dictionary of arguments required by method collect of class FcWwnInitiatorFactCollector
    fc_collector_args = {}
    # Calling method collect of class FcWwnInitiatorFactCollector with parameters fc_collector_args
    fc_collector_facts = fc_collector_obj.collect(fc_collector_args)
    # Calling ansible assert module for validating the data returned by method collect of class FcWwnInitiatorFactCollector
    assert fc_collector_facts is not None


# Generated at 2022-06-13 01:31:18.009472
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    facts = {}
    col = FcWwnInitiatorFactCollector()

    # check linux platform
    if sys.platform == 'linux':
        facts['ansible_system'] = 'Linux'
        # fake a linux platform and check content of collect method
        facts['ansible_facts'] = {}
        col.collect(collected_facts=facts)
        assert 'fibre_channel_wwn' in facts['ansible_facts'], \
            "linux - results of collect method should contain 'fibre_channel_wwn'"

    # check solaris 10 platform
    if sys.platform == 'sunos5':
        facts['ansible_system'] = 'SunOS'
        facts['ansible_distribution'] = 'Solaris'
        facts['ansible_distribution_major_version'] = '10'
        #

# Generated at 2022-06-13 01:31:27.224088
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class MockModule:
        def __init__(self):
            self.name = 'module name'
            self.paths = {}

        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'fcinfo':
                return 'fcinfo'
            elif name == 'ioscan':
                return 'ioscan'
            elif name == 'lscfg':
                return 'lscfg'
            elif name == 'prtconf':
                return 'prtconf'
            elif name == 'fcmsutil':
                return 'fcmsutil'

        def run_command(self, cmd):
            rc = 0
            stdout = stderr = ''

# Generated at 2022-06-13 01:31:30.403283
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_obj = FcWwnInitiatorFactCollector()
    assert fc_fact_obj is not None

# Generated at 2022-06-13 01:31:33.553609
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    fc_fact_collector = FcWwnInitiatorFactCollector()

    assert fc_fact_collector.name == "fibre_channel_wwn"
    assert fc_fact_collector.collect()

# Generated at 2022-06-13 01:31:50.097336
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert obj._fact_ids == set()



# Generated at 2022-06-13 01:31:53.422670
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc.valid is False
    assert '_fact_ids' in dir(fc)

# Generated at 2022-06-13 01:31:57.648413
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector.collect() == {'fibre_channel_wwn': []}

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:32:00.075303
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert len(fc._fact_ids) == 0

# Generated at 2022-06-13 01:32:07.929482
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # check with empty file
    module = DummyModule()
    fc_facts = FcWwnInitiatorFactCollector().collect(module=module, collected_facts=None)
    assert fc_facts['fibre_channel_wwn'] == []
    # check with content of file
    module = DummyModule(data="0x21000014ff52a9bb")
    fc_facts = FcWwnInitiatorFactCollector().collect(module=module, collected_facts=None)
    assert fc_facts['fibre_channel_wwn'] == ['21000014ff52a9bb']


# Generated at 2022-06-13 01:32:09.955020
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test_obj = FcWwnInitiatorFactCollector()
    assert(test_obj.name == 'fibre_channel_wwn')

# Generated at 2022-06-13 01:32:18.746364
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    base_dir = 'ansible_collections.notstdlib.moveitallout.tests/' + \
               'unit/module_utils/facts/collector/fibre_channel_wwn'
    module = None
    facts_collector = FcWwnInitiatorFactCollector()
    # items defined by a function in ansible.module_utils.facts.utils.get.py
    # are tested in each fact collector's test
    required_keys = [
        'fibre_channel_wwn'
    ]
    collected_facts = facts_collector.collect(module=module)
    assert set(collected_facts.keys()) == set(required_keys)

# Generated at 2022-06-13 01:32:30.978469
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    # initalize test data
    mock_module = type('module', (), {})()
    mock_module.run_command = lambda command: ['', '', '']
    mock_module.get_bin_path = lambda name, opt_dirs=None: '/usr/bin/'
    mock_module.exit_json = lambda: None

    # initalize instance of class FcWwnInitiatorFactCollector
    fact_collector = FcWwnInitiatorFactCollector()

    # run unit test with mock data
    result = fact_collector.collect(mock_module)

    # verify result
    assert result['fibre_channel_wwn']
    assert isinstance(result['fibre_channel_wwn'], list)

    # verify class variables
    assert FcWwnInitiatorFact

# Generated at 2022-06-13 01:32:33.833356
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []
    fc_facts['fibre_channel_wwn'].append('210000e08b332a4b')
    assert FcWwnInitiatorFactCollector.collect() == fc_facts

# Generated at 2022-06-13 01:32:36.907394
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_initiator_fc = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator_fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:33:12.825373
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class MockModule:
        def __init__(self):
            self.params = dict(
                gather_subset='!all',
                gather_timeout=10,
            )
        def get_bin_path(self, name, **kwargs):
            return name
        def run_command(self, cmd):
            return 0, '', ''
    # Test fc_facts on linux platforms
    module = MockModule()
    test_FcWwnInitiatorFactCollector_collect_platform('linux', module)
    # Test fc_facts on aix platforms
    module = MockModule()
    test_FcWwnInitiatorFactCollector_collect_platform('aix', module)
    # Test fc_facts on hp-ux platforms
    module = MockModule()
    test_FcWwnInitiatorFact

# Generated at 2022-06-13 01:33:14.517761
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert 'fibre_channel_wwn' == obj.name



# Generated at 2022-06-13 01:33:16.815001
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    result = FcWwnInitiatorFactCollector().collect()
    assert result.get('fibre_channel_wwn') is not None

# Generated at 2022-06-13 01:33:28.579366
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import Collectors

    class FakeModule(object):

        def __init__(self, platform):
            self.platform = platform

        def get_bin_path(self, name, opt_dirs=[]):
            if 'ioscan' in name:
                return '/usr/sbin/ioscan'
            elif 'fcmsutil' in name:
                return '/opt/fcms/bin/fcmsutil'
            elif 'lscfg' in name:
                return '/usr/sbin/lscfg'
            elif 'lsdev' in name:
                return '/usr/sbin/lsdev'
            elif 'fcinfo' in name:
                return '/usr/sbin/fcinfo'

# Generated at 2022-06-13 01:33:29.157349
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    pass

# Generated at 2022-06-13 01:33:32.909535
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test_obj = FcWwnInitiatorFactCollector()
    assert test_obj.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:33:38.239852
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Test method FcWwnInitiatorFactCollector.collect
    """
    fcwwn_fact_collector = FcWwnInitiatorFactCollector()
    assert fcwwn_fact_collector.name == 'fibre_channel_wwn'
    assert fcwwn_fact_collector._fact_ids == set()
    fcwwn_fact_collector.collect()

# Generated at 2022-06-13 01:33:39.396326
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_obj = FcWwnInitiatorFactCollector()


# Generated at 2022-06-13 01:33:45.794162
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    import sys
    sys.platform = 'linux2'
    FcWwnInitiatorFactCollector._fact_ids.clear()
    collect_fc_facts = FcWwnInitiatorFactCollector.collect(None)
    assert collect_fc_facts['fibre_channel_wwn'] == []
    sys.platform = 'sunos5'
    collect_fc_facts = FcWwnInitiatorFactCollector.collect(None)
    assert collect_fc_facts['fibre_channel_wwn'] == []
    sys.platform = 'aix7'
    collect_fc_facts = FcWwnInitiatorFactCollector.collect(None)
    assert collect_fc_facts['fibre_channel_wwn'] == []
    sys.platform = 'hp-ux11'

# Generated at 2022-06-13 01:33:49.310673
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector(None, None).collect()
    assert fc_facts['fibre_channel_wwn']
    assert len(fc_facts['fibre_channel_wwn']) > 0

# Generated at 2022-06-13 01:34:24.484031
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class MockModule:
        def __init__(self, platform_startswith, cmd_bin_path, cmd_bin_path_optional):
            self.platform = platform_startswith
            self.cmd_bin_path = cmd_bin_path
            self.cmd_bin_path_optional = cmd_bin_path_optional

        def get_bin_path(self, binary, opt_dirs=[]):
            if self.cmd_bin_path_optional == 0:
                if binary in self.cmd_bin_path:
                    return self.cmd_bin_path[binary]
            else:
                return self.cmd_bin_path[binary]


# Generated at 2022-06-13 01:34:26.546356
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:37.980289
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class MyModule(object):
        def __init__(self, rc, stdout, stderr):
            self.rc = rc
            self.stdout = stdout
            self.stderr = stderr
        def run_command(self, cmd):
            return (self.rc, self.stdout, self.stderr)
        def get_bin_path(self, cmd, opt_dirs=[]):
            return cmd
    """
    Test expected output for Linux platform
    """
    module = MyModule(0, '''
    /sys/class/fc_host/host4/port_name:0x21000014ff52a9bb
    /sys/class/fc_host/host5/port_name:0x21000014ff52a9bc
    ''', '')

    obj = Fc

# Generated at 2022-06-13 01:34:41.243418
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    facts = collector.collect()
    assert type(facts) is dict
    assert 'fibre_channel_wwn' in facts
    assert type(facts['fibre_channel_wwn']) is list

# Generated at 2022-06-13 01:34:44.368697
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn = FcWwnInitiatorFactCollector()
    assert fc_wwn.name == 'fibre_channel_wwn'
    assert fc_wwn._fact_ids == set()

# Generated at 2022-06-13 01:34:47.142963
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'
    assert collector.collect() == {}

# Generated at 2022-06-13 01:34:54.771690
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    sys.platform = 'linux'
    sys.modules['ansible.module_utils.facts'] = type('module', (object,), {'__name__': 'module'})
    class module(object):
        def __init__(self):
            self.fail_json = lambda x: None
            self.get_bin_path = lambda name, opt_dirs = None: None
            self.run_command = lambda name: (0, '0x21000014ff52a9bb', '')
    fc = FcWwnInitiatorFactCollector()
    facts = fc.collect({}, {})
    assert facts == dict(fibre_channel_wwn=['21000014ff52a9bb'])

# Generated at 2022-06-13 01:34:58.195304
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:35:06.944535
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector.
    """
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import get_collector_instance
    
    class Module:
        
        def __init__(self):
            self.params = {}
        
        def run_command(self, cmd):
            output = ""
            # check ioscan command

# Generated at 2022-06-13 01:35:09.273592
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == "fibre_channel_wwn"
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:36:21.098449
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector().name == 'fibre_channel_wwn'
    assert FcWwnInitiatorFactCollector()._fact_ids == set()
    assert isinstance(FcWwnInitiatorFactCollector()._fact_ids, set)

# Generated at 2022-06-13 01:36:27.413193
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import tempfile, os
    from ansible.module_utils.facts.collector import base_platform
    from ansible.module_utils.facts.collector import BaseFactCollector

    # test object to be used by unit tests
    FC_TEST = FcWwnInitiatorFactCollector()

    # create temp directory
    tmpDir = tempfile.mkdtemp()

    # platform tests
    PLATFORM_FC_FACTS = {}
    if 'linux' in base_platform.BASE_PLATFORM:
        PLATFORM_FC_FACTS = {'fibre_channel_wwn': ['21000014ff52a9bb', '21000014ff52a9bc']}
        # create temporary files

# Generated at 2022-06-13 01:36:35.902057
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import GetDataException
    from ansible.module_utils.facts import defaults

    def get_bin_path(name, opt_dirs=[]):
        if name == 'ioscan':
            return '/opt/bin/ioscan'
        elif name == 'fcmsutil':
            return '/opt/fcms/bin/fcmsutil'
        return name

    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.tmpdir = defaults.get_default_fact_cache_dir()
            self.debug = False


# Generated at 2022-06-13 01:36:41.027709
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModule
    module.debug = True
    module.run_command = mocked_run_command
    fci = FcWwnInitiatorFactCollector()
    facts = fci.collect(module=module)
    assert facts == {'fibre_channel_wwn': ['10:00:00:90:fa:17:3b:1a']}

# Mock of subprocess.run_command

# Generated at 2022-06-13 01:36:45.538666
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # cannot create an instance of BaseFactCollector, as it is an abstract class
    f = FcWwnInitiatorFactCollector()
    print(f.collect())

if __name__ == '__main__':
    # Unit test of the method collect() in class FcWwnInitiatorFactCollector
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:36:47.286343
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fwci = FcWwnInitiatorFactCollector()
    assert fwci.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:36:49.450455
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in collector._fact_ids

# Generated at 2022-06-13 01:36:55.122645
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn_fact_collector = FcWwnInitiatorFactCollector()
    assert fcwwn_fact_collector.name == 'fibre_channel_wwn'
    assert fcwwn_fact_collector.collect() == {}
    assert fcwwn_fact_collector.depends_on() == []

# Generated at 2022-06-13 01:37:01.631501
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    testing = FcWwnInitiatorFactCollector()
    assert testing.name == 'fibre_channel_wwn'
    assert testing._fact_ids == set(['fibre_channel_wwn'])

    # platform specific facts are not collected on all platforms
    if sys.platform.startswith('linux'):
        assert 'fibre_channel_wwn' in testing.collect().keys()


if __name__ == '__main__':
    # Unit test for class FcWwnInitiatorFactCollector
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:37:05.280354
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector is not None
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()
