

# Generated at 2022-06-13 04:05:11.605171
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    #
    # test get_virtual_facts of class LinuxVirtual
    #
    module = AnsibleModule(argument_spec=dict())

    test_module = LinuxVirtual(module)
    test_facts = test_module.get_virtual_facts()
    assert ('virtualization_type' in test_facts)
    assert ('virtualization_role' in test_facts)
    assert ('virtualization_tech_host' in test_facts)
    assert ('virtualization_tech_guest' in test_facts)
# Unit test executed when named "test_LinuxVirtual_SomeTestName"

# Generated at 2022-06-13 04:05:17.151265
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest

    class ConstructorTestCase(unittest.TestCase):
        def test_init_with_required_params(self):
            inst = LinuxVirtualCollector()
            self.assertIsInstance(inst, VirtualCollector)
            self.assertIsInstance(inst, LinuxVirtualCollector)

    unittest.main()



# Generated at 2022-06-13 04:05:18.403060
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    virtual = LinuxVirtualCollector()
    assert virtual is not None



# Generated at 2022-06-13 04:05:22.293484
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    facts = LinuxVirtual()
    virtual_facts = facts.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'NA'
    assert virtual_facts['virtualization_role'] == 'NA'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()


# ===========================================
# Subclass: DarwinVirtual
# ===========================================

# Generated at 2022-06-13 04:05:27.899399
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    ut_mock = Mock()
    ut_module = Mock()
    ut_module.get_bin_path.return_value = 'dmidecode'
    ut_mock.module = ut_module


# Generated at 2022-06-13 04:05:29.512338
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    lvc = LinuxVirtualCollector()
    assert lvc.fact_class == 'LinuxVirtual'

# Generated at 2022-06-13 04:05:37.249204
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    facts={}
    virtual = LinuxVirtual(None, None)
    virtual.module = object()
    ## Patch helper methods
    import __builtin__ as builtins
    builtins.open = mock_open()
    virtual.get_file_content = MagicMock(return_value="")
    virtual.get_file_lines = MagicMock(return_value=[])
    virtual.module.run_command = MagicMock(return_value=(0, "", ""))
    virtual.module.get_bin_path = MagicMock(return_value="/bin/dmidecode")
    virtual.get_virtual_facts(facts)

# Generated at 2022-06-13 04:05:42.962864
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    """Unit test for LinuxVirtualCollector"""

    virtual_disclaimer = {
        'msg': 'This module only works on Linux systems using the procfs filesystem (procfs is mounted).',
        'failed': True
    }
    module = AnsibleModule(argument_spec={})
    collector = LinuxVirtualCollector(module)
    if not 'procfs' in collector.get_mounts():
        assert collector.collect() == virtual_disclaimer
    else:
        if not 'Linux' in collector.get_platform().strip():
            assert collector.collect() == virtual_disclaimer
        else:
            assert collector.collect() is not None
            assert collector.collect().get('virtualization_type') == 'NA'


# Run ansible module unit tests when called as a script

# Generated at 2022-06-13 04:05:45.345698
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    linuxVC = LinuxVirtualCollector()
    assert linuxVC._fact_class == LinuxVirtual

# Generated at 2022-06-13 04:05:47.137157
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModuleMock()
    collector = LinuxVirtualCollector(module)
    assert collector._platform == 'Linux'
    assert isinstance(collector._fact_class, LinuxVirtual)