

# Generated at 2022-06-13 04:09:53.166741
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector

# Generated at 2022-06-13 04:09:55.031061
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_obj = NetBSDVirtual()
    assert netbsd_virtual_obj.platform == 'NetBSD'


# Generated at 2022-06-13 04:09:57.008350
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nv = NetBSDVirtualCollector()
    assert nv.platform == 'NetBSD'
    assert nv._fact_class == NetBSDVirtual
    assert nv.detected

# Generated at 2022-06-13 04:10:00.470524
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    instance = NetBSDVirtualCollector()
    assert isinstance(instance, NetBSDVirtualCollector)


# Generated at 2022-06-13 04:10:02.299031
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    nbsd_virtual = NetBSDVirtual()
    assert nbsd_virtual.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:04.569400
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_facts = NetBSDVirtual()
    assert netbsd_virtual_facts.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:06.726083
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdVirt_obj = NetBSDVirtual({})
    # check if the class is a instance of a class
    assert isinstance(netbsdVirt_obj, NetBSDVirtual)

# Generated at 2022-06-13 04:10:08.427589
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsdVirtualObj = NetBSDVirtual(None)
    assert netbsdVirtualObj.platform == 'NetBSD'


# Generated at 2022-06-13 04:10:13.238914
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    from ansible.module_utils import basic
    import sys

    if sys.version_info.major < 3:
        input_func = raw_input  # noqa: F821
    else:
        input_func = input

    # Fake a module
    mock_module = type('AnsibleModule', (object,), {
        'params': {},
        'check_mode': False
    })

    # Fake a system
    mock_system = type('System', (object,), {
        'sysname': 'NetBSD',
        'machine': 'amd64',
        'distribution': ('NetBSD', '7.0', 'GENERIC')
    })

    # Fake a distro class

# Generated at 2022-06-13 04:10:14.656666
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert isinstance(virtual_facts, dict)

# Generated at 2022-06-13 04:10:18.867719
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    NetBSDVirtualCollector()


# Generated at 2022-06-13 04:10:21.527915
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    virtual = NetBSDVirtualCollector()
    assert virtual._platform == 'NetBSD'
    assert virtual._fact_class.__name__ == 'NetBSDVirtual'

# Generated at 2022-06-13 04:10:23.118229
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector().platform == 'NetBSD'


# Generated at 2022-06-13 04:10:25.995526
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert isinstance(netbsd_virtual, NetBSDVirtual)
    assert isinstance(netbsd_virtual, Virtual)


# Generated at 2022-06-13 04:10:27.398434
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    net_bsd_virtual_collector = NetBSDVirtualCollector()
    assert net_bsd_virtual_collector._fact_class is NetBSDVirtual
    assert net_bsd_virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:29.392791
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert type(netbsd_virtual.get_virtual_facts()) is dict

# Generated at 2022-06-13 04:10:31.616358
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_netbsd = NetBSDVirtual()
    assert virtual_netbsd.platform == 'NetBSD'

# Generated at 2022-06-13 04:10:40.448855
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual({})
    virtual.sysctl = {'machdep.dmi.system-product': 'Bochs',
                      'machdep.dmi.system-vendor': 'innotek GmbH',
                      'machdep.hypervisor': 'bhyve',
                      'kern.hostname': 'test-host'
                    }
    virtual.product_name = virtual.sysctl['machdep.dmi.system-product']
    virtual.product_serial = None
    virtual.product_uuid = None
    virtual.device_name = virtual.sysctl['machdep.hypervisor']
    virtual.vendor_name = virtual.sysctl['machdep.dmi.system-vendor']
    virtual.system_name = virtual.sysctl['kern.hostname']
    virtual

# Generated at 2022-06-13 04:10:42.248416
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert type(netbsd_virtual_collector) is NetBSDVirtualCollector

# Generated at 2022-06-13 04:10:46.223458
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    netbsd_virtual_collector = NetBSDVirtualCollector()
    assert netbsd_virtual_collector._fact_class == NetBSDVirtual
    assert netbsd_virtual_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:10:57.521966
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Given: I have an instance of NetBSDVirtual
    facts = NetBSDVirtual()
    # Then: It should have a `platform` attribute that is set to `NetBSD` 
    assert facts.platform == "NetBSD"
    # Then: It should have a `get_virtual_facts` method that is callable
    assert callable(facts.get_virtual_facts)

