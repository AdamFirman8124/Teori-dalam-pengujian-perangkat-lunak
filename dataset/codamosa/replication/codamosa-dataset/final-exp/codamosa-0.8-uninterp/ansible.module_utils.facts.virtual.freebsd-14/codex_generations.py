

# Generated at 2022-06-13 03:44:01.943058
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    f_virtual = FreeBSDVirtual()

    ####
    # Empty case
    ####
    f_virtual.file_exists_mock = lambda x: False
    f_virtual.get_sysctl_mock = lambda x: None
    f_virtual.get_file_content_mock = lambda x: None
    virtual_facts = f_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

    ####
    # Only xen
    ####
    f_virtual.file_exists_mock = lambda x: x == '/dev/xen/xenstore'
   

# Generated at 2022-06-13 03:44:04.987797
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual()
    result = v.get_virtual_facts()
    assert result['virtualization_type'] == ''
    assert result['virtualization_role'] == ''

# Generated at 2022-06-13 03:44:11.998456
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = dict()
    with open(os.path.join(os.path.dirname(__file__), '../unit/fixtures/virtual/FreeBSD/sysctl.txt')) as fp:
        data = fp.read()
        virtual = FreeBSDVirtual(module=None, config=dict())
        virtual._detect_freebsd_sysctl(data, facts)
    assert set(facts['virtualization_tech_guest']) == set(['xen', 'bhyve', 'jail'])
    assert set(facts['virtualization_tech_host']) == set(['xen', 'bhyve', 'jail'])
    assert facts['virtualization_type'] == 'jail'
    assert facts['virtualization_role'] == 'guest'


# Generated at 2022-06-13 03:44:21.632034
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    class MockSysctl(object):
        def __init__(self, sysctl_return_value):
            self.sysctl_return_value = sysctl_return_value

        def __call__(self, value):
            return self.sysctl_return_value

    class MockProcFS(object):
        def __init__(self, procfs_return_value):
            self.procfs_return_value = procfs_return_value

        def __call__(self, value):
            return self.procfs_return_value

    def mock_detect_virt_product(*args, **kwargs):
        return {
            'virtualization_type': '',
            'virtualization_role': '',
            'virtualization_tech_guest': set(),
            'virtualization_tech_host': set()
        }



# Generated at 2022-06-13 03:44:22.814922
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # Run the constructor
    bsd_virt = FreeBSDVirtualCollector()

    assert bsd_virt._fact_class is FreeBSDVirtual
    assert bsd_virt._platform == 'FreeBSD'

# Generated at 2022-06-13 03:44:26.589725
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():

    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert isinstance(freebsd_virtual_collector, VirtualCollector)

if __name__ == '__main__':
    test_FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:44:30.997903
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    results = dict(
        virtual=FreeBSDVirtual(dict(), dict()).get_virtual_facts()
    )
    assert results == {'virtual': {'virtualization_role': '', 'virtualization_type': '',
                                   'virtualization_tech_guest': set(), 'virtualization_tech_host': set()}}

# Generated at 2022-06-13 03:44:33.055695
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    freebsd_virtual_collector = FreeBSDVirtualCollector()
    assert freebsd_virtual_collector.platform == 'FreeBSD'


# Generated at 2022-06-13 03:44:39.388527
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    freebsd_virtual = FreeBSDVirtual()

    virtual_facts = freebsd_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == set(['xen', 'vmware', 'oracle'])
    assert virtual_facts['virtualization_tech_host'] == set(['vmware', 'oracle'])

# Generated at 2022-06-13 03:44:48.205308
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual()

    # Fill the kern.vm_guest with a specific value
    kern_vm_guest = {
        "kern.vm_guest": {
            "type": "string",
            "value": "other"
        }
    }
    freebsd_virtual.kern = kern_vm_guest

    # Fill the hw.hv_vendor with a specific value
    hw_hv_vendor = {
        "hw.hv_vendor": {
            "type": "string",
            "value": "none"
        }
    }
    freebsd_virtual.hw = hw_hv_vendor

    # Fill the security.jail.jailed with a specific value

# Generated at 2022-06-13 03:44:54.971905
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    facts = FreeBSDVirtualCollector()
    assert facts._platform == 'FreeBSD'
    assert facts._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:44:58.830788
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    host_virtual_facts = {}
    host_virtual_facts = virtual_collector.collect()
    assert host_virtual_facts.keys() == ['virtualization_type',
                                         'virtualization_role',
                                         'virtualization_tech_host',
                                         'virtualization_tech_guest']


