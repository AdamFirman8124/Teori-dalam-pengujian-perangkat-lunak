

# Generated at 2022-06-13 02:19:53.974784
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule(object):
        def run_command(self, command):
            class MockResult(object):
                def __init__(self, rc=0, out='', err=''):
                    self.rc = rc
                    self.out = out
                    self.err = err
            return MockResult()

    module = MockModule()
    sut = SystemCapabilitiesFactCollector()
    result = sut.collect(module=module)
    assert 'system_capabilities' in result
    assert 'system_capabilities_enforced' in result

# Generated at 2022-06-13 02:20:04.389804
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:20:12.231281
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    In this test, MockModuleHelper is used to mock a module and the
    SystemCapabilitiesFactCollector class is instantiated with it.
    The collect method is then called and the module.run_command method
    is tested for proper usage.

    The test for the output of the collect method is implemented in
    test_get_system_capabilities_facts.py
    """
    import ansible.module_utils.facts.collectors.system.system_capabilities

    from ansible.module_utils.facts.collectors.system.system_capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils._text import to_bytes

    import ansible.module_utils.facts.collectors.system

    module = MockModuleHelper(argument_spec={})

    capsh_path = '/usr/bin/capsh'
   

# Generated at 2022-06-13 02:20:20.420168
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mod = Mock()
    mod.get_bin_path.return_value = None
    path = '/usr/bin/capsh'
    sys_cap = 'cap_net_raw,cap_sys_chroot=ep'
    sys_cap_enforced = 'False'
    out = 'Current: =ep\nBounding set =cap_net_raw,cap_sys_chroot\n'
    err = ''
    rc = 0

    mod.run_command.return_value = (rc, out, err)

    mod.get_bin_path.return_value = path
    sys_cap_dict = {}
    sys_cap_dict['system_capabilities'] = [i.strip() for i in sys_cap.split(',')]
    sys_cap_dict['system_capabilities_enforced'] = sys_

# Generated at 2022-06-13 02:20:25.549801
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = FakeAnsibleModule()
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect(module)

    assert 'system_capabilities' in result.keys()
    assert 'system_capabilities_enforced' in result.keys()
    assert 'NA' in result.values()

# Class which simulates an 'ansible.module_utils.basic.AnsibleModule' instance

# Generated at 2022-06-13 02:20:36.509136
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector

    class TestModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name):
            # on test machines capsh is available in /usr/sbin
            if name == 'capsh':
                return '/usr/sbin/capsh'
            else:
                return None


# Generated at 2022-06-13 02:20:47.869214
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys
    import platform
    import types
    import tempfile

    import ansible.module_utils.facts.collector.system.system.collectors.capsh as capsh
    import ansible.module_utils.facts.collector.system.system.core as sys_core

    # a simple mock module and module.run_command()
    class MockModule():
        @staticmethod
        def get_bin_path(name, *args, **kwargs):
            if name == 'capsh':
                return "/usr/bin/capsh"
            return None


# Generated at 2022-06-13 02:20:58.579091
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    SystemCapabilitiesFactCollector.collect() collect facts related to systems'
    capabilities via 'capsh' command.
    """
    class mockmodule:
        def get_bin_path(self, path):
            return '/bin/capsh'

        def run_command(self, command, errors):
            return 0, "Current: =ep", ""

    class mockmodule2:
        def get_bin_path(self, path):
            return '/bin/capsh'

        def run_command(self, command, errors):
            return 0, "Current:   =ep", ""

    class mockmodule3:
        def get_bin_path(self, path):
            return '/bin/capsh'

        def run_command(self, command, errors):
            return 0, "Current: =ep=ep", ""


# Generated at 2022-06-13 02:20:59.517135
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass # TODO



# Generated at 2022-06-13 02:21:01.636298
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: how to mock this
    pass

# Generated at 2022-06-13 02:21:11.827111
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    def run_command_mock(module, args, errors='surrogate_then_replace'):
        capsh_path = module.get_bin_path('capsh')