# Generated at 2022-06-13 04:11:02.592273
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_info = NetBSDVirtual()
    virtual_info.collect_facts()
    result = virtual_info.get_virtual_facts()
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''
    assert result['virtualization_tech_guest'] == ['']
    assert result['virtualization_tech_host'] == set('')

# Generated at 2022-06-13 04:11:14.473914
# Unit test for method get_virtual_facts of class NetBSDVirtual

# Generated at 2022-06-13 04:11:23.007623
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fake_sysctl = {
        'machdep.hypervisor': 'KVM',
        'machdep.dmi.system-product': 'KVM',
        'machdep.dmi.system-vendor': 'KVM',
    }

    virtual = NetBSDVirtual('dummy_module', 'dummy_collector', [], {}, {}, fake_sysctl)
    facts = virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'kvm'
    assert 'guest' in facts['virtualization_role']
    assert 'host' in facts['virtualization_role']
    assert 'kvm' in facts['virtualization_tech_guest']
    assert 'kvm' in facts['virtualization_tech_host']

# Generated at 2022-06-13 04:11:26.334959
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    c = NetBSDVirtualCollector()
    assert(c._fact_class == NetBSDVirtual)
    assert(c._platform == 'NetBSD')
    assert(c._capability == 'virtual')


# Generated at 2022-06-13 04:11:28.269077
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nv = NetBSDVirtualCollector()
    assert isinstance(nv, NetBSDVirtualCollector)
    assert nv._platform == 'NetBSD'

# Generated at 2022-06-13 04:11:30.964271
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual_facts_class = NetBSDVirtual()
    assert netbsd_virtual_facts_class._platform == 'NetBSD'
    assert netbsd_virtual_facts_class._fact_class._platform == 'NetBSD'

# Generated at 2022-06-13 04:11:32.496945
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual({})
    assert isinstance(netbsd_virtual, NetBSDVirtual)


# Generated at 2022-06-13 04:11:36.427129
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    """
    Constructor of NetBSDVirtualCollector class can be initialized.
    """
    netbsdVirtualCollector = NetBSDVirtualCollector()
    assert netbsdVirtualCollector

# Generated at 2022-06-13 04:11:38.610090
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert virtual._fact_class is NetBSDVirtual
    assert virtual._platform == 'NetBSD'

# Generated at 2022-06-13 04:11:53.604809
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    virtual_facts = netbsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_type'] == ''


# Generated at 2022-06-13 04:11:55.409078
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd = NetBSDVirtual()
    assert netbsd.get_virtual_facts() == {}


# Generated at 2022-06-13 04:11:57.252155
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    result = NetBSDVirtualCollector()
    assert result._fact_class == NetBSDVirtual
    assert result._platform == 'NetBSD'


# Generated at 2022-06-13 04:11:58.773761
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual()
    assert(virt.__class__.__name__ == 'NetBSDVirtual')


# Generated at 2022-06-13 04:12:00.438562
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    assert issubclass(NetBSDVirtual, Virtual)


# Generated at 2022-06-13 04:12:11.927590
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    with open('/sysctl.out') as f:
        sysctl_out = f.read()

    with open('/dmesg.boot') as f:
        dmesg_boot = f.read()

    netbsd_virtual = NetBSDVirtual()

    def run_mock(self, module, module_args, check_rc=True):
        return {'rc': 0, 'stdout': sysctl_out, 'stdout_lines': sysctl_out.splitlines()}

    netbsd_virtual.module.run_command = run_mock

    setattr(netbsd_virtual.module, 'dmesg_boot', dmesg_boot)

    get_virtual_facts_result = netbsd_virtual.get_virtual_facts()
    # Check the result of the method
    assert get_virtual

# Generated at 2022-06-13 04:12:14.135667
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual()
    assert virt.platform == 'NetBSD'

# Generated at 2022-06-13 04:12:16.603888
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    facts_collector = NetBSDVirtualCollector()
    assert facts_collector._fact_class == NetBSDVirtual
    assert facts_collector._platform == 'NetBSD'

