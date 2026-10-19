

# Generated at 2022-06-13 03:44:01.176368
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''
    Test get_virtual_facts of class FreeBSDVirtual
    '''
    test_facts = {}
    test_facts['kernel'] = 'FreeBSD'
    test_facts['virtualization_type'] = ''
    test_facts['virtualization_role'] = ''
    test_facts['virtualization_tech_guest'] = set()
    test_facts['virtualization_tech_host'] = set()

    # Test case 1
    # Test for '/dev/xen/xenstore' path
    test_facts['virtualization_type'] = ''
    test_facts['virtualization_role'] = ''
    test_facts['virtualization_tech_guest'] = set()
    test_facts['virtualization_tech_host'] = set()
    os.path.exists = lambda x: True
    virtual_facts = FreeBSD

# Generated at 2022-06-13 03:44:02.686724
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:44:11.189269
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    test_virtual_facts = dict()
    test_virtual_facts['virtualization_type'] = ''
    test_virtual_facts['virtualization_role'] = ''
    test_virtual_facts['virtualization_tech_guest'] = set()
    test_virtual_facts['virtualization_tech_host'] = set()

    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual.get_virtual_facts = Virtual.get_virtual_facts.__get__(freebsd_virtual)
    freebsd_virtual.detect_virt_product = VirtualSysctlDetectionMixin.detect_virt_product.__get__(freebsd_virtual)

# Generated at 2022-06-13 03:44:14.378054
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = dict()
    virtual = FreeBSDVirtual(facts)
    virtual.get_virtual_facts()
    # TODO: test the output of get_virtual_facts() with a FreeBSD
    # system running in a supported virtualization context.

# Generated at 2022-06-13 03:44:16.040828
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    module = FreeBSDVirtualCollector()
    assert module._platform == 'FreeBSD'


# Generated at 2022-06-13 03:44:18.016620
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    Checks whether constructor of FreeBSDVirtualCollector class works.
    """
    virt_class = FreeBSDVirtualCollector()
    assert virt_class._platform == 'FreeBSD'
    assert virt_class._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:18.986862
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:44:22.735806
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = {
        'kernel': 'FreeBSD',
    }

    f = FreeBSDVirtual(module=None, facts=facts)
    assert 'FreeBSD' == f.platform

    result = f.get_virtual_facts()
    assert result['virtualization_type'] == 'None'
    assert result['virtualization_role'] == 'guest'



# Generated at 2022-06-13 03:44:28.351311
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collection = FreeBSDVirtualCollector()
    assert collection.platform == 'FreeBSD'
    assert collection.fact_class == FreeBSDVirtual
    assert collection.collect() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }

# Generated at 2022-06-13 03:44:33.304856
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    def create_FreeBSDVirtual(*args):
        return FreeBSDVirtual(*args)

    virtual = create_FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert type(virtual_facts) == dict
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:44:39.540959
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:41.398871
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    modules = LinuxVirtualCollector().collect()
    assert isinstance(modules, list)

# Generated at 2022-06-13 03:44:42.790269
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 03:44:46.378167
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virt_collector = FreeBSDVirtualCollector()
    assert virt_collector.platform == 'FreeBSD'
    assert virt_collector.__class__.__bases__[0] is VirtualCollector
    assert virt_collector.get_virtual_facts().__class__.__name__ == 'FreeBSDVirtual'

# Generated at 2022-06-13 03:44:54.249333
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsdvirtual = FreeBSDVirtual()
    freebsdvirtual.sysctl = dict(
        kern=dict(vm_guest='bsd'),
        hw=dict(hv_vendor='n/a'),
        security=dict(jail=dict(jailed='0')),
    )
    facts = freebsdvirtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'bsd'
    assert facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:44:54.737884
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector


# Generated at 2022-06-13 03:44:57.104461
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == "FreeBSD"
    assert virtual_collector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:45:00.926060
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''
    Constructor of class FreeBSDVirtualCollector
    '''
    obj = FreeBSDVirtualCollector("test")
    assert obj.platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:04.328424
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)
    fvc = FreeBSDVirtualCollector()
    assert fvc.platform == 'FreeBSD'
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:10.949470
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector()
    facts_dict = virtual_facts.collect()

    # Test if facts_dict is empty
    if not facts_dict:
        raise AssertionError("Failed: Unable to create facts_dict, it is empty")

    # Test if 'virtual_facts' key is present in facts_dict
    if 'virtual_facts' not in facts_dict:
        raise AssertionError("Failed: Unable to create facts_dict, key 'virtual_facts' not present")


