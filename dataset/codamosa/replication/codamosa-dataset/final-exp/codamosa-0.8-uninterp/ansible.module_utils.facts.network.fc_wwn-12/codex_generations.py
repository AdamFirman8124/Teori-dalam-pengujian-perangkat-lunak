

# Generated at 2022-06-13 01:27:36.370601
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Create mock execution module
    module = None
    # Create mock execution module class
    class AnsibleModule:
        def get_bin_path(self, arg1, arg2=None):
            cmd = None
            # specific commands to be mocked
            if arg1 == 'ioscan':
                cmd = '/usr/sbin/ioscan'
            if arg1 == 'fcmsutil':
                cmd = '/opt/fcms/bin/fcmsutil'
            return(cmd)

        def run_command(self, cmd):
            rc = 0
            out = ''
            err = ''
            # specific commands to be mocked

# Generated at 2022-06-13 01:27:39.004587
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids is not None

# Generated at 2022-06-13 01:27:41.520128
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector.collect() == {}

# Generated at 2022-06-13 01:27:43.478560
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:47.479784
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fact_collector._fact_ids

# Generated at 2022-06-13 01:27:52.513765
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test to validate object constructor of FcWwnInitiatorFactCollector class
    """
    fci = FcWwnInitiatorFactCollector()

    assert fci.name == 'fibre_channel_wwn'
    assert fci._fact_ids == set()
    assert callable(fci.collect)

# Generated at 2022-06-13 01:27:53.614118
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Just check if class can be instantiated
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:27:59.874768
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Test that the constructor raises a TypeError
    # when no module parameter is provided.
    with pytest.raises(TypeError) as excinfo:
        FcWwnInitiatorFactCollector()
    assert 'missing 2 required positional arguments' in str(excinfo.value)

# Generated at 2022-06-13 01:28:03.332631
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()
    assert fc.collect() == {}


# Generated at 2022-06-13 01:28:14.597880
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Test method collect of class FcWwnInitiatorFactCollector
    """
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors import which, get_module
    from ansible.module_utils.facts.collectors import FcWwnInitiatorFactCollector

    module_name = 'ansible.module_utils.facts.collectors.FcWwnInitiatorFactCollector'
    fc_fact_collector = FcWwnInitiatorFactCollector(module=None, collected_facts=None)

    result = fc_fact_collector.collect()
    assert isinstance(fc_fact_collector, BaseFactCollector)
    assert isinstance(result, dict)

# Generated at 2022-06-13 01:28:28.685592
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:31.416920
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import BaseFactCollector
    fc = FcWwnInitiatorFactCollector()
    assert isinstance(fc, BaseFactCollector)

# Generated at 2022-06-13 01:28:33.050641
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test_fww = FcWwnInitiatorFactCollector()
    assert test_fww.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:38.953634
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    #from ansible.module_utils.facts import ansible_facts

    #from ansible.module_utils.facts.collectors.network import FcWwnInitiatorFactCollector

    #from ansible.module_utils.facts.utils import get_file_lines

    fc_host_port_name_list = [
        '0x50060b00006975ec',
        '0x50060b00006975ed',
        '0x50060b00006975ee',
    ]
    # mock the filesystem
    # fc_host_path = '/sys/class/fc_host'

    # TODO: das alles ist nur ein Test-Gerüst.
    # mock the filesystem
    # fc_host_path = '/sys/class/fc_host'
    # import os
   

# Generated at 2022-06-13 01:28:40.685005
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn = FcWwnInitiatorFactCollector()
    assert fcwwn.name == 'fibre_channel_wwn', 'Test_name_failure'
    assert fcwwn._fact_ids == set(), 'Test_fact_ids_failure'



