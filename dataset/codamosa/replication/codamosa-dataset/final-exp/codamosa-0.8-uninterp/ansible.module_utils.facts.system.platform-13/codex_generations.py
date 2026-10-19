

# Generated at 2022-06-13 03:13:12.210026
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    platform_fact_collector.collect()

# Generated at 2022-06-13 03:13:16.030858
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts.name == 'platform'
    assert platform_facts._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:13:21.986454
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

# Generated at 2022-06-13 03:13:31.085018
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import os
    import sys
    import platform
    import socket
    import re

    # Initialize some variables
    platform_system = platform.system()
    platform_machine = platform.machine()
    platform_python_version = platform.python_version()
    hostname = socket.gethostname()
    fqdn = socket.getfqdn()
    domain = '.'.join(fqdn.split('.')[1:])
    nodename = platform.node()
    lsb_distrib_id = lsb_distrib_release = lsb_distrib_codename = lsb_distrib_description = None

    # Set some variables
    if platform_system == 'Linux':
        lsb_distrib_id = lsb_distrib_release = lsb_distrib_codename = lsb_distrib_description

# Generated at 2022-06-13 03:13:36.146349
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Test empty parameter
    platform_fc = PlatformFactCollector()
    (platform_facts, has_changed) = platform_fc.collect()
    assert 'ansible_architecture' in platform_facts
    assert 'ansible_fqdn' in platform_facts
    assert 'ansible_hostname' in platform_facts
    assert 'ansible_nodename' in platform_facts
    assert 'ansible_system' in platform_facts
    assert 'ansible_machine' in platform_facts
    assert 'ansible_kernel' in platform_facts
    assert 'ansible_python_version' in platform_facts
    assert 'ansible_machine_id' in platform_facts

# Generated at 2022-06-13 03:13:41.994284
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import sys
    import platform
    from ansible.module_utils.facts.collector import BaseFactCollector

    class FakeModule(object):
        def get_bin_path(self):
            return '/bin/ls'

    class FakeGetconfMachineArch(object):
        code = 0
        stdout = 'PowerPC_POWER7'
        stderr = ''

        def run(self):
            return (self.code, self.stdout, self.stderr)

    class FakeBootinfoPowerPC(object):
        code = 0
        stdout = 'powerpc\n'
        stderr = ''

        def run(self):
            return (self.code, self.stdout, self.stderr)

    class FakeBootinfoNotPowerPC(object):
        code = 0

# Generated at 2022-06-13 03:13:44.861519
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert hasattr(p, 'name')
    assert p.name == 'platform'
    assert hasattr(p, '_fact_ids')
    assert len(p._fact_ids) == 8


# Generated at 2022-06-13 03:13:48.716714
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    test_platform_fact_collector = PlatformFactCollector()
    assert test_platform_fact_collector.name == "platform"
    assert test_platform_fact_collector._fact_ids == set(['system',
                                                          'kernel',
                                                          'kernel_version',
                                                          'machine',
                                                          'python_version',
                                                          'architecture',
                                                          'machine_id'])

# Generated at 2022-06-13 03:13:58.488119
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    def test_data_path(filename):
        return 'ansible/module_utils/facts/collectors/platform/data/' + filename

    PlatformFactCollector.collect()

    try:
        import unittest.mock as mock
        from unittest.mock import patch
    except ImportError:
        import mock
        from mock import patch


# Generated at 2022-06-13 03:14:05.562575
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    fact_collector = PlatformFactCollector()
    llist = ['system', 'kernel', 'kernel_version', 'machine',
             'python_version', 'architecture', 'machine_id']
    assert fact_collector._fact_ids == set(llist)
    platform_facts = fact_collector.collect()
    assert isinstance(platform_facts, dict)
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

# Generated at 2022-06-13 03:14:55.724464
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert(x)

    #Make sure we get back the correct class
    assert(x.__class__.__name__ == 'PlatformFactCollector')


# Generated at 2022-06-13 03:14:58.900851
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'
    assert PlatformFactCollector._fact_ids == set([u'system', u'kernel', u'kernel_version',
                                                   u'machine', u'python_version', u'architecture', u'machine_id'])

# Generated at 2022-06-13 03:15:09.231599
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import set_collector_instance

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import json

    # Create a fake module to pass to PlatformFactCollector
    class FakeModule(object):

        def __init__(self):
            pass

        @staticmethod
        def get_bin_path(arg1, required=False):
            return "/usr/bin/python"