# Generated at 2022-06-13 04:12:19.380169
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    netbsd_virtual = NetBSDVirtual()
    expected_virtual_facts = dict(
            virtualization_type='xen',
            virtualization_role='guest',
            virtualization_type_role='xen_guest',
            virtualization_tech_guest=set(['xen']),
            virtualization_tech_host=set([]),
    )
    assert netbsd_virtual.get_virtual_facts() == expected_virtual_facts

# Generated at 2022-06-13 04:12:21.852781
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    vc = NetBSDVirtualCollector()
    assert isinstance(vc, VirtualCollector)
    assert isinstance(vc._fact_class(), Virtual)


# Generated at 2022-06-13 04:12:52.261383
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    '''
    Constructor of NetBSDVirtualCollector class is tested
    '''
    netbsd_virtual_object = NetBSDVirtualCollector()
    assert netbsd_virtual_object.platform == 'NetBSD'
    assert netbsd_virtual_object._fact_class.platform == 'NetBSD'


# Generated at 2022-06-13 04:13:00.104961
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Set up mock facts
    sysctl_dmi = {'machdep': {'dmi': {'system-product': 'VMware Virtual Platform',
                                      'system-vendor': 'GOOGLE'}}}
    sysctl_hypervisor = {'machdep': {'hypervisor': 'BHYVE'}}

    # Requested virtual facts
    virtual_facts = {'virtualization_type': '',
                     'virtualization_role': '',
                     'virtualization_product_name': '',
                     'virtualization_product_version': ''}

    # NetBSDVirtual class instance with mocked facts
    bhyve_virtual = NetBSDVirtual(sysctl_dmi, sysctl_hypervisor, None)

    # Returned virtual facts with mocked facts

# Generated at 2022-06-13 04:13:09.346190
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.netbsd_virtual import NetBSDVirtual
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    from ansible.module_utils._text import to_bytes
    import sys
    # Create an instance of NetBSDVirtual class
    netbsd_virtual_object = NetBSDVirtual()
    # Create an instance of the FactCollector class
    fact_collector_object = FactCollector(None, None)
    # Create a dictionary which holds all the sysctl_paths and sysctl_keys
    # used during get_virtual_facts method of NetBSDVirtual class

# Generated at 2022-06-13 04:13:10.274189
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    assert NetBSDVirtualCollector() is not None

# Generated at 2022-06-13 04:13:13.407477
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert virtual_facts.get_virtual_facts()


# Generated at 2022-06-13 04:13:17.529830
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts



# Generated at 2022-06-13 04:13:20.635787
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    nbsd_vc = NetBSDVirtualCollector()
    assert nbsd_vc._platform == 'NetBSD'
    assert nbsd_vc._fact_class == NetBSDVirtual

# Generated at 2022-06-13 04:13:29.462293
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    netbsdvirtual = NetBSDVirtual()
    input_path = netbsdvirtual._sysctl_path + '/machdep.dmi.system-product'
    netbsdvirtual._write_file(input_path, 'VMware Virtual Platform\n')
    assert netbsdvirtual.get_virtual_facts()['virtualization_type'] == 'vmware'
    assert netbsdvirtual.get_virtual_facts()['virtualization_role'] == 'guest'
    assert netbsdvirtual.get_virtual_facts()['virtualization_tech_guest'] == {'vmware'}
    assert netbsdvirtual.get_virtual_facts()['virtualization_tech_host'] == set()
    netbsdvirtual._remove_file(input_path)

    netbsdvirtual = NetBSDVirtual()
    input_path = net

# Generated at 2022-06-13 04:13:39.401278
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fact_test_dict = {}
    fact_test_label = 'test_label'

    test_NetBSDVirtual = NetBSDVirtual(fact_test_dict, fact_test_label)

    def mock_detect_virt_product(self, key, regexp=None):
        return {'virtualization_type': 'oracle',
                'virtualization_role': 'guest',
                'virtualization_tech_guest': set(['oracle']),
                'virtualization_tech_host': set(['oracle'])}

    test_NetBSDVirtual.detect_virt_product = mock_detect_virt_product


