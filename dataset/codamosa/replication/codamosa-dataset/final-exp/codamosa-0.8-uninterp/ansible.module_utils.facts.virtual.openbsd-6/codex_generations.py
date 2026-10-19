

# Generated at 2022-06-13 04:09:56.062251
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # OpenBSD is a host
    facts = OpenBSDVirtual({}).get_virtual_facts()
    assert facts['virtualization_type'] == 'vmm'
    assert facts['virtualization_role'] == 'host'
    assert 'vmm' in facts['virtualization_tech_host']

# Generated at 2022-06-13 04:10:01.213195
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    osd_virtual = OpenBSDVirtual()
    virtual_facts = osd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

    virtual_facts = OpenBSDVirtual.get_virtual_facts(osd_virtual)
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:10:02.570477
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 04:10:04.531322
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector()
    assert openbsd_virtual.platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:08.125573
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()

    assert virtual_facts['virtualization_type'] in ('vmm', '')
    assert virtual_facts['virtualization_role'] in ('host', 'guest', '')
    assert virtual_facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:10:11.345614
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual()
    # pylint: disable=protected-access
    virtual_facts = openbsd_virtual_facts._get_virtual_facts()
    assert 'OpenBSD' == virtual_facts['virtualization_type']
    assert 'guest' == virtual_facts['virtualization_role']
    assert 'OpenBSD' in virtual_facts['virtualization_tech_guest']
    assert not virtual_facts['virtualization_tech_host']

# Generated at 2022-06-13 04:10:23.369047
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from os.path import dirname, join, abspath
    import json
    import sys

    mock_data_path = join(dirname(abspath(__file__)), 'virtual', 'sysctl.mock')
    sys.modules['ansible.module_utils.facts.virtual.sysctl'] = \
        __import__('ansible.module_utils.facts.virtual.sysctl', globals(), locals(), ['*'])
    sys.modules['ansible.module_utils.facts.virtual.sysctl'].get_file_content = \
        lambda filename: json.load(open(mock_data_path))

    facts_obj = OpenBSDVirtual()
    virtual_facts = facts_obj.get_virtual_facts()
    # assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts

# Generated at 2022-06-13 04:10:32.398059
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    test_cases = [
        ['virtio', [], ['virtio'], 'QEMU', 'guest', {
            'virtualization_type': 'QEMU',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': ['virtio'],
            'virtualization_tech_host': [],
        }],
    ]

    for (dmesg_boot, expected_guest_tech, expected_host_tech,
         expected_type, expected_role, expected_facts) in test_cases:
        test_obj = OpenBSDVirtual({})
        test_obj._dmesg_boot = dmesg_boot
        assert test_obj.get_virtual_facts() == expected_facts

# Generated at 2022-06-13 04:10:39.487291
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/bin/sysctl'
    module_mock.run_command.return_value = (0, "hw.product=OpenBSD\nhw.vendor=OpenBSD", '')

    o = OpenBSDVirtual(module=module_mock)
    expected = {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_host': {'vmm'},
        'virtualization_tech_guest': set()
    }
    assert o.get_virtual_facts() == expected

# Generated at 2022-06-13 04:10:45.119824
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    collector = OpenBSDVirtualCollector({}, {})
    virtual = OpenBSDVirtual({}, {})

    # Virtualization test 1
    virtual.set_property_readers(['hw.vendor'])

# Generated at 2022-06-13 04:10:52.757673
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    facts = virt.get_virtual_facts()
    assert facts['virtualization_tech_guest'] == {'vmm'}

# collect_virtualization_facts() is called implicitly by Ansible
# but we should call it explicitly during unit tests
collect_virtualization_facts()

# Generated at 2022-06-13 04:11:03.006826
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Setup a class for testing
    class DummyOpenBSDVirtual(OpenBSDVirtual):
        # We don't want to call sysctl
        def detect_virt_vendor(self, sysctl_virtual):
            return {}
        def detect_virt_product(self, sysctl_virtual):
            return {'virtualization_type': '',
                    'virtualization_role': '',
                    'virtualization_technologies': [],
                    'virtualization_tech_guest': set(),
                    'virtualization_tech_host': set()}

    openbsd_virtual = DummyOpenBSDVirtual()

    # Test the instance is correctly set up
    assert openbsd_virtual.platform == 'OpenBSD'
    assert openbsd_virtual.DMESG_BOOT == '/var/run/dmesg.boot'

    # Produce a

