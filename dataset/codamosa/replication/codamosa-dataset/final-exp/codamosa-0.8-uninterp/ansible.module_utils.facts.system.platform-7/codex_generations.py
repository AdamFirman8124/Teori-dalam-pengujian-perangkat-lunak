

# Generated at 2022-06-13 03:13:09.045263
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == {'system', 'kernel', 'kernel_version', 'machine',
                                                 'python_version', 'architecture', 'machine_id'}

# Generated at 2022-06-13 03:13:19.261658
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts.name == 'platform'
    assert platform_facts._fact_ids is not None

# Generated at 2022-06-13 03:13:24.745778
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector(module=None)

    assert not obj.collect(module=None, collected_facts=None) is None
    assert obj._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])
    assert obj.name == "platform"
    assert obj.condition == ""

# Generated at 2022-06-13 03:13:27.231281
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector = PlatformFactCollector()

    facts = PlatformFactCollector.collect()
    assert facts['system'] is not None
    assert facts['kernel'] is not None
    assert facts['kernel_version'] is not None
    assert facts['machine'] is not None
    assert facts['python_version'] is not None
    assert facts['architecture'] is not None
    assert 'machine_id' in facts

# Generated at 2022-06-13 03:13:32.036938
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert p.fact_ids == set(['system',
                              'kernel',
                              'kernel_version',
                              'machine',
                              'python_version',
                              'architecture',
                              'machine_id'])


# Generated at 2022-06-13 03:13:38.174413
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    dut = PlatformFactCollector()
    assert dut.name == 'platform'
    #pylint: disable=too-many-boolean-expressions
    assert dut._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:13:41.953638
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()

    assert set(platform_facts._fact_ids) == set(['system',
                                                 'kernel',
                                                 'kernel_version',
                                                 'machine',
                                                 'python_version',
                                                 'architecture',
                                                 'machine_id'])


# Generated at 2022-06-13 03:13:49.192435
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self.run_command_result = (0, "", "")
            self.run_command_exception = None
            self.run_command_calls = []

        def get_bin_path(self, executable):
            return "path"

        def run_command(self, args, executable=None, check_rc=True, close_fds=True, cwd=None, data=None, binary_data=False, path_prefix=None, env=None, use_unsafe_shell=False):
            self.run_command_calls.append(args)
            if self.run_command_exception:
                raise self.run_command_exception
            else:
                return self.run_command_result

    # Test case 1: test X

# Generated at 2022-06-13 03:13:58.771473
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import pytest
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.platform import PlatformFactCollector
    import os

    platform.uname = lambda: ('Linux', 'test.example.com', '5.5.5-1-MANJARO',
                          '#1 SMP PREEMPT Sun Mar 8 20:40:53 UTC 2020',
                          'x86_64', 'x86_64')
    platform.system = lambda: 'Linux'
    platform.release = lambda: '5.5.5-1-MANJARO'
    platform.version = lambda: '#1 SMP PREEMPT Sun Mar 8 20:40:53 UTC 2020'
   

# Generated at 2022-06-13 03:14:04.631953
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    _platform_facts = PlatformFactCollector().collect()

    assert _platform_facts['system'] == platform.system()
    assert _platform_facts['kernel'] == platform.release()
    assert _platform_facts['kernel_version'] == platform.version()
    assert _platform_facts['machine'] == platform.machine()
    assert _platform_facts['python_version'] == platform.python_version()

# Generated at 2022-06-13 03:14:51.792248
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



# Generated at 2022-06-13 03:14:55.837625
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert p._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])


if __name__ == '__main__':
    test_PlatformFactCollector()

# Generated at 2022-06-13 03:14:59.358679
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    #Test with module argument and collected_facts=None
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])



# Generated at 2022-06-13 03:15:03.344859
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()
    assert pf
    assert pf.name == 'platform'
    assert sorted(pf.collect().keys()) == sorted(pf._fact_ids)