# Generated at 2022-06-13 01:28:52.698904
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collectors.network import FcWwnInitiatorFactCollector
    fc_wwn_fact_collector = FcWwnInitiatorFactCollector()
    # test on Linux platform
    facts_obj = Facts({'kernel': 'Linux','system': 'Linux','machine': 'x86_64','kernelrelease':'4.4.0-72-generic'})
    initial_facts = dict(facts_obj.get_facts())
    returned_facts = fc_wwn_fact_collector.collect(None, initial_facts)
    # the object returned_facts is of type dict
    assert isinstance(returned_facts, dict)
    # test on Solaris platform

# Generated at 2022-06-13 01:28:58.423055
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModuleMock('fibre_channel_wwn')
    fc_fact_collector = FcWwnInitiatorFactCollector(module)
    result = fc_fact_collector.collect()
    wwn_fact = result['fibre_channel_wwn']

    assert isinstance(wwn_fact, list)

    for wwn in wwn_fact:
        assert isinstance(wwn, str)
        assert len(wwn) == 16
        assert wwn.startswith('50060b')


# Generated at 2022-06-13 01:29:00.899240
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:02.298115
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()


# Generated at 2022-06-13 01:29:07.020986
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import FactCollector

    factCollector = FactCollector()
    assert 'fibre_channel_wwn' in factCollector._collectors


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:29:20.452653
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:30.082219
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    For each platform we should get a fibre_channel_wwn list with at least one wwn
    No matter which platform you are on, you should have a list of at least
    one WWN with you. Depending on machine, you may have multiple WWN's

    """

    import sys

    import platform
    import pytest

    from ansible.module_utils.facts import collector

    fc_facts = { 'fibre_channel_wwn': [] }
    fc = collector.get_collector('fibre_channel_wwn')
    fc_facts.update(fc.collect())

    assert 'fibre_channel_wwn' in fc_facts

    # we should have at least one fibre channel WWN
    #

# Generated at 2022-06-13 01:29:32.986562
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:29:36.116209
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 01:29:41.547777
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Test for constructor of class FcWwnInitiatorFactCollector.
    """
    print("TEST 1: test_FcWwnInitiatorFactCollector()")
    FcWwnInitiatorFactCollector()
    print("END 1")


# Generated at 2022-06-13 01:29:51.129820
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    from ansible.module_utils.facts.collector.fc_wwn_initiator import FcWwnInitiatorFactCollector
    # Create instance of class FcWwnInitiatorFactCollector
    obj = FcWwnInitiatorFactCollector()
    # Create instance of `Facts` class
    facts = Facts(obj=obj)
    # Call created instance's method collect
    # Parameter `obj` is instance of `Facts` class
    obj.collect(facts=facts)
    # Call method `populate` of class `Facts`
    facts.populate()
    # Call method `get` of class `Facts`
    facts_dict = facts.get('ansible_facts', {})
    print(facts_dict)


# Generated at 2022-06-13 01:29:57.439619
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Instantiate the FcWwnInitiatorFactCollector object
    FcWwnInitiatorFactCollector_obj = FcWwnInitiatorFactCollector()

    # Get the facts
    facts_dict = FcWwnInitiatorFactCollector_obj.collect()

    assert facts_dict == {
        'fibre_channel_wwn': ['21000014ff52a9bb'],
    }

# Generated at 2022-06-13 01:29:59.598108
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Test the method `collect` of class FcWwnInitiatorFactCollector
    """
    pass


# Generated at 2022-06-13 01:30:01.953531
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:07.378748
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector
    import module_utils.facts.support as support
    from ansible.module_utils.facts.collector.linux import LinuxFactCollector

    module = support.MockModule()
    collector = FcWwnInitiatorFactCollector(module=module)
    linux_collector = LinuxFactCollector(module=module)

    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []

    fc_facts['fibre_channel_wwn'].append('21000014ff52a9bb')
   

# Generated at 2022-06-13 01:30:31.810020
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'
    assert FcWwnInitiatorFactCollector._fact_ids == set()


# Generated at 2022-06-13 01:30:34.922362
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 01:30:41.636518
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact = FcWwnInitiatorFactCollector()
    assert fact.name == 'fibre_channel_wwn', 'test_FcWwnInitiatorFactCollector failed'
    assert fact._fact_ids == set(), 'test_FcWwnInitiatorFactCollector failed'
    assert type(fact.collect()) is dict, 'test_FcWwnInitiatorFactCollector failed'

# Generated at 2022-06-13 01:30:48.454237
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for constructor of class FcWwnInitiatorFactCollector
    """
    fact_collector = FcWwnInitiatorFactCollector()

    assert "name" in dir(fact_collector)
    assert isinstance(fact_collector.name, property)
    assert fact_collector.name == "fibre_channel_wwn"

    assert "fact_ids" in dir(fact_collector)
    assert isinstance(fact_collector.fact_ids, property)
    assert fact_collector.fact_ids == set()


