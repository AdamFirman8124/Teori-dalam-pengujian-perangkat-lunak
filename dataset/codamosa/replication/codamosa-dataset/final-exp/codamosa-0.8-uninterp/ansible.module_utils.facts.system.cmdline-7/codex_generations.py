

# Generated at 2022-06-13 02:30:18.997232
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    tester = CmdLineFactCollector()
    assert tester.name == 'cmdline'

# Generated at 2022-06-13 02:30:21.418467
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert len(collector._fact_ids) == 0


# Generated at 2022-06-13 02:30:24.837628
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    test_class = CmdLineFactCollector()
    assert test_class.name == 'cmdline'
    assert test_class.collect() == {'cmdline': {}, 'proc_cmdline': {}}


# Generated at 2022-06-13 02:30:27.970297
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    CmdLineFactCollector_obj = CmdLineFactCollector()
    cmdline = CmdLineFactCollector_obj.collect()['cmdline']

    assert isinstance(cmdline, dict)

# Generated at 2022-06-13 02:30:29.572594
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert not c._fact_ids

# Generated at 2022-06-13 02:30:38.300469
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    result = cmdline_fact_collector.collect()


# Generated at 2022-06-13 02:30:43.850185
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import observer
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector

    module = basic.AnsibleModule(argument_spec={})
    mock_observer = observer.Observer()

    # get a handle on the correct collector automatically
    cmdline_collector = get_collector_instance('cmdline', module=module, observer=mock_observer)

    assert isinstance(cmdline_collector, CmdLineFactCollector)

    cmdline_facts = cmdline_collector.collect()

    assert 'cmdline' in cmdline_facts

# Generated at 2022-06-13 02:30:46.987430
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()


# Generated at 2022-06-13 02:30:51.046717
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    ''' Unit test for method collect of class CmdLineFactCollector '''
    cmdline_fact_collector = CmdLineFactCollector()
    collected_facts = dict()
    result = cmdline_fact_collector.collect(collected_facts=collected_facts)
    assert isinstance(result, dict)



# Generated at 2022-06-13 02:31:00.533442
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Unit test for method collect of class CmdLineFactCollector when no data is present in
    # /proc/cmdline
    mock_cmdline_content = ''
    mock_get_file_content = lambda file_name: mock_cmdline_content
    c = CmdLineFactCollector(get_file_content=mock_get_file_content)
    cmdline_facts_collected = c.collect()
    assert cmdline_facts_collected == {}

    # Unit test for method collect of class CmdLineFactCollector when data is present in
    # /proc/cmdline

# Generated at 2022-06-13 02:31:13.329502
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector_obj = CmdLineFactCollector()
    ansible_facts = {}
    collected_facts = cmdline_collector_obj.collect(collected_facts=ansible_facts)
    assert collected_facts['cmdline']['root'] == '/dev/mapper/VolGroup00-LogVol00'
    assert collected_facts['proc_cmdline']['ro'] == True
    assert collected_facts['proc_cmdline']['S'] == True
    assert collected_facts['proc_cmdline']['rd_NO_LUKS'] == True
    assert collected_facts['proc_cmdline']['rd_LVM_LV=VolGroup00/LogVol00'] == True
    assert collected_facts['proc_cmdline']['rd_NO_MD'] == True

# Generated at 2022-06-13 02:31:14.288751
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    CmdLineFactCollector().collect()

# Generated at 2022-06-13 02:31:19.509769
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    import copy
    cmdline1 = CmdLineFactCollector()
    cmdline2 = CmdLineFactCollector()
    assert cmdline1 == cmdline2
    assert cmdline1 is not cmdline2
    assert cmdline1.__dict__ == cmdline2.__dict__
    assert cmdline1.name == cmdline2.name
    assert cmdline1._fact_ids == cmdline2._fact_ids

# Generated at 2022-06-13 02:31:21.139878
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    objs = CmdLineFactCollector()
    assert objs is not None


# Generated at 2022-06-13 02:31:29.531703
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:31:32.843109
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = {}
    cmdline_facts = CmdLineFactCollector().collect()
    assert isinstance(cmdline_facts, dict)
    assert 'cmdline' in cmdline_facts
    assert 'proc_cmdline' in cmdline_facts
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:31:38.029493
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.utils import AnsibleFactCollector

    # Test initialization
    module = AnsibleFactCollector
    collected_facts = {}
    module.options = {}
    Collector.__init__ = lambda self, module: None
    FactCollector.__init__ = lambda self, module: None

    # Test simple collect
    test_collector = CmdLineFactCollector(module)
    test_collector._get_proc_cmdline = lambda: 'root=LABEL=ROOT-A rw quiet'
    cmdline_facts = test_collector.collect(module, collected_facts)

