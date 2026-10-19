

# Generated at 2022-06-13 02:19:55.761498
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = None
    system_capabilities_enforced = 'True'
    system_capabilities = ['=ep', 'cap_setuid+ep', 'cap_setgid+ep', 'cap_sys_admin+ep', 'cap_dac_override+ep', 'cap_net_admin+ep']

    class Capsh:
        def __init__(self, capsh_path, cmd, errors):
            self.codes = 0, 'Current: =ep\nBounding set =cap_setuid+ep,cap_setgid+ep,cap_sys_admin+ep,cap_dac_override+ep,cap_net_admin+ep', ''

        @property
        def rc(self):
            return self.codes[0]


# Generated at 2022-06-13 02:20:06.440906
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # NOTE: In this unit test, system_capabilities and system_capabilities_enforced
    # should always be present in the result as they are keys of the facts_dict
    # returned by method collect of class SystemCapabilitiesFactCollector

    # CASE: capsh is not present
    # NOTE: method get_bin_path returns None if capsh is not installed
    module = MagicMock()
    module.get_bin_path.return_value = None
    result = SystemCapabilitiesFactCollector.collect(module=module, collected_facts=None)

    assert result == {'system_capabilities': [], 'system_capabilities_enforced': 'NA'}
    module.get_bin_path.assert_called_once_with('capsh')


    # CASE: capsh is present but there is an error
    module = MagicM

# Generated at 2022-06-13 02:20:09.396227
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    ''' Test case for collect method of SystemCapabilitiesFactCollector
    '''
    # This currently generates a SystemCapabilitiesFactCollector instance
    # with self.module as None
    collector = SystemCapabilitiesFactCollector()
    # You cannot unit test collect() as you don't have a module, which is
    # required in the collect() method
    # TODO: What should we do? -akl
    assert collector.collect() == {}

# Generated at 2022-06-13 02:20:17.218702
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # call tested method
    from ansible_collections.ansible.community.tests.unit.plugins.module_utils.facts import ModuleUtilsGenericTestFacts
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector(
        ModuleUtilsGenericTestFacts(None, None, None))
    capabilities = system_capabilities_fact_collector.collect()

    assert 'system_capabilities_enforced' in capabilities
    assert 'system_capabilities' in capabilities
    assert isinstance(capabilities['system_capabilities_enforced'], str)
    assert isinstance(capabilities['system_capabilities'], list)

# Generated at 2022-06-13 02:20:24.593105
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Simple test of the method collect of SystemCapabilitiesFactCollector
    # class when a capsh_path is not given. This causes the method
    # to early exit and return an empty dict.
    from ansible.module_utils.facts import collector

    sut = SystemCapabilitiesFactCollector()

    out = sut.collect(None, None)

    assert out == {}

    # Simple test of the method collect of SystemCapabilitiesFactCollector
    # class when a capsh_path is given. This causes the method
    # to return a dict containing the fact ids 'system_capabilities' and
    # 'system_capabilities_enforced' and their corresponding vals.
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.basic
   

# Generated at 2022-06-13 02:20:35.713239
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collectors.system import SystemCapabilitiesFactCollector

    global module
    module = MockAnsibleModule()
    global module
    module = MockAnsibleModule()
    global enforce
    enforce = 'True'
    global capsh
    capsh = 'True'
    global caps
    caps = []
    global out
    out = 'Current: =ep'
    global rc
    rc = 'NA'
    global err
    err = 'NA'

    sut = SystemCapabilitiesFactCollector()
    result = sut.collect(module=module, collected_facts={})
    assert rc == 'NA'
    assert err == 'NA'
    assert capsh == 'True'
    assert next(iter(result.keys())) == 'system_capabilities_enforced'

# Generated at 2022-06-13 02:20:43.423896
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.system.capabilities import SystemCapabilitiesFactCollector

    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand

    capsh_path = module.get_bin_path('capsh')

    facts = FactCollector().collect(module=module)
    SystemCapabilitiesFactCollector().collect(module=module, collected_facts=facts)

    assert 'system_capabilities' in facts['ansible_facts']

