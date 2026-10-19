

# Generated at 2022-06-13 01:27:32.187637
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector().name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:33.896820
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert(fact_collector.name == 'fibre_channel_wwn')
    assert(fact_collector._fact_ids == set())

# Generated at 2022-06-13 01:27:36.673003
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fwi = FcWwnInitiatorFactCollector()
    assert fwi.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:39.210650
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()

    # Test name
    name = 'fibre_channel_wwn'

    assert name == fact_collector.name

# Generated at 2022-06-13 01:27:41.369124
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:27:43.313692
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:54.259536
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
  """
  Test method to test collection of facts
  """
  from ansible.module_utils.facts.collector import BaseFactCollector
  from ansible.module_utils.facts import collector

  class MockModule(object):
    def __init__(self):
      self.fail_json = BaseFactCollector.fail_json
      self.exit_json = BaseFactCollector.exit_json
      self.get_bin_path = BaseFactCollector.get_bin_path

  TestModule = MockModule()
  TestModule.run_command = BaseFactCollector.run_command
  TestModule.get_bin_path = BaseFactCollector.get_bin_path
  TestModule.collector = collector.get_collector_instance(TestModule)
  TestModule.collector.collect(TestModule, {})

# Generated at 2022-06-13 01:28:01.025934
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert (obj.name == 'fibre_channel_wwn')
    assert (obj.platforms == ['Linux', 'SunOS', 'AIX', 'HPUX'])


# Generated at 2022-06-13 01:28:12.433246
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.fibre_channel_wwn import FcWwnInitiatorFactCollector
    import sys
    if sys.version_info >= (3, 0):
        from unittest.mock import MagicMock, patch
        from io import StringIO
    else:
        from mock import MagicMock, patch
        from StringIO import StringIO

    # collect should return a dict of facts
    my_object = FcWwnInitiatorFactCollector()
    assert isinstance(my_object.collect(), dict)

    # mocked results for RedHat
    my_object = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:28:14.330094
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import collector

    test = FcWwnInitiatorFactCollector()
    test.collect()

    assert collector.collector.collected_facts['fibre_channel_wwn']



# Generated at 2022-06-13 01:28:38.473199
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:28:42.668123
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fw = FcWwnInitiatorFactCollector()
    assert 'fibre_channel_wwn' in fw.name
    assert 'fibre_channel_wwn' in fw._fact_ids

# Generated at 2022-06-13 01:28:43.916509
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:48.678524
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.collector.fc_wwn_initiator import FcWwnInitiatorFactCollector

    FcWwnInitiatorFactCollector.collect()
#    assertResult

# Generated at 2022-06-13 01:28:57.911667
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.facts import Facts
    fc_facts_collector = FcWwnInitiatorFactCollector()
    facts_collector = FactsCollector()
    facts_collector.add_collector(fc_facts_collector)
    collected_facts = Facts(facts_collector, {})
    # invoke collect method of FcWwnInitiatorFactCollector
    fc_facts_collector.collect(collected_facts=collected_facts)
    fc_facts = collected_facts.get('fibre_channel_wwn')
    if fc_facts:
        print("fc_facts: %s" % fc_facts)

if __name__ == '__main__':
    test

# Generated at 2022-06-13 01:29:01.051586
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'
    assert c._fact_ids == set()



# Generated at 2022-06-13 01:29:09.677959
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    from ansible.module_utils.facts.collectors.network import FcWwnInitiatorFactCollector

    test_collector = FcWwnInitiatorFactCollector()
    test_facts = test_collector.collect()
    assert isinstance(test_facts, dict), 'test_facts is not dict'
    assert 'fibre_channel_wwn' in test_facts, 'test_facts[fibre_channel_wwn] is not present'
    assert isinstance(test_facts['fibre_channel_wwn'], list), 'test_facts[fibre_channel_wwn] is not list'

# Generated at 2022-06-13 01:29:13.387515
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in x.collect()

# Generated at 2022-06-13 01:29:19.239020
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # create an instance of the class
    instance = FcWwnInitiatorFactCollector()
    assert isinstance(instance,FcWwnInitiatorFactCollector)
    # verify name
    assert instance.name == 'fibre_channel_wwn'
    # verify that there are no fact_ids (set is empty)
    assert instance._fact_ids == set()