# Generated at 2022-06-13 03:15:10.600501
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """
    This method is used to run unit tests on method collect
    """
    pass

# Generated at 2022-06-13 03:15:17.459927
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pf = PlatformFactCollector()
    platform_facts = pf.collect()

    assert platform_facts['system'] == platform.system()
    assert platform_facts['kernel'] == platform.release()
    assert platform_facts['kernel_version'] == platform.version()
    assert platform_facts['machine'] == platform.machine()
    assert platform_facts['python_version'] == platform.python_version()
    assert platform_facts['fqdn'] == socket.getfqdn()
    assert platform_facts['hostname'] == platform.node().split('.')[0]
    assert platform_facts['nodename'] == platform.node()

    assert platform_facts['architecture'] == ('i386' if solaris_i86_re.search(platform_facts['machine'])
                                              else platform_facts['machine'])



# Generated at 2022-06-13 03:15:26.324532
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """
    Returns a dictionary of platform facts.
    :return: A dictionary of platform facts.
    """
    from ansible.module_utils.facts.facts import FACT_CACHE
    import ansible.module_utils.facts as facts_module

    def fake_run_command(params, *args, **kwargs):
        class FakeResult:
            def __init__(self):
                self.returncode = 0
                self.stdout = 'x86_64'
                self.stderr = ''

            def __str__(self):
                return self.stdout

        return FakeResult()

    # Mock module_utils.facts.PlatformFactCollector._run_command
    facts_module.PlatformFactCollector._run_command = fake_run_command
    facts_module.FACT_CACHE = FACT_

# Generated at 2022-06-13 03:15:35.742735
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform = None
    python_version = None
    fqdn = None
    hostname = None
    nodename = None
    domain = None
    userspace_bits = None
    architecture = None
    machine_id = None

    def mock_platform():
        return platform

    def mock_python_version():
        return python_version

    def mock_fqdn():
        return fqdn

    def mock_hostname():
        return hostname

    def mock_nodename():
        return nodename

    def mock_domain():
        return domain

    def mock_userspace_bits():
        return userspace_bits

    def mock_architecture():
        return architecture

    def mock_machine_id():
        return machine_id

    def mock_node():
        return nodename


# Generated at 2022-06-13 03:15:44.448438
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import socket

    saved_python_platform = platform.system
    saved_socket_getfqdn = socket.getfqdn

    platform.system = lambda: 'Linux'
    socket.getfqdn = lambda: 'example.com'

    platform_facts = PlatformFactCollector().collect()
    assert platform_facts['system'] == 'Linux'
    assert platform_facts['kernel'] == platform.release()
    assert platform_facts['kernel_version'] == platform.version()
    assert platform_facts['machine'] == platform.machine()
    assert platform_facts['fqdn'] == 'example.com'
    assert platform_facts['hostname'] == 'example'
    assert platform_facts['domain'] == 'com'
    assert platform_facts['architecture'] == 'x86_64'
    assert platform_

# Generated at 2022-06-13 03:15:55.839750
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=False)
    PlatformFactCollector().collect(module, {})

# Generated at 2022-06-13 03:16:04.787065
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """Unit test for method collect of class PlatformFactCollector"""

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import ansible_collections

    # Module name is fact and it's compiled in the same directory
    module_name = 'ansible_collections.ansible.builtin.fact'

    # Base class for custom ansible module
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = {}
            self.result = dict(changed=False)

        def exit_json(self, *args, **kwargs):
            return

        def fail_json(self, *args, **kwargs):
            return

        def get_bin_path(self, *args, **kwargs):
            return


# Generated at 2022-06-13 03:16:58.677310
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    x._fact_ids.add('test')
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'fqdn',
                               'hostname',
                               'nodename',
                               'domain',
                               'architecture',
                               'machine_id',
                               'test'])
    assert x.collect() != {}



# Generated at 2022-06-13 03:17:07.701339
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """
    Test correct return structure and values for method collect of class PlatformFactCollector
    """
    import platform

    class MockOsModule(object):
        def __init__(self):
            self.uname_result = ('Linux', 'tst_host', '3.10.0-327.4.4.el7.x86_64','#1 SMP Fri Jan 29 17:01:28 EST 2016', 'x86_64', 'x86_64')
            self.environ = {'PATH': ''}
        def getenv(self, key):
            if key in self.environ:
                return self.environ[key]
            else:
                return None
        def uname(self):
            return self.uname_result

