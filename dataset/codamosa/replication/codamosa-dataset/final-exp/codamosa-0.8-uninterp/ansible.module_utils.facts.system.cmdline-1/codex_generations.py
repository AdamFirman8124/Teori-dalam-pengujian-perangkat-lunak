

# Generated at 2022-06-13 02:30:19.962688
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'

# Generated at 2022-06-13 02:30:25.638738
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    variable_manager = MagicMock()
    loader = MagicMock()
    variable_manager.get_vars.return_value = {}
    variable_manager.extra_vars = {}
    cmdline = CmdLineFactCollector(loader=loader, variable_manager=variable_manager)
    cmdline.collect()
    variable_manager.get_vars.assert_called_with(loader=None, play=None)



# Generated at 2022-06-13 02:30:30.073523
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import json

    module = None
    collected_facts = {}
    fact_collector = CmdLineFactCollector()

    cmdline_facts = fact_collector.collect(module, collected_facts)
    cmdline_facts_json = json.dumps(cmdline_facts)
    print(cmdline_facts_json)

# Generated at 2022-06-13 02:30:33.880008
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    my_obj = CmdLineFactCollector()
    my_obj._get_proc_cmdline = lambda: "rdinit=/sbin/init ro"
    cmdline_facts = my_obj.collect()
    assert cmdline_facts['proc_cmdline'] == {}
    assert cmdline_facts['cmdline'] == {'rdinit': '/sbin/init', 'ro': True}

# Generated at 2022-06-13 02:30:40.814970
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    module = MockModule()
    base_facts = {}
    cmdline_facts_collector = CmdLineFactCollector(module=module, collected_facts=base_facts)

    cmdline_facts_collector._get_proc_cmdline = Mock(return_value='ip=192.168.1.1 netmask=255.255.255.0 gateway=192.168.1.254')
    cmdline_facts_collector._parse_proc_cmdline = Mock(return_value={'ip': '192.168.1.1', 'netmask': '255.255.255.0', 'gateway': '192.168.1.254'})

# Generated at 2022-06-13 02:30:42.450834
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    coll = CmdLineFactCollector()
    assert coll.name == 'cmdline'


# Generated at 2022-06-13 02:30:44.359823
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    print(CmdLineFactCollector())



# Generated at 2022-06-13 02:30:46.192904
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_instance = CmdLineFactCollector()
    assert cmdline_instance is not None

# Generated at 2022-06-13 02:30:47.941749
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert 'cmdline' == cmdline_facts.name

# Generated at 2022-06-13 02:30:57.453321
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Create new instance of CmdLineFactCollector
    cmd_line_fact_collector = CmdLineFactCollector()

    # Parse command line
    cmdline_facts = cmd_line_fact_collector.collect()

    # Check if command line was parsed correctly
    assert isinstance(cmdline_facts, dict)
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)
    assert cmdline_facts['cmdline']['quiet'] == True
    assert cmdline_facts['proc_cmdline']['quiet'] == True

# Generated at 2022-06-13 02:31:03.564371
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj=CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:31:05.651197
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    Cfg = CmdLineFactCollector(None, None)

    assert Cfg.name == 'cmdline'
    assert Cfg._fact_ids == set()


# Generated at 2022-06-13 02:31:15.682664
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = """BOOT_IMAGE=/vmlinuz-4.4.0-53-generic root=UUID=507d15d4-4c21-4f24-a638-a6d443f7c8a3 ro
    console=ttyS0,38400n8 console=tty1 net.ifnames=0 biosdevname=0 quiet
    """
    cmdline_facts = {}


# Generated at 2022-06-13 02:31:25.435065
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class mock_get_file_content():
        def __init__(self, data):
            self.data = data

        def __call__(self, file_path):
            return self.data

    class mock_cmdline_collector():
        def __init__(self):
            self.test_data = None
            self.test_result = None

        def _get_proc_cmdline(self):
            return mock_get_file_content(self.test_data)

        def _parse_proc_cmdline(self, data):
            return data

        def _parse_proc_cmdline_facts(self, data):
            return data

        def collect(self):
            self.test_result = self._parse_proc_cmdline(self.test_data)
            return self.test_result


# Generated at 2022-06-13 02:31:27.749630
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector_ins = CmdLineFactCollector()
    cmdline_facts = cmdline_collector_ins.collect()
    assert isinstance(cmdline_facts, dict)

# Generated at 2022-06-13 02:31:34.332908
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.pycompat24 import mock

    module = mock.MagicMock()
    collected_facts = dict()
    cmdline_collector = CmdLineFactCollector(module=module, collected_facts=collected_facts,
                                             ansible_facts=dict())
    cmdline_collector.collect()


