

# Generated at 2022-06-13 03:43:50.689990
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector._fact_class.platform == 'FreeBSD'


# Generated at 2022-06-13 03:43:54.364495
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    my_collector = FreeBSDVirtualCollector()
    assert my_collector._platform == 'FreeBSD'
    assert my_collector._fact_class.__name__ == 'FreeBSDVirtual'

# Generated at 2022-06-13 03:44:00.710204
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class MockSysctl:
        @staticmethod
        def read_sysctl_entry(a):
            return "1"

    sysctl_mock = MockSysctl()
    facts = FreeBSDVirtual(sysctl_mock).get_virtual_facts()
    assert facts['virtualization_tech_host'] == {'container'}
    assert facts['virtualization_tech_guest'] == {'jail', 'container'}
    assert facts['virtualization_type'] == 'jail'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:44:02.148105
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:03.738977
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert not FreeBSDVirtualCollector() is None

# Generated at 2022-06-13 03:44:11.396070
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Unit test for method get_virtual_facts of the class FreeBSDVirtual

    # Configure the variables
    module_name = 'ansible.module_utils.facts.virtual.freebsd'
    detect_sysctl_values = module_name + '.VirtualSysctlDetectionMixin.detect_sysctl'
    detect_hw_model_values = module_name + '.VirtualSysctlDetectionMixin.detect_hw_model'

    kern_vm_guest = {'virtualization_type': 'xen', 'virtualization_role': 'guest'}
    hw_hv_vendor = {'virtualization_type': '', 'virtualization_role': ''}
    sec_jail_jailed = {'virtualization_type': '', 'virtualization_role': ''}

# Generated at 2022-06-13 03:44:21.050001
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import freebsd

    freebsd.sysctl = lambda x: (0, 'no such sysctl')
    freebsd.read_file = lambda x: (0, '')

    fbsd_virtual_ins = freebsd.FreeBSDVirtual(module=None)
    virtual_facts = fbsd_virtual_ins.get_virtual_facts()
    assert virtual_facts == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

    # Test Xen guest
    open('/dev/xen/xenstore', 'a').close()
    virtual_facts = fbsd_virtual_ins.get_virtual_facts()


# Generated at 2022-06-13 03:44:28.637086
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    with open('/proc/cpuinfo', 'r') as f:
        cpuinfo = f.read()

    # cpuinfo does not contain virtualization info.
    with open('/proc/self/status', 'r') as f:
        status = f.read()

    # status does not contain virtualization info.
    with open('/proc/1/cmdline', 'r') as f:
        cmdline = f.read()

    # cmdline does not contain virtualization info.
    with open('/proc/1/mountinfo', 'r') as f:
        mountinfo = f.read()

    # mountinfo does not contain virtualization info.

    # sysfs does not contain virtualization info.

    # dmesg does not contain virtualization info.
    with open('/dev/null', 'w') as f:
        dmes

# Generated at 2022-06-13 03:44:32.357373
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fb_virtual_facts = FreeBSDVirtual({})
    assert fb_virtual_facts.get_virtual_facts() == {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}


# Generated at 2022-06-13 03:44:43.137037
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create a test FreeBSDVirtual object
    fbs = FreeBSDVirtual()
    facts = fbs.get_virtual_facts()

    # Assert that virtualization_tech_guest is a set and is as expected
    assert isinstance(facts['virtualization_tech_guest'], set)
    assert 'freebsd' in facts['virtualization_tech_guest']
    assert 'jail' in facts['virtualization_tech_guest']

    # Assert that virtualization_tech_host is a set and is empty
    assert isinstance(facts['virtualization_tech_host'], set)
    assert facts['virtualization_tech_host'] == set()

    # Assert that virtualization_type is 'xen', as expected
    assert facts['virtualization_type'] == 'xen'

    # Assert that virtualization_role is

# Generated at 2022-06-13 03:44:48.754505
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    assert isinstance(virtual_facts, dict)