# Generated at 2022-06-13 01:30:52.642684
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # create FcWwnInitiatorFactCollector object
    obj = FcWwnInitiatorFactCollector()
    # verify that the object is an instance of FcWwnInitiatorFactCollector
    assert isinstance(obj, FcWwnInitiatorFactCollector)

# Generated at 2022-06-13 01:30:55.473340
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    fwwnfc = FcWwnInitiatorFactCollector()
    assert fwwnfc.name == 'fibre_channel_wwn'
    assert fwwnfc._fact_ids == set()


# Generated at 2022-06-13 01:31:00.901749
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = mock.Mock()
    module.get_bin_path = lambda cmd, opt_dirs=[] : cmd
    module.run_command = lambda cmd : (0, '\n 0x21000014ff52a9bb\n', '')
    fc_facts = FcWwnInitiatorFactCollector.collect(module)
    assert fc_facts['fibre_channel_wwn'] == ['21000014ff52a9bb']

# Generated at 2022-06-13 01:31:08.686815
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector import get_collector_instance

    fc_wwn = get_collector_instance(FcWwnInitiatorFactCollector)

    facts = FactsCollector()
    facts.collect(FcWwnInitiatorFactCollector.name, fc_wwn)

    print("WWN: %s" % facts.facts['fibre_channel_wwn'])



# Generated at 2022-06-13 01:31:11.298511
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact = FcWwnInitiatorFactCollector()
    assert fc_fact.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:13.286196
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:38.339230
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:31:42.730990
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert type(fc_facts) == FcWwnInitiatorFactCollector
    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts._fact_ids == set()

# Generated at 2022-06-13 01:31:53.879913
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import os
    import sys
    import platform
    import tempfile
    module = sys.modules['__main__']
    module.run_command = lambda *a, **kw: (0, '', '')

    # define test cases
    solaris_sparc_10 = {
        'platform' : 'sunos',
        'platform_version' : '5.10',
        'architecture' : 'sparc'
    }
    solaris_x86_11 = {
        'platform' : 'sunos',
        'platform_version' : '5.11',
        'architecture' : 'i86pc'
    }

