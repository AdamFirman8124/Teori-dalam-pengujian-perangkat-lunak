

# Generated at 2022-06-13 02:19:53.458354
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    # DummyModule - Object
    testobj = basic.DummyModule(argument_spec={})

    # SystemCapabilitiesFactCollector - Object
    testcollector = SystemCapabilitiesFactCollector()

    assert testcollector.name == 'caps'

    # DummyModule.run_command
    testobj.run_command = lambda x, y: (0, "Current: =ep", "")

    caps_facts = testcollector.collect(module=testobj)
    assert caps_facts['system_capabilities_enforced'] == 'False'

    # DummyModule.run_command

# Generated at 2022-06-13 02:19:53.982751
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:20:04.389624
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import ModuleFacts
    import mock
    module = mock.Mock()
    module.get_bin_path.return_value = '/usr/bin/capsh'
    rc, out, err = 0, 'Current: =ep\n', ''
    module.run_command.return_value = (rc, out, err)
    sut = SystemCapabilitiesFactCollector()
    facts_dict = sut.collect(module)
    assert 'system_capabilities_enforced' in facts_dict
    assert 'NA' == facts_dict['system_capabilities_enforced']
    assert 'system_capabilities' in facts_dict
    assert [] == facts_dict['system_capabilities']

# Generated at 2022-06-13 02:20:12.230698
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Verify that collect method as expected for different input.
    """
    from ansible.module_utils.facts.collector import DictData

    # NOTE: (dont-care-variable, module) -> fact_dict
    # Setup a mocked out module with a working capsh_path
    capsh_path = '/usr/bin/capsh'
    test_module = DictData(dict(get_bin_path=lambda x: capsh_path,
                                run_command=lambda x, **kwargs: (0, 'Current: =ep', '')))
    # Test expected results when capsh is installed, but it's not enforcing capabilities (['=ep'])

# Generated at 2022-06-13 02:20:13.976830
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: set up mocks for get_caps_data and parse_caps_data
    pass

# Generated at 2022-06-13 02:20:19.039895
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import pytest
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.system.capabilities_collector import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collectors.system.capabilities_collector import get_caps_data
    from ansible.module_utils.facts.collectors.system.capabilities_collector import parse_caps_data

    class FakeModule:
        def get_bin_path(self, bin_name):
            return '/usr/bin/capsh'

        def run_command(self, command):
            return 0, get_caps_data(), None

    fake_module = FakeModule()
    SystemCapabilitiesFactCollector.collect(fake_module)

# Generated at 2022-06-13 02:20:20.804723
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: need better mocking of module 'run_command()' to test this -akl
    assert SystemCapabilitiesFactCollector().collect() == {}

# Generated at 2022-06-13 02:20:24.470059
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # instantiate collector, assert __doc__
    c = SystemCapabilitiesFactCollector()
    assert c.__doc__ == '''Collect facts related to systems 'capabilities' via capsh'''
    # TODO: assert c.name = 'caps'
    # TODO: assert c._fact_ids = set(['system_capabilities', 'system_capabilities_enforced'])


# Generated at 2022-06-13 02:20:24.953045
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:20:36.086587
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector

    def make_fake_module(out):
        import json
        import platform
        import distro
        import tempfile
        class TmpFile(object):
            def __exit__(self, *args):
                pass
            def __enter__(self):
                return self
            def write(self, data):
                pass
        class FakeModule(object):
            def __init__(self):
                self.params = {}
                self.version_info = {'python': platform.python_version(), 'distribution': distro.id(), 'release': distro.release(), 'system': platform.system()}
                self.tmpdir = tempfile.gettempdir()

# Generated at 2022-06-13 02:20:43.376799
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Initialise the SystemCapabilitiesFactCollector
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector()

    # Should always return the same dictionary
    assert system_capabilities_fact_collector.collect() == {
        u'system_capabilities': [],
        u'system_capabilities_enforced': u'NA'
    }

# Generated at 2022-06-13 02:20:50.859542
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = FakeAnsibleModule()
    module.get_bin_path.return_value = "/usr/bin/capsh"

# Generated at 2022-06-13 02:21:01.364236
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:21:10.356814
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector

    # get instance of SystemCapabilitiesFactCollector
    capsh = Collector.fetch_collector('caps')

    # create a fake module object
    # NOTE: this is different than the module object in __main__.py
    class FakeModule(object):
        def __init__(self):
            self.params = {}
            self.args = {}
            self.config = {}
            self.tmpdir = self.config.get("ansible_tmpdir", '')
            if not self.tmpdir:
                self.tmpdir = sys.argv[-1].split("/", 1)[1]
       

# Generated at 2022-06-13 02:21:19.135706
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector

    _values_dict = {'system_capabilities': [],
                    'system_capabilities_enforced': 'NA'}

    # NOTE: changes here must also be applied in test_get_caps_data() below
    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self._ansible_module = None
            self._ansible_module_kwargs = None

        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/capsh'


# Generated at 2022-06-13 02:21:22.815071
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import platform
    import os
    import tempfile
    import sys
    import pytest
    import subprocess
    if sys.version_info[0] != 2:
        pytest.skip("Only run this on python2")

    class test_module(object):
        def run_command(self, cmd, errors):
            return 0, 'Current: =ep', b''
        def get_bin_path(self, cmd):
            return '/bin/capsh'

    os_facts = {}
    (fd, test_file) = tempfile.mkstemp()
    os_facts['test_file'] = test_file
    os_facts['test_file_fd'] = fd

    c = SystemCapabilitiesFactCollector(module=test_module(), collected_facts=os_facts)
    results = c.collect()
   

# Generated at 2022-06-13 02:21:26.335684
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # if test_SystemCapabilitiesFactCollector_collect:
        # return facts_dict
    # else:
    #     return False

    test_SystemCapabilitiesFactCollector_collect.return_value = False
    
    # assert False

# Generated at 2022-06-13 02:21:29.683605
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Test the method SystemCapabilitiesFactCollector.collect of class SystemCapabilitiesFactCollector"""
    SystemCapabilitiesFactCollector().collect()

