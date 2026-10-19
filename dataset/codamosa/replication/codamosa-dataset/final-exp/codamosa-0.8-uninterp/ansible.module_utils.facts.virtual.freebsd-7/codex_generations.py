

# Generated at 2022-06-13 03:43:59.075530
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    v.collect()

    assert v.data['virtualization_type'] == 'xen'
    assert v.data['virtualization_role'] == 'guest'
    assert 'xen' in v.data['virtualization_tech_guest']
    assert 'xen' not in v.data['virtualization_tech_host']
    assert 'bsd' not in v.data['virtualization_tech_guest']
    assert 'bsd' in v.data['virtualization_tech_host']

# Generated at 2022-06-13 03:44:01.132821
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.__name__ == 'FreeBSDVirtualCollector'
    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:09.872390
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Correct data:
    virtual = FreeBSDVirtual({})
    virtual._sysctl_data = {
        "hw.hv_vendor": "KVM",
        "kern.vm_guest": "other",
        "security.jail.jailed": "0",
    }
    virtual._vendor_data = {
        "hw.model": "OpenBSD",
    }
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == "other"
    assert virtual_facts['virtualization_role'] == ""

    # Virtualization is detected from kern.vm_guest (xen)
    virtual = FreeBSDVirtual({})

# Generated at 2022-06-13 03:44:14.159256
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Run constructor of the class
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    # Check if virtual_collector is of type FreeBSDVirtualCollector
    assert isinstance(freebsd_virtual_collector, FreeBSDVirtualCollector)
    # Check platform attribute of the class
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:24.113489
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()

    """
    Case 1: Standing on bare metal machine
    """
    v._sysctl_output = {
        'kern.vm_guest': 'other',
        'hw.model': 'Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz',
        'security.jail.jailed': 0
    }
    virtual_facts = v.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

    """
    Case 2: Standing on a FreeBSD jail
    """

# Generated at 2022-06-13 03:44:26.182058
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd = FreeBSDVirtual({})
    vf = freebsd.get_virtual_facts()


# Test for class FreeBSDVirtualCollector

