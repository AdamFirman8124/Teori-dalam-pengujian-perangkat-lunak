

# Generated at 2022-06-13 01:27:31.253890
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert isinstance(fc_facts._fact_ids, set)

# Generated at 2022-06-13 01:27:36.643251
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for constructor of class FcWwnInitiatorFactCollector
    """
    class MockModule(object):
        """
        AnsibleModule mock class
        """
        @staticmethod
        def get_bin_path(binary, opt_dirs=[]):
            """
            AnsibleModule.get_bin_path() mock function
            """
            bin_path = None
            if binary == 'fcinfo':
                bin_path = '/usr/sbin/fcinfo'
            elif binary == 'lsdev':
                bin_path = '/usr/sbin/lsdev'
            elif binary == 'lscfg':
                bin_path = '/usr/sbin/lscfg'
            elif binary == 'ioscan':
                bin_path = '/sbin/ioscan'

# Generated at 2022-06-13 01:27:38.757992
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'



# Generated at 2022-06-13 01:27:48.587908
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    if platform.system() != 'Linux':
        print("Test skipped due to not Linux platform")
        return

    class Module:
        def __init__(self, sysfs_path='/sys'):
            self.sysfs_path = sysfs_path

        def get_bin_path(self, exe, opt_dirs=None):
            if exe == 'fcinfo':
                return '/usr/sbin/fcinfo'
            if exe == 'lsdev':
                return '/usr/sbin/lsdev'
            if exe == 'lscfg':
                return '/usr/sbin/lscfg'
            if exe == 'ioscan':
                return '/sbin/ioscan'

# Generated at 2022-06-13 01:27:53.601060
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    factCollector = FcWwnInitiatorFactCollector()
    wwn_facts = factCollector.collect()
    assert type(wwn_facts) is dict
    assert 'fibre_channel_wwn' in wwn_facts
    assert type(wwn_facts['fibre_channel_wwn']) is list

# Generated at 2022-06-13 01:27:59.048145
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector()
    fc_facts_result = fc_facts.collect()
    assert fc_facts_result['fibre_channel_wwn']

# Generated at 2022-06-13 01:28:02.591563
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_fact_collector = FcWwnInitiatorFactCollector()
    result = fc_fact_collector.collect()
    assert isinstance(result, dict)
    assert 'fibre_channel_wwn' in result

# Generated at 2022-06-13 01:28:06.041305
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test_obj = FcWwnInitiatorFactCollector()
    assert test_obj
    assert test_obj.name == 'fibre_channel_wwn'
    assert test_obj._fact_ids == set()


# Generated at 2022-06-13 01:28:09.350618
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'
    assert x._fact_ids == set()


# Generated at 2022-06-13 01:28:19.482092
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collectors.system.fibre_channel_wwn_initiator import FcWwnInitiatorFactCollector
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import builtins

    module = FactsCollector()

    # mock read_file to return desired output
    def mock_read_file(fname, default=None):
        if "port_name" in fname:
            return "0x21000014ff52a9bb"
        return default
    builtins.open = mock_read_file

    # run the collect method
    fc_facts = FcWwnInitiatorFactCollector.collect(module)

    # check if

# Generated at 2022-06-13 01:28:33.083725
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Skip test on platforms other than Linux
    if not sys.platform.startswith('linux'):
        return

    fc = FcWwnInitiatorFactCollector()
    assert fc is not None

# Generated at 2022-06-13 01:28:44.948958
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # test values to be used by mock os module in place of /sys/class/fc_host/*/port_name
    mock_values = ['0x21000014ff52a9bb', '0x21000014ff52a9cc']

    # test values to be used by mock os module in place of /dev/disk/.../wwn

# Generated at 2022-06-13 01:28:47.985878
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact = FcWwnInitiatorFactCollector()
    assert fact.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:28:57.713085
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import CollectionFailedError
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    module.get_bin_path.side_effect = lambda x, opt_dirs: x
    collector = FcWwnInitiatorFactCollector()
    # should not throw exception if fcinfo hba-port returns 0
    collector.collect(module)
    module.run_command.assert_called_with('fcinfo hba-port')
    # should throw exception if fcinfo hba-port returns non-zero
    module.run_command.return_value = (1, '', '')
    with pytest.raises(CollectionFailedError):
        collector.collect(module)

# Generated at 2022-06-13 01:29:08.471834
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    platform_dict = {
        'platform': 'linux',
        'path': 'fake/path/to/fixtures',
        'lsb': {
            'distributor_id': 'Ubuntu',
            'release': '14.04',
            'codename': 'trusty'
        },
        'distribution': 'Ubuntu',
        'distribution_version': '14.04',
        'distribution_release': 'trusty',
        'distribution_major_version': '14'
    }

    args = {
        'module_name': 'FcWwnInitiatorFactCollector'
    }

    test_class = BaseFactCollector.load_collector_from_name(args['module_name'], platform_dict)
    obj = test_class(args)

    result = obj.collect()

# Generated at 2022-06-13 01:29:17.589483
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Test FcWwnInitiatorFactCollector
    #  - no facts are returned
    #  - a single fact is returned
    #  - multiple facts are returned
    #
    # Note that actual os.linesep is used here because we are mocking the
    # file and os.linesep is platform specific
    #
    # TODO: more testing for multiple platforms (linux, solaris, aix, hpux)
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import get_collector_facts
    from ansible.module_utils.facts.utils import get_file_lines

    Collector.collectors = [('fibre_channel_wwn', FcWwnInitiatorFactCollector)]
    Collector.collected_facts = dict()

    #

# Generated at 2022-06-13 01:29:28.197883
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import os
    import sys
    import test.utils as tu
    import test.runner as tr
    # make sure module can be imported when running unit tests
    # (we have to set PYTHONPATH; see also __main__ below)
    this_module_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, this_module_path + '/../')

    # create dummy module
    module = tu.dummy_module()

    # create dummy facts
    collected_facts = tu.dummy_collector_facts()

    # instantiate object
    this_object = FcWwnInitiatorFactCollector()

    # call facts collection

# Generated at 2022-06-13 01:29:40.426788
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    def sys_platform(self):
        return 'linux'

    def get_file_lines(self, *args, **kwargs):
        line = "0x21000014ff52a9bb\n0x21000014ff52a9bc"

        return line.splitlines()

    FcWwnInitiatorFactCollector.__file__ = '/some/path/somefile.py'

    setattr(sys, 'platform', 'linux')
    FcWwnInitiatorFactCollector._platform = 'linux'
    FcWwnInitiatorFactCollector._file_path = "/sys/class/fc_host/*/port_name"
    FcWwnInitiatorFactCollector._file_name = "port_name"
    FcWwnInitiatorFactCollector.get_file_lines = get

# Generated at 2022-06-13 01:29:50.683630
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for FcWwnInitiatorFactCollector class
    """
    print("Test if class FcWwnInitiatorFactCollector is correctly defined:")
    # instance of class
    fact_ins = FcWwnInitiatorFactCollector()
    print("Testing class %s: " % (fact_ins.__class__))

    # compare name
    print("\tName    :", fact_ins.name)
    assert fact_ins.name == 'fibre_channel_wwn'

    # test if _fact_ids property was defined
    assert hasattr(fact_ins, '_fact_ids')
    # test if _fact_ids is set
    assert fact_ins._fact_ids == fact_ins.name
    # test if _fact_ids is a set