# Generated at 2022-06-13 04:13:47.847810
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts_method = NetBSDVirtual()
    virtual_facts_method.sysctl_hardware_machdep_dmi_system_product = 'VirtualBox'
    virtual_facts_method.sysctl_hardware_machdep_dmi_system_vendor = 'innotek GmbH'
    virtual_facts_method.sysctl_hardware_machdep_hypervisor = 'VMWare'
    virtual_facts = virtual_facts_method.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_product_name'] == 'VirtualBox'
    assert virtual_facts['virtualization_product_version'] == ''

# Generated at 2022-06-13 04:14:55.104732
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    """
    Fake sysctl output for Debian
    """
    sysctl_output_qemu = (
        '''
        machdep.dmi.system-product=QEMU Virtual CPU version 2.5+
        machdep.dmi.system-vendor=QEMU
        machdep.hypervisor=QEMU
        '''
    )

    v = NetBSDVirtual()

    fake_dict_1 = {
        b'out': sysctl_output_qemu,
        b'rc': 0,
        b'err': ''
    }
    assert v.get_virtual_facts() == {
        'virtualization_type': 'kvm',
        'virtualization_role': 'guest',
        'virtualization_technologies': ['qemu']
    }

# Generated at 2022-06-13 04:14:56.865814
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt_obj = NetBSDVirtual()
    assert virt_obj.platform == 'NetBSD'


# Generated at 2022-06-13 04:15:04.647956
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual = NetBSDVirtual({})

    # Test for virtualization_tech_guest, virtualization_tech_host and
    # virtualization_type
    inst = virtual.get_virtual_facts()
    assert 'virtualization_tech_guest' in inst
    assert 'virtualization_tech_host' in inst
    assert 'virtualization_type' in inst
    assert isinstance(inst['virtualization_tech_guest'], set)
    assert isinstance(inst['virtualization_tech_host'], set)
    assert isinstance(inst['virtualization_type'], str)

# Generated at 2022-06-13 04:15:05.527130
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virt = NetBSDVirtual()

# Generated at 2022-06-13 04:15:10.110817
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    # Check if class has been initialized properly
    netbsdVirtual = NetBSDVirtual()
    assert netbsdVirtual.platform == 'NetBSD'
    assert netbsdVirtual.product_name == 'machdep.dmi.system-product'


# Generated at 2022-06-13 04:15:14.424271
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # Execute the method under test
    VirtualCollector._private_temp_dir = os.path.join(os.path.dirname(__file__), 'private_dir')
    facts = NetBSDVirtualCollector.fetch_virtual_facts()
    # Virtualization type should be 'xen'
    assert facts['virtualization_type'] == 'xen'
    # Virtualization role should be 'guest'
    assert facts['virtualization_role'] == 'guest'
    # Virtualization guest techiniques should be ['xen']
    assert facts['virtualization_tech_guest'] == set(['xen'])
    # Virtualization host techiniques should be empty
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 04:15:17.022239
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual = NetBSDVirtual()
    assert isinstance(virtual, Virtual)
    assert isinstance(virtual, VirtualSysctlDetectionMixin)
    assert isinstance(virtual, NetBSDVirtual)
    assert virtual._platform == 'NetBSD'


# Generated at 2022-06-13 04:15:27.991797
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():

    class Mock_NetBSDVirtual(NetBSDVirtual):
        def sysctl(self, keys):

            mock_sysctl_facts = {
                'machdep.dmi.system-product': 'OpenStack Nova',
                'machdep.dmi.system-vendor': 'OpenStack Foundation',
                'machdep.hypervisor': 'bhyve'
            }

            return {keys: mock_sysctl_facts[keys]}

    virtual_facts = NetBSDVirtual()
    assert virtual_facts.get_virtual_facts() == {'virtualization_type': 'openstack', 'virtualization_role': 'guest'}

    virtual_facts = Mock_NetBSDVirtual()
    assert virtual_facts.get_virtual_facts() == {'virtualization_type': 'bhyve', 'virtualization_role': 'guest'}

