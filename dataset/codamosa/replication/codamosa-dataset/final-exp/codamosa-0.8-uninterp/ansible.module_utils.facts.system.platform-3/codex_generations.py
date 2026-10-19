

# Generated at 2022-06-13 03:13:10.624260
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create a mock module
    mock_module = MagicMock()
    mock_module.run_command.return_value = (0, 'X86_64', '')
    mock_module.get_bin_path.return_value = 'getconf'
    # Create a PlatformFactCollector
    pfc = PlatformFactCollector()
    # Run the collect method
    fact_data = pfc.collect(module=mock_module)
    assert 'architecture' in fact_data
    assert fact_data['architecture'] == 'X86_64'

# Generated at 2022-06-13 03:13:12.131802
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_collector = PlatformFactCollector()
    collected_facts = platform_collector.collect()
    assert collected_facts

# Generated at 2022-06-13 03:13:12.928438
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x

# Generated at 2022-06-13 03:13:21.376463
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """Test PlatformFactCollector.collect()
    """
    import platform
    import socket
    import re

    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestPlatformFactCollector(PlatformFactCollector):
        name = 'platform'
        _fact_ids = set(['system',
                         'kernel',
                         'kernel_version',
                         'machine',
                         'python_version',
                         'architecture',
                         'machine_id'])


# Generated at 2022-06-13 03:13:30.295367
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import pytest

    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collectors.platform import PlatformFactCollector

    get_file_content_mock = get_file_content
    get_file_content_mock.return_value = "1bb1a9dd00d24b009c8223a7e35efa75"

    fqdn = "testing.ansible.com"
    nodename = "testing"
    system = "Linux"
    kernel = "4.4.5-1-ARCH"
    kernel_version = "#1 SMP PREEMPT Sat Mar 19 15:12:06 CET 2016"
    userspace_bits = "64"
    machine = "x86_64"
    architecture = "x86_64"
    users

# Generated at 2022-06-13 03:13:32.995860
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.collect()['system'] == 'Windows'

# Generated at 2022-06-13 03:13:40.063071
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_collector = PlatformFactCollector()
    collected_facts = platform_collector.collect()
    assert collected_facts["system"] == platform.system()
    assert collected_facts["kernel"] == platform.release()
    assert collected_facts["machine"] == platform.machine()
    assert collected_facts["architecture"] == platform.machine()
    assert collected_facts["python_version"] == platform.python_version()
    assert collected_facts["fqdn"] == socket.getfqdn()
    assert collected_facts["hostname"] == platform.node().split('.')[0]
    assert collected_facts['nodename'] == platform.node()
    assert collected_facts["domain"]
    assert collected_facts["userspace_bits"]
    assert collected_facts["userspace_architecture"]

    # Test machine ID fact


# Generated at 2022-06-13 03:13:47.965106
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    # -------------------------------------------------------
    # Test running on a FreeBSD machine
    # -------------------------------------------------------

    test_system = "FreeBSD"
    test_kernel = "12.0-RELEASE"
    test_machine = "amd64"
    test_platform_system = "FreeBSD"
    test_platform_release = "12.0-RELEASE"
    test_platform_version = "FreeBSD 12.0-RELEASE r354233 GENERIC"
    test_platform_machine = "amd64"
    test_platform_python_version = "2.7.13"
    test_platform_architecture = "amd64"

    test_platform = PlatformFactCollector()

    test_platform.platform_system = test_system
    test_platform.platform_release = test_kernel
    test_platform.platform_machine = test_machine

# Generated at 2022-06-13 03:13:51.422661
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = AnsibleModuleMock()
    platform_facts = PlatformFactCollector.collect(module)

    assert platform_facts
    assert module.run_command.call_count == 0
    assert module.get_bin_path.call_count == 0

# Generated at 2022-06-13 03:14:03.248236
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


# Generated at 2022-06-13 03:15:16.362511
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'

# Generated at 2022-06-13 03:15:20.621332
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

# Generated at 2022-06-13 03:15:24.916829
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

# Generated at 2022-06-13 03:15:34.997485
# Unit test for method collect of class PlatformFactCollector

# Generated at 2022-06-13 03:15:38.704334
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf_collector = PlatformFactCollector()
    assert pf_collector.name == 'platform'
    assert pf_collector._fact_ids == set(['system',
                                          'kernel',
                                          'kernel_version',
                                          'machine',
                                          'python_version',
                                          'architecture',
                                          'machine_id'])


# Generated at 2022-06-13 03:15:40.508779
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'

# Generated at 2022-06-13 03:15:41.100208
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()

# Generated at 2022-06-13 03:15:47.820449
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()

    assert x.name == 'platform'
    assert 'system' in x._fact_ids
    assert 'kernel' in x._fact_ids
    assert 'kernel_version' in x._fact_ids
    assert 'machine' in x._fact_ids
    assert 'python_version' in x._fact_ids
    assert 'fqdn' in x._fact_ids
    assert 'hostname' in x._fact_ids
    assert 'nodename' in x._fact_ids



# Generated at 2022-06-13 03:15:54.001052
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert (PlatformFactCollector.name == 'platform')
    assert (PlatformFactCollector._fact_ids == {'system',
                                                'kernel',
                                                'kernel_version',
                                                'machine',
                                                'python_version',
                                                'architecture',
                                                'machine_id'})

# Generated at 2022-06-13 03:15:58.999336
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
    assert x._platform is platform

