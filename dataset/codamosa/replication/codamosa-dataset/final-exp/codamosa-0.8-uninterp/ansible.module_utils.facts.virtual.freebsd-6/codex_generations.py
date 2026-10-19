

# Generated at 2022-06-13 03:43:55.559985
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual({})
    virtual.get_virtual_facts()


if __name__ == '__main__':
    test_FreeBSDVirtual_get_virtual_facts()

# Generated at 2022-06-13 03:43:58.750455
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """Test class constructor for FreeBSDVirtualCollector
    """
    FreeBSD_virtual_collector = FreeBSDVirtualCollector()
    assert FreeBSD_virtual_collector._platform == 'FreeBSD'
    assert FreeBSD_virtual_collector._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:43:59.376298
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:44:00.643272
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector(None, None)
    assert f is not None


# Generated at 2022-06-13 03:44:03.603009
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtualCollector().get_virtual_facts()
    # We have to have at least some facts
    assert facts['virtualization_type']
    assert facts['virtualization_role']
    assert facts['virtualization_type'] in facts['virtualization_tech_host']
    assert facts['virtualization_role'] in facts['virtualization_tech_guest']

# Generated at 2022-06-13 03:44:05.278634
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x._fact_class == FreeBSDVirtual
    assert x._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:10.200918
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert isinstance(x, FreeBSDVirtualCollector)
    assert isinstance(x._fact_class, FreeBSDVirtual)
    assert hasattr(x, '_platform')
    assert x._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:18.651588
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():  # pylint: disable=invalid-name
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    facts_collector = collector.get_collector('FreeBSDVirtualCollector', module)

    res = facts_collector._collect_platform_facts()
    assert res['virtualization_type'] == ''
    assert res['virtualization_role'] == ''
    assert res['virtualization_technologies_host'] == set()
    assert res['virtualization_technologies_guest'] == set()

# Generated at 2022-06-13 03:44:22.164318
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:44:22.715438
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector is not None

# Generated at 2022-06-13 03:44:28.083069
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtualCollector.collect()
    assert 'virtualization_type' in facts

# Generated at 2022-06-13 03:44:35.472507
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    #
    # Unit test for method get_virtual_facts of class FreeBSDVirtual
    # This test covers the case for being in a jailed environment.
    #

    mock_module = type('module', (object,), dict(params={'gather_subset': '!all'}))()
    mock_module.get_bin_path = lambda x: 'echo'

    mock_run_output = [
    'security.jail.jailed: 1'
    ]

    def mock_run_command(a, b):
        return (0, '\n'.join(mock_run_output), '')

    import sys
    if sys.version_info[0] < 3:
        builtin_module = '__builtin__'
    else:
        builtin_module = 'builtins'


# Generated at 2022-06-13 03:44:37.448008
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    platforms = ['FreeBSD']
    for platform in platforms:
        result = Virtual(platform)
        assert result.platform == platform

# Generated at 2022-06-13 03:44:42.145227
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fbsd_virtualization_facts = {'virtualization_type': 'jail', 'virtualization_role': 'guest', 'virtualization_tech_guest': {'jail'}, 'virtualization_tech_host': set()}
    assert fbsd_virtualization_facts == FreeBSDVirtual(None).get_virtual_facts()

# Generated at 2022-06-13 03:44:44.574505
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:45.370901
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd = FreeBSDVirtualCollector()
    assert hasattr(freebsd, '_fact_class')

# Generated at 2022-06-13 03:44:47.699820
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:58.881622
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create a class if we're not being run in a module
    class Module:
        def fail_json(self, msg):
            raise Exception(msg)

    # Create a class with some stub methods for testing purposes
    class TestFreeBSDVirtual(FreeBSDVirtual):
        def __init__(self, module):
            self.module = module

        def detect_virt_product(self, mib):
            return {
                'virtualization_type': 'kvm',
                'virtualization_role': 'guest',
                'virtualization_tech_guest': set(['kvm']),
                'virtualization_tech_host': set(['kvm']),
            }


# Generated at 2022-06-13 03:45:00.318025
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:09.792459
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fake_module = _create_fake_module()
    facts_collector = FreeBSDVirtual(fake_module)

    facts_collector.get_virtual_facts()

    assert fake_module.exit_json.call_count == 1
    args = fake_module.exit_json.call_args[0]
    assert args[0]['ansible_facts']['virtualization_type'] == 'VendorB'
    assert args[0]['ansible_facts']['virtualization_role'] == 'guest'
    assert args[0]['ansible_facts']['virtualization_tech_guest'] == set(['VendorB'])
    assert args[0]['ansible_facts']['virtualization_tech_host'] == set(['VendorB'])



