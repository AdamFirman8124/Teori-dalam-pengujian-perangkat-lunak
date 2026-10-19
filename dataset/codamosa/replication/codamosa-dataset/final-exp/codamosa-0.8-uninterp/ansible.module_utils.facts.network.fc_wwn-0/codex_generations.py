

# Generated at 2022-06-13 01:27:29.454788
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:31.745567
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # collect facts
    facts = FcWwnInitiatorFactCollector().collect()
    # check if necessary keys are present
    assert facts
    assert 'fibre_channel_wwn' in facts, "no 'fibre_channel_wwn' key in facts"

# Generated at 2022-06-13 01:27:35.888092
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_module = sys.modules[__name__]
    obj = fact_module.FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 01:27:36.413644
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
  pass

# Generated at 2022-06-13 01:27:39.992405
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
  fc_wwn_initiator_fact_collector = FcWwnInitiatorFactCollector()
  if fc_wwn_initiator_fact_collector is None:
    raise ImportError('Failed to load FcWwnInitiatorFactCollector.')


# Generated at 2022-06-13 01:27:41.824749
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == "fibre_channel_wwn"

# Generated at 2022-06-13 01:27:47.936464
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Unit Test for method collect of class FcWwnInitiatorFactCollector:
#
# - test 'linux' platform
# - test 'sunos' platform
# - test 'aix' platform
# - test 'hp-ux' platform
#

# Generated at 2022-06-13 01:27:57.401079
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    import sys
    import os.path

    if platform.system() == 'Linux':
        sys.modules['ansible.module_utils.facts.sys_info'] = type('DummyModule', (object,), {'distribution': 'Linux', 'distribution_release': '7.5'})
        sys.modules['ansible_module_utils.facts.collector.sys_info'] = sys.modules['ansible.module_utils.facts.sys_info']
        sys.modules['ansible.module_utils.facts.collector.base'] = sys.modules['ansible.module_utils.facts.sys_info']
    elif platform.system() in 'SunOS':
        os.environ['PATH'] = '/bin:/usr/bin'

# Generated at 2022-06-13 01:27:59.880519
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    # instantiate an object
    fact_collector = FcWwnInitiatorFactCollector()
    # make sure that instance is valid and its name is properly set
    assert fact_collector is not None
    assert fact_collector.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:28:02.960741
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnInitiatorFactCollector_obj = FcWwnInitiatorFactCollector()
    print(FcWwnInitiatorFactCollector_obj.collect())


# Generated at 2022-06-13 01:28:17.290919
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModuleMock()
    fc = FcWwnInitiatorFactCollector()
    fc_facts = fc.collect(module=module)
    assert "fibre_channel_wwn" in fc_facts
    assert isinstance(fc_facts['fibre_channel_wwn'], list)



# Generated at 2022-06-13 01:28:20.241622
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    v = FcWwnInitiatorFactCollector()
    fc_facts = v.collect()
    assert 'fibre_channel_wwn' in fc_facts
    assert isinstance(fc_facts['fibre_channel_wwn'], list)


# Generated at 2022-06-13 01:28:21.280448
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:28:22.182152
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnInitiatorFactCollector.collect()

# Generated at 2022-06-13 01:28:23.782984
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:28:25.485367
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    facts = collector.collect()
    assert 'fibre_channel_wwn' in facts

# Generated at 2022-06-13 01:28:33.125999
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    FACTS_COLLECTOR = FcWwnInitiatorFactCollector()
    FACTS_COLLECTOR._module = MagicMock()

    FACTS_COLLECTOR._module.run_command = MagicMock(return_value=(0, '{"fibre_channel_wwn": ["0x50060b00006975ec", "0x50060b00006975ed", "0x50060b00006975ee"]}', ''))

    assert FACTS_COLLECTOR.collect() == {"fibre_channel_wwn": ["0x50060b00006975ec", "0x50060b00006975ed", "0x50060b00006975ee"]}

# Generated at 2022-06-13 01:28:35.110357
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x

# Generated at 2022-06-13 01:28:41.966153
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # create an instance of the class, and test function
    m = FcWwnInitiatorFactCollector()
    fc_facts = m.collect()
    # example data
    # {'fibre_channel_wwn': ['21000014ff52a9bb']}
    print(fc_facts)



if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:28:44.329564
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:16.884527
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import sys
    import os
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.network.fc_wwn import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collectors.network.fc_wwn import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils.facts.utils.get_file_lines import get_file_lines_generic
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils.facts.utils.get_file_lines import get_file_lines_generic

    fc