# Generated at 2022-06-13 03:17:16.642533
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils.facts.collector import collect_facts

    platform_fc = PlatformFactCollector()
    platform_fc._collect_platform_facts = platform_fc.collect
    my_platform_fc = lambda: platform_fc
    # Create a dummy module from which the run_command method can be invoked
    module = type('', (), {})
    def dummy_get_bin_path(bin_name):
        return "/usr/bin/{}".format(bin_name)
    module.get_bin_path = dummy_get_bin_path



# Generated at 2022-06-13 03:17:22.027787
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import socket

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.platform import PlatformFactCollector
    from ansible.module_utils.facts.utils import FactsDict

    pfc = PlatformFactCollector()

    test_facts = FactsDict()
    test_facts['system'] = 'Linux'
    test_facts['kernel'] = '3.10.0-229.20.1.el7.x86_64'
    test_facts['kernel_version'] = '1.0.15-1.el7.centos'
    test_facts['machine'] = 'x86_64'
    test_facts['python_version'] = '2.7.5'
    test_facts['fqdn'] = socket.getfqdn()
    test

# Generated at 2022-06-13 03:17:25.766147
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

# Generated at 2022-06-13 03:17:33.772003
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts import get_collector_instance

    module_facts_instance = ModuleFacts(None)

    platform_fact_collector = get_collector_instance(PlatformFactCollector, module_facts_instance)

    assert isinstance(platform_fact_collector, PlatformFactCollector)

    # Test collect() method
    platform_facts = platform_fact_collector.collect()

    assert 'system' in platform_facts
    assert 'kernel' in platform_facts
    assert 'kernel_version' in platform_facts
    assert 'machine' in platform_facts
    assert 'python_version' in platform_facts

    assert 'architecture' in platform_facts
    assert 'userspace_bits' in platform_facts


# Generated at 2022-06-13 03:17:38.022805
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert 'system' in PlatformFactCollector._fact_ids
    assert 'python_version' in PlatformFactCollector._fact_ids
    assert 'kernel' in PlatformFactCollector._fact_ids
    assert 'machine' in PlatformFactCollector._fact_ids
    assert 'architecture' in PlatformFactCollector._fact_ids
    assert 'kernel_version' in PlatformFactCollector._fact_ids
    assert 'machine_id' in PlatformFactCollector._fact_ids

# Generated at 2022-06-13 03:17:43.084794
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # The goal of this test is to check PlatformFactCollector.collect()
    # This method was reset to the default FactCollector.collect()
    # So this test is used to check that the method returns an empty dict
    # This test is run in the 'unit' directory but uses the test_utils module in the root directory
    # so we need to add the root directory to path
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from test_utils import FakeModule

    # Create collector and test 'collect' method
    obj = PlatformFactCollector()
    facts_dict = obj.collect(module=None, collected_facts=None)
    assert facts_dict == {}

# Generated at 2022-06-13 03:17:48.601314
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Test with simple values
    x = PlatformFactCollector()

    assert x.name == 'platform'
    assert x._fact_ids == {'system',
                           'kernel',
                           'kernel_version',
                           'machine',
                           'python_version',
                           'architecture',
                           'machine_id'}

# Generated at 2022-06-13 03:17:54.563342
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



# Generated at 2022-06-13 03:18:59.602012
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    from ansible.module_utils.facts.collector import TestAnsibleModule, TestConnection
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.platform.collectors import PlatformFactCollector


# Generated at 2022-06-13 03:19:07.337366
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert 'system' in platform_collector._fact_ids
    assert 'kernel' in platform_collector._fact_ids
    assert 'kernel_version' in platform_collector._fact_ids
    assert 'machine' in platform_collector._fact_ids
    assert 'python_version' in platform_collector._fact_ids
    assert 'architecture' in platform_collector._fact_ids
    assert 'userspace_bits' in platform_collector._fact_ids
    assert 'userspace_architecture' in platform_collector._fact_ids

