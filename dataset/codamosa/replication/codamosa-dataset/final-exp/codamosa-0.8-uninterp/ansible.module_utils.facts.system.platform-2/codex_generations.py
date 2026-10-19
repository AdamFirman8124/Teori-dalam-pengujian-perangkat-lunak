

# Generated at 2022-06-13 03:13:04.037061
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils._text import to_bytes
    import platform

    # Create a PlatformFactCollector instance to test
    pfc = PlatformFactCollector()

    # Create a local test function to mock out platform.uname and platform.python_version
    def local_uname(system=None, nodename=None, release=None, version=None, machine=None, processor=None, hardware=None):
        return [system, nodename, release, version, machine, processor, hardware]

    def local_python_version():
        return "3.6.0"

    # Set up the platform.uname() and platform.python_version() mocks
    platform.uname = local_uname
    platform.python_version = local_python_version

    # Create a dictionary

# Generated at 2022-06-13 03:13:06.472490
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pc = PlatformFactCollector()
    assert pc.collect() == {}

# Generated at 2022-06-13 03:13:13.612860
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create a mock AnsibleModule object, and assign it to the module
    # argument of PlatformFactCollector
    fake_module = type('AnsibleModule', (object,),
        dict(run_command=lambda *args: (0, 'x86_64', ''),
        get_bin_path=lambda *args: '/bin/getconf'))()

    collector = PlatformFactCollector(fake_module)

    # Perform the collection and verify the result
    facts = collector.collect()

    assert facts is not None
    assert type(facts) is dict
    assert 'architecture' in facts
    assert facts['architecture'] == 'x86_64'

# Generated at 2022-06-13 03:13:21.967369
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_collector = PlatformFactCollector()
    p_facts = platform_collector.collect()
    assert p_facts['system'] == 'Darwin'
    assert p_facts['kernel'] == '17.5.0'
    assert p_facts['kernel_version'] == 'Darwin Kernel Version 17.5.0: Mon Mar  5 22:24:32 PST 2018; root:xnu-4570.51.1~1/RELEASE_X86_64'
    assert p_facts['machine'] == 'x86_64'
    assert p_facts['python_version'] == '2.7.14'
    assert p_facts['architecture'] == 'x86_64'
    assert p_facts['userspace_bits'] == '64'

# Generated at 2022-06-13 03:13:24.808018
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pc = PlatformFactCollector()
    platform_facts = pc.collect(None, {})
    # Check for values we can easily test for
    assert(platform_facts['system'] == platform.system())
    assert(platform_facts['kernel'] == platform.release())
    assert(platform_facts['kernel_version'] == platform.version())
    assert(platform_facts['machine'] == platform.machine())
  

# Generated at 2022-06-13 03:13:25.803397
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector is not None

# Generated at 2022-06-13 03:13:35.488595
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import injector
    from ansible.module_utils.facts.collector.platform import PlatformFactCollector

    obj = Collector(None);
    platform_collector = PlatformFactCollector(obj)

    assert platform_collector._fact_ids == {'kernel', 'kernel_version', 'python_version', 'system', 'architecture', 'userspace_bits', 'domain', 'nodename', 'hostname', 'machine', 'machine_id', 'fqdn', 'userspace_architecture'}
    assert 'platform_' + platform_collector.name == platform_collector.collector
    assert platform_collector.depends == set()
    assert platform_collector.priority == 1

# Generated at 2022-06-13 03:13:39.973500
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == {'system',
                             'kernel',
                             'kernel_version',
                             'machine',
                             'python_version',
                             'architecture',
                             'machine_id'}

# Generated at 2022-06-13 03:13:45.161590
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """Unit test for constructor of class PlatformFactCollector"""
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])


# Generated at 2022-06-13 03:13:47.561383
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector()
    assert obj.name == 'platform'
    assert obj._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine',
                                 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:14:45.509462
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()

# Generated at 2022-06-13 03:14:50.620140
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == set(['system',
                                                'kernel',
                                                'kernel_version',
                                                'machine',
                                                'python_version',
                                                'architecture',
                                                'machine_id'])

# Generated at 2022-06-13 03:14:58.731347
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    import sys

    collector = PlatformFactCollector()

    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins

    class MockModule(object):
        def __init__(self):
            self.params = {
                'gather_subset': '!all',
                'gather_timeout': 10,
                'filter': '*'
            }

        def run_command(self, args):
            return 1, 'x86_64', ''

        def get_bin_path(self, name, opts=None, required=False):
            return '/bin/' + name


