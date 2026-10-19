

# Generated at 2022-06-13 04:05:31.475009
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """
    Compares output of method with expected output to check if it's working correctly
    """
    with open('tests/unit/ansible_module_system_platform/test_fixtures/LinuxVirtual_get_virtual_facts_1.json', 'r') as fixture_file:
        fixture = json.load(fixture_file)
    fixture_output = fixture['output']
    fixture_call_args = fixture['call_args']

    module_mock = MagicMock()
    module_mock.params = {
        'gather_subset': '!all,!min'
    }
    module_mock.run_command.return_value = fixture_call_args['run_command_output']

# Generated at 2022-06-13 04:05:33.350053
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModule(argument_spec={})
    facts = LinuxVirtualCollector(module).get_facts()
    assert isinstance(facts, dict) and facts



# Generated at 2022-06-13 04:05:42.133267
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    result = dict(
        changed = False,
        ansible_facts = dict()
    )
    # Fix the 'module' fixture
    module.params.clear()
    setattr(_ansible_module, 'params', module.params)
    setattr(_ansible_module, 'check_mode', module._name == 'check_mode')

    # Unit test here
    linux_virtual = LinuxVirtual(module)
    module.exit_json(**linux_virtual.get_virtual_facts())

if __name__ == '__main__':
    test_LinuxVirtual_get_virtual_facts()

# Generated at 2022-06-13 04:05:47.076092
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    import unittest
    import ansible.module_utils.facts.collector.virtual

    class TestModule(object):
        def __init__(self):
            self.params = dict()
            self.fail_json = lambda **x: "fail"

        def run_command(self, args, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False):
            self.args = args
            self.check_rc = check_rc
            self.close_fds = close_fds
            self.executable = executable
            self.data = data
            self.binary_data = binary_data
            return (0, 'test_executable_path /dev/kvm', '')

    class TestVirtual(object):
        def __init__(self):
            self.module

# Generated at 2022-06-13 04:05:53.428723
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # Testing with empty object, before set_virtual_facts()
    virtual_obj = LinuxVirtual()
    virtual_facts = virtual_obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'NA'
    assert virtual_facts['virtualization_role'] == 'NA'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

    # Testing with set_virtual_facts()
    set_virtual_facts_obj = LinuxVirtual()
    set_virtual_facts_obj.set_virtual_facts()
    virtual_facts = set_virtual_facts_obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] != 'NA'
    assert virtual_facts['virtualization_role'] != 'NA'


# Generated at 2022-06-13 04:06:01.756910
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # Note: All assert statements are used to define expected input and
    # output for the test cases.
    mock_module = MagicMock(name='AnsibleModule')
    mock_module.get_bin_path.return_value = None
    # Define test case input arguments
    lv = LinuxVirtual(module=mock_module)
    out = lv.get_virtual_facts()
    assert out[0]['virtualization_role'] == 'NA'
    assert out[0]['virtualization_type'] == 'NA'
    assert out[0]['virtualization_tech_guest'] == set()
    assert out[0]['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:06:04.467621
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    # Test the VirtualCollector constructor
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    # test_collector_init is dependent on module, so we have to provide
    # it with a module instance.
    test_collector_init(module, LinuxVirtualCollector, LinuxVirtual, 'Linux')


# Generated at 2022-06-13 04:06:15.139279
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    class MockModule(object):

        def __init__(self):
            self.params = {}
            self.exit_json = MagicMock()
            self.fail_json = MagicMock()

        def get_bin_path(self, arg):
            return '/bin/%s' % arg

        def fail_json(self, *args, **kwargs):
            self.exit_json(*args, **kwargs)

        def exit_json(self, *args, **kwargs):
            self.exit_json_args = args
            self.exit_json_kwargs = kwargs
            self.exit_json_called = True

        def run_command(self, *args, **kwargs):
            raise NotImplementedError()


# Generated at 2022-06-13 04:06:19.183316
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModuleMock()

    linuxvirtualcollector = LinuxVirtualCollector(module)

    assert linuxvirtualcollector._fact_class == LinuxVirtual
    assert linuxvirtualcollector._platform == 'Linux'



# Generated at 2022-06-13 04:06:20.125251
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    LinuxVirtualCollector()