# Generated at 2022-06-13 03:45:23.933549
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible_collections.ansible.community.tests.unit.module_utils.facts.virtual.test_linux_virtual import (
        TestLinuxVirtual, MockHardware, MockSysctl)

    # hypervisor xen, guest
    virtual = FreeBSDVirtual(MockHardware, MockSysctl(virtualization={
        'kern.vm_guest': 'Xen',
        'hw.hv_vendor': 'HVM domU',
        'hw.model': 'Xen HVM domU'
    }))
    virtual_facts = virtual.get_virtual_facts()

# Generated at 2022-06-13 03:45:27.324099
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    """
    This method is called via pytest test framework.
    """
    # The first parameter is the class name of the fact module
    # The second parameter is the name of this test
    facts_obj = FreeBSDVirtualCollector()
    assert isinstance(facts_obj, FreeBSDVirtualCollector)
    assert facts_obj._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:28.945696
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import doctest
    doctest.testmod(FreeBSDVirtual)
    doctest.testmod(FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:45:34.144519
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual.collect()
    # The test is only valid on FreeBSD.
    if virtual.facts['system'] == 'FreeBSD':
        assert virtual.facts['virtualization_role'] == virtual.facts['ansible_virtualization_role']
        assert virtual.facts['virtualization_type'] == virtual.facts['ansible_virtualization_type']
        assert virtual.facts['virtualization_role'] != ''
        assert virtual.facts['virtualization_type'] != ''

# Generated at 2022-06-13 03:45:35.444427
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
  virtual = FreeBSDVirtual()
  assert virtual.get_virtual_facts()['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:45:47.030193
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

    # Create instance of FreeBSDVirtual
    frbsd_virtual = FreeBSDVirtual()
    assert isinstance(frbsd_virtual, FreeBSDVirtual)

    # Test detect_virt_product method
    frbsd_virtual.detect_virt_product = lambda sysctl: {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

    # Test detect_virt_vendor method

# Generated at 2022-06-13 03:45:48.960049
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv._fact_class == FreeBSDVirtual
    assert fv._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:55.805843
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    mock_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'unit', 'module_utils', 'facts', 'virtual', 'fixtures', 'freebsd.yml')
    mock_data = {'ansible_facts': {'virtual_facts': {}}}
    with open(mock_data_path, 'rb') as f:
        mock_data['ansible_facts']['virtual_facts'] = yaml.safe_load(f)
    bsd_virtual = FreeBSDVirtual()
    assert bsd_virtual.get_virtual_facts() == mock_data['ansible_facts']['virtual_facts']

# Generated at 2022-06-13 03:46:07.067945
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    import platform
    import os

    class kern_vm_guest_mock(object):
        @staticmethod
        def _get_value(key):
            if key == 'kern.vm_guest':
                return 'other'
            raise AttributeError

    class hw_hv_vendor_mock(object):
        @staticmethod
        def _get_value(key):
            if key == 'hw.hv_vendor':
                return 'Other'
            raise AttributeError

    class sec_jail_jailed_mock(object):
        @staticmethod
        def _get_value(key):
            if key == 'security.jail.jailed':
                return '0'
            raise AttributeError


# Generated at 2022-06-13 03:46:15.973025
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Test normal behavior of FreeBSDVirtual.get_virtual_facts
    test_facts = {}
    test_facts.update({'virtualization_type': '',
                       'virtualization_role': '',
                       'virtualization_tech_guest': [],
                       'virtualization_tech_host': []})
    # all paths will lead to get_virtual_facts()
    # initializing with virtual_facts and returning it.
    expected_facts = test_facts
    test_instance = FreeBSDVirtual(test_facts)
    test_facts = test_instance.get_virtual_facts()
    assert test_facts == expected_facts

# Generated at 2022-06-13 03:46:31.878778
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils import basic
    import json


# Generated at 2022-06-13 03:46:34.410099
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts_obj = FreeBSDVirtualCollector()
    assert facts_obj._platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:35.483855
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'

# Generated at 2022-06-13 03:46:39.519502
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtual('/usr/bin/freebsd-version', '/sbin/sysctl')
    assert fv.has_command_available('/usr/bin/freebsd-version')
    assert fv.has_command_available('/sbin/sysctl')

# Generated at 2022-06-13 03:46:48.401834
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # pylint: disable=protected-access
    # No kernel technology detected
    kern_vm_guest = {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }
    # No hardware technology detected
    hw_hv_vendor = {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }
    # No jail technology detected
    sec_jail_jailed = {
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set()
    }
    # No virtualization detected

# Generated at 2022-06-13 03:46:52.729543
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Unit test for the function get_virtual_facts of class FreeBSDVirtual
    """
    freebsd_virtual = FreeBSDVirtual()
    # If no virtualization is detected, then we expect the keys
    # 'virtualization_role' and 'virtualization_type' in result to be ''
    assert freebsd_virtual.get_virtual_facts()['virtualization_role'] == ''
    assert freebsd_virtual.get_virtual_facts()['virtualization_type'] == ''



# Generated at 2022-06-13 03:46:59.209852
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    test_virtual_facts = {
        'virtualization_technologies_guest' : { 'xen' },
        'virtualization_technologies_host' : set(),
        'virtualization_type' : 'xen',
        'virtualization_role' : 'guest',
        'virtualization_type_full' : 'xen',
    }
    virtual = FreeBSDVirtual(None, None)
    test_virtual_facts_result = virtual.get_virtual_facts()

    assert test_virtual_facts == test_virtual_facts_result

# Generated at 2022-06-13 03:47:00.126422
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:02.475975
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_collector = FreeBSDVirtualCollector()
    assert freebsd_collector._fact_class is FreeBSDVirtual
    assert freebsd_collector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:47:07.503106
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector

    c_ins = get_collector_instance(FreeBSDVirtualCollector)
    assert c_ins.platform == 'FreeBSD'
    assert isinstance(c_ins.collector, FreeBSDVirtualCollector)
    assert c_ins.guest_virtual_facts == {}

# Generated at 2022-06-13 03:47:28.138116
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    f = FreeBSDVirtual()
    assert f.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_technologies_guest': set(),
        'virtualization_technologies_host': set(),
    }

# Generated at 2022-06-13 03:47:35.985612
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:47:37.735121
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj._platform == 'FreeBSD'
    assert obj._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:47:38.630451
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert isinstance(f, FreeBSDVirtualCollector)

# Generated at 2022-06-13 03:47:44.734175
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    class mock_path_exists(object):
        def __init__(self, path):
            self.path = path
            self.path_exists_return = False
            self.call_count = 0

        def __call__(self, path=None):
            self.call_count += 1
            if self.path is not None and path is not None and path == self.path:
                return self.path_exists_return
            return False

    class mock_detect_virt_product(object):
        def __init__(self, value):
            self.value = value
            self.call_count = 0

        def __call__(self, value=None):
            self.call_count += 1

# Generated at 2022-06-13 03:47:55.458707
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Mock sysctl
    mock_sysctl_output = '''
kern.vm_guest: other
hw.hv_vendor: VMware, Inc.
security.jail.jailed: 0
'''

    mock_sysctl = {
        'kern.vm_guest': 'other',
        'hw.hv_vendor': 'VMware, Inc.',
        'security.jail.jailed': '0'
    }

    # Mock get_file_content
    import sys
    import builtins
    if sys.version_info.major < 3:
        builtin_open = '__builtin__.open'
    else:
        builtin_open = 'builtins.open'


# Generated at 2022-06-13 03:48:02.883232
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:48:14.339180
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts_output = {
      'virtualization_type': '',
      'virtualization_role': '',
      'virtualization_tech_guest': {'jail'},
      'virtualization_tech_host': set()
    }
    virtual_facts = FreeBSDVirtual()
    virtual_facts.get_platform_specific_facts = lambda: {
      'hw.model': 'FreeBSD/amd64 (foo) (bar)',
      'kern.vm_guest': 'other',
      'security.jail.jailed': 1,
      'hw.hv_vendor': '12345'
    }
    virtual_facts.get_virtual_facts() == virtual_facts_output
    virtual_facts.get_virtual_facts()['virtualization_type'] == 'jail'
    virtual_facts.get

# Generated at 2022-06-13 03:48:21.554214
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virt = FreeBSDVirtual()
    virt.detect_virt_product = lambda sysctl: {'virtualization_tech_guest': ['xen'],
                                               'virtualization_tech_host': ['xen']}
    virt.detect_virt_vendor = lambda sysctl: {'virtualization_tech_guest': ['xen'],
                                              'virtualization_tech_host': ['xen']}
    virt.sysctl_is_jail = lambda: False
    virtual_facts = virt.get_virtual_facts()
    assert virtual_facts['virtualization_type'] is 'xen'
    assert virtual_facts['virtualization_role'] is 'guest'
    assert virtual_facts['virtualization_tech_guest'] == set(['xen'])

# Generated at 2022-06-13 03:48:23.191904
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.facts is not None
    assert obj.fact_subclass is not None
    assert obj.platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:26.498426
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    fv = FreeBSDVirtual(module=None)

    virtual_fact = fv.get_virtual_facts()

    assert virtual_fact['virtualization_type'] == ''
    assert virtual_fact['virtualization_role'] == ''
    assert virtual_fact['virtualization_tech_host'] == set()
    assert virtual_fact['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 03:49:33.554456
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    fv = FreeBSDVirtual(False)

    # Set base expected results
    virtual_facts = {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    guest_tech = virtual_facts['virtualization_tech_guest']
    host_tech = virtual_facts['virtualization_tech_host']

    # Not running on FreeBSD
    if fv.distribution.name != 'FreeBSD':
        virtual_facts['virtualization_type'] = 'host'
        host_tech.add('host')
        assert fv.get_virtual_facts() == virtual_facts

    # Running on FreeBSD
    if fv.distribution.name == 'FreeBSD':
        # Not virtualised
        virtual

# Generated at 2022-06-13 03:49:34.186179
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector._fact_class is FreeBSDVirtual

# Generated at 2022-06-13 03:49:41.320042
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Test :class:`ansible.module_utils.facts.virtual.FreeBSDVirtual`
    :method get_virtual_facts()
    """
    # host OS: FreeBSD 12.1 (not jailed)
    # hardware: Intel(R) Core(TM) i3-4130 CPU @ 3.40GHz
    # virtualization: KVM, QEMU, VirtualBox, VMWare, Xen (not running)
    fbsd_virtual = FreeBSDVirtual({}, {})
    fbsd_virtual_facts = fbsd_virtual.get_virtual_facts()
    facts_keys = tuple(fbsd_virtual_facts.keys())
    assert facts_keys == ('virtualization_tech_guest', 'virtualization_tech_host', 'virtualization_type', 'virtualization_role')
    virtualization_tech_guest

# Generated at 2022-06-13 03:49:43.709190
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert isinstance(FreeBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 03:49:44.203717
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:49:45.806516
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert True, "Instantiated FreeBSDVirtualCollector()"


# Generated at 2022-06-13 03:49:48.962880
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv.platform == 'FreeBSD'
    assert fv._platform == 'FreeBSD'
    assert fv._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:49:51.478234
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc._fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:49:53.629117
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'
    assert FreeBSDVirtualCollector.fact_class == FreeBSDVirtual
    assert FreeBSDVirtualCollector.fact_class.platform == 'FreeBSD'

# Generated at 2022-06-13 03:51:06.975763
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector.platform == 'FreeBSD'
    assert virtual_collector.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:13.058821
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    FreeBSDVirtualFacts = FreeBSDVirtual()
    virtual_facts = FreeBSDVirtualFacts.get_virtual_facts()

    # Check isinstance of virtual_facts
    assert isinstance(virtual_facts, dict)

    # Check virtualization_tech_guest/host keys
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

    # Check virtualization_tech_guest/host is set
    assert virtual_facts['virtualization_tech_guest'] is not None
    assert virtual_facts['virtualization_tech_host'] is not None

    # Check all keys
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_system' in virtual_facts
    assert 'virtualization_product_name'

# Generated at 2022-06-13 03:51:15.977372
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(virtual_collector, FreeBSDVirtualCollector)
    assert virtual_collector._platform == 'FreeBSD'
    assert virtual_collector._fact_class == FreeBSDVirtual

# Unit test fot method FreeBSDVirtualCollector.collect()

# Generated at 2022-06-13 03:51:17.964934
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
    c = FreeBSDVirtualCollector()
    assert type(c) == FreeBSDVirtualCollector

# Generated at 2022-06-13 03:51:20.673362
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import FreeBSDVirtual

    obj = FreeBSDVirtual()
    facts = obj.get_virtual_facts()

    assert(facts['virtualization_type'] == '')
    assert(facts['virtualization_role'] == '')

# Generated at 2022-06-13 03:51:24.284695
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc.fact_class.platform == 'FreeBSD'
    assert vc.fact_class.__name__ == 'FreeBSDVirtual'

# Generated at 2022-06-13 03:51:29.686938
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    mock_facts = {
        'ansible_facts': {
            'ansible_system': 'FreeBSD',
            'ansible_distribution': 'FreeBSD',
            'ansible_distribution_version': '10.3-RELEASE',
            'ansible_distribution_release': 'RELEASE',
            'ansible_architecture': 'amd64',
            'ansible_virtualization_role': 'guest',
            'ansible_virtualization_type': 'xen',
            'ansible_virtualization_technologies': ['xen'],
        },
        'changed': True,
    }
    class_instance = FreeBSDVirtual()
    assert mock_facts == class_instance.get_virtual_facts()

# Generated at 2022-06-13 03:51:34.676902
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    '''
    Unit test for method get_virtual_facts of class FreeBSDVirtual
    '''
    test_class = FreeBSDVirtual()
    test_facts = test_class.get_virtual_facts()

    # Every item of virtual_facts should be in test_facts
    for key, val in test_facts.items():
        assert key in test_facts
        assert test_facts[key] == val

# Generated at 2022-06-13 03:51:44.275721
# Unit test for method get_virtual_facts of class FreeBSDVirtual

# Generated at 2022-06-13 03:51:47.043461
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''Test FreeBSDVirtualCollector constructor'''
    obj = FreeBSDVirtualCollector()
    assert obj.platform == 'FreeBSD'
    assert obj.fact_class is FreeBSDVirtual
# End of unit test for constructor of class FreeBSDVirtualCollector