# Generated at 2022-06-13 02:21:38.753240
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Unit test for method collect of class SystemCapabilitiesFactCollector"""
    #
    # Preconditions
    #
    #
    # Setup and prepare test data
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY3

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import helpers
    from ansible.module_utils.facts.system import platform

    # NOTE: need to init collectors as BaseFactCollector.collect() does
    # NOTE: also needed because BaseFactCollector.populate_fact_cache() calls BaseFactCollector.collect()
   

# Generated at 2022-06-13 02:21:44.003875
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Create an instance of Module()
    module = ansible.module_utils.facts.module_common.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True)

    # Create an instance of SystemCapabilitiesFactCollector
    scfc = SystemCapabilitiesFactCollector()
    scfc.collect(module=module, collected_facts=None)

# Generated at 2022-06-13 02:21:55.242332
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # test collect when capsh does not exist
    import ansible.module_utils.facts.collector as caps_collector
    import ansible.module_utils.facts.system.caps as caps_facts
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils import basic
    c = caps_collector.SystemCapabilitiesFactCollector()
    module = basic.AnsibleModule(argument_spec={})
    module.run_command = get_file_lines(caps_facts.OUTPUT_PATH)
    c.collect(module=module)

# Generated at 2022-06-13 02:22:02.554380
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector

    testmod = AnsibleModule(
        argument_spec=dict()
    )

    # NOTE: capsh_path=>capsh_bin, get_caps_data()/parse_caps_data() for easier mocking -akl
    capsh_bin = '/bin/capsh'
    test_file = os.path.join(os.path.dirname(__file__), 'unit', 'test_capabilities.txt')

    def mock_get_caps_data(module, path):
        if module.get_bin_path('capsh') == path:
            return read_file(test_file)


# Generated at 2022-06-13 02:22:07.824443
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.system.caps as system_caps

    module = AnsibleModule(argument_spec={})
    facts = system_caps.SystemCapabilitiesFactCollector()
    result = facts.collect(module=module)

    assert result['system_capabilities_enforced'] == 'NA'
    assert result['system_capabilities'] == []

# Generated at 2022-06-13 02:22:17.753030
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.base import BaseFactCollector
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    # create test object
    collector = SystemCapabilitiesFactCollector()
    fc = FactCollector()
    BaseFactCollector.get_fact_subclasses = lambda x: [BaseFactCollector]
    fc._fact_classes = BaseFactCollector.get_fact_subclasses()
    fc._supported_os = set([])
    fc._validate_facts()
    fc._populate_fact_cache()
    fc.collect(module=None)
    caps_data = collector.collect

# Generated at 2022-06-13 02:22:24.584875
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Stub module class for module_utils/basic.py and module_utils/facts/system/caps.py
    class ModuleStub():
        def get_bin_path(self, arg):
            return None
        def run_command(self, cmd, errors='raise'):
            return (0, 'Current: =ep', '')
    # End of Stub module class

    # Stub AnsibleModule class for module_utils/facts/collector/base.py and module_utils/facts/system/caps.py
    class AnsibleModuleStub():
        def __init__(self):
            self.params = {}
            self.facts = {}
            self.exit_json = lambda x: 0
            self.fail_json = lambda x: 0
    # End of Stub AnsibleModule class

    # Stub
    subject = SystemCapabilitiesFactCollect

# Generated at 2022-06-13 02:22:30.435073
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.ansible.misc.tests.unit.compat.mock import MagicMock, patch
    from ansible.module_utils.facts.collector import Facts

    # NOTE: fact_ids/name values guaranteed to match by init of class
    m_fact_ids = set(SystemCapabilitiesFactCollector._fact_ids)
    m_name = SystemCapabilitiesFactCollector.name

    mock_module = MagicMock(name='mock_module')
    mock_module.get_bin_path.return_value = 'capsh'
    mock_module.run_command.return_value = (0, 'Current:\t=ep\nVersion:\t\n', '')

    with patch('ansible.module_utils.facts.collector.Facts') as m_Facts:
        mock_Facts

# Generated at 2022-06-13 02:22:37.389868
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat import mock
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.modules.utils import set_module_args
    from ansible_collections.notmintest.not_a_real_collection.plugins.modules.facts import ansible_facts
    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils import basic
    import os

    SystemCapabilitiesFactCollector.config = dict()
    SystemCapabilitiesFactCollector.config['exclude'] = ['capsh']
    SystemCapabilitiesFactCollector.config['include'] = ['system_capabilities']

    myobj = SystemCapabilitiesFactCollector()


# Generated at 2022-06-13 02:22:47.666674
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile
    import os
    import pprint
    from ansible_collections.ansible.misc.plugins.module_utils import facts
    from ansible_collections.ansible.misc.plugins.module_utils.facts.collectors import system

    # mocked capsh '--print' output

# Generated at 2022-06-13 02:22:56.736665
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''Unit test for method collect of class SystemCapabilitiesFactCollector'''
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/bin/capsh'
    module.run_command.return_value = (0,'Current: =ep\nBounding set =cap_chown,cap_dac_override,cap_net_raw+ep\nInheritable set =cap_chown,cap_dac_override,cap_net_raw+i\nPermitted set =cap_chown,cap_dac_override,cap_net_raw+p\nEffective set =cap_chown,cap_dac_override,cap_net_raw+e\n','error')
    collector = SystemCapabilitiesFactCollector()
    facts = collector.collect(module)
   

# Generated at 2022-06-13 02:23:06.568418
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: rather than import via relative path, use absolute path
    #       to ensure proper unit tests when running full test suite.
    #       (running this as a standalone unit test '-m' also works.)
    #       Also, replace '.' with '_' since pytest matches on 'test_<func>'
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector

    import ansible.module_utils.basic
    test_module = ansible.module_utils.basic.AnsibleModule(
        argument_spec = dict(),
    )

    fact_collector = SystemCapabilitiesFactCollector(test_module)
    collected_facts = fact_collector.collect()

    assert collected_facts.get('system_capabilities_enforced', None) == 'True'
    assert collected

# Generated at 2022-06-13 02:23:23.944453
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import copy
    import sys

    if sys.version_info.major >= 3:
        import io
        StringIO = io.StringIO
    else:
        import StringIO
        StringIO = StringIO.StringIO

    current_dir = os.path.abspath(os.path.dirname(__file__))
    test_data_dir = os.path.join(current_dir, 'test_data')

    # Collect a dict of facts for a 32-bit system:
    def _mocked_run_command_32bit(*args, **kwargs):
        command = args[0]

        if command == ['capsh', '--print']:
            file_path = os.path.join(test_data_dir, 'capsh_print_32bit.txt')

# Generated at 2022-06-13 02:23:34.256414
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import platform
    import mock
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import FactsView
    import ansible.module_utils.facts.system.distribution as dist_utils
    # mock module
    class MockModule(object):
        def __init__(self):
            self.run_command = mock.Mock()
            self.run_command.return_value = (0, 'Current: =ep', '')
        def get_bin_path(self, path):
            return '/usr/local/bin/capsh'

    mock_module = MockModule()
    # call object under test
    capsh_fact_collector = get_collector_instance

# Generated at 2022-06-13 02:23:42.500451
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test if capsh is present and if it is run successfully
    """
    import os
    import platform
    module_path = os.path.dirname(os.path.abspath(__file__)) + "/fixtures"
    if platform.system() == 'Linux':
        capsh_path = '/usr/bin/capsh'
    else:
        capsh_path = '/bin/sh'
    mock_module = MockModule(capsh_path=capsh_path)
    # If capsh is not present
    mock_module.run_command = Mock(return_value=(1, '', 'no capsh'))

    coll = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:23:50.831396
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    try:
        import ansible.module_utils.facts.hardware.linux
        import ansible.module_utils.facts.system.linux
        import ansible.module_utils.facts.virtual.linux
        import ansible.module_utils.facts.collector
    except:
        import ansible.module_utils.facts.hardware.linux
        import ansible.module_utils.facts.system.linux
        import ansible.module_utils.facts.virtual.linux
        import ansible.module_utils.facts.collector

    sut = ansible.module_utils.facts.collector.BaseFactCollector()

    # set up parameters
    module = sut

    # invoke method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:24:00.278768
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Test the SystemCapabilitiesFactCollector._collect() method."""
    # Stub out module.run_command() to return capsh's output
    import sys
    import ansible.module_utils.facts.collector.system.caps as caps
    from unittest.mock import patch

    # Mock out the helper methods to isolate this test, then revert to originals
    caps_helper_patcher = patch.object(caps, 'get_bin_path')
    caps_helper_patcher.start()

    if sys.version_info >= (2, 7):
        import builtins
        original_open = builtins.open
        builtins.open = open
    else:
        import __builtin__
        original_open = __builtin__.open
        __builtin__.open = open


# Generated at 2022-06-13 02:24:08.617666
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys
    import shutil
    import tempfile
    import subprocess
    import pytest


    @pytest.fixture()
    def temp_mingw_bindir(request):
        """Return path to temporary MinGW binaries directory."""
        import os
        import sys
        import shutil
        import tempfile
        import subprocess

        mingw_bindir = tempfile.mkdtemp()
        if sys.version_info >= (2, 7):
            subprocess.check_call([
                'gcc',
                '-g',
                '-Wall',
                '-Werror',
                '-o', os.path.join(mingw_bindir, 'capsh.exe'),
                '-xc', request.param,
            ])

# Generated at 2022-06-13 02:24:14.994105
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible.module_utils.facts.collector import get_collector

    # Expected results for a system with enforced capabilities (True)
    enforced_caps_result = {
                            'system_capabilities': ['setuid', 'setgid', 'setpcap', 
                                                    'setfcap', 'sys_pacct', 'sys_admin', 
                                                    'sys_nice', 'sys_resource', 'sys_time', 
                                                    'sys_tty_config', 'mknod', 'audit_write', 
                                                    'audit_control', 'mac_override', 
                                                    'mac_admin', 'syslog', 'wake_alarm', 
                                                    'block_suspend'],
                            'system_capabilities_enforced': 'True'
                           }

   

# Generated at 2022-06-13 02:24:16.391413
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:24:21.681310
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:24:30.663684
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    fact_collector = SystemCapabilitiesFactCollector()

    # NOTE: get_caps_data()/parse_caps_data() for easier mocking -akl
    # NOTE: mock needs to be fixed/changed when
    # SystemCapabilitiesFactCollector.collect() is refactored and unindented.

# Generated at 2022-06-13 02:25:08.762170
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import ModuleStub
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

    capsh_cmd_output = """Current: =ep
