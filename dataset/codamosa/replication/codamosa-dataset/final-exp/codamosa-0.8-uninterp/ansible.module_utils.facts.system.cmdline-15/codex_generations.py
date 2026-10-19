

# Generated at 2022-06-13 02:30:20.589558
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'

# Generated at 2022-06-13 02:30:23.325800
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line = CmdLineFactCollector()
    assert cmd_line.name == 'cmdline'
    assert not cmd_line._fact_ids
    assert not cmd_line.facts


# Generated at 2022-06-13 02:30:26.247746
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    cmd_collector = CmdLineFactCollector()
    assert cmd_collector.name == 'cmdline'


# Generated at 2022-06-13 02:30:27.922396
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'

# Generated at 2022-06-13 02:30:29.494078
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    tmp = CmdLineFactCollector()
    assert tmp
    assert tmp.name == 'cmdline'

# Generated at 2022-06-13 02:30:37.322738
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class TestModule:
        def __init__(self):
            self._ansible_module = True

    class TestCollector(CmdLineFactCollector):
        def _get_proc_cmdline(self):
            return "ansible_foo='bar' foo bar 'ansible_fizz=buzz'"

    class TestData:
        pass

    test_module = TestModule()
    test_data = TestData()
    test_collector = TestCollector(test_module, test_data)
    
    result = test_collector.collect()

    assert isinstance(result, dict)
    assert 'cmdline' in result
    assert isinstance(result['cmdline'], dict)
    assert 'ansible_foo' in result['cmdline']
    assert result['cmdline']['ansible_foo'] == 'bar'

# Generated at 2022-06-13 02:30:41.550837
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fact_collector = CmdLineFactCollector()
    assert cmd_line_fact_collector.name == 'cmdline'
    assert cmd_line_fact_collector._fact_ids == set()
    assert cmd_line_fact_collector._get_proc_cmdline() == ''

# Generated at 2022-06-13 02:30:42.113172
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert True

# Generated at 2022-06-13 02:30:46.194316
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'


# Test case to test the method _get_proc_cmdline in the class CmdLineFactCollector

# Generated at 2022-06-13 02:30:50.115939
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    # The following will return None as /proc/cmdline may not be available in unit tests.
    # This will be skipped by ansible in fact_collector() function.
    assert cmdline_fact_collector.collect() == {}

# Generated at 2022-06-13 02:31:00.762752
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Test to read command line arguments from proc/cmdline when it has data
    def mock_get_proc_cmdline(data):
        return data

    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = mock_get_proc_cmdline
    data = 'ro root=LABEL=root-1  rhgb quiet'

    assert collector._parse_proc_cmdline(data) == {'rhgb': 'quiet', 'root': 'LABEL=root-1', 'ro': True}

# Generated at 2022-06-13 02:31:01.941389
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fc = CmdLineFactCollector()
    assert fc.collect() == {}

# Generated at 2022-06-13 02:31:02.804034
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    assert CmdLineFactCollector().collect()

# Generated at 2022-06-13 02:31:04.120809
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd = CmdLineFactCollector()
    assert cmd.name == 'cmdline'

# Generated at 2022-06-13 02:31:15.268832
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import collector_registry
    from ansible.module_utils.facts import FactManager
    from ansible.module_utils._text import to_bytes

    cmdline = 'root=/dev/mapper/VolGroup-LogVol00 rd_NO_LUKS  KEYBOARDTYPE=pc   KEYTABLE=us  rd_NO_MD  SYSFONT=latarcyrheb-sun16 crashkernel=auto   rd_NO_LVM  LANG=en_US.UTF-8  console=tty0 console=ttyS0,115200'
    cmd_line_collector = CmdLineFactCollector()

    with open('/tmp/cmdline_test.txt', 'wb') as f:
        f.write(to_bytes(cmdline))

    # execute