# Generated at 2022-06-13 03:19:13.157434
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    import platform

    PLATFORM_FACTS = {
        '_ansible_machine_id': "",
        'architecture': platform.machine(),
        'domain': "",
        'fqdn': platform.node(),
        'hostname': platform.node().split('.')[0],
        'kernel': platform.release(),
        'kernel_version': platform.version(),
        'machine': platform.machine(),
        'nodename': platform.node(),
        'python_version': platform.python_version(),
        'system': platform.system()
    }

    myCollector = FactCollector(module=None)
    myCollector.add_collector(PlatformFactCollector)


# Generated at 2022-06-13 03:19:20.541938
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = {}
    platform_facts['system'] = platform.system()
    platform_facts['kernel'] = platform.release()
    platform_facts['kernel_version'] = platform.version()
    platform_facts['machine'] = platform.machine()
    platform_facts['architecture'] = platform.architecture()[0]
    platform_facts['python_version'] = platform.python_version()

    pfc = PlatformFactCollector(None, None, None)

    assert pfc.collect() == platform_facts

# Generated at 2022-06-13 03:19:21.445154
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    '''
    Constructor test
    '''
    PlatformFactCollector()

# Generated at 2022-06-13 03:19:26.000303
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_obj = PlatformFactCollector()
    assert platform_obj.name == 'platform'
    assert platform_obj._fact_ids == set(['system',
                                          'kernel',
                                          'kernel_version',
                                          'machine',
                                          'python_version',
                                          'architecture',
                                          'machine_id'])

# Generated at 2022-06-13 03:19:27.325043
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts is not None

# Generated at 2022-06-13 03:19:28.157015
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect()

# Generated at 2022-06-13 03:19:35.112505
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()

    assert x
    assert x.name == 'platform'
    assert 'system' in x._fact_ids
    assert 'kernel' in x._fact_ids
    assert 'kernel_version' in x._fact_ids
    assert 'machine' in x._fact_ids
    assert 'python_version' in x._fact_ids
    assert 'architecture' in x._fact_ids
    assert 'machine_id' in x._fact_ids


# Generated at 2022-06-13 03:19:35.886111
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect()

# Generated at 2022-06-13 03:21:28.730174
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])
    assert x.collect()

# Generated at 2022-06-13 03:21:36.092111
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    import platform
    import os
    import mock

    platform.system = mock.Mock(return_value='Linux')
    platform.release = mock.Mock(return_value='4.4.4-1-ARCH')
    platform.version = mock.Mock(return_value='')
    platform.machine = mock.Mock(return_value='x86_64')
    platform.python_version = mock.Mock(return_value='2.7.2')
    platform.node = mock.Mock(return_value='test-node')
    # platform.architecture() return a tuple
    platform.architecture = mock.Mock(return_value=('32bit', 'ELF'))

    os = mock.Mock()
    os.get

# Generated at 2022-06-13 03:21:40.671039
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
    assert platform_fact_collector.dependencies == set()

# Generated at 2022-06-13 03:21:47.278143
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import gather_subset
    from ansible.module_utils.facts.utils import AnsibleFactCollector

    platform = PlatformFactCollector()

    class Options(object):
        def __init__(self, gather_subset):
            self.gather_subset = gather_subset

    class TestModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, arg):
            if arg in ['getconf', 'bootinfo']:
                return arg
            else:
                return None

        def run_command(self, cmd, check_rc=True):
            return (0, "", "")

    options = Options(gather_subset)


# Generated at 2022-06-13 03:21:49.893866
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """
    Test to verify creation of object for class PlatformFactCollector
    """
    platform = PlatformFactCollector()
    assert platform._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture'])

# Generated at 2022-06-13 03:21:53.112292
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc.collect()['system'] == platform.system()
    assert pfc.collect()['kernel'] == platform.release()
    assert pfc.collect()['kernel_version'] == platform.version()
    assert pfc.collect()['machine'] == platform.machine()
    assert pfc.collect()['python_version'] == platform.python_version()
    assert pfc.collect()['architecture'] == solaris_i86_re.sub(r'\1', platform.machine())

# Generated at 2022-06-13 03:21:57.161158
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
  pfc = PlatformFactCollector()
  assert pfc.name == 'platform'
  assert list(pfc._fact_ids) == ['system',
   'kernel',
   'kernel_version',
   'machine',
   'python_version',
   'architecture',
   'machine_id']

# Generated at 2022-06-13 03:22:02.692915
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

# Generated at 2022-06-13 03:22:05.635600
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert collector._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 
        'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:22:09.266014
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])
