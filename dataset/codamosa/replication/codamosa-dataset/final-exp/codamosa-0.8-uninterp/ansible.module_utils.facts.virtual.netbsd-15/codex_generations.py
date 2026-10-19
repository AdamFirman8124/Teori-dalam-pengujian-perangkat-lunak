

# Generated at 2022-06-13 04:09:54.433650
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    """
    This test runs when file is called directly.
    """
    test_obj = NetBSDVirtualCollector()
    assert test_obj._platform == 'NetBSD'
    assert test_obj._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:09:56.397500
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    obj = NetBSDVirtualCollector()
    assert obj._platform == 'NetBSD'
    assert obj._fact_class is NetBSDVirtual


# Generated at 2022-06-13 04:10:08.258618
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual({}, None)
    netbsd_virtual.sysctl = {'machdep.dmi.system-product': 'VirtualBox',
                             'machdep.dmi.system-vendor': 'innotek GmbH',
                             'machdep.hypervisor': 'None'}
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == {'virtualbox'}
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_product_name'] == 'VirtualBox'


# Generated at 2022-06-13 04:10:13.050188
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create a new instance of class NetBSDVirtual
    netbsd_virtual_obj = NetBSDVirtual()
    # Get the results of method get_virtual_facts of class NetBSDVirtual
    netbsd_virtual_results = netbsd_virtual_obj.get_virtual_facts()
    # Create the expected results
    expected_results = dict(
        virtualization_type='xen',
        virtualization_role='guest',
        virtualization_tech_guest={'xen'},
        virtualization_tech_host=set(),
    )
    # Assert that the results of method get_virtual_facts of class NetBSDVirtual
    # match the expected results
    assert netbsd_virtual_results == expected_results, (
        'netbsd_virtual_results != expected_results')

# Generated at 2022-06-13 04:10:14.851090
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual({})
    assert netbsdvirtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:15.419019
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    NetBSDVirtual()

# Generated at 2022-06-13 04:10:27.919372
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_product_facts = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
    }

    virtual_vendor_facts = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'kvm'},
        'virtualization_tech_host': set(),
    }

    virtual_facts = {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen', 'kvm'},
        'virtualization_tech_host': set(),
    }

   

# Generated at 2022-06-13 04:10:38.108047
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual().get_virtual_facts()
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_type'] == ''

    # The following tests the VirtualSysctlDetectionMixin class,
    # which has been implemented in the NetBSDVirtual class.

    # No value behind key
    assert NetBSDVirtual().detect_virt_vendor('') == {}

    # Unknown key
    assert NetBSDVirtual().detect_virt_vendor('xen.domain-type') == {}

    # Key 'machdep.hypervisor'
    data = {
        'machdep.hypervisor': 'None',
        'machdep.hv_vendor': 'None',
        'machdep.hv_version': 'None',
    }
    assert NetBSDVirtual().detect_virt_v

# Generated at 2022-06-13 04:10:49.750180
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """
    Take a sample get_virtual_facts from a NetBSD Virtual machine and compare it against
    a generated dictionary to make sure the parsing logic for the NetBSDVirtual class is
    correct.
    """
    expected_virtual_facts = {'virtualization_type': 'VMWare', 'virtualization_role': 'guest'}
    result = {
        'ansible_facts': {
            'ansible_virtualization_type': 'VMWare',
            'ansible_virtualization_role': 'guest'
        },
        'changed': False
    }

    # Create a NetBSDVirtual object
    nb_virtual = NetBSDVirtual()

    # Create some sample data to pass to the NetBSDVirtual object

# Generated at 2022-06-13 04:10:51.792512
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts_module = NetBSDVirtual()
    assert virtual_facts_module.platform == 'NetBSD'


# Generated at 2022-06-13 04:11:02.634560
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    get_virtual_facts = NetBSDVirtual().get_virtual_facts()
    assert get_virtual_facts['virtualization_tech_guest'] is not None
    assert get_virtual_facts['virtualization_tech_host'] is not None
    assert get_virtual_facts['virtualization_type'] is not None
    assert get_virtual_facts['virtualization_role'] is not None
    assert get_virtual_facts['virtualization_product_name'] is not None
    assert get_virtual_facts['virtualization_product_version'] is not None

