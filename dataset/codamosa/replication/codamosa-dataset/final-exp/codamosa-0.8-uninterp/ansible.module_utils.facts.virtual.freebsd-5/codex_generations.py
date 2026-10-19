

# Generated at 2022-06-13 03:43:54.998634
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_subclass = FreeBSDVirtualCollector(None, None, None)
    assert facts_subclass.__class__.__name__ == 'FreeBSDVirtualCollector'

# Generated at 2022-06-13 03:44:01.211394
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] in ('', 'xen')
    assert virtual_facts['virtualization_role'] in ('', 'guest')
    assert virtual_facts['virtualization_tech_guest'] == set(['xen']) or virtual_facts['virtualization_tech_guest'] == set([])
    assert virtual_facts['virtualization_tech_host'] == set(['xen']) or virtual_facts['virtualization_tech_host'] == set([])

# Generated at 2022-06-13 03:44:03.783164
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert fbc._platform == 'FreeBSD'
    assert fbc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:05.108800
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Constructor of class FreeBSDVirtualCollector should return object of class FreeBSDVirtualCollector
    FreeBSDVirtualCollector()


# Generated at 2022-06-13 03:44:10.024712
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual(module=None).get_virtual_facts()
    assert virtual_facts['virtualization_type']
    assert virtual_facts['virtualization_role']
    assert virtual_facts['virtualization_role'] == 'physical' or virtual_facts['virtualization_role']
    assert virtual_facts['virtualization_role'] == 'guest' or virtual_facts['virtualization_role']
    assert virtual_facts['virtualization_role'] == 'host' or virtual_facts['virtualization_role']

# Generated at 2022-06-13 03:44:12.402857
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """Test FreeBSDVirtualCollector class"""
    obj = FreeBSDVirtualCollector()
    assert obj.platform == "FreeBSD"
    assert obj._fact_class is FreeBSDVirtual


# Generated at 2022-06-13 03:44:14.204434
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsdvirtual = FreeBSDVirtualCollector()
    assert freebsdvirtual.platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:17.795013
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    collector = FreeBSDVirtualCollector()
    assert collector.__class__.__name__ == 'FreeBSDVirtualCollector'



# Generated at 2022-06-13 03:44:19.874303
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert(vc.platform == 'FreeBSD')
    assert(isinstance(vc.facts, FreeBSDVirtual))

# Generated at 2022-06-13 03:44:21.540833
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:44:30.160408
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fact_subclass = FreeBSDVirtual()
    virtual_facts = fact_subclass.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:44:40.609370
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    module_utils = 'ansible.module_utils.facts.virtual.freebsd'
    module_utils_path = 'ansible.module_utils.facts.virtual.freebsd.FreeBSDVirtual'
    kern_vm_guest = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': '',
    }
    hw_hv_vendor = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': '',
    }

# Generated at 2022-06-13 03:44:43.926723
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    "Test constructor of FreeBSDVirtualCollector"
    osfacts = FreeBSDVirtualCollector(None, None, None, None)
    assert osfacts._fact_class is FreeBSDVirtual
    assert osfacts._platform == 'FreeBSD'