Bounding set =ep
Securebits: 00/0x0/1'b0 secure-noroot, secure-no-suid-fixup secure-keep-caps
  secure-noroot secure-no-suid-fixup secure-keep-caps
  ambient-caps=EP
CapEff: =ep
CapInh: 
CapPrm: 
CapAmb: =ep"""

    module = ModuleStub()

# Generated at 2022-06-13 02:25:18.628492
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    def get_bin_path(arg):
        return "/bin/capsh"

    def run_command(command, errors):
        return (0, 'Current: =ep', '')

    def mock_module(bin_path_func, run_cmd_func):
        class MockModule(object):
            get_bin_path = bin_path_func
            run_command = run_cmd_func
        return MockModule()

    out = SystemCapabilitiesFactCollector.collect(module=mock_module(get_bin_path, run_command))
    assert out['system_capabilities_enforced'] == 'False'
    assert out['system_capabilities'] == []

    def run_command(command, errors):
        return (0, 'Current: =eip', '')


# Generated at 2022-06-13 02:25:28.016558
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock()

# Generated at 2022-06-13 02:25:33.163228
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    1. Success - populated
    2. Success - empty
    """

    # 1. Success - populated
    # NOTE: for better mocking, split into: get_caps_data() & parse_caps_data() -akl
    module = Mock()