if __name__ == '__main__':
    test_CmdLineFactCollector_collect()

# Generated at 2022-06-13 02:31:37.055314
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert fact_collector.name == "cmdline"
    assert fact_collector._fact_ids == set()
    assert isinstance(fact_collector, CmdLineFactCollector)


# Generated at 2022-06-13 02:31:44.201007
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    class MockFile(object):
        def __init__(self, content):
            self.content = content

        def read(self):
            return self.content

    from ansible.module_utils.facts.utils import mock_open
    from ansible.module_utils.facts import collector

    base_collector = collector.BaseFactCollector()
    base_collector._cache = {}
    base_collector._cache_by_collector = {}

    data = 'root=/dev/sda1 ro console=tty0 console=ttyS0,9600n8 ip=dhcp'
    with mock_open(MockFile(data)):
        cmdline_col = CmdLineFactCollector()
        cmdline_facts = cmdline_col.collect(base_collector.get_collection(cmdline_col.name))

   

# Generated at 2022-06-13 02:31:47.236336
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    x = CmdLineFactCollector()
    assert x.name == 'cmdline'

# Generated at 2022-06-13 02:31:50.138873
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFactCollector = CmdLineFactCollector()
    assert cmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:32:02.445549
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import fact_collector

    # Testing with expected cmdline data
    cmdline_data = "clock=apic console=ttyS0,115200 nofault32 no-hlt no-real-mode no-remap reboot=bios rw root=LABEL=admin init=/bin/bash net.ifnames=0 biosdevname=0 BOOT_IMAGE=/mnt/openwrt/openwrt.img"

# Generated at 2022-06-13 02:32:04.011501
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # unit test for constructor
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 02:32:04.846912
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert isinstance(CmdLineFactCollector(), CmdLineFactCollector)

# Generated at 2022-06-13 02:32:05.458710
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:32:06.795743
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_obj = CmdLineFactCollector({})
    assert cmdline_obj

# Generated at 2022-06-13 02:32:08.701277
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    # Check if the object is instance of object CmdLineFactCollector
    assert isinstance(obj, CmdLineFactCollector)

# Generated at 2022-06-13 02:32:10.807250
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:32:21.252926
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_data = 'BOOT_IMAGE=/boot/vmlinuz-3.10.0-327.18.2.el7.x86_64 '\
                   'root=/dev/mapper/rhel-root ro crashkernel=auto '\
                   'console=tty0 console=ttyS0,115200n8 crashkernel=auto '\
                   'console=tty0 console=ttyS0,115200n8 '\
                   'rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap LANG=en_US.UTF-8'

    cmdline_facts = CmdLineFactCollector().collect({})
    # the expected format of the cmdline facts is a dict with two keys:
    # cmdline (dict) and proc_cmdline (dict). Let's just test the first one

