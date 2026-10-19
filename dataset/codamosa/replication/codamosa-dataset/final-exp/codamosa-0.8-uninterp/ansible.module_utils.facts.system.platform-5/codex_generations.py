

# Generated at 2022-06-13 03:13:16.665528
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector().collect()
    assert platform_facts['system']
    assert platform_facts['kernel']
    assert platform_facts['kernel_version']
    assert platform_facts['machine']
    assert platform_facts['python_version']
    assert platform_facts['fqdn']
    assert platform_facts['hostname']
    assert platform_facts['nodename']
    assert platform_facts['domain']
    assert platform_facts['userspace_bits']
    assert platform_facts['userspace_architecture']
    assert platform_facts['architecture']
    assert platform_facts['machine_id']

# Generated at 2022-06-13 03:13:24.077887
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert 'system' in platform_collector._fact_ids
    assert 'kernel' in platform_collector._fact_ids
    assert 'kernel_version' in platform_collector._fact_ids
    assert 'machine' in platform_collector._fact_ids
    assert 'python_version' in platform_collector._fact_ids
    assert 'architecture' in platform_collector._fact_ids
    assert 'machine_id' in platform_collector._fact_ids

# Generated at 2022-06-13 03:13:25.215068
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 03:13:29.826604
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    assert fact_collector.name == 'platform'
    assert fact_collector._fact_ids == set(['system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id'])

# Generated at 2022-06-13 03:13:38.413277
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    class Fake_Module:
        def get_bin_path(self, arg):
            return True

        def run_command(self, cmd):
            return (0, True, False)

    class Fake_Collector(FactCollector):
        def __init__(self):
            self.collectors = []

        def add_collector(self, collector):
            self.collectors.append(collector)

    class Fake_BaseFactCollector(BaseFactCollector):
        def __init__(self, module):
            pass

    mod = Fake_Module()
    fake_basefact = Fake_BaseFactCollector(mod)
    fake_collector = Fake_Collector()
    platform

# Generated at 2022-06-13 03:13:42.886139
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    instance = PlatformFactCollector()
    assert instance.name == 'platform'
    assert 'system' in instance._fact_ids
    assert 'kernel' in instance._fact_ids
    assert 'machine' in instance._fact_ids
    assert 'python_version' in instance._fact_ids
    assert 'architecture' in instance._fact_ids
    assert 'machine_id' in instance._fact_ids

# Generated at 2022-06-13 03:13:45.877995
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine',
                                 'python_version', 'architecture', 'machine_id'])


# Generated at 2022-06-13 03:13:56.742924
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pc = PlatformFactCollector()
    facts = pc.collect()

    assert isinstance(facts, dict)
    assert 'system' in facts.keys()
    assert 'kernel' in facts.keys()
    assert 'kernel_version' in facts.keys()
    assert 'machine' in facts.keys()
    assert 'python_version' in facts.keys()
    assert 'architecture' in facts.keys()
    assert 'userspace_bits' in facts.keys()
    assert 'machine_id' in facts.keys()
    assert 'fqdn' in facts.keys()
    assert 'hostname' in facts.keys()
    assert 'nodename' in facts.keys()
    assert 'domain' in facts.keys()

# Generated at 2022-06-13 03:14:02.067005
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    import socket
    import platform
    import tempfile

    temp_dir = tempfile.mkdtemp()
    temp_file1 = tempfile.mkstemp(dir=temp_dir)[1]
    temp_file2 = tempfile.mkstemp(dir=temp_dir)[1]

# Generated at 2022-06-13 03:14:06.625199
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert collector._fact_ids == set(['system',
                                       'kernel',
                                       'kernel_version',
                                       'machine',
                                       'python_version',
                                       'architecture',
                                       'machine_id'])


# Generated at 2022-06-13 03:15:17.177271
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import random
    import string
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector

    class MockModule:
        def __init__(self):
            self.params = {}
            self.tmpdir = tempfile.mkdtemp()

        def get_bin_path(self, program):
            if program in ["getconf", "bootinfo", "sysctl"]:
                return program
            return None

        def run_command(self, args):
            if args[0] == "getconf":
                random_arch = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
                return 0, random_arch, ""

