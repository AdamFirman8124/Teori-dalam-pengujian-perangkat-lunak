

# Generated at 2022-06-13 01:27:43.226991
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    # mock class object FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.collector import Collector
    class mock_FcWwnInitiatorFactCollector(FcWwnInitiatorFactCollector, Collector):
        def __init__(self):
            Collector.__init__(self)
        def collect(self):
            pass

    # mock class object BaseFactCollector

# Generated at 2022-06-13 01:27:54.174810
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    import unittest
    import sys
    import platform

    class TestFcWwnInitiatorFactCollector(unittest.TestCase):

        def setUp(self):
            self.collector = FcWwnInitiatorFactCollector()

        def test_name_returns_wwwn(self):
            self.assertEqual(self.collector.name, 'fibre_channel_wwn')

        def test_platform_is_linux(self):
            sys.platform = 'linux'
            self.assertEqual(self.collector.collect()['fibre_channel_wwn'], [])

        def test_platform_is_linux_with_facts(self):
            sys.platform = 'linux'

# Generated at 2022-06-13 01:27:59.678591
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector.
    """
    class MockModule(object):
        """
        Mock class for Ansible module.
        """
        def __init__(self):
            self.params = {}

        def run_command(self, command):
            if 'aix' in command:
                out = '''
ent0 Defined
ent1 Available
ent2 Defined
ent3 Defined
ent4 Available
ent5 Defined
ent6 Available
ent7 Available
'''
                return 0, out, ''

# Generated at 2022-06-13 01:28:01.010160
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcw = FcWwnInitiatorFactCollector()
    assert fcw.name == "fibre_channel_wwn"
    assert fcw._fact_ids == set()



# Generated at 2022-06-13 01:28:05.738002
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj1 = FcWwnInitiatorFactCollector()
    with open('/tmp/FcWwnInitiatorFactCollector.facts', 'w') as fh:
        fh.write(str(obj1.collect()))

if __name__ == "__main__":
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:28:09.622089
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Test case for collect method of FcWwnInitiatorFactCollector
    """
    fc_facts = FcWwnInitiatorFactCollector()

    if sys.platform.startswith('linux'):
        assert fc_facts.collect() == {'fibre_channel_wwn': []}

    if sys.platform.startswith('sunos'):
        assert fc_facts.collect() == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:28:19.679068
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    hostvars = dict()
    hostvars['ansible_kernel'] = 'Linux'
    hostvars['ansible_lsb'] = dict()
    hostvars['ansible_lsb']['id'] = "RedHatEnterpriseServer"
    hostvars['ansible_lsb']['major_release'] = 7
    module = "os"
    args = dict()
    args['paths'] = dict()
    args['paths']['bin'] = list()
    args['paths']['bin'].append("/usr/bin")
    host = "localhost"
    collector = FcWwnInitiatorFactCollector(module=module, args=args, host=host)

# Generated at 2022-06-13 01:28:26.524121
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector
    import ansible.module_utils.facts.collector.base
    import ansible.module_utils.facts.utils

    fact_collector = FactCollector()
    fc_wwn = FcWwnInitiatorFactCollector()
    fc_wwn.collect()


# Generated at 2022-06-13 01:28:35.023726
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self.run_command_calls = []

        def get_bin_path(self, _, opt_dirs=[]):
            # dummy implementation: just return the command string itself
            return _

        def run_command(self, cmd, check_rc=True):
            self.run_command_calls.append(cmd)

            if 'linux' in cmd:
                return (0, '0x21000014ff52a9bb', '')

            if 'sunos' in cmd:
                return (0, 'HBA Port WWN: 10000090fa1658de', '')

            if 'aix' in cmd:
                return (0, 'fcs3 Available FC Adapter: FC Adapter', '')