# Generated at 2022-06-13 04:11:09.221478
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.vmware import VMware
    from ansible.module_utils.facts.virtual.xen import Xen
    from ansible.module_utils.facts.virtual.kvm import KVM
    from ansible.module_utils.facts.virtual.hyperv import Hyperv
    from ansible.module_utils.facts.virtual.vbox import VirtualBox
    from ansible.module_utils.facts.virtual.vserver import VServer
    from ansible.module_utils.facts.virtual.jails import Jails
    from ansible.module_utils.facts.virtual.zones import Zones
    from ansible.module_utils.facts.virtual.docker import Docker
    from ansible.module_utils.facts.virtual.chroot import Chroot

    # VM Hosts

# Generated at 2022-06-13 04:11:14.580396
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    data = {
        "sysctl": {
            "hw.product": "OpenBSD",
            "hw.vendor": "OpenBSD"
        }
    }
    result = OpenBSDVirtual.get_virtual_facts(data)
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''
    assert not result['virtualization_tech_guest']
    assert not result['virtualization_tech_host']

# Generated at 2022-06-13 04:11:21.409446
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Instantiate the class
    virtual = OpenBSDVirtual()
    # Build the expected dictionary
    expected_virtual_facts = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': {'vmm'},
        }
    # Assert if method returns expected result
    assert virtual.get_virtual_facts() == expected_virtual_facts

# Generated at 2022-06-13 04:11:31.034417
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    '''
    Test the OpenBSDVirtual.get_virtual_facts() method
    '''

# Generated at 2022-06-13 04:11:36.259685
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()

    # Initialize the virtual facts
    virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

    # OpenBSD dmesg output

# Generated at 2022-06-13 04:11:40.660490
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()

    expected_virtual_facts = {'virtualization_type': '',
                              'virtualization_role': '',
                              'virtualization_tech_guest': set(),
                              'virtualization_tech_host': set()}

    assert virtual_facts == expected_virtual_facts

# Generated at 2022-06-13 04:11:48.252130
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsdvirtual = OpenBSDVirtual()
    virtual_facts = {'virtualization_type': '',
                     'virtualization_role': '',
                     'virtualization_product_name': '',
                     'virtualization_product_version': '',
                     'virtualization_product_serial': '',
                     'virtualization_product_uuid': ''}
    openbsd_virtual_facts = openbsdvirtual.get_virtual_facts()
    assert virtual_facts == openbsd_virtual_facts

# Generated at 2022-06-13 04:11:54.123804
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:12:02.467545
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual(module=None)

    # Virtualization product facts unit test cases
    openbsd_virtual_facts.get_file_content = lambda x: 'OpenBSD'
    assert openbsd_virtual_facts.detect_virt_product('hw.product') == {'virtualization_type': '',
                                                                      'virtualization_role': '',
                                                                      'virtualization_tech_host': set(),
                                                                      'virtualization_tech_guest': set()}

    # Virtualization vendor facts unit test cases
    openbsd_virtual_facts.get_file_content = lambda x: 'OpenBSD'

# Generated at 2022-06-13 04:12:03.897718
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    o = OpenBSDVirtualCollector()
    assert o._platform == 'OpenBSD'

# Generated at 2022-06-13 04:12:04.958318
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:12:12.126867
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    openbsd_virtual_facts = virt.get_virtual_facts()
    openbsd_virtual_facts_expected = {
        'virtualization_role': 'host',
        'virtualization_type': 'vmm',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['vmm'])
    }
    assert openbsd_virtual_facts == openbsd_virtual_facts_expected

# Generated at 2022-06-13 04:12:19.154331
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Test VirtIO detection
    test_virtio = OpenBSDVirtual()
    assert test_virtio.get_virtual_facts()['virtualization_tech_guest'] == set(['virtio'])

    # Test HyperV detection
    test_hyperv = OpenBSDVirtual(hw_product="Virtual Machine")
    assert test_virtio.get_virtual_facts()['virtualization_tech_guest'] == set(['virtio'])

    # Test VMM detection
    test_vmm = OpenBSDVirtual()
    test_vmm.DMESG_BOOT = "/test_dmesg.boot"
    with open(test_vmm.DMESG_BOOT, "w") as dmesg:
        dmesg.write("vmm0 at mainbus0: VMX/EPT\n")
    assert test_

