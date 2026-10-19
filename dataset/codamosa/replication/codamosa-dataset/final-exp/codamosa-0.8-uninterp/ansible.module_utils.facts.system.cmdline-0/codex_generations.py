

# Generated at 2022-06-13 02:30:18.998442
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'

# Generated at 2022-06-13 02:30:29.011818
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:30:31.052370
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    tm = CmdLineFactCollector()
    assert tm.name == 'cmdline'
    assert  tm._fact_ids == set()

# Generated at 2022-06-13 02:30:38.688892
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = {}

    collector = CmdLineFactCollector()


# Generated at 2022-06-13 02:30:49.920280
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    def _get_file_content_mock(path):
        return "BOOT_IMAGE=/vmlinuz-4.4.0-31-generic root=UUID=47d2acf1-414e-46a7-a006-1d1b56c0c9e9 ro console=tty1 console=ttyS0"
    get_file_content_mock = _get_file_content_mock
    data = get_file_content_mock('/proc/cmdline')
    cmdline_facts = CmdLineFactCollector().collect()
    assert isinstance(cmdline_facts, dict)
    assert 'cmdline' in cmdline_facts
    assert 'proc_cmdline' in cmdline_facts

# Generated at 2022-06-13 02:30:52.251073
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'

# Generated at 2022-06-13 02:30:54.788511
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()

# Generated at 2022-06-13 02:30:57.181674
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fact_collector = CmdLineFactCollector()
    assert isinstance(cmd_line_fact_collector, CmdLineFactCollector)


# Generated at 2022-06-13 02:30:59.449787
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    my_CmdLineFactCollector = CmdLineFactCollector()

    assert my_CmdLineFactCollector.name == 'cmdline'

test_CmdLineFactCollector()

# Generated at 2022-06-13 02:31:00.941171
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector.collect()

# Generated at 2022-06-13 02:31:14.761450
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    cmdline_facts = c.collect()

    assert 'cmdline' in cmdline_facts
    assert 'proc_cmdline' in cmdline_facts
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)


# Generated at 2022-06-13 02:31:15.766041
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import mock
    fact_collector = CmdLineFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 02:31:18.557248
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Tested with fake proc file
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert isinstance(collector._fact_ids, set)

# Generated at 2022-06-13 02:31:24.701400
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector(None, None)

    if not cmdline_fact_collector:
        raise Exception("Failed to create CmdLineFactCollector")

    if cmdline_fact_collector.name != 'cmdline':
        raise Exception("cmdline_fact_collector.name is not 'cmdline'")

    if not cmdline_fact_collector._fact_ids:
        raise Exception("cmdline_fact_collector._fact_ids is empty")


# Generated at 2022-06-13 02:31:31.084528
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = {}
    data = 'ansible_facts={"some_fact": "some_value"}'
    cmdline_facts['cmdline'] = {'ansible_facts': '{"some_fact": "some_value"}'}
    cmdline_facts['proc_cmdline'] = {'ansible_facts': '{"some_fact": "some_value"}'}
    collector = CmdLineFactCollector
    collector._get_proc_cmdline = lambda: data
    result = collector.collect()
    assert result == cmdline_facts


# Generated at 2022-06-13 02:31:40.722282
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    _collector = CmdLineFactCollector()
    data = "root=/dev/mapper/vg00-root.img ro rd_NO_LUKS KEYBOARDTYPE=pc KEYTABLE=us rd_NO_MD rd_NO_LVM rd_NO_DM LANG=en_US.utf8 SYSFONT=latarcyrheb-sun16 crashkernel=auto rhgb quiet rd.lvm.lv=vg00/swap rd.lvm.lv=vg00/root audit=1 initrd=boot/initramfs-0.el6.x86_64.img"

# Generated at 2022-06-13 02:31:42.009285
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()


# Generated at 2022-06-13 02:31:46.487962
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Given
    # When
    res = cmdline_fact_collector.collect()

    # Then
    assert 'cmdline' in res
    assert isinstance(res['cmdline'], dict)
    assert 'proc_cmdline' in res
    assert isinstance(res['proc_cmdline'], dict)