# Generated at 2022-06-13 01:28:45.676474
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    TBD

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    module = AnsibleModuleMock()
    fcwwn_collector = FcWwnInitiatorFactCollector()
    fcwwn_collector.collect(module=module)
    assert module.get_bin_path('fcinfo')
    assert module.run_command()
    assert module.get_bin_path('lsdev')
    assert module.get_bin_path('lscfg')
    assert module.get_bin_path('ioscan')
    assert module.get_bin_path('fcmsutil', opt_dirs=['/opt/fcms/bin'])


# Generated at 2022-06-13 01:29:09.450599
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collectors.linux import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.plugins.system.linux import sys_info
    from ansible.module_utils.facts.plugins.system.linux import dist_info
    from ansible.module_utils.facts.plugins import cpu
    from ansible.module_utils.facts.plugins.network.linux import interfaces
    from ansible.module_utils.facts.plugins.network.linux import default_ipv4
    from ansible.module_utils.facts.plugins.network.linux import default_ipv6
    from ansible.module_utils.facts.plugins.misc.linux import selinux

# Generated at 2022-06-13 01:29:18.130391
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class TestModule(object):
        def __init__(self):
            self._module = {'run_command': {'shell': None, 'executable': None, 'chdir': None, 'data': None, 'binary_data': None, 'warn': True}}
            self.params = {}
            self.check_mode = False
            self.no_log = False
            self.saved_obj = None
            self.saved_args = None
            self._ansible_version = "2.9.13"
            self._ansible_module_name = "ansible_facts"
            self._ansible_sysversion = (1, 1, 0)
            self._ansible_debug = False

        def get_bin_path(self, cmd, opt_dirs=[]):
            return cmd


# Generated at 2022-06-13 01:29:20.242064
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    a = FcWwnInitiatorFactCollector()
    assert a is not None