# Generated at 2022-06-13 03:15:09.081861
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    result = platform_fact_collector.collect()

    assert result.get('system')
    assert result.get('kernel')
    assert result.get('kernel_version')
    assert result.get('machine')
    assert result.get('python_version')
    assert result.get('architecture')
    assert result.get('machine_id')
    assert result.get('fqdn')
    assert result.get('hostname')
    assert result.get('nodename')
    assert result.get('domain')
    assert result.get('userspace_bits')
    assert result.get('userspace_architecture')

    assert isinstance(result.get('system'), str)
    assert isinstance(result.get('kernel'), str)

# Generated at 2022-06-13 03:15:12.720056
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert p._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:15:16.389287
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    class_instance = PlatformFactCollector()
    result = class_instance.collect(collected_facts={})
    assert isinstance(result, dict)
    assert result['system'] == platform.system()
    assert result['kernel'] == platform.release()
    assert result['kernel_version'] == platform.version()
    assert result['machine'] == platform.machine()
    assert result['python_version'] == platform.python_version()

# Generated at 2022-06-13 03:15:20.195607
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = FakeModule()
    pm = PlatformFactCollector(module)
    result = pm.collect()

    assert result['kernel'] is not None
    assert result['system'] == 'Linux'
    assert result['machine'] == 'x86_64'

# Generated at 2022-06-13 03:15:21.958408
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()

    assert pfc.name == 'platform'


# Generated at 2022-06-13 03:15:26.106768
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x
    assert x.name == 'platform'
    assert sorted(x._fact_ids) == sorted(['system',
                                          'kernel',
                                          'kernel_version',
                                          'machine',
                                          'python_version',
                                          'architecture',
                                          'machine_id'])



# Generated at 2022-06-13 03:15:35.613748
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    class FakeModule(object):
        def get_bin_path(self, name):
            return '/bin/%s' % name

        def run_command(self, args):
            return 0, '', ''

    class FakeFactCollector(BaseFactCollector):
        name = 'fakecollector'
        _fact_ids = set(['fakecollector_fact_id'])

        def collect(self, module=None, collected_facts=None):
            return {'fakecollector_fact_id': 'fake value'}


# Generated at 2022-06-13 03:17:39.573186
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create a instance of class PlatformFactCollector
    platformfact_collector = PlatformFactCollector()

    # Verify if facts are being parsed correctly
    if platformfact_collector.collect()['system'] == platform.system():
        assert True
    else:
        assert False


# Generated at 2022-06-13 03:17:49.403742
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.utils import mock_uname_func

    # Test case for method collect when all the variables are satisfied
    mock_uname = mock_uname_func(platform='linux', release='2', version='#1 SMP Ubuntu 1.1', machine='x86_64', nodename='foo.bar')
    platform_fc = PlatformFactCollector()
    platform_fc.collect()
    # Test case for method collect when platform.system() returns None
    mock_uname = mock_uname_func(platform=None, release='2', version='#1 SMP Ubuntu 1.1', machine='x86_64', nodename='foo.bar')
    platform_fc = PlatformFactCollector()
    platform_fc.collect()
    # Test case for method collect when platform.release() returns None
    mock_

# Generated at 2022-06-13 03:18:00.252612
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform as plat

    class FakeModule(object):
        @staticmethod
        def run_command(cmd):
            if cmd == ["getconf", "MACHINE_ARCHITECTURE"]:
                output = plat.machine()
            elif cmd == ["bootinfo", "-p"]:
                output = plat.machine()
            return 0, output, ""

        @staticmethod
        def get_bin_path(name):
            return name

    class FakeCollector(object):
        def __init__(self, module):
            pass

        def collect(self, module=None, collected_facts=None):
            return {}


# Generated at 2022-06-13 03:18:05.780349
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj_c = PlatformFactCollector()
    assert obj_c.name == "platform"

    assert obj_c._fact_ids == {'system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'}


# Generated at 2022-06-13 03:18:08.887600
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()

    assert platform_facts.name == 'platform'
    assert platform_facts._fact_ids == set(
            ['system', 'kernel', 'kernel_version', 'machine',
             'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:18:13.206463
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()

    assert x != None
    assert x.name == 'platform'
    assert x._fact_ids != None
    assert 'machine_id' in x._fact_ids
    assert 'system' in x._fact_ids
    assert 'kernel' in x._fact_ids
    assert 'kernel_version' in x._fact_ids
    assert 'machine' in x._fact_ids
    assert 'python_version' in x._fact_ids
    assert 'architecture' in x._fact_ids
# --


# Generated at 2022-06-13 03:18:15.685376
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    instance = PlatformFactCollector()
    assert instance.name == 'platform'
    expected_fact_ids = set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])
    assert instance._fact_ids == expected_fact_ids