# Generated at 2022-06-13 02:31:16.153333
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:31:23.841900
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    test_collector = CmdLineFactCollector()
    cmdline_facts = test_collector.collect()

    assert isinstance(cmdline_facts['cmdline'], dict)
    assert 'console' in cmdline_facts['cmdline']
    assert isinstance(cmdline_facts['cmdline']['console'], basestring)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)
    assert 'console' in cmdline_facts['proc_cmdline']
    assert isinstance(cmdline_facts['proc_cmdline']['console'], basestring)

# Generated at 2022-06-13 02:31:29.137891
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = {}

    data = get_file_content('/proc/cmdline')
    if not data:
        return cmdline_facts

    cmdline_facts['cmdline'] = CmdLineFactCollector._parse_proc_cmdline(data)
    cmdline_facts['proc_cmdline'] = CmdLineFactCollector._parse_proc_cmdline_facts(data)

    return cmdline_facts

# Generated at 2022-06-13 02:31:29.905373
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()

# Generated at 2022-06-13 02:31:35.613191
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmd_line_value = "root=/dev/mapper/rhel-root ro rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rd.md.uuid=bebe8527:03f6a1be:da1f99a8:8cd2e3db rhgb quiet"
    expected_cmdline_dict = {
        'root': '/dev/mapper/rhel-root',
        'ro': True,
        'rd.lvm.lv': ['rhel/root', 'rhel/swap'],
        'rd.md.uuid': 'bebe8527:03f6a1be:da1f99a8:8cd2e3db',
        'rhgb': True,
        'quiet': True,
    }
    expected_proc

# Generated at 2022-06-13 02:31:45.387469
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert False


# Generated at 2022-06-13 02:31:55.211745
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import sys
    from tempfile import TemporaryFile
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Create temporary file /proc/cmdline used in this test
    proc_cmdline = TemporaryFile()
    proc_cmdline.write(b'test=False test2=True test3=2 test4="toto" test5=" aaa bbb=ccc ddd \\"'
                       b'eee \\"fff" test6=" aaa bbb=ccc ddd \\ eee \\ fff" test7=1 test7=2 test7=3')

    # Define mock module class with temporary file
    class MockModule:
        def __init__(self, tmp_file):
            self.tmp_file = tmp_file

# Generated at 2022-06-13 02:32:02.802418
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os
    import json
    import sys
    import uuid
    import tempfile
    from ansible.module_utils.facts import collector

    # We find the first usable /proc/cmdline
    proc_cmdline = '/proc/cmdline'
    for test_cmdline in ['/proc/cmdline-not-there', '/no/such/path', '/etc/hosts']:
        if os.path.isfile(test_cmdline):
            proc_cmdline = test_cmdline
            break

    test_data = 'key1=value1 key2 key3 key4=value4=too-long key5=value5 key6="value 6"'

# Generated at 2022-06-13 02:32:09.408991
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():

    temp_file_name = "/tmp/temp_file"
    temp_file = open(temp_file_name, "w")
    temp_file.write("foo=bar bar=baz")
    temp_file.close()
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector._get_proc_cmdline = lambda : get_file_content(temp_file_name)
    cmdline_dict = cmdline_collector._parse_proc_cmdline(get_file_content(temp_file_name))
    
    assert (cmdline_dict['foo'] == 'bar'
            and cmdline_dict['bar'] == 'baz')

# Generated at 2022-06-13 02:32:12.849856
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == 'set()'

# Generated at 2022-06-13 02:32:16.438273
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Test constructor of class CmdLineFactCollector
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

#
# Unit tests for method get_proc_cmdline()
#

# Generated at 2022-06-13 02:32:17.476484
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert set(collector._fact_ids) == set()

# Generated at 2022-06-13 02:32:18.160160
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:32:19.689588
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'


# Generated at 2022-06-13 02:32:21.728712
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Test with no arguments passed
    test_obj = CmdLineFactCollector()
    assert test_obj.name == 'cmdline'
    assert test_obj._fact_ids == set()

