

# Generated at 2022-06-13 01:27:38.285962
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    module = sys.modules['ansible.module_utils.facts.collector.base']
    sys.modules['ansible.module_utils.facts.collector.base'] = None
    # initialize test values

# Generated at 2022-06-13 01:27:48.142034
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit tests for method collect of class FcWwnInitiatorFactCollector.
    """
    test_collector = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:27:52.043379
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts = FcWwnInitiatorFactCollector()
    assert facts.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in facts._fact_ids


# Generated at 2022-06-13 01:27:56.587857
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    # check with empty class instance
    collector = FcWwnInitiatorFactCollector()
    facts = collector.collect()
    assert facts == {'fibre_channel_wwn': []}


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:27:57.847545
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name is not None

# Generated at 2022-06-13 01:28:00.117908
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact = FcWwnInitiatorFactCollector()
    assert fc_fact.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:03.967340
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_fact = FcWwnInitiatorFactCollector()
    assert fc_wwn_fact.name == 'fibre_channel_wwn'
    assert fc_wwn_fact.platform_independent == True


# Generated at 2022-06-13 01:28:07.107628
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    module = AnsibleModuleMock()
    fc_facts = FcWwnInitiatorFactCollector(module, {})
    assert fc_facts.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:28:16.853952
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    This is more of a functional (integration) test than a unit test
    to make sure that the class is called and works with data
    available on the system.
    """
    facts_module = sys.modules['ansible.module_utils.facts.fibre_channel_wwn']
    fact_module = facts_module.FcWwnInitiatorFactCollector()
    result = fact_module.collect()
    assert 'fibre_channel_wwn' in result
    # make sure we have at least one WWN in the resulting list
    assert len(result['fibre_channel_wwn']) >= 1
    # assert result['fibre_channel_wwn'] == ['foo']

# Generated at 2022-06-13 01:28:23.783950
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import ansible_collector
    from ansible.module_utils.facts import modules

    class MockModule:
        def __init__(self):
            self.params = None
            self.exit_json = None

        def get_bin_path(self, arg1, opt_dirs=None):
            if arg1 == 'fcinfo':
                return '/usr/sbin/fcinfo'
            elif arg1 == 'lsdev':
                return '/usr/bin/lsdev'
            elif arg1 == 'lscfg':
                return '/usr/sbin/lscfg'
            elif arg1 == 'ioscan' and opt_dirs == ['/opt/fcms/bin']:
                return '/usr/sbin/ioscan'

# Generated at 2022-06-13 01:28:44.589661
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    test_module = AnsibleModuleMock()
    test_module.run_command = run_command_mock
    test_module.get_bin_path = get_bin_path_mock
    test_facts = FcWwnInitiatorFactCollector().collect(module=test_module)
    assert test_facts['fibre_channel_wwn'] == ['0x21000014ff52a9bb']


###################################################################################
#  MOCKS for Unit testing
###################################################################################

import os