# Generated at 2022-06-13 03:44:56.024380
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] in ['', 'xen', 'vmware', 'kvm', 'virtualbox', 'jail', 'hyperv', 'openvz', 'vserver', 'vbox', 'venet', 'uml', 'lxc', 'systemd-nspawn']
    assert virtual_facts['virtualization_role'] in ['', 'guest']

# Generated at 2022-06-13 03:45:07.532856
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual_facts = FreeBSDVirtual({})
    freebsd_virtual_facts._sysctl_cmd = '/sbin/sysctl'
    freebsd_virtual_facts._lsdev_cmd = '/usr/bin/lsdev'
    freebsd_virtual_facts._sysctl_path = 'tests/unit/module_utils/facts/virtual/sysctl'
    freebsd_virtual_facts._lsdev_path = 'tests/unit/module_utils/facts/virtual/lsdev'

    # Known results from outputs of lsdev and sysctl on FreeBSD 8.3

# Generated at 2022-06-13 03:45:13.946217
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    expected_virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': ['jail'],
        'virtualization_tech_host': ['xen_dom0', 'vbox', 'kvm', 'virtualbox']}
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts == expected_virtual_facts

# Generated at 2022-06-13 03:45:17.693087
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fbsd_collector = FreeBSDVirtualCollector()
    fbsd_virtual = fbsd_collector.collect(None, None)
    facts = fbsd_virtual.get_virtual_facts()
    print(facts)

# Generated at 2022-06-13 03:45:26.631974
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    class SystemMock:

        def __init__(self, name, version):
            self.name = name
            self.version = version

    class FileMock:
        @staticmethod
        def exists(path):
            if path == '/dev/xen/xenstore':
                return True
            if path == '/dev/vmm/fbsd.vmm':
                return True
            if path == '/dev/vboxdrv':
                return True
            return False


# Generated at 2022-06-13 03:45:35.249522
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Setup FreeBSDVirtual instance for testing get_virtual_facts method
    test_instance = FreeBSDVirtual()

    # Setup testdata
    virtual_sysctl_data = {
        'sysctl': {
            'kern.vm_guest': 'user',
            'hw.hv_vendor': 'bhyve',
            'security.jail.jailed': 1,
        },
    }

    hw_model_data = {
        'hw.model': 'VirtualBox',
    }

    expected_result = {
        'virtualization_type': 'vbox',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['vbox', 'jail']),
        'virtualization_tech_host': set(['vbox']),
    }

    # Patch VirtualSysctl

# Generated at 2022-06-13 03:45:39.041972
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual = FreeBSDVirtualCollector()
    assert freebsd_virtual._platform == 'FreeBSD'
    assert freebsd_virtual._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:41.089437
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert isinstance(virtual_facts, dict)