# Generated at 2022-06-13 02:32:46.909057
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from os.path import isfile
    cmdline_data = 'ansible=True random_data=1'
    with open('/proc/cmdline', 'w') as cmdline_file:
        cmdline_file.write(cmdline_data)
        cmdline_file.close()

    cmdline_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_collector.collect()

    assert cmdline_facts.get('cmdline') == {'ansible': 'True', 'random_data': '1'}
    assert cmdline_facts.get('proc_cmdline') == {'ansible': 'True', 'random_data': '1'}

    # Removing fake /proc/cmdline
    try:
        os.remove('/proc/cmdline')
    except:
        pass

# Generated at 2022-06-13 02:32:47.324345
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    pass

# Generated at 2022-06-13 02:32:58.434088
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = {}

    data = """BOOT_IMAGE=/vmlinuz-3.10.0-957.1.3.el7.x86_64 root=UUID=5b5d5c5e-6f50-4e28-b17f-c2d58ef8e4e4 rhgb quiet LANG=en_US.UTF-8
    """

    if not data:
        return cmdline_facts

    cmdline_facts['cmdline'] = {}
    cmdline_facts['proc_cmdline'] = {}


# Generated at 2022-06-13 02:33:01.033213
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert isinstance(CommandLineFactCollector(), CommandLineFactCollector)


# Generated at 2022-06-13 02:33:03.712725
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fc = CmdLineFactCollector()
    assert cmdline_fc.name == 'cmdline'
    assert cmdline_fc._fact_ids == set()

# Generated at 2022-06-13 02:33:04.593877
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert hasattr(CmdLineFactCollector, 'collect')

# Generated at 2022-06-13 02:33:07.182220
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()


# Generated at 2022-06-13 02:33:09.079695
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == "cmdline"
    assert collector._fact_ids == set()


# Generated at 2022-06-13 02:33:15.436273
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Given a CmdLineFactCollector instance
    c = CmdLineFactCollector()

    # When I call method collect
    facts = c._get_proc_cmdline()

    # Then a dict is returned
    assert True is isinstance(facts, dict)

    # And it contains the following keys
    assert True is isinstance(facts['cmdline'], dict)
    assert True is isinstance(facts['proc_cmdline'], dict)
    assert True is isinstance(facts['proc_cmdline']['audit'], str)
    assert True is isinstance(facts['proc_cmdline']['crashkernel'], str)
    assert True is isinstance(facts['proc_cmdline']['rd.lvm.lv'], list)

# Generated at 2022-06-13 02:33:19.869725
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Case1: When data is None
    class TestArgs:
        def __init__(self, data):
            self.data = data

    class TestClass:
        def __init__(self, data):
            self.args = TestArgs(data)

        def get_file_content(self, filename):
            return self.args.data

    test_obj = TestClass('')
    cmdline_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_collector.collect(module=test_obj)
    cmdline_facts_exp = {}
    assert cmdline_facts == cmdline_facts_exp

    # Case2: When data is populated
    test_content = 'rw root=/dev/mapper/system-root ro init=/usr/lib/systemd/systemd'
    test_obj

# Generated at 2022-06-13 02:33:54.268900
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():

    obj = CmdLineFactCollector()


# Generated at 2022-06-13 02:33:56.858802
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdlineFactCollector = CmdLineFactCollector()
    assert cmdlineFactCollector.name == 'cmdline'
    assert cmdlineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:34:04.656154
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_collector.collect()

    assert cmdline_facts['cmdline'] == {'root': '/dev/sda3',
                                        'ro': True,
                                        'LANG': 'en_US.UTF-8',
                                        'rhgb': True,
                                        'quiet': True,
                                        'vconsole.keymap': 'uk'}
    assert cmdline_facts['proc_cmdline'] == {'root': '/dev/sda3',
                                             'ro': True,
                                             'LANG': ['en_US.UTF-8'],
                                             'rhgb': True,
                                             'quiet': True,
                                             'vconsole.keymap': 'uk'}

