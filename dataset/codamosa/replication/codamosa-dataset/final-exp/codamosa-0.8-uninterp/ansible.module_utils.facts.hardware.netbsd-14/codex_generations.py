

# Generated at 2022-06-13 00:56:55.779503
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    content = """MemTotal:       16272268 kB
SwapTotal:      2428724 kB
MemFree:          69976 kB
SwapFree:        995916 kB"""

    input_lines = content.splitlines()
    facts_dict = NetBSDHardware(dict()).get_memory_facts()
    assert facts_dict == {'memfree_mb': 69, 'swapfree_mb': 971,
                          'memtotal_mb': 15869, 'swaptotal_mb': 2359}


# Generated at 2022-06-13 00:57:02.456605
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = AnsibleModuleMock()
    hardware_collector = NetBSDHardwareCollector(module=module)
    hardware = hardware_collector.collect()[0]
    hardware.populate()
    facts = hardware.get_facts()

    assert facts['processor'][0] == 'ARMv7 Processor rev 5 (v7l)'
    assert facts['memtotal_mb'] == 514
    assert facts['swaptotal_mb'] == 992
    assert facts['processor_cores'] == 4
    assert facts['processor_count'] == 1
    assert facts['mounts'][0]['mount'] == '/'
    assert facts['mounts'][0]['device'] == '/dev/wd0a'



# Generated at 2022-06-13 00:57:11.860261
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    """Unit test for method populate of class NetBSDHardware."""
    #
    # This test checks that the NetBSDHardware.populate() method works
    # as expected.
    #
    # References
    #
    # - http://docs.python-guide.org/en/latest/writing/tests/
    #

    def test_func():
        hw = NetBSDHardware()
        return hw.populate()

    class FakeModule:
        def __init__(self):
            self.params = {}

    fake_module = FakeModule()


# Generated at 2022-06-13 00:57:20.893293
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # Test NetBSDHardware.populate() with a simple set of facts.
    import textwrap

# Generated at 2022-06-13 00:57:31.757614
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import get_collector
    from ansible.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector
    import json
    import sys

    # Create a new module object
    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    # Load the hardware facts
    collector = get_collector(module, 'NetBSDHardwareCollector')

    # Get the facts
    hardware_facts = collector.collect()
    hardware = NetBSDHardware(module)
    hardware_facts = hardware.populate()

    # Load the output into a JSON object

# Generated at 2022-06-13 00:57:36.649111
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    module = None
    facts = NetBSDHardwareCollector.collect(module=module, collected_facts=None)
    assert 'memtotal_mb' in facts
    assert 'memfree_mb' in facts
    assert 'swaptotal_mb' in facts
    assert 'swapfree_mb' in facts
    assert 'processor_cores' in facts
    assert 'processor_count' in facts
    assert 'processor' in facts
    assert isinstance(facts['processor'], list)

# Generated at 2022-06-13 00:57:39.200750
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    hc = NetBSDHardwareCollector()
    assert(hc.__class__.__name__ == 'NetBSDHardwareCollector')
    assert(hc._platform == 'NetBSD')
    assert(hc._fact_class.__name__ == 'NetBSDHardware')

# Generated at 2022-06-13 00:57:50.151421
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    sysctl = {'machdep.dmi.system-product': 'System Product Name',
              'machdep.dmi.system-version': 'System Version',
              'machdep.dmi.system-uuid': '89898989-8989-8989-8989-898989898989',
              'machdep.dmi.system-serial': 'System Serial',
              'machdep.dmi.system-vendor': 'System Vendor'}

    dmi_facts = NetBSDHardware.get_dmi_facts(sysctl)

    assert dmi_facts['product_name'] == 'System Product Name'
    assert dmi_facts['product_version'] == 'System Version'

# Generated at 2022-06-13 00:57:53.316713
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    x = NetBSDHardwareCollector()
    assert isinstance(x, NetBSDHardwareCollector)

# Generated at 2022-06-13 00:58:00.929702
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class MockModule(object):
        def __init__(self, sysctl):
            self.sysctl = sysctl
            self.fail_json = lambda **kwargs: None

    h = NetBSDHardware(MockModule({}))
    assert h.get_dmi_facts() == {}

    h = NetBSDHardware(MockModule({'machdep.dmi.system-product': 'ham',
                                   'machdep.dmi.system-version': 'spam',
                                   'machdep.dmi.system-uuid': 'bacon',
                                   'machdep.dmi.system-serial': 'eggs',
                                   'machdep.dmi.system-vendor': 'baz'}))

