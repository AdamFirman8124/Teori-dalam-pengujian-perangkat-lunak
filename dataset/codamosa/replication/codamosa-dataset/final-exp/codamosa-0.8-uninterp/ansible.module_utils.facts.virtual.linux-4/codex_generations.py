

# Generated at 2022-06-13 04:05:15.818133
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    m = mock.MagicMock()
    l = LinuxVirtualCollector(m)
    assert l.platform == 'Linux'
    m.assert_has_calls([])

# Generated at 2022-06-13 04:05:17.978759
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    assert LinuxVirtualCollector._fact_class is LinuxVirtual
    assert LinuxVirtualCollector._platform == 'Linux'


# Generated at 2022-06-13 04:05:21.297893
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    v = LinuxVirtualCollector()

    # Check if it's the right class
    assert v.__class__.__name__ == 'LinuxVirtualCollector'
    # Check if platform is right
    assert v._platform == 'Linux'
    # Check if fact_class is right
    assert v._fact_class.__name__ == 'LinuxVirtual'

# Generated at 2022-06-13 04:05:29.371147
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    """
    Tests the constructor of LinuxVirtualCollector
    """
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.virtual.linux.linux_virtual import LinuxVirtual
    from ansible.module_utils.facts.collectors.virtual.linux.linux_virtual import LinuxVirtualCollector
    # Call the constructor of LinuxVirtualCollector
    lv_collector = LinuxVirtualCollector()
    # Check the collector type
    assert type(lv_collector) == Collector
    # Check the _fact_class of linux_virtual_collector
    assert isinstance(lv_collector._fact_class, LinuxVirtual)

# Generated at 2022-06-13 04:05:39.618144
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    async_ansible_module = ansible_module_get_init_mock(spec=['shell', 'run_command'])
    async_ansible_module.params = {}
    virtual_facts_mock = AsyncMock(return_value={'virtualization_type': 'virtualbox', 'virtualization_role': 'guest'})
    async_ansible_module.ansible_module.get_bin_path = AsyncMock(return_value='/usr/bin/dmidecode')
    async_ansible_module.ansible_module.get_file_lines = AsyncMock(return_value=[])
    async_ansible_module.ansible_module.run_command = AsyncMock(return_value=(0, '', ''))


# Generated at 2022-06-13 04:05:44.192373
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
  import json, os
  with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         "test_data/ansible_virtual_facts_output.json"),'r') as f:
    expected = json.load(f)

  class MockModule(object):
    params = {}

# Generated at 2022-06-13 04:05:49.038590
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    # mock_open does not work on a class method.
    with patch('ansible.module_utils.facts.virtual.LinuxVirtual.get_file_lines', return_value = ['systemd-1']):
        with patch('ansible.module_utils.facts.virtual.LinuxVirtual.get_file_content', side_effect = [None, None, None, None, None, 'docker', None, None, None, None, None, None, 'libvirtd']):
            with patch('os.path', new=MockPath(exists=True, isdir=True)):
                linux_virtual = LinuxVirtual()
                assert 'NA' == linux_virtual.get_virtual_facts()['virtualization_type']
                assert 'NA' == linux_virtual.get_virtual_facts()['virtualization_role']

# Generated at 2022-06-13 04:05:51.958587
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    collector = LinuxVirtualCollector(None)
    assert collector.platform == 'Linux'
    assert collector.fact_class == LinuxVirtual
    assert collector.config == None

if __name__ == "__main__":
    test_LinuxVirtualCollector()

# Generated at 2022-06-13 04:05:59.151508
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """Test method get_virtual_facts of class LinuxVirtual
    Get virtualization facts
    """
    # Setup
    linuxvirtual_obj = LinuxVirtual()
    # Execute
    result_virtual_facts = linuxvirtual_obj.get_virtual_facts()
    # Verify
    assert result_virtual_facts['virtualization_type'] == 'NA'
    assert result_virtual_facts['virtualization_role'] == 'NA'
    assert result_virtual_facts['virtualization_tech_guest'] == set(['NA'])
    assert result_virtual_facts['virtualization_tech_host'] == set(['NA'])
    # Cleanup - none necessary


# Generated at 2022-06-13 04:06:01.601361
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.linux import LinuxVirtual
    linux_virtual = LinuxVirtual()
    assert linux_virtual.get_virtual_facts()