# Generated at 2022-06-13 02:31:40.326398
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()


# Generated at 2022-06-13 02:31:46.097156
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = CmdLineFactCollector()._get_proc_cmdline()

    cmdline_facts = CmdLineFactCollector().collect()

    # Check data is not empty
    assert data

    # Check if the data was parsed correctly
    assert data == 'BOOT_IMAGE=(hd0,msdos1)/boot/vmlinuz-linux root=UUID=f83e253d-cad0-489e-a27e-2a1e624a0c55 rootfstype=ext4 rw add_efi_memmap quiet loglevel=3 initrd=\initramfs-linux.img systemd.show_status=0'

    # Check if the data was parsed correctly into a dictionary

# Generated at 2022-06-13 02:31:55.899193
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    from ansible.module_utils.facts.collector import LocalCollector
    from ansible.module_utils.facts.collectors import collect_subset
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector
    import os
    import pytest
    import json

    # Initiate a local collector
    local_collector = LocalCollector()

    # Create the class object
    obj = CmdLineFactCollector(local_collector)

    # Check the name of the object
    assert obj.name == 'cmdline'

    # Check if we can get the cmdline facts
    cmdline_facts = obj.collect(None, None)
    os.environ['PROC_CMDLINE'] = open('/proc/cmdline').read()

# Generated at 2022-06-13 02:32:23.190759
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    facts = cmdline_fact_collector.collect()
    assert facts == {'cmdline': {'BOOT_IMAGE': '/boot/vmlinuz-3.13.0-29-generic',
                                 'root': '/dev/mapper/ubuntu--vg-root',
                                 'ro': True,
                                 'quiet': True,
                                 'splash': True},
                     'proc_cmdline': {'BOOT_IMAGE': '/boot/vmlinuz-3.13.0-29-generic',
                                      'root': '/dev/mapper/ubuntu--vg-root',
                                      'ro': True,
                                      'quiet': True,
                                      'splash': True}}

# Generated at 2022-06-13 02:32:26.487832
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    facts = collector.collect()
    assert isinstance(facts['cmdline'], dict)
    assert isinstance(facts['proc_cmdline'], dict)


# Generated at 2022-06-13 02:32:36.379674
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import __virtual__
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts import module

    class MockCmdLineFactCollector(CmdLineFactCollector):
        def _get_proc_cmdline(self):
            return "root=/dev/mapper/vg_trixbox-lv_root ro rd_NO_LUKS rd_NO_MD rd_NO_DM LANG=en_US.UTF-8 SYSFONT=latarcyrheb-sun16 rhgb quiet crashkernel=auto KEYBOARDTYPE=pc KEYTABLE=us audit=1"

    # Setup the mock environment
    #__virtual__.__globals__['__salt__'] = {'cmd.run': cmdrun}


# Generated at 2022-06-13 02:32:39.053996
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()

    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()



# Generated at 2022-06-13 02:32:40.502635
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:32:42.366065
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    list1 = CmdLineFactCollector()
    assert list1.name == 'cmdline'
    assert not list1._fact_ids

# Generated at 2022-06-13 02:32:43.930100
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact = CmdLineFactCollector()
    assert cmdline_fact.name == "cmdline"

# Generated at 2022-06-13 02:32:46.041695
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert fact_collector.name == 'cmdline'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:32:47.350917
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():

    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert isinstance(obj._fact_ids, object)

# Generated at 2022-06-13 02:32:58.434310
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:33:26.669548
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os
    import tempfile
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    # Create an in-memory file for /proc/cmdline
    with tempfile.NamedTemporaryFile(mode='wt') as f:
        # Set current process cmdline as content of this file
        f.write(' '.join(x.decode('utf-8') for x in os.uname()))
        f.flush()

        # init CmdLineFactCollector
        cmdline_collector = CmdLineFactCollector()

        # Make this in-memory file available to get_file_content

# Generated at 2022-06-13 02:33:36.156199
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    ansible_facts = {}
    ansible_facts['proc_cmdline'] = "BOOT_IMAGE=/vmlinuz-3.10.0-957.5.1.el7.x86_64 root=/dev/mapper/cl-root ro crashkernel=auto rhgb quiet LANG=en_US.UTF-8"
    ansible_facts['cmdline'] = {'BOOT_IMAGE': '/vmlinuz-3.10.0-957.5.1.el7.x86_64',
                                'crashkernel': 'auto',
                                'root': '/dev/mapper/cl-root',
                                'ro': True,
                                'rhgb': True,
                                'quiet': True,
                                'LANG': 'en_US.UTF-8'}
    cmd = C