# Generated at 2022-06-13 03:17:21.801678
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector_obj = PlatformFactCollector()
    PlatformFactCollector_collect_obj = PlatformFactCollector_obj.collect()
    assert PlatformFactCollector_collect_obj['system'] == platform.system()
    assert PlatformFactCollector_collect_obj['kernel'] == platform.release()
    assert PlatformFactCollector_collect_obj['kernel_version'] == platform.version()
    assert PlatformFactCollector_collect_obj['machine'] == platform.machine()
    assert PlatformFactCollector_collect_obj['python_version'] == platform.python_version()
    assert PlatformFactCollector_collect_obj['fqdn'] == socket.getfqdn()
    assert PlatformFactCollector_collect_obj['hostname'] == platform.node().split('.')[0]

# Generated at 2022-06-13 03:17:27.496286
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert set(collector._fact_ids) == set(['system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id'])



# Generated at 2022-06-13 03:17:29.500176
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x
    assert x.name == 'platform'



# Generated at 2022-06-13 03:17:30.905506
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    assert fact_collector.name == 'platform'

# Generated at 2022-06-13 03:17:34.844360
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

# Generated at 2022-06-13 03:17:38.214770
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()

    fact_subset = set([
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id'
    ])
    assert fact_subset.issubset(fact_collector._fact_ids)

# Generated at 2022-06-13 03:17:38.862466
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector().collect()

# Generated at 2022-06-13 03:17:41.346776
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert frozenset(p._fact_ids) == frozenset(['system',
                                                'kernel',
                                                'kernel_version',
                                                'machine',
                                                'python_version',
                                                'architecture',
                                                'machine_id'])

# Generated at 2022-06-13 03:17:43.392836
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


# Generated at 2022-06-13 03:17:47.657218
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import sys
    import json

    import platform

    platform_facts = PlatformFactCollector().collect()

    assert platform_facts['system'] == platform.system()
    assert platform_facts['kernel'] == platform.release()
    assert platform_facts['kernel_version'] == platform.version()
    assert platform_facts['machine'] == platform.machine()

    assert platform_facts['python_version'] == platform.python_version()

    assert platform_facts['fqdn'] == socket.getfqdn()
    assert platform_facts['hostname'] == platform.node().split('.')[0]
    assert platform_facts['nodename'] == platform.node()

    assert platform_facts['domain'] == '.'.join(platform_facts['fqdn'].split('.')[1:])

    arch_bits = platform.architecture()

# Generated at 2022-06-13 03:20:35.383001
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = AnsibleModuleMock()
    module.run_command = _run_command

    result = PlatformFactCollector.collect(module)

    assert result["system"] == "Linux"
    assert result["kernel"] == "3.10.0-514.6.1.el7.x86_64"
    assert result["kernel_version"] == "#1 SMP Fri Mar 3 00:04:05 UTC 2017"
    assert result["machine"] == "x86_64"
    assert result["python_version"] == "2.7.5"
    assert result["fqdn"] == "node1.com"
    assert result["nodename"] == "node1"
    assert result["hostname"] == "node1"
    assert result["domain"] == "com"
    assert result["userspace_bits"] == "64"


# Generated at 2022-06-13 03:20:43.657831
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    class TestAnsibleModule(object):
        _ansible_module = None
        _ansible_version = None
        _ansible_verbosity = None
        _ansible_no_log = None
        _ansible_debug = None

        def __init__(self, ansible_module):
            self._ansible_module = ansible_module

        def run_command(self, args):
            return ['Uname data', '', '']

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return ['/bin/uname', '']

    class TestAnsibleModuleArgumentSpec(object):
        _module_args = None

        def __init__(self, module_args):
            self._module_args = module_args


# Generated at 2022-06-13 03:20:53.249027
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import CollectorsRunner
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import utils

    class PlatformFactCollector(BaseFactCollector):
        name = 'platform'
        _fact_ids = set(['system',
                         'kernel',
                         'kernel_version',
                         'machine',
                         'python_version',
                         'architecture',
                         'machine_id'])

        def collect(self, module=None, collected_facts=None):
            import platform
            import socket

            # platform.system() can be Linux, Darwin, Java, or Windows
            system = platform.system()
            kernel = platform.release()
            kernel_version = platform.version()
            machine = platform.machine()
           

# Generated at 2022-06-13 03:20:56.935177
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

# Generated at 2022-06-13 03:21:00.989943
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Initialize instance of PlatformFactCollector
    platform_fact_collector = PlatformFactCollector()

    expected_fact_ids = {'system',
                         'kernel',
                         'kernel_version',
                         'machine',
                         'python_version',
                         'architecture',
                         'machine_id'}

    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == expected_fact_ids

# Generated at 2022-06-13 03:21:03.510906
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:21:06.407360
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

# Generated at 2022-06-13 03:21:11.676495
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_collector = PlatformFactCollector()
    platform_facts = platform_collector.collect()

    assert platform_facts['kernel']
    assert platform_facts['architecture']
    assert platform_facts['fqdn']
    assert platform_facts['kernel_version']
    assert platform_facts['machine']
    assert platform_facts['machine_id']
    assert platform_facts['domain']
    assert platform_facts['nodename']
    assert platform_facts['python_version']
    assert platform_facts['system']
    assert platform_facts['userspace_architecture']
    assert platform_facts['userspace_bits']

# Generated at 2022-06-13 03:21:14.939229
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p
    assert p._fact_ids == set([
        'system', 'kernel', 'kernel_version',
        'machine', 'python_version', 'architecture',
        'machine_id'])

# Generated at 2022-06-13 03:21:18.226722
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()

    assert pf.name == 'platform'
    assert set(pf._fact_ids) == set(['system',
                                     'kernel',
                                     'kernel_version',
                                     'machine',
                                     'python_version',
                                     'architecture',
                                     'machine_id'])