cmdline_fact_collector = CmdLineFactCollector()

# Generated at 2022-06-13 02:31:48.169654
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector


# Generated at 2022-06-13 02:31:55.547370
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector
    collector = CmdLineFactCollector()
    results = collector.collect()

    assert results['cmdline']['ip'] == '172.16.0.1'
    assert results['cmdline']['gateway'] == '172.16.0.254'
    assert results['proc_cmdline']['ip'] == '172.16.0.1'
    assert results['proc_cmdline']['gateway'] == '172.16.0.254'


# Generated at 2022-06-13 02:32:21.803041
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Creating an instance of class CmdLineFactCollector
    cmdline_fact_collector_obj = CmdLineFactCollector()

    # Call method collect of class CmdLineFactCollector
    cmdline_facts = cmdline_fact_collector_obj.collect()

    # Asserting equality

# Generated at 2022-06-13 02:32:32.115808
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Test the collect method of CmdLineFactCollector
    """
    expected = {'cmdline': {'console': 'ttyS', 'key': 'value', 'no_key': True}, 'proc_cmdline': {'console': ['ttyS'], 'key': ['value'], 'no_key': True}}

    # Create an mock of the class CmdLineFactCollector
    cmdline_fact_collector = CmdLineFactCollector()
    # Create a mock of the method _get_proc_cmdline
    cmdline_fact_collector._get_proc_cmdline = lambda: 'console=ttyS key=value no_key'
    # Run the method collect
    result = cmdline_fact_collector.collect()

    assert result == expected

# Generated at 2022-06-13 02:32:32.653371
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:32:36.498561
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Test constructor of CmdLineFactCollector
    cmdline_fact_collector = CmdLineFactCollector()

    assert cmdline_fact_collector.name == "cmdline"
    assert cmdline_fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:32:40.056724
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Setup
    collector = CmdLineFactCollector()

    # Act
    collected_facts = collector.collect()

    # Assert
    assert isinstance(collected_facts, dict)
    assert isinstance(collected_facts['cmdline'], dict)
    assert isinstance(collected_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:32:41.906758
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'


# Generated at 2022-06-13 02:32:47.966256
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.collect.__name__ == 'collect'
    assert CmdLineFactCollector.name == 'cmdline'
    assert isinstance(CmdLineFactCollector._fact_ids, set)
    assert CmdLineFactCollector._get_proc_cmdline.__name__ == '_get_proc_cmdline'
    assert CmdLineFactCollector._parse_proc_cmdline.__name__ == '_parse_proc_cmdline'
    assert CmdLineFactCollector._parse_proc_cmdline_facts.__name__ == '_parse_proc_cmdline_facts'

# Generated at 2022-06-13 02:32:57.104247
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = "root=UUID=67faa474-f0cd-478d-b198-9dd382666a37"
    cmdline_facts = {}

    cmdline_facts['cmdline'] = {'root': 'UUID=67faa474-f0cd-478d-b198-9dd382666a37'}
    cmdline_facts['proc_cmdline'] = {'root': 'UUID=67faa474-f0cd-478d-b198-9dd382666a37'}

    assert CmdLineFactCollector().collect(None, None) == cmdline_facts

# Generated at 2022-06-13 02:32:58.484740
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:33:02.973179
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:33:29.096530
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Test class CmdLineFactCollector
    """
    # Create an instance of class CmdLineFactCollector using the constructor
    # test_proc_cmdline_obj is used to access protected methods
    test_cmdline_obj = CmdLineFactCollector()

    # Used to access protected methods
    class MockCmdLineFactCollector(CmdLineFactCollector):
        def __init__(self):
            CmdLineFactCollector.__init__(self)

        def _get_proc_cmdline(self):
            return 'rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet'

    dummy_cmdline_fact_data = MockCmdLineFactCollector()

    # Create an instance of a class for parameter 'module'