# Generated at 2022-06-13 03:15:30.226040
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    '''Unit test for constructor of class PlatformFactCollector'''
    obj = PlatformFactCollector()
    assert obj.name == "platform"
    assert obj._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])


# Generated at 2022-06-13 03:15:46.794867
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform as platform_module
    from ansible.module_utils.facts import collector

    platform_fact_collector = collector.get_collector('platform')

    # Return an empty dict when the platform module is mocked out
    assert platform_fact_collector.collect() == {}

    def get_file_content(filename):
        raise IOError('Failed to read file')

    platform_fact_collector.get_file_content = get_file_content
    assert 'machine_id' not in platform_fact_collector.collect()['platform']

    del platform_fact_collector.get_file_content
    assert platform_fact_collector.collect()['platform']['machine_id'] == '4eda4f37db3f4b9c8b4d4afcfaafd2a1'

    # Return

# Generated at 2022-06-13 03:15:47.757865
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_collector = PlatformFactCollector()
    platform_collector.collect()

# Generated at 2022-06-13 03:15:48.412537
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector().collect()

# Generated at 2022-06-13 03:15:51.074159
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()

    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])

# Generated at 2022-06-13 03:15:55.058199
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect()

if __name__ == '__main__':
    test_PlatformFactCollector_collect()

# Generated at 2022-06-13 03:16:04.255632
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create a PlatformFactCollector to test with
    pfc = PlatformFactCollector()

    # Test return value
    expected_result = {
        'domains': None,
        'architecture': 'x86_64',
        'nodename': 'ansible-controller',
        'kernel': '3.10.0-327.13.1.el7.x86_64',
        'python_version': '2.7.5',
        'userspace_architecture': 'x86_64',
        'userspace_bits': '64',
        'kernel_version': '#1 SMP Thu Mar 31 16:04:38 UTC 2016',
        'system': 'Linux',
        'fqdn': 'ansible-controller.example.com',
        'machine': 'x86_64'
    }
   

# Generated at 2022-06-13 03:16:10.300768
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    hostvars = {}
    platformFactCollector = PlatformFactCollector()
    platformFactCollector.collect(hostvars)
    assert 'system' in hostvars, 'Failed to find system'
    assert 'kernel' in hostvars, 'Failed to find kernel'
    assert 'kernel_version' in hostvars, 'Failed to find kernel_version'
    assert 'machine' in hostvars, 'Failed to find machine'
    assert 'python_version' in hostvars, 'Failed to find python_version'
    assert 'architecture' in hostvars, 'Failed to find architecture'

# Generated at 2022-06-13 03:16:16.239459
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_col = PlatformFactCollector()
    assert platform_fact_col.name == 'platform'
    assert platform_fact_col._fact_ids == set(['system',
                                               'kernel',
                                               'kernel_version',
                                               'machine',
                                               'python_version',
                                               'architecture',
                                               'machine_id'])

# Generated at 2022-06-13 03:17:44.043222
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])

# Generated at 2022-06-13 03:17:49.799808
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfact_collector = PlatformFactCollector()

    assert pfact_collector.name == 'platform'
    assert pfact_collector._fact_ids == set(['system',
                                             'kernel',
                                             'kernel_version',
                                             'machine',
                                             'python_version',
                                             'architecture',
                                             'machine_id'])

# Generated at 2022-06-13 03:18:00.396666
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # This test is Linux specific....
    # Because we're mocking a lot of things I'm setting the
    # get_file_content return value to a known string so that we
    # don't need to mock file functions as well.
    content = "d9a7e51a-8b79-46e5-a6d7-6b8ac2f2a6b9"

    my_test_module = AnsibleModuleMock()
    my_test_module.run_command = MagicMock(return_value=(0, "", ""))
    my_test_module.get_bin_path = MagicMock(return_value="/bin")
    get_file_content = MagicMock(return_value=content)
    my_platform_fct_collector = PlatformFactCollector(my_test_module)
    my