# Generated at 2022-06-13 02:25:42.329803
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os

    module = type('MockModule', (), {})()
    capsh_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'capsh')
    module.get_bin_path = lambda x: capsh_path
    module.run_command = lambda x, **kwargs: (0, "Current: =ep", "")

    if os.path.exists(capsh_path):
        facts_dict = SystemCapabilitiesFactCollector().collect(module=module)
        assert facts_dict['system_capabilities_enforced'] == 'False'
        assert facts_dict['system_capabilities'] == []

# Generated at 2022-06-13 02:25:50.587494
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    This unit test checks that run_command is called and that function exits properly
    """

    # Define parameters
    params = {'run_command': [{'bin_path': 'capsh', 'check_rc': True,
                               'data': '', 'executable': None,
                               'path_prefix': None, 'prompt': None,
                               'remove_tmp': True, 'split_lines': True,
                               'strip_empty_ends': True}],
              'capsh_path':'capsh'}

    # Define module object
    module = object

    # Define output of run_command
    module.run_command = [0, 'Current: =ep', '']

    # Define data to be returned

# Generated at 2022-06-13 02:25:51.257337
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: Implement
    assert False

# Generated at 2022-06-13 02:26:01.177209
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class TestModule(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, capsh_path, required=False, opt_dirs=[]):
            return '/usr/bin/capsh'

        def run_command(self, cmd, errors='strict'):
            return self.rc, self.out, self.err

    class TestModuleFail(object):
        def get_bin_path(self, capsh_path, required=False, opt_dirs=[]):
            return 'capsh'

    fact_collector = SystemCapabilitiesFactCollector()
    enforced = 'False'

# Generated at 2022-06-13 02:26:09.117649
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(object):
        @staticmethod
        def get_bin_path(binary):
            return '/bin/capsh'


# Generated at 2022-06-13 02:26:19.260779
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Test running with a capsh binary
    mock_module = MagicMock()
    mock_module.run_command.return_value = (0, 'Current: =ep', '')
    mock_module.get_bin_path.return_value = '/usr/bin/capsh'

    collector = SystemCapabilitiesFactCollector(module=mock_module)
    facts = collector.collect()

    # Verify the run_command() of mock_module.
    mock_module.run_command.assert_called_once_with(['/usr/bin/capsh', '--print'], errors='surrogate_then_replace')

    # Verify the results.
    assert facts == {'system_capabilities': [],
                     'system_capabilities_enforced': 'False'}


# Generated at 2022-06-13 02:27:24.944143
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test method `collect` of class SystemCapabilitiesFactCollector.
    """
    test_module = SystemCapabilitiesFactCollector()
    test_module.get_bin_path('capsh')
    test_module.run_command()