# Generated at 2022-06-13 02:33:41.465220
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import ListCollector

    l1 = ListCollector('cmdline')
    l2 = ListCollector('proc_cmdline')
    cmdline_f1 = CmdLineFactCollector()
    cmdline_f2 = CmdLineFactCollector()

    cmdline_f1.collect()
    cmdline_f2.collect()

    assert("cmdline" in cmdline_f1.fact_ids)
    assert("proc_cmdline" in cmdline_f2.fact_ids)

# Generated at 2022-06-13 02:33:50.975976
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import CollectorsRegistry
    from ansible.module_utils.facts import get_fact_names
    from ansible.module_utils.facts import get_facts
    from ansible.module_utils.facts.utils import remove_fact
    from ansible.module_utils.facts.utils import set_fact

    # Note: If we do not use remove_fact, the test can fail if run after other tests
    # that have added facts
    remove_fact("cmdline")
    remove_fact("proc_cmdline")

    # Test 1: Run collect() without data and check the result
    set_fact("/proc/cmdline", "")
    collectors_registry = CollectorsRegistry(None, None)
    collectors_registry.collect()
    assert "cmdline" not in get_

# Generated at 2022-06-13 02:34:01.279224
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    kwargs = {}
    kwargs['module'] = None
    kwargs['collected_facts'] = {}

    # ARRANGE
    class_name = 'CmdLineFactCollector'
    file_name = 'ansible.module_utils.facts.collectors.cmdline'
    CmdLineFactCollector_mock = type(class_name, (object,), {'_get_proc_cmdline': classmethod(lambda cls: 'BOOT_IMAGE'
        '/vmlinuz-4.4.0-72-generic.efi.signed root=UUID=1e825149-8502-4cb2-b72e-fdc0aa8e95a9 ro quiet splash vt.handoff=7')})


# Generated at 2022-06-13 02:34:02.063535
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:34:05.747235
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils._text import to_text

    # Retrieve and parse cmdline
    collector = get_collector_instance(CmdLineFactCollector)
    cmdline_facts = collector.collect()
    cmdline_text = to_text(cmdline_facts, errors='surrogate_then_replace')
    assert cmdline_facts
    assert cmdline_text

# Generated at 2022-06-13 02:34:10.374380
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    '''
    Unit test for method collect of class CmdLineFactCollector
    '''
    file_content = """
BOOT_IMAGE=/vmlinuz-3.10.0-862.2.3.el7.x86_64 root=/dev/mapper/cl-root ro crashkernel=auto rd.lvm.lv=cl/root rd.lvm.lv=cl/swap rhgb console=tty1 console=ttyS0,115200n8 rd.lvm.lv=cl/home
"""

    file_content = file_content.strip()


# Generated at 2022-06-13 02:34:12.188129
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == "cmdline"
    assert CmdLineFactCollector()._fact_ids == set()

# Generated at 2022-06-13 02:34:14.702107
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:35:06.564689
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Test with no data
    cmdline_fc = CmdLineFactCollector()
    cmdline_facts = cmdline_fc._get_proc_cmdline = lambda: None
    assert cmdline_fc.collect() == {}

    # Test with data
    cmdline_fc = CmdLineFactCollector()
    cmdline_data = """
    BOOT_IMAGE=/vmlinuz-3.13.0-24-generic
    root=UUID=e7fcd1c1-1e75-4213-9b61-dce7464c39a4 ro quiet splash vt.handoff=7
    """
    cmdline_fc._get_proc_cmdline = lambda: cmdline_data
    cmdline_facts = cmdline_fc.collect()


# Generated at 2022-06-13 02:35:08.106490
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:35:09.733530
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert(CmdLineFactCollector.name == 'cmdline')
    assert(len(CmdLineFactCollector._fact_ids) is 0)

# Generated at 2022-06-13 02:35:10.186357
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:35:11.442700
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.collect() == None

# Generated at 2022-06-13 02:35:16.353341
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    test_collector = CmdLineFactCollector()

    test_collector._get_proc_cmdline = lambda: 'BOOT_IMAGE=/vmlinuz-4.4.0-150-generic root=/dev/mapper/ubuntu--vg-root ro console=ttyS0,9600n81 rd.udev.log-priority=3 systemd.show_status=true'
    test_cmdline_facts = test_collector.collect()


# Generated at 2022-06-13 02:35:22.053151
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline is not None
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()
    assert cmdline._get_proc_cmdline() is not None
    assert cmdline._parse_proc_cmdline('foo=bar') == {'foo': 'bar'}
    assert cmdline._parse_proc_cmdline('foo=bar baz=qux') == {'foo': 'bar', 'baz': 'qux'}