# Generated at 2022-06-13 02:20:50.860463
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # test case #1
    mock_module = None
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector()
    result = system_capabilities_fact_collector.collect(mock_module)
    assert result == {}

    # test case #2
    mock_module = MagicMock()
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector()
    result = system_capabilities_fact_collector.collect(mock_module)
    assert result == {}

    # test case #3
    mock_module = MagicMock()
    mock_module.get_bin_path.return_value = "/usr/bin/capsh"

# Generated at 2022-06-13 02:21:01.367504
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Init class
    collect = SystemCapabilitiesFactCollector()
    # Get module args
    module_args = dict()

    def get_bin_path(arg):
        return '/sbin/capsh'

    # Init module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    setattr(module, 'get_bin_path', get_bin_path)

    def run_command(params, errors=None):
        output = "Current: =ep\n"
        output += "Bounding set =cap_chown,cap_dac_override,cap_dac_read_search,"
        output += "cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,"

# Generated at 2022-06-13 02:21:10.358874
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # 1. create an instance of the class in question
    fact_collector = SystemCapabilitiesFactCollector()

    # 2. create a return value for the collect() method
    # NOTE: not using the 'out' tuple defined in the collect() method
    #       but assigning the first return item directly to the
    #       return_dict
    #       (1) return_dict = {'system_capabilities': <enforced_caps>,
    #                          'system_capabilities_enforced': <enforced>}
    return_dict = {'system_capabilities': ['chown', 'fowner', 'fsetid',
                                           'net_bind_service', 'net_raw',
                                           'setfcap', 'setpcap', 'sys_chroot'],
                   'system_capabilities_enforced': 'True'}

# Generated at 2022-06-13 02:21:20.389694
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Mock module args
    test_module = dict(
        run_command=dict(
            return_value=(
                0,
                "Current: =ep",
                ""),
        ),
        get_bin_path=dict(
            return_value='/usr/bin/capsh'),
        )

    # Run collect() with above mocked object
    actual_output = SystemCapabilitiesFactCollector().collect(test_module, test_module)

    assert actual_output == dict(
        system_capabilities_enforced='False',
        system_capabilities=[],
    )

# Generated at 2022-06-13 02:21:31.635180
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Initializing mock module and SystemCapabilitiesFactCollector object
    module = Mock()
    caps_fact = SystemCapabilitiesFactCollector()

    # Returing empty dictionary
    module = Mock()
    module.get_bin_path = Mock(return_value=None)
    caps_fact = SystemCapabilitiesFactCollector()
    output = caps_fact.collect(module)
    expected_data = {}
    assert output == expected_data

    # Returing expected data for enforced and capabilities
    module.run_command = Mock(return_value=(0, "Current: =ep\n", ''))
    output = caps_fact.collect(module)
    expected_data = {
        'system_capabilities': [],
        'system_capabilities_enforced': 'False'
    }
    assert output == expected_data

    # Ret

# Generated at 2022-06-13 02:21:32.810652
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:40.152797
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    module.run_command = lambda *args, **kwargs: (0, "Current: =ep\nBounding set =cap_net_bind_service,cap_net_admin,cap_net_raw+eip\nSecurebits: 00/0x0/1'b0 secure-noroot, secure-no-suid\nSecure-noroot secure-no-suid\ncap_net_bind_service = cap_net_bind_service\ncap_net_admin = cap_net_admin\ncap_net_raw = cap_net_raw+eip\n")
    collector.collectors.append(SystemCapabilitiesFactCollector())