# Generated at 2022-06-13 03:45:08.946191
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    testcases = {}

    # FreeBSD 10.3-Release x86_64
    testcases['FreeBSD10-3'] = {}
    testcases['FreeBSD10-3']['kern.vm_guest'] = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': '',
        }
    testcases['FreeBSD10-3']['hw.hv_vendor'] = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_type': '',
        'virtualization_role': '',
        }

# Generated at 2022-06-13 03:45:11.261087
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fbc = FreeBSDVirtualCollector()
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'

# Generated at 2022-06-13 03:45:11.870409
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    pass

# Generated at 2022-06-13 03:45:16.864192
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    test_virtual_facts = FreeBSDVirtual()

    assert test_virtual_facts.get_virtual_facts() == {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_technologies_guest': set(),
        'virtualization_technologies_host': set(),
    }

# Generated at 2022-06-13 03:45:19.833558
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual(None, {})
    facts = v.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:45:22.131452
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create instance of class FreeBSDVirtual
    freebsd_virtual = FreeBSDVirtual()
    freebsd_virtual.get_virtual_facts()


# Generated at 2022-06-13 03:45:26.013438
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    import sys
    import os
    sys.modules['ansible'] = type('mock_ansible', (), {})
    os.environ['ANSIBLE_MODULE_UTILS'] = './'
    f = FreeBSDVirtual()
    result = f.get_virtual_facts()
    print(result)
    assert isinstance(result, dict)

# Generated at 2022-06-13 03:45:34.864617
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()

    def _fake_sysctl(mock):
        ret = dict()
        ret['kern.vm_guest'] = 'other'
        ret['hw.hv_vendor'] = 'Generic'
        ret['security.jail.jailed'] = '0'
        return ret
    virtual._query_sysctl = _fake_sysctl

    def _fake_virtual(mock, key):
        ret = dict()
        ret['hw.model'] = 'FreeBSD/amd64'
        return ret
    virtual._query_virtual_product = _fake_virtual

    expected_facts = dict()
    expected_facts['virtualization_type'] = 'other'
    expected_facts['virtualization_role'] = ''
    expected_facts['virtualization_product'] = 'Generic'
    expected_facts

# Generated at 2022-06-13 03:45:52.928309
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = {}
    ven = {'virtualization_type': '', 'virtualization_role': ''}
    ven2 = {'virtualization_type': '', 'virtualization_role': ''}

    # Test with empty facts
    ven = FreeBSDVirtual(facts).get_virtual_facts()
    assert ven['virtualization_type'] == ''
    assert ven['virtualization_role'] == ''

    # Update facts with the values returned by the class FreeBSDVirtual
    facts = {
        'kern_vm_guest': 'other',
        'hw_hv_vendor': 'unknown',
        'sec_jail_jailed': '0',
        'hw_model': 'VirtualBox'
    }

    # Test with valid facts
    ven = FreeBSDVirtual(facts).get_virtual_facts()

# Generated at 2022-06-13 03:45:54.579687
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    vc = FreeBSDVirtualCollector()
    assert vc.platform == 'FreeBSD'
    assert vc.fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:46:02.032864
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual = FreeBSDVirtualCollector().collect()
    # test FreeBSDVirtualCollector() object
    assert virtual.__class__.__name__ == 'dict'
    # test FreeBSDVirtualCollector() object instance of FreeBSDVirtual
    assert isinstance(virtual, FreeBSDVirtual)
    assert virtual.__class__.__name__ == 'FreeBSDVirtual'
    # test FreeBSDVirtualCollector() returns a dict
    assert virtual.__class__.__name__ == 'FreeBSDVirtual'

# Generated at 2022-06-13 03:46:06.411530
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual({}, {})
    assert v.get_virtual_facts() == {
        u'virtualization_type': u'',
        u'virtualization_role': u'',
        u'virtualization_tech_guest': set(),
        u'virtualization_tech_host': set()
    }

# Generated at 2022-06-13 03:46:06.750754
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:46:08.246107
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert type(obj.platform_virtual) == FreeBSDVirtual

# Generated at 2022-06-13 03:46:08.819856
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:46:19.369553
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Case 1: FreeBSD guest on Xen hypervisor
    virt_test_dict = {
        'hw.model': 'Xen HVM domU on FreeBSD 9.2-RELEASE-p3',
        'kern.vm_guest': 'xen',
        'security.jail.jailed': 0
    }

    expected_output_1 = {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': set(['xen'])
    }

    # Case 2: FreeBSD host hypervisor

