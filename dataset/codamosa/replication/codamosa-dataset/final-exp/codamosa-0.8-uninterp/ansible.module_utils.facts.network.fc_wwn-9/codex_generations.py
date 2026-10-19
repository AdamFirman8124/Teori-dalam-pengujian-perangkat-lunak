

# Generated at 2022-06-13 01:27:32.613560
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Test FcWwnInitiatorFactCollector.collect
    """

    from ansible.module_utils.facts import ansible_collector

    fc = FcWwnInitiatorFactCollector()
    facts_dict = fc.collect(ansible_collector, None)
    assert facts_dict is not None
    fc_wwn_list = facts_dict.get("fibre_channel_wwn", None)
    assert fc_wwn_list is not None
    assert isinstance(fc_wwn_list, list)

# Generated at 2022-06-13 01:27:36.625289
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector()
    result = fc_facts.collect()
    assert result == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:27:38.759084
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:27:47.122858
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class Module(object):
        def __init__(self, platform):
            self.platform = platform

        def get_bin_path(self, *args, **kwargs):
            if self.platform.startswith('linux'):
                return "/usr/bin/which"
            elif self.platform.startswith('sunos'):
                return "/usr/sbin/which"
            elif self.platform.startswith('aix'):
                return "/usr/bin/which"
            elif self.platform.startswith('hp-ux'):
                return "/usr/bin/which"


# Generated at 2022-06-13 01:27:49.565822
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for class FcWwnInitiatorFactCollector

    """
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 01:27:50.872159
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:58.819666
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module_mock = type('module_mock', (), dict())()
    collected_facts = dict()
    fci = FcWwnInitiatorFactCollector()

    # Test with expected facts
    fc_facts = {'fibre_channel_wwn': ['10000090fa1658de']}
    module_mock.run_command = lambda x: (0, 'HBA Port WWN: 10000090fa1658de', '')
    module_mock.get_bin_path = lambda x: '/usr/sbin/' + x
    fci.collect(module_mock, collected_facts)
    assert collected_facts == fc_facts

    # Test with missing fact, expect empty fact
    fc_facts = {'fibre_channel_wwn': []}
    module_mock

# Generated at 2022-06-13 01:28:06.702553
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in fc_facts._fact_ids
    assert fc_facts.collector_type == 'fibre_channel_wwn_initiator'
    # return module and collected_facts
    mod, coll_fmts = fc_facts.collect()
    assert mod.run_command
    assert coll_fmts
    assert coll_fmts['fibre_channel_wwn']


# Generated at 2022-06-13 01:28:08.422735
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()


# Generated at 2022-06-13 01:28:18.886191
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fcwwn_initiator_fact_collector = FcWwnInitiatorFactCollector()
    ansible_module = DummyAnsibleModule()
    ansible_module.run_command = MagicMock(return_value=(123, '', ''))
    ansible_module.get_bin_path = MagicMock(return_value=True)
    ansible_module.command_warnings = []
    res = fcwwn_initiator_fact_collector.collect(ansible_module)
    assert 'fibre_channel_wwn' in res
    assert type(res['fibre_channel_wwn']) == list
    assert len(res['fibre_channel_wwn']) == 0
    assert ansible_module.run_command.call_count == 2

# Generated at 2022-06-13 01:28:35.252515
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # create a class instance
    FcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector(None, None)
    # initialize fc_facts
    fc_facts = {}
    """
    # test for linux system
    # on windows (i use cygwin) WWNs are not available
    # platform.system() returns 'Windows', so this case will be skipped
    """
    if sys.platform.startswith('linux'):
        fc_facts['fibre_channel_wwn'] = []
        # set fake data
        fc_facts['fibre_channel_wwn'].append('0x21000014ff52a9bb')
        fc_facts['fibre_channel_wwn'].append('0x21000014ff52a9cc')
        # get

# Generated at 2022-06-13 01:28:47.434019
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.facts import Facts

    ffc = FcWwnInitiatorFactCollector()
    facts_dict = Facts()
    facts_dict.add(ffc.collect)
    # unit test check
    if sys.platform.startswith('linux'):
        assert facts_dict['fibre_channel_wwn'][0] == '21000014ff52a9bb'
    elif sys.platform.startswith('sunos'):
        assert facts_dict['fibre_channel_wwn'][0] == '21000014ff52a9bb'

# Generated at 2022-06-13 01:28:52.351789
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_col = FcWwnInitiatorFactCollector()
    assert fc_fact_col.name == "fibre_channel_wwn"
    assert 'fibre_channel_wwn' in fc_fact_col.collect()

# unit test