# Generated at 2022-06-13 01:30:00.615750
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule

    # Create a mock module
    module = MockModule()

    # Create an instance
    fact_collector = FcWwnInitiatorFactCollector()

    # Get facts
    facts = fact_collector.collect(module=module)

    assert facts
    assert 'fibre_channel_wwn' in facts
    if sys.platform.startswith('hp-ux'):
        assert len(facts['fibre_channel_wwn']) > 0
        assert isinstance(facts['fibre_channel_wwn'], list)


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:30:13.159495
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts

# Generated at 2022-06-13 01:30:19.351215
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # create instance of class FcWwnInitiatorFactCollector
    facts_instance = FcWwnInitiatorFactCollector()
    assert isinstance(facts_instance, FcWwnInitiatorFactCollector)
    # verify name of instance
    assert facts_instance.name == 'fibre_channel_wwn'
    # verify if method 'collect' is implemented
    assert callable(getattr(facts_instance, 'collect', None))

# Generated at 2022-06-13 01:30:23.188114
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'
    assert FcWwnInitiatorFactCollector._fact_ids == set()


if __name__ == "__main__":
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:29.176882
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'
    assert FcWwnInitiatorFactCollector._fact_ids == set()
    assert FcWwnInitiatorFactCollector.get_fact_ids() == set()
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()
    assert fact_collector.get_fact_ids() == set()

