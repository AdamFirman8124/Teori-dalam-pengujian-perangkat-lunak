

# Generated at 2022-06-13 03:44:00.711388
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = {'virtualization_type': '', 'virtualization_role': ''}
    virt = FreeBSDVirtual()
    collected_facts = {'ansible_facts': {'virtualization': virtual_facts}}
    test_facts = {'ansible_facts': {'virtualization': {'virtualization_type': 'Desktop', 'virtualization_role': 'host'}}}
    # Empty facts
    assert virt.get_virtual_facts()['ansible_facts']['virtualization'] == test_facts['ansible_facts']['virtualization']
    # Facts with virtualization_type and virtualization_role
    facts = {'ansible_facts': {'virtualization': {'virtualization_type': 'xen', 'virtualization_role': 'guest'}}}

# Generated at 2022-06-13 03:44:03.876700
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector.platform is 'FreeBSD'
    assert freebsd_virtual_collector.fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:44:06.459730
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts = FreeBSDVirtualCollector()
    assert virtual_facts._platform == 'FreeBSD'
    assert virtual_facts._fact_class.__name__ == 'FreeBSDVirtual'


# Generated at 2022-06-13 03:44:07.604843
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd = FreeBSDVirtual()
    freebsd.get_virtual_facts()

# Generated at 2022-06-13 03:44:13.182990
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector._fact_class, FreeBSDVirtual), \
        "virtual_collector._fact_class is not instance of FreeBSDVirtual"
    assert virtual_collector._platform == 'FreeBSD', \
        "virtual_collector._platform is not 'FreeBSD'"


# Generated at 2022-06-13 03:44:14.410268
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class FreeBSDVirtual'''
    module = FreeBSDVirtual()
    module.get_virtual_facts()

# Generated at 2022-06-13 03:44:24.511382
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual({'ansible_facts': {'kernel': 'FreeBSD'}})

    virtual_facts = virtual.get_virtual_facts()
    assert type(virtual_facts) == dict
    assert virtual_facts['virtualization_type']
    assert virtual_facts['virtualization_type'] == 'xen' or virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role']
    assert virtual_facts['virtualization_role'] == 'guest' or virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest']
    assert type(virtual_facts['virtualization_tech_guest']) == set

# Generated at 2022-06-13 03:44:33.178072
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = {}
    virtual = FreeBSDVirtual(module=None)
    virtual_facts = virtual.get_virtual_facts()
    facts.update(virtual_facts=virtual_facts)
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

    # Fake hw.model
    virtual._hw_model = 'QEMU Virtual CPU version 2.5+'
    virtual_facts = virtual.get_virtual_facts()
    facts.update(virtual_facts=virtual_facts)
    assert virtual_facts['virtualization_type'] == 'kvm'
    assert 'kvm' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:44:38.725940
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    test_virtual = FreeBSDVirtual()
    test_virtual_facts = test_virtual.get_virtual_facts()

    assert 'virtualization_role' in test_virtual_facts
    assert 'virtualization_type' in test_virtual_facts
    assert 'virtualization_tech_guest' in test_virtual_facts
    assert 'virtualization_tech_host' in test_virtual_facts

# Generated at 2022-06-13 03:44:40.949658
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''Unit test for constructor of class FreeBSDVirtualCollector'''

    bsd_virtual = FreeBSDVirtualCollector()
    assert bsd_virtual