# Generated at 2022-06-13 04:15:37.513128
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    if not hasattr(os, 'uname') or not hasattr(os, 'access'):
        # On some platforms (e.g. windows) these functions may not exist
        return False
    uname_result = os.uname()
    if uname_result[0] != 'NetBSD':
        return False
    f = '/dev/xen/evtchn'
    collect_instance = NetBSDVirtualCollector()
    return collect_instance._platform == 'NetBSD' and \
        'NetBSDVirtual' in collect_instance._fact_class.__name__ and \
        (not os.path.exists(f) or os.access(f, os.R_OK | os.W_OK)) and \
        len(collect_instance.collect()) == 0

# Generated at 2022-06-13 04:15:44.364999
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_input_fact_sysctl = {
        'machdep.hypervisor': 'none',
        'machdep.dmi.system-product': 'VMware Virtual Platform',
        'machdep.dmi.system-vendor': 'VMware, Inc.',
    }
    vm = NetBSDVirtual(module=None, collected_facts={'ansible_facts': test_input_fact_sysctl})
    virtual_facts = vm.get_virtual_facts()
    assert virtual_facts == {
        'virtualization_type': 'VMware Virtual Platform',
        'virtualization_role': 'guest',
        'virtualization_tech_host': set(['VMware']),
        'virtualization_tech_guest': set(['VMware']),
    }



# Generated at 2022-06-13 04:18:18.218405
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual().get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'oracle'
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:18:19.751282
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    virtual_facts = NetBSDVirtual()
    assert type(virtual_facts.get_virtual_facts()) is dict

# Generated at 2022-06-13 04:18:23.311478
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():

    netbsd = NetBSDVirtual(dict())

    assert netbsd.platform == 'NetBSD'

# Generated at 2022-06-13 04:18:32.178365
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    v = NetBSDVirtual()

    # Test empty data
    v.sysctl = {}
    v.dmi_data = {}
    v.facts = {}

    assert v.get_virtual_facts() == {}

    # Test empty data
    v.sysctl = {'machdep.dmi.system-product': 'KVM'}
    v.dmi_data = {}
    v.facts = {}


# Generated at 2022-06-13 04:18:37.482825
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    # arrange
    netbsd_virtual_obj = NetBSDVirtual()
    # act
    netbsd_virtual_obj.get_virtual_facts()
    # assert
    assert netbsd_virtual_obj.platform == 'NetBSD'

# Generated at 2022-06-13 04:18:41.728224
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    test_virt_facts = NetBSDVirtual()
    virt_facts = test_virt_facts.get_virtual_facts()

    assert 'virtualization_tech_guest' in virt_facts
    assert 'virtualization_tech_host' in virt_facts
    assert 'virtualization_type' in virt_facts
    assert 'virtualization_role' in virt_facts

# Generated at 2022-06-13 04:18:44.988228
# Unit test for constructor of class NetBSDVirtualCollector
def test_NetBSDVirtualCollector():
    print('Testing constructor of class NetBSDVirtualCollector')

    virtual_collector = NetBSDVirtualCollector()
    assert virtual_collector.platform == 'NetBSD'
    assert virtual_collector.__class__.__bases__[0] == VirtualCollector


# Generated at 2022-06-13 04:18:51.180700
# Unit test for method get_virtual_facts of class NetBSDVirtual
def test_NetBSDVirtual_get_virtual_facts():
    fake_sysctl = {
        'machdep.dmi.system-vendor': 'HP',
        'machdep.dmi.system-product': 'ProLiant DL380 G6',
        'machdep.hypervisor': 'None'
    }

    test_instance = NetBSDVirtual(fake_sysctl)
    test_facts = test_instance.get_virtual_facts()

    assert test_facts['virtualization_type'] == 'hvm'
    assert test_facts['virtualization_role'] == 'guest'

    assert 'xen' not in test_facts['virtualization_tech_guest']
    assert 'xen' not in test_facts['virtualization_tech_host']
# Unit test end

# Generated at 2022-06-13 04:18:53.143810
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    virtual_facts = NetBSDVirtual()
    assert hasattr(virtual_facts, 'platform')
    assert virtual_facts.platform == 'NetBSD'


# Generated at 2022-06-13 04:18:55.404796
# Unit test for constructor of class NetBSDVirtual
def test_NetBSDVirtual():
    netbsd_virtual = NetBSDVirtual()
    assert netbsd_virtual.platform == 'NetBSD'