# Generated at 2022-06-13 01:29:22.618875
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:25.426961
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:29.427494
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Unit test for method collect of class FcWwnInitiatorFactCollector"""
    collector = FcWwnInitiatorFactCollector()
    result = collector.collect()

    assert 'fibre_channel_wwn' in result, "Could not find 'fibre_channel_wwn' in %s" % result

# Generated at 2022-06-13 01:29:30.046307
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    pass

# Generated at 2022-06-13 01:29:34.483601
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert 'fibre_channel_wwn' in fc_facts.name
    assert 'fibre_channel_wwn' in fc_facts._fact_ids
    assert isinstance(fc_facts._fact_ids, set)

# Generated at 2022-06-13 01:29:46.907071
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    from ansible.module_utils import basic

    # --------------------------------------------------------
    #  Unit test for method collect of class FcWwnInitiatorFactCollector
    # --------------------------------------------------------

    # create instance of FcWwnInitiatorFactCollector
    fc_wwn = FcWwnInitiatorFactCollector()

    # create ansible module mock
    mock_module = basic.AnsibleModule(argument_spec={},
                                      supports_check_mode=False)

    # create instance of module_utils.facts.collector.BaseFactCollector
    mock_base_fc = basic.AnsibleModule(argument_spec={},
                                       supports_check_mode=False)

    # collect facts: call method collect of class FcWwnInitiatorFactCollector

# Generated at 2022-06-13 01:29:49.653615
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()


# Generated at 2022-06-13 01:30:18.565037
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = {}
    fc_facts = dict(fibre_channel_wwn=[])
    fc_facts['fibre_channel_wwn'].append(0x21000014ff52a9bb)
    assert fc_facts == FcWwnInitiatorFactCollector.collect()

# Generated at 2022-06-13 01:30:21.707878
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test_collector = FcWwnInitiatorFactCollector()
    assert test_collector is not None
    assert test_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:23.800299
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'
    assert f.collect() == {}

# Generated at 2022-06-13 01:30:31.145778
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    fc_fact_collector = FcWwnInitiatorFactCollector(module=module)

    # no facts should be collected when not on a supported platform
    fc_facts = fc_fact_collector.collect()
    assert fc_facts == {'fibre_channel_wwn':[]}

    # collect facts when running on various supported platforms
    module.run_command = lambda x: (0, '26000014ff52a9bb', '')
    fc_facts = fc_fact_collector.collect(module=module)
    assert fc_facts == {'fibre_channel_wwn': ['26000014ff52a9bb']}



# Generated at 2022-06-13 01:30:33.894045
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn = FcWwnInitiatorFactCollector()
    assert fc_wwn.name == "fibre_channel_wwn"
    assert fc_wwn._fact_ids == set()

# Generated at 2022-06-13 01:30:35.524665
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_fact_collector is not None

# Generated at 2022-06-13 01:30:39.235242
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'
    assert x.collect() == {}

# Generated at 2022-06-13 01:30:48.618717
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    from ansible.module_utils.facts import  Collector
    module = type('obj', (object,), {})()
    module.run_command = lambda *args, **kwargs: (0, '', '')
    collector_mock = type('obj', (object,), {})()
    collector_mock.collect.return_value = {'fibre_channel_wwn': ['0x21000014ff52a9bb']}
    Collector.collectors = [collector_mock]
    Collector.collectors_available = {'fibre_channel_wwn': collector_mock}
    collected_facts = Collector.collect(module)

    assert collected_facts['fibre_channel_wwn'] == ['0x21000014ff52a9bb']

# Generated at 2022-06-13 01:30:49.289273
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    pass

# Generated at 2022-06-13 01:30:51.152363
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj

# Generated at 2022-06-13 01:31:47.754208
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import platform

    fc_wwn = FcWwnInitiatorFactCollector()
    # unit test should run in linux or sunos
    assert platform.system().lower() in ('linux', 'sunos', 'aix', 'hp-ux')

# Generated at 2022-06-13 01:31:54.296259
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """Tests the constructor of class FcWwnInitiatorFactCollector"""

    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert len(obj._fact_ids) == 1
    assert 'fibre_channel_wwn' in obj._fact_ids

# Generated at 2022-06-13 01:32:05.590148
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils import basic
    import ansible.module_utils.facts.collector.network


    class MockModule(object):
        def __init__(self):
            self.params = {}
            self._ansible_debug = True
            self.called = False

        def get_bin_path(self, arg1, opt_dirs=None):
            return '/usr/bin/' + arg1

        def run_command(self, arg1):
            if arg1.endswith('port_name'):
                return 0, "0x21000014ff52a9bb\n0x22000014ff52a9bc\n0x23000014ff52a9bd", ""
            else:
                return 0, "", ""

    m = MockModule()
    # initialize fact collector
    fact_

# Generated at 2022-06-13 01:32:07.601206
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    class TestModule:
        def get_bin_path(self, command):
            return '/sbin/' + command
    module = TestModule()
    fcfacts = FcWwnInitiatorFactCollector(module)
    assert fcfacts.name == 'fibre_channel_wwn'
    assert fcfacts._fact_ids == set()

# Generated at 2022-06-13 01:32:16.932037
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    collected_facts = collector.collect_facts(module=None, collected_facts=None)
    myfact = FcWwnInitiatorFactCollector(basic.AnsibleModule, collected_facts=collected_facts)
    if sys.platform.startswith('aix'):
        assert(len(myfact.collect()) == 2)
    elif sys.platform.startswith('linux'):
        assert(len(myfact.collect()) == 4)
    elif sys.platform.startswith('hp-ux'):
        assert(len(myfact.collect()) >= 2)

# Generated at 2022-06-13 01:32:24.813976
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # configure test for linux
    sys.modules['ansible.module_utils.facts.utils'] = MagicMock()
    sys.modules['ansible.module_utils.facts.utils'].get_file_lines = MagicMock()
    sys.modules['ansible.module_utils.facts.utils'].get_file_lines.return_value = ['0x21000014ff52a9bb']
    sys.modules['ansible.module_utils.facts.collector'] = MagicMock()
    sys.modules['ansible.module_utils.facts.collector.BaseFactCollector'] = MagicMock()
    # tests
    collection = FcWwnInitiatorFactCollector()
    assert collection.collect() == {'fibre_channel_wwn': ['21000014ff52a9bb']}

    #

# Generated at 2022-06-13 01:32:29.012338
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_initiator_collector = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator_collector.name == 'fibre_channel_wwn'
    assert fc_wwn_initiator_collector._fact_ids == set()

# Generated at 2022-06-13 01:32:38.125529
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Test the method collect of class FcWwnInitiatorFactCollector

    :return: None
    """
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collectors
    fcwwn_collector = FcWwnInitiatorFactCollector()
    facts_dict = {}

    try:
        fcwwn_collector.collect(facts_dict=facts_dict)
    except Exception as e:
        pytest.fail("Unexpected exception raised %s" % e, pytrace=True)

    # check that we have added fcwwn fact
    assert 'fibre_channel_wwn' in facts_dict
    assert facts_dict['fibre_channel_wwn'] is not None
    # check that the fact value

