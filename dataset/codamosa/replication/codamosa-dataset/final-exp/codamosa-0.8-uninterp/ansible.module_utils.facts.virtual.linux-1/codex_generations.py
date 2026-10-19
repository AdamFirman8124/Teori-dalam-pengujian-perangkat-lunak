

# Generated at 2022-06-13 04:05:31.964292
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # setup
    module = AnsibleModule(argument_spec={})
    module.exit_json = MagicMock()
    obj = LinuxVirtual(module)
    _dict_uniq = obj._dict_uniq

    # sample return value
    sample_ret = {
        'virtualization_role': 'guest',
        'virtualization_type': 'kvm',
        'virtualization_tech_host': set(['kvm']),
        'virtualization_tech_guest': set(['kvm']),
    }

    # setup mock for get_virtual_facts
    _get_virtual_facts = MagicMock(return_value=sample_ret)
    obj.get_virtual_facts = _get_virtual_facts

    # test
    obj.virtualization()
    _get_virtual_facts.assert_called_once

# Generated at 2022-06-13 04:05:33.758890
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    vc = LinuxVirtualCollector()
    assert vc._platform == "Linux"
    assert isinstance(vc._fact_class(None), LinuxVirtual)

# Generated at 2022-06-13 04:05:43.724698
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec=dict())
    if not HAS_PSUTIL:
        module.fail_json(msg='psutil is required for this module')
    if not HAS_PYVIRT:
        module.fail_json(msg='pyvirt is required for this module')

    obj = LinuxVirtual(module)
    exit = obj.get_virtual_facts()

    # stub out the exit_json call during test, which is normally a noop
    # 4 is the number of kwargs that exit_json takes, so this saves us from
    # having to specify all 4 parameters
    def exit_json(*args, **kwargs):
        return {
            'changed': kwargs['changed'],
            'ansible_facts': kwargs['ansible_facts'],
        }


# Generated at 2022-06-13 04:05:47.746148
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModule(argument_spec={})
    result = dict(
        ansible_facts=dict(
            ansible_local=dict(virtual=dict())
        )
    )
    virtual_collector = LinuxVirtualCollector(module)

    # If a Virtual() object was created, then all objects were
    # initialized properly.
    assert dict == type(virtual_collector.facts)
    assert Virtual == type(virtual_collector.collector)


# Generated at 2022-06-13 04:05:49.399524
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    linux_virtual = LinuxVirtual()
    # FIXME: write tests for get_virtual_facts

# Generated at 2022-06-13 04:05:53.065194
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    with open("/tmp/test_LinuxVirtual_get_virtual_facts.json", "r") as f:
        return_val = json.load(f)

    module = MagicMock()
    module.run_command.return_value = 0, 'test', ''
    module.get_bin_path.return_value = '/usr/bin/lscpu'
    test_virtual = LinuxVirtual(module=module)

    assert test_virtual.get_virtual_facts() == return_val


# Generated at 2022-06-13 04:06:02.968296
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    class MockedModule:
        def run_command(self, cmd):
            return (0, '', '')
        def get_bin_path(self, cmd):
            return cmd
    class MockedLinuxDistribution:
        def __init__(self, **kwargs):
            self.id = 'Fedora'
    class MockedLinuxPlatform:
        def linux_distribution(self):
            return MockedLinuxDistribution()
    class MockedOpenFile:
        def __init__(self, content=None, err=None):
            self.content = content or 'VirtualBox'
            self.err = err or None

        def read(self):
            return self.content

        def readlines(self):
            return self.content.splitlines()

        def __enter__(self):
            return self


# Generated at 2022-06-13 04:06:10.221120
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    linux_virtual = LinuxVirtual(module)
    assert linux_virtual.get_virtual_facts() == {'virtualization_role': 'host', 'virtualization_type': 'kvm', 'virtualization_tech_host': {'kvm'}, 'virtualization_tech_guest': set()}


# Generated at 2022-06-13 04:06:13.749412
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    test_object = LinuxVirtual()
    if not test_object.module.check_mode:
        test_object.module.exit_json(changed=False, meta=test_object.get_virtual_facts())
    test_object.module.exit_json(changed=False)



# Generated at 2022-06-13 04:06:24.112071
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    content = '''
  Model: "Google Google Compute Engine"
  Model name:          QEMU Standard PC (i440FX + PIIX, 1996)
  Vendor:              Coreboot
  VRAM:                128 MiB
  UUID:                564D0000-0000-0000-0000-0000100000000
  System ROM:          OVMF
  BIOS:                OVMF

  Hypervisor vendor:   KVM
  Virtualization type: full

'''
    l = LinuxVirtual(dict(module=MockModule(params=dict())))
    l.is_linux = Mock(return_value=True)
    l.is_sunos = Mock(return_value=False)
    l.get_file_content = Mock(return_value='EC2\0\0\0\0')
    l.get_file_