# Generated at 2022-06-13 03:44:33.050356
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import mock
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual.detect_virt_product = mock.Mock(return_value='foo')
    freebsd_virtual.detect_virt_vendor = mock.Mock(return_value='bar')
    facts = freebsd_virtual.get_virtual_facts()
    assert facts['virtualization_type'] == 'foo'
    assert facts['virtualization_role'] == 'bar'
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:44:36.114088
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Prerequisities
    # check that _platform is defined correctly
    assert FreeBSDVirtualCollector._platform == "FreeBSD"
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:39.222469
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    Constructor of class FreeBSDVirtualCollector
    """
    assert(FreeBSDVirtualCollector._platform == 'FreeBSD')
    assert(FreeBSDVirtualCollector._fact_class == FreeBSDVirtual)

# Generated at 2022-06-13 03:44:44.830193
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    test_subject = FreeBSDVirtual()
    result = test_subject.get_virtual_facts()
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''
    assert result['virtualization_tech_guest'] == set()
    assert result['virtualization_tech_host'] == set()
    assert result['virtualization_product_guest'] == set()
    assert result['virtualization_product_host'] == set()

# Generated at 2022-06-13 03:44:50.651417
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_info = FreeBSDVirtualCollector()
    assert virtual_info is not None
    assert virtual_info._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:00.205673
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector


# Generated at 2022-06-13 03:45:07.790724
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSD_facts = FreeBSDVirtualCollector(None, None).collect()
    assert isinstance(FreeBSD_facts['virtualization_type'], str)
    assert isinstance(FreeBSD_facts['virtualization_role'], str)
    assert isinstance(FreeBSD_facts['virtualization_technologies'], set)
    assert isinstance(FreeBSD_facts['virtualization_technologies_host'], set)
    assert isinstance(FreeBSD_facts['virtualization_technologies_guest'], set)
    assert isinstance(FreeBSD_facts['virtualization_type_role'], str)

# Generated at 2022-06-13 03:45:11.284871
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    from ansible.module_utils.facts.virtual.base import Virtual

    _collector = FreeBSDVirtualCollector()
    assert isinstance(_collector, FreeBSDVirtualCollector)
    assert isinstance(_collector._fact_class, Virtual)

# Generated at 2022-06-13 03:45:17.515414
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fv = FreeBSDVirtual()
    mock = VirtualSysctlDetectionMixin()

    os.environ["ANSIBLE_KERNEL"] = "FreeBSD"
    os.environ["ANSIBLE_PRODUCT_NAME"] = "HVM domU"
    os.environ["ANSIBLE_VIRTUALIZATION_TYPE"] = "xen"
    os.environ["ANSIBLE_VIRTUALIZATION_ROLE"] = "guest"
    os.environ["ANSIBLE_VIRTUALIZATION_TECH_HOST"] = "xen"
    os.environ["ANSIBLE_VIRTUALIZATION_TECH_GUEST"] = "hvm"
    os.environ["ANSIBLE_HW_MODEL"] = "vNode"

    r = fv.get_virtual_facts()
    assert r

# Generated at 2022-06-13 03:45:19.301274
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:20.556218
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:22.779799
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    bvc = FreeBSDVirtualCollector()
    assert bvc is not None


# Generated at 2022-06-13 03:45:31.523498
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    sysctl_vendor_product = {'hw.hv_vendor': 'Microsoft',
                             'hw.model': 'VirtualBox',
                             'kern.vm_guest': 'other',
                             'security.jail.jailed': '1'}
    virtual_facts = FreeBSDVirtual(sysctl_vendor_product).get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmware'
    assert 'virtualbox' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_tech_guest'] == virtual_facts['virtualization_tech_host']
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'jail' in virtual_facts['virtualization_tech_guest']

# Generated at 2022-06-13 03:45:38.279802
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:45:51.865368
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    test_object = FreeBSDVirtual({}, None)

    test_object.module = MockAnsibleModule()
    test_object.module.exit_json = lambda x: None

    # normal case, host is physical BSD
    test_object.module.get_bin_path = lambda x: '/bin/sysctl'
    test_object.module.run_command = MockBSDModule.run_command
    test_object.module.run_command.return_value = (0, "security.jail.jailed: 0", "")
    test_facts = test_object.get_virtual_facts()
    assert test_facts['virtualization_type'] == ''
    assert test_facts['virtualization_role'] == ''

    # normal case, host is virtualized BSD
    test_object.module.run_command = MockBSDModule.run

# Generated at 2022-06-13 03:45:53.084479
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert hasattr(vc, 'platform')

# Generated at 2022-06-13 03:45:54.984100
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x._fact_class == FreeBSDVirtual
    assert x._platform == 'FreeBSD'


# Generated at 2022-06-13 03:45:55.837085
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:45:58.388972
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fvc = FreeBSDVirtualCollector()
    assert fvc.platform == "FreeBSD"
    assert fvc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:01.286833
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.platform == 'FreeBSD'
    assert collector._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:04.400799
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:46:06.368450
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv_obj = FreeBSDVirtualCollector()
    # Test that the fact_class variable is set to FreeBSDVirtual class
    assert fv_obj.fact_class

# Generated at 2022-06-13 03:46:10.467907
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Set up test vars
    kern_vm_guest = {'kern.vm_guest': 'user',
                     'virtualization_tech_guest': set(['user']),
                     'virtualization_tech_host': set()}
    hw_hv_vendor = {'hw.hv_vendor': 'unknown',
                    'virtualization_tech_guest': set(),
                    'virtualization_tech_host': set()}
    sec_jail_jailed = {'security.jail.jailed': '0',
                       'virtualization_tech_guest': set(),
                       'virtualization_tech_host': set()}

# Generated at 2022-06-13 03:46:13.033508
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert f._platform == 'FreeBSD'
    assert f._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:46:24.381111
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({})
    virtual_facts = facts.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

    assert virtual_facts['virtualization_tech_guest'] is not None
    assert virtual_facts['virtualization_tech_host'] is not None

# Generated at 2022-06-13 03:46:32.548743
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Init variables
    FreeBSDVirtual_get_virtual_facts_output = {'virtualization_type': '', 'virtualization_tech_guest': set(), 'virtualization_tech_host': set(), 'virtualization_role': ''}

    # Test with: virtualization_type = None, virtualization_tech_guest = None, virtualization_tech_host = None, virtualization_role = None
    FreeBSDVirtual_get_virtual_facts_input = {'virtualization_type': None, 'virtualization_tech_guest': None, 'virtualization_tech_host': None, 'virtualization_role': None}
    obj = FreeBSDVirtual(FreeBSDVirtual_get_virtual_facts_input)
    obj.get_virtual_facts()
    assert obj.virtual_facts == FreeBSDVirtual_get_virtual_facts_output

    # Test with: virtual

# Generated at 2022-06-13 03:46:43.980321
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    cache = dict()
    facts = dict()
    F = VirtualCollector(cache, facts, False)._fact_class(cache, facts, False)
    virtual_facts = F.get_virtual_facts()
    assert type(virtual_facts['virtualization_type']) == str
    assert type(virtual_facts['virtualization_role']) == str
    assert type(virtual_facts['virtualization_tech_guest']) == set
    assert type(virtual_facts['virtualization_tech_host']) == set
    # SYSCTL sysctl detections
    assert (virtual_facts['virtualization_type'] == 'xen'
            or virtual_facts['virtualization_type'] == '')

# Generated at 2022-06-13 03:46:56.371918
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fbsd_virtual_facts = FreeBSDVirtual(module=None, collected_facts=None)
    kvm_data = {'hw.hv_vendor': ' KVMKVMKVM', 'kern.vm_guest': 'kvm',
                'security.jail.jailed': '0'}
    virtualbox_data = {'hw.hv_vendor': ' VirtualBox',
                       'hw.model': ' VirtualBox',
                       'kern.vm_guest': 'user', 'security.jail.jailed': '0'}
    vbox_data = {'hw.hv_vendor': 'VBoxVBoxVBox',
                 'hw.model': 'VirtualBox',
                 'kern.vm_guest': 'user', 'security.jail.jailed': '0'}
   

# Generated at 2022-06-13 03:46:58.008974
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector._fact_class is FreeBSDVirtual
    assert collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:59.405675
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector is not None

# Generated at 2022-06-13 03:47:04.078404
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Unit test of get_virtual_facts for FreeBSDVirtual"""

    # Set Virtual.platform to FreeBSD
    Virtual.platform = 'FreeBSD'

    virtual = FreeBSDVirtual()

    # Initialize virtual_facts to empty dictionary
    virtual_facts = {}

    # Call get_virtual_facts method to populate virtual_facts
    virtual_facts = virtual.get_virtual_facts()

    # Verify virtual_facts is not empty
    assert virtual_facts, 'virtual_facts is empty'