# Generated at 2022-06-13 01:29:04.126133
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockModule(object):
        """
        Mock module for unit tests
        """
        def __init__(self):
            pass

        @staticmethod
        def run_command(cmd, *args, **kwargs):
            """
            Fake run_command
            """
            if cmd.startswith('fcinfo hba-port'):
                if sys.version_info[0] >= 3:
                    return 0, "HBA Port WWN: 10000090fa1658de".encode('utf-8'), ""
                else:
                    return 0, "HBA Port WWN: 10000090fa1658de", ""


# Generated at 2022-06-13 01:29:15.109187
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class TestModule:
        def run_command(self,cmd):
            print(cmd)
            if "aix" in cmd1 or "hp" in cmd1:
                class TestOutput:
                    stdout = '''lscfg -vpl fcs3 | grep "Network Address"
                            Network Address.............10000090FA551509
                        '''
                output = TestOutput()
            elif "linux" in cmd:
                class TestOutput:
                    stdout = '''/sys/class/fc_host/host0/port_name
                        0x21000014ff52a9bb
                        '''
                output = TestOutput()
            elif "fcinfo hba-port" in cmd:
                class TestOutput:
                    stdout = '''HBA Port WWN: 10000090fa1658de'''
                output

# Generated at 2022-06-13 01:29:19.562808
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModuleStub()
    # without parameter facts
    fc_collector = FcWwnInitiatorFactCollector()
    assert len(fc_collector.collect(module).keys()) == 1
    assert 'fibre_channel_wwn' in fc_collector.collect(module).keys()

# Generated at 2022-06-13 01:29:28.267593
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import Collector
    DEVNULL = open(os.devnull, 'w')
    module = FakeModule(DEFAULT_FCINFO = ['10000090fa1658de'])
    collector = FcWwnInitiatorFactCollector(module=module)
    collected_fibre_channel_wwn_facts = collector.collect()
    print(collected_fibre_channel_wwn_facts)
    assert collected_fibre_channel_wwn_facts['fibre_channel_wwn'] == ['10000090fa1658de']

# Generated at 2022-06-13 01:29:30.710666
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:36.436988
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    ftc = get_collector_instance('Fibre_channel_wwn')
    assert ftc is not None, 'Fibre_channel_wwn FactCollector instance not initialized'
    assert hasattr(ftc, 'collect'), 'Fibre_channel_wwn FactCollector has no collect method'

# Generated at 2022-06-13 01:29:44.514659
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fact_collector = FcWwnInitiatorFactCollector()
    facts = fact_collector.collect(collected_facts={})
    # at least one wwn should be found
    assert 'fibre_channel_wwn' in facts, \
        'fcwwn fact does not exist in facts'


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:30:11.305498
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn_obj = FcWwnInitiatorFactCollector()
    assert fcwwn_obj.name == "fibre_channel_wwn", "fcwwn_obj.name should be 'fibre_channel_wwn', but is: " + str(fcwwn_obj.name)


# Generated at 2022-06-13 01:30:13.390732
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:21.835745
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import Collector

    fc = FcWwnInitiatorFactCollector()
    collected_facts = Collector()
    test_facts = {
            'fibre_channel_wwn': ['2102000090fa1658de', '2102000090fa1658df']
    }
    fc.collect(collected_facts=collected_facts)
    print(collected_facts.get_facts())
    assert collected_facts.get_facts() == test_facts

# if __name__ == "__main__":
#     test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:30:28.946936
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import ansible.module_utils.facts.collectors.network.fibre_channel_wwn
    import ansible.module_utils.facts.collectors.network.fibre_channel_wwn as fibre_channel_wwn
    from ansible.module_utils.facts.collectors.network.fibre_channel_wwn import FcWwnInitiatorFactCollector
    import sys

    # test returns list of length 0
    test_object = FcWwnInitiatorFactCollector()
    collected_facts = {}
    module = ansible.module_utils.facts.collectors.network.fibre_channel_wwn.AnsibleModuleMock()
    result = test_object.collect(module=module, collected_facts=collected_facts)

# Generated at 2022-06-13 01:30:31.932738
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector().collect()
    assert 'fibre_channel_wwn' in fc_facts
    assert isinstance(fc_facts['fibre_channel_wwn'], list)



# Generated at 2022-06-13 01:30:34.309278
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 01:30:37.231453
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 01:30:41.129026
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_collector = FcWwnInitiatorFactCollector()
    print(fc_fact_collector.collect())

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:49.820874
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collectors
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils._text import to_bytes

    class MockModule():
        def __init__(self):
            self.params = {}

        def get_bin_path(self, arg, opt_dirs=[]):
            return "/usr/bin/" + arg

        def run_command(self, cmd):
            return 0, to_bytes(get_file_lines(cmd)), ''

    collectors = Collectors()
    collector = FcWwnInitiatorFactCollector(MockModule(), {}, collectors)

    print(collector.collect())

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:30:56.938924
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector

    # create instance of collector and add FcWwnInitiatorFactCollector
    test_instance = Collector()
    test_instance.collectors.append(FcWwnInitiatorFactCollector())

    # create facts dictionary
    facts = {}

    # run collect method of FcWwnInitiatorFactCollector
    test_instance.collect(module=None, collected_facts=facts)
    print(facts)