# Generated at 2022-06-13 03:45:25.340112
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = Virtual('')

    # Test empty facts
    fact_virtual = FreeBSDVirtual(v)
    facts = fact_virtual.get_virtual_facts()
    assert not facts['virtualization_type']
    assert not facts['virtualization_role']
    assert not facts['virtualization_tech_host']
    assert not facts['virtualization_tech_guest']

    # Test kern.vm_guest=other
    v.add_fact('kern.vm_guest', 'other')
    fact_virtual = FreeBSDVirtual(v)
    facts = fact_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'other'
    assert facts['virtualization_role'] == 'guest'
    assert not facts['virtualization_tech_host']
    assert facts['virtualization_tech_guest']

# Generated at 2022-06-13 03:45:27.209387
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert c.platform == 'FreeBSD', \
            'Collector platform is not FreeBSD.'

# Generated at 2022-06-13 03:45:28.483279
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    assert facts.get_all()

# Generated at 2022-06-13 03:45:29.710013
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert {'virtualization_role', 'virtualization_type'}.issubset(virtual_facts)

# Generated at 2022-06-13 03:45:31.605114
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc._platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:32.392298
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector is not None

# Generated at 2022-06-13 03:45:42.261317
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import FakeVirtualFacts
    x = FreeBSDVirtual(FakeVirtualFacts())
    x.facts.update({
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
    })
    assert x.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(),
    }