# Generated at 2022-06-13 03:47:04.633477
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    return {}

# Generated at 2022-06-13 03:47:09.496201
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    x = FreeBSDVirtual()
    res = x.get_virtual_facts()
    assert res.get('virtualization_type') == 'kvm'
    assert res.get('virtualization_role') == 'guest'
    assert res.get('virtualization_tech_guest') == set(['kvm'])
    assert res.get('virtualization_tech_host') == set(['qemu'])

# Generated at 2022-06-13 03:47:11.419035
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    ctor = FreeBSDVirtualCollector()
    assert ctor.platform == 'FreeBSD'
    assert ctor._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:21.250744
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert issubclass(FreeBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 03:47:22.184406
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    result = FreeBSDVirtualCollector()
    assert result.platform == 'FreeBSD'


# Generated at 2022-06-13 03:47:32.506554
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from argparse import Namespace
    from importlib import import_module
    kern_vm_guest = {
        'virtualization_tech_host': set(),
        'virtualization_type': 'kvm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(['kvm']),
    }
    hw_hv_vendor = {
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(),
    }

# Generated at 2022-06-13 03:47:36.893105
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    obj_FreeBSDVirtual = FreeBSDVirtual({})
    obj_FreeBSDVirtual.get_virtual_facts()
    obj_FreeBSDVirtual.facts == \
        {
            'virtualization_type': '',
            'virtualization_role': '',
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set(),
        }
    del obj_FreeBSDVirtual

# Generated at 2022-06-13 03:47:37.311122
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:40.587634
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Constructor of FreeBSDVirtualCollector does not have any argument.
    # Use arbitrary argument for test
    test_var = BDSVirtualCollector('foo')
    assert isinstance(test_var, VirtualCollector)
    assert test_var.platform == 'FreeBSD'
    assert test_var.fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:47:50.041231
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts_values = {
        'virtualization_type': '',
        'virtualization_role': ''
    }
    virtual_facts_keys_expected = virtual_facts_values.keys()
    virtual_facts_keys_got = set()

    get_virtual_facts_result = FreeBSDVirtual().get_virtual_facts()
    assert isinstance(get_virtual_facts_result, dict)

    virtual_facts_keys_got = set(get_virtual_facts_result.keys())
    assert virtual_facts_keys_expected == virtual_facts_keys_got

    for key in virtual_facts_values:
        assert get_virtual_facts_result[key] == virtual_facts_values[key]

# Generated at 2022-06-13 03:47:59.303417
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    return_val = dict(
        virtualization_tech_host={'virtualization_tech_host'},
        virtualization_tech_guest={'virtualization_tech_guest'},
        virtualization_role='guest',
        virtualization_type='xen'
    )
    virtual_obj = FreeBSDVirtual()

    class dummy_sysctl(object):
        def detect_virt_product(self, key):
            return dict(
                virtualization_tech_host={'virtualization_tech_host'},
                virtualization_tech_guest={'virtualization_tech_guest'},
                virtualization_role='guest',
                virtualization_type='xen'
            )


# Generated at 2022-06-13 03:48:05.151302
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Create instance of FreeBSDVirtual
    freebsd_virtual_instance = FreeBSDVirtual()

    # Create structure to store current sysctl values
    sysctl_values = {}

    # Check that the 'kern.vm_guest' sysctl key is not present
    sysctl_values['kern.vm_guest'] = ''

    # Check that the 'hw.hv_vendor' sysctl key is not present
    sysctl_values['hw.hv_vendor'] = ''

    # Check that the 'security.jail.jailed' sysctl key is not present
    sysctl_values['security.jail.jailed'] = ''

    # Return the current sysctl values
    def get_sysctl_values(sysctl_keys):
        sysctl_values_copy = sysctl_values.copy()
        # Return sysctl

# Generated at 2022-06-13 03:48:07.868680
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:48:35.577277
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:38.090717
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector._fact_class == FreeBSDVirtual, 'Class for virtual collector should be FreeBSDVirtual'
    assert collector._platform == 'FreeBSD', 'Platform for virtual collector should be FreeBSD'

# Generated at 2022-06-13 03:48:40.085362
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_dict = dict()
    freebsd_virtual_collector = FreeBSDVirtualCollector(facts_dict)
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:40.491213
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:41.955545
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    facts = v.get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts

# Generated at 2022-06-13 03:48:52.598418
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # We need to mock sysctl results here
    class MockCommandResult:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def __getattr__(self, attr):
            try:
                return self.kwargs[attr]
            except KeyError:
                return ''

    kern_vm_guest = MockCommandResult(rc=0, stdout='0\n', stderr='')
    hw_hv_vendor = MockCommandResult(rc=0, stdout='QEMU', stderr='')
    sec_jail_jailed = MockCommandResult(rc=0, stdout='0\n', stderr='')
    hw_model = MockCommandResult(rc=0, stdout='QEMU', stderr='')

# Generated at 2022-06-13 03:48:56.198411
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:48:58.287054
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == "FreeBSD"
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:06.283846
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:49:09.487086
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert fbc.platform == 'FreeBSD'
    assert fbc.virt_what_platform == 'FreeBSD'
    assert fbc.sysctl_platform == 'FreeBSD'

# Generated at 2022-06-13 03:50:15.684262
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv.platform == 'FreeBSD'
    assert fv.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:17.145418
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'



# Generated at 2022-06-13 03:50:19.804938
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    vm = FreeBSDVirtual()
    facts = vm.get_virtual_facts()

    assert(facts['virtualization_type'] in ['', 'xen'])
    assert(facts['virtualization_role'] in ['', 'guest'])

# Generated at 2022-06-13 03:50:20.441374
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:50:24.050188
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    assert len(facts) == 5
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_technologies_guest' in facts
    assert 'virtualization_technologies_host' in facts
    assert 'virtualization_vendor' in facts

# Generated at 2022-06-13 03:50:26.918118
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Check that get_virtual_facts returns a dict
    fbsdvirt = FreeBSDVirtual()
    assert isinstance(fbsdvirt.get_virtual_facts(), dict)

# Generated at 2022-06-13 03:50:29.661006
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual()
    assert freebsd_virtual.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
    }

