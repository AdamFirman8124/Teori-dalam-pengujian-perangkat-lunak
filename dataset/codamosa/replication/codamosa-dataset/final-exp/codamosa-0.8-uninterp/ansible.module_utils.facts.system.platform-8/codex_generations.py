

# Generated at 2022-06-13 03:13:08.080743
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts
    assert platform_facts.name == 'platform'
    assert platform_facts._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine',
                                            'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:13:17.254722
# Unit test for method collect of class PlatformFactCollector

# Generated at 2022-06-13 03:13:23.308028
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert len(pfc._fact_ids) == 9
    assert set(pfc._fact_ids) == set(['system',
                                      'kernel',
                                      'kernel_version',
                                      'machine',
                                      'python_version',
                                      'architecture',
                                      'machine_id'])

# Generated at 2022-06-13 03:13:26.137637
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'
    assert PlatformFactCollector._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:13:32.619322
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

# Unit tests for PlatformFactCollector.collect(module, collected_facts)

# Generated at 2022-06-13 03:13:35.073712
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids is not None
    assert 'system' in x._fact_ids
    assert x._collect_subset is None

# Generated at 2022-06-13 03:13:44.169596
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """Generates a fact datastructure with all the platform related data
       that can be collected."""
    # initialize the collector instance
    pfc = PlatformFactCollector()

    # call the collect method
    fact = pfc.collect()

    print("Platform fact %s" % fact)

    # assert that we have a system fact
    assert 'system' in fact

    # assert that we have a kernel fact
    assert 'kernel' in fact

    # assert that we have a kernel version fact
    assert 'kernel_version' in fact

    # assert that we have a machine fact
    assert 'machine' in fact

    # assert that we have a python version fact
    assert 'python_version' in fact

    # assert that we have a architecture fact
    assert 'architecture' in fact

# Generated at 2022-06-13 03:13:49.973796
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    assert(fact_collector.name == 'platform')
    assert('kernel' in fact_collector._fact_ids)
    assert(len(fact_collector._fact_ids) == 5)

# Generated at 2022-06-13 03:13:54.474375
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])
    assert isinstance(x._fact_ids, set)


# Generated at 2022-06-13 03:13:58.674997
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'

    # Assert the attrs are correctly set
    assert p._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])


# Generated at 2022-06-13 03:15:17.594086
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == "platform"
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:15:20.046853
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'


# Generated at 2022-06-13 03:15:27.535602
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    try:
        import platform
        import socket
        import re
    except ImportError:
        raise ImportError('The platform and socket modules are not available')

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, arg1):
            return arg1

        def run_command(self, arg1):
            return [0, arg1[0],'error']

    class MockSocket(object):
        def getfqdn(self):
            return 'test1.example.net'

    class MockPlatform(object):
        def __init__(self):
            self.system = 'Linux'
            self.release = 'testrelease'
            self.version = 'testversion'
            self.machine = 'x86_64'
            self.python_version

# Generated at 2022-06-13 03:15:33.081374
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert set(platform_fact_collector._fact_ids) == set(['system',
                                                          'kernel',
                                                          'kernel_version',
                                                          'machine',
                                                          'python_version',
                                                          'architecture',
                                                          'machine_id'])
    assert platform_fact_collector.name == 'platform'

# Generated at 2022-06-13 03:15:39.015808
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """
    This is a minimal test.  We might want a more complete unit test.
    """
    fact_collector = PlatformFactCollector()
    assert fact_collector.name == 'platform'
    assert sorted(fact_collector._fact_ids) == sorted(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

    facts_ret = fact_collector.collect()

    assert sorted(facts_ret.keys()) == sorted(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'fqdn', 'hostname', 'nodename', 'domain', 'userspace_bits'])

    assert facts_ret['system'] == 'Linux'
    assert facts_ret['machine'] == 'x86_64'

# Generated at 2022-06-13 03:15:40.145636
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'

# Generated at 2022-06-13 03:15:49.183811
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector.system import PlatformFactCollector

    # Initialization of collector
    platform_collector = PlatformFactCollector()

    # Initialization of facts collector
    facts_collector = FactsCollector()

    # Collect facts
    collected_facts = facts_collector.collect(module=None,
                                              collected_facts=None)

    # Get collected platform facts
    result = platform_collector.collect(module=None,
                                        collected_facts=collected_facts)

    # Result should not be empty
    assert len(result) > 0

    # Presence of expected platform facts
    assert 'system' in result
    assert 'kernel' in result
    assert 'kernel_version' in result
    assert 'machine'

# Generated at 2022-06-13 03:15:53.135568
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """This is a test to verify that we can create an instance of PlatformFactCollector."""
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector is not None

# Generated at 2022-06-13 03:15:56.972556
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()

    assert hasattr(fact_collector, 'collect')
    assert fact_collector.name == "platform"
    assert fact_collector.platform_linux == False

# Generated at 2022-06-13 03:15:58.369466
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x
    assert x.collect()

# Generated at 2022-06-13 03:17:24.466958
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert platform_collector.collect()