# Generated at 2022-06-13 01:30:31.770283
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collected_facts=None
    obj = FcWwnInitiatorFactCollector(collected_facts=collected_facts)
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:36.911291
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    # Create instance
    fcwwn_instance = FcWwnInitiatorFactCollector()

    # Check instance
    assert fcwwn_instance
    assert fcwwn_instance.name == 'fibre_channel_wwn'
    assert fcwwn_instance._fact_ids == set()


# Generated at 2022-06-13 01:30:47.584354
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fact_collector = FcWwnInitiatorFactCollector()

    # example simulated output from /sys/class/fc_host/*/port_name
    port_name_files = ['-rw-r--r--. 1 root root 4096 Sep 22 05:06 /sys/class/fc_host/host0/port_name',
             '-rw-r--r--. 1 root root 4096 Sep 22 05:06 /sys/class/fc_host/host1/port_name',
             '-rw-r--r--. 1 root root 4096 Sep 22 05:06 /sys/class/fc_host/host2/port_name']

    # simulate output of 'fcinfo hba-port'

# Generated at 2022-06-13 01:30:48.710737
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:51.352899
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:00.644228
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector.
    """
    # mock ansible module so we can use it
    class MockModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name, opt_dirs=[]):
            return "/bin/%s" % name

        def run_command(self, cmd):
            return 0, "Mock command output", ""

    class MockAnsibleModuleInstance(object):
        """
        Mock for ansible module instance.
        """
        def __init__(self):
            self.module = MockModule()

    mock_module_instance = MockAnsibleModuleInstance()

    # mock object returned by class BaseFactCollector

# Generated at 2022-06-13 01:31:15.652932
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn_obj = FcWwnInitiatorFactCollector()
    assert fcwwn_obj
    assert fcwwn_obj.name == 'fibre_channel_wwn'
    assert len(fcwwn_obj.collect().items()) == 1

# Generated at 2022-06-13 01:31:17.118781
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert len(c._fact_ids) > 0

# Generated at 2022-06-13 01:31:26.415951
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    # Create Collector with mocked ansible file module
    class MockAnsibleFileModule:
        def get_bin_path(self, arg1, opt_dirs=[]):
            if arg1 == 'lsdev':
                return '/usr/sbin/lsdev'
            elif arg1 == 'lscfg':
                return '/usr/sbin/lscfg'
            elif arg1 == 'ioscan':
                return '/usr/sbin/ioscan'
            elif arg1 == 'fcmsutil':
                return '/opt/fcms/bin/fcmsutil'
            elif arg1 == 'fcinfo':
                return '/usr/sbin/fcinfo'

# Generated at 2022-06-13 01:31:27.051706
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    pass

# Generated at 2022-06-13 01:31:38.902721
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    class NullModule(object):
        def __init__(self):
            self.params = {}
        def run_command(self, cmd):
            return 0, None, None
        def get_bin_path(self, cmd, opt_dirs=[]):
            if cmd == 'fcinfo':
                return "/usr/sbin/fcinfo"
            elif cmd == 'ioscan':
                return "/usr/sbin/ioscan"
            elif cmd == 'fcmsutil':
                return "/opt/fcms/bin/fcmsutil"
            elif cmd == 'lscfg':
                return "/usr/sbin/lscfg"
    null_module = NullModule()

# Generated at 2022-06-13 01:31:47.083770
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.utils import AnsibleFacts

    class MockModule(object):
        def __init__(self):
            self.run_command = None
            self.get_bin_path = None
            self.run_command = None
            self.exit_json = None

        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'ioscan':
                return '/sbin/ioscan'
            if name == 'fcmsutil':
                return '/opt/fcms/bin/fcmsutil'
            if name == 'lsdev':
                return '/bin/lsdev'
            if name == 'lscfg':
                return '/bin/lscfg'
            if name == 'fcinfo':
                return '/usr/sbin/fcinfo'


# Generated at 2022-06-13 01:31:56.758374
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """ Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    from ansible.module_utils.facts.collectors.network.fibre_channel_wwn import FcWwnInitiatorFactCollector
    fact_collector = FcWwnInitiatorFactCollector()
    from ansible.module_utils.facts.collector import BaseFactCollector
    my_base_fact_collector = BaseFactCollector()
    my_base_fact_collector.collect()
    my_base_fact_collector.populate()
    fact_collector.collect(collected_facts=my_base_fact_collector.collected_facts)

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:31:58.844463
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn = FcWwnInitiatorFactCollector()
    assert fcwwn.name == 'fibre_channel_wwn'
    assert isinstance(fcwwn._fact_ids, set), '_fact_ids is not a set'

