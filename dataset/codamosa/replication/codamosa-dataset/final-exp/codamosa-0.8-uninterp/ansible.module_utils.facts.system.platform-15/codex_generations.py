

# Generated at 2022-06-13 03:13:26.447619
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from mock import patch, Mock
    from ansible.module_utils import basic

    import platform as p
    run_command_mock = Mock()

    attrs = {'system.return_value': 'Linux',
             'version.return_value': '2.6.18-164.el5',
             'release.return_value': 'pae',
             'machine.return_value': 'i686',
             'python_version.return_value': '2.7.5',
             'architecture.return_value': ('32bit', 'ELF')}
    p_mock = Mock(**attrs)

    PlatformFactCollector._platform = p_mock
    PlatformFactCollector._socket = Mock()
    PlatformFactCollector._socket.getfqdn.return_value = 'foo'

    PlatformFactCollector

# Generated at 2022-06-13 03:13:31.954436
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert sorted(p._fact_ids) == sorted(set(['system',
                                              'kernel',
                                              'kernel_version',
                                              'machine',
                                              'python_version',
                                              'architecture',
                                              'machine_id']))

# Generated at 2022-06-13 03:13:36.568275
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


# Generated at 2022-06-13 03:13:46.348598
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact = PlatformFactCollector()
    assert isinstance(platform_fact, PlatformFactCollector)

# Generated at 2022-06-13 03:13:57.823199
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = {}
    pfc = PlatformFactCollector()

    # Test for Linux
    platform.system = lambda: 'Linux'
    platform.release = lambda: '4.9.0-6-amd64'
    platform.version = lambda: '#1 SMP Debian 4.9.88-1+deb9u1 (2018-05-07)'
    platform.machine = lambda: 'x86_64'
    platform.python_version = lambda: '2.7.13'
    socket.getfqdn = lambda: 'pavilion.labs.example.org'
    platform.node = lambda: 'pavilion.labs.example.org'
    platform.architecture = lambda: ('64bit', '')

    platform_facts = pfc.collect()


# Generated at 2022-06-13 03:14:08.139492
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = FakeModule()

    platform_system = platform.system()
    platform_system_data_file_name = "unit_tests/ansible_collections/ansible/community/plugins/module_utils/facts/collector/platform/{}.txt".format(platform_system)
    with open(platform_system_data_file_name) as f:
        platform_system_data = f.read()

    cp_platform_system_data_file_name_abs_path = "/etc/issue"
    cp_platform_system_data_file_name = "unit_tests/ansible_collections/ansible/community/plugins/module_utils/facts/collector/platform/{}.txt".format(cp_platform_system_data_file_name_abs_path)

# Generated at 2022-06-13 03:14:10.681947
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


# Generated at 2022-06-13 03:14:16.827527
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == "platform"
    assert platform_fact_collector._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])

# Generated at 2022-06-13 03:14:22.705744
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(0, 'x86_64', None))
    mock_platform = Mock()
    mock_platform.architecture = Mock(side_effect=[('64bit', 'ELF'), ('64bit', 'ELF')])
    platform_fact_collector = PlatformFactCollector(mock_module, mock_platform)
    platform_facts = platform_fact_collector.collect()

    assert platform_facts['architecture'] == 'x86_64'


# Generated at 2022-06-13 03:14:23.341782
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pass

# Generated at 2022-06-13 03:15:06.139561
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    t_platform_fact_collector = PlatformFactCollector()
    assert t_platform_fact_collector.name == 'platform'
    assert t_platform_fact_collector._fact_ids == set(['system',
                                                       'kernel',
                                                       'kernel_version',
                                                       'machine',
                                                       'python_version',
                                                       'architecture',
                                                       'machine_id'])

# Generated at 2022-06-13 03:15:10.872113
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

# Generated at 2022-06-13 03:15:12.134017
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert 'platform' == pfc.name

# Generated at 2022-06-13 03:15:17.636220
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert isinstance(platform_fact_collector, BaseFactCollector)
    assert set(platform_fact_collector.fact_collector._fact_ids) == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:15:19.702468
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """ This is a test stub that exercises the constructor of class PlatformFactCollector()
    """
    PlatformFactCollector()