# Generated at 2022-06-13 03:50:31.427493
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:50:39.330955
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import sys
    import subprocess
    # Prevent execution of get_virtual_facts method
    # In case of exception method should return empty dictionary
    Virtual.get_virtual_facts = lambda self: {}
    # Create virtual_facts dictionary to compare with result
    virtual_facts = {'virtualization_type': 'xen', 'virtualization_role': 'guest'}
    # Create object of class FreeBSDVirtual
    freebsd_virtual = FreeBSDVirtual()
    # Initialize subprocess module to emulate sysctl command execution
    subprocess.Popen = lambda x, **kwargs: x
    sys.stdout.readline = lambda: 'hw.hv_vendor: FreeBSD'
    # Create result dictionary
    result = freebsd_virtual.get_virtual_facts()
    # Compare result with virtual_facts dictionary
    # Check virtualization_role

# Generated at 2022-06-13 03:50:42.365584
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    # Compare the collector with itself
    assert FreeBSDVirtualCollector == FreeBSDVirtualCollector

# Generated at 2022-06-13 03:51:49.815271
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    result = FreeBSDVirtualCollector()
    assert result._platform == 'FreeBSD'
    assert result._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:51:53.236954
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert(fv)
    assert(fv._fact_class == FreeBSDVirtual)
    assert(fv._platform == 'FreeBSD')