# Generated at 2022-06-13 02:32:28.999261
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import collector
    collector.collector.add(CmdLineFactCollector())
    cmdline_facts = collector.collector.collect(module=None, collected_facts=None)
    assert isinstance(cmdline_facts, dict)
    assert 'cmdline' in cmdline_facts
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert 'proc_cmdline' in cmdline_facts
    assert isinstance(cmdline_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:32:33.067626
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Unit test for method CmdLineFactCollector.collect
    """

    import tempfile
    import os

    ############################################################################
    # Test 1: test_CmdLineFactCollector_collect_no_file

    # Create a temporary file to use for /proc/cmdline
    file_fd, file_path = tempfile.mkstemp()
    with os.fdopen(file_fd, 'w') as file_handle:
        file_handle.write("this is /proc/cmdline data")

    # Test the results when /proc/cmdline does not exist.
    my_cmdline = CmdLineFactCollector()
    result = my_cmdline.collect()
    assert result == {}, "Expected empty dict, got %s" % str(result)

    # Remove the temporary file

# Generated at 2022-06-13 02:32:49.345820
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    proc_cmdline_data = 'BOOT_IMAGE=/vmlinuz-3.10.0-957.5.1.el7.x86_64 root=UUID=d6e338ee-5ef9-43fc-8b69-e4e46545e4c4 ro crashkernel=auto resume=UUID=e99b3972-04f8-4b54-a581-7f59d1b96a8b rhgb quiet console=tty1 console=ttyS0,115200n8 initrd=/initramfs-3.10.0-957.5.1.el7.x86_64.img'

# Generated at 2022-06-13 02:32:53.836305
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:32:55.384559
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    assert c.collect() == {}

# Generated at 2022-06-13 02:32:58.433968
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """
    Test constructor of class CmdLineFactCollector

    Arguments:
        None

    Returns:
        None

    Raises:
        None
    """

    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline', 'name mismatch'
    assert collector._fact_ids == set(), '_fact_ids mismatch'

# Generated at 2022-06-13 02:33:01.032610
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:33:03.094671
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:33:04.875345
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    gf = CmdLineFactCollector()
    v = gf.collect()
    assert v['cmdline']['nofb'] == True

# Generated at 2022-06-13 02:33:07.062342
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts.name == "cmdline"


# Generated at 2022-06-13 02:33:07.592506
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:33:08.898359
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'

# Generated at 2022-06-13 02:33:28.300619
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'

# Generated at 2022-06-13 02:33:32.131456
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector("")
    result = cmdline_collector.collect()
    assert result['cmdline']['ansible_test'] == 'test'
    assert result['proc_cmdline']['ansible_test'] == 'test'

# Generated at 2022-06-13 02:33:40.726559
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os
    from ansible.module_utils.facts import FactCollector

    os.environ['ANSIBLE_CACHE_PLUGIN'] = 'jsonfile'
    os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION'] = '/tmp'

    # test with empty file
    fd = open('/tmp/ansible.fact', 'w')
    fd.write('{}')
    fd.close()
    CmdLineFactCollector.collect(None)
    fd = open('/tmp/ansible.fact', 'r')
    data = fd.read()
    fd.close()
    facts = eval(data)
    assert facts == {'cmdline': {}, 'proc_cmdline': {}}

    # test with valid file

# Generated at 2022-06-13 02:33:44.104348
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'

# Generated at 2022-06-13 02:33:45.508487
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector.collect() == {}

# Generated at 2022-06-13 02:33:53.101890
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    parameter_list = [
        'selinux=0',
        'driver=nfs',
        'rhgb',
        'quiet',
        'ipv6.disable=1',
        'LANG=en_US.UTF-8',
        'boot=boot1 boot2',
        'boot1',
        'boot2',
    ]

# Generated at 2022-06-13 02:34:02.234044
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fixture = CmdLineFactCollector()

    fixture._get_proc_cmdline = lambda: '''
        BOOT_IMAGE=/boot/vmlinuz-2.6.32-642.el6.x86_64 root=UUID=516dd442-d832-4cbe-a1a1-f3d3e3cb1236 ro
        crashkernel=auto rhgb quiet LANG=en_US.UTF-8
        console=ttyS1,115200n8 console=tty0
        '''

    # Fact `cmdline` should not contain lists
    collected_facts = fixture.collect()
    assert not isinstance(collected_facts['cmdline'], list)

    # Fact `proc_cmdline` should contain lists

# Generated at 2022-06-13 02:34:03.973004
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fc = CmdLineFactCollector()
    assert cmd_line_fc.name == 'cmdline'
    assert not cmd_line_fc._fact_ids


# Generated at 2022-06-13 02:34:08.968170
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Test function:
    - Get cmdline facts

    """
    # Generate data
    data = 'ro console=ttyAMA0,38400n8 console=ttyAMA0,38400n8\
            BOOT_IMAGE=/boot/vmlinuz-4.9.0-3-amd64 root=/dev/md2\
            ro rdblacklist=nouveau elevator=deadline'

    # Create instance of class CmdLineFactCollector
    cmdline_fact_collector = CmdLineFactCollector()

    # Collect cmdline facts
    actual_cmdline_facts = cmdline_fact_collector.collect()

    # Generate expected cmdline facts

# Generated at 2022-06-13 02:34:18.971252
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    test_cmdline = "rd.luks.uuid=luks-bae1edc2-5587-4adf-b375-ecadc9e61cd9 " \
                   "rd.lvm.lv=fedora/swap " \
                   "rd.lvm.lv=fedora/root " \
                   "rhgb quiet"
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector._get_proc_cmdline = lambda: test_cmdline
    facts = cmdline_collector.collect()

    assert isinstance(facts['cmdline'], dict)
    assert isinstance(facts['proc_cmdline'], dict)
    assert facts['cmdline']['rhgb']
    assert facts['cmdline']['quiet']


# Generated at 2022-06-13 02:35:07.716370
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import six
    from ansible.module_utils._text import to_bytes
    import os
    import pytest
    from ansible_collections.community.general.tests.unit.compat.mock import patch
    from ansible_collections.community.general.plugins.modules.system.nxos.facts import (
        CmdLineFactCollector,
    )
    from ansible_collections.community.general.plugins.modules.system.nxos.facts.cmdline import get_file_content

    # Build mock data

# Generated at 2022-06-13 02:35:14.014140
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """ Test method collect of class CmdLineFactCollector
    """

    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    import pytest
    from ansible_collections.ansible.netcommon.plugins.module_utils.facts.collector.cmdline import test_CmdLineFactCollector_data

    collector = CmdLineFactCollector()
    cmdline_data = collector._get_proc_cmdline()

    if cmdline_data:
        result = collector._parse_proc_cmdline_facts(cmdline_data)
        test_result = collector._parse_proc_cmdline_facts(test_CmdLineFactCollector_data.CMDLINE_DATA)
        assert result == test_result

# Generated at 2022-06-13 02:35:16.021581
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    if cmdline_fact_collector:
        pass


# Generated at 2022-06-13 02:35:23.998397
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    '''Test that CmdLineFactCollector.collect returns correct values and parses correctly'''

    # Import here since this depends on a file
    from ansible.module_utils.facts.collector import Collector

    # Create a Collector and build the facts
    collector = Collector()
    collector.collect(filter_facts=False)
    facts = collector.get_facts()

    # Get the test data
    test_data = get_file_content('./test/unittests/cmdline_data.txt')

    # Parse the test data
    cmdline_facts = {}
    cmdline_facts['cmdline'] = {}
    cmdline_facts['proc_cmdline'] = {}
    for piece in shlex.split(test_data, posix=False):
        item = piece.split('=', 1)

# Generated at 2022-06-13 02:35:26.099352
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd = CmdLineFactCollector()
    assert cmd.name == 'cmdline'
    assert isinstance(cmd._fact_ids, set)
    assert len(cmd._fact_ids) == 0
    assert cmd._aliases == {}


# Generated at 2022-06-13 02:35:28.262185
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector

# Generated at 2022-06-13 02:35:32.300366
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    text = 'This is my text'
    with open('/proc/cmdline', 'w') as fw:
        fw.write(text)
    CmdLineFactCollector().collect()
    with open('/proc/cmdline') as fr:
        text_new = fr.read()
    assert text == text_new, 'Unit test for method collect of class CmdLineFactCollector failed.'

# Generated at 2022-06-13 02:35:39.395353
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Unit test for CmdLineFactCollector.collect
    """
    # Orginal data
    data = "rd.lvm.lv=fedora/swap rd.lvm.lv=fedora/root " \
    "rhgb quiet LANG=en_US.UTF-8 rd.shell=0 rd.lvm.lv=fedora/home"

    # Parse data

# Generated at 2022-06-13 02:35:40.413132
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.collect()

# Generated at 2022-06-13 02:35:42.688811
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name=='cmdline'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 02:37:33.148734
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    hostvars = {}
    cmdline_dict = {'a': 'b', 'c': 'd', 'e': True, 'f': 'g'}
    cmdline_facts_dict = {'a': 'b', 'c': 'd', 'e': True, 'f': ['g', 'h', 'i']}

    test_obj = CmdLineFactCollector()
    test_obj.hostvars = hostvars

    # data is None
    test_obj._get_proc_cmdline = lambda: None
    res = test_obj.collect()
    assert res == {}

    # data is not None
    test_obj._get_proc_cmdline = lambda: " ".join(['{}={}'.format(k, v) for k, v in cmdline_dict.items()])
    res = test_

# Generated at 2022-06-13 02:37:40.568535
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import ansible.module_utils.facts.collector as facts_collector

    cmdline_facts_collector_obj = facts_collector.get_collector('cmdline')
    assert isinstance(cmdline_facts_collector_obj, CmdLineFactCollector)

    # this will call module setup in all collectors
    facts_collector.setup_collectors()
    cmdline_facts = cmdline_facts_collector_obj.collect()
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:37:48.389724
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fc = CmdLineFactCollector()

# Generated at 2022-06-13 02:37:49.800888
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()

# Generated at 2022-06-13 02:37:52.282096
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()
    assert isinstance(c, BaseFactCollector)


# Generated at 2022-06-13 02:37:58.165401
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector

    # Create an instance of class CmdLineFactCollector for testing
    test_CmdLineFactCollector = CmdLineFactCollector()

    # Create instance of dummy class for testing
    test_base_fact_collector = BaseFactCollector()

    # Create mock for method 'get_file_content'
    def get_file_content_mock(key):
        return 'selinux=0'

    # Set return value of method 'get_file_content' to mock value
    test_CmdLineFactCollector.get_file_content = get_file_content_mock

    # Execute method 'collect'
    result = test_CmdLineFactCollector.collect()

    # Assert method 'collect' returns dictionary
    assert isinstance(result, dict)

# Generated at 2022-06-13 02:38:02.539808
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'
    assert CmdLineFactCollector()._fact_ids == set()

# Generated at 2022-06-13 02:38:03.072571
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:38:04.541233
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector is not None


# Generated at 2022-06-13 02:38:08.194412
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert 'cmdline' in collector._fact_ids
    assert 'proc_cmdline' in collector._fact_ids