# Generated at 2022-06-13 01:29:27.360520
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModule(argument_spec={})
    base = BaseFactCollector()

    if base.can_collect:
        collector = FcWwnInitiatorFactCollector(module=module)
        result = collector.collect(module=module)

        assert isinstance(result, dict)
        assert len(list(result.keys())) == 1
        assert 'fibre_channel_wwn' in result
        for value in result.values():
            assert isinstance(value, list)
            for item in value:
                assert isinstance(item, str)
                assert len(item) == 16

# Generated at 2022-06-13 01:30:16.324132
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    result = dict(ansible_facts=dict(fibre_channel_wwn=[u'21000014ff52a9bb']))
    FcWwnInitiatorFactCollector().collect() == result

# Generated at 2022-06-13 01:30:19.152240
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'



# Generated at 2022-06-13 01:30:27.244503
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class MockModule(object):

        def __init__(self):
            self.params = {'gather_subset': ['all']}
        def get_bin_path(self, cmd):
            return cmd

    class MockAnsibleModule(object):
        @staticmethod
        def run_command(cmd):
            # emulate no fcinfo installed
            if cmd.startswith('fcinfo'):
                return 127, "", "error"
            # emulate linux
            if cmd.startswith('ls /sys/class/fc_host'):
                return 0, "0x21000014ff52a9bb", ""
            # emulate solaris 11
            if cmd.startswith('lsdev -Cc adapter -l fcs*'):
                return 0, "fcs2 Available 04-10-1,00", ""

# Generated at 2022-06-13 01:30:31.139341
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'
    assert isinstance(f._fact_ids, set)
    assert f.collect() == {}

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:33.902078
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
   x = FcWwnInitiatorFactCollector()
   print(x.name)
   print(x._fact_ids)

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:39.001586
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    '''
    Unit test of constructor of class FcWwnInitiatorFactCollector
    '''
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 01:30:46.106865
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    module = mock.MagicMock()
    module.run_command.return_value = (0, '0x21000014ff52a9bb', '')

    #check if facts are collected correctly
    fw = FcWwnInitiatorFactCollector()
    facts = fw.collect(module)
    assert facts['ansible_facts']['fibre_channel_wwn'] == ['21000014ff52a9bb']

# vim: set expandtab ts=4 sw=4:

# Generated at 2022-06-13 01:30:51.933093
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector()
    print("fc_facts['fibre_channel_wwn']: %s" % fc_facts['fibre_channel_wwn'])

if __name__ == "__main__":
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:30:54.452503
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector('FcWwnInitiator')
    assert collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:00.104908
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    class MockModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, command):
            return 0, command, None

        def get_bin_path(self, command, opt_dirs=[]):
            return command

    mock_module = MockModule()
    fc_wwn_facts = FcWwnInitiatorFactCollector()
    fc_wwn_facts.collect(module=mock_module)

# Generated at 2022-06-13 01:31:56.897838
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector

    fake_module = MockAnsibleModule()
    fake_module.params = {'gather_subset': ['all']}
    fake_module.exit_json = Mock()
    fake_module.run_command = Mock(return_value=(0, '', ''))

    # Mock `Collector` methods not needed to process the class under test
    Collector._get_subset = Mock(return_value=['all'])
    Collector.validate_subset = Mock(return_value=['all'])


# Generated at 2022-06-13 01:32:08.627355
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = ModuleStub()
    fact_collector = FcWwnInitiatorFactCollector(module=module, discovered_facts={})
    if sys.platform.startswith('linux'):
        expected = {'fibre_channel_wwn': [u'21000014ff52a9bb']}
    elif sys.platform.startswith('sunos'):
        expected = {'fibre_channel_wwn': [u'10000090fa1658de']}
    elif sys.platform.startswith('aix'):
        expected = {'fibre_channel_wwn': [u'21000014ff52a9bb']}

# Generated at 2022-06-13 01:32:10.614392
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Unit test method FcWwnInitiatorFactCollector.collect