# Generated at 2022-06-13 02:21:49.598020
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    Unit test for method collect of class SystemCapabilitiesFactCollector
    '''
    import mock
    import tempfile
    class FakeResult():
        def __init__(self, output, error, rc):
            self.output = output
            self.error = error
            self.rc = rc
        def __call__(self, *args, **kwargs):
            return (self.output, self.error, self.rc)

    capsh_path = tempfile.mkstemp(prefix='ansible-')[1]

# Generated at 2022-06-13 02:21:57.701284
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.system_capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.utils.caps_data import get_caps_data

    # Test when capsh is not available
    test_SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector('', '', '', '')

    assert test_SystemCapabilitiesFactCollector.collect() == {}

    # Test when capsh is available
    mock_module_helper = Mock()
    mock_module_helper.get_bin_path.return_value = '/usr/bin/capsh'
    mock_module_helper.run_command.return_value = (0, get_caps_data(), '')

    test_SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector('', '', '', '')


# Generated at 2022-06-13 02:22:06.516890
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    def run_cmd(args, errors='strip'):
        rc = 0
        out = "Current: =ep\n"
        err = ''
        return (rc, out, err)

    import sys
    import os
    import socket
    import json
    import tempfile

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import cached
    from ansible.module_utils._text import to_bytes

    class MockModule(object):
        def __init__(self):
            self.run_command = run_cmd
            self.params = {}
            self.tmpdir = tempfile.gettempdir()
            self.cache = cached.FactCache()


# Generated at 2022-06-13 02:22:11.978387
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # set up params to ensure coverage of all methods tested within collect
    module = object()
    collected_facts = object()

    # instantiate SystemCapabilitiesFactCollector with test params
    test_collector = SystemCapabilitiesFactCollector()

    # run method collect on SystemCapabilitiesFactCollector
    # assert results
    assert test_collector.collect(module=module,
                                  collected_facts=collected_facts) == {}

# Generated at 2022-06-13 02:22:21.007047
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.system.system_capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.system_capabilities import get_system_capabilities

    fake_module = FactCollector()

# Generated at 2022-06-13 02:22:22.809077
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    # NOTE: -> get_caps_data()/parse_caps_data() for easier mocking -akl

# Generated at 2022-06-13 02:22:32.966432
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Tests the method 'collect' of class 'SystemCapabilitiesFactCollector'
    """
    import os
    import tempfile
    import ansible.module_utils
    import ansible.module_utils.basic
    import ansible.module_utils.facts
    import ansible.module_utils.facts.system


# Generated at 2022-06-13 02:22:41.723075
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import GetDataParseDataTestHelper


# Generated at 2022-06-13 02:22:52.356869
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:22:53.062357
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:22:59.917966
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test method collect() of class SystemCapabilitiesFactCollector
    """
    # Test with capsh binary
    # Test with capsh binary
    module = MockAnsibleModule('debug')
    module.get_bin_path.return_value = "capsh_path"

# Generated at 2022-06-13 02:23:03.920219
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_module = FakeAnsibleModuleUtil(
        enforce_status='True',
        capsh_path='/usr/bin/capsh',
        rc=0
    )
    fake_fact_collector = SystemCapabilitiesFactCollector()
    assert fake_fact_collector.collect(test_module) != []

# Generated at 2022-06-13 02:23:12.416496
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    In this test, the output of capsh --print is mocked, and the
    result of collect() is tested to see if it returns an entry for
    'system_capabilities_enforced' and 'system_capabilities' using
    the mocked output.

    """
    from collections import namedtuple
    import os
    import sys

    # Create a mock 'module'
    class Options:
        def __init__(self):
            self.connection = 'local'
            # Set these options to avoid execution of a real ansible module
            self.remote_user = 'mockuser'
            self.become_user = 'mockuser'

        def get_bin_path(self, executable, required=False):
            return '/usr/bin/capsh'


# Generated at 2022-06-13 02:23:12.877446
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert True

# Generated at 2022-06-13 02:23:15.100066
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collect_facts

    result = collect_facts.collect_facts(dict(gather_subset=['system_capabilities']))
    assert result['ansible_system_capabilities_enforced'] == 'NA'
    assert len(result['ansible_system_capabilities']) == 0

# Generated at 2022-06-13 02:23:16.078122
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:23:26.727074
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert SystemCapabilitiesFactCollector.collect() == dict()

# Generated at 2022-06-13 02:23:34.966737
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

    module = 'module'

    Collector = SystemCapabilitiesFactCollector()
    Collector._module = module
    Collector._module.get_bin_path = lambda x: x
    Collector._module.run_command = lambda x, **kwargs: ("errorcode", x, "error")
    Collector.collect()

    # Check if system_capabilities_enforced is set to NA
    assert Collector.get_fact('system_capabilities_enforced') == 'NA'
    # Check if system_capabilities is empty list
    assert Collector.get_fact('system_capabilities') == []

# Generated at 2022-06-13 02:23:39.878333
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    module = ansible_collector._load_plugins('/usr/share/ansible/plugins/module_utils/facts/',
                                             'ansible.module_utils.facts',
                                             'SystemCapabilitiesFactCollector').pop()
    module.run_command = lambda args, **kwargs: (0, "Current: =ep\n", "")
    assert module.collect()['system_capabilities_enforced'] == 'False'
    assert module.collect()['system_capabilities'] == []

# Generated at 2022-06-13 02:23:40.481930
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:23:49.392469
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    ''' Unit test for method collect of class SystemCapabilitiesFactCollector '''
    import ansible.module_utils.facts.system.capabilities as capab
    import platform

    # NOTE: alot of 'mocking' needed here...

    if platform.system() == 'FreeBSD':
        # NOTE: use a FreeBSD 12.2 Jail for testing the testing!
        # NOTE: FreeBSD Jail
        pass
    else:
        # NOTE: Debian 9 Jail
        out = [
            'Version:	3.24.2',
            'Capability Bounding Set =cap_setgid,cap_setuid',
            'Securebits:	00/0x0/1\'b0',
            'secure-noroot:	no (unlocked)',
            '',
            'CapEff:	=ep',
            '',
        ]


# Generated at 2022-06-13 02:23:58.964442
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    # NOTE: ansible_module_fake -> ansible_module_use_shell -> setup_module_object
    # NOTE: create fake module instance for testing
    fake_module = FactCollector.ansible_module_use_shell(
        'capsh', [capsh_command], dict(), False, '/dev/null'
    )

    # NOTE: Create instance of SystemCapabilitiesFactCollector
    facts_system_capabilities = SystemCapabilitiesFactCollector()

    # NOTE: generate system_capabilities facts
    result = facts_system_capabilities.collect(fake_module)

    # NOTE: Assert equality of expected and result
    assert result == expected_result

# NOTE: Stub out module.run_command

# Generated at 2022-06-13 02:24:06.933709
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModule(
        argument_spec=dict(
            filter=dict(required=False, type='list'),
            gather_subset=dict(required=False, type='list'),
        )
    )
    # Mock 'capsh' command

# Generated at 2022-06-13 02:24:13.870178
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModuleMock()
    module.run_command = mock.Mock(autospec=True, spec_set=True)

# Generated at 2022-06-13 02:24:23.894296
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:24:32.706001
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Mocking necessary items for testing.
    class module_mock(object):
        @staticmethod
        def get_bin_path(cmd, opt_dirs=[]):
            return '/usr/bin/capsh'


# Generated at 2022-06-13 02:24:59.682989
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = False
    m_cls = SystemCapabilitiesFactCollector()
    assert m_cls.collect(module) == {}

# Generated at 2022-06-13 02:25:07.386753
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Unit test for method collect of class SystemCapabilitiesFactCollector
    """
    class TestModule(object):
        def get_bin_path(self, arg1):
            return "capsh"

        def run_command(self,arg1,arg2):
            return 0, "\nCurrent: =ep\n", "err"

    collector = SystemCapabilitiesFactCollector()
    ansible_module = TestModule()
    result = collector.collect(ansible_module)

    assert result is not None
    assert result['system_capabilities_enforced'] == 'False'
    assert result['system_capabilities'] == []

# Generated at 2022-06-13 02:25:11.722320
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible.module_utils.facts import FactCollector

    class MyMock(object):
        def __init__(self, rc=0, out='fake-out', err='fake-err'):
            self.rc = rc
            self.out = out
            self.err = err

        @staticmethod
        def get_bin_path(program, required=False, opt_dirs=[]):
            return '/bin/capsh'

        def run_command(self, cmd, errors='surrogate_then_replace'):
            return self.rc, self.out, self.err


# Generated at 2022-06-13 02:25:19.113563
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Arrange:
    module = mock.MagicMock()
    module.get_bin_path.return_value = ''
    module.run_command.return_value = ('', 'Current: =ep\nBounding set =ep', '')

    # Act:
    actual = SystemCapabilitiesFactCollector().collect(module)

    # Assert
    assert actual['system_capabilities_enforced'] == 'False'
    assert actual['system_capabilities'] == ['ep']



# Generated at 2022-06-13 02:25:27.842663
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: 'mock' module not available in Python 2.6, use simple class instead -akl
    class MockModule(object):
        def get_bin_path(*p):
            return '/bin/capsh'
        def run_command(*p):
            return 0, "Current: =ep\nCurrent: = cap_net_admin,cap_net_raw+eip", None

    m = MockModule()
    # NOTE: use any string for module_path, not None as for real module -akl
    s = SystemCapabilitiesFactCollector('/module/path')
    assert s.collect(m) == {
        'system_capabilities_enforced': 'False',
        'system_capabilities': [],
    }

# Generated at 2022-06-13 02:25:32.990950
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:25:43.948829
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Create class instance
    collector = SystemCapabilitiesFactCollector()

    # Define mocked methods to replace in module
    mocked_methods = {
        'get_bin_path': classmethod(lambda *args, **kwargs: '/bin/capsh'),
        'run_command': lambda *args, **kwargs: (0, 'Current: =ep', ''),
    }

    # Define class instance to replace in module
    class Mock(object):
        @staticmethod
        def __call__(*args, **kwargs):
            return

    mocked_class = Mock

    # Set up module
    module = type('', (object,), {})
    for name, method in mocked_methods.items():
        setattr(module, name, method)

    # Set up module return values

# Generated at 2022-06-13 02:25:51.834901
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = mock.Mock()

# Generated at 2022-06-13 02:26:01.905037
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os
    import re
    import uuid
    import tempfile
    import subprocess
    import functools

    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.distribution

    def _random_uuid():
        return uuid.uuid4().hex

    def _run_subprocess(*args, **kwargs):
        kwargs = dict(kwargs)
        if 'stdin' not in kwargs:
            kwargs['stdin'] = subprocess.PIPE
        if 'stderr' not in kwargs:
            kwargs['stderr'] = subprocess.PIPE
        if 'shell' not in kwargs:
            k

# Generated at 2022-06-13 02:26:02.585747
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:27:04.802480
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fake_module = AnsibleModuleMock({})
    capsh_path = '/usr/bin/capsh'
    capsh_out = '''Current: =ep
        Bounding set =ep
        Securebits: 00/0x0/1'b0
        secure-noroot: no (unlocked)
        secure-no-suid-fixup: no (unlocked)
        secure-keep-caps: no (unlocked)
        uid=0(root)
        gid=0(root)
        groups=0(root)
        Capabilities:
        '''
    fake_module.run_command = MagicMock(return_value=(0, capsh_out, ''))
    fake_module.get_bin_path = MagicMock(return_value=capsh_path)
    fake_collector = System

# Generated at 2022-06-13 02:27:14.054322
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Tests the collect method of class SystemCapabilitiesFactCollector"""

    # Only test for this fact if the module is present
    capsh_path = module_runner.get_bin_path('capsh')
    if capsh_path:
        # NOTE: Maybe init an instance of the class and call the collect method directly?
        #       ->  collector = SystemCapabilitiesFactCollector()
        #           facts_dict = collector.collect(module, {})
        #       -> Please think about it, this would make mocking much easier, too
        ansible_facts = module_runner.run_command('setup', '-m', 'local')['ansible_facts']
        # TEST: Capabilities are enforced
        assert ansible_facts['system_capabilities_enforced'] == 'True'

# Generated at 2022-06-13 02:27:23.488427
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Mock module class
    mock_module = MagicMock(name="AnsibleModule")
    mock_module.run_command = MagicMock(side_effect = [
            (None, 'Current: = cap_net_raw,cap_sys_admin', None),
            (1, None, None),
        ])

    mock_module.get_bin_path = MagicMock(side_effect = [ "capsh" ])

    # Create an instance of SystemCapabilitiesFactCollector
    # to be tested.
    cap_fact_collector = SystemCapabilitiesFactCollector()

    # Create a dummy ansible module instance
    # and fill in the required facts by calling the
    # collect method of SystemCapabilitiesFactCollector
    collected_facts = {}

# Generated at 2022-06-13 02:27:26.778895
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = {
        "get_bin_path": lambda foo: "capsh",
        "run_command": lambda *args, **kwargs: (0, "Current: =ep", "")
    }
    assert SystemCapabilitiesFactCollector().collect(module) == {
        'system_capabilities': [],
        'system_capabilities_enforced': 'False'
    }

# Generated at 2022-06-13 02:27:31.513038
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector()
    module = mock.Mock()

    # test for capsh not found
    module.get_bin_path.return_value = None
    facts = {'caps': {'system_capabilities': None, 'system_capabilities_enforced': None}}
    assert fact_collector.collect(module=module, collected_facts=facts) == {}

    # Test for capsh found; command failed
    module.get_bin_path.return_value = '/usr/bin/capsh'
    module.run_command.return_value = ('', '', 'error')
    assert fact_collector.collect(module=module, collected_facts=facts) == {}

    # Test for capsh found; no capabilities enforced

# Generated at 2022-06-13 02:27:41.319857
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json

    # Setup

# Generated at 2022-06-13 02:27:48.642051
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock(run_command=Mock(return_value=(0, 'Current: =ep', '')))
    mock_module.get_bin_path = Mock(return_value='/usr/bin/capsh')
    collect_capabilities = SystemCapabilitiesFactCollector.collect(mock_module)
    assert collect_capabilities['system_capabilities_enforced'] == 'False'
    assert collect_capabilities['system_capabilities'] == []
    mock_module.run_command.assert_called_with(['/usr/bin/capsh', "--print"], errors='surrogate_then_replace')

# Generated at 2022-06-13 02:27:54.520206
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import tempfile

    test_path = os.path.dirname(__file__)
    output_path = os.path.join(test_path, 'output.txt')

    with open(output_path) as f:
        output = f.read()

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(output)
        tmp.close()

        class TestModule:
            def __init__(self):
                self.params = {}

            def get_bin_path(self, executable):
                return tmp.name

            def run_command(self, args, errors='surrogate_then_replace'):
                return 0, output, ''

        collected_facts = {'system': {'distribution': 'Fedora'}}
        test_system_caps = System

# Generated at 2022-06-13 02:28:02.406179
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import platform, os
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import ansible_collector

    module = AnsibleModule(
        argument_spec = dict()
    )
    module.run_command = lambda x: (0, '', '')
    module.get_bin_path = lambda x: os.path.join(os.path.dirname(os.path.abspath(__file__)), 'capsh_fixture')

    system_capabilities_collector = SystemCapabilitiesFactCollector(module=module)
    ret = system_capabilities_collector.collect()


# Generated at 2022-06-13 02:28:10.966859
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import collections
    module = mock.Mock()
    capsh_path = '/usr/bin/capsh'
    module.get_bin_path.return_value = capsh_path