# Generated at 2022-06-13 00:59:15.136714
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hardware = NetBSDHardware()
    netbsd_hardware_facts = {'processor_cores': 4,
                             'devices': [],
                             'processor_count': 4,
                             'processor': [],
                             'memfree_mb': 1024,
                             'memtotal_mb': 2047,
                             'swaptotal_mb': 0,
                             'swapfree_mb': 0}

    assert netbsd_hardware.populate({}) == netbsd_hardware_facts

# Generated at 2022-06-13 00:59:23.200807
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    import io
    import unittest
    from unittest.mock import MagicMock, patch

    from ansible.module_utils.facts.hardware import NetBSDHardware


# Generated at 2022-06-13 00:59:24.840565
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    NetBSDHardwareCollector()

# Generated at 2022-06-13 00:59:34.266622
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():

    class NetBSDHardwareTest(NetBSDHardware):
        def __init__(self):
            self.sysctl = {
                'machdep.dmi.system-product': 'Not a real product',
                'machdep.dmi.system-version': 'Not a real version',
                'machdep.dmi.system-uuid': '00000000-0000-0000-0000-000000000000',
                'machdep.dmi.system-serial': '00000000000000000000',
                'machdep.dmi.system-vendor': 'Not a real vendor'}

    netbsd_hardware = NetBSDHardwareTest()
    netbsd_hardware.populate()
    dmi_facts = netbsd_hardware.get_dmi_facts()


# Generated at 2022-06-13 00:59:40.287993
# Unit test for method get_cpu_facts of class NetBSDHardware
def test_NetBSDHardware_get_cpu_facts():
    netbsd_hw = NetBSDHardware()
    cpu_facts = netbsd_hw.get_cpu_facts()

    processor_count = cpu_facts['processor_count']
    processor_cores = cpu_facts['processor_cores']
    processor = cpu_facts['processor']

    assert processor_count > 0
    assert processor_cores > 0
    assert processor



# Generated at 2022-06-13 00:59:41.340363
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hw = NetBSDHardware()
    hw.populate()

    assert hw.facts['os']['name'] == 'NetBSD'

# Generated at 2022-06-13 00:59:43.361134
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    netbsd_hw = NetBSDHardware(None)
    netbsd_hw.populate()

# Generated at 2022-06-13 00:59:50.616857
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    Hardware = NetBSDHardware()
    Hardware.sysctl = {'machdep.dmi.system-product': 'System',
                       'machdep.dmi.system-version': 'Version',
                       'machdep.dmi.system-uuid': '01234567-89AB-CDEF-0123-456789ABCDEF',
                       'machdep.dmi.system-serial': 'Serial number',
                       'machdep.dmi.system-vendor': 'Vendor'}

# Generated at 2022-06-13 00:59:58.609417
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    # test when /proc/meminfo is not accessible
    nhw = NetBSDHardware()
    assert nhw.get_memory_facts() == {}

    # helper function for the rest of the test
    def get_contents(*path):
        "Reads the content from the given path."
        from ansible.module_utils._text import to_bytes
        from ansible.module_utils.facts.hardware.netbsd import get_file_content

        content = get_file_content(to_bytes('/'.join(path)))
        return content if content else b''

    # setup for below tests
    import pytest


# Generated at 2022-06-13 01:00:02.829184
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    module = AnsibleModuleFake({})
    hardware = NetBSDHardware(module)

# Generated at 2022-06-13 01:02:33.859619
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware_obj = NetBSDHardware()
    m = hardware_obj.populate()
    assert type(m['mounts']) is list
    assert type(m['processor']) is list
    assert type(m['memtotal_mb']) is int
    assert type(m['memfree_mb']) is int
    assert type(m['swaptotal_mb']) is int
    assert type(m['swapfree_mb']) is int
    assert type(m['processor_count']) is int
    assert type(m['processor_cores']) is str or type(m['processor_cores']) is int