# Generated at 2022-06-13 03:17:29.647494
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    actual_platform_facts = PlatformFactCollector().collect()
    assert actual_platform_facts['system'] == 'Linux'
    assert actual_platform_facts['kernel'] == '2.6.32-358.el6.x86_64'
    assert actual_platform_facts['kernel_version'] == '#1 SMP Fri Feb 22 00:31:26 UTC 2013'
    assert actual_platform_facts['machine'] == 'x86_64'
    assert actual_platform_facts['python_version'] == '2.6.6'
    assert actual_platform_facts['fqdn'] == 'localhost.localdomain'
    assert actual_platform_facts['hostname'] == 'localhost'
    assert actual_platform_facts['nodename'] == 'localhost'

# Generated at 2022-06-13 03:17:32.207303
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    try:
        import ansible.module_utils.facts.system.platform.PlatformFactCollector as platform_module
    except ImportError:
        raise

    cur_platform = platform_module.PlatformFactCollector()
    cur_platform.collect()

# Generated at 2022-06-13 03:17:38.948404
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    result = {
        'system': 'Linux',
        'kernel': '3.10.0-327.el7.x86_64',
        'kernel_version': '#1 SMP Thu Oct 29 17:29:29 EDT 2015',
        'machine': 'x86_64',
        'python_version': '2.7.5',
        'fqdn': 'docker.example.local',
        'hostname': 'docker',
        'nodename': 'docker.example.local',
        'domain': 'example.local',
        'userspace_bits': '64',
        'architecture': 'x86_64',
        'userspace_architecture': 'x86_64',
        'machine_id': '1234567890abcdef1234567890abcdef'
    }
    collector = PlatformFact

# Generated at 2022-06-13 03:17:48.343908
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """Tests if platform fact is collected correctly"""
    facts = dict()
    pc = PlatformFactCollector(dict(), facts)
    result = pc.collect()
    assert result.get("system") == platform.system()
    assert result.get("kernel") == platform.release()
    assert result.get("kernel_version") == platform.version()
    assert result.get("machine") == platform.machine()
    assert result.get("python_version") == platform.python_version()
    assert result.get("fqdn") == socket.getfqdn()
    assert result.get("hostname") == platform.node().split('.')[0]
    assert result.get("nodename") == platform.node()

# Generated at 2022-06-13 03:17:49.634790
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """Platform Fact Collector - Instantiation test"""
    pfc = PlatformFactCollector()
    assert isinstance(pfc, PlatformFactCollector)


# Generated at 2022-06-13 03:17:52.855238
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids is not None

# Generated at 2022-06-13 03:17:57.572130
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()

    assert platform_facts.name == 'platform'
    assert platform_facts._fact_ids == set(['system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id'])



# Generated at 2022-06-13 03:17:59.551748
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector().name == 'platform'
    assert len(PlatformFactCollector()._fact_ids) > 0



# Generated at 2022-06-13 03:18:03.083342
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    actual_result = PlatformFactCollector.name
    expected_result = 'platform'
    assert actual_result == expected_result

    actual_result = PlatformFactCollector()._fact_ids
    expected_result = set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])
    assert actual_result == expected_result


# Generated at 2022-06-13 03:21:14.787693
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert sorted(collector._fact_ids) == sorted(['system',
                                                  'kernel',
                                                  'kernel_version',
                                                  'machine',
                                                  'python_version',
                                                  'architecture',
                                                  'machine_id'])


# Generated at 2022-06-13 03:21:21.586801
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform

    # Override platform.system() - return 'Linux'
    platform_system_real = platform.system
    platform.system = lambda: 'Linux'
    platform_release_real = platform.release
    platform.release = lambda: '3.10.0-514.10.2.el7.x86_64'
    platform_version_real = platform.version
    platform.version = lambda: '#1 SMP Wed Mar 15 11:44:59 EDT 2017'
    platform_machine_real = platform.machine
    platform.machine = lambda: 'x86_64'
    platform_node_real = platform.node
    platform.node = lambda: 'test.example.com'
    socket_getfqdn_real = socket.getfqdn

# Generated at 2022-06-13 03:21:29.053458
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import socket
    import re

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    class MockModule(object):
        def run_command(self, cmd):
            return 0, "", ""

    class MockPlatform(object):
        @property
        def machine(self):
            return "x86_64"

        @property
        def python_version(self):
            return "2.7.0"

        @property
        def release(self):
            return "2.6.32-504.8.1.el6.x86_64"

        @property
        def system(self):
            return "Linux"


# Generated at 2022-06-13 03:21:30.276321
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    print(x.collect())



# Generated at 2022-06-13 03:21:33.773592
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    class_inst = PlatformFactCollector()
    assert class_inst.name == "platform"
    assert class_inst._fact_ids == set(['system',
                                        'kernel',
                                        'kernel_version',
                                        'machine',
                                        'python_version',
                                        'architecture',
                                        'machine_id'])

# Generated at 2022-06-13 03:21:35.041592
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    plc = PlatformFactCollector()
    assert plc.name == 'platform', plc.name

# Generated at 2022-06-13 03:21:37.877718
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert set(platform_fact_collector._fact_ids) == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:21:40.938808
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()

    assert x.collect() == {
        'system': 'Linux',
        'kernel': '3.10.0-693.el7.x86_64',
        'architecture': 'x86_64',
        'machine': 'x86_64',
        'python_version': '2.7.5',
    }

# Generated at 2022-06-13 03:21:43.996217
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

# Generated at 2022-06-13 03:21:47.420561
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