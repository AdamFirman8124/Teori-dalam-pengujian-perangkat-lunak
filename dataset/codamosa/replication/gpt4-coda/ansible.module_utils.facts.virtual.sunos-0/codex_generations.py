

# Generated at 2024-03-18 02:02:37.792486
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:02:39.572212
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:02:41.063574
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:02:48.070455
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used by SunOSVirtual
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global', ''),  # zonename
        (0, '', ''),  # modinfo
        (0, '', ''),  # virtinfo
        (0, 'VMware Virtual Platform', '')  # smbios
    ])

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected outcomes
    assert facts['virtualization_type'] == 'vmware'
    assert facts['virtualization_role'] == 'guest'
    assert facts['container'] == 'zone'

# Generated at 2024-03-18 02:02:50.023296
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:02:52.280135
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:02:53.534546
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:02:56.356231
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:03:03.787139
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used in get_virtual_facts
    mock_module = MagicMock()
    mock_module.get_bin_path.side_effect = lambda x: '/usr/bin/' + x if x in ['zonename', 'modinfo', 'virtinfo', 'smbios'] else None
    mock_module.run_command.side_effect = [
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'DOMAINROLE|impl=LDoms|control=true|io=true|service=true|root=true\n', ''),  # virtinfo output
        (0, 'System Information\nManufacturer: VMware, Inc.\n', '')  # smbios output
    ]

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call get_virtual_facts and store

# Generated at 2024-03-18 02:03:05.430601
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:03:39.449921
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mocking the module and its methods for the test
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, '', ''),  # virtinfo output
        (0, 'System Information\nManufacturer: VMware, Inc.\n', '')  # smbios output
    ])

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected outcomes
    assert facts['virtualization_type'] == 'vmware'

# Generated at 2024-03-18 02:03:47.148326
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    from ansible.module_utils.basic import AnsibleModule

    # Mock the AnsibleModule and its methods used by SunOSVirtual

# Generated at 2024-03-18 02:03:55.214093
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mocking the module and its methods for the test
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'virtinfo can only be run from the global zone\n', ''),  # virtinfo output
        (0, 'System Information\nManufacturer: VMware, Inc.\n', '')  # smbios output
    ])

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test
    virtual_facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the behavior of the method
    assert virtual_facts['container']

# Generated at 2024-03-18 02:03:57.258578
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:04:04.285949
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used in get_virtual_facts
    mock_module = MagicMock()
    mock_module.get_bin_path.side_effect = lambda x: '/usr/sbin/' + x
    mock_module.run_command.side_effect = [
        (0, 'global\n', ''),  # zonename
        (0, 'VMware virtual platform\n', ''),  # modinfo
        (0, '', ''),  # virtinfo
        (0, 'System Configuration: Oracle Corporation sun4v SPARC T4-1\n', '')  # smbios
    ]

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call get_virtual_facts and store the result
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected behavior
    assert facts['virtualization_type'] == 'vmware'

# Generated at 2024-03-18 02:04:06.528335
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:04:08.664531
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:04:09.955512
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:04:11.072033
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:04:20.700808
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used in SunOSVirtual.get_virtual_facts
    mock_module = MagicMock()
    mock_module.get_bin_path.side_effect = lambda x: '/usr/sbin/' + x
    mock_module.run_command.side_effect = [
        (0, 'global\n', ''),  # zonename
        (0, 'VMware virtual platform\n', ''),  # modinfo
        (0, '', ''),  # virtinfo
        (0, 'System Configuration: Oracle Corporation sun4v SPARC T4-1\n', '')  # smbios
    ]

    # Create an instance of the SunOSVirtual class with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the returned virtual facts
    assert facts['container'] == 'zone'

# Generated at 2024-03-18 02:04:47.942642
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:04:56.486632
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used in get_virtual_facts
    mock_module = mock.Mock()
    mock_module.get_bin_path.side_effect = lambda x: '/usr/bin/' + x if x in ['zonename', 'modinfo', 'virtinfo', 'smbios'] else None
    mock_module.run_command.side_effect = [
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'DOMAINROLE|impl=LDoms|control=true|io=true|service=true|root=true\n', ''),  # virtinfo output
        (0, 'System Information\nManufacturer: VMware, Inc.\n', '')  # smbios output
    ]

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call get_virtual_facts and

# Generated at 2024-03-18 02:04:58.106263
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:04:59.414988
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:05:05.946396
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used in get_virtual_facts
    mock_module = MagicMock()
    mock_module.get_bin_path.side_effect = lambda x: '/usr/sbin/' + x
    mock_module.run_command.side_effect = [
        (0, 'global', ''),  # zonename output
        (0, 'VMware Virtual Platform\n', ''),  # modinfo output
        (0, 'System Configuration: Oracle Corporation sun4v SPARC T4-1\n', ''),  # virtinfo output
        (0, 'VMware, Inc. VMware Virtual Platform\n', '')  # smbios output
    ]

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call get_virtual_facts and store the result
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected behavior