# Generated at 2022-06-13 04:12:24.004627
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Set up a test instance of class OpenBSDVirtual
    openbsd_virtual = OpenBSDVirtual()
    facts = {
            'kernel': 'OpenBSD',
            'os_family': 'OpenBSD',
            'virtualization_role': 'guest',
            'virtualization_type': 'xen'
            }

    # Set private attribute with mock method results
    openbsd_virtual.sysctl_all = mock_sysctl_all(
            {'hw.vendor': 'Xen', 'hw.product': 'HVM domU'})

    # Call private method
    facts = openbsd_virtual.get_virtual_facts()

    # Assert the results are as expected
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_type'] == 'xen'

# Generated at 2022-06-13 04:12:33.714041
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    test1 = OpenBSDVirtual()
    test2 = OpenBSDVirtual()
    test3 = OpenBSDVirtual()

    # Test1: Physical machine
    test1.get_dmesg_boot = lambda: '''
OpenBSD 6.2-stable (GENERIC.MP) #0: Sun Feb 11 03:28:03 UTC 2018
    root@build1.openbsd.org:/usr/src/sys/arch/amd64/compile/GENERIC.MP
real mem = 2626990080 (2501MB)
avail mem = 2483173376 (2371MB)
mainbus0 at root: OpenBSD
bios0 at mainbus0: SMBIOS rev. 2.7 @ 0xeef80 (41 entries)
'''

# Generated at 2022-06-13 04:12:42.134086
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class OpenBSDVirtual'''

    # Test for virtual_facts with empty values
    virtual_facts = {}
    virtual_facts['virtualization_type'] = 'vmm'
    virtual_facts['virtualization_role'] = 'guest'
    virtual_facts['virtualization_tech_guest'] = set(['vmm'])
    virtual_facts['virtualization_tech_host'] = set(['vmm'])
    assert OpenBSDVirtual().get_virtual_facts() == virtual_facts

# Generated at 2022-06-13 04:12:43.384661
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()

# Generated at 2022-06-13 04:12:47.058326
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_vf = OpenBSDVirtual(module=None)
    result = openbsd_vf.get_virtual_facts()

    assert result.get('virtualization_type') in ['', 'vmm']
    assert result.get('virtualization_role') in ['', 'host']

# Generated at 2022-06-13 04:12:58.704428
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    # Create an instance of OpenBSDVirtual
    fact = OpenBSDVirtual({})
    assert True

    # Call method get_virtual_facts
    virtual_facts = fact.get_virtual_facts()

    # Check the result
    assert virtual_facts['virtualization_type'] in ['', 'vmm']
    assert virtual_facts['virtualization_role'] in ['', 'host', 'guest']

    assert virtual_facts['virtualization_type'] == virtual_facts['virtualization_type_full']
    assert virtual_facts['virtualization_type'] == virtual_facts['virtualization_type_full']

# Generated at 2022-06-13 04:13:09.013306
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:13:15.049204
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:13:19.205561
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # Ensure that class handles constructor parameter properly
    res = OpenBSDVirtualCollector(chroot='initdir')
    assert res._chroot == 'initdir'

# Generated at 2022-06-13 04:13:20.124697
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector()
    assert type(openbsd_virtual) == OpenBSDVirtualCollector


# Generated at 2022-06-13 04:13:23.069483
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = OpenBSDVirtual()
    virtual_facts = v.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == {'vmm'}
    assert virtual_facts['virtualization_product_name'] == ''
    assert virtual_facts['virtualization_product_version'] == ''

# Generated at 2022-06-13 04:13:24.517233
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 04:13:31.479638
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Test data
    sysctl_virtual_hw_product = '''
hw.product=OpenBSD Virtual Machine
'''
    sysctl_virtual_hw_vendor = '''