# Generated at 2022-06-13 02:33:30.794502
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:33:39.791834
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    cmdline_collector = CmdLineFactCollector()
    new_cmdline = 'ro root=/dev/mapper/vg_xen-lv_root rd_NO_LUKS  KEYBOARDTYPE=pc  KEYTABLE=us LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=auto rd_LVM_LV=vg_xen/lv_swap rd_LVM_LV=vg_xen/lv_root  rd_NO_DM rhgb quiet audit=1'
    cmdline_collector._get_proc_cmdline = lambda: new_cmdline
    facts = cmdline_collector.collect()

# Generated at 2022-06-13 02:33:40.834621
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:33:50.909611
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()

    def fake_get_proc_cmdline():
        return 'ro root=/dev/mapper/vg_tsv-lv_root rd_LVM_LV=vg_tsv/lv_root rd_LVM_LV=vg_tsv/lv_swap rd_NO_LUKS rd_NO_MD rd_NO_DM LANG=en_US.UTF-8 SYSFONT=latarcyrheb-sun16 KEYBOARDTYPE=pc KEYTABLE=us crashkernel=128M rhgb quiet'

    def fake_parse_proc_cmdline(data):
        cmdline_dict = {}
        for piece in shlex.split(data, posix=False):
            item = piece.split('=', 1)

# Generated at 2022-06-13 02:33:58.864693
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    assert c.collect() == {'cmdline': {}, 'proc_cmdline': {}}

    c = CmdLineFactCollector(module=None, collected_facts={})
    assert c.collect() == {'cmdline': {}, 'proc_cmdline': {}}

    c = CmdLineFactCollector(module=None, collected_facts={'ansible_facts': {'cmdline': {}, 'proc_cmdline': {}}})
    assert c.collect() == {'cmdline': {}, 'proc_cmdline': {}}

# Generated at 2022-06-13 02:34:00.272004
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'


# Generated at 2022-06-13 02:34:05.523423
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Check for empty content
    cmd_line_string = ''
    cmd_line_dict = will_be_returned_by(CmdLineFactCollector._parse_proc_cmdline).when.called_with(cmd_line_string)
    cmd_line_facts = will_be_returned_by(CmdLineFactCollector._parse_proc_cmdline_facts).when.called_with(cmd_line_string)
    will_be_returned_by(CmdLineFactCollector._get_proc_cmdline).when.called_with().be(cmd_line_string)
    cmd_line_collector = CmdLineFactCollector()

    cmd_line_data = cmd_line_collector.collect()


# Generated at 2022-06-13 02:34:07.019343
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # unit test for collect method of class CmdLineFactCollector
    l = []

    c = CmdLineFactCollector(l)
    facts = c.collect()

    assert 'cmdline' in facts.keys()
    assert 'proc_cmdline' in facts.keys()

# Generated at 2022-06-13 02:34:09.112549
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:34:52.645240
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact = CmdLineFactCollector()

    # cmdline fact not found
    cmdline_fact._get_proc_cmdline = lambda: None
    assert cmdline_fact.collect() == {}

    # cmdline fact availible
    _get_cmdline = lambda: ' BOOT_IMAGE=/vmlinuz-3.13.0-24-generic root=/dev/mapper/ubuntu-root ro console=tty1 console=ttyS0'
    cmdline_fact._get_proc_cmdline = _get_cmdline


# Generated at 2022-06-13 02:34:54.610709
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()


# Generated at 2022-06-13 02:35:02.829730
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils import basic

    testobj = CmdLineFactCollector()

    all_facts = testobj.collect()

    # results should be dict type
    assert isinstance(all_facts, dict)

    # results should have key 'cmdline'
    assert "cmdline" in all_facts and \
           isinstance(all_facts['cmdline'], dict)

    # results should have key 'proc_cmdline'
    assert "proc_cmdline" in all_facts and \
           isinstance(all_facts['proc_cmdline'], dict)


# Generated at 2022-06-13 02:35:10.772897
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Set cmdline as read from /proc/cmdline
    # (the expected values)
    cmdline = "BOOT_IMAGE=/boot/vmlinuz-4.4.0-21-generic \
        root=UUID=40ce3aa3-7b69-4a1a-8cc6-c85369f89b6e ro quiet splash"

    # Call the collect method of CmdLineFactCollector
    cmdline_facts = CmdLineFactCollector().collect()

    # Get the fact 'proc_cmdline'
    # (the actual result)
    actual_cmdline = cmdline_facts['proc_cmdline']

    # Get a list of the key-value pairs from the cmdline string
    key_value_pairs = cmdline.split(" ")

    # Compare the actual and expected results
    #