# Generated at 2022-06-13 01:28:55.986936
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    This unit test was written to test the method collect of the class FcWwnInitiatorFactCollector on all supported operating systems
    """

    class Module:
        def __init__(self):
            self.params = {}
            self.run_command_result = dict({'rc': 0, 'stdout': "", 'stderr': "", 'stdin': "", 'start': 0, 'end': 0, 'delta': 0, 'cmd': ''})

        def get_bin_path(self, cmd, required=False, opt_dirs=[]):
            if cmd == 'ioscan':
                return '/usr/sbin/ioscan'
            if cmd == 'fcmsutil':
                return '/opt/fcms/bin/fcmsutil'

# Generated at 2022-06-13 01:28:58.950460
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 01:29:01.921049
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn_facts = FcWwnInitiatorFactCollector()
    assert fcwwn_facts.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:13.354037
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    # Create the instance of FcWwnInitiatorFactCollector class
    f = FcWwnInitiatorFactCollector()

    # Create mock ansible module
    class AnsibleModuleMock():
        def __init__(self):
            self.params = {}
            self.facts = {}

        def get_bin_path(self, *args):
            cmd = args[0]
            if cmd == 'fcinfo':
                return '/usr/sbin/fcinfo'
            elif cmd == 'lsdev':
                return '/usr/sbin/lsdev'
            elif cmd == 'lscfg':
                return '/usr/sbin/lscfg'
            elif cmd == 'ioscan':
                return '/usr/sbin/ioscan'

# Generated at 2022-06-13 01:29:19.248990
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_obj = FcWwnInitiatorFactCollector()
    assert fc_obj.name == 'fibre_channel_wwn'
    assert fc_obj.platform == 'All'
    assert fc_obj.priority == 6
    assert fc_obj.collection_only == False
    assert fc_obj._fact_ids == set()

# Generated at 2022-06-13 01:29:22.858109
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_init = FcWwnInitiatorFactCollector()
    assert fc_wwn_init.name == 'fibre_channel_wwn'
    assert fc_wwn_init._fact_ids == set()

# Generated at 2022-06-13 01:29:26.809467
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    # not implemented, how to unit test this?
    #fc_facts = collector.collect()
    #assert isinstance(fc_facts, dict)
    #assert 'fibre_channel_wwn' in fc_facts

# Generated at 2022-06-13 01:29:33.976781
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collectors.network.fibre_channel_wwn import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.collectors.network.fibre_channel_wwn import test_FcWwnInitiatorFactCollector
    fcwwnFactCollector = FactCollector(
        module=None,
        traveled_path=set(),
        collected_facts=dict(ansible_facts=dict()),
    )
    fcwwnFactCollector._collectors[FcWwnInitiatorFactCollector.name] = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:29:38.210512
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts._fact_ids == set(['fibre_channel_wwn'])


# Generated at 2022-06-13 01:30:04.123368
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector.collect() == {}


# Generated at 2022-06-13 01:30:05.953149
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    '''
    This function returns the class FcWwnInitiatorFactCollector
    '''
    return FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:12.434770
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """Unit test class constructor."""
    fact_collector = FcWwnInitiatorFactCollector()
    # testing fact names
    assert fact_collector.name == 'fibre_channel_wwn', \
        "The constructor of class FcWwnInitiatorFactCollector " + \
        "does not create valid object."
    # testing collector ID
    assert len(fact_collector._fact_ids) == 1, \
        "The constructor of class FcWwnInitiatorFactCollector " + \
        "does not create valid object."
    assert 'fibre_channel_wwn' in fact_collector._fact_ids, \
        "The constructor of class FcWwnInitiatorFactCollector " + \
        "does not create valid object."

# Generated at 2022-06-13 01:30:22.289792
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnInitiatorFactCollector._fact_ids = set()
    fc_facts = FcWwnInitiatorFactCollector().collect()
    if 'fibre_channel_wwn' in fc_facts:
        wwn_list = fc_facts['fibre_channel_wwn']
        if len(wwn_list) > 0:
            print("OK: WWNs found: %s" % ' '.join(wwn_list))
            return True
        else:
            print("ERROR: WWNs found but list empty")
            return False
    else:
        print("ERROR: WWNs not found")
        return False

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:30:30.361162
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class_inst = FcWwnInitiatorFactCollector()

    class_inst._ansible_module = object()
    def module_run_command_side_effect(command):
        # return same output for all commands, since this is only a test
        return (0, '10000090fa1658de', '')

    class_inst._ansible_module.run_command = module_run_command_side_effect

    class_inst._ansible_module.get_bin_path = lambda x, opt_dirs=None: "ioscan"
    class_inst._ansible_module.get_file_lines = \
        lambda file_path: ['HBA Port WWN: 10000090FA1658DE']


# Generated at 2022-06-13 01:30:33.262759
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for constructor of class FcWwnInitiatorFactCollector
    """
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'


if __name__ == '__main__':
    # unittest.main()
    test_FcWwnInitiatorFactCollector()
    pass

# Generated at 2022-06-13 01:30:37.700974
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()
    assert fact_collector._platform == 'Generic'