# Generated at 2022-06-13 02:27:30.319703
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class FakeModule:
        def __init__(self, *args, **kwargs):
            pass

        def get_bin_path(self, *args, **kwargs):
            return 'capsh'

        def run_command(self, *args, **kwargs):
            return (0, 'Current: =ep', None)

    false_collector = SystemCapabilitiesFactCollector()
    false_facts = false_collector.collect(module=FakeModule())
    assert false_facts['system_capabilities_enforced'] == 'False'
    assert len(false_facts['system_capabilities']) == 0

    true_collector = SystemCapabilitiesFactCollector()
    true_facts = true_collector.collect(module=FakeModule())
    assert true_facts['system_capabilities_enforced'] == 'True'


# Generated at 2022-06-13 02:27:40.595199
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os
    import re

    class ModuleStub():
        def get_bin_path(self, command):
            if command == 'capsh':
                if sys.platform == 'darwin':
                    return '/bin/bash'
                else:
                    return '/bin/capsh'

        def run_command(self, args, errors='surrogate_then_replace'):
            if args[0] == '/bin/capsh':
                return 0, 'Current: =ep', ''
            elif args[0] == '/bin/bash':
                if '-c' in args and re.match("capsh --print", args[-1]):
                    return 0, 'Current: =ep', ''
                else:
                    return 0, '', ''
            else:
                return 1, '', ''