# Generated at 2022-06-13 01:31:56.266400
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Test that constructor of FcWwnInitiatorFactCollector works
    """
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == "fibre_channel_wwn"
    assert fact_collector._fact_ids is not None

# Generated at 2022-06-13 01:32:07.449994
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    fc_facts = FcWwnInitiatorFactCollector().collect()
    # check results
    if sys.platform.startswith('linux'):
        assert fc_facts['fibre_channel_wwn'] == [u'21000014ff52a9bb']
    elif sys.platform.startswith('sunos'):
        assert fc_facts['fibre_channel_wwn'] == [u'10000090fa1658de']
    elif sys.platform.startswith('aix'):
        assert fc_facts['fibre_channel_wwn'] == [u'10000090FA551509']

# Generated at 2022-06-13 01:32:13.677572
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    m = __import__('module_utils.facts.fibre_channel_wwn.fibre_channel_wwn')
    m.ANSIBLE_METADATA = {}
    m.ANSIBLE_METADATA['status'] = 'preview'
    m.ANSIBLE_METADATA['metadata_version'] = '1.1'
    fc = FcWwnInitiatorFactCollector(m)
    assert isinstance(fc, FcWwnInitiatorFactCollector)

# Generated at 2022-06-13 01:32:15.354528
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:17.967919
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == "fibre_channel_wwn"
    assert obj._fact_ids == set(['fibre_channel_wwn'])


# Generated at 2022-06-13 01:32:19.651608
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnInitiatorFactCollector().collect()

# Generated at 2022-06-13 01:32:22.603290
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    print('--- test_FcWwnInitiatorFactCollector_collect() ---')
    # TODO: fill test
    pass


# Generated at 2022-06-13 01:32:49.876113
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids == set()

# Generated at 2022-06-13 01:32:59.487889
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = MockAnsibleModule()
    if sys.platform.startswith('linux'):
        module.run_command = Mock(return_value=(0, '', ''))  # return an empty list
    if sys.platform.startswith('sunos'):
        module.run_command = Mock(return_value=(0, 'HBA Port WWN: 10000090fa1658de', ''))
    if sys.platform.startswith('aix'):
        module.run_command = Mock(return_value=(0, "fscsi0 Available 09-08-04-3,0                    FC Adapter    fcs0 Available  09-08-04-3,0                    FC Adapter", ''))

# Generated at 2022-06-13 01:33:01.101591
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 01:33:06.742525
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Constructor of class FcWwnInitiatorFactCollector
    """
    fcwwn_fc = FcWwnInitiatorFactCollector()
    assert fcwwn_fc.name == 'fibre_channel_wwn'
    assert fcwwn_fc._fact_ids == set()

# Generated at 2022-06-13 01:33:15.065663
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    testing_facts_dict = {
        'ansible_facts': {
           'fibre_channel_wwn': [
                '21000014ff52a9bb',
                '21000014ff52a9bc',
            ]
        }
    }
    testing_facts_dict_empty = {
        'ansible_facts': {
           'fibre_channel_wwn': [],
        }
    }
    if sys.platform.startswith('linux'):
        my_test_fc = FcWwnInitiatorFactCollector()
        my_test_fc_fact_dict = my_test_fc.collect()
        assert my_test_fc_fact_dict == testing_facts_dict
    elif sys.platform.startswith('sunos'):
        # TBD
        my_test

# Generated at 2022-06-13 01:33:18.246564
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact = FcWwnInitiatorFactCollector()
    assert fc_fact.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fc_fact._fact_ids

# Generated at 2022-06-13 01:33:22.384917
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:33:33.986010
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fcinfo_out = """
HBA Port WWN: 10000090fa1658de
HBA Driver Name: lpfc
HBA Driver Version: 10.0.42.0
HBA Driver Alpha: No
HBA Driver Beta: No
HBA Driver Gamma: No
Driver Name: lpfc
Driver Version: 10.0.42.0
Driver Description: LPFC - Link Problem Fast Crash
Node WWN: 20000000c957d970
Link Status: Up
Link Speed: 8.0Gb/sec
Supported Speed: Unknown-Speed
Current Frame Size: 2148
Max Frame Size: 2148
OS Device Name: /dev/cfg/c3
"""
    lsdev_out = """
fcs2    Available   03-08-08  N/A
fcs3    Available   03-08-08  N/A
"""


# Generated at 2022-06-13 01:33:42.230051
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # test function collect of class FcWwnInitiatorFactCollector
    facts = FcWwnInitiatorFactCollector().collect()
    assert isinstance(facts, dict)
    assert set(facts.keys()) == {'ansible_facts', 'fibre_channel_wwn'}
    assert len(facts['fibre_channel_wwn']) >= 0
    # test whether the list has only WWN id entries
    if len(facts['fibre_channel_wwn']) >= 1:
        for WWN_id in facts['fibre_channel_wwn']:
            assert isinstance(WWN_id, str)
            # WWN id has 16 hexadecimal digits
            assert len(WWN_id) == 16
            # WWN id contains only hexadecimal digits
            id_

