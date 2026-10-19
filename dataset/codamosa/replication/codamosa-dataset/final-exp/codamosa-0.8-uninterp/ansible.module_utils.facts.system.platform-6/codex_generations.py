

# Generated at 2022-06-13 03:13:07.110932
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert len(pfc._fact_ids) == 9

# Generated at 2022-06-13 03:13:16.430691
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """
    Test the collect method of PlatformFactCollector class
    """
    import platform
    import ansible.module_utils.facts.collectors.platform

    # Create instances of ModuleUtils and PlatformFactCollector
    platform_module_utils = ansible.module_utils.facts.collectors.platform.ModuleUtils()
    platform_fact_collector = ansible.module_utils.facts.collectors.platform.PlatformFactCollector()

    # Create return values for platform.system(), platform.release(), platform.version()
    # platform.machine(), platform.python_version()
    platform_system_return_val = "Linux"
    platform_release_return_val = "4.14.129-103.105.amzn2.x86_64"

# Generated at 2022-06-13 03:13:21.209790
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids is not None
    assert len(platform_fact_collector._fact_ids) == 9

# Generated at 2022-06-13 03:13:30.141973
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

# Generated at 2022-06-13 03:13:35.376660
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    from ansible.module_utils.facts import FactCollector

    # instantiate the module
    fact_collector = FactCollector()

    # Run the module
    result = fact_collector.get_facts()

    # Assert some results
    assert 'system' in result
    assert 'kernel' in result
    assert 'kernel_version' in result
    assert 'machine' in result
    assert 'architecture' in result

# Generated at 2022-06-13 03:13:50.640802
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    assert fact_collector.collect() == {
        'system': platform.system(),
        'kernel': platform.release(),
        'machine': platform.machine(),
        'kernel_version': platform.version(),
        'python_version': platform.python_version(),
        'fqdn': socket.getfqdn().split('.')[-1],
        'hostname': platform.node().split('.')[0],
        'nodename': platform.node()
    }

# Generated at 2022-06-13 03:13:51.505057
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()


# Generated at 2022-06-13 03:14:00.180382
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.facts.collector.platform import PlatformFactCollector

    def my_get_file_content(file_name):
        return "21b2f1af84d841f06e8a9f9c2b44be98"

    def my_get_bin_path(binary, required=False):
        if binary == 'getconf':
            return '/usr/bin/getconf'
        elif binary == 'bootinfo':
            return '/usr/sbin/bootinfo'
        else:
            return None

    def my_run_command(cmd, check_rc=True):
        if cmd[0] == '/usr/bin/getconf':
            return

# Generated at 2022-06-13 03:14:01.571188
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector()
    assert hasattr(obj, '_fact_ids')

# Generated at 2022-06-13 03:14:04.300731
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert 'system' in platform_fact_collector._fact_ids



# Generated at 2022-06-13 03:14:49.837967
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



# Generated at 2022-06-13 03:14:54.744668
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

# Generated at 2022-06-13 03:15:00.444213
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    fact_collector = PlatformFactCollector()
    facts = fact_collector.collect()

    # Arch
    assert facts['architecture'] is not None

    # Hostname
    assert facts['hostname'] is not None

    # Userspace Arch
    assert facts['userspace_architecture'] is not None

    # System
    assert facts['system'] is not None

    # Kernel
    assert facts['kernel'] is not None

    # Kernel Version
    assert facts['kernel_version'] is not None

    # Domain
    assert facts['domain'] is not None

    # FQDN
    assert facts['fqdn'] is not None

    # Nodename
    assert facts['nodename'] is not None

# Generated at 2022-06-13 03:15:08.365336
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    '''
    Unit test for method collect of class PlatformFactCollector
    '''
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collectors.platform.platform import PlatformFactCollector

    # Create a system fact object
    platform_collector = PlatformFactCollector()

    # Create a collector object
    fake_module = object()
    collector_obj = Collector(fake_module)

    platform_collector.collect(fake_module, collector_obj)

    # Asserts the fact 'kernel' is not None
    assert collector_obj.get_fact('kernel') is not None

    return True