# Generated at 2022-06-13 02:34:08.255875
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class ModuleStub:
        pass

    import os.path
    proc_cmdline_file = os.path.join('..', 'files', 'cmdline_sample')

    class CmdLineFactCollectorStub(CmdLineFactCollector):
        def _get_proc_cmdline(self):
            return get_file_content(proc_cmdline_file)

    module = ModuleStub()
    collector = CmdLineFactCollectorStub()
    cmdline_facts = collector.collect(module=module, collected_facts=None)

    assert cmdline_facts["cmdline"]["quiet"] is True
    assert cmdline_facts["cmdline"]["radeon.dpm"] == "1"
    assert cmdline_facts["cmdline"]["selinux"] is True

# Generated at 2022-06-13 02:34:10.895397
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cfc = CmdLineFactCollector()
    assert cfc.name == 'cmdline'
    assert cfc._fact_ids == set()


# Generated at 2022-06-13 02:34:13.465455
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:34:23.557149
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    data = [{'key': 'root', 'val': 'LABEL=cloudimg-rootfs'},
            {'key': 'root', 'val': 'LABEL=cloudimg-rootfs'},
            {'key': 'ro', 'val': True},
            {'key': 'init', 'val': '/usr/lib/systemd/systemd'},
            {'key': 'quiet', 'val': True},
            {'key': 'selinux', 'val': True}]

    def get_file_content(filename):
        if filename == '/proc/cmdline':
            return 'root=LABEL=cloudimg-rootfs root=LABEL=cloudimg-rootfs ro init=/usr/lib/systemd/systemd quiet selinux=1'
        else:
            return ''

    result = dict()

# Generated at 2022-06-13 02:34:25.699528
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'

# Generated at 2022-06-13 02:34:33.014698
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class test:
        def __init__(self, content=None):
            self.content = content

    def get_file_content(*args, **kwargs):
        return content

    content = 'ip=10.10.10.11 ro'

    test_obj = test()
    test_obj.content = content

    fac = CmdLineFactCollector()

    # monkey patch
    fac.get_file_content = get_file_content

    result = fac.collect()

    assert 'cmdline' in result
    assert 'proc_cmdline' in result

    assert result['cmdline'] == {'ro': True, 'ip': '10.10.10.11'}
    assert result['proc_cmdline'] == {'ro': True, 'ip': '10.10.10.11'}

# Generated at 2022-06-13 02:34:34.384313
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Method collect should correctly return the value of /proc/cmdline to the caller
    assert True

# Generated at 2022-06-13 02:35:58.477070
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    def mock_get_file_content(file_path, default=None):
        return 'test_value'
    def mock_parse_cmdline_facts(data):
        return {'test_key': 'test_value'}

    CmdLineFactCollector._get_proc_cmdline = mock_get_file_content
    CmdLineFactCollector._parse_proc_cmdline_facts = mock_parse_cmdline_facts
    cmdline_facts = CmdLineFactCollector().collect()
    assert cmdline_facts['proc_cmdline'] == {'test_key': 'test_value'}

# Generated at 2022-06-13 02:36:00.695087
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdlinefact = CmdLineFactCollector()
    assert cmdlinefact.name == 'cmdline'
    assert isinstance(cmdlinefact._fact_ids, set)
    assert len(cmdlinefact._fact_ids) == 0

# Generated at 2022-06-13 02:36:03.014670
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = CmdLineFactCollector.collect()
    assert isinstance(cmdline_facts, dict)


# Generated at 2022-06-13 02:36:04.425995
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'


# Generated at 2022-06-13 02:36:09.416888
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    with open('/proc/cmdline', 'w') as f:
        f.write("initrd=initrd.img")
    facts = c.collect()
    assert 'cmdline' in facts
    assert 'proc_cmdline' in facts
    assert facts['cmdline'] == {'initrd': 'initrd.img'}
    assert facts['proc_cmdline'] == {'initrd': 'initrd.img'}