# Generated at 2022-06-13 03:15:07.075070
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == "platform"
    assert "_fact_ids" in pfc.__dict__
    assert pfc._fact_ids == set(['system', 'kernel', 'kernel_version',
                                 'machine', 'python_version',
                                 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:15:15.275056
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    platform_facts = PlatformFactCollector().collect()
    assert platform_facts["system"] == platform.system()
    assert platform_facts["kernel"] == platform.release()
    assert platform_facts["kernel_version"] == platform.version()
    assert platform_facts["machine"] == platform.machine()
    assert platform_facts["python_version"] == platform.python_version()
    assert platform_facts["fqdn"] == socket.getfqdn()
    assert platform_facts["hostname"] == platform.node().split('.')[0]
    assert platform_facts["nodename"] == platform.node()
    assert platform_facts["domain"] == '.'.join(platform_facts['fqdn'].split('.')[1:])
    arch_bits = platform.architecture()[0]
    assert platform_

# Generated at 2022-06-13 03:15:21.113404
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector_instance = PlatformFactCollector()
    assert platform_fact_collector_instance.name == 'platform'
    assert platform_fact_collector_instance._fact_ids == set(['system',
                                                               'kernel',
                                                               'kernel_version',
                                                               'machine',
                                                               'python_version',
                                                               'architecture',
                                                               'machine_id'])

# Generated at 2022-06-13 03:15:29.138787
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    res_get_file_content = ['123456789012345678901234567890123456']
    fc = PlatformFactCollector(res_get_file_content)
    res = fc.collect()

# Generated at 2022-06-13 03:15:32.270332
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == {'system', 'kernel', 'kernel_version', 'machine',
        'python_version', 'architecture', 'machine_id'}

# Generated at 2022-06-13 03:15:35.806063
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'
    assert PlatformFactCollector._fact_ids == set(['system',
                                                   'kernel',
                                                   'kernel_version',
                                                   'machine',
                                                   'python_version',
                                                   'architecture',
                                                   'machine_id'])

# Generated at 2022-06-13 03:16:22.326820
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """
    check a basic PlatformFactCollector.collect call
    """

    platform_facts = PlatformFactCollector().collect()
    assert platform_facts['system'] == platform.system(), 'System should match'
    assert platform_facts['kernel'] == platform.release(), 'Kernel should match'
    assert platform_facts['kernel_version'] == platform.version(), 'Version should match'
    assert platform_facts['machine'] == platform.machine(), 'Machine should match'
    assert platform_facts['python_version'] == platform.python_version(), 'Python version should match'

# Generated at 2022-06-13 03:16:31.134894
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collectors.platform import PlatformFactCollector
    from ansible.module_utils.facts.utils import skip_if_not_imported
    from ansible.module_utils.facts.utils import get_file_content
    import mock

    mock_platform = mock.patch.object(platform, 'uname')
    mock_platform.start()
    platform.uname.return_value = ('Linux', 'localhost.localdomain', '2.6.32-358.el6.x86_64',
                                   '#1 SMP Fri Feb 22 00:31:26 UTC 2013', 'x86_64')

    mock_get_file_content = mock.patch.object(get_file_content, 'get_file_content')
    mock_get_file_content.start()
    get

# Generated at 2022-06-13 03:16:35.143808
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector()

    assert obj.name == 'platform'
    assert obj._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])


if __name__ == '__main__':
    test_PlatformFactCollector()

# Generated at 2022-06-13 03:16:38.140439
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set([
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id'
    ])

# Generated at 2022-06-13 03:16:38.992499
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts.collect() is not None

# Generated at 2022-06-13 03:16:44.908292
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    import platform
    import sys

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import FetchException
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts import utils

    test_collector = PlatformFactCollector(None)

    #Test 1
    #Testing collection from class PlatformFactCollector when file /var/lib/dbus/machine-id is present
    test_platform = "Linux"
    test_release = "4.19.0-9-amd64"
    test_version = "#1 SMP Debian 4.19.118-2+deb10u1 (2021-01-07)"
    test

# Generated at 2022-06-13 03:16:49.933287
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.reset_mock()
    PlatformFactCollector.collect()
    assert PlatformFactCollector.has_run
    assert PlatformFactCollector.previous_call == (PlatformFactCollector.collect, (), {})
    assert PlatformFactCollector._fact_cache['system'] == platform.system()
    assert PlatformFactCollector._fact_cache['kernel'] == platform.release()
    assert PlatformFactCollector._fact_cache['kernel_version'] == platform.version()
    assert PlatformFactCollector._fact_cache['machine'] == platform.machine()
    assert PlatformFactCollector._fact_cache['python_version'] == platform.python_version()

