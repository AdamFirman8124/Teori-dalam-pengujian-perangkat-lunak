

# Generated at 2022-06-13 03:13:10.934231
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Test with a known platform.system()
    module = FakeAnsibleModule()
    collector = PlatformFactCollector()
    platform_facts = collector.collect(module)
    assert platform_facts['system'] == 'Linux'


# Generated at 2022-06-13 03:13:14.013534
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()
    assert pf.name == 'platform'
    assert pf._fact_ids == set(['system',
                                'kernel',
                                'kernel_version',
                                'machine',
                                'python_version',
                                'architecture',
                                'machine_id'])

# Generated at 2022-06-13 03:13:22.139699
# Unit test for method collect of class PlatformFactCollector

# Generated at 2022-06-13 03:13:31.433585
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x

# Generated at 2022-06-13 03:13:41.708934
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    '''
    Test code to validate that PlatformFactCollector.collect()
    functions as expected
    '''
    import os
    import mock
    import sys
    import platform

    # Set up system as we're overriding platform.system() and
    # platform.release()
    sys.platform = 'darwin'
    platform.system = lambda: 'Darwin'
    platform.release = lambda: '10.0.0.0'

    # Create a mock for the module
    module = mock.Mock()

    # Create the PlatformFactCollector object
    pfc = PlatformFactCollector(module=module)

    # The facts that should be returned by calling the collect() method
    # of the PlatformFactCollector class

# Generated at 2022-06-13 03:13:45.501997
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


# Generated at 2022-06-13 03:13:51.669041
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'
    platform = PlatformFactCollector()
    assert platform._fact_ids == set(['system', 'kernel', 'kernel_version',
                                      'machine', 'python_version', 'architecture',
                                      'machine_id'])
    assert 'system' in platform.collect()

# Generated at 2022-06-13 03:13:56.461386
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:14:00.020714
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert collector.platform == 'all'
    assert sorted(collector._fact_ids) == sorted(['system',
                                                  'kernel',
                                                  'kernel_version',
                                                  'machine',
                                                  'python_version',
                                                  'architecture',
                                                  'machine_id'])

# Generated at 2022-06-13 03:14:05.040426
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

# Generated at 2022-06-13 03:15:17.238920
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import sys
    import platform_collector_mock
    class platform_mock:
        system = 'TestSystem'
        release = 'TestRelease'
        version = 'TestVersion'
        machine = 'TestMachine'
        architecture = ('64bit', 'TestArchitecture')
        python_version = 'TestPythonVersion'
        node = 'TestNode'

    platform_collector = platform_collector_mock.PlatformFactCollectorClass()
    platform_collector.platform = platform_mock
    platform_collector.socket = platform_collector_mock.socket_mock()
    platform_collector.socket.getfqdn = lambda x: 'TestFQDN'
    platform_collector.os = platform_collector_mock.os_mock()
    platform_collector.os.path = platform

# Generated at 2022-06-13 03:15:26.185084
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    import ansible.module_utils.facts.system.platform

    _platform_get_base_class_mock = ansible.module_utils.facts.system.platform.BaseFactCollector()
    _platform_get_base_class_mock.get_file_content = lambda x : x

    _platform_get_base_class_mock.get_bin_path = lambda x : 'ok'
    _platform_get_base_class_mock.run_command = lambda x : [0, "Linux", ""]

    _platform_get_base_class_mock.get_file_content = lambda x : x
    _platform_get_base_class_mock.python_version = lambda: "2.7.15"

# Generated at 2022-06-13 03:15:27.035812
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pass

# Generated at 2022-06-13 03:15:36.063694
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    class fake_module(object):
        def get_bin_path(s, x):
            if x == 'getconf':
                return '/usr/bin/getconf'
            elif x == 'bootinfo':
                return '/usr/sbin/bootinfo'
        def run_command(s, x):
            if x[0] == '/usr/bin/getconf':
                return (0, "64-bit PowerPC\n", '')
            elif x[0] == '/usr/sbin/bootinfo':
                return (0, "chrp\n", '')
            else:
                raise Exception('Unexpected command called: ' + x[0])
    pf = PlatformFactCollector()
    ret = pf.collect(fake_module())
    assert ret['architecture'] == 'powerpc64'

# Generated at 2022-06-13 03:15:44.787220
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """ Return platform facts """

    # Construct a mock module
    mock_module = MockModule()

    # Instantiate PlatformFactCollector object
    platform_fact_collector_object = PlatformFactCollector()

    # Execute method platform_fact_collector_object.collect()
    platform_facts = platform_fact_collector_object.collect(module=mock_module)

    # Assert that the value of key 'system' in platform_facts dictionary equal to attribute 'system' of mock_module object
    assert platform_facts['system'] == mock_module.system

    # Assert that the value of key 'machine' in platform_facts dictionary equal to attribute 'machine' of mock_module object
    assert platform_facts['machine'] == mock_module.machine

    # Assert that the value of key 'architecture' in platform_facts dictionary equal to

# Generated at 2022-06-13 03:15:48.559599
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Create instance of class PlatformFactCollector
    platform_collector = PlatformFactCollector()
    # Check that _fact_id is equal to expected value
    assert platform_collector._fact_ids == {'system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id'}

# Generated at 2022-06-13 03:15:53.798720
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform = PlatformFactCollector()
    assert platform.name == 'platform'
    assert platform.collect()['system'] == platform.collect()['system']
    assert 'hostname' in platform.collect()
    assert 'kernel' in platform.collect()
    assert 'kernel_version' in platform.collect()

# Generated at 2022-06-13 03:15:58.953216
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])