# Generated at 2022-06-13 02:36:15.453116
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import CollectorExecutionError
    from ansible.module_utils.facts.collector import get_collector
    cmdline_fc = get_collector('CmdLineFactCollector')
    # _get_proc_cmdline
    cmdline_fc._get_proc_cmdline = lambda x: "abc=123"
    # _parse_proc_cmdline
    cmdline_fc._parse_proc_cmdline = lambda x: {'abc': '123'}
    # _parse_proc_cmdline_facts
    cmdline_fc._parse_proc_cmdline_facts = lambda x: {'abc': '123'}

    assert cmdline_fc.collect() == {'cmdline': {'abc': '123'}, 'proc_cmdline': {'abc': '123'}}

# Generated at 2022-06-13 02:36:22.092948
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # object for class CmdLineFactCollector
    test_cmdline_obj = CmdLineFactCollector()

    # mock function _get_proc_cmdline()
    test_cmdline_obj._get_proc_cmdline = lambda: 'root=UUID=6a58abcb-b89c-4f86-bd57-d5c8129a6f52 ro quiet vga=0x317 initrd=initrd.img-3.13.0-32-generic intel_pstate=disable'

    # calling method collect of class CmdLineFactCollector
    result = test_cmdline_obj.collect()

    # assert result of method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:36:24.826511
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert isinstance(CmdLineFactCollector._get_proc_cmdline, object)
    assert isinstance(CmdLineFactCollector._parse_proc_cmdline, object)
    assert isinstance(CmdLineFactCollector._parse_proc_cmdline_facts, object)

# Generated at 2022-06-13 02:36:31.932349
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:36:39.839505
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = {}

    data = None
    cmdline_facts['cmdline'] = {}
    cmdline_facts['proc_cmdline'] = {}

    assert CmdLineFactCollector().collect(collected_facts=None) == cmdline_facts

    data = 'root=/dev/sda1 ro'
    cmdline_facts['cmdline'] = {
        'root': '/dev/sda1',
        'ro': True
    }
    cmdline_facts['proc_cmdline'] = {
        'root': '/dev/sda1',
        'ro': True
    }
    assert CmdLineFactCollector().collect(collected_facts=None) == cmdline_facts


# Generated at 2022-06-13 02:40:05.117913
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()

    assert cmdline_facts['cmdline'] == {'console': 'ttyS0,115200', 'root': '/dev/sda1', 'rootfstype': 'ext4', 'rw': True, 'quiet': True}
    assert cmdline_facts['proc_cmdline'] == {'console': 'ttyS0,115200', 'root': '/dev/sda1', 'rootfstype': 'ext4', 'rw': True, 'quiet': True}

# Generated at 2022-06-13 02:40:06.614123
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector(None)
    assert cmdline_facts
    assert isinstance(cmdline_facts, CmdLineFactCollector)

# Generated at 2022-06-13 02:40:11.462327
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmd_line_collector = CmdLineFactCollector()
    cmd_line_facts = cmd_line_collector.collect()
    cmd_line_dict = cmd_line_facts['cmdline']
    assert cmd_line_dict
    assert 'root' in cmd_line_dict
    assert 'BOOT_IMAGE' in cmd_line_dict
    assert 'console=tty0' in cmd_line_dict
    assert 'console' in cmd_line_dict
    assert cmd_line_dict['console'] == 'tty0'
    assert cmd_line_dict['BOOT_IMAGE'] == '/boot/vmlinuz-2.6.32-431.el6.x86_64'
    assert cmd_line_dict['root'] == '/dev/mapper/vg_rhel-lv_root'

# Generated at 2022-06-13 02:40:20.779471
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Class CmdLineFactCollector is defined inside class CmdLineFactCollector
    # in module ansible.module_utils.facts.collector. There is no easy way to
    # access CmdLineFactCollector class outside class CmdLineFactCollector
    # (without changing its code). Class CmdLineFactCollector is based on
    # BaseFactCollector and there is no method collect in BaseFactCollector.
    # Hence, mocking class CmdLineFactCollector with class BaseFactCollector.
    mock_CmdLineFactCollector = BaseFactCollector

    # No need to mock class BaseFactCollector

    # Mocking method _get_proc_cmdline and mocking return value of method
    # _get_proc_cmdline