# Generated at 2022-06-13 01:30:47.914210
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class TestModule:
        def get_bin_path(self, command):
            if command == 'fcinfo' and sys.platform.startswith('sunos'):
                return "/usr/sbin/fcinfo"
            elif command == 'ioscan' and sys.platform.startswith('hp-ux'):
                return "/usr/sbin/ioscan"
            elif command == 'fcmsutil' and sys.platform.startswith('hp-ux'):
                return "/opt/fcms/bin/fcmsutil"
            elif (command == 'lscfg' and sys.platform.startswith('hp-ux')) or (command == 'lscfg' and sys.platform.startswith('aix')):
                return "/usr/sbin/lscfg"

# Generated at 2022-06-13 01:30:58.393563
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class AnsibleModuleMock():
        def get_bin_path(self, module, opt_dirs=None):
            if module == 'fcinfo':
                return '/usr/sbin/fcinfo'
            elif module == 'grep':
                return '/usr/bin/grep'
            elif module == 'lsdev':
                return '/usr/bin/lsdev'
            elif module == 'lscfg':
                return '/usr/bin/lscfg'
            elif module == 'ioscan':
                return '/usr/sbin/ioscan'
            elif module == 'fcmsutil':
                return '/opt/fcms/bin/fcmsutil'
            else:
                return None


# Generated at 2022-06-13 01:31:00.645397
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    t = FcWwnInitiatorFactCollector()
    assert t.name == 'fibre_channel_wwn'
    assert t._fact_ids == set()



# Generated at 2022-06-13 01:31:48.326103
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_facts = FcWwnInitiatorFactCollector()
    assert fc_wwn_facts.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:55.633605
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    'Unit test for method collect of class FcWwnInitiatorFactCollector'

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.network.fibre_channel import FcWwnInitiatorFactCollector
    module = BaseFactCollector()
    fc_facts = FcWwnInitiatorFactCollector().collect(module)
    assert(fc_facts['fibre_channel_wwn'] == [])



# Generated at 2022-06-13 01:32:07.226453
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            return

        def run_command(self, command):
            return (0, 'HBA Port WWN: 10000090fa1658de', '')

        def get_bin_path(self, command, opt_dirs=[]):
            if command == "fcinfo":
                return "/usr/sbin/fcinfo"
            elif command == "lsdev":
                return "/usr/sbin/lsdev"
            elif command == "lscfg":
                return "/usr/sbin/lscfg"
            elif command == "ioscan" and '/opt/fcms/bin/fcmsutil' in opt_dirs:
                return "/opt/fcms/bin/fcmsutil"
            else:
                return False

# Generated at 2022-06-13 01:32:16.654771
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule

    # create object
    FcWwnInitiatorFactCollector_obj = FcWwnInitiatorFactCollector()

    # create a mock module and mock facts
    module = MockModule()
    collected_facts = {}
    # execute the method collect of FcWwnInitiatorFactCollector
    fact_dict = FcWwnInitiatorFactCollector_obj.collect(module=module, collected_facts=collected_facts)

    # check the facts
    assert 'fibre_channel_wwn' in fact_dict
    assert type(fact_dict['fibre_channel_wwn']).__name__ == 'list'