# Generated at 2022-06-13 03:44:51.621239
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_collector = FreeBSDVirtualCollector()
    assert facts_collector._platform == 'FreeBSD'
    assert facts_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:00.366967
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:45:03.078489
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    VFC = FreeBSDVirtualCollector()
    assert VFC._fact_class == FreeBSDVirtual
    assert VFC._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:13.707780
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:45:15.671389
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector._platform == 'FreeBSD'
    assert collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:45:25.484662
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    This is a FreeBSD-specific subclass of Virtual.  It defines
    - virtualization_type
    - virtualization_role
    """
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

    class FakeFreeBSDVirtual(FreeBSDVirtual, VirtualSysctlDetectionMixin):
        """
        This is a Fake class of FreeBSDVirtual. It was made to test the get_virtual_facts method
        """
        platform = 'FreeBSD'

        def __init__(self):
            self.virtual_facts = dict()


# Generated at 2022-06-13 03:45:28.440029
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsdC = FreeBSDVirtualCollector()
    assert freebsdC.platform == 'FreeBSD'
    assert freebsdC._fact_class.platform == 'FreeBSD'


# Generated at 2022-06-13 03:45:29.798555
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector(None, None, None)._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:37.260680
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Test behavior with a true value
    collector = FreeBSDVirtualCollector(True)
    assert collector._platform == 'FreeBSD'
    assert isinstance(collector._fact_class, FreeBSDVirtual)
    assert collector._fact_class.platform == 'FreeBSD'

    # Test behavior with a false value
    collector = FreeBSDVirtualCollector(False)
    assert collector._platform == 'FreeBSD'
    assert isinstance(collector._fact_class, FreeBSDVirtual)
    assert collector._fact_class.platform == 'FreeBSD'

    # Test behavior with a 1 value
    collector = FreeBSDVirtualCollector(1)
    assert collector._platform == 'FreeBSD'
    assert isinstance(collector._fact_class, FreeBSDVirtual)
    assert collector._fact_class.platform == 'FreeBSD'

    # Test behavior with a 0 value
    collector = FreeBSD

# Generated at 2022-06-13 03:45:40.811395
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:06.916333
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    facts = v.get_virtual_facts()
    assert isinstance(facts, dict)
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert isinstance(facts['virtualization_tech_guest'], set)
    assert isinstance(facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 03:46:08.489653
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:46:11.715150
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt = FreeBSDVirtual()
    facts = virt.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''

# Generated at 2022-06-13 03:46:16.199303
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from sys import platform as _platform
    from ansible.module_utils.facts.virtual.bsd import FreeBSDVirtualCollector
    # there is no FreeBSD on non-BSD platforms,
    # so FreeBSDVirtualCollector should not be available

    if _platform != 'freebsd8':
        assert FreeBSDVirtualCollector == None

# Generated at 2022-06-13 03:46:18.189517
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:46:27.523822
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_detector = FreeBSDVirtualCollector.factory()
    # Test for jail
    jail_sysctl = {'security.jail.jailed': '1'}
    jail_model = {'hw.model': 'Xeon E5420'}

    assert virtual_detector.get_virtual_facts('jail', 'sysctl', jail_sysctl, jail_model) == {
        'virtualization_role': 'guest',
        'virtualization_type': 'jail',
        'virtualization_tech_host': set(['jail']),
        'virtualization_tech_guest': set(['jail'])
    }

    # Test for Xen
    xen_sysctl = {'security.jail.jailed': '0', 'kern.vm_guest': 'xen'}
    xen_

# Generated at 2022-06-13 03:46:34.803729
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = VIRTUAL_TO_SYSCTL['vm_guest']['freebsd']
    x = VIRTUAL_TO_SYSCTL['hv_vendor']['freebsd']
    y = VIRTUAL_TO_SYSCTL['jail_jailed']['freebsd']
    z = VIRTUAL_TO_VENDOR['freebsd']
    t = 'FreeBSD'

    # Set empty values as default
    virtual_facts = {'virtualization_type' : '',
                     'virtualization_role' : ''}

    virtual = FreeBSDVirtual({'kernel' : 'freebsd'})

    # Test if virtual_facts is changed

# Generated at 2022-06-13 03:46:37.664028
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts


# Generated at 2022-06-13 03:46:40.022747
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''Unit test for constructor of class FreeBSDVirtualCollector'''
    c = FreeBSDVirtualCollector()
    assert c._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:42.355233
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():

    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:09.939229
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    facts = FreeBSDVirtual(module).get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'



# Generated at 2022-06-13 03:47:16.946921
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''FreeBSDVirtual.get_virtual_facts()'''
    ansible_module = module_mock()
    fbsd_virtual = FreeBSDVirtual(ansible_module)
    res = fbsd_virtual.get_virtual_facts()

    # expected is a dict of dict.
    # Each dict is sorted by key.
    expected = dict()

    # Do not validate the field virtual_facts['virtualization_tech_guest'] and
    # virtual_facts['virtualization_tech_host'].
    # It should be tested as a unit test of its own.
    for k in res.keys():
        if k in ['virtualization_tech_guest', 'virtualization_tech_host']:
            continue

        expected[k] = dict()
        if not isinstance(res[k], dict):
            expected[k]

# Generated at 2022-06-13 03:47:23.956130
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Test with a system that is a FreeBSD VM running under Xen
    collect_mock = {
        'uname_s': 'FreeBSD',
        'uname_r': '12.0-RELEASE',
        '/dev/xen/xenstore': True,
        'sysctl_kern_vm_guest': 'xen',
        'sysctl_hw_hv_vendor': 'Xen',
        'sysctl_security_jail_jailed': '0',
        'hw_model': 'FreeBSD/amd64 on Xen HVM'
    }


# Generated at 2022-06-13 03:47:26.621739
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv.platform == 'FreeBSD'
    assert fv._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:28.938405
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    backend = FreeBSDVirtualCollector(None, None, None)
    assert isinstance(backend.facts, FreeBSDVirtual)

# Generated at 2022-06-13 03:47:34.272713
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsdvirtual_instance = FreeBSDVirtual()
    freebsdvirtual_instance.detect_virt_sysctl = lambda x: 'somevalue'
    freebsd_get_virtual_facts = freebsdvirtual_instance.get_virtual_facts()
    import pdb;pdb.set_trace()
    assert freebsd_get_virtual_facts == {'virtualization_type': '', 'virtualization_role': '', 'virtualization_technologies': [], 'virtualization_product': 'somevalue'}

# Generated at 2022-06-13 03:47:35.593214
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector._fact_class == FreeBSDVirtual
    assert collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:38.490251
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    _freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(_freebsd_virtual_collector._fact_class, FreeBSDVirtual)
    assert _freebsd_virtual_collector._platform == 'FreeBSD'


# Generated at 2022-06-13 03:47:39.531933
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:47:41.764754
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv.__class__ == FreeBSDVirtualCollector
    assert fv.platform() == 'FreeBSD'


if __name__ == '__main__':
    test_FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:36.512301
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual(None).get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:48:39.130925
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Verify all variables are initialized
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:48:44.989044
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fake_module = type('module', (object,), {'params': {}})
    fact_class = FreeBSDVirtual(fake_module)

    test_virt_product_results = {
        'kern_vm_guest': {
            'virtualization_tech_guest': ['kvm'],
            'virtualization_tech_host': ['kvm']
        },
        'hw_hv_vendor': {
            'virtualization_tech_guest': [],
            'virtualization_tech_host': []
        },
        'sec_jail_jailed': {
            'virtualization_tech_guest': [],
            'virtualization_tech_host': []
        }
    }


# Generated at 2022-06-13 03:48:56.007860
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    This is a unit test for method get_virtual_facts of class FreeBSDVirtual
    """