# Generated at 2022-06-13 03:15:23.586838
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    supported_facts = set(['system',
                           'kernel',
                           'kernel_version',
                           'machine',
                           'python_version',
                           'architecture',
                           'machine_id'])
    p = PlatformFactCollector()
    assert p._fact_ids == supported_facts

# Generated at 2022-06-13 03:15:34.330218
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Set up a mock module object
    class MockModule(object):
        def get_bin_path(self, arg):
            return arg

    class MockFactsCollector(object):
        def __init__(self):
            self.ansible_all_ipv4_addresses = None

    module = MockModule()
    facts_collector = MockFactsCollector()
    platform = PlatformFactCollector(module=module, collected_facts=facts_collector)
    platform_facts = platform.collect()

    assert platform_facts['system'] == platform.system()
    assert platform_facts['kernel'] == platform.release()
    assert platform_facts['kernel_version'] == platform.version()
    assert platform_facts['machine'] == platform.machine()
    assert platform_facts['python_version'] == platform.python_version()


# Generated at 2022-06-13 03:15:40.649998
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector().collect()

    assert isinstance(platform_facts, dict)
    assert 'system' in platform_facts
    assert isinstance(platform_facts['system'], str)
    assert platform_facts['system'].lower() in ['linux', 'darwin', 'java', 'windows']
    assert 'kernel' in platform_facts
    assert isinstance(platform_facts['kernel'], str)
    assert 'kernel_version' in platform_facts
    assert isinstance(platform_facts['kernel_version'], str)
    assert 'machine' in platform_facts
    assert isinstance(platform_facts['machine'], str)
    assert 'python_version' in platform_facts
    assert isinstance(platform_facts['python_version'], str)
    # The following are not required to be present, but if they are

# Generated at 2022-06-13 03:15:48.710563
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert platform.system().lower() != 'java'

    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert sorted(x._fact_ids) == sorted(['system',
                                          'kernel',
                                          'kernel_version',
                                          'machine',
                                          'python_version',
                                          'architecture',
                                          'machine_id'])

    data = x.collect()
    assert isinstance(data, dict)
    assert 'system' in data
    assert 'kernel' in data
    assert 'python_version' in data
    assert 'fqdn' in data
    assert 'hostname' in data
    assert 'domain' in data

# Generated at 2022-06-13 03:15:54.749482
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platformCollector = PlatformFactCollector()
    assert platformCollector
    assert platformCollector.name == 'platform'
    assert platformCollector._fact_ids == set(['system',
                                               'kernel',
                                               'kernel_version',
                                               'machine',
                                               'python_version',
                                               'architecture',
                                               'machine_id'])

# Generated at 2022-06-13 03:17:21.476236
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_fact_collector = PlatformFactCollector()

    result = platform_fact_collector.collect()

    assert type(result) is dict
    assert sorted(result.keys()) == sorted(['system', 'kernel_version', 'machine_id', 'nodename', 'fqdn', 'hostname', 'kernel', 'domain', 'python_version', 'architecture', 'userspace_bits', 'machine', 'userspace_architecture'])

# Generated at 2022-06-13 03:17:22.491444
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'

# Generated at 2022-06-13 03:17:25.710370
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
    assert x.collect()

# Generated at 2022-06-13 03:17:27.191352
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert collector.fact_class == 'platform'

# Generated at 2022-06-13 03:17:28.301877
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platformFactCollector = PlatformFactCollector()
    assert platformFactCollector is not None

# Generated at 2022-06-13 03:17:30.195603
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()

    assert pfc
    assert isinstance(pfc, PlatformFactCollector)

# Generated at 2022-06-13 03:17:32.387953
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    from ansible.module_utils.facts import collector

    fact_collector_class = collector.get_fact_collector_class('platform')
    assert fact_collector_class == PlatformFactCollector

# Generated at 2022-06-13 03:17:35.599991
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector('test', {})
    assert pfc.name == 'test'
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                     'architecture',
                                     'machine_id'])

# Generated at 2022-06-13 03:17:38.583597
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """Test creation of PlatformFactCollector instance
    """
    x = PlatformFactCollector()
    assert isinstance(x, PlatformFactCollector)
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:17:42.991082
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert hasattr(x, 'name')
    assert hasattr(x, 'get_facts')
    assert x.name == 'platform'
    assert x._fact_ids == {'system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'}