# Generated at 2022-06-13 01:32:40.907666
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = {}
    obj = FcWwnInitiatorFactCollector()
    assert obj.collect(collected_facts=fc_facts) == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:32:43.500487
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fwc = FcWwnInitiatorFactCollector()
    assert fwc.name == 'fibre_channel_wwn'
    assert fwc._fact_ids == set()


# Generated at 2022-06-13 01:34:28.160888
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'
    assert c._fact_ids == set()

# Generated at 2022-06-13 01:34:34.167712
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts import namespace_facts
    from ansible.module_utils.facts.collector import _get_collectors
    facts_dict = namespace_facts.NamespaceFacts(
        _get_collectors()).collect(
        namespace='fibre_channel_wwn',
        collected_facts=dict(ansible_facts=dict()))
    assert facts_dict['ansible_facts']['fibre_channel_wwn'] == ['02000024ff40cc3e', '02000024ff40cc3d']

# Generated at 2022-06-13 01:34:39.315811
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'
    assert FcWwnInitiatorFactCollector._fact_ids == set()

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:34:48.464401
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import gather_subset
    from ansible.module_utils.facts.collectors import network

    kwargs = dict(path='/usr/sbin:/usr/bin', gather_subset=['all'])
    collected_facts = ansible_facts.AnsibleFacts(None, network.NetworkCollector, kwargs).populate()

    assert 'fibre_channel_wwn' in collected_facts
    assert 'ansible_fibre_channel_wwn' in collected_facts['ansible_facts']


# Generated at 2022-06-13 01:34:51.869944
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for class FcWwnInitiatorFactCollector
    """

    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'
    assert len(f.collect()) > 0

# Generated at 2022-06-13 01:34:55.281252
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    test_fc_facts = {'fibre_channel_wwn': ['21000014ff52a9bb', '21000014ff52b1a8', '21000014ff52b9ad']}
    fc_wwn = FcWwnInitiatorFactCollector()
    assert fc_wwn.collect() == test_fc_facts

# Generated at 2022-06-13 01:34:58.621659
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:35:07.199939
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import Facts

    class MockModule:
        class MockRunCommand:
            def __init__(self, rc, stdout, err):
                self._rc = rc
                self._stdout = stdout
                self._err = err

            def __call__(self, cmd, *args):
                return self._rc, self._stdout, self._err

        def __init__(self):
            self.run_command = self.MockRunCommand(0, '', '')
            self.get_bin_path = lambda cmd: ''

    sys_platform = sys.platform
    # Mock Linux
    sys.platform = 'linux'
    fc_facts = FcWwnInitiatorFactCollector().collect()
    assert sys.platform == 'linux'

# Generated at 2022-06-13 01:35:09.398849
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    test_class = FcWwnInitiatorFactCollector()
    from ansible.module_utils.facts import ModuleTestCase
    test_class.collect(ModuleTestCase())

# Generated at 2022-06-13 01:35:14.231535
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """

    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector

    c = Collector()
    fc = FcWwnInitiatorFactCollector()
    assert fc.collect() == {}