# Generated at 2022-06-13 03:46:28.945509
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # generate test data
    keys_data = ('virtualization_type', 'virtualization_role',
                 'virtualization_tech_guest', 'virtualization_tech_host')
    virtual_type = ('', '', 'xen', '')
    virtual_role = ('', '', 'guest', '')
    # set() is designed for performance improvement by avoiding duplicate items
    virtual_tech_guest = (set(), set(), {'xen'}, {'jail'})
    virtual_tech_host = (set(), set(), set(), {'bhyve'})
    data_virtual_facts = zip(keys_data, virtual_type, virtual_role,
                             virtual_tech_guest, virtual_tech_host)

    # test data for subfunction detect_virt_product

# Generated at 2022-06-13 03:46:37.043753
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create an instance of FreeBSDVirtual class
    test_instance = FreeBSDVirtual()

    # Specify the test data
    test_data = {
        'sysctl': {
            'kern.vm_guest': ['freebsd'],
            'hw.hv_vendor': ['bhyve'],
            'security.jail.jailed': '0'},
        'vendor': {
            'hw.model': 'FreeBSD Virtual Machine'},
        'expected_facts': {
            'virtualization_role': 'guest',
            'virtualization_type': 'vmware',
            'virtualization_technologies_host': set(['vmware']),
            'virtualization_technologies_guest': set(['vmware'])}
    }

    # Get the virtualization facts
    actual_facts = test_