# Generated at 2022-06-13 03:18:18.621108
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """Test that the PlatformFactCollector class can be instansiated."""
    PlatformFactCollector()


# Generated at 2022-06-13 03:18:25.741795
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, cmd):
            # cmd[0] is the program called
            if cmd[0] == 'getconf':
                data = ['64-bit']
                return 0, '\n'.join(data), ''
            if cmd[0] == 'bootinfo':
                data = ['64-bit']
                return 0, '\n'.join(data), ''
            return 0, '', ''

        def get_bin_path(self, arg):
            if arg == 'bootinfo':
                return '/usr/bin/bootinfo'
            if arg == 'getconf':
                return '/usr/bin/getconf'
            if arg == 'cat':
                return '/bin/cat'

# Generated at 2022-06-13 03:18:35.022779
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create test fixture
    platform_facts = PlatformFactCollector()
    collected_facts = {}
    # Call method
    platform_facts.collect(collected_facts=collected_facts)
    # Assert results
    assert collected_facts['system'] == platform.system()
    assert collected_facts['kernel'] == platform.release()
    assert collected_facts['kernel_version'] == platform.version()
    assert collected_facts['machine'] == platform.machine()
    assert collected_facts['python_version'] == platform.python_version()
    assert collected_facts['fqdn'] == socket.getfqdn()
    assert collected_facts['hostname'] == platform.node().split('.')[0]
    assert collected_facts['nodename'] == platform.node()

# Generated at 2022-06-13 03:21:31.835998
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()

# Generated at 2022-06-13 03:21:33.644505
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector.collect() is not None

# Generated at 2022-06-13 03:21:34.373540
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect(platform)

# Generated at 2022-06-13 03:21:37.301439
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    c = PlatformFactCollector()
    assert set(c.fact_ids) == {'system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'}


# Generated at 2022-06-13 03:21:40.173901
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fc = PlatformFactCollector()
    assert fc.name == "platform"
    assert fc._fact_ids == set(['system',
                                'kernel',
                                'kernel_version',
                                'machine',
                                'python_version',
                                'architecture',
                                'machine_id'])

# Generated at 2022-06-13 03:21:46.541504
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    from ansible.module_utils.facts import module_cache
    from ansible.module_utils.facts.collector import FactsCollector
    facts_collector = FactsCollector(module_cache.module_cache,
                                     module_name='FactsModule',
                                     timeout=10,
                                     collectors=[PlatformFactCollector()])
    facts_collector.collect()
    assert facts_collector.collectors[0].name == 'platform'
    assert set(facts_collector.collectors[0]._fact_ids) == set(['system',
                                                                'kernel',
                                                                'kernel_version',
                                                                'machine',
                                                                'python_version',
                                                                'architecture',
                                                                'machine_id'])

# Generated at 2022-06-13 03:21:51.485314
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import ansible.module_utils.facts.collectors.platform

    # construct a mock class to represent module
    class module:
        def __init__(self):
            self.exit_json = lambda ** kwargs: None
            self.run_command = lambda cmd, check_rc=True: ('', '', 0)
            self.get_bin_path = lambda name, opts=None: name

    # construct a PlatformFactCollector object
    p = ansible.module_utils.facts.collectors.platform.PlatformFactCollector()

    # test collect method
    p.collect(module(), None)

# Generated at 2022-06-13 03:21:56.738979
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:22:02.281361
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_obj = PlatformFactCollector()
    assert platform_obj.name == "platform"
    assert platform_obj._fact_ids == set(['system',
                                          'kernel',
                                          'kernel_version',
                                          'machine',
                                          'python_version',
                                          'architecture',
                                          'machine_id'])


# Generated at 2022-06-13 03:22:08.835827
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    testPlatformFactCollector = PlatformFactCollector()
    testPlatformFactCollector._module = FakeAnsibleModule()
    testPlatformFactCollector._module.run_command = run_command_mock
    testPlatformFactCollector._module.get_bin_path = get_bin_path_mock

    # Testing system = "Linux"
    # Testing machine = "x86_64"
    # Testing userspace_bits = "64"
    sys = "Linux"
    machine = "x86_64"
    userspace_bits = "64"