# Unit tests for methods in class FreeBSDVirtual

# Generated at 2022-06-13 03:51:55.523105
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Create the FreeBSDVirtualCollector object
    facts_collector = FreeBSDVirtualCollector()

    # Check if it is an instance of VirtualCollector
    assert isinstance(facts_collector, VirtualCollector)

    # Check the platform
    assert facts_collector._platform == 'FreeBSD'

    # Check the fact class
    assert facts_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:56.129591
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:52:03.021377
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Test 1:
    # FreeBSD 10.0-RELEASE, see https://wiki.freebsd.org/Virtualization
    # The uname output of this machine is
    # FreeBSD freebsd10.freebsdhost.cz 10.0-RELEASE FreeBSD 10.0-RELEASE #0 r260789: Tue Jan 21 10:59:35 UTC 2014     root@snap.freebsd.org:/usr/obj/usr/src/sys/GENERIC  amd64
    # It is xen host but it can be recognized by sysctl only as a jail.

    info_dir = os.path.dirname(os.path.abspath(__file__))
    xenstore_file = os.path.join(info_dir, 'freebsd10_xenstore')

# Generated at 2022-06-13 03:52:03.749678
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x._platform == 'FreeBSD'

# Generated at 2022-06-13 03:52:08.560305
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create a FreeBSDVirtual object
    fbsd_virtual = FreeBSDVirtual()

    # Create a fake device
    class FakeDevice(object):
        def __init__(self, virtualization_type, virtualization_role,
                     virtualization_tech_guest, virtualization_tech_host):
            self.virtualization_type = virtualization_type
            self.virtualization_role = virtualization_role
            self.virtualization_tech_guest = virtualization_tech_guest
            self.virtualization_tech_host = virtualization_tech_host

        def read_file(self, path):
            if path.startswith('/dev/xen/'):
                # A Xen guest
                return self.virtualization_type

# Generated at 2022-06-13 03:52:09.212872
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:52:10.676716
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_facts_collector = FreeBSDVirtualCollector()
    assert freebsd_facts_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:52:14.852993
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual(None).get_virtual_facts()
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''