# Generated at 2022-06-13 03:47:01.588810
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''
    unit test for constructor of class FreeBSDVirtualCollector
    '''
    new_instance = FreeBSDVirtualCollector()
    assert new_instance.platform == 'FreeBSD'
    assert new_instance._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:47:05.977333
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    freebsd_virtual = FreeBSDVirtual({'ansible_system_capabilities': []})
    freebsd_virtual_facts = freebsd_virtual.get_virtual_facts()
    assert freebsd_virtual.platform == "FreeBSD"
    assert freebsd_virtual_facts['virtualization_type'] == ''
    assert freebsd_virtual_facts['virtualization_role'] == ''
    assert freebsd_virtual_facts['virtualization_tech_guest'] == set()
    assert freebsd_virtual_facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:47:08.033035
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual().get_virtual_facts()
    assert virtual_facts.get('virtualization_type') == ''
    assert virtual_facts.get('virtualization_role') == ''
    assert virtual_facts.get('virtualization_tech_guest') == set()
    assert virtual_facts.get('virtualization_tech_host') == set()

# Generated at 2022-06-13 03:47:11.461207
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    collector = FreeBSDVirtualCollector()
    assert collector.facts['virtualization_type'] == 'xen'
    assert collector.facts['virtualization_role'] == 'guest'

if __name__ == '__main__':
    test_FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:47:13.534506
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    c = FreeBSDVirtualCollector(None, None)
    assert isinstance(c, FreeBSDVirtualCollector)


# Generated at 2022-06-13 03:47:22.226169
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class FreeBSDVirtual.
    """

    import os
    import unittest
    import sys

    class FakeOS(object):

        @staticmethod
        def path_exists(pathname):
            return True if pathname == '/dev/xen/xenstore' else False

    class FakeSysctl(object):

        def __init__(self):
            self.outputs = {
                'hw.model': 'VirtualBox',
                'kern.vm_guest': 'other',
                'security.jail.jailed': 1,
                'hw.hv_vendor': 'bhyve'
            }
            self.popen_calls = []

        def __call__(self, var):
            return self.outputs[var]


# Generated at 2022-06-13 03:47:32.500995
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts of class FreeBSDVirtual"""
    fake_subprocess_call = FakeSubprocess()


# Generated at 2022-06-13 03:47:33.613008
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    virtual_collector = FreeBSDVirtualCollector()
    assert virtual_collector is not None

# Generated at 2022-06-13 03:47:38.049399
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts import facts

    # Instantiate FreeBSDVirtual class
    freebsd = FreeBSDVirtual(facts=facts)
    freebsd_virtual_facts = freebsd.get_virtual_facts()
    assert isinstance(freebsd_virtual_facts['virtualization_type'], str)
    assert isinstance(freebsd_virtual_facts['virtualization_role'], str)

# Generated at 2022-06-13 03:47:38.947974
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    assert FreeBSDVirtualCollector.platform == 'FreeBSD'


# Generated at 2022-06-13 03:48:36.780862
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    f = FreeBSDVirtualCollector()
    assert isinstance(f,VirtualCollector)
    assert f._platform == 'FreeBSD'
    assert f._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:48:40.871761
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual = FreeBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == set(['xen'])
    assert virtual_facts['virtualization_tech_host'] == set([])

# Generated at 2022-06-13 03:48:50.698428
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Setup FreeBSDVirtual instance
    test_instance = FreeBSDVirtual(None)

    # Test the get_virtual_facts method with empty dicts
    test_dicts = ([], [{}, {}], [{}, {'kern.vm_guest': 'none'}, {}])
    for d in test_dicts:
        assert test_instance.get_virtual_facts() == \
            {'virtualization_type': '', 'virtualization_role': '',
             'virtualization_tech_host': set(),
             'virtualization_tech_guest': set()}

    # Test with kvm hypervisor
    d = [{'hw.model': 'QEMU Virtual CPU version 2.4.2'}]

# Generated at 2022-06-13 03:48:51.404744
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:48:53.117879
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    '''Test class FreeBSDVirtualCollector constructor'''
    assert FreeBSDVirtualCollector

# Generated at 2022-06-13 03:48:57.896224
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}, {}).get_virtual_facts()
    assert facts['virtualization_type'] == 'jail'
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_tech_guest'] == set(['jail'])
    assert facts['virtualization_tech_host'] == set()

# Generated at 2022-06-13 03:49:03.310440
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    # Create a FreeBSDVirtual object
    fv = FreeBSDVirtual(module=None)

    # Set some return values
    fv.detect_virt_vendor = lambda x: dict(virtualization_type='xen')
    fv.detect_virt_product = lambda x: dict(virtualization_type='xen')

    facts = fv.get_virtual_facts()
    assert facts['virtualization_type'] == 'xen'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 03:49:05.282777
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    import sys
    import subprocess
    collect = FreeBSDVirtualCollector()
    assert collect._platform == 'FreeBSD'
    assert collect._fact_class == FreeBSDVirtual


# Generated at 2022-06-13 03:49:08.400542
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    h = FreeBSDVirtualCollector()
    assert type(h._fact_class) is FreeBSDVirtual
    assert h._platform == 'FreeBSD'


# Generated at 2022-06-13 03:49:09.083437
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:51:24.879490
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert obj.get_all_facts() != {}

# Generated at 2022-06-13 03:51:25.953854
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    obj = FreeBSDVirtualCollector()
    assert type(obj) is FreeBSDVirtualCollector
    assert type(obj._fact_class) is FreeBSDVirtual
    assert obj._platform == 'FreeBSD'

# Generated at 2022-06-13 03:51:28.025269
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    # initializing the object of FreeBSDVirtualCollector
    freebsd_obj = FreeBSDVirtualCollector()
    assert(freebsd_obj.platform=='FreeBSD')
    assert(freebsd_obj._fact_class==FreeBSDVirtual)

# Generated at 2022-06-13 03:51:30.570139
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    v = FreeBSDVirtual({})
    result = v.get_virtual_facts()
    assert type(result) == dict, "get_virtual_facts should return a dict"
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result

# Generated at 2022-06-13 03:51:32.873383
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    x = FreeBSDVirtualCollector()
    assert x.platform == 'FreeBSD'
    assert x._fact_class == FreeBSDVirtual

# Generated at 2022-06-13 03:51:34.676901
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    fv = FreeBSDVirtualCollector()
    assert fv.platform == 'FreeBSD'


# Generated at 2022-06-13 03:51:40.274219
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    virtual_facts = FreeBSDVirtual({}).get_virtual_facts()
    # Test default values
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_system' not in virtual_facts
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''



# Generated at 2022-06-13 03:51:42.602026
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():
    facts = FreeBSDVirtual({}).get_virtual_facts()
    assert facts['virtualization_type'] in ['', 'virtualbox', 'vmware', 'jail', 'xen', 'hvm', 'paravirtual']

# Generated at 2022-06-13 03:51:43.276626
# Unit test for constructor of class FreeBSDVirtualCollector
def test_FreeBSDVirtualCollector():
    FreeBSDVirtualCollector()

# Generated at 2022-06-13 03:51:51.846230
# Unit test for method get_virtual_facts of class FreeBSDVirtual
def test_FreeBSDVirtual_get_virtual_facts():

    # Dummy object
    freebsd_virtual_facts = FreeBSDVirtual({})

    # Load up our mock facts
    freebsd_virtual_facts.sysctl = {
        'hw.model': 'SKYTRAQ Venus 638FLPx-T',
        'security.jail.jailed': '0',
        'kern.vm_guest': 'none',
        'hw.hv_vendor': 'None',
        'hw.hv_support': '0',
        'hw.hv_version': 'None',
        'hw.hv_vendor_id': 'None',
    }

    # Make sure hw.hv_vendor_id is set
    assert 'hw.hv_vendor_id' in freebsd_virtual_facts.sysctl
    assert freebsd_