# Generated at 2022-06-13 03:16:55.552606
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id']) == set(pfc._fact_ids)

# Generated at 2022-06-13 03:16:59.143800
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == {'system', 'kernel', 'kernel_version', 'machine', 'python_version',
                                                 'architecture', 'machine_id'}

# Generated at 2022-06-13 03:17:08.398686
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils._text import to_bytes

    # set up required input for method under test
    module = SharedFakeModule()
    # set up required and expected output for method under test

# Generated at 2022-06-13 03:19:47.839159
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    plat_fact_coll = PlatformFactCollector()
    assert(plat_fact_coll.name == 'platform')
    assert(plat_fact_coll._fact_ids == set(
        ['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture',
         'machine_id']))

# Generated at 2022-06-13 03:19:57.155936
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import sys

    temp_platform = platform.__dict__.copy()

    def test_platform_system():
        return "Linux"

    def test_platform_release():
        return "2.6.32-431.el6.x86_64"

    def test_platform_version():
        return "#1 SMP Fri Nov 22 03:15:09 UTC 2013"

    def test_platform_machine():
        return "x86_64"

    def test_platform_python_version():
        return "2.7.5"

    def test_socket_getfqdn():
        return "test.example.com"

    def test_platform_node():
        return "test.example.com"

    platform.system = test_platform_system
    platform.release = test_platform_release
    platform.version

# Generated at 2022-06-13 03:20:00.211099
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_collector = PlatformFactCollector()
    platform_collector.collect()

if __name__ == "__main__":
    test_PlatformFactCollector_collect()

# Generated at 2022-06-13 03:20:05.337396
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector.collect()
    assert set(platform_fact_collector._fact_ids) == set(['system',
                                                          'kernel',
                                                          'kernel_version',
                                                          'machine',
                                                          'python_version',
                                                          'architecture',
                                                          'machine_id'])


# Generated at 2022-06-13 03:20:08.490351
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id']) == platform_fact_collector._fact_ids

# Generated at 2022-06-13 03:20:09.139950
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect()

# Generated at 2022-06-13 03:20:14.270349
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # create the mock module class
    class MockModule():
        def get_bin_path(self, arg):
            return "/usr/bin/{0}".format(arg)
        def run_command(self, arg):
            return (0, "mock_out", "mock_err")

    pfc = PlatformFactCollector()
    gf = pfc.collect(module=MockModule())

    assert "system" in gf
    assert "kernel" in gf
    assert "kernel_version" in gf
    assert "machine" in gf
    assert "python_version" in gf
    assert "architecture" in gf
    assert "fqdn" in gf
    assert "hostname" in gf
    assert "nodename" in gf
    assert "domain" in gf


# Generated at 2022-06-13 03:20:22.964627
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    test_platform_fact_collector = PlatformFactCollector()
    assert test_platform_fact_collector
    assert isinstance(test_platform_fact_collector, PlatformFactCollector)
    assert test_platform_fact_collector.name == 'platform'
    assert test_platform_fact_collector._fact_ids == set(['system',
                                                          'kernel',
                                                          'kernel_version',
                                                          'machine',
                                                          'python_version',
                                                          'architecture',
                                                          'machine_id'])


# Generated at 2022-06-13 03:20:29.568823
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # mock
    module = type('module', (object,), {
        'run_command': lambda self, cmd, check_rc=True: (0, 'out', 'err'),
        'get_bin_path': lambda self, cmd: 'path/to/{0}'.format(cmd)
    })()
    # execute
    platform_facts = PlatformFactCollector(module=module).collect()
    # assert
    assert len(platform_facts.keys()) > 0
    assert 'system' in platform_facts
    assert 'kernel' in platform_facts
    assert 'kernel_version' in platform_facts
    assert 'machine' in platform_facts
    assert 'python_version' in platform_facts
    assert 'architecture' in platform_facts
    assert 'userspace_bits' in platform_facts



# Generated at 2022-06-13 03:20:35.335909
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    test_platform_fact_collector = PlatformFactCollector()
    assert test_platform_fact_collector.name == 'platform'
    assert test_platform_fact_collector._fact_ids == set(['system',
                                                           'kernel',
                                                           'kernel_version',
                                                           'machine',
                                                           'python_version',
                                                           'architecture',
                                                           'machine_id'])