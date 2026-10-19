

# Generated at 2022-06-13 04:05:19.407632
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    assert LinuxVirtualCollector.__doc__ != None
    assert LinuxVirtualCollector.__name__ != None
    lsc = LinuxVirtualCollector()
    assert lsc.is_valid()


# Generated at 2022-06-13 04:05:24.404704
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """
    Search for the following criteria:
        - system type: virtual or not
        - virtual host or guest
        - virtual system type
    """

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    lx = LinuxVirtual(module, platform.system())

    # We can't know in advance why virtualization can not be detected on a given system
    # Assert only that this method returns a dict without throwing an exception
    assert isinstance(lx.get_virtual_facts(), dict)

# Search for the following criteria
#   - system type: virtual or not
#   - virtual host or guest
#   - virtual system type

# Generated at 2022-06-13 04:05:27.053000
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    # Test to see if class can be instantiated
    linuxvirtual_collector_object = LinuxVirtualCollector()
    if linuxvirtual_collector_object:
        print("LinuxVirtualCollector class instantiated")


# Generated at 2022-06-13 04:05:30.306323
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    from ansible.module_utils.facts.collector.linux import LinuxVirtualCollector
    x = LinuxVirtualCollector()
    assert x.__class__.__name__ == 'LinuxVirtualCollector', "constructor of class LinuxVirtualCollector failed"


# Generated at 2022-06-13 04:05:37.061630
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    module.fail_json = fail_json
    linux_virtual = LinuxVirtual(module)
    set_module_args({
        '_ansible_no_log': False,
        '_ansible_verbosity': 3,
        '_ansible_debug': True
    })
    linux_virtual._get_virtual_facts()
    print(linux_virtual._get_virtual_facts())


# Generated at 2022-06-13 04:05:45.889264
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    return


if __name__ == '__main__':
    test_LinuxVirtual_get_virtual_facts()


# In older Linux Kernel versions, /sys filesystem is not available
# dmidecode is the safest option to parse virtualization related values
dmi_bin = module.get_bin_path('dmidecode')
# We still want to continue even if dmidecode is not available
if dmi_bin is not None:
    (rc, out, err) = module.run_command('%s -s system-product-name' % dmi_bin)
    if rc == 0:
        # Strip out commented lines (specific dmidecode output)
        vendor_name = ''.join([line.strip() for line in out.splitlines() if not line.startswith('#')])


# Generated at 2022-06-13 04:05:51.925594
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts.
    """

    import sys
    import os
    import yaml
    import __builtin__
    setattr(__builtin__, '_', lambda x: x)

    test_dir = os.path.dirname(os.path.realpath(__file__))
    lib_dir = os.path.join(test_dir, 'lib')
    sys.path.insert(0, lib_dir)

    class MockLinux(object):
        def __init__(self):
            self.module = type('object', (object, ), {})()
            self.module.run_command = self.run_command
            self.module.get_bin_path = lambda x: ''


# Generated at 2022-06-13 04:05:53.074465
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    collector = LinuxVirtualCollector()
    assert collector._fact_class == LinuxVirtual

# Generated at 2022-06-13 04:06:02.968521
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=False
    )
    lx_virt = LinuxVirtual(module=module)
    virtual_facts = lx_virt.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_status' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert virtual_facts['virtualization_role'] in ('guest', 'host', 'NA')

# Generated at 2022-06-13 04:06:04.494501
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModuleMock()
    lvc = LinuxVirtualCollector(module)
    assert lvc.platform == 'Linux'
    assert lvc._fact_class == LinuxVirtual