# Generated at 2022-06-13 01:31:43.793639
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:31:54.575319
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Test with empty sys.platform
    sys.platform = ''
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids == {'ansible_fibre_channel_wwn'}
    # Test with linux in sys.platform
    sys.platform = 'linux'
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids == {'ansible_fibre_channel_wwn'}
    # Test with sunos in sys.platform
    sys.platform = 'sunos'

# Generated at 2022-06-13 01:31:59.139430
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """test_FcWwnInitiatorFactCollector_collect"""
    pass


# Generated at 2022-06-13 01:32:08.778716
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleCollector
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils._text import to_bytes

    a = AnsibleCollector(None, '')
    fc = FcWwnInitiatorFactCollector(a, None)

    # we need to register our collector in order to be able to use it
    a._FACTS_CACHE['fibre_channel_wwn'] = fc

    # before writing a file, we check whether it exists or not
    cmd = a.module.get_bin_path('rm')
    a.module.run_command(cmd + " -f /tmp/port_name")

    # we write a file as if it were a fibre channel wwn file
    to

# Generated at 2022-06-13 01:32:13.224328
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.network.fibre_channel_wwn import FcWwnInitiatorFactCollector

    assert isinstance(Collector.fact_collectors[-1], FcWwnInitiatorFactCollector)

# Generated at 2022-06-13 01:32:16.065313
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fact_collector_object = FcWwnInitiatorFactCollector()
    result = fact_collector_object.collect()
    fact = 'fibre_channel_wwn'
    assert fact in dict(result), 'expected %s in results' % fact

# Generated at 2022-06-13 01:32:18.518239
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for constructor of class FcWwnInitiatorFactCollector
    """
    fc = FcWwnInitiatorFactCollector()
    assert fc is not None

# Generated at 2022-06-13 01:32:20.919458
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector
    assert fact_collector.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:32:23.184997
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    a = FcWwnInitiatorFactCollector(None)
    assert a.name == 'fibre_channel_wwn'
    assert a._fact_ids == set()



# Generated at 2022-06-13 01:32:25.119434
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    result = FcWwnInitiatorFactCollector()
    assert result is not None

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 01:33:51.815158
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    result = {}
    result['fibre_channel_wwn'] = []
    result['fibre_channel_wwn'].append('20000090fa1658de')
    collector = FcWwnInitiatorFactCollector()
    facts_dict = collector.collect()
    assert facts_dict == result

# Generated at 2022-06-13 01:33:58.679276
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import os
    import tempfile
    import shutil
    import platform

    (fd, path) = tempfile.mkstemp(prefix='ansible_test')
    with open(path, 'w') as fd:
        fd.write("0x50060b00006975ec")
    collector = FcWwnInitiatorFactCollector()
    collected_facts = {}

# Generated at 2022-06-13 01:34:01.372403
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_wwn_initiator_collector = FcWwnInitiatorFactCollector()
    assert 'fibre_channel_wwn' in fc_wwn_initiator_collector.collect()

# Generated at 2022-06-13 01:34:05.201718
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    '''
    Test method collect of class FcWwnInitiatorFactCollector with the Linux platform.
    The test checks the results for a device with known id.
    '''
    fc_facts = {}
    fact_collector = FcWwnInitiatorFactCollector()
    fc_facts['fibre_channel_wwn'] = fact_collector.collect(collected_facts=fc_facts)
    assert len(fc_facts['fibre_channel_wwn']) > 0
    assert fc_facts['fibre_channel_wwn'][0] == '000014ff52a9bb'

# Generated at 2022-06-13 01:34:07.364808
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts_collector = FcWwnInitiatorFactCollector()
    assert fc_facts_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:10.281201
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts=FcWwnInitiatorFactCollector()
    assert facts.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:14.185008
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts._fact_ids == set()


# Generated at 2022-06-13 01:34:15.180501
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:34:23.955918
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    import os
    import glob
    import types
    import subprocess
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import FcWwnInitiatorFactCollector

    mysys = sys.platform
    mypath = os.path.dirname(__file__)
    mypath = mypath + "/"
    os.chdir(mypath)
    print("--")
    print("mypath: " + mypath)
    myfiles = glob.glob('test/test_FcWwnInitiatorFactCollector*')
    print("myfiles: " + str(myfiles))
    print("--")

    if 'solaris' in mysys:
        sys.platform = 'sunos10'

# Generated at 2022-06-13 01:34:27.193290
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts.fact_ids == ['fibre_channel_wwn']