# Generated at 2022-06-13 03:44:45.198570
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 03:44:51.021116
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Function to check for FreeBSDVirtual class method get_virtual_facts
    """
    virtual_facts = FreeBSDVirtual()
    # Set static values for results for sysctl and vendor detection
    # for testing

# Generated at 2022-06-13 03:44:54.247535
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """Check that an instance of FreeBSDVirtualCollector with FreeBSD can be instantiated"""
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:44:56.230580
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:07.791430
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    if os.path.exists('/dev/xen/xenstore'):
        vf_xen = {'virtualization_type': 'xen', 'virtualization_role': 'guest',
                'virtualization_technologies_guest': ['xen', 'hw_vendor'],
                'virtualization_technologies_host': []}
    else:
        vf_xen = {'virtualization_type': '', 'virtualization_role': '',
                'virtualization_technologies_guest': [],
                'virtualization_technologies_host': []}

# Generated at 2022-06-13 03:45:19.035669
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    def get_sysctl_mock(*args, **kwargs):
        if args[0] == 'security.jail.jailed':
            return (1, '')
        elif args[0] == 'hw.hv_vendor':
            return (0, 'KVM')
        elif args[0] == 'kern.vm_guest':
            return (0, 'user')
        return (0, '')

    def get_file_content_mock(*args, **kwargs):
        filename = args[0]
        if filename == '/dev/xen/xenstore':
            return 'Xen Virtual Block Device Interface Version 4.4'

# Generated at 2022-06-13 03:45:21.687147
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:33.886222
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    virtual_facts_expected = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
    }
    freebsd_virtual = FreeBSDVirtual('unit test')
    freebsd_virtual._is_dev_xen_xenstore = lambda: True
    freebsd_virtual.get_virtual_facts()
    assert virtual_facts == virtual_facts_expected

# Generated at 2022-06-13 03:45:35.369258
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """Unit test for constructor of class FreeBSDVirtualCollector
    """
    freebsd = FreeBSDVirtualCollector()
    assert "FreeBSDVirtual" == freebsd.get_fact_class()
    assert "FreeBSD" == freebsd.get_platform()

# Generated at 2022-06-13 03:45:46.931589
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Test case 1: FreeBSD 11.2 running in VirtualBox on macOS Mojave
    kern_vm_guest_data = [
        'kern.vm_guest',
        'hw.hv_vendor',
        'security.jail.jailed'
    ]
    kern_vm_guest_values = [
        'other',
        '',
        '0'
    ]
    hw_hv_vendor_data = [
        'hw.hv_vendor',
        'hw.model'
    ]
    hw_hv_vendor_values = [
        '',
        'VirtualBox'
    ]
    sec_jail_jailed_data = [
        'security.jail.jailed',
        'hw.model'
    ]
    sec_jail

# Generated at 2022-06-13 03:45:48.401066
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    v = FreeBSDVirtualCollector()
    assert v._platform == 'FreeBSD'
    assert v._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:49.888854
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    v.get_virtual_facts()

# Generated at 2022-06-13 03:45:51.883304
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert c.platform == 'FreeBSD'
    assert c._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:54.521778
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    collector = FreeBSDVirtualCollector()
    assert isinstance(collector, VirtualSysctlDetectionMixin)

# Generated at 2022-06-13 03:45:58.145928
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Need to create the object from parent constructor
    VirtualCollector._platform = 'FreeBSD'
    assert FreeBSDSyctlVirtualCollector()._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:06.732153
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = {'virtualization_type': '', 'virtualization_role': ''}
    sysctl_fake_facts = {'kern.vm_guest': 'other', 'hw.hv_vendor': '', 'security.jail.jailed': 0}
    hw_model_fake_facts = {'hw.model': 'pc'}
    v = FreeBSDVirtual()
    v._sysctl_all = sysctl_fake_facts
    v._hw_model = hw_model_fake_facts
    assert v.get_virtual_facts() == virtual_facts
    return True


# Generated at 2022-06-13 03:46:17.699293
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fake_module = {'run_command': lambda x, environ=None, check_rc=True: (0, '', '')}

    # Test on openvz
    freebsd_virtual = FreeBSDVirtual(fake_module)
    freebsd_virtual.module.run_command.side_effect = [
        # Return as if running sysctl on openvz
        (0, 'security.jail.jailed: 0', ''),
        # Return as if runing sysctl on openvz
        (0, 'hw.hv_vendor: OpenVZ', ''),
        # Return as if runing sysctl on openvz
        (0, 'kern.vm_guest: vkernel', '')
    ]
    # Get a dict of virtual facts from FreeBSDVirtual
    facts = freebsd_virtual.get_

# Generated at 2022-06-13 03:46:26.704533
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert isinstance(obj, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:46:28.253631
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    factCollector = FreeBSDVirtualCollector()
    assert factCollector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:30.172016
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''
    Unit test for class FreeBSDVirtualCollector.
    '''
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'


# Generated at 2022-06-13 03:46:31.239846
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:32.621203
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    import platform
    assert platform.system() == 'FreeBSD'
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:46:35.661547
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():

    assert(FreeBSDVirtualCollector._platform == 'FreeBSD')
    assert(FreeBSDVirtualCollector._fact_class == FreeBSDVirtual)

# Generated at 2022-06-13 03:46:39.735324
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Constructor of class FreeBSDVirtualCollector should construct object
    # with both _platform and _fact_class attributes set to 'FreeBSD'
    collector = FreeBSDVirtualCollector()

    assert collector._platform == 'FreeBSD'
    assert collector._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:41.209094
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert hasattr(FreeBSDVirtualCollector(), '_platform')

# Generated at 2022-06-13 03:46:44.704037
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'
    assert obj._fact_class.platform == 'FreeBSD'
    assert obj.regenerate_facter_cache_cmd == 'pkill -KILL facter ; true'

# Generated at 2022-06-13 03:46:48.206017
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:47:06.589199
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector, VirtualCollector)
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:07.178587
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 03:47:13.958567
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert isinstance(virtual_facts['virtualization_type'], str)
    assert isinstance(virtual_facts['virtualization_role'], str)
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:47:15.606159
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    Test to create (instantiate) an object of FreeBSDVirtualCollector.
    """
    obj = FreeBSDVirtualCollector([])
    assert obj is not None