# Generated at 2022-06-13 01:32:19.079869
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    if sys.platform.startswith('linux'):
        """
        RedHatEnterpriseServer release 7.2 (Maipo)
        RedHatEnterpriseServer release 7.3 (Maipo)
        RedHatEnterpriseServer release 7.4 (Maipo)
        RedHatEnterpriseServer release 7.5 (Maipo)
        RedHatEnterpriseServer release 7.6 (Maipo)
        RedHatEnterpriseLinuxServer release 7.7 (Maipo)
        CentOS Linux release 7.4.1708 (Core)
        CentOS Linux release 7.5.1804 (Core)
        CentOS Linux release 7.6.1810 (Core)
        CentOS Linux release 7.7.1908 (Core)
        """
        class FakeModule(object):
            def __init__(self, out):
                self.out = out


# Generated at 2022-06-13 01:32:22.223546
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc = FcWwnInitiatorFactCollector()
    assert fc.collect() == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:32:24.562889
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """unit tests for method FcWwnInitiatorFactCollector.collect"""
    fake_module = {}
    fake_module.run_command = lambda x: (0, "", "")
    fake_module.get_bin_path = lambda x: ""
    facts_collector = FcWwnInitiatorFactCollector()
    assert facts_collector.collect(fake_module) == {"fibre_channel_wwn": []}

# Generated at 2022-06-13 01:32:26.712411
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    col = FcWwnInitiatorFactCollector()
    assert col.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:32.707831
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import collector_class_map
    try:
        collector = collector_class_map['fibre_channel_wwn']()
    except KeyError:
        pytest.fail("Can not load collector fibre_channel_wwn from collector_class_map")

    assert collector is not None
    assert collector.name == 'fibre_channel_wwn'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 01:32:34.887038
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:39.052325
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class Module(object):
        @staticmethod
        def get_bin_path(name, opt_dirs=[]):
            return None

        @staticmethod
        def run_command(name):
            return 0, '', ''

    fact = FcWwnInitiatorFactCollector()
    assert fact.collect() == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:34:11.410077
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == "fibre_channel_wwn"

# Generated at 2022-06-13 01:34:13.816521
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:23.332594
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    from ansible.module_utils.facts.utils import AnsibleModule
    from ansible.module_utils.facts.collectors import collector_module
    import ansible.module_utils.facts.collectors.network as network

    # This example show contents of file:
    # [root@cpe-test1 ~]# cat /sys/class/fc_host/host1/port_name
    # 0x21000014ff52a9bb

    fact_data = {
        '/sys/class/fc_host/host1/port_name':
        """0x21000014ff52a9bb""",
    }

    def _exec_command(cmd, check_rc=False, data=None):
        return 0, fact_data.get(cmd), ''


# Generated at 2022-06-13 01:34:30.254976
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector().collect()
    assert fc_facts['fibre_channel_wwn'] is not None
    assert len(fc_facts['fibre_channel_wwn']) > 0
    # check if wwns are long enough
    for wwn in fc_facts['fibre_channel_wwn']:
        assert len(wwn) == 16

# Run module as a standalone fact
if __name__ == '__main__':
    print(json.dumps(FcWwnInitiatorFactCollector().collect(), indent=2))

# Generated at 2022-06-13 01:34:41.437486
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import os
    import sys
    import json
    import unittest

    class TestFcWwnInitiatorFactCollector(unittest.TestCase):
        # test case: tests if /sys/class/fc_host/*/port_name files exist on Linux
        def test_linux_fc_file(self):
            if sys.platform.startswith('linux'):
                fc_facts = FcWwnInitiatorFactCollector().collect()
                fc_wwns = []
                for fcfile in glob.glob('/sys/class/fc_host/*/port_name'):
                    for line in get_file_lines(fcfile):
                        fc_wwns.append(line.rstrip()[2:])

# Generated at 2022-06-13 01:34:51.419389
# Unit test for method collect of class FcWwnInitiatorFactCollector

# Generated at 2022-06-13 01:34:53.837306
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fc = FcWwnInitiatorFactCollector()
    assert fc_fc.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fc_fc.collect()

# Generated at 2022-06-13 01:34:58.525935
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    colFcWwn = FcWwnInitiatorFactCollector()
    assert colFcWwn.name == 'fibre_channel_wwn'


if __name__ == "__main__":
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:35:02.979039
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()
    assert 'fibre_channel_wwn' in fact_collector._legacy_fact_names


# Generated at 2022-06-13 01:35:09.986960
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collectors import get_collector_facts
    from ansible.module_utils.facts.utils import AnsibleFactCollector
    from ansible.module_utils.facts.utils import execute_module