# Generated at 2022-06-13 04:11:11.752815
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'
    assert netbsd.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_userspace_type': '',
        'virtualization_technologies': set(),
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
        'virtualization_product_name': '',
        'virtualization_product_version': '',
    }

# Generated at 2022-06-13 04:11:14.042987
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts._platform == 'NetBSD'
    assert virtual_facts._fact_class == NetBSDVirtual



# Generated at 2022-06-13 04:11:20.276511
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    # Check that platform is NetBSD
    assert virtual_facts.platform == 'NetBSD'
    # Check that required virtual fact keys are present
    virtual_facts.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts.data
    assert 'virtualization_role' in virtual_facts.data

# Generated at 2022-06-13 04:11:30.360725
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    fake_virtual_facts = {
        'virtualization_type': None,
        'virtualization_role': None,
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

    fake_sysctl_info = {
        'machdep.dmi.system-product': 'OpenStack Nova',
        'machdep.dmi.system-vendor': 'QEMU',
        'machdep.hypervisor': 'Xen',
    }

    # Set up the hypervisor detection class
    fake_hypervisor_detection_class = NetBSDVirtual()

    # Set up a fake path to the sysctl command
    fake_sysctl_path = 'path/to/sysctl'
    fake_hypervisor_detection_class.sysctl_cmd = fake_sysctl

# Generated at 2022-06-13 04:11:41.523897
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    def mock_do_cmd(cmd):
        facts = {
            'machdep.dmi.system-vendor': 'VendorABC',
            'machdep.hypervisor': 'Hypervisor',
            'machdep.dmi.system-product': 'ProductABC',
        }
        if cmd in facts:
            return facts[cmd]
        return ''

    netbsd_virtual = NetBSDVirtual()
    netbsd_virtual._do_cmd = mock_do_cmd

# Generated at 2022-06-13 04:11:44.106494
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector.__class__._platform == "NetBSD"

# Generated at 2022-06-13 04:11:52.273439
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Note: as this is a unit test for a platform-specific class, we are not
    # mocking any methods. Also, no new functions are defined so there is no
    # need to add them to the mocked_function_set.

    netbsd_virtual = NetBSDVirtual()

    # get_virtual_facts() should succeed and return a dict with a subdict
    # named 'virtual'.
    assert netbsd_virtual.get_virtual_facts() == {
        'virtual': {
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
            'virtualization_type': '',
            'virtualization_role': ''
        }
    }

# Generated at 2022-06-13 04:12:00.249157
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test = NetBSDVirtual()
    # mock sysctl output

# Generated at 2022-06-13 04:12:02.407305
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert NetBSDVirtual(None, None, None).get_virtual_facts() == {}


# Generated at 2022-06-13 04:12:17.446430
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    netbsd_virtual = NetBSDVirtual()

    # case: system is NetBSD physical host
    netbsd_virtual.sysctl = {'machdep.dmi.system-product': 'None'}
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

    # case: system is NetBSD virtual machine with products in sysctl
    netbsd_virtual.sysctl = {'machdep.dmi.system-product': 'KVM'}
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:12:19.297417
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == "NetBSD"

# Generated at 2022-06-13 04:12:23.372515
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """
    When /sbin/sysctl exists, but returns a non-zero (error) exit code
    get_virtual_facts() should return an empty dictionary.
    """

    import os.path
    from ansible.module_utils.facts.virtual.sysctl import Sysctl
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

    # Make sure we're testing what we think we are.
    assert NetBSDVirtual._platform == 'NetBSD'

    #
    # Test #1: Call sysctl mock_run_command method which raise exception
    #
    Sysctl._mock_run_command = mock_run_command_raises

    # Create instance of NetBSDVirtual
    netbsd_virtual = NetBSDVirtual()

    # Invocke method get_virtual_facts
    actual_result

# Generated at 2022-06-13 04:12:26.858922
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()

    assert virtual_facts._platform == 'NetBSD'

    assert virtual_facts.get_virtual_facts() == virtual_facts._virtual_facts



# Generated at 2022-06-13 04:12:35.195018
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # pylint: disable=too-many-statements
    # This is a long test, expected to be broken into smaller tests.
    # pylint: disable=unused-variable
    # Some variables are not used yet
    test_base_dir = os.path.dirname(os.path.dirname(__file__))
    sys_class_hypervisor_dir = os.path.join(test_base_dir,
                                            'unit',
                                            'ansible_test_mocks',
                                            'module_utils',
                                            'facts',
                                            'virtual',
                                            'sysctl')

# Generated at 2022-06-13 04:12:38.429818
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    test_object = NetBSDVirtualCollector()
    assert type(test_object._fact_class) == NetBSDVirtual
    assert test_object._platform == 'NetBSD'

# Generated at 2022-06-13 04:12:42.410512
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    '''
    The constructor of NetBSDVirtual might cause a NameError if
    the sysctl program is not found.  This test is to ensure that
    does not happen.
    '''
    testobj = NetBSDVirtual()
    assert isinstance(testobj, NetBSDVirtual)

# Generated at 2022-06-13 04:12:52.634592
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Test with a host platform of NetBSD
    netbsd_virtual = NetBSDVirtual({'ansible_facts': {'system': 'NetBSD'}})
    # Check that virtual_facts is not empty
    assert(netbsd_virtual.virtual_facts != {})
    # Check that virtual_facts['virtualization_type'] is not an empty string
    assert(netbsd_virtual.virtual_facts['virtualization_type'] != '')

    # Test with a host platform that is not NetBSD, this should return an
    # empty dictionary for all the virtualization facts
    netbsd_virtual = NetBSDVirtual({'ansible_facts': {'system': 'Linux'}})
    # Check that virtual_facts is an empty dictionary
    assert(netbsd_virtual.virtual_facts == {})

# Generated at 2022-06-13 04:12:58.963794
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtfacts = NetBSDVirtual({}, {})
    facts = virtfacts.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_subtype'] == 'full'
    assert facts['virtualization_l1_host'] == 'amazon'
    assert facts['virtualization_l1_guest'] == 'xen'
    assert facts['virtualization_l2_guest'] == 'kvm'
    assert 'virtualization_l3_guest' not in facts

# Generated at 2022-06-13 04:13:02.017175
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    obj = NetBSDVirtualCollector()
    assert obj.platform == 'NetBSD'
    assert obj._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:13:19.140573
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    results = dict(platform='NetBSD')
    virtual = NetBSDVirtualCollector(results, None)
    assert virtual._platform == 'NetBSD'


# Generated at 2022-06-13 04:13:21.709672
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    vnetbsd = NetBSDVirtual({}, {}, {}, {})
    assert vnetbsd is not None


# Generated at 2022-06-13 04:13:25.825872
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_obj = NetBSDVirtual()
    netbsd_virtual_obj.sysctl_all_facts = {
        'machdep.dmi.system-product': 'VMware Virtual Platform',
        'machdep.dmi.system-vendor': 'VMware, Inc.',
        }
    if os.path.exists('/dev/xencons'):
        expected_virtual_facts = {
            'virtualization_type': 'xen',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': set(['xen', 'vmware']),
            'virtualization_tech_host': set(['vmware']),
            }

# Generated at 2022-06-13 04:13:27.223587
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual


# Generated at 2022-06-13 04:13:29.458379
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual('')
    assert virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:13:30.908207
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    bsd_virtual = NetBSDVirtual()
    assert bsd_virtual


# Generated at 2022-06-13 04:13:32.426327
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    facts = NetBSDVirtual().get_virtual_facts()
    assert isinstance(facts, dict)

# Generated at 2022-06-13 04:13:35.485632
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    v = NetBSDVirtual()
    actual = v.get_virtual_facts()
    expected = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_system': '',
    }
    assert actual == expected