# Generated at 2022-06-13 03:45:45.129705
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc is not None
    assert isinstance(vc, FreeBSDVirtualCollector)
    assert vc._platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:54.299409
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Unit test for method ``get_virtual_facts`` of class ``FreeBSDVirtual``"""
    # pylint: disable=protected-access
    target = FreeBSDVirtual()
    target._platform = 'FreeBSD'

# Generated at 2022-06-13 03:46:04.405595
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = dict()
    virtual_facts = FreeBSDVirtual(facts).get_virtual_facts()
    assert virtual_facts == dict()

    facts = dict()
    facts['kernel'] = 'FreeBSD'
    virtual_facts = FreeBSDVirtual(facts).get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:46:18.644386
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # GIVEN: No arguments
    # WHEN: FreeBSDVirtualCollector().collect() is called
    # THEN: The FreeBSDVirtual.platform must be 'FreeBSD' and
    #       the FreeBSDVirtual instance must be returned
    #       as a dictionary
    virtual_collector = FreeBSDVirtualCollector()
    result = virtual_collector.collect()
    assert result['virtual'].platform == 'FreeBSD'



# Generated at 2022-06-13 03:46:22.372683
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fact = FreeBSDVirtualCollector()
    assert fact._platform == 'FreeBSD',\
        'Platform value is not the expected platform'
    assert fact._fact_class == FreeBSDVirtual,\
        'The class value is not the expected class'

# Generated at 2022-06-13 03:46:30.208163
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = {}
    shared_utils = {}
    shared_utils['get_file_content'] = lambda x: ''
    shared_utils['get_mount_size'] = lambda x: (0, 0)
    shared_utils['get_file_lines'] = lambda x: []
    shared_utils['get_mount_info'] = lambda x: {'mountpoints': []}
    module = VirtualCollector()
    module.get_virtual_facts = FreeBSDVirtual(module, facts, shared_utils).get_virtual_facts
    assert module.get_virtual_facts() == dict(virtualization_role='',
                                              virtualization_type='',
                                              virtualization_tech_guest=set(),
                                              virtualization_tech_host=set())

# Generated at 2022-06-13 03:46:40.312134
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import sys
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.collector import BaseFileReadCollector

    class FreebsdVirtualWrapper(BaseFileReadCollector, VirtualSysctlDetectionMixin, FreeBSDVirtual):
        pass


# Generated at 2022-06-13 03:46:49.010662
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Declare a mock of class FreeBSDVirtual and set test conditions
    mock_false_sysctl_values = {
        'hw.model': '',
        'hw.hv_vendor': '',
        'kern.vm_guest': 'none',
        'security.jail.jailed': 0,
    }

    mock_xen_sysctl_values = {
        'hw.model': '',
        'hw.hv_vendor': '',
        'kern.vm_guest': 'none',
        'security.jail.jailed': 0,
    }


# Generated at 2022-06-13 03:46:51.229924
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v1 = FreeBSDVirtual()
    assert 'virtualization_type' in v1.get_virtual_facts()

# Generated at 2022-06-13 03:46:52.473055
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:47:01.664518
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """ Unit test for method get_virtual_facts of class FreeBSDVirtual.
        This test is based on the output of command 'sysctl -a'.
    """
    facts = {}

    # Set the facts to a FreeBSD virtual machine.
    facts['kernel'] = 'FreeBSD'
    facts['kernel_version'] = '9.1-RELEASE'
    facts['product_name'] = 'Virtual Machine'
    facts['product_version'] = '1.0-FreeBSD-amd64'
    facts['product_serial'] = ''
    facts['system'] = 'FreeBSD'

    # Set sysctl output.

# Generated at 2022-06-13 03:47:10.970950
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class MockFreeBSDVirtual(FreeBSDVirtual):
        """
        Mock class for FreeBSDVirtual
        """

        def detect_virt_product(self, sysctl_name):
            """
            Mock method for detect_virt_product of class FreeBSDVirtual
            """
            return {
                "sysctl_name": sysctl_name,
                'virtualization_type': sysctl_name,
                'virtualization_role': sysctl_name,
                'virtualization_tech': sysctl_name,
                'virtualization_tech_guest': set(),
                'virtualization_tech_host': set()
            }

        def detect_virt_vendor(self, dmidecode_product_name):
            """
            Mock method for detect_virt_vendor of class FreeBSDVirtual
            """

# Generated at 2022-06-13 03:47:17.576654
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = dict(os_family='FreeBSD', os='FreeBSD')
    # Create a new instance of FreeBSDVirtual
    virt = FreeBSDVirtual(facts)
    # Set the module_utils virtual facts collector
    virtual_facts = dict(virtual='FreeBSD')
    virt.module_utils_fact_collector(VirtualCollector,
                                     facts,
                                     virtual_facts,
                                     FreeBSDVirtualCollector)
    # Simulate the sysctl_values to be returned by sysctl_values
    # method of VirtualSysctlDetectionMixin
    # This simulates kern.vm_guest
    virt_product = dict(kern_vm_guest=dict(virtualization_type='none',
                                           virtualization_role='guest'))
    virt.detect_virt_product = lambda _: virt_product
    # This

# Generated at 2022-06-13 03:47:48.760639
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt = FreeBSDVirtual()

    # Set empty values as default
    virtual_facts = {'virtualization_type': '',
                     'virtualization_role': '',
                     'virtualization_tech_guest': set(),
                     'virtualization_tech_host': set()}

    # Case #1
    # sysctl
    # - kern.vm_guest - 'none'
    # - hw.hv_vendor - 'FreeBSD_HV'
    # - security.jail.jailed - '0'
    # hw.model - 'VMWare Virtual Platform'

    # mock sysctl data

# Generated at 2022-06-13 03:47:52.038141
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''
    Create an object of class FreeBSDVirtualCollector.
    '''
    class_inst = FreeBSDVirtualCollector()
    assert class_inst is not None

# Generated at 2022-06-13 03:47:54.914749
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector, FreeBSDVirtualCollector)
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:47:56.409251
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fact = FreeBSDVirtualCollector()
    assert fact.platform == 'FreeBSD'


# Generated at 2022-06-13 03:47:57.893330
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = dict()
    assert FreeBSDVirtualCollector(facts, {})._platform == 'FreeBSD'


# Generated at 2022-06-13 03:47:59.595871
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    import platform
    virtual_freebsd = FreeBSDVirtualCollector(platform)
    assert isinstance(virtual_freebsd, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:48:01.718783
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd = FreeBSDVirtual()
    virtual_facts = freebsd.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:48:02.631287
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:48:03.927141
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 03:48:15.165857
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    data = dict(
        virtualization_type='unknown'
    )
    result = dict(
        virtualization_type='',
        virtualization_role='',
        virtualization_tech_guest=set(),
        virtualization_tech_host=set(),
        virtualization_vendor='',
    )
    assert FreeBSDVirtual().get_virtual_facts() == result

    result['virtualization_role'] = 'guest'
    result['virtualization_type'] = 'xen'
    result['virtualization_tech_guest'] = set(['xen'])
    data['dev_xen_xenstore'] = '/dev/xen/xenstore'
    assert FreeBSDVirtual(data).get_virtual_facts() == result

    result['virtualization_role'] = 'host'

# Generated at 2022-06-13 03:49:22.785050
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """This test case checks if the FreeBSDVirtualCollector class could be initialized correctly."""
    assert(FreeBSDVirtualCollector is not None)

# Generated at 2022-06-13 03:49:24.312947
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert c._fact_class == FreeBSDVirtual
    assert c._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:25.099583
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.virtual() == FreeBSDVirtual

# Generated at 2022-06-13 03:49:26.660393
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual = FreeBSDVirtualCollector()
    assert isinstance(freebsd_virtual._fact_class, type)

# Generated at 2022-06-13 03:49:28.101214
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f.platform == 'FreeBSD'
    assert f._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:31.967138
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fbsdvirtual = FreeBSDVirtual()
    facts = fbsdvirtual.get_virtual_facts()

    assert type(facts['virtualization_type']) == str
    assert type(facts['virtualization_role']) == str
    assert type(facts['virtualization_technologies_guest']) == set
    assert type(facts['virtualization_technologies_host']) == set



# Generated at 2022-06-13 03:49:34.132471
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert fbc._fact_class == FreeBSDVirtual
    assert fbc._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:35.427502
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:49:42.320936
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''
    Test of method get_virtual_facts of class FreeBSDVirtual
    '''
    # Test 2 - Case:
    # - Swapping variables in sysctl_vals dict
    # - Swapping variables in hwmodel_vals dict
    # - Swapping variables in jail_vals dict
    # Expected Result:
    # - virtual_facts['virtualization_type'] = 'openvz'
    # - virtual_facts['virtualization_role'] = 'guest'
    collector = FreeBSDVirtualCollector()
    sysctl_vals2 = {
        'hw.hv_vendor': 'KVM',
        'security.jail.jailed': '0',
        'kern.vm_guest': 'other',
    }
    hwmodel_vals2 = ['OpenVZ']

# Generated at 2022-06-13 03:49:44.727636
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:53.004714
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    result = FreeBSDVirtualCollector()
    assert result._fact_class == FreeBSDVirtual
    assert result._platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:55.156901
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Unit test for the FreeBSDVirtual.get_virtual_facts() method
    """
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''