# Generated at 2022-06-13 03:45:50.293399
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts_dict = FreeBSDVirtual().get_virtual_facts()
    assert sorted(virtual_facts_dict.keys()) == sorted(['virtualization_type', 'virtualization_role',
                                                        'virtualization_tech_guest', 'virtualization_tech_host'])
    assert virtual_facts_dict['virtualization_role'] in ['guest', 'host']
    assert virtual_facts_dict['virtualization_type'] in ['xen', 'docker', 'jail', 'VMWare ESXi', 'KVM', 'Bhyve', '']
    assert isinstance(virtual_facts_dict['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts_dict['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:45:57.837054
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()

    assert type(virtual_facts) == dict
    assert type(virtual_facts['virtualization_type']) == str
    assert virtual_facts['virtualization_type'] in [ '', 'xen', 'vbox', 'vmware', 'parallels' ]
    assert type(virtual_facts['virtualization_role']) == str
    assert virtual_facts['virtualization_role'] in [ '', 'guest', 'host' ]

# Generated at 2022-06-13 03:46:00.970634
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:05.606599
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    ''' Unit test of constructor of class FreeBSDVirtualCollector. '''
    my_obj = FreeBSDVirtualCollector()
    my_facts = my_obj.collect()

    assert 'virtualization_type' in my_facts
    assert 'virtualization_role' in my_facts

    assert my_obj._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:06.170141
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:46:07.489789
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    p = FreeBSDVirtualCollector()
    assert repr(p) == \
        '<ansible.module_utils.facts.virtual.freebsd.FreeBSDVirtualCollector object at 0x%x>' % id(p)

# Generated at 2022-06-13 03:46:18.411694
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from mock import patch

    # Values that would be returned by detect_virt_product('kern.vm_guest')
    kern_vm_guest = {'virtualization_type': 'virtualbox',
                     'virtualization_role': 'guest',
                     'virtualization_tech': set(['vmware', 'xen', 'kvm'])}
    # Values that would be returned by detect_virt_vendor('hw.model')
    hw_model = {'virtualization_type': 'parallels',
                'virtualization_role': 'guest',
                'virtualization_tech': set(['vmware', 'xen', 'kvm'])}
    # Values that would be returned by detect_virt_product('security.jail.jailed')

# Generated at 2022-06-13 03:46:22.516625
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    c = FreeBSDVirtual()
    assert c.get_virtual_facts() == {'virtualization_type': '',
                                     'virtualization_role': '',
                                     'virtualization_tech_guest': set(),
                                     'virtualization_tech_host': set()}

# Generated at 2022-06-13 03:46:28.283698
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    obj = Virtual('')
    obj.sysctl = {'kern.vm_guest': 'none',
                  'hw.hv_vendor': 'None',
                  'security.jail.jailed': '0',
                  'hw.model': 'Vendor product'}
    result = obj.get_virtual_facts()
    assert result == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 03:46:28.986116
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector

# Generated at 2022-06-13 03:46:29.650155
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc is not None

# Generated at 2022-06-13 03:46:47.630701
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # These are a temporary place to put the test results
    # until the get_virtual_facts is re-written to be more
    # flexible and the unit test framework is re-written
    expected_virtual_facts = {
        'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set([])
    }

    # A class instance
    bsd_virtual = FreeBSDVirtual()

    # Results from the get_virtual_facts method
    virtual_facts = bsd_virtual.get_virtual_facts()

    # Assert for the equalty of the test results and expected results

# Generated at 2022-06-13 03:46:57.924619
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import sys
    if sys.version_info[0] == 3:
        import unittest.mock as mock
    else:
        import mock

    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual

    mock_retval = {
        'hw.hv_vendor': 'bhyve',
        'hw.model': 'QEMU Virtual CPU version 2.5+',
        'kern.vm_guest': 'bhyve',
        'security.jail.jailed': '0'
    }

    mock_get_sysctl_values = mock.Mock(return_value=mock_retval)
    m = FreeBSDVirtual()
    m.get_sysctl_values = mock_get_sysctl_values


# Generated at 2022-06-13 03:46:58.540938
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector

# Generated at 2022-06-13 03:46:59.625094
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # When
    fvc = FreeBSDVirtualCollector()
    # Then
    assert fvc._platform == 'FreeBSD'
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:06.143790
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    test_object = FreeBSDVirtual()

    # FreeBSD 7.x, 8.x
    set_module_args({'sysctl': dict(kern_vm_guest={'value': 'other', 'present': False})})
    result = test_object.get_virtual_facts()
    assert 'virtualization_type' in result
    assert result['virtualization_type'] == 'other'
    assert result['virtualization_role'] == 'host'

    # FreeBSD 10.x, 11.x
    set_module_args({'sysctl': dict(kern_vm_guest={'value': 'vmware', 'present': True})})
    result = test_object.get_virtual_facts()
    assert 'virtualization_type' in result
    assert result['virtualization_type'] == 'vmware'

# Generated at 2022-06-13 03:47:14.451227
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create a named temporary file
    with open("/tmp/out", "w") as temp_file:
        # Define a fake content
        content = """
kern.vm_guest: none
security.jail.jailed: 0
hw.hv_vendor: ""
hw.model: 'Intel(R) Core(TM) i5-6600K CPU @ 3.50GHz'
"""
        # Write the content
        temp_file.write(content)
    # Call the method get_virtual_facts of class FreeBSDVirtual
    facts = FreeBSDVirtual().get_virtual_facts()
    # Assert the returned facts
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 03:47:16.269473
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt_facts = FreeBSDVirtual({'ansible_system': 'FreeBSD'}).get_virtual_facts()
    assert virt_facts['virtualization_type'] == ''
    assert virt_facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:47:18.068575
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    assert FreeBSDVirtual.get_virtual_facts(None) == dict(
        virtualization_type=u'',
        virtualization_role=u''
    )

# Generated at 2022-06-13 03:47:23.459409
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    ''' Unit test for constructor of class FreeBSDVirtualCollector '''
    # VirtualCollector is abstract class and doesn't have implementation
    # of __init__() and get_virtual_facts() functions.
    from sys import version_info
    if version_info[0] == 2:
        import __builtin__ as builtins
    else:
        import builtins
    builtins.__ansible_module_utils_facts_virtual_freebsd = __import__('ansible.module_utils.facts.virtual.freebsd')
    fvc = FreeBSDVirtualCollector()
    assert fvc is not None

# Generated at 2022-06-13 03:47:29.985721
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # We cannot test this class easily.  This method is only called if
    # we run on a FreeBSD host, and is not covered by a unittest inside
    # the facts directory.  We need to test it here, since we want to
    # make sure that a recent change did not break this class.
    collector = FreeBSDVirtualCollector()
    facts = collector.collect(None, None)
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts

# Generated at 2022-06-13 03:47:59.850683
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class FreeBSDVirtual'''
    testobj = FreeBSDVirtual()
    result_virt_facts = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
    }
    testobj.facts['kernel'] = 'FreeBSD'
    testobj.facts['product_name'] = 'VirtualBox'
    testobj.facts['product_version'] = '1.2'


# Generated at 2022-06-13 03:48:03.164691
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform is 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class is FreeBSDVirtual
    assert isinstance(FreeBSDVirtualCollector()._fact_class(), FreeBSDVirtual)

# Generated at 2022-06-13 03:48:12.406997
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create a FreeBSDVirtual object
    freebsd_virtual = FreeBSDVirtual()
    # Set the virtual_facts that we expect in the test
    freebsd_virtual_facts = {'virtualization_role': 'guest',
                             'virtualization_type': 'xen',
                             'virtualization_tech_guest': set(['xen']),
                             'virtualization_tech_host': set([])}
    # Check that the output of get_virtual_facts contains the expected
    # virtual_facts
    assert freebsd_virtual.get_virtual_facts() == freebsd_virtual_facts

# Generated at 2022-06-13 03:48:15.001685
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fv = FreeBSDVirtual()
    facts = fv.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:48:16.260715
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x._platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:24.698964
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    data = {}
    data['virtual_facts'] = {}
    data['sysctl'] = {}
    data['sysctl']['kern.vm_guest'] = {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
    data['sysctl']['hw.hv_vendor'] = {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
    data['sysctl']['security.jail.jailed'] = {'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}
    data['files'] = {}

# Generated at 2022-06-13 03:48:27.055523
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    result = FreeBSDVirtual().get_virtual_facts()
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''

# Generated at 2022-06-13 03:48:29.111570
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector()
    assert c.platform == 'FreeBSD'
    assert c._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:48:31.359775
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x._fact_class.__name__ == 'FreeBSDVirtual'


# Generated at 2022-06-13 03:48:33.508503
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Test without any arguments
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:49:40.611333
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    _fact_class = FreeBSDVirtual
    _platform = 'FreeBSD'
    f = FreeBSDVirtualCollector(_fact_class, _platform)
    assert isinstance(f, FreeBSDVirtualCollector)
    assert f.platform == 'FreeBSD'

# Unit tests for FreeBSDVirtual

# Generated at 2022-06-13 03:49:41.857784
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    assert 'virtualization_type' in facts

# Generated at 2022-06-13 03:49:43.787954
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc._platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:53.586697
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:49:55.171071
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:57.130200
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(freebsd_virtual_collector, VirtualCollector)



# Generated at 2022-06-13 03:49:58.392182
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    inst = FreeBSDVirtualCollector()
    assert inst.platform == 'FreeBSD'
    assert inst._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:04.996603
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    module = type('', (object,), {
        'params': {},
    })


# Generated at 2022-06-13 03:50:06.575906
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    v = FreeBSDVirtualCollector()
    assert v.platform == 'FreeBSD'
    assert v._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:16.675624
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()

    virtual._module.params = {}

    # Detect no virtualization
    virtual._module.boolean = lambda x: False
    virtual.get_virtual_facts()
    assert not virtual.facts['virtualization_type']
    # assert not virtual.facts['virtualization_role']
    # TODO: why doesn't this condition hold?

    # Detect VMWare ESXi host
    virtual._module.boolean = lambda x: True
    virtual.get_virtual_facts()
    assert virtual.facts['virtualization_type'] == 'vmware'
    assert virtual.facts['virtualization_role'] == 'host'
    assert 'vmware' in virtual.facts['virtualization_tech_guest']
    assert 'vmware' in virtual.facts['virtualization_tech_host']

    # Detect QEMU guest


# Generated at 2022-06-13 03:51:35.197733
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Setup
    from ansible.module_utils._text import to_bytes
    b_platform_paths = {
        'kern.vm_guest': '/kern.vm_guest',
        'hw.model': '/hw.model',
        'security.jail.jailed': '/security.jail.jailed',
    }
    virtual_facts = dict()
    virtual_facts['virtualization_type'] = ''
    virtual_facts['virtualization_role'] = ''
    virtual_facts['virtualization_tech_guest'] = set()
    virtual_facts['virtualization_tech_host'] = set()

    # Test 1:
    # No sysctl keys
    # Expected result:
    # virtualization_type = ''
    # virtualization_role = ''

# Generated at 2022-06-13 03:51:40.389547
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # On FreeBSD, facts should report no virtualization as default
    expected_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
    }

    freebsd_virtual = FreeBSDVirtual()
    actual_facts = freebsd_virtual.get_virtual_facts()

    assert expected_facts == actual_facts


# Generated at 2022-06-13 03:51:43.356517
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt_facts = {}
    v = FreeBSDVirtual()
    virt_facts = v.get_virtual_facts()
    assert virt_facts['virtualization_type'] != ''
    assert virt_facts['virtualization_role'] != ''

# Generated at 2022-06-13 03:51:44.503935
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == "FreeBSD"

# Generated at 2022-06-13 03:51:53.072806
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    from ansible.module_utils.facts.virtual.hv_vendor import VirtualVendorDetectionMixin
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    # Initialise BSDVirtual object with mocked attributes
    fv = FreeBSDVirtual()
    fv.collect_sysctl_values = (lambda arg: arg)
    fv.detect_virt_product = (lambda arg1, arg2=False: arg1)
    fv.detect_virt_vendor = (lambda arg1, arg2=False: arg1)
    # Invoke get_virtual_facts method of BSDVirtual
    fv_virtual_facts = fv.get_virtual_facts()

# Generated at 2022-06-13 03:52:01.210786
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:52:03.607525
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_facts_collector = FreeBSDVirtualCollector()
    assert isinstance(freebsd_facts_collector, VirtualCollector)

# Generated at 2022-06-13 03:52:06.004120
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc is not None
    assert fvc.platform == 'FreeBSD'
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:52:07.457478
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:52:13.987337
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts_dict = {'virtualization_type': 'virtualbox',
                          'virtualization_role': 'guest',
                          'virtualization_tech_guest': set(['vbox']),
                          'virtualization_tech_host': set(['virtualbox'])}

    virtual_facts_dict_1 = {'virtualization_type': '',
                            'virtualization_role': '',
                            'virtualization_tech_guest': set(['unknown']),
                            'virtualization_tech_host': set(['unknown'])}