# Generated at 2022-06-13 02:35:25.426324
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()

    assert cmdline_facts['proc_cmdline']['BOOT_IMAGE'] == '/vmlinuz-4.15.0-29-generic'
    assert cmdline_facts['cmdline']['BOOT_IMAGE'] == '/vmlinuz-4.15.0-29-generic'

# Generated at 2022-06-13 02:35:34.102975
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Create a CmdLineFactCollector
    cmdline_fact_collector = CmdLineFactCollector()

    # Create a mock module
    module = type('', (), {})

    # Return of method _get_proc_cmdline
    cmdline_fact_collector._get_proc_cmdline = lambda: 'BOOT_IMAGE=/boot/vmlinuz-3.10.0-693.eeval.el7.x86_64 root=UUID=909b5c5b-7aa1-4a25-91fb-6068b4a4a1c4 ro crashkernel=auto rhgb quiet LANG=en_US.UTF-8 real_init=/usr/lib/systemd/systemd'

    # Return of method _parse_proc_cmdline
    cmdline_fact_collector._parse_proc_

# Generated at 2022-06-13 02:35:40.813929
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = """root=/dev/disk/by-id/scsi-360a98000437504632334f454a31343130-part3 console=tty0 console=ttyS0,115200 rw init=/usr/lib/systemd/systemd rootwait
    """
    # Define the module class and name for the test

    class TestModule:
        pass

    TestModule.__name__ = 'ansible.module_utils.facts.system.cmdline.CmdLineFactCollector'

    # Instantiate the module class
    cmdline_collector = CmdLineFactCollector()

    # Results of the method execution
    results = cmdline_collector.collect(module=TestModule())
    assert results

    # Verify that kernel is present in the results
    assert 'cmdline' in results
    # Verify that kernel_release is

# Generated at 2022-06-13 02:37:30.877347
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()
    assert isinstance(cmdline_facts, dict)
    assert 'cmdline' in cmdline_facts
    assert 'proc_cmdline' in cmdline_facts
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)
    return cmdline_facts

# Generated at 2022-06-13 02:37:35.923231
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    class TestModule(object):
        pass

    obj = CmdLineFactCollector()
    obj._get_proc_cmdline = lambda self: "BOOT_IMAGE=(hd0,gpt1)/vmlinuz-4.4.0-21-generic root=UUID=6a5e5d5d-e040-49a7-b263-3f3c1d52c1f8 ro rootflags=subvol=@"
    result = obj.collect(module=TestModule())


# Generated at 2022-06-13 02:37:37.260921
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert not collector._fact_ids

# Generated at 2022-06-13 02:37:39.397796
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert isinstance(obj, CmdLineFactCollector)

# Generated at 2022-06-13 02:37:47.491998
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Unit tests for the method collect of the class CmdLineFactCollector"""
    cmdlineFactCollector = CmdLineFactCollector()

    # __init__
    assert cmdlineFactCollector is not None

    from ansible.module_utils.facts.utils import get_file_content
    # _get_proc_cmdline
    # This method will return the content of /proc/cmdline
    assert cmdlineFactCollector._get_proc_cmdline() is not None

    # _parse_proc_cmdline
    # This method will return a dictionary where the key is the first
    # argument before the equal sign and the value is the rest of the
    # argument after the equal sign
    assert cmdlineFactCollector._parse_proc_cmdline('foo=bar') == {'foo':'bar'}

    # _parse_proc_

# Generated at 2022-06-13 02:37:49.893389
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline', 'Test CmdLineFactCollector constructor failed!'
    assert not cmdline_fact_collector._fact_ids, 'Test CmdLineFactCollector constructor failed!'


# Generated at 2022-06-13 02:37:57.433626
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import collector
    import mock

    mock_open = mock.mock_open(read_data='console=ttyS0 \
console=ttyAMA0,115200n8r root=/dev/mmcblk0p2 rw rootwait \
rootfstype=ext4 elevator=deadline')
    mock_get_file_content = mock.Mock(return_value='console=ttyS0 \
console=ttyAMA0,115200n8r root=/dev/mmcblk0p2 rw rootwait \
rootfstype=ext4 elevator=deadline')


# Generated at 2022-06-13 02:38:01.598040
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector != None

# Generated at 2022-06-13 02:38:02.900940
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert isinstance(CmdLineFactCollector(), BaseFactCollector)


# Generated at 2022-06-13 02:38:11.780258
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector
    collector = CmdLineFactCollector()

    # Set File /proc/cmdline
    collector._get_proc_cmdline = lambda: 'ro root=UUID=4b9a9e56-f6ee-479d-a5c7-1f2bdda76630'

    # Run collect
    result = collector.collect()

    # Check result