hw.vendor=OpenBSD
'''

# Generated at 2022-06-13 04:13:33.000856
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:13:34.533872
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:13:51.187571
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = OpenBSDVirtual()
    virtual_facts = v.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'OpenBSD'
    # OpenBSD is always a host
    assert virtual_facts['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:13:57.445721
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Run only on OpenBSD
    if OpenBSDVirtual.platform != 'OpenBSD':
        return

    openbsd_virtual = OpenBSDVirtual()
    facts = openbsd_virtual.get_virtual_facts()

    # Ensure we detect the virtualization technologies
    if facts['virtualization_type'] == '':
        print('ERROR: Failed to detect virtualization technology')
        exit(1)

    if facts['virtualization_role'] == '':
        print('ERROR: Failed to detect virtualization role')
        exit(1)

# Generated at 2022-06-13 04:13:59.264006
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    obj = OpenBSDVirtualCollector()
    assert obj.platform == 'OpenBSD'
    assert obj._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:14:04.925149
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Create an instance of OpenBSDVirtual
    openbsd_virtual = OpenBSDVirtual()

    # Get the virtual facts
    virtual_facts = openbsd_virtual.get_virtual_facts()

    # It should be empty
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_product_name'] == ''

# Generated at 2022-06-13 04:14:10.960520
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    import pytest
    from ansible.module_utils.facts.virtual import OpenBSDVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector
    import os

    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = ':'.join(['.',
        '..' + os.sep + '..' + os.sep + 'collection_plugins'])


# Generated at 2022-06-13 04:14:11.956242
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual = OpenBSDVirtualCollector()
    assert virtual._platform == 'OpenBSD'
    assert isinstance(virtual._fact_class, OpenBSDVirtual)

# Generated at 2022-06-13 04:14:15.120626
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    module = OpenBSDVirtualCollector()
    assert isinstance(module.fact_class, OpenBSDVirtual)
    assert module.fact_class.platform == 'OpenBSD'


# Generated at 2022-06-13 04:14:24.743663
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()

    # Generate test data

    # Test with no known virtualization product
    testdata = {
        'hw.product': '',
        'hw.vendor': '',
        'dmesg.boot': '',
    }
    virtual._get_sysctl = lambda key: testdata[key]
    virtual._get_file_content = lambda f: ''
    virtual_facts = virtual.get_virtual_facts()

    expected_virtual_facts = {}
    expected_virtual_facts['virtualization_type'] = ''
    expected_virtual_facts['virtualization_role'] = ''
    expected_virtual_facts['virtualization_tech_guest'] = set()
    expected_virtual_facts['virtualization_tech_host'] = set()


# Generated at 2022-06-13 04:14:26.645489
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector()
    assert openbsd_virtual.platform == 'OpenBSD'
    assert openbsd_virtual._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:14:28.490504
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    c = OpenBSDVirtualCollector()
    assert c.collect()['virtualization_type'] == ''
    assert c.collect()['virtualization_role'] == ''

# Generated at 2022-06-13 04:14:56.945380
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.openbsd.collector import OpenBSDVirtualCollector
    from ansible.module_utils.facts.virtual.openbsd.virtual import OpenBSDVirtual
    assert OpenBSDVirtualCollector().__class__
    assert OpenBSDVirtualCollector()._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector()._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:15:04.326355
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    import sys
    import pytest
    from tests.utils import set_module_args

    module_args = dict(
        gather_subset='!all',
        gather_timeout=10,
    )
    set_module_args(module_args)

    # Setup the test_instance
    test_instance = OpenBSDVirtual()
    test_instance.get_virtual_facts()

    # Reset the module_arg spec
    sys.modules['ansible.module_utils.facts.virtual.openbsd'].argument_spec = dict()

# Generated at 2022-06-13 04:15:16.308560
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Test 1: on OpenBSD physical server
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.get_file_content = lambda path: ''
    openbsd_virtual.get_sysctl = lambda key: ''
    assert openbsd_virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

    # Test 2: on OpenBSD virtual server with vmm(4)

# Generated at 2022-06-13 04:15:18.212304
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_facts = OpenBSDVirtualCollector()
    assert virtual_facts._fact_class == OpenBSDVirtual
    assert virtual_facts._platform == 'OpenBSD'

# Generated at 2022-06-13 04:15:29.461905
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    results = dict()

    openbsd_virtual = OpenBSDVirtual()

# Generated at 2022-06-13 04:15:39.077498
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    # Run method get_virtual_facts of class Virtual
    OpenBSDVirtual_get_virtual_facts_obj = OpenBSDVirtual()
    OpenBSDVirtual_get_virtual_facts_return = OpenBSDVirtual_get_virtual_facts_obj.get_virtual_facts()
    OpenBSDVirtual_get_virtual_facts_return_expected = {'virtualization_role': '',
                          'virtualization_type': '',
                          'virtualization_tech_host': set(),
                          'virtualization_tech_guest': set()}

    # Compare the two dictionaries.
    for key in OpenBSDVirtual_get_virtual_facts_return_expected:
        assert key in OpenBSDVirtual_get_virtual_facts_return
    for key in OpenBSDVirtual_get_virtual_facts_return:
        assert key in OpenBSDVirtual_get_virtual

# Generated at 2022-06-13 04:15:40.322125
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    c = OpenBSDVirtualCollector()
    assert c.platform == 'OpenBSD'
    assert c._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:15:42.100672
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    """
    Test the constructor of the class OpenBSDVirtualCollector
    """
    obv = OpenBSDVirtualCollector()
    assert obv.platform == 'OpenBSD'

# Generated at 2022-06-13 04:15:46.779435
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():

    obj = OpenBSDVirtualCollector()
    assert obj.platform == 'OpenBSD'
    assert obj._fact_class == OpenBSDVirtual
    assert obj._platform == 'OpenBSD'


# Generated at 2022-06-13 04:15:50.562235
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_vc = OpenBSDVirtualCollector()
    assert openbsd_vc.platform == 'OpenBSD'
    assert openbsd_vc.fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:16:57.485131
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 04:17:08.004186
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    with open('test/unit/module_utils/facts/virtual/test_VirtualOpenBSD_dmesg.boot') as dmesg_boot:
        dmesg_boot_content = dmesg_boot.read()

    openbsd_virtual = OpenBSDVirtual(module=None)
    openbsd_virtual.DMESG_BOOT = 'test/unit/module_utils/facts/virtual/test_VirtualOpenBSD_dmesg.boot'
    virtual_facts = openbsd_virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_host'] == set(['vmm'])
    assert virtual_facts['virtualization_tech_guest'] == set

# Generated at 2022-06-13 04:17:10.885218
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    host_facts = {}
    openbsd_virtual_class = OpenBSDVirtual(host_facts)
    openbsd_virtual_class.get_virtual_facts()

# Generated at 2022-06-13 04:17:21.024115
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Init other values as they're initialized during __init__
    virtual_facts = OpenBSDVirtual()
    virtual_facts.sysctl_cmd = 'sysctl'

    # Case 1: When there is no valid output for hw.product, hw.vendor
    virtual_facts.get_virtual_product = lambda paths: ''
    virtual_facts.get_virtual_vendor = lambda paths: ''
    expected_virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    assert virtual_facts.get_virtual_facts() == expected_virtual_facts

    # Case 2: When hw.product returns output and virtualization_type
    # is still not found.
    virtual

# Generated at 2022-06-13 04:17:21.657796
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    o = OpenBSDVirtual()
    o.get_virtual_facts()

# Generated at 2022-06-13 04:17:31.028919
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:17:36.055334
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()

    # Add a fake_file_content
    OpenBSDVirtual.DMESG_BOOT = 'tests/unittests/unit/module_utils/facts/virtual/files/dmesg_boot_vmm_only'
    virtual_facts = virtual.get_virtual_facts()

    # Check if the values are set as expected.
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set(['vmm'])

    # Clean up the fake file
    OpenBSDVirtual.DMESG_BOOT = '/var/run/dmesg.boot'

# Generated at 2022-06-13 04:17:38.834901
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector.platform == 'OpenBSD'
    assert collector._fact_class._platform == 'OpenBSD'


# Generated at 2022-06-13 04:17:45.347668
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    expected_virtual_facts = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_host': {'vmm'},
        'virtualization_tech_guest': {'vmm'},
        'product_name': 'Virtual Machine',
        'product_version': '',
    }
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.data = {'dmesg_boot':
                            'vmm0 at mainbus0: SVM/RVI',
                            'hw_product': 'Virtual Machine',
                            'hw_vendor': 'VMWare'}
    openbsd_virtual.get_virtual_facts()
    assert openbsd_virtual.facts == expected_virtual_facts


# Generated at 2022-06-13 04:17:46.908579
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector._fact_class == OpenBSDVirtual
    assert collector._platform == 'OpenBSD'