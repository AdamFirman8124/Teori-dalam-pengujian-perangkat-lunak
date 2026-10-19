

# Generated at 2022-06-13 04:09:55.351420
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    '''Test case for OpenBSDVirtual.get_virtual_facts method'''

    o = OpenBSDVirtual()
    o.get_virtual_facts()

# Generated at 2022-06-13 04:10:01.400374
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class OpenBSDVirtual
    """
    v = OpenBSDVirtual()
    facts = v.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

    # No vmm0 in dmesg.boot
    v.dmesg_boot = ""
    facts = v.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert 'virtualization_role' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

    # vmm0 in dmesg.boot

# Generated at 2022-06-13 04:10:02.813538
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    result = OpenBSDVirtualCollector()
    assert result._platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:04.643969
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    x = OpenBSDVirtualCollector()
    assert x.platform == 'OpenBSD'
    assert x._fact_class.platform == 'OpenBSD'
    assert x._fact_class.DMESG_BOOT == '/var/run/dmesg.boot'

# Generated at 2022-06-13 04:10:11.366075
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Input arguments
    host = OpenBSDVirtual()
    # Expected output
    virtual_facts_expected = dict(product_name='OpenBSD', vendor='OpenBSD',
                                  virtualization_type='vmm',
                                  virtualization_role='host',
                                  virtualization_tech_host=set('vmm'),
                                  virtualization_tech_guest=set())
    # Run code to be tested
    virtual_facts = host.get_virtual_facts()
    # Compare expected output with actual output
    for key in virtual_facts_expected:
        assert virtual_facts[key] == virtual_facts_expected[key]

# Generated at 2022-06-13 04:10:23.418570
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """Validates result of get_virtual_facts method for given output"""

# Generated at 2022-06-13 04:10:25.942316
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:27.744904
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    o = OpenBSDVirtualCollector()
    assert o._fact_class.platform == 'OpenBSD'

# Generated at 2022-06-13 04:10:37.913499
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """
    Unit test for method get_virtual_facts of class OpenBSDVirtual
    """
    openbsd_virtual = OpenBSDVirtual()

    # Indicates the host is capable of virtualization.

# Generated at 2022-06-13 04:10:49.570980
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    test_OpenBSDVirtual = OpenBSDVirtual()
    dmesg_boot = get_file_content(OpenBSDVirtual.DMESG_BOOT)
    assert test_OpenBSDVirtual.get_virtual_facts() == {'virtualization_type': '', 'virtualization_role': '', 'virtualization_tech_host': set(), 'virtualization_tech_guest': set()}
    for line in dmesg_boot.splitlines():
        match = re.match('^vmm0 at mainbus0: (SVM/RVI|VMX/EPT)$', line)

# Generated at 2022-06-13 04:10:56.453621
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()

    if virtual_facts['virtualization_tech_guest'] or virtual_facts['virtualization_tech_host']:
        assert virtual_facts['virtualization_type']
        assert virtual_facts['virtualization_role']

# Generated at 2022-06-13 04:11:04.381394
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    # create an instance
    openbsd_virtual_collector = OpenBSDVirtualCollector()

    # get a fact instance
    fact_instance = openbsd_virtual_collector.collect()

    supported_facts = frozenset([
        'virtualization_type',
        'virtualization_role',
        'virtualization_technology',
    ])

    # check if fact_instance is an instance of Virtual
    assert isinstance(fact_instance, Virtual)
    assert fact_instance.platform == openbsd_virtual_collector._platform
    # check if fact_instance provides all the supported facts
    assert supported_facts == fact_instance.supported_facts

# Generated at 2022-06-13 04:11:15.676728
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin
    import shutil
    import sys
    import tempfile
    import os
    import json

    dmesg_boot = tempfile.NamedTemporaryFile(prefix='ansible-test_OpenBSDVirtual_get_virtual_facts')
    dmesg_boot_path = dmesg_boot.name

# Generated at 2022-06-13 04:11:18.494283
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert isinstance(OpenBSDVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 04:11:25.164409
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual({'module_setup': {'filter': '*'}, 'gather_subset': 'all'})
    facts = virtual.get_virtual_facts()
    assert not facts['virtualization_role']
    assert not facts['virtualization_type']
    assert facts['virtualization_tech_host'] == facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_product_name'] == facts['virtualization_product_version'] == ''

# Generated at 2022-06-13 04:11:26.518870
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert issubclass(OpenBSDVirtualCollector, VirtualCollector)

# Generated at 2022-06-13 04:11:28.098931
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    c = OpenBSDVirtualCollector()
    assert(c.platform == 'OpenBSD')


# Generated at 2022-06-13 04:11:32.434446
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual({})
    virtual_facts = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
        'virtualization_vendor': '',
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_product': ''
    }
    assert openbsd_virtual_facts.get_virtual_facts() == virtual_facts

# Generated at 2022-06-13 04:11:34.548162
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    print(OpenBSDVirtualCollector())


# Generated at 2022-06-13 04:11:38.938213
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    facts = OpenBSDVirtual().get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''


if __name__ == '__main__':
    test_OpenBSDVirtual_get_virtual_facts()

# Generated at 2022-06-13 04:11:47.889071
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual()
    virtual_facts = openbsd_virtual_facts.get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_technology_host'] == set()
    assert virtual_facts['virtualization_technology_guest'] == set()
    assert virtual_facts['virtualization_product_name'] == ''
    assert virtual_facts['virtualization_product_version'] == ''

# Generated at 2022-06-13 04:11:57.582357
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_collector = OpenBSDVirtualCollector()
    virtual_facts = virtual_collector.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_product'] == 'VirtualBox'
    assert virtual_facts['virtualization_sysctl'] == 'hw.vboxguest'
    assert 'virtualbox' in virtual_facts['virtualization_tech_guest']
    assert 'virtualization_system' not in virtual_facts
    assert 'virtualization_role' not in virtual_facts

# Generated at 2022-06-13 04:12:05.496192
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    expected_virtual_facts = {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_host': {'vmm'},
        'virtualization_tech_guest': set()
    }

    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.facts = {'kernel': 'OpenBSD'}
    virtual_facts = openbsd_virtual.get_virtual_facts()
    assert virtual_facts == expected_virtual_facts

# Generated at 2022-06-13 04:12:12.225561
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    platform_virtual = OpenBSDVirtual()
    facts = platform_virtual.get_virtual_facts()

    # Dictionary of virtualization facts which should be returned by
    # get_virtual_facts()
    expected_facts = {
        'virtualization_role': '',
        'virtualization_type': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    assert facts == expected_facts

# Generated at 2022-06-13 04:12:17.840265
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()
    assert isinstance(virtual_facts['virtualization_type'], str)
    assert isinstance(virtual_facts['virtualization_role'], str)
    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 04:12:19.209409
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    obj = OpenBSDVirtualCollector()
    assert obj.platform == 'OpenBSD'
    assert obj._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:12:20.033489
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert not OpenBSDVirtualCollector().is_virtual()

# Generated at 2022-06-13 04:12:23.976573
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._fact_class == OpenBSDVirtual
    assert openbsd_virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:12:31.661062
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Test get_virtual_facts() with a OpenBSD virtual machine
    test_OpenBSD_vm = OpenBSDVirtual()

    virtual_facts = test_OpenBSD_vm.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == 'vmm'
    assert 'vmm' in virtual_facts['virtualization_tech_host']
    assert virtual_facts['virtualization_role'] == 'guest'
    assert 'vmware' in virtual_facts['virtualization_tech_guest']
    assert 'hv' in virtual_facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:12:33.348732
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:12:49.219638
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    import json
    # Create instance of the OpenBSDVirtual class
    virtualTest = OpenBSDVirtual({})
    # Create mock facts
    testFacts = {
        'kernel': 'OpenBSD',
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    # Check the call of method get_virtual_facts with mock data
    virtualFacts = virtualTest.get_virtual_facts()
    # Check values
    assert virtualFacts['kernel'] == 'OpenBSD'
    assert virtualFacts['virtualization_type'] == ''
    assert virtualFacts['virtualization_role'] == ''
    assert virtualFacts['virtualization_tech_guest'] == set()

# Generated at 2022-06-13 04:12:51.393695
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    vc = OpenBSDVirtualCollector()
    assert vc.platform == 'OpenBSD'


# Generated at 2022-06-13 04:12:53.824020
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    test = OpenBSDVirtualCollector()
    assert test._platform == 'OpenBSD'
    assert test._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:12:56.164268
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert virtual_collector._fact_class == OpenBSDVirtual
    assert virtual_collector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:12:56.955359
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    OpenBSDVirtualCollector()



# Generated at 2022-06-13 04:13:07.682177
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts = OpenBSDVirtual().get_virtual_facts()

    # Test to make sure the information returned is the information
    # required by the module.
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_technologies_guest' in virtual_facts
    assert 'virtualization_technologies_host' in virtual_facts

    assert virtual_facts['virtualization_type'] \
        in ('vmm', 'openvz', 'linux-vserver', 'xen', 'kvm', 'qemu', 'virtualbox', '')
    assert virtual_facts['virtualization_role'] \
        in ('guest', 'host', '')

# Generated at 2022-06-13 04:13:09.347130
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    fact_subclass = OpenBSDVirtualCollector()
    assert fact_subclass._platform == 'OpenBSD'


# Generated at 2022-06-13 04:13:19.563149
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts_obj = OpenBSDVirtual()
    virtual_facts_obj.facts = {}

    # Test case for hw.product is empty
    virtual_facts_obj.sysctl_cmd = 'sysctl -a 2> /dev/null'

    virtual_facts_obj._get_sysctl_output = lambda: 'hw.product=\n'
    assert virtual_facts_obj.get_virtual_facts() == {
        'virtualization_type': '',
        'virtualization_role': '',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }

    # Test case for hw.product is VirtualBox
    virtual_facts_obj.sysctl_cmd = 'sysctl -a 2> /dev/null'
    virtual_facts_obj._get_sysctl

# Generated at 2022-06-13 04:13:24.146085
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    detector = OpenBSDVirtual()
    assert detector.get_virtual_facts() == {
        'virtualization_type': 'vmm',
        'virtualization_role': 'host',
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': {'vmm'}
    }

# Generated at 2022-06-13 04:13:29.572902
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # Set the expected result
    expected_result = {
        'virtualization_type': 'guest',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': {'xen'},
    }

    # Create an instance of the OpenBSDVirtual class
    test_obj = OpenBSDVirtual()

    # Test method get_virtual_facts of class OpenBSDVirtual
    assert test_obj.get_virtual_facts() == expected_result

# Generated at 2022-06-13 04:13:43.991967
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector()
    assert openbsd_virtual._fact_class is not None
    assert openbsd_virtual._platform is not None

# Generated at 2022-06-13 04:13:45.688083
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector._platform == 'OpenBSD'



# Generated at 2022-06-13 04:13:51.187585
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virt = OpenBSDVirtual()
    facts = virt.get_virtual_facts()
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts
    assert 'virtualization_role' in facts
    assert 'virtualization_type' in facts

# Generated at 2022-06-13 04:13:53.874876
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual = OpenBSDVirtualCollector().collect()
    assert openbsd_virtual.get('virtualization_type') == ''
    assert openbsd_virtual.get('virtualization_role') == ''

# Generated at 2022-06-13 04:14:00.232694
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtual._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector.virtual is OpenBSDVirtual
    assert OpenBSDVirtualCollector.virtual_collector is OpenBSDVirtualCollector
    assert OpenBSDVirtualCollector.collect is OpenBSDVirtualCollector.collect_virtual_facts
    oobc = OpenBSDVirtualCollector()
    assert oobc.platform == 'OpenBSD'
    assert oobc.virtual is OpenBSDVirtual

# Generated at 2022-06-13 04:14:03.730301
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    openbsd_virtual_collector = OpenBSDVirtualCollector()
    assert openbsd_virtual_collector.platform == "OpenBSD"
    assert isinstance(openbsd_virtual_collector._fact_class(), OpenBSDVirtual)

# Generated at 2022-06-13 04:14:08.510581
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual_facts_obj = OpenBSDVirtual()
    virtual_facts_obj.sysctl.read_sysctl_values()
    virtual_facts_obj.sysctl.read_file(OpenBSDVirtual.DMESG_BOOT)
    virtual_facts = virtual_facts_obj.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['vmware_guest_id'] == 'OpenBSD'

# Generated at 2022-06-13 04:14:12.105673
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    """This function is a unit test of the constructor of the
    OpenBSDVirtualCollector class.
    """
    fact_class = OpenBSDVirtualCollector._fact_class
    platform = OpenBSDVirtualCollector._platform
    fc = OpenBSDVirtualCollector()
    assert fc._fact_class == fact_class
    assert fc._platform == platform

# Generated at 2022-06-13 04:14:13.802368
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd = OpenBSDVirtual()
    virtual_facts = openbsd.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmm'

# Generated at 2022-06-13 04:14:15.775849
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    result = openbsd_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:14:44.154162
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'
    assert OpenBSDVirtualCollector._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:14:48.342920
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    """ Test for method get_virtual_facts of class OpenBSDVirtual """
    module = OpenBSDVirtual()
    assert module.get_virtual_facts() == dict(
        virtualization_type='OpenBSD virtualization',
    )

# Generated at 2022-06-13 04:14:50.234692
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virt = OpenBSDVirtual()
    openbsd_virt.get_virtual_facts()


# Generated at 2022-06-13 04:14:54.991248
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual = OpenBSDVirtual()
    openbsd_virtual.will_virtualize = False
    openbsd_virtual.get_virtual_facts()
    assert openbsd_virtual.virtualization_type == ''
    assert openbsd_virtual.virtualization_role == ''
    assert set(openbsd_virtual.virtualization_tech_guest) == set([])
    assert set(openbsd_virtual.virtualization_tech_host) == set([])

# Generated at 2022-06-13 04:14:57.068910
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector.platform == 'OpenBSD'
    assert collector.fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:15:07.113440
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    openbsd_virtual_facts = OpenBSDVirtual()
    openbsd_virtual_facts_dict = openbsd_virtual_facts.get_virtual_facts()

    assert 'virtualization_type' in openbsd_virtual_facts_dict
    assert 'virtualization_role' in openbsd_virtual_facts_dict
    assert 'virtualization_product_name' in openbsd_virtual_facts_dict
    assert 'virtualization_product_version' in openbsd_virtual_facts_dict
    assert 'virtualization_host_hostname' in openbsd_virtual_facts_dict
    assert 'virtualization_host_product_name' in openbsd_virtual_facts_dict
    assert 'virtualization_host_product_version' in openbsd_virtual_facts_dict
    assert 'virtualization_host_uuid'

# Generated at 2022-06-13 04:15:13.536679
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():

    # The dmesg should be read from a file, so we can test
    # for different scenarios
    class TestOpenBSDVirtual(OpenBSDVirtual):
        DMESG_BOOT = 'tests/unittests/dmesg_boot.txt'

    # Virtualization is neither host nor guest
    virtual = TestOpenBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()

    # Virtualization is only guest
    virtual = TestOpenBSDVirtual()
    virtual._sysctl_value = 'VirtualBox'
    virtual_facts = virtual.get_virtual_facts()

# Generated at 2022-06-13 04:15:14.472695
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    assert OpenBSDVirtualCollector.get_instance(None) is not None


# Generated at 2022-06-13 04:15:15.070049
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector is not None

# Generated at 2022-06-13 04:15:17.130894
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    virtual_collector = OpenBSDVirtualCollector()
    assert virtual_collector.platform == 'OpenBSD'
    assert virtual_collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:16:28.918199
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    virtual = OpenBSDVirtual()
    virtual_facts = virtual.get_virtual_facts()

    assert virtual_facts.get('virtualization_type') == ''
    assert virtual_facts.get('virtualization_role') == ''
    assert virtual_facts.get('virtualization_tech_host') == set()
    assert virtual_facts.get('virtualization_tech_guest') == set()

# Generated at 2022-06-13 04:16:33.534009
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    vm = OpenBSDVirtual()
    virtual_facts = vm.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts

# Generated at 2022-06-13 04:16:34.427692
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    """
    Constructor of class OpenBSDVirtualCollector
    """
    assert OpenBSDVirtualCollector._platform == 'OpenBSD'

# Generated at 2022-06-13 04:16:35.252385
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    collector = OpenBSDVirtualCollector()
    assert collector._fact_class == OpenBSDVirtual

# Generated at 2022-06-13 04:16:45.301054
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    mock_virtual_product = {'virtualization_tech_guest': set(), 'virtualization_tech_host': set(), 'virtualization_type': '', 'virtualization_role': ''}

    # Case 1: guest_tech and host_tech are empty sets
    mock_virtual_vendor = {'virtualization_tech_guest': set(), 'virtualization_tech_host': set(), 'virtualization_type': '', 'virtualization_role': ''}
    mock_dmesg = '''
    BIOS callOEMService(0xfb) returned 0xffffffff
    vmm0 at mainbus0: SVM/RVI
    '''
    virtual = OpenBSDVirtual(dmesg=mock_dmesg)

# Generated at 2022-06-13 04:16:49.499480
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # No virtualization facts
    p = OpenBSDVirtual({}, {})
    facts = p.get_virtual_facts()
    assert facts['virtualization_type'] == ''
    assert facts['virtualization_role'] == ''
    assert facts['virtualization_technology_guest'] == set()
    assert facts['virtualization_technology_host'] == set()

# Generated at 2022-06-13 04:16:52.966170
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    obj = OpenBSDVirtualCollector()
    assert obj.get_platform() == 'OpenBSD'
    assert obj.get_fact_class() == OpenBSDVirtual


# Generated at 2022-06-13 04:16:55.050279
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    v = OpenBSDVirtualCollector()
    assert v.platform == 'OpenBSD'
    assert v._fact_class == OpenBSDVirtual


# Generated at 2022-06-13 04:16:59.371809
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    v = OpenBSDVirtual({'path': '.'})
    virtual_facts = v.get_virtual_facts()

    assert virtual_facts['virtualization_type'] == ''
    assert virtual_facts['virtualization_role'] == ''

# Generated at 2022-06-13 04:17:01.954969
# Unit test for constructor of class OpenBSDVirtualCollector
def test_OpenBSDVirtualCollector():
    try:
        obj = OpenBSDVirtualCollector()
        assert obj._fact_class == OpenBSDVirtual
        assert obj._platform == 'OpenBSD'
    except Exception as e:
        print(e)
        assert False

# Generated at 2022-06-13 04:19:41.601931
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    # pylint: disable=too-few-public-methods
    class test_args:
        def __init__(self, vargs):
            self.args = vargs

    # This class is used to get the desired output
    # from the get_virtual_facts method of class OpenBSDVirtual
    class OpenBSDVirtual_test:
        # pylint: disable=too-few-public-methods
        def get_virtual_facts(self):
            res = {'virtualization_type': '', 'virtualization_role': ''}
            res.update(self.__dict__)
            return res

    # This is the input data for this test
    vargs = test_args({'virtualization_type': '', 'virtualization_role': ''})
    OpenBSDVirtual_test.__dict__ = vargs.args

   

# Generated at 2022-06-13 04:19:46.977353
# Unit test for method get_virtual_facts of class OpenBSDVirtual

# Generated at 2022-06-13 04:19:54.697273
# Unit test for method get_virtual_facts of class OpenBSDVirtual
def test_OpenBSDVirtual_get_virtual_facts():
    mocker = Mocker()
    mock_collector = mocker.mock()
    mock_collector.get_file_content(OpenBSDVirtual.DMESG_BOOT)
    mocker.result('''
vmm0 at mainbus0: SVM/RVI
vmd0 at mainbus0
fuse0 at mainbus0
fuse0: mem 0xffffffff80000000-0xffffffff9fffffff,0xffffffffc0000000-0xffffffffcfffffff
fuse0: 32-bit applications not supported
fuse0: using FDSE mode
boot device: sd0
root on sd0a swap on sd0b dump on sd0b
''')