# Generated at 2024-03-18 02:05:07.278859
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:05:08.696673
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:05:09.965737
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:05:11.197201
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:05:13.296174
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:06:03.174928
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:06:04.445251
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:06:05.706303
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:06:07.867171
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:06:09.458178
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:06:10.575533
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:06:12.237112
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:06:13.740010
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:06:20.931588
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used in get_virtual_facts
    mock_module = MagicMock()
    mock_module.get_bin_path.side_effect = lambda x: '/usr/bin/' + x
    mock_module.run_command.side_effect = [
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'System Configuration: Oracle Corporation sun4v SPARC T5-2\n', ''),  # virtinfo output
        (0, 'BIOS Information\n\tVendor: VMware, Inc.\n', '')  # smbios output
    ]

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call get_virtual_facts and store the result
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected behavior

# Generated at 2024-03-18 02:06:33.432807
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mocking the module and its methods for the test
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'LDoms\n', ''),  # virtinfo output
        (0, 'VMware Virtual Platform\n', '')  # smbios output
    ])

    # Create an instance of the SunOSVirtual class with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test
    virtual_facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected outcomes
    assert virtual_facts['container'] == 'zone'

# Generated at 2024-03-18 02:08:18.767492
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used by SunOSVirtual
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x if x in ['zonename', 'modinfo', 'virtinfo', 'smbios'] else None)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware Virtual Platform\n', ''),  # modinfo output
        (0, 'DOMAINROLE|impl=LDoms|control=true|io=true|service=false|root=false\n', ''),  # virtinfo output
        (0, 'System Information\nManufacturer: VMware, Inc.\n', '')  # smbios output
    ])

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test


# Generated at 2024-03-18 02:08:20.005696
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:08:22.377187
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:08:31.467596
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mocking the module and its methods for the test
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'DOMAINROLE|impl=LDoms|control=true|io=true|service=true|root=false\n', ''),  # virtinfo output
        (0, 'System Information\nManufacturer: VMware, Inc.\n', '')  # smbios output
    ])

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test
    virtual_facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected output
   

# Generated at 2024-03-18 02:08:39.191558
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mocking the module and its methods for the test
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'LDoms\n', ''),  # virtinfo output
        (0, 'VMware\n', '')  # smbios output
    ])

    sunos_virtual = SunOSVirtual(mock_module)
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected behavior
    assert facts['container'] == 'zone'
    assert facts['virtualization_type'] == 'vmware'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2024-03-18 02:08:45.202179
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mock the module and its methods used in SunOSVirtual.get_virtual_facts
    mock_module = MagicMock()
    mock_module.get_bin_path.side_effect = lambda x: '/usr/bin/' + x
    mock_module.run_command.side_effect = [
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'LDoms\n', ''),  # virtinfo output
        (0, 'VMware Virtual Platform\n', '')  # smbios output
    ]

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected behavior
    assert facts['virtualization_type'] == 'vmware'

# Generated at 2024-03-18 02:08:46.705238
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:08:54.890275
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mocking the module and its methods for the test
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global', ''),  # zonename output
        (0, 'VMware virtual platform', ''),  # modinfo output
        (0, 'LDoms', ''),  # virtinfo output
        (0, 'VMware', '')  # smbios output
    ])

    sunos_virtual = SunOSVirtual(mock_module)
    facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected behavior
    assert facts['virtualization_type'] == 'vmware'
    assert facts['virtualization_role'] == 'guest'
    assert facts['container'] == 'zone'
    assert 'vmware' in facts['virtualization_tech_guest']

# Generated at 2024-03-18 02:08:56.506144
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:08:57.902701
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:12:14.177267
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():    module = Mock()

# Generated at 2024-03-18 02:12:16.563152
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():    collector = SunOSVirtualCollector()

# Generated at 2024-03-18 02:12:25.537621
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():    # Mocking the module and its methods for the test
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x)
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global\n', ''),  # zonename output
        (0, 'VMware virtual platform\n', ''),  # modinfo output
        (0, 'virtinfo can only be run from the global zone\n', ''),  # virtinfo output
        (0, 'System Information\nManufacturer: VMware, Inc.\n', '')  # smbios output
    ])

    # Create an instance of SunOSVirtual with the mocked module
    sunos_virtual = SunOSVirtual(mock_module)

    # Call the method to test
    virtual_facts = sunos_virtual.get_virtual_facts()

    # Assertions to validate the expected output