# Generated at 2022-06-13 03:18:05.277898
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == "platform"
    assert pfc._fact_ids.issubset({"system",
                                   "kernel",
                                   "kernel_version",
                                   "machine",
                                   "python_version",
                                   "architecture"})

# Generated at 2022-06-13 03:18:09.662756
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])

# Generated at 2022-06-13 03:18:15.061751
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # TODO: The fact_collector should be mocked in a more useful way
    from ansible.module_utils.facts.collector import get_collector_instance

    pfc = get_collector_instance('platform')
    result = pfc.collect()

    assert(result['system'] == platform.system())
    assert(result['kernel'] == platform.release())
    assert(result['kernel_version'] == platform.version())
    assert(result['machine'] == platform.machine())
    assert(result['python_version'] == platform.python_version())
    assert(result['fqdn'] == socket.getfqdn())
    assert(result['hostname'] == platform.node().split('.')[0])
    assert(result['nodename'] == platform.node())

# Generated at 2022-06-13 03:18:15.634347
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector().name == 'platform'

# Generated at 2022-06-13 03:18:25.010484
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    os_uname = platform.uname()

    collector = PlatformFactCollector()


# Generated at 2022-06-13 03:18:33.690595
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import types
    import platform

    test_module = types.ModuleType('test_module')
    # Simulate a module object
    test_module.get_bin_path = lambda x: x
    platform_facts = PlatformFactCollector().collect(module=test_module)
    # Just a couple of basic tests, need more
    assert 'system' in platform_facts
    assert 'kernel' in platform_facts
    assert 'kernel_version' in platform_facts
    assert 'machine' in platform_facts
    assert 'python_version' in platform_facts
    assert 'architecture' in platform_facts
    assert 'userspace_bits' in platform_facts
    assert 'userspace_architecture' in platform_facts

    # Test if the method 'collect' returns the same value for
    # the userspace architecture as 'platform.machine()

# Generated at 2022-06-13 03:18:38.818778
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platformFactCollector = PlatformFactCollector()
    assert platformFactCollector.name == 'platform'
    assert platformFactCollector._fact_ids == set(['system',
                                                    'kernel',
                                                    'kernel_version',
                                                    'machine',
                                                    'python_version',
                                                    'architecture',
                                                    'machine_id'])
    assert platformFactCollector.priority == 60



# Generated at 2022-06-13 03:21:49.988003
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platformfact_collector = PlatformFactCollector()
    assert platformfact_collector.name == 'platform', \
       "PlatformFactCollector() constructor doesn't set name correctly"
    assert platformfact_collector._fact_ids == set(['system',
                                                    'kernel',
                                                    'kernel_version',
                                                    'machine',
                                                    'python_version',
                                                    'architecture',
                                                    'machine_id']), \
       "PlatformFactCollector() constructor doesn't set _fact_ids correctly"

# Generated at 2022-06-13 03:21:54.948605
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    sut = PlatformFactCollector()
    assert sut.name == 'platform'
    assert set(sut.fact_ids()) == set(['system',
                                       'kernel',
                                       'kernel_version',
                                       'machine',
                                       'python_version',
                                       'architecture',
                                       'machine_id'])

test_PlatformFactCollector()

# Generated at 2022-06-13 03:21:57.649222
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    instance = PlatformFactCollector()
    assert isinstance(instance, BaseFactCollector)
    assert "python_version" in instance._fact_ids


# Generated at 2022-06-13 03:22:00.535437
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc is not None

# vim: expandtab:ts=4:sw=4

# Generated at 2022-06-13 03:22:04.839542
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """Tests if the constructor of PlatformFactCollector works as expected."""
    p = PlatformFactCollector()
    assert p._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:22:13.090232
# Unit test for method collect of class PlatformFactCollector

# Generated at 2022-06-13 03:22:13.519774
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()

# Generated at 2022-06-13 03:22:15.566907
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert p._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine',
                               'python_version', 'architecture', 'machine_id'])