# Generated at 2022-06-13 03:51:05.533452
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    ansible_sysname = "FreeBSD"
    ansible_kernel = "FreeBSD"
    ansible_machine = "amd64"
    facts = dict()
    facts['kernel'] = ansible_kernel
    facts['machine'] = ansible_machine
    facts['sysname'] = ansible_sysname
    # If a virtualization_tech_host or virtualization_tech_guest key is in the
    # dictionary returned by get_virtual_facts, it should contain a set with
    # the following values:
    #     virtualization_tech_host:
    #         "jail"
    #     virtualization_tech_guest:
    #         "xen"
    #         "vbox"
    #         "jail"
    #
    # virtualization_type and virtualization_role keys should only be populated
   

# Generated at 2022-06-13 03:51:07.373445
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    col = FreeBSDVirtualCollector()
    assert col.platform == 'FreeBSD'
    assert col.fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:51:08.952094
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert hasattr(FreeBSDVirtualCollector, '_fact_class')
    assert hasattr(FreeBSDVirtualCollector, '_platform')



# Generated at 2022-06-13 03:51:14.262196
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    ''' Test FreeBSDVirtual.get_virtual_facts()
    '''
    fake_res = {
        'virtualization_tech_guest': set(),
        'virtualization_type': 'kvm',
        'virtualization_tech_host': set(),
        'virtualization_role': 'guest',
    }
    kern = {
        'kern.vm_guest': 'kvm',
        'hw.hv_vendor': 'bhyve',
    }
    freebsd_virtual = FreeBSDVirtual(None, kern, None)
    virtual_facts = freebsd_virtual.get_virtual_facts()
    assert virtual_facts == fake_res

    # Failover test

# Generated at 2022-06-13 03:51:14.761494
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:51:20.361028
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    test_virtual_facts = {'virtualization_type': 'xen',
                           'virtualization_role': 'guest',
                           'virtualization_tech_guest': set(['xen']),
                           'virtualization_tech_host': set([])
                           }
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual.collect()
    assert(freebsd_virtual.get_virtual_facts() == test_virtual_facts)

# Generated at 2022-06-13 03:51:21.867283
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:25.985820
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    detector = FreeBSDVirtual()

    # Generic testing
    facts = detector.get_virtual_facts()
    assert "virtualization_type" in facts
    assert "virtualization_role" in facts
    assert "virtualization_tech_guest" in facts
    assert "virtualization_tech_host" in facts

# Generated at 2022-06-13 03:53:45.468467
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsdvc = FreeBSDVirtualCollector()
    assert freebsdvc._fact_class == FreeBSDVirtual
    assert freebsdvc._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'