# Generated at 2022-06-13 01:33:48.142572
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector import get_collector_instance
    facts = Collector()
    table_fact_collector = get_collector_instance(FcWwnInitiatorFactCollector,
                                                  facts.collector)
    assert table_fact_collector is not None
    fc_facts = table_fact_collector.collect()
    assert isinstance(fc_facts, dict)

# Generated at 2022-06-13 01:34:38.488282
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert isinstance(FcWwnInitiatorFactCollector(), FcWwnInitiatorFactCollector)

# Generated at 2022-06-13 01:34:40.728828
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFC = FcWwnInitiatorFactCollector()
    assert FcWwnInitiatorFC is not None


# Generated at 2022-06-13 01:34:51.125829
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Create a stub module object.  The method collect
    is tested with this dummy module object.

    Module stub is a class that has static fields
    and methods and can be used as a dummy object.

    @see https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
    @see ansible/test/units/module_utils/test_facts.py
    """
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts.collector import BaseFactCollector
    module = ModuleStub()
    test_collector = BaseFactCollector.get_collector('fibre_channel_wwn')
    fc_facts = test_collector.collect(module)
    # test on aix

# Generated at 2022-06-13 01:35:01.426407
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test method collect of class FcWwnInitiatorFactCollector
    """
    from ansible.module_utils.facts import collector

    # Set facts for FcWwnInitiatorFactCollector
    facts_collected = {'fibre_channel_wwn': [u'50060b00006975ec', u'50060a00006975ed']}

    # Get instance of FcWwnInitiatorFactCollector
    fact_collector = FcWwnInitiatorFactCollector()

    # Assert FcWwnInitiatorFactCollector is instance of BaseFactCollector
    assert isinstance(fact_collector, BaseFactCollector)
    # Assert FcWwnInitiatorFactCollector name equals 'fibre_channel_wwn'

# Generated at 2022-06-13 01:35:08.958621
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import platform
    import unittest
    FcWwnInitiatorFactCollector._initialize_platform()
    fc_wwn_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_wwn_fact_collector.name == 'fibre_channel_wwn'
    assert fc_wwn_fact_collector.linux_platform == 'Linux'
    assert fc_wwn_fact_collector.linux_distribution == 'OpenWrt'
    if platform.system() != 'Linux':
        assert fc_wwn_fact_collector.linux_distribution == platform.linux_distribution()[0]
    else:
        assert fc_wwn_fact_collector.linux_distribution == platform.linux_distribution()[0]

    # test

# Generated at 2022-06-13 01:35:09.832374
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:35:17.650615
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModule(
        argument_spec = dict()
    )

    #
    # create a class instance with a faked ansible module
    #
    fcwwn_fact_collector = FcWwnInitiatorFactCollector(module)

    #
    # test collect method
    #
    fcwwn_faked_fact = {}
    if sys.platform.startswith('linux'):
        fcwwn_faked_fact['fibre_channel_wwn'] = ["21000014ff52a9bb"]
    elif sys.platform.startswith('sunos'):
        fcwwn_faked_fact['fibre_channel_wwn'] = ["10000090fa1658de"]
    elif sys.platform.startswith('aix'):
        f

# Generated at 2022-06-13 01:35:20.862919
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_wwn_fact_collector.name == 'fibre_channel_wwn'
    assert fc_wwn_fact_collector._fact_ids == set()

# Generated at 2022-06-13 01:35:24.067916
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'
    assert x.collect() != None

# Generated at 2022-06-13 01:35:31.723883
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import FactCache
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.network.fc_wwn import FcWwnInitiatorFactCollector
    import ansible.module_utils.facts.collectors.base
    import sys
    import os
    import glob
    module = ansible.module_utils.facts.collectors.base.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    os.system('rm -Rf /tmp/ansible_test_facts_dir')