# Generated at 2022-06-13 04:13:37.668133
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'


# Generated at 2022-06-13 04:13:40.371544
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert isinstance(c, VirtualCollector)
    assert isinstance(c._fact_class, NetBSDVirtual)


# Generated at 2022-06-13 04:14:11.183693
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_detector = NetBSDVirtualCollector()
    virtual_detector.collect()
    assert isinstance(virtual_detector.facts['virtualization_role'], str)
    assert isinstance(virtual_detector.facts['virtualization_type'], str)
    assert isinstance(virtual_detector.facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_detector.facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 04:14:16.881853
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    '''
    Unit test for NetBSDVirtual.get_virtual_facts().
    '''
    class MockSysctl(object):
        '''
        Mock class for Sysctl().get_all()
        '''
        def __init__(self):
            '''
            Constructor
            '''
            self.sysctl_dict = {}

        def get_all(self):
            '''
            Return sysctl_dict
            '''
            return self.sysctl_dict

    class MockOs(object):
        '''
        Mock class for os.path.exists
        '''
        def __init__(self):
            '''
            Constructor
            '''
            self.exists_check = False


# Generated at 2022-06-13 04:14:19.094540
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virt = NetBSDVirtualCollector('')
    assert virt.platform == 'NetBSD'
    assert virt.fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:14:21.838916
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._platform == 'NetBSD'
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual



# Generated at 2022-06-13 04:14:23.770635
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:14:30.468293
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    class MockFile(object):
        def __init__(self, content):
            self._content = content
            self._position = 0

        def readline(self):
            line = self._content[self._position]
            self._position = self._position + 1
            return line

        def readlines(self):
            return self._content

        def read(self):
            return self._content

    virtual_facts = {}
    virtual_facts['virtualization_type'] = ''
    virtual_facts['virtualization_role'] = ''

    class MockOs(object):
        def __init__(self, path_exists):
            self._path_exists = path_exists

        def path_exists(self, path):
            return self._path_exists[path]

    # Test case 1: Fake a real hardware system


# Generated at 2022-06-13 04:14:31.938532
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    try:
        NetBSDVirtualCollector()
    except Exception as e:
        assert False, "failed to execute function 'test_NetBSDVirtualCollector' with error: " + str(e)


# Generated at 2022-06-13 04:14:35.020676
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'


# Generated at 2022-06-13 04:14:39.135188
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:14:42.597795
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    # call class constructor of NetBSDVirtualCollector
    try:
        NetBSDVirtualCollector()
    except Exception as e:
        print('Exception from constructor call: %s' % str(e))
    else:
        print('Expected exception not thrown from constructor call')

# Generated at 2022-06-13 04:15:41.193797
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    # Setup
    collect_mock = NetBSDVirtualCollector()

    expected = {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_technologies': ['xen']
    }

    # Test
    actual = collect_mock._fact_class.get_virtual_facts()

    # Verify
    assert(expected == actual)

# Generated at 2022-06-13 04:15:44.776636
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual(module=object())
    assert netbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:15:47.178107
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdvirtual = NetBSDVirtual('module')
    assert netbsdvirtual.platform == 'NetBSD'
    assert netbsdvirtual.module == 'module'

# Generated at 2022-06-13 04:15:48.690613
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Create an instance of the NetBSDVirtual class
    virtual_facts = NetBSDVirtual()

    # Ensure that get_virtual_facts() returns a dictionary
    assert isinstance(virtual_facts.get_virtual_facts(), dict)

# Generated at 2022-06-13 04:15:53.533570
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual('netbsd')
    virtual._get_sysctl = lambda x: 'foo'
    assert virtual.get_virtual_facts() == {'virtualization_tech_guest': set(), 'virtualization_tech_host': set(), 'virtualization_role': 'host', 'virtualization_type': ''}
    virtual._get_sysctl = lambda x: 'KVM'
    assert virtual.get_virtual_facts() == {'virtualization_tech_guest': set(), 'virtualization_tech_host': {'kvm'}, 'virtualization_role': 'host', 'virtualization_type': 'kvm'}
    virtual._get_sysctl = lambda x: 'VirtualBox'

# Generated at 2022-06-13 04:15:54.511777
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual(None)
    # Test the constructor, can't assume anything about the resulting
    # instantiated objects
    assert(virtual is not None)

# Generated at 2022-06-13 04:15:57.314391
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtualCollector().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'

# Generated at 2022-06-13 04:16:00.043082
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector._platform == 'NetBSD'
    assert NetBSDVirtualCollector._fact_class == NetBSDVirtual


# Generated at 2022-06-13 04:16:10.243956
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    netbsd_virtual._module = object()
    netbsd_virtual._module.get_bin_path = lambda x: '/sbin/sysctl'
    netbsd_virtual.get_file_content = lambda x: 'QEMU Virtual CPU'

    facts = dict()
    facts['kernel'] = 'NetBSD'
    facts['virtual_facts'] = dict()
    facts['virtual_facts']['virtualization_type'] = ''
    facts['virtual_facts']['virtualization_role'] = ''
    facts['virtual_facts']['virtualization_tech_guest'] = set()
    facts['virtual_facts']['virtualization_tech_host'] = set()

    netbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:16:11.018066
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:17:21.959465
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    collect = NetBSDVirtualCollector()
    assert collect._platform == 'NetBSD'
    assert collect._fact_class is NetBSDVirtual

# Generated at 2022-06-13 04:17:29.638808
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual({'ansible_facts': {'machdep.dmi.system-product': 'KVM', 'machdep.dmi.system-vendor': ''}, 'ansible_system': 'NetBSD'})

    assert netbsd.collect()['virtualization_type'] == 'kvm'
    assert netbsd.collect()['virtualization_role'] == 'guest'
    assert 'kvm' in netbsd.collect()['virtualization_tech_guest']
    assert not netbsd.collect()['virtualization_tech_host']

# Generated at 2022-06-13 04:17:30.406713
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()

# Generated at 2022-06-13 04:17:35.725498
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    v = NetBSDVirtual()

    # Test 1: Empty machdep.dmi.system-vendor and machdep.hypervisor
    empty = {'machdep.dmi.system-vendor': '', 'machdep.hypervisor': ''}
    v._get_sysctl_info = lambda: empty
    assert v.get_virtual_facts() == {'virtualization_type': '', 'virtualization_role': '',
                                     'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}

    # Test 2: Non-empty machdep.dmi.system-vendor, machdep.hypervisor
    non_empty = {'machdep.dmi.system-vendor': '-VirtualBox-', 'machdep.hypervisor': 'KVM'}
    v._get_sys

# Generated at 2022-06-13 04:17:40.476256
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Test if object instance of class NetBSDVirtual
    netbsd_virtual = NetBSDVirtual()
    assert isinstance(netbsd_virtual, NetBSDVirtual)
    # Test if object instance of class Virtual
    assert isinstance(netbsd_virtual, Virtual)
    # Test if object instance of class VirtualCollector
    assert isinstance(netbsd_virtual, VirtualCollector)

# Generated at 2022-06-13 04:17:43.523204
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual({})
    assert netbsd.data['virtualization_type'] == ''
    assert netbsd.data['virtualization_role'] == ''
    assert netbsd.data['virtualization_subtype'] == ''
    assert netbsd.data['virtualization_systems'] == {}

# Generated at 2022-06-13 04:17:46.939353
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'
    assert isinstance(netbsd, Virtual)
    assert isinstance(netbsd, VirtualSysctlDetectionMixin)
    assert hasattr(netbsd, 'get_virtual_facts')


# Generated at 2022-06-13 04:17:50.302945
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual_fact = NetBSDVirtual()
    assert isinstance(netbsd_virtual_fact, NetBSDVirtual)
    assert netbsd_virtual_fact.get_virtual_facts()['virtualization_type'] == ''
    assert netbsd_virtual_fact.get_virtual_facts()['virtualization_role'] == ''

# Generated at 2022-06-13 04:17:51.124178
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'

# Generated at 2022-06-13 04:17:52.229965
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.platform == 'NetBSD'