# Generated at 2022-06-13 03:49:01.436094
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual([])
    virtual_facts = virtual.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_host'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_product_host'] == ''
    assert virtual_facts['virtualization_product_guest'] == ''

# Generated at 2022-06-13 03:49:08.552486
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    base_facts = {
        'kernel': 'FreeBSD'
    }

    fake_sysctl_values = {
        'kern.vm_guest': '',
        'hw.hv_vendor': '',
        'security.jail.jailed': '',
        'hw.model': ''
    }

    expected_virtual_facts = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': set(['xen']),
        'virtualization_tech_host': set()
    }

    # The required condition to run get_virtual_facts is to
    # have '/dev/xen/xenstore' on the host
    # Mocking the base_module, os module and the FakeDict object
    # that contains

# Generated at 2022-06-13 03:49:10.801639
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Verify __init__() returns object of class FreeBSDVirtualCollector
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)


# Generated at 2022-06-13 03:49:13.004128
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    instance = FreeBSDVirtualCollector()
    assert isinstance(instance.get_virtual_facts(), dict)


# Generated at 2022-06-13 03:49:13.947584
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    myClass = FreeBSDVirtualCollector()
    assert isinstance(myClass, object)

# Generated at 2022-06-13 03:49:14.401655
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:51:33.390898
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:37.234098
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_facts_collector = FreeBSDVirtualCollector()
    assert virtual_facts_collector.platform == 'FreeBSD'
    assert virtual_facts_collector._fact_class == FreeBSDVirtual
    assert virtual_facts_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:51:38.965903
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsdvirtual = FreeBSDVirtualCollector()
    assert freebsdvirtual._platform == 'FreeBSD'

# Generated at 2022-06-13 03:51:42.787434
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts_module = FreeBSDVirtual()
    virtual_facts = virtual_facts_module.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 03:51:50.815005
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts of class FreeBSDVirtual"""

    # Prepare test input
    class Testclass:
        """
        This is a test class for testing FreeBSDVirtual.get_virtual_facts()

        The class simulates the BSD object interface to the sysctl
        system call by using the following dictionaries:

        sysctl_dict has one dummy output per sysctl variable:
        {sysctl variable name: (sysctl variable data type, sysctl variable value)}

        sysctl_vendor_dict has one dummy output per hw.<attribute> sysctl variable:
        {hw.<attribute>: <hw.<attribute> value>}

        """

        def __init__(self, sysctl_dict, sysctl_vendor_dict):

            self.sysctl_dict = sysctl_dict
            self.sysctl_vendor_dict = sys

# Generated at 2022-06-13 03:51:59.810126
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import sys
    import os

    fake_sysctl_pipe = os.path.join(os.path.dirname(__file__), 'sysctl.out')
    fake_xen_pipe = os.path.join(os.path.dirname(__file__), 'xen.out')
    fake_model_pipe = os.path.join(os.path.dirname(__file__), 'model.out')

    open_fds = []
    old_within_container = sys.platform.startswith("linux")

# Generated at 2022-06-13 03:52:10.401745
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:52:19.782598
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():  # pylint: disable=invalid-name
    host_facts = FreeBSDVirtual({})
    guest_facts = FreeBSDVirtual({})
    jail_facts = FreeBSDVirtual({})
    baremetal_facts = FreeBSDVirtual({})

    # Test host facts
    xennet_exists = os.path.exists('/dev/xen/xenstore')

    host_facts_expected = {
        'virtualization_type': 'xen' if xennet_exists else 'kvm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(['kvm', 'xen'])
    }
    host_facts_actual = host_facts.get_virtual_facts()

    for key in host_facts_expected:
        assert host_

# Generated at 2022-06-13 03:52:22.234789
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector
    assert issubclass(freebsd_virtual_collector._fact_class, Virtual)

# Generated at 2022-06-13 03:52:24.440132
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
  assert FreeBSDVirtualCollector._platform == 'FreeBSD'
  assert FreeBSDVirtual == FreeBSDVirtualCollector._fact_class
  assert isinstance(FreeBSDVirtualCollector._fact_class(), FreeBSDVirtual)