# Generated at 2022-06-13 02:35:12.666573
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:35:14.829774
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    f = CmdLineFactCollector(None)

    assert f.name == "cmdline"
    assert f._fact_ids == set()

# Generated at 2022-06-13 02:35:23.340742
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    collected_facts = collector.collect()


# Generated at 2022-06-13 02:35:28.718466
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector

    # Create an instance of CmdLineFactCollector
    cmdline_instance = CmdLineFactCollector()

    # Get the results of running collect method
    results = cmdline_instance.collect()

    # Make sure the result is not None or empty dict
    assert(results and results != {})

    # Make sure the result of collect method is a dict
    assert(isinstance(results, dict))

    # Make sure the result of collect method is the same as expected

# Generated at 2022-06-13 02:35:30.422200
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector._fact_ids == set()
    assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:35:37.737360
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    cmdline_fact_collector = FactCollector.fact_collector['cmdline']

    cmdline_fact_collector._get_proc_cmdline = lambda: 'vconsole.font=latarcyrheb-sun16 vconsole.keymap=us root=/dev/mapper/linux-root rw rootflags=subvol=@ boot=zfs zfs_pool=linux zfs_root=/@ zfs_root_mountpoint=/ zfs_force=1 initrd=/boot/intel-ucode.img initrd=/boot/initramfs-linux.img'

    facts = cmdline_fact_collector.collect()

    assert facts['cmdline']['vconsole.font'] == 'latarcyrheb-sun16'

# Generated at 2022-06-13 02:37:24.358960
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import random
    import string
    import sys
    import tempfile
    import os

    def randomString(stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    num_of_items = random.randint(0,100)
    cmdline_string = str()
    cmdline_dict = {}
    cmdline_facts_dict = {}

    fd, temp_proc_cmdline_file_path = tempfile.mkstemp()
    
    for i in range(num_of_items):
        item = randomString()
        value = randomString()
        cmdline_dict[item] = value

# Generated at 2022-06-13 02:37:31.134064
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    '''Unit test for method collect of class CmdLineFactCollector'''

    cmdline_facts = CmdLineFactCollector().collect()
    expected_facts_cmdline = {'cmdline': {'root': '/dev/vda1', 'rw': True, 'console': 'ttyS0,115200n8'}}
    expected_facts_proc_cmdline = {'proc_cmdline': {'root': '/dev/vda1', 'rw': True, 'console': 'ttyS0,115200n8'}}

    assert cmdline_facts == expected_facts_cmdline
    assert cmdline_facts == expected_facts_proc_cmdline

# Generated at 2022-06-13 02:37:32.467009
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'

# Generated at 2022-06-13 02:37:33.923530
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fc = CmdLineFactCollector()
    assert fc.name == 'cmdline'



# Generated at 2022-06-13 02:37:36.602289
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()

    assert c.name == 'cmdline'
    assert len(c._fact_ids) == 0


# Generated at 2022-06-13 02:37:45.462036
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    test_input = 'BOOT_IMAGE=/vmlinuz-4.6.0-1.el7.elrepo.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap  rhgb quiet'

# Generated at 2022-06-13 02:37:46.558895
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:37:48.116890
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:37:49.774053
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()


# Generated at 2022-06-13 02:37:57.433298
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from io import StringIO

    mocked_paths = [
            '/proc/cmdline',
        ]

    mocked_files = {
            '/proc/cmdline': StringIO("""
            root=/dev/sda1
            ro
            console=ttyS0,115200
            earlyprintk=ttyS0,115200
            reboot=a,b
            consoleblank=0
            net.ifnames=0
            biosdevname=0
            hwaddress=DE:AD:BE:CC:DE:01
            hwaddress=DE:AD:BE:CC:DE:02
            hwaddress=DE:AD:BE:CC:DE:03
            """)
        }