# Generated at 2022-06-13 01:32:20.415813
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    unit test for method collect of class FcWwnInitiatorFactCollector
    """
    pass

# Unit test execution
if __name__ == '__main__':
    print('=== Testing... ===')
    test_FcWwnInitiatorFactCollector_collect()
    print('=== Done. ===')

# Generated at 2022-06-13 01:32:25.569962
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnFactCollector = FcWwnInitiatorFactCollector()
    fc_facts = FcWwnFactCollector.collect()
    assert isinstance(fc_facts['fibre_channel_wwn'], list)

# Generated at 2022-06-13 01:32:34.888028
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.network import CollectorNetwork
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector
    the_Collector = Collector(None, None, None, None)
    the_Collector.collectors = [CollectorNetwork(), FcWwnInitiatorFactCollector()]

    the_FcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()
    the_FcWwnInitiatorFactCollector.collect()


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:32:37.551853
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn = FcWwnInitiatorFactCollector()
    assert fcwwn is not None
    assert 'fibre_channel_wwn' == fcwwn.name


# Generated at 2022-06-13 01:32:46.377301
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    import os
    import sys
    from collections import namedtuple

    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes

    def _mock_ansible_module():
        AnsibleModule = namedtuple('AnsibleModule', ['get_bin_path'])
        return AnsibleModule(get_bin_path=_mock_get_bin_path)

    def _mock_get_bin_path(module_name, opt_dirs=[]):
        if module_name == 'fcinfo' and platform.system() == 'SunOS':
            return '/usr/sbin/fcinfo'

# Generated at 2022-06-13 01:32:48.566463
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_col = FcWwnInitiatorFactCollector()
    assert fc_col.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:26.359695
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.utils import AnsibleExitModule
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector

    # create a mock module
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.run_command_calls = []
            self.exit_args = []
            self.exit_kwargs = []
            self.run_command_rcs = []
            self.run_command_outputs = []

        def run_command(self, args, check_rc=True):
            self.run_command_calls.append(args)

# Generated at 2022-06-13 01:34:37.724278
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch

    FcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()

    class TestModule(object):
        def __init__(self, facts):
            self.params = {}
            self.facts = facts
            self.run_command = mock_run_command

        def get_bin_path(self, path, opt_dirs=[]):
            if path in ('ioscan', '/opt/fcms/bin/fcmsutil'):
                return path
            elif path in ('lsdev', 'lscfg'):
                return 'aix_' + path


# Generated at 2022-06-13 01:34:45.447113
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    # name and version should be different
    assert fc_facts.name != "FcWwnInitiatorFactCollector"
    assert fc_facts.name != "fcwwninitiatorfactcollector"
    assert fc_facts.name != "FcWwnInitiatorfactcollector"
    assert fc_facts.name != "FcWwnInitiatorFactcollector"
    assert fc_facts.name != "fcwwninitiatorFactcollector"
    assert fc_facts.name != "fcwwninitiatorFactcollector"
    assert fc_facts.name != "fibre_channel_wwn"
    assert fc_facts.name != ""


# Generated at 2022-06-13 01:34:54.262208
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
  """Test method collect of FcWwnInitiatorFactCollector"""
  import platform
  import sys
  # unit test with mock platform.system()
  class MockPlatformSystem(object):
    """Mock platform.system()"""
    def system(sysname):
      """Mock platform.system()"""
      if sysname == 'hp-ux':
        return 'hp-ux'
      if sysname == 'linux':
        return 'linux'
      if sysname == 'sunos':
        return 'sunos'
      if sysname == 'aix':
        return 'aix'
      else:
        return 'unittest'
  # save platform.system
  platformSystem = platform.system
  # mock platform.system
  platform.system = MockPlatformSystem.system
  # unit test with mock sys.platform

# Generated at 2022-06-13 01:34:57.974410
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:35:04.419902
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # Use https://pypi.python.org/pypi/pytest-mock/ to mock modules
    # and http://www.voidspace.org.uk/python/mock/examples.html
    # to make the mock more realistic
    # Here we just check that the FcWwnInitiatorFactCollector().collect()
    # function returns something
    result = FcWwnInitiatorFactCollector().collect()
    assert result is not None
    assert result['fibre_channel_wwn'] is not None

# Generated at 2022-06-13 01:35:07.931856
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    '''Test to validate constructor of class FcWwnInitiatorFactCollector.'''
    fc = FcWwnInitiatorFactCollector()
    assert fc  # assert that fc is defined


# Generated at 2022-06-13 01:35:10.417612
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc = FcWwnInitiatorFactCollector()
    fc.collect()

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:35:13.447098
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Constructor of class FcWwnInitiatorFactCollector
    """
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:35:16.049720
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert 'fibre_channel_wwn' == fc_collector.name
    assert set() == fc_collector._fact_ids