# Generated at 2022-06-13 01:02:38.417596
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    netbsd_hw = NetBSDHardware()
    memory = netbsd_hw.get_memory_facts()
    assert memory['swapfree_mb'] > 0
    assert memory['swaptotal_mb'] > 0
    assert memory['memfree_mb'] > 0
    assert memory['memtotal_mb'] > 0


# Generated at 2022-06-13 01:02:42.072398
# Unit test for constructor of class NetBSDHardwareCollector
def test_NetBSDHardwareCollector():
    import os
    os.environ['PATH'] = '/usr/local/bin:/usr/bin:/bin:/usr/pkg/bin'
    hc = NetBSDHardwareCollector()
    assert(hc.sysfs_path == '/kern')
    assert(hc.platform == 'NetBSD')
    assert(isinstance(hc.collect(), dict))

# Generated at 2022-06-13 01:02:48.884258
# Unit test for method get_memory_facts of class NetBSDHardware
def test_NetBSDHardware_get_memory_facts():
    netbsd_hardware = NetBSDHardware()
    content = ""
    for line in NetBSDHardware.MEMORY_FACTS:
        content += "%s:128\n" % line
    setattr(netbsd_hardware, 'get_file_content', lambda x: content)
    facts = netbsd_hardware.get_memory_facts()
    assert facts['swaptotal_mb'] == 128
    assert facts['memtotal_mb'] == 128
    assert facts['swapfree_mb'] == 128
    assert facts['memfree_mb'] == 128

# Generated at 2022-06-13 01:02:55.526159
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hardware = NetBSDHardware({})
    hardware_facts = hardware.populate()

    facts_to_check = ['processor_cores', 'processor', 'processor_count', 'processor_cores']
    for fact in facts_to_check:
        if hardware_facts[fact] < 1:
            assert False, '%s fact is missing: %s' % (fact, hardware_facts[fact])

    facts_to_check = ['devices', 'mounts']
    for fact in facts_to_check:
        if hardware_facts[fact] == []:
            assert False, '%s fact is missing: %s' % (fact, hardware_facts[fact])

# Generated at 2022-06-13 01:02:58.151602
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    facts = NetBSDHardware().populate()
    assert facts['processor_count'] == 1
    assert facts['processor_cores'] == 'NA'
    assert facts['memtotal_mb'] > 0
    assert facts['swaptotal_mb'] > 0


# Generated at 2022-06-13 01:03:03.970243
# Unit test for method get_dmi_facts of class NetBSDHardware
def test_NetBSDHardware_get_dmi_facts():
    class NetBSDHardwareFacts():
        def __init__(self, module, sysctl):
            # dmi_facts = self.get_dmi_facts()
            self.sysctl = sysctl

    sysctl_to_dmi = {
        'machdep.dmi.system-product': 'product_name',
        'machdep.dmi.system-version': 'product_version',
        'machdep.dmi.system-uuid': 'product_uuid',
        'machdep.dmi.system-serial': 'product_serial',
        'machdep.dmi.system-vendor': 'system_vendor',
    }

    # Create a sysctl dict
    sysctl = {}
    for mib in sysctl_to_dmi:
        sysctl[mib] = m

# Generated at 2022-06-13 01:03:13.147481
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    import sys
    import ast
    import json

    sys.path.append('../..')
    sys.path.append('..')
    import lib_netbsd_hardware as nb

    # Define the module parameters
    module = 'test_module'
    timeout = 10
    gather_subset = set(['all'])
    filter_exclude = []

    # Instantiate NetBSDHardware class
    nb_hw = nb.NetBSDHardware(module, timeout, gather_subset, filter_exclude)

    # Populate the facts and get the result
    res = nb_hw.populate()
    print(json.dumps(res, indent=4))

# Generated at 2022-06-13 01:03:21.101841
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    hw = NetBSDHardware()
    hw.module = MagicMock()
    hw.module.get_mount_size.return_value = {'size_total': 169902202880, 'size_available': 58811144192}

# Generated at 2022-06-13 01:03:24.717654
# Unit test for method populate of class NetBSDHardware
def test_NetBSDHardware_populate():
    # NetBSDHardware
    # Requires running in a NetBSD VM
    collected_facts = {}
    set_module_args({})
    nh = NetBSDHardware()
    nh.populate(collected_facts)
    assert 'processor' in collected_facts
    assert 'processor_cores' in collected_facts
    assert 'processor_count' in collected_facts
    assert 'devices' in collected_facts