# Generated at 2022-06-13 02:27:42.361438
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    caps_facts = SystemCapabilitiesFactCollector()
    assert isinstance(caps_facts.collect(), dict)

# Generated at 2022-06-13 02:27:50.947139
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: create mock class, initialize, create stubs -akl
    # NOTE: -> get_caps_data()/parse_caps_data() for easier mocking -akl
    # NOTE: -> access to protected member -akl
    collector = SystemCapabilitiesFactCollector()
    collector._module.run_command.return_value = (0, '', '')
    collector._module.get_bin_path.return_value = '/bin/capsh'

# Generated at 2022-06-13 02:28:01.036230
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector
    import ansible.module_utils.facts.system.capabilities

    # NOTE: mock _capability_run() to return fake data -akl
    class MyModule():

        def get_bin_path(self, name):
            return '/bin/capsh'

        def run_command(self, args, **kwargs):
            return (0, MY_FAKE_CAPSH_OUT, '')


# Generated at 2022-06-13 02:28:06.101784
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = FakeAnsibleModule()
    task_vars = dict(ansible_facts=dict(system_capabilities=["cap_setpcap", "cap_net_raw"]))
    result = task_vars['ansible_facts']['system_capabilities']
    assert isinstance(result, list)
    assert result == ["cap_setpcap", "cap_net_raw"]

# Generated at 2022-06-13 02:28:08.283815
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = object()
    collected_facts = object()
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect(module, collected_facts) == {}

# Generated at 2022-06-13 02:28:10.982359
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test for method collect of class SystemCapabilitiesFactCollector
    """
    fact_collector = SystemCapabilitiesFactCollector()
    assert fact_collector.collect() == {'system_capabilities': [], 'system_capabilities_enforced': 'NA'}

# Generated at 2022-06-13 02:28:21.553025
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys

    # mock module obj
    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.args = args
            self.kwargs = kwargs
            self._ansible_version = '2.9.6'
            self._ansible_debug = False
            self._ansible_diff = False
            self._ansible_verbosity = 0
            self._ansible_check_mode = False
            self._ansible_no_log = False
            self.mock_run_command = 'mock-run-command'
            self.mock_caps_data = CAPS_DATA
            self.mock_get_bin_path = lambda x: x
