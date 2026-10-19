

# Generated at 2022-06-13 04:05:15.258023
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    collector = LinuxVirtualCollector()
    assert collector._platform == 'Linux'


# Generated at 2022-06-13 04:05:22.757360
# Unit test for constructor of class LinuxVirtualCollector

# Generated at 2022-06-13 04:05:28.379269
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    import pytest
    from ansible.module_utils.facts.virtual.linux import LinuxVirtual
    from ansible.module_utils.facts.virtual.linux import get_file_content
    from ansible.module_utils.facts.virtual.linux import get_file_lines

    class MockModule(object):
        def __init__(self, params={}):
            self.params = params

        def get_bin_path(self, binary, required=False):
            class MockFile(object):
                def __init__(self, lines):
                    self.lines = lines

                def readlines(self):
                    return self.lines

            if binary == 'lscpu':
                return 'lscpu'

            elif binary == 'dmidecode':
                return 'dmidecode'

            elif binary == 'hypervisor':
                lines

# Generated at 2022-06-13 04:05:32.285919
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    # Call constructor
    collect = LinuxVirtualCollector()

    # Assert correct fact_class
    assert collect.fact_class == LinuxVirtual
    # Assert correct fact_class
    assert collect.platform == 'Linux'
    # Call collect method. Should return a dictionary.
    result = collect.collect()
    assert isinstance(result, dict)

# Generated at 2022-06-13 04:05:34.594413
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # TODO: Implement
    pass

# Class for Linux hardware and system related facts

# Generated at 2022-06-13 04:05:44.309616
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """
    Testing method get_virtual_facts
    """

    module_mock = MagicMock()
    module_mock.run_command.return_value = (0, 'data', '')
    module_mock.get_bin_path.return_value = '/bin/dmidecode'
    linux_virtual_obj = LinuxVirtual(module_mock)
    mock_data_dir = "ansible/module_utils/facts/ansible_local/virtual/0/"
    with open(mock_data_dir + "virtual_facts_data.json") as json_data:
        virtual_facts_data = json.load(json_data)
    with open(mock_data_dir + "virtual_facts_expected.json") as json_data:
        virtual_facts_expected = json.load(json_data)

# Generated at 2022-06-13 04:05:49.658989
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():

    # Create a mock module
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text

    module = basic.AnsibleModule(
        argument_spec=dict()
    )
    module_return_value = dict(
        changed=False,
        ansible_facts={},
    )

    # Invoke the get_virtual_facts method of class LinuxVirtual
    linux_virtual_obj = LinuxVirtual(module)
    try:
        linux_virtual_obj.get_virtual_facts()
    except Exception as exc:
        module.fail_json(msg=to_text(exc))

    # Assertion that the module successfully finished
    assert not module.fail_json.called


# Generated at 2022-06-13 04:05:51.861756
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    c = LinuxVirtualCollector()
    assert c._platform == 'Linux'
    assert c._fact_class == LinuxVirtual


# Generated at 2022-06-13 04:06:00.879506
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():

    class Args(object):
        def __init__(self):
            pass
    class TestEndpoint(object):
        def __init__(self, args):
            self.args = args
        def get_option(self, *keys, **kwargs):
            return self.args.get('test_option', None)
        def module_run_command(self, *args, **kwargs):
            return 2, '', ''
    class TestModule(object):
        def __init__(self):
            self.args = Args()
            self.params = Args()
            self.endpoint = TestEndpoint(self.args)
        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('FAIL')


# Generated at 2022-06-13 04:06:06.087420
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    '''
    This function is unit test for method get_virtual_facts of LinuxVirtual,
    based on the following inputs:
    - **is_virtual** = True
    - **is_linux** = True
    - **virtualization_type** = 'kvm'
    - **virtualization_role** = 'guest'
    '''
    input_data = get_input_data()
    if input_data['is_virtual'] == True and input_data['is_linux'] == True:
        i_virtualization_type = input_data['virtualization_type']
        i_virtualization_role = input_data['virtualization_role']