# Generated at 2022-06-13 01:32:01.635476
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    FcWwnInitiatorFactCollector_collect may be tested in integration tests only:
    - for now, no testing for linux platform
    - testing for other platforms will be done using mocks
    """
    pass

# Generated at 2022-06-13 01:32:05.937631
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_initiator_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator_fact_collector.name == 'fibre_channel_wwn'
    assert fc_wwn_initiator_fact_collector._fact_ids == set()

# Generated at 2022-06-13 01:32:20.981726
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    module = BaseFactCollector()
    fc_collector = FcWwnInitiatorFactCollector()
    fc_facts = fc_collector.collect(module)
    assert 'fibre_channel_wwn' in fc_facts

# Generated at 2022-06-13 01:32:28.073025
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    sys.modules["ansible.module_utils.facts.system.fibre_channel_wwn_initiator"] = __import__('ansible.module_utils.facts.system.fibre_channel_wwn_initiator_stub')
    import ansible.module_utils.facts.system.fibre_channel_wwn_initiator
    fcwwn_coll = ansible.module_utils.facts.system.fibre_channel_wwn_initiator.FcWwnInitiatorFactCollector()
    test_ansible_module = ansible.module_utils.facts.system.fibre_channel_wwn_initiator.AnsibleModuleMock()

# Generated at 2022-06-13 01:32:30.617867
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    instance = FcWwnInitiatorFactCollector()
    assert instance.name == 'fibre_channel_wwn'
    assert instance._fact_ids is not None

# Generated at 2022-06-13 01:32:33.610596
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcfacts_collector = FcWwnInitiatorFactCollector()
    assert fcfacts_collector.name == 'fibre_channel_wwn'
    assert fcfacts_collector._fact_ids == set()
    assert isinstance(fcfacts_collector, FcWwnInitiatorFactCollector)


# Generated at 2022-06-13 01:32:41.659084
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.virtual.sysctl import SysctlFactCollector
    from ansible.module_utils.facts.virtual.smartos import SmartOSFactCollector
    from ansible.module_utils.facts.virtual.openvz import OpenVzFactCollector
    from ansible.module_utils.facts.virtual.xen import XenFactCollector
    from ansible.module_utils.facts.virtual.kvm import KVMFactCollector
    from ansible.module_utils.facts.virtual.bhyve import BhyveFactCollector
    from ansible.module_utils.facts.virtual.vmware import VMwareFactCollector

# Generated at 2022-06-13 01:32:42.581618
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:32:50.518185
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.exit_args = {}
        def fail_json(self, *args, **kwargs):
            self.exit_args = kwargs
            self.exit_args.update({'failed': True})
            raise Exception(kwargs['msg'])
        def get_bin_path(self, *args, **kwargs):
            return '/bin/uname'

# Generated at 2022-06-13 01:32:55.236623
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector.collect()
    assert fc_facts['fibre_channel_wwn'] == []

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:33:01.265419
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    # Create a dummy module object
    module = type('module', (object,), {'run_command': lambda x: (0, '', ''),
                                        'get_bin_path': lambda x: True})
    # Create an instance of class FcWwnInitiatorFactCollector
    # This class collects facts on fibre channel wwn initiator.
    fc_initiator_collector = FcWwnInitiatorFactCollector()

    # Call method collect of class FcWwnInitiatorFactCollector
    data = fc_initiator_collector.collect(module=module)
    assert type(data) == dict
    assert data['fibre_channel_wwn'] == []

# Generated at 2022-06-13 01:33:04.947784
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """ Unit test for method collect of class FcWwnInitiatorFactCollector """
    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []
    fc_facts['fibre_channel_wwn'].append("21000014ff52a9bb")
    fc_facts['fibre_channel_wwn'].append("21000014ff52a9bc")
    fc = FcWwnInitiatorFactCollector()
    assert fc.collect() == fc_facts

# Generated at 2022-06-13 01:33:31.086697
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:33:35.726530
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """Unit test for constructor of class FcWwnInitiatorFactCollector"""

    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'
    assert c._fact_ids == set()


# Generated at 2022-06-13 01:33:37.078845
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:33:47.784950
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.utils import get_file_lines

    def create_fake_file(file, lines=None):
        if not lines:
            # Define an empty list of lines
            lines = []
        with open(file, 'w') as f:
            for line in lines:
                f.write(line + '\n')

    def remove_fake_file(file):
        # Remove a file
        os.unlink(file)

    import os, copy, sys, tempfile
    from distutils.version import LooseVersion

    # Define a collector object
    collector = Collector()
    # Add FcWwnInitiatorFactCollector to collectors list of collector object
   

# Generated at 2022-06-13 01:33:49.549760
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:33:55.150897
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    print("Test: method collect of class FcWwnInitiatorFactCollector")
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import get_collector_instance
    # init collector
    facts_collector = get_collector_instance(collector.FcWwnInitiatorFactCollector)
    facts = facts_collector.collect()
    # test if fibre_channel_wwn is a list
    assert isinstance(facts['fibre_channel_wwn'], list)

# Generated at 2022-06-13 01:33:59.230538
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert len(fact_collector._fact_ids) == 0

# Generated at 2022-06-13 01:34:01.916509
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert isinstance(fact_collector.name, str)
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:08.222749
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # TODO: change this test case to actually match the FcWwnInitiatorFactCollector output
    # it's totally useless as it is
    test_module = type('TestModule', (object,), {'run_command': run_command})
    test_collector = FcWwnInitiatorFactCollector()
    data = test_collector.collect(module=test_module)
    assert data['fibre_channel_wwn'] == ['10000090fa1658de']

# Fake -c command: returns output and return code 0

# Generated at 2022-06-13 01:34:11.238497
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == "fibre_channel_wwn"



# Generated at 2022-06-13 01:34:57.973893
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_init_fc = FcWwnInitiatorFactCollector()
    assert fc_wwn_init_fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:35:01.032290
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'
    assert c._fact_ids == set()


# Generated at 2022-06-13 01:35:03.351920
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:35:05.927329
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test_obj = FcWwnInitiatorFactCollector()
    assert test_obj
    assert test_obj.name == "fibre_channel_wwn"
    assert test_obj._fact_ids == set()

# Generated at 2022-06-13 01:35:07.949423
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert c.name == "fibre_channel_wwn"
    assert c._fact_ids == set()
    assert c.collect() == {}

# Generated at 2022-06-13 01:35:09.368125
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts_collector = FcWwnInitiatorFactCollector()
    assert fc_facts_collector is not None


# Generated at 2022-06-13 01:35:14.834202
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    import ansible.module_utils.facts.collector
    sys.modules['ansible.module_utils.facts.collector'] = ansible.module_utils.facts.collector
    fc_wwn = FcWwnInitiatorFactCollector()
    module = ansible.module_utils.facts.collector.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    fc_wwn.collect(module)


# Generated at 2022-06-13 01:35:16.690260
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_initiator = FcWwnInitiatorFactCollector()
    assert fc_initiator.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:35:25.128452
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible_collections.ansible.netcommon.plugins.module_utils.facts.collector.fc import FcWwnInitiatorFactCollector
    from ansible_collections.ansible.netcommon.plugins.module_utils.facts import FactsHelper

    # Set up
    module = FactsHelper("linux_fibre_channel_wwn", '', {}, {}, [])
    fcwwn_collector = FcWwnInitiatorFactCollector(module)
    fcwwn_collector._module = module

    # Testing
    fc_facts = fcwwn_collector.collect()
    assert fc_facts == {}


# Generated at 2022-06-13 01:35:27.010314
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x
    assert x.name == 'fibre_channel_wwn'