# Generated at 2022-06-13 03:47:17.935094
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Test calling the constructor with a valid _platform
    virtual_detect = FreeBSDVirtualCollector()
    assert virtual_detect._platform == 'FreeBSD'

    # Test calling the constructor with an invalid _platform
    try:
        virtual_detect = FreeBSDVirtualCollector(platform='Linux')
    except:
        pass

# Generated at 2022-06-13 03:47:24.499029
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts of class FreeBSDVirtual."""
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    from . import patched_call, virtual_sysctl_facts, virtual_vendor_facts

    class TestFreeBSDVirtual(FreeBSDVirtual, VirtualSysctlDetectionMixin):
        def __init__(self):
            self.platform = 'FreeBSD'

    bsd_virtual = TestFreeBSDVirtual()
    bsd_virtual.detect_virt_product = patched_call(virtual_sysctl_facts)
    bsd_virtual.detect_virt_vendor = patched_call(virtual_vendor_facts)

# Generated at 2022-06-13 03:47:33.751233
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.sysctl import ModuleStub
    fb = FreeBSDVirtual(ModuleStub())
    facts = fb.get_virtual_facts()
    assert len(facts['virtualization_tech_host']) == 0, facts['virtualization_tech_host']
    assert len(facts['virtualization_tech_guest']) == 0, facts['virtualization_tech_gues']
    assert len(facts['virtualization_vendor']) == 0, facts['virtualization_vendor']
    assert facts['virtualization_role'] == '', facts['virtualization_role']
    assert facts['virtualization_type'] == '', facts['virtualization_type']

if __name__ == '__main__':
    test_FreeBSD

# Generated at 2022-06-13 03:47:36.567336
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert(isinstance(fvc._fact_class, FreeBSDVirtual))
    assert(fvc._platform == 'FreeBSD')
    assert(fvc.collect() == fvc._fact_class)

# Generated at 2022-06-13 03:47:37.881666
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv._fact_class.platform == 'FreeBSD'
    assert fv._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:38.297397
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector

# Generated at 2022-06-13 03:48:04.568855
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    def fake_sysctl(fact):
        return {'security.jail.jailed': 0, 'hw.hv_vendor': 'bhyve', 'kern.vm_guest': 'none'}[fact]

    virt_facts = FreeBSDVirtual(collect_sysctl_facts=fake_sysctl)

    assert virt_facts.get_virtual_facts() == {'virtualization_type': '',
                                              'virtualization_role': '',
                                              'virtualization_tech_host': set(),
                                              'virtualization_tech_guest': set()}

# Generated at 2022-06-13 03:48:07.706998
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    data = {'virtualization_type': '',
            'virtualization_role': ''}
    assert FreeBSDVirtual().get_virtual_facts() == data

# Generated at 2022-06-13 03:48:10.984413
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = VirtualCollector(None, None)
    assert virtual_facts.__class__.__name__ == 'FreeBSDVirtualCollector'


# Generated at 2022-06-13 03:48:19.350776
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:48:29.157468
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from multiprocessing import Pipe
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import FactCache

    conn, child_conn = Pipe()
    cache = FactCache()
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    freebsd = FreeBSDVirtual(module=module, cache=cache, conn=child_conn)

    # Add test, this is a bit dangerous but it works.
    freebsd.detect_virt_product = lambda x: dict(
        virtualization_tech_guest=set(['bhyve']),
        virtualization_tech_host=set(['docker']),
    )


# Generated at 2022-06-13 03:48:38.298115
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    custom_facts = {}
    custom_facts['path_exists'] = {
        '/dev/xen/xenstore': True,
        '/dev/xen/backend': False,
    }
    custom_facts['file_contents'] = {
        '/proc/xen': '',
    }
    custom_facts['sysctl'] = {
        'kern.vm_guest': '',
        'security.jail.jailed': '',
        'hw.hv_vendor': '',
        'hw.hv_version': '',
    }
    custom_facts['cmd'] = {
        '/sbin/sysctl -n hw.model': '',
    }
    virtual = FreeBSDVirtual(custom_facts)

    # Test when all custom_facts are empty.
    assert virtual.get

# Generated at 2022-06-13 03:48:42.819082
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual(None).get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:48:44.988220
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    class_inst = FreeBSDVirtualCollector()
    assert class_inst.platform == 'FreeBSD'
    assert class_inst._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:48:46.963494
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    print(facts)


# Generated at 2022-06-13 03:48:48.106664
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 03:49:56.085020
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Create instance of class FreeBSDVirtualCollector
    freebsd_virtual_collector = FreeBSDVirtualCollector()

    # Check instance of class FreeBSDVirtualCollector
    assert isinstance(freebsd_virtual_collector, VirtualCollector)
    assert isinstance(freebsd_virtual_collector, FreeBSDVirtualCollector)


# Generated at 2022-06-13 03:49:57.163375
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    assert isinstance(v.get_virtual_facts(), dict)

# Generated at 2022-06-13 03:49:58.813794
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert(FreeBSDVirtualCollector._platform == 'FreeBSD')


# Generated at 2022-06-13 03:50:05.321426
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Setup a test FreeBSD file system
    def setup_fs(d):
        d.add(u'tmp', 'dir')
        d.add(u'/tmp/ansible_facts_virtual_kern.vm_guest', 'symlink')
        d.add(u'/tmp/ansible_facts_virtual_hw.hv_vendor', 'symlink')
        d.add(u'/tmp/ansible_facts_virtual_security.jail.jailed', 'symlink')
        d.add(u'/tmp/ansible_facts_virtual_hw.model', 'symlink')
        d.add(u'/tmp/ansible_facts_virtual_kern.vm_guest_Xen', 'symlink')

# Generated at 2022-06-13 03:50:13.666065
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'
    assert obj._fact_class == FreeBSDVirtual
    assert obj.collect() is True
    assert isinstance(obj.get_sysctl_virtual_facts(), dict)
    assert isinstance(obj.get_virtual_facts(), dict)
    # Make sure all mandatory keys are there in virtual_facts.
    for key in ('virtualization_type',
                'virtualization_role',
                'virtualization_tech_host',
                'virtualization_tech_guest'):
        assert key in obj.get_virtual_facts()


# Generated at 2022-06-13 03:50:15.095441
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert isinstance(fbc._fact_class, FreeBSDVirtual)

# Generated at 2022-06-13 03:50:19.368919
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert isinstance(FreeBSDVirtualCollector._fact_class(None), Virtual)
    assert isinstance(FreeBSDVirtualCollector._fact_class(None), VirtualSysctlDetectionMixin)
    assert isinstance(FreeBSDVirtualCollector(None), VirtualCollector)


# Generated at 2022-06-13 03:50:24.728800
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    expected_facts = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
    }
    with open('/proc/cpuinfo') as (cpuinfo):
        cpu_lines = cpuinfo.readlines()
    with open('/proc/self/status') as (status):
        status_lines = status.readlines()
    with open('/proc/self/mountinfo') as (mountinfo):
        mnt_lines = mountinfo.readlines()
    with open('/proc/self/sched') as (sched):
        sched_lines = sched.readlines()
    with open('/proc/self/mounts') as (proc_mounts):
        mounts_lines = proc_mounts.readlines()

# Generated at 2022-06-13 03:50:26.911294
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.platform == "FreeBSD"
    assert obj._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:31.203855
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual({'ansible_system': 'FreeBSD'})
    vf = v.get_virtual_facts()

    assert 'virtualization_type' in vf
    assert 'virtualization_role' in vf
    assert 'virtualization_tech_guest' in vf
    assert 'virtualization_tech_host' in vf

# Generated at 2022-06-13 03:52:54.398016
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.get_virtual_facts().get('virtualization_type') == 'xen'
    assert virtual_collector.get_virtual_facts().get('virtualization_role') == 'guest'
    assert 'host' not in virtual_collector.get_virtual_facts().get('virtualization_type')

# Generated at 2022-06-13 03:52:59.576396
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    mock_obj = FreeBSDVirtual()
    fake_sysctl_output = 'hw.model: QEMU Virtual CPU version 2.5+\n' \
                         'kern.vm_guest: other\n' \
                         'security.jail.jailed: 0'
    cloud_provider_facts = {'virtual_facts': {'hw_model': 'QEMU Virtual CPU version 2.5+'}}
    sysctl = {'kern_vm_guest': 'other', 'sec_jail_jailed': '0'}
    guest_tech = {'qemu', 'kvm', 'virtualbox-2.2', 'virtualbox-ose-4.2', 'vmware-vmx', 'bhyve'}
    host_tech = set()

# Generated at 2022-06-13 03:53:05.342774
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create a class instance
    test_class = FreeBSDVirtual()
    # Create a fact dictionary
    fact_dict = {}
    # Call method get_virtual_facts of the class
    virtual_facts = test_class.get_virtual_facts(fact_dict)
    # Assert method get_virtual_facts returns expected values
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:53:07.181563
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''
    Args:
        None
    Returns:
        None
    '''
    # call the function
    virtual_instance = FreeBSDVirtual()
    facts = virtual_instance.get_virtual_facts()
    # convert result to dict
    facts = dict(facts)
    assert not facts


# Generated at 2022-06-13 03:53:08.002503
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert isinstance(x, dict)

# Generated at 2022-06-13 03:53:10.013020
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():  # pylint: disable=invalid-name
    obj = FreeBSDVirtual()
    assert isinstance(obj.get_virtual_facts(), dict)

# Generated at 2022-06-13 03:53:10.393633
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 03:53:11.750958
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_instance = FreeBSDVirtualCollector()
    assert facts_instance._platform == 'FreeBSD'
    assert facts_instance._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:53:14.429817
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Given
    module_mock = MockModule()
    # When
    virtual_facts = FreeBSDVirtual(module_mock).get_virtual_facts()
    # Then
    assert virtual_facts == {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': ['xen'],
        'virtualization_tech_host': None,
    }



# Generated at 2022-06-13 03:53:15.235431
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector()
    assert isinstance(virtual_facts, FreeBSDVirtual)