# Generated at 2022-06-13 01:29:27.549941
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors.network.fibre_channel_wwn import FcWwnInitiatorFactCollector
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock

    collected_facts = dict()

    # range of test data
    fc_facts_1 = {'fibre_channel_wwn': ['5006048b4001e84e',
                                        '5006048b4001e850',
                                        '5006048b4001e84f',
                                        '5006048b4001e851']}

# Generated at 2022-06-13 01:29:28.885210
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:29:41.020511
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.params = {}
        def get_bin_path(self, arg, opt_dirs=[]):
            if arg == 'fcinfo':
                return '/sbin/fcinfo'
            elif arg == 'lsdev':
                return '/usr/sbin/lsdev'
            elif arg == 'lscfg':
                return '/usr/sbin/lscfg'
            elif arg == 'ioscan':
                return '/sbin/ioscan'
            elif arg == 'fcmsutil':
                return '/opt/fcms/bin/fcmsutil'
            elif arg == 'prtconf':
                # no implementation yet
                return False
            return False

# Generated at 2022-06-13 01:29:51.092939
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModuleStub
    from ansible.module_utils.facts.collector import get_collectors
    from ansible.module_utils.facts import cached
    from ansible.module_utils._text import to_bytes

    module = AnsibleModuleStub()
    fc_collector = FcWwnInitiatorFactCollector()
    facts_dict = {}
    fc_facts = fc_collector.collect(module=module, collected_facts=facts_dict)
    cached.flush()

    # The following are temporary and should be replaced with an assert_equal
    # statement once the facts are stable
    module.exit_json(changed=False, ansible_facts=fc_facts)

# Generated at 2022-06-13 01:30:01.937518
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    # import needed objects
    sys.path.insert(0, os.path.dirname(__file__))
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    module_args = dict()
    facts_module = basic.AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    
    # define our own mock class for the os.path module
    class MockOsPath(object):
        def __init__(self):
            self.os_path_exists_called = 0
            self.os_path_exists_return_value = True

# Generated at 2022-06-13 01:30:03.999169
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:30:06.142739
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = did_test_fact_collector_collect(FcWwnInitiatorFactCollector)
    assert 'fibre_channel_wwn' in fc_facts

# Generated at 2022-06-13 01:30:08.012962
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:09.565242
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()


# Generated at 2022-06-13 01:30:33.862802
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert len(fc._fact_ids) == 0

# Generated at 2022-06-13 01:30:35.503434
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcw = FcWwnInitiatorFactCollector()
    assert fcw.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:38.432303
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_fact_collector.name == 'fibre_channel_wwn'
    assert fc_fact_collector._fact_ids == set()

# Generated at 2022-06-13 01:30:44.937042
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    m = FcWwnInitiatorFactCollector()
    r = m.collect()
    assert 'fibre_channel_wwn' in r
    assert len(r['fibre_channel_wwn']) >= 1
    assert len(r['fibre_channel_wwn']) <= 2
    for wwn in r['fibre_channel_wwn']:
        assert len(wwn) == 16

# Generated at 2022-06-13 01:30:49.059462
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import Collector
    module = AnsibleModuleMock()
    fcwwninitiator = FcWwnInitiatorFactCollector.factory(module)
    assert isinstance(fcwwninitiator, Collector)
    assert isinstance(fcwwninitiator, FcWwnInitiatorFactCollector)



# Generated at 2022-06-13 01:30:54.410559
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts = FcWwnInitiatorFactCollector()
    assert facts is not None
    assert type(facts) == FcWwnInitiatorFactCollector
    assert facts.name == 'fibre_channel_wwn'
    assert len(facts._fact_ids) == 1
    assert 'fibre_channel_wwn' in facts._fact_ids


# Generated at 2022-06-13 01:31:02.526202
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    This is a unit test for method 'collect' of class
    FcWwnInitiatorFactCollector.
    """

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import FcWwnInitiatorFactCollector
    from ansible.module_utils._text import to_bytes

    # create a Collector instance
    test_collector = Collector()
    # create a FcWwnInitiatorFactCollector object
    fcwwn_obj = FcWwnInitiatorFactCollector()
    # add the FcWwnInitiatorFactCollector object to the Collector instance
    test_collector.add_collector(fcwwn_obj)
    # call method 'collect' of the Collector instance and get a dictionary
    # of facts

# Generated at 2022-06-13 01:31:04.118771
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    ob = FcWwnInitiatorFactCollector()
    assert ob.name == 'fibre_channel_wwn'
    assert ob._fact_ids == set()

# Generated at 2022-06-13 01:31:08.146096
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible_collections.ansible.community.plugins.module_utils.facts import collector

    fact_collector = FcWwnInitiatorFactCollector()
    fact_collector._module = object
    fact_collector._module.get_bin_path = lambda x: x
    fact_collector._module.run_command = lambda x: ('', '', '')

    facts = collector.device_factory(fact_collector, 'fibre_channel_wwn')
    assert facts == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:31:12.290979
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for constructor of class FcWwnInitiatorFactCollector
    """

    fc_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:01.496965
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts = FcWwnInitiatorFactCollector()
    # check that the instance got initialized correctly
    assert hasattr(facts, 'name')
    assert hasattr(facts, '_fact_ids')
    assert facts.name == 'fibre_channel_wwn'
    assert facts._fact_ids == set()