# Generated at 2022-06-13 02:21:19.456423
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # create class instance
    c = SystemCapabilitiesFactCollector()
    # configure the following return values
    c.module = None
    c.collected_facts = {}
    # run the method
    returned_facts = c.collect()
    # assert expected results
    assert returned_facts == {}
    # configure the following return values
    c.module = None
    c.collected_facts = {}
    c.module.get_bin_path.return_value = '/usr/bin/capsh'
    c.module.run_command.return_value = ('0', 'Current: =ep', 'error')
    # run the method
    returned_facts = c.collect()
    # assert expected results
    assert returned_facts == {'system_capabilities_enforced': 'False', 'system_capabilities': []}
    #

# Generated at 2022-06-13 02:21:26.456687
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    Test collect method of class SystemCapabilitiesFactCollector
    '''
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.capabilities import SystemCapabilitiesFactCollector

    collector.collectors['ansible_facts.system.capabilities'] = SystemCapabilitiesFactCollector()
    print(collector.collectors['ansible_facts.system.capabilities'].collect(module=None, collected_facts=None))

# Generated at 2022-06-13 02:21:37.414511
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:21:38.820011
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:39.790667
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO -akl
    pass

# Generated at 2022-06-13 02:21:40.373975
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:49.740852
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector

    # NOTE: in unit tests, double underscore members are not wrapped
    #       (i.e. _BaseFactCollector__get_caps_data) -akl

# Generated at 2022-06-13 02:21:57.853602
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """This is a test for verifying that collectors.system_capabilities.SystemCapabilitiesFactCollector._collect
    collects facts related to systems capabilities per capsh output.
    """
    # create a SystemCapabilitiesFactCollector instance
    fact_collector = SystemCapabilitiesFactCollector()
    # create a mock module without 'capsh'
    module = lambda: None
    setattr(module, 'get_bin_path', lambda x: None)
    # collect facts and verify expected facts
    assert dict() == fact_collector.collect(module)

    # create a mock module with 'capsh'
    module = lambda: None
    setattr(module, 'get_bin_path', lambda x: '/usr/bin/capsh')

# Generated at 2022-06-13 02:22:04.332335
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import re
    from ansible.module_utils.six import StringIO
    from ansible.module_utils import basic
    ansible_module = basic.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

# Generated at 2022-06-13 02:22:18.346697
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import _parse_caps_data as parse_caps_data
    from ansible.module_utils.facts.system.caps import _get_caps_data as get_caps_data
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    import os
    import re

    # setting global value in the module to True
    # the module is used in test_SystemCapabilitiesFactCollector_collect
    SystemCapabilitiesFactCollector._fact_ids = True

    # test running with pypy and with python

# Generated at 2022-06-13 02:22:19.449802
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    SystemCapabilitiesFactCollector.collect should return capabilities
    """
    assert True

# Generated at 2022-06-13 02:22:29.547183
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    try:
        import  mock
    except:
        # Do nothing for now if python-mock isn't installed
        pass
    else:
        from ansible.module_utils.facts.collector import BaseFactCollector
        from ansible.module_utils.facts.collectors.system.capabilities import SystemCapabilitiesFactCollector
        from ansible.module_utils.facts.collectors.system import CapshMock
        from ansible.module_utils._text import to_bytes
        from ansible.module_utils.facts import get_collector_instance
        from ansible.module_utils.six import iteritems

        module_mock_args = dict(
            get_bin_path=CapshMock().get_bin_path,
            run_command=CapshMock().run_command,
        )

        module_

# Generated at 2022-06-13 02:22:34.372390
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    TestModule = type('TestModule', (object,), {
        'run_command': lambda self, command, errors=None: (0, "Current: =ip\nVersion: 2.23", None)
    })
    test_module = TestModule()

    fact_collector = SystemCapabilitiesFactCollector()
    facts = fact_collector.collect(module=test_module)

    assert facts["system_capabilities"] == []
    assert facts["system_capabilities_enforced"] == 'False'



# Generated at 2022-06-13 02:22:43.744841
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import inspect

    # NOTE: This is somewhat silly, but the code is already in place and
    #       all it needs is a pseudo-module argument.
    #       I'm hesitant to change the structure of the code, as it does seem
    #       to work as it is (with the addition of mock.patch, of course).
    #       -akl
    mock_module = Mock()
    mock_module.run_command.return_value = (0, 'Current: =ep', '')
    mock_module.get_bin_path.return_value = '/sudo/capsh'
    mock_module.check_mode.return_value = False

    # NOTE: I'm not sure why the temp config is needed, but that's what's there.
    #       It's possible this is some sort of vestige of the older code (when
    #      

# Generated at 2022-06-13 02:22:54.276584
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector.system
    import platform
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes

    # Create 'SystemCapabilitiesFactCollector' object
    module = ansible.module_utils.facts.collector.system.SystemCapabilitiesFactCollector()
    # Mock values for 'run_command()' method
    module.run_command = lambda x, **kwargs: (0, 'Current: =ep', '')

    module.get_bin_path = lambda x: '/bin/capsh'

    # Assert none of the following values are empty
    assert module.name
    assert module._fact_ids
    assert module.collect()

# Generated at 2022-06-13 02:23:05.636908
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fake_module = [{'run_command.return_value': (0, 'Current: = cap_net_bind_service,cap_net_raw+eip\nBounding set =cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap+eip\nSecurebits: 00/0x0/1\'b0 secure-noroot,secure-no-suid-fixup secure-keep-caps\nAmbient set =\n', '')}, {'get_bin_path.return_value': 'capsh'}]
    system

# Generated at 2022-06-13 02:23:13.448106
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    ''' Unit test for method collect of class SystemCapabilitiesFactCollector '''
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector as capsh_class

# Generated at 2022-06-13 02:23:23.550970
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test collect method of class SystemCapabilitiesFactCollector.
    Assumes that the execution of capsh command completes successfully.
    """
    import os

    class MockModule(object):
        def __init__(self):
            self.path_exists_map = {'capsh': True}
            self.command_results_map = {
                'capsh --print': (
                    0,
                    '\nCurrent:\t= cap_chown,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid+ep',
                    ''
                )
            }

        def get_bin_path(self, app, opt_dirs=[]):
            return self.path_exists_map[app]


# Generated at 2022-06-13 02:23:26.509512
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    assert SystemCapabilitiesFactCollector.collect() == {}

# Generated at 2022-06-13 02:23:39.040907
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test = SystemCapabilitiesFactCollector()
    result = test.collect()

# Generated at 2022-06-13 02:23:39.605353
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:23:49.008864
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # arrange
    module = AnsibleModule()
    capsh_path = module.get_bin_path('capsh')
    rc, out, err = module.run_command([capsh_path, "--print"], errors='surrogate_then_replace')
    enforced_caps = []
    enforced = 'NA'
    for line in out.splitlines():
        if len(line) < 1:
            continue
        if line.startswith('Current:'):
            if line.split(':')[1].strip() == '=ep':
                enforced = 'False'
            else:
                enforced = 'True'
                enforced_caps = [i.strip() for i in line.split('=')[1].split(',')]


# Generated at 2022-06-13 02:23:52.540341
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    ''' Unit test for method collect of class SystemCapabilitiesFactCollector '''
    from ansible.module_utils.facts import ansible_collector

    caps = ansible_collector.get_collector('caps')
    print(caps)
    assert caps is not None
    facts = caps.collect()
    print(facts)
    assert 'system_capabilities_enforced' in facts
    assert 'system_capabilities' in facts

# Generated at 2022-06-13 02:24:01.300359
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts import _system_capabilities_facts

    collector = get_collector_instance(_system_capabilities_facts)

    # mock module and its capabilities
    m = Mock()
    m.get_bin_path.return_value = 'capsh_path'
    m.run_command.return_value = 0, ('Current: = cap_sys_admin,cap_sys_chroot',), ''

    # execute method to be tested
    collector.collect(m)

    # assert result
    assert m.mock_calls == [call.get_bin_path('capsh'), call.run_command(['capsh_path', '--print'])]

# Generated at 2022-06-13 02:24:08.992779
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()

    module = collector.module

    # return an empty dict if module is not runable
    assert collector.collect() == {}

    module.params['capsh'] = True
    module.run_command = MagicMock(return_value=(0, 'a\nCurrent: =ep\n', ''))
    # return system capabilities and system_capabilities_enforced is set False
    assert collector.collect() == {'system_capabilities_enforced': 'False',
                                   'system_capabilities': []}

    module.run_command = MagicMock(return_value=(0, 'a\nCurrent: =eip\n', ''))
    # return system capabilities and system_capabilities_enforced is set True

# Generated at 2022-06-13 02:24:15.262805
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    This test is just for code coverage as the code is very hard to test.

    Args:
        mock_ansible_module (MagicMock): Mocked ansible module instance.
        test_instance (MagicMock): Mocked class instance.
    """
    mock_ansible_module = MagicMock()
    test_instance = SystemCapabilitiesFactCollector(mock_ansible_module)

    # Test with capsh_path not None
    mock_ansible_module.get_bin_path.return_value = 'capsh_path'
    mock_ansible_module.run_command.return_value = [do_not_use, '=ep', do_not_use]
    expected_result = dict(system_capabilities_enforced='False', system_capabilities=[])

# Generated at 2022-06-13 02:24:24.594679
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class TestHost(object):
        def __init__(self, output, return_code):
            self.output = output
            self.return_code = return_code

        def run_command(self, cmd):
            return self.return_code, self.output, None

    # Test for capabilities enforced

# Generated at 2022-06-13 02:24:25.088601
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:24:26.490496
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:24:54.919025
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    This is a unit test of method collect of class SystemCapabilitiesFactCollector
    It only covers the case where 'capsh' is not available.
    """
    # Inputs
    fact_collector = SystemCapabilitiesFactCollector()
    module = None

    # Expected results
    expected_results = {}

    # Perform the test
    result = fact_collector.collect(module)

    # Assertions
    assert result == expected_results


# Generated at 2022-06-13 02:24:58.950558
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    with patch("ansible.module_utils.facts.collector.BaseFactCollector.collect", return_value=None):
        fixture = SystemCapabilitiesFactCollector()
        result = fixture.collect()
        assert {} == result

# Generated at 2022-06-13 02:25:01.497981
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test = SystemCapabilitiesFactCollector()
    result = test.collect()
    assert result.get('system_capabilities_enforced') == 'NA'
    assert result.get('system_capabilities') == []

# Generated at 2022-06-13 02:25:07.347102
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import Collector
    from ansible.module_util.facts.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Create instance of class BaseFactCollector
    base_fact_collector_instance = BaseFactCollector()
    # Create instance of class SystemCapabilitiesFactCollector
    system_capabilities_fact_collector_instance = SystemCapabilitiesFactCollec

# Generated at 2022-06-13 02:25:13.186432
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # create instance of SystemCapabilitiesFactCollector
    system_capability_collector = SystemCapabilitiesFactCollector()

    # create an ansible module
    class AnsibleModuleMock(object):
        class RunCommandResultMock(object):
            def __init__(self, rc=0, out='', err=''):
                self.rc = rc
                self.out = out
                self.err = err


# Generated at 2022-06-13 02:25:23.679421
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector

    # NOTE: mock AnsibleModule
    # NOTE: -> class DummyAnsibleModule (construct w args /me)
    # NOTE: -> -> get_bin_path()
    # NOTE: -> -> run_command()
    # NOTE: -> -> fail_json()
    class DummyAnsibleModule(object):
        class AnsibleModule(object):
            def __init__(self, obj):
                self.obj = obj

            def get_bin_path(self, path, required=False, opt_dirs=None):
                return '/bin/bash'


# Generated at 2022-06-13 02:25:24.177590
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:26.383480
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: get_caps_data()/parse_caps_data() for easier mocking -akl
    pass


# Generated at 2022-06-13 02:25:33.439475
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    import sys
    import textwrap

    from ansible.module_utils.facts.collector import BaseFactCollector

    from io import StringIO

    class MockModule:
        def __init__(self):
            self.fail_json_called = False
            self.params = {}

        def fail_json(self, *args, **kwargs):
            self.fail_json_called = True
            self.fail_json_args = args
            self.fail_json_kwargs = kwargs

        def get_bin_path(self, *args, **kwargs):
            return "capsh"


# Generated at 2022-06-13 02:25:43.993908
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Verifies that system_capabilities_enforced, system_capabilities are returned as expected
    from ansible.module_utils.facts.utils.capabilities import Capabilities

    Capabilities.get_caps_data = lambda self: (0, "Current: =ep", '')
    system_caps_fact_collector = SystemCapabilitiesFactCollector(None)
    res_dict = system_caps_fact_collector.collect()
    assert res_dict['system_capabilities_enforced'] == 'False'
    assert res_dict['system_capabilities'] == []

    # Verifies that system_capabilities_enforced, system_capabilities are returned as expected

# Generated at 2022-06-13 02:26:48.923695
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: rough draft; deliberate duplication of functionality from
    # SystemCapabilitiesFactCollector.collect()
    class FakeModule(object):

        def __init__(self, caps_data=None, caps_path=None, caps_rc=0, caps_err=''):
            self.caps_data = caps_data
            self.caps_path = caps_path
            self.caps_rc = caps_rc
            self.caps_err = caps_err

        def get_bin_path(self, name, opts=None, required=False):
            return self.caps_path

        def run_command(self, cmd, errors='surrogate_then_replace'):
            return self.caps_rc, self.caps_data, self.caps_err


# Generated at 2022-06-13 02:26:54.619467
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: create mock module and its run_command result -akl
    # capsh_path mock module
    facts_dict = SystemCapabilitiesFactCollector().collect()
    # Check for facts_dict keys and their values
    # TODO: test for valid output with && without capabilities enforced -akl
    assert 'system_capabilities_enforced' in facts_dict
    assert 'system_capabilities' in facts_dict



# Generated at 2022-06-13 02:27:03.184325
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test SystemCapabilitiesFactCollector::collect. If capsh is
    installed on any supported distribution, the following
    keys and their respective values will be included in the
    collected facts:

    - system_capabilities
    - system_capabilities_enforced

    If capsh is not available, these keys will be missing.
    """

    import sys
    import os
    import tempfile
    import shutil
    import ansible.module_utils.facts.system.caps as caps

    # Create fake capsh executable
    tmp_dir = tempfile.mkdtemp()
    capsh_path = "%s/capsh" % tmp_dir


# Generated at 2022-06-13 02:27:13.518279
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_facts

    # NOTE: ansible_facts_collector does not exist
    #       without 'collectors'
    for c in ansible_facts.collectors:
        c.collect = MagicMock(name='collect')

    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

    c = SystemCapabilitiesFactCollector()
    assert c.collect(module=None, collected_facts=None) == {}
    assert c.collect(module=MagicMock(name='module'), collected_facts=None) == {}

# Generated at 2022-06-13 02:27:23.304439
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    mod = ansible.module_utils.facts.collector.BaseFactCollector

    class MockModule(object):
        def __init__(self, capsh_path):
            self.caps_path = capsh_path

        def get_bin_path(self, command):
            return self.caps_path


# Generated at 2022-06-13 02:27:29.278624
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collection_mock
    from ansible.module_utils.facts import ansible_module_mock


# Generated at 2022-06-13 02:27:39.566248
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:27:49.129855
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import LocalCollector
    from ansible.module_utils.facts.collector import CachingCollector, BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_lines

    LocalCollector.available = False
    get_collector_instance.reset_cache()
    # NOTE: cache_then_local can be removed when LocalCollector is available
    cache_then_local_fact_collector = CachingCollector(get_collector_instance('cache_then_local'),
                                                       'cache_then_local_facts',
                                                       '/tmp/ansible_local_facts_cache')
    SystemCapabilitiesFactCollector.available = True
    get_collect

# Generated at 2022-06-13 02:28:00.119340
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_text

    sut = SystemCapabilitiesFactCollector()
    m_capsh_path = '/bin/capsh'
    m_run_command = ['capsh', '--print']

    def get_bin_path(module):
        return m_capsh_path


# Generated at 2022-06-13 02:28:09.081897
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    system_cap_collector = SystemCapabilitiesFactCollector()
    system_cap_collector.module = None
    result = system_cap_collector.collect()
    assert(result == {})

    system_cap_collector.module = "Test"
    system_cap_collector.module.get_bin_path = lambda x: None
    result = system_cap_collector.collect()
    assert(result == {})

    system_cap_collector.module = "Test"
    system_cap_collector.module.get_bin_path = lambda x: "/bin/sh/capsh"
    system_cap_collector.module.run_command = lambda x, y: (0, "Current: =ep\n", "Error")
    result = system_cap_collector.collect()