# Generated at 2022-06-13 03:20:42.734076
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Executing the constructor should simply return an object of type PlatformFactCollector as this class is a subclass of BaseFactCollector
    platform_collector_object = PlatformFactCollector()
    assert isinstance(platform_collector_object, PlatformFactCollector)

# Generated at 2022-06-13 03:20:45.851638
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector().collect()
    assert platform_facts['architecture'] == platform.machine()
    assert platform_facts['userspace_bits'] in ['32', '64']
    assert platform_facts['kernel_version'] == platform.version()
    assert platform_facts['kernel'] == platform.release()

# Generated at 2022-06-13 03:20:50.418084
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert 'system' in pfc._fact_ids
    assert 'kernel' in pfc._fact_ids
    assert 'kernel_version' in pfc._fact_ids
    assert 'machine' in pfc._fact_ids
    assert 'python_version' in pfc._fact_ids
    assert 'architecture' in pfc._fact_ids
    assert 'machine_id' in pfc._fact_ids
    assert pfc._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])
    assert pfc.name == 'platform'


# Generated at 2022-06-13 03:20:58.377172
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    fake_module = type('ansible.module_utils.facts.collector.platform', (), {})()
    fake_module.run_command = lambda *args, **kwargs: (0, '', '')
    fake_module.get_bin_path = lambda command: None
    fake_collector = PlatformFactCollector(fake_module)
    real_platform_facts = platform.uname()
    fake_platform_facts = fake_collector.collect()

    assert fake_platform_facts['kernel'] == real_platform_facts.release
    assert fake_platform_facts['system'] == real_platform_facts.system
    assert fake_platform_facts['machine'] == real_platform_facts.machine
    assert fake_platform_facts['python_version'] == real_platform_facts.version

# Generated at 2022-06-13 03:21:05.592109
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """Unit test for method collect of class PlatformFactCollector"""

    import ansible.module_utils.facts.collector.platform
    from ansible.module_utils.facts import timeout

    class ModuleMock(object):
        def __init__(self, run_command_result, get_bin_path_result):
            self.run_command_result = run_command_result
            self.get_bin_path_result = get_bin_path_result


# Generated at 2022-06-13 03:21:11.002904
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # When I create a PlatformFactCollector object
    x = PlatformFactCollector()
    # I should see that the name is 'platform'
    assert x.name == 'platform'
    # And I should see that it has a list of fact names
    assert sorted(x._fact_ids) == [u'architecture',
                                   u'domain',
                                   u'fqdn',
                                   u'hostname',
                                   u'kernel',
                                   u'kernel_version',
                                   u'machine',
                                   u'machine_id',
                                   u'nodename',
                                   u'python_version',
                                   u'system',
                                   u'userspace_architecture',
                                   u'userspace_bits']


# Generated at 2022-06-13 03:21:15.789496
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


# Generated at 2022-06-13 03:21:20.769248
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    assert fact_collector.name == 'platform'
    assert 'system' in fact_collector._fact_ids
    assert 'kernel' in fact_collector._fact_ids
    assert 'kernel_version' in fact_collector._fact_ids
    assert 'machine' in fact_collector._fact_ids
    assert 'python_version' in fact_collector._fact_ids
    assert 'architecture' in fact_collector._fact_ids
    assert 'machine_id' in fact_collector._fact_ids

# Generated at 2022-06-13 03:21:26.316251
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_obj = PlatformFactCollector()
    platform_facts = platform_obj.collect()
    check_list = {'architecture': ['i386', 'x86_64', 'sparc'], 'kernel_version': ['5.7', '6', '7'], 'kernel': ['Darwin', 'Linux', 'SunOS'], 'system': ['Darwin', 'Linux', 'SunOS'], 'python_version': ['3.4.0', '3.8.0', '3.9.0'], 'machine': ['i386', 'x86_64', 'sparc'], }
    for key, value in check_list.items():
        assert platform_facts[key] in value

# Generated at 2022-06-13 03:21:30.348203
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    # method name: collect()
    assert hasattr(pfc, 'collect')
    # object's attribute name: name
    assert hasattr(pfc, 'name')
    # object's attribute name: _fact_ids
    assert isinstance(pfc._fact_ids, set)