# Generated at 2022-06-13 01:32:02.709437
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector is not None

# Generated at 2022-06-13 01:32:07.627179
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids is not None

# Generated at 2022-06-13 01:32:09.955866
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'
    assert x._fact_ids == set()

# Generated at 2022-06-13 01:32:18.745627
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModule()
    fc_facts = FcWwnInitiatorFactCollector().collect(module=module)
    assert isinstance(fc_facts, dict)
    assert 'ansible_facts' in fc_facts
    assert 'fibre_channel_wwn' in fc_facts['ansible_facts']
    assert isinstance(fc_facts['ansible_facts']['fibre_channel_wwn'], list)
    assert 2 == len(fc_facts['ansible_facts']['fibre_channel_wwn'])
    for fcwwpn in fc_facts['ansible_facts']['fibre_channel_wwn']:
        assert 16 == len(fcwwpn)
        assert isinstance(fcwwpn, str)

# Generated at 2022-06-13 01:32:23.117308
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    test_dict = { 'fibre_channel_wwn': [] }
    fc_facts = FcWwnInitiatorFactCollector()
    ret = fc_facts.collect()
    assert ret == test_dict

# Generated at 2022-06-13 01:32:24.525803
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc is not None

# Generated at 2022-06-13 01:32:27.295584
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    facts = fc.collect()
    assert facts is not None
    assert 'fibre_channel_wwn' in facts

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:32:29.217680
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fwc = FcWwnInitiatorFactCollector()
    assert fwc.name == 'fibre_channel_wwn'
    assert fwc._fact_ids == set()


# Generated at 2022-06-13 01:32:29.807429
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    assert True

# Generated at 2022-06-13 01:34:08.921805
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Unit test for method collect of class FcWwnInitiatorFactCollector"""
    from ansible.module_utils.facts import ModuleFactsCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    # initialization
    fc_facts = {
                'fibre_channel_wwn': [
                                '21000014ff52a9bb',
                                '200000E08B1C7700'
                            ]
            }
    # test
    fc_collector = FcWwnInitiatorFactCollector()
    fc_results = fc_collector.collect()
    # assert
    assert fc_results == fc_facts

# Generated at 2022-06-13 01:34:18.578968
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector

    c = Collector.collector_class['fibre_channel_wwn']
    assert isinstance(c, FcWwnInitiatorFactCollector)

    if not sys.platform.startswith('linux'):
        assert c.collect() == {'fibre_channel_wwn': []}
    else:
        assert c.collect() == {'fibre_channel_wwn': ['21000014ff52a9bb']}

# Generated at 2022-06-13 01:34:21.283890
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcInitiator = FcWwnInitiatorFactCollector()
    assert fcInitiator.name == 'fibre_channel_wwn'
    assert fcInitiator.collect() == {}

# Generated at 2022-06-13 01:34:30.295144
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import collect_subset

    # create a dummy module
    module = FakeAnsibleModule()

    # generate facts of platform linux
    module.mock_command('/bin/ls /sys/class/fc_host/*/port_name', rc=0, stdout="0x21000014ff52a9bb\n0x21000034ff52a9bb\n")
    module.mock_command('/bin/uname', rc=0, stdout="Linux")
    ansible_collector.module = module
    collected_facts = collect_subset('!all', 'fibre_channel_wwn')

# Generated at 2022-06-13 01:34:33.469591
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []
    test_obj = FcWwnInitiatorFactCollector()
    assert test_obj.name == 'fibre_channel_wwn'
    return test_obj.collect(collected_facts=fc_facts)

# Generated at 2022-06-13 01:34:34.787653
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:38.167810
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn_test_obj = FcWwnInitiatorFactCollector()
    assert fcwwn_test_obj is not None

# Generated at 2022-06-13 01:34:40.470292
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    use the following file to test the collect method
    of class FcWwnInitiatorFactCollector
    unittest_fact_fibre_channel_wwn_factory.py

    """
    pass

# Generated at 2022-06-13 01:34:43.578826
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_subclass = FcWwnInitiatorFactCollector()
    assert fact_subclass.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:45.759975
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    myFactCollector = FcWwnInitiatorFactCollector()
    assert myFactCollector.name == 'fibre_channel_wwn'