# Generated at 2022-06-13 03:15:12.951747
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Verify that the correct dictionary is returned
    collector = PlatformFactCollector()
    facts = collector.collect()
    assert facts['system'] == platform.system()
    assert facts['kernel'] == platform.release()
    assert facts['kernel_version'] == platform.version()
    assert facts['machine'] == platform.machine()
    assert facts['python_version'] == platform.python_version()


# Generated at 2022-06-13 03:15:23.586685
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """Unit test for method collect of class PlatformFactCollector."""
    # Test for the 'architecture' fact
    # x86_64
    platform = PlatformFactCollector()
    machine = 'x86_64'
    arch_bits = '64bit'
    result = platform.collect(machine=machine,
                              arch_bits=arch_bits)
    assert result['architecture'] == 'x86_64'
    assert result['userspace_architecture'] == 'x86_64'
    assert result['userspace_bits'] == '64'

    # i86pc
    platform = PlatformFactCollector()
    machine = 'i86pc'
    arch_bits = '64bit'
    result = platform.collect(machine=machine,
                              arch_bits=arch_bits)

# Generated at 2022-06-13 03:15:25.085221
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # This is just to test if the constructor of PlatformFactCollector class
    # works as expected
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'

# Generated at 2022-06-13 03:15:28.138436
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert type(platform_facts) == PlatformFactCollector
    assert platform_facts.name == 'platform'
    assert platform_facts._fact_ids == set(['system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id'])

# Generated at 2022-06-13 03:15:36.309605
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from tests.unit.module_utils.facts import mock_module


# Generated at 2022-06-13 03:15:41.540696
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert type(pfc) is PlatformFactCollector
    assert pfc.name == "platform"
    assert type(pfc._fact_ids) is set
    assert len(pfc._fact_ids) == 9

# Generated at 2022-06-13 03:16:43.002301
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_info = PlatformFactCollector.collect(BaseFactCollector.setup_module({}))
    assert platform_info['kernel'] == platform.release()
    assert platform_info['system'] == platform.system()
    assert platform_info['machine'] == platform.machine()
    assert 'python_version' in platform_info
    assert 'architecture' in platform_info


# Generated at 2022-06-13 03:16:46.199769
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])
    assert platform_fact_collector._legacy_fact_ids == set()