# Generated at 2022-06-13 03:16:12.235305
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    instance = PlatformFactCollector()
    assert instance is not None
    assert instance.name == 'platform'
    assert instance._fact_ids == set(['system', 'kernel', 'kernel_version',
                                      'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:16:16.732364
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    my_collector = PlatformFactCollector()

    # test to confirm class attributes were set correctly
    assert my_collector.name == 'platform'
    assert my_collector.fact_ids == set(['system','kernel','kernel_version',
                                         'machine','python_version','architecture',
                                         'machine_id'])

test_PlatformFactCollector()

# Generated at 2022-06-13 03:17:40.756097
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module_mock = AnsibleModuleMock()
    module_mock.params = {}
    module_mock.run_command = run_command_mock
    module_mock.get_bin_path = get_bin_path_mock

    platform_fact_collector = PlatformFactCollector(module_mock)
    result = platform_fact_collector.collect()

    # Check returned facts
    assert result["userspace_bits"] == "64"
    assert result["userspace_architecture"] == "x86_64"
    assert result["system"] == "Linux"
    assert result["kernel"] == "3.10.0-862.el7.x86_64"
    assert result["kernel_version"] == "#1 SMP Mon Mar 26 19:29:39 UTC 2018"

# Generated at 2022-06-13 03:17:46.752603
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

# Generated at 2022-06-13 03:17:49.854237
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()

    # Test for the instance attributes
    assert x.name == 'platform'
    assert x._fact_ids == set(['system', 'kernel', 'kernel_version',
                               'machine', 'python_version', 'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:17:51.525210
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert callable(PlatformFactCollector)

# Generated at 2022-06-13 03:17:56.476101
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


# Generated at 2022-06-13 03:17:57.008071
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pass

# Generated at 2022-06-13 03:17:58.688591
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == "platform"

# Generated at 2022-06-13 03:18:03.923616
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector().collect()
    assert len(platform_facts) > 0
    assert platform_facts["system"] == platform.system()
    assert platform_facts["kernel"] == platform.release()
    assert platform_facts["kernel_version"] == platform.version()
    assert platform_facts["machine"] == platform.machine()
    assert platform_facts["python_version"] == platform.python_version()
    assert platform_facts["fqdn"] == socket.getfqdn()
    assert platform_facts["hostname"] == platform.node().split('.')[0]
    assert platform_facts["nodename"] == platform.node()

# Generated at 2022-06-13 03:18:11.859976
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    input = "Linux test 3.10.0-514.21.2.el7.x86_64 #1 SMP Tue May 23 16:56:59 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux"
    m = re.match('^(?P<system>(\S+)) (?P<nodename>(\S+)) (?P<kernel_release>(\S+)) (?P<kernel_version>([\w+\.]+)) #(?P<architecture>([\w+\.]+)) (?P<processor>(\S+)) (?P<python_version>(\S+)) (?P<kernel_name>([\w+\.]+))$', input)

# Generated at 2022-06-13 03:18:14.946650
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()

    assert platform_fact_collector.name == 'platform'
    expected_fact_ids = set(['system',
                             'kernel',
                             'kernel_version',
                             'machine',
                             'python_version',
                             'architecture',
                             'machine_id'])
    assert platform_fact_collector._fact_ids == expected_fact_ids

# Generated at 2022-06-13 03:21:21.785878
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert set(platform_collector._fact_ids) == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])


# Generated at 2022-06-13 03:21:26.995992
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Given:
    pc = PlatformFactCollector()
    # When:
    actual = pc.collect()
    # Then:

# Generated at 2022-06-13 03:21:28.387389
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect()


# Generated at 2022-06-13 03:21:32.979604
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    test_collector = PlatformFactCollector()
    test_platform_facts = {'machine': 'x86_64',
                           'machine_id': '12345',
                           'system': 'Linux'}

    platform_facts = test_collector.collect(None, test_platform_facts)
    assert platform_facts['machine'] == 'x86_64'
    assert platform_facts['machine_id'] == '12345'
    assert platform_facts['system'] == 'Linux'

# Generated at 2022-06-13 03:21:39.598270
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    class TestModule(object):
        def __init__(self, run_command_args, machine_id=None):
            self.run_command_args = run_command_args
            machine_id_f = tempfile.NamedTemporaryFile(mode="w", delete=False)
            machine_id_f.write(machine_id)
            machine_id_f.close()
            self.machine_id_file = machine_id_f.name

        def get_bin_path(self, executable):
            if executable == "getconf" and self.run_command_args[0] == "GETCONF_CMD":
                return "/bin/getconf"

# Generated at 2022-06-13 03:21:46.172122
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = FakeAnsibleModule()
    fact_collector = PlatformFactCollector(module=module)
    collected_facts = fact_collector.collect(module=module)

# Generated at 2022-06-13 03:21:48.002373
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_fact_collector = PlatformFactCollector()
    platform_fact_collector._get_file_content = get_file_content
    platform_fact_collector.collect()

# Generated at 2022-06-13 03:21:50.295574
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fc = PlatformFactCollector()
    assert fc.name == 'platform'
    assert fc._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine',
                                'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:21:59.823782
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform = PlatformFactCollector()
    assert platform.collect() == dict(system='Linux',
                                      kernel='4.4.0-119-generic',
                                      kernel_version='#143-Ubuntu SMP Mon Apr 2 16:08:24 UTC 2018',
                                      machine='x86_64',
                                      python_version='2.7.14',
                                      fqdn='jenkins.example.com',
                                      hostname='jenkins',
                                      nodename='jenkins.example.com',
                                      domain='example.com',
                                      userspace_bits='64',
                                      architecture='x86_64',
                                      userspace_architecture='x86_64')

# Generated at 2022-06-13 03:22:02.241180
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts.name == 'platform'
    assert platform_facts.collect()['system'] == platform.system()