# Generated at 2022-06-13 03:16:48.026875
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():

    p = PlatformFactCollector()

    assert p.name == 'platform'
    assert p._fact_ids == set(['system', 'kernel',
                               'kernel_version', 'machine',
                               'python_version', 'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:16:51.014211
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    collector = PlatformFactCollector()
    facts = collector.collect()
    assert isinstance(facts['nodename'], str)
    assert isinstance(facts['architecture'], str)
    assert facts['architecture'] in ['i386', 'i686', 'x86_64']
    assert isinstance(facts['machine'], str)

# Generated at 2022-06-13 03:17:01.055863
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collectors import collector_registry

    PlatformFactCollector.populate()
    assert PlatformFactCollector.name == 'platform'
    assert 'system' in PlatformFactCollector._fact_ids
    assert 'kernel' in PlatformFactCollector._fact_ids
    assert 'kernel_version' in PlatformFactCollector._fact_ids
    assert 'machine' in PlatformFactCollector._fact_ids
    assert 'python_version' in PlatformFactCollector._fact_ids
    assert 'architecture' in PlatformFactCollector._fact_ids
    assert 'machine_id' in PlatformFactCollector._fact_ids

    assert isinstance(PlatformFactCollector.collect(), dict)

    for collector in collector_registry.values():
        assert collector.collect() is not None


# Generated at 2022-06-13 03:17:03.073024
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf_collector = PlatformFactCollector()
    assert pf_collector.name == 'platform'

# Generated at 2022-06-13 03:17:05.554251
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PFC = PlatformFactCollector()
    res = PFC.collect()

    assert set(res.keys()) == PFC._fact_ids

# Generated at 2022-06-13 03:17:06.608901
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()


# Generated at 2022-06-13 03:17:07.533773
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()


# Generated at 2022-06-13 03:17:08.907785
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector()
    platform_facts.collect()

# Generated at 2022-06-13 03:19:30.617999
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector._fact_ids == {'system',
                                               'kernel',
                                               'kernel_version',
                                               'machine',
                                               'python_version',
                                               'architecture',
                                               'machine_id'}

# Generated at 2022-06-13 03:19:35.467706
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Create an instance
    platform_collector = PlatformFactCollector()

    # Test parameters
    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:19:45.932860
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector().collect()
    assert platform_facts['python_version'] == platform.python_version()
    assert platform_facts['hostname'] == platform.node().split('.')[0]
    assert platform_facts['nodename'] == platform.node()
    assert platform_facts['domain'] == '.'.join(platform_facts['fqdn'].split('.')[1:])
    # Note that arch_bits is the bits for userspace and architecture is for the platform
    # This is different for Solaris, 32-bit userspace on a 64-bit platform is possible there
    # But that's a special case, which we should not treat as the norm
    assert platform_facts['userspace_bits'] in ('32', '64')
    assert platform_facts['architecture'] == platform.machine()

# Generated at 2022-06-13 03:19:55.662329
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_fact_collector = PlatformFactCollector()
    platform_facts = platform_fact_collector.collect()

    assert platform_facts
    assert platform_facts['system'] == platform.system()
    assert platform_facts['kernel'] == platform.release()
    assert platform_facts['kernel_version'] == platform.version()
    assert platform_facts['machine'] == platform.machine()
    assert platform_facts['python_version'] == platform.python_version()
    assert platform_facts['fqdn'] == socket.getfqdn()
    assert platform_facts['hostname'] == platform.node().split('.')[0]
    assert platform_facts['nodename'] == platform.node()
    assert platform_facts['domain'] == '.'.join(platform_facts['fqdn'].split('.')[1:])

# Generated at 2022-06-13 03:20:05.061595
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.utils import get_file_content

    # mock get_file_content
    get_file_content_orig = get_file_content
    get_file_content_mock = lambda *args, **kwargs: "machine_id"

    facts_collector = FactsCollector()
    platform_collector = PlatformFactCollector()

    platform_collector.collect()
    collect_result = facts_collector.get_facts()

    # restore get_file_content
    get_file_content = get_file_content_orig

    assert "machine_id" in collect_result['platform']
    assert collect_result['platform']['machine_id'] == "machine_id"

# Generated at 2022-06-13 03:20:08.943013
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert sorted(platform_fact_collector._fact_ids) == sorted(['system',
                                                                'kernel',
                                                                'kernel_version',
                                                                'machine',
                                                                'python_version',
                                                                'architecture'])

# Generated at 2022-06-13 03:20:14.118224
# Unit test for method collect of class PlatformFactCollector

# Generated at 2022-06-13 03:20:25.157262
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_fact_collector = PlatformFactCollector()

    platform_facts = platform_fact_collector.collect()

    assert platform_facts["system"] == platform.system()
    assert platform_facts["kernel"] == platform.release()
    assert platform_facts["kernel_version"] == platform.version()
    assert platform_facts["machine"] == platform.machine()
    assert platform_facts["python_version"] == platform.python_version()
    assert platform_facts["fqdn"] == socket.getfqdn()
    assert platform_facts["hostname"] == platform.node().split('.')[0]
    assert platform_facts["nodename"] == platform.node()
    assert platform_facts["domain"] == '.'.join(platform_facts['fqdn'].split('.')[1:])

# Generated at 2022-06-13 03:20:28.120297
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    plat_col = PlatformFactCollector()
    assert len(plat_col._fact_ids) == 8
    assert plat_col._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])
    assert plat_col.name == 'platform'


# Generated at 2022-06-13 03:20:38.633038
# Unit test for method collect of class PlatformFactCollector