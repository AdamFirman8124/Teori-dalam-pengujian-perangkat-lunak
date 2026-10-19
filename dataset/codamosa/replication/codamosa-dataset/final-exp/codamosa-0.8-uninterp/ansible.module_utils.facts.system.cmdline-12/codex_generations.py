

# Generated at 2022-06-13 02:30:18.233502
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    coll = CmdLineFactCollector()
    assert coll.name == 'cmdline'

# Generated at 2022-06-13 02:30:28.146378
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest

    from ansible.module_utils.facts.utils import FactsCollector

    class Mock(unittest.TestCase):

        def _get_proc_cmdline(self):
            return 'ansible_test_param=ansible_test_value'

    mock = Mock()

    collector = CmdLineFactCollector(mock)

    cmdline_facts = collector.collect()

    assert(mock._get_proc_cmdline.called)

# Generated at 2022-06-13 02:30:35.353664
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import collect_subset, get_collector_instance

    facts_dict = {}
    cmdline_fact_collector = get_collector_instance('CmdLineFactCollector')

    facts_dict.update(cmdline_fact_collector.collect())

    assert 'cmdline' in facts_dict
    assert 'proc_cmdline' in facts_dict
    assert 'root' in facts_dict['proc_cmdline']
    assert 'rd.lvm.lv' in facts_dict['proc_cmdline']
    assert 'rd.lvm.lv' in facts_dict['cmdline']


# Generated at 2022-06-13 02:30:37.251957
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = CmdLineFactCollector().collect()

    assert cmdline_facts['cmdline']
    assert cmdline_facts['proc_cmdline']

# Generated at 2022-06-13 02:30:48.395390
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    import sys
    import os
    import stat

    # Create a temporary file for proc_cmdline
    (fd, temp_path) = tempfile.mkstemp(
            prefix='/proc/cmdline',
            text=True)
    os.chmod(temp_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP)

    # Write something to the file
    os.write(fd, 'ansible_test=1 ansible_foo=bar')
    os.close(fd)
    os.environ['ANSIBLE_UNIT_TESTING'] = '1'

    # Instantiate the collector
    collector = CmdLineFactCollector()
    results = collector.collect()

    # Delete proc_file
    os.unlink(temp_path)
    del os

# Generated at 2022-06-13 02:30:49.661233
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Run constructor
    CmdLineFactCollector()


# Generated at 2022-06-13 02:30:59.856166
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    cmdline_facts = {}
    cmdline_facts['cmdline'] = {'foo': 'bar', 'baz': True, 'quux': 'foo', 'quux': 'bar'}
    cmdline_facts['proc_cmdline'] = {'foo': 'bar', 'baz': True, 'quux': ['foo', 'bar']}

    class FakeModule:
        pass

    class FakeFactCollector:

        def get_file_content(self, file_path):
            return 'foo=bar baz quux=foo quux=bar'

    fc = FakeFactCollector()
    cmdline_cc = CmdLineFactCollector(module=FakeModule(), facts={})

    fc.parse_proc_cmdline = cmdline_cc._parse_proc_cmdline
    fc.parse_proc_cmdline

# Generated at 2022-06-13 02:31:07.593716
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector.get_file_content = lambda path: 'BOOT_IMAGE=/boot/vmlinuz-4.4.0-122-generic root=UUID=8a905c59-7e42-4a3d-8d90-bfd0e3241e4d ro quiet'
    cmdline_facts = cmdline_collector.collect()
    assert 'cmdline' in cmdline_facts

# Generated at 2022-06-13 02:31:18.363110
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import platform
    from ansible.module_utils.facts import collector

    # create a new CmdLineFactCollector instance
    cmd_line_fc = CmdLineFactCollector()

    # create a fake Platform object
    class Platform:
        name = platform.system()
        distro_name = platform.linux_distribution()[0]
        distro_major_version = platform.linux_distribution()[1]
        distro_version = platform.linux_distribution()[1]
        version_like = ''
        platform = Platform.name
        machine = platform.machine()
        release = platform.release()
        system = Platform.name
        processor = platform.processor()
        virtual = ''
        virtual_subtype = ''

    # create a new PlatformFactCollector instance

# Generated at 2022-06-13 02:31:27.355488
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    mock_data = 'console=tty0 console=ttyS0,9600n8 root=/dev/mapper/vg1-rootlv ro net.ifnames=0 biosdevname=0 elevator=noop'

    collector = CmdLineFactCollector()

# Generated at 2022-06-13 02:31:39.330581
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fake_cmdline = open("/tmp/fake_cmdline", "w")
    fake_cmdline.write("BOOT_IMAGE=/vmlinuz-4.4.0-31-generic root=UUID=6e829f70-797c-4b6c-b197-8b93dd92c24d ro quiet splash vt.handoff=7")
    fake_cmdline.close()
    collector = CmdLineFactCollector()
    result = collector._get_proc_cmdline()
    assert result == "BOOT_IMAGE=/vmlinuz-4.4.0-31-generic root=UUID=6e829f70-797c-4b6c-b197-8b93dd92c24d ro quiet splash vt.handoff=7"
    collector = CmdLineFactCollector

# Generated at 2022-06-13 02:31:40.247550
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fc = CmdLineFactCollector()
    assert cmdline_fc.name == 'cmdline'


# Generated at 2022-06-13 02:31:41.825890
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'
    assert CmdLineFactCollector()._fact_ids == set([])

# Generated at 2022-06-13 02:31:43.281991
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()
    assert x.name == 'cmdline'
    assert x._fact_ids == set()


# Generated at 2022-06-13 02:31:46.161129
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    if c is None:
        raise AssertionError("CmdLineFactCollector() returned None")


# Generated at 2022-06-13 02:31:48.510767
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_dict = CmdLineFactCollector().collect()
    assert cmdline_dict['cmdline'] == {}
    assert cmdline_dict['proc_cmdline'] == {}

# Generated at 2022-06-13 02:31:51.229096
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_factscollector = CmdLineFactCollector()

test_CmdLineFactCollector()

# Generated at 2022-06-13 02:31:59.452276
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    test_data = 'BOOT_IMAGE=/kernel-3.10.0-123.el7.x86_64 root=UUID=473c04a6-eb8c-4cfa-a9a9-d0f9c865a6ca ro crashkernel=auto LANG=en_US.UTF-8 rhgb quiet transparent_hugepage=never'

# Generated at 2022-06-13 02:32:03.472695
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()

    # Assert object is instance of BaseFactCollector
    assert isinstance(cmdline_facts, BaseFactCollector)

    # Assert properties
    assert cmdline_facts.name == 'cmdline'
    assert cmdline_facts._fact_ids == set()

# Generated at 2022-06-13 02:32:04.124430
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:32:21.801454
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fake_module = None
    fake_collected_facts = None

# Generated at 2022-06-13 02:32:25.878305
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    ofc = CmdLineFactCollector()
    output = ofc.collect()
    assert "ansible_cmdline" in output
    assert "ansible_proc_cmdline" in output

# Generated at 2022-06-13 02:32:35.760565
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    import tempfile
    import shell

    # Write fake /proc/cmdline
    (handle, fake_cmdline) = tempfile.mkstemp(prefix='ansible_test_fake_cmdline_', text=True)

    fake_cmdline_data = "hello=world # this is a comment\nfoo=bar\nbar=\n"

    with open(fake_cmdline, "w") as f:
        f.write(fake_cmdline_data)

    # Create shell object
    sh = shell.Shell()

    # Create FactsCollector object
    fc = FactsCollector(sh, junk_name=True)

    # Add CmdLineFactCollector to FactsCollector object
    fc.collectors = [CmdLineFactCollector]

# Generated at 2022-06-13 02:32:45.048291
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    r_cmdline={'audit': '1', 'mem': '1G', 'rhel': '7', 'cgroup_enable': 'memory swap'}
    r_proc_cmdline={'audit': '1', 'mem': '1G', 'rhel': [True, '7'], 'cgroup_enable': ['memory', 'swap']}

    c = CmdLineFactCollector()
    proc_cmdline = c._get_proc_cmdline()
    cmdline_facts = c.collect()

    assert cmdline_facts == {'cmdline': r_cmdline, 'proc_cmdline': r_proc_cmdline}
    assert cmdline_facts['cmdline'] == r_cmdline
    assert cmdline_facts['cmdline']['audit'] == r_cmdline['audit']

# Generated at 2022-06-13 02:32:50.128988
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    no_data = {}
    c = CmdLineFactCollector()

    data_1 = 'initrd=initrd.img-4.9.0-8-amd64  console=ttyS0,115200n8'
    c.get_file_content = lambda x: data_1

    assert c.collect() == {'cmdline': {'initrd': 'initrd.img-4.9.0-8-amd64',
                                       'console': 'ttyS0,115200n8'},
                           'proc_cmdline': {'initrd': 'initrd.img-4.9.0-8-amd64',
                                            'console': 'ttyS0,115200n8'}}


# Generated at 2022-06-13 02:32:58.982693
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import facts_dumper
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import CollectorExecutionError
    from ansible.module_utils.facts.utils import get_file_content

    def get_file_content_mock(path):
        if path == '/proc/cmdline':
            return "ro rootflags=subvol=@/test/snapshots/1 net.ifnames=0 biosdevname=0 elevator=noop"
        else:
            raise Exception("Unexpected call to get_file_content")

    def append_collector(collection=[], collector=None):
        collection.append(collector)

    collected_facts = {}
    collectors = []

    cmdline_fact_collector = CmdLineFactCollect

# Generated at 2022-06-13 02:33:01.677575
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == "cmdline"

# Generated at 2022-06-13 02:33:10.130879
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    def _get_proc_cmdline(self):
        return 'root=UUID=12345-678-90 boot=UUID=abcde-fg-hijk ro'

    collector = CmdLineFactCollector()

    collector._get_proc_cmdline = _get_proc_cmdline

    result = collector.collect()

    assert result == {
        'cmdline': {
            'root': 'UUID=12345-678-90',
            'boot': 'UUID=abcde-fg-hijk',
            'ro': True
        },
        'proc_cmdline': {
            'root': 'UUID=12345-678-90',
            'boot': 'UUID=abcde-fg-hijk',
            'ro': True
        }
    }

# Generated at 2022-06-13 02:33:10.829653
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:33:12.340789
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:33:22.718372
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:33:25.703021
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts is not None
    assert cmdline_facts._fact_ids == set()
    assert cmdline_facts._name == 'cmdline'


# Generated at 2022-06-13 02:33:27.119249
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert len(c._fact_ids) == 0


# Generated at 2022-06-13 02:33:32.213920
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # create an instance of class SystemdFactCollector
    my_obj = CmdLineFactCollector()

    # check type of object
    assert isinstance(my_obj, CmdLineFactCollector)

    # check value of attribute 'name'
    assert my_obj.name == 'cmdline'

    # check value of attribute '_fact_ids'
    assert my_obj._fact_ids == set()

# Generated at 2022-06-13 02:33:34.005313
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact = CmdLineFactCollector()
    assert cmdline_fact is not None


# Generated at 2022-06-13 02:33:35.291353
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:33:42.842259
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    cmdline_collector = CmdLineFactCollector()

    # test one line
    cmdline_dict = cmdline_collector._parse_proc_cmdline("foo=bar")
    assert cmdline_dict == {'foo': 'bar'}

    cmdline_facts = cmdline_collector._parse_proc_cmdline_facts("foo=bar")
    assert cmdline_facts == {'foo': 'bar'}

    # test multiple lines
    cmdline_dict = cmdline_collector._parse_proc_cmdline("foo=bar boz=baz")
    assert cmdline_dict == {'foo': 'bar', 'boz': 'baz'}

    cmdline_facts = cmdline_collector._parse

# Generated at 2022-06-13 02:33:48.889916
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert (CmdLineFactCollector().name == 'cmdline')
    assert (CmdLineFactCollector()._fact_ids == set())
    assert (CmdLineFactCollector()._get_proc_cmdline() is not None)
    assert (CmdLineFactCollector()._parse_proc_cmdline_facts("") == {})
    assert (CmdLineFactCollector()._parse_proc_cmdline("") == {})
    assert (CmdLineFactCollector().collect() is not None)

# Generated at 2022-06-13 02:33:58.971144
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class Args:
        pass

    cmdline_collector = CmdLineFactCollector
    cmdline_collector.collect_methods = ['_parse_proc_cmdline']

    # Set up a file with fake data to read
    fake_file_data = 'ro root=/dev/hdb1 foo=bar baz=false'
    (fd, file_path) = tempfile.mkstemp()
    with open(file_path, "w") as f:
        f.write(fake_file_data)
    os.close(fd)

    #  Mock the get_file_content method of CmdLineFactCollector class
    with patch.object(cmdline_collector, '_get_proc_cmdline') as mock_get_cmdline:
        mock_get_cmdline.return_value = fake_file

# Generated at 2022-06-13 02:34:01.493759
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()

    assert cmdline_collector.name == 'cmdline'
    assert isinstance(cmdline_collector, BaseFactCollector)


# Generated at 2022-06-13 02:34:22.533537
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import collector_registry
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    cmdline = CmdLineFactCollector()
    assert collector_registry[cmdline.name] is CmdLineFactCollector
    assert cmdline.collect()

# Generated at 2022-06-13 02:34:30.514489
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Creation of instance of CmdLineFactCollector
    cmdline = CmdLineFactCollector()
    # Test values of name, _fact_ids, _file_paths
    assert cmdline.name == 'cmdline', "Error - test_CmdLineFactCollector(): cmdline.name != 'cmdline'"
    assert cmdline._fact_ids == set(), "Error - test_CmdLineFactCollector(): cmdline._fact_ids != set()"
    assert cmdline._file_paths == set(), "Error - test_CmdLineFactCollector(): cmdline._file_paths != set()"

# Generated at 2022-06-13 02:34:32.526231
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'


# Generated at 2022-06-13 02:34:35.225208
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj.collect() == {'cmdline': {}, 'proc_cmdline': {}}

# Generated at 2022-06-13 02:34:43.242876
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Unit test for method collect of class CmdLineFactCollector"""

    # Define needed mocks
    class MockCMDLineFactCollector():
        def __init__(self):
            self.name = 'cmdline'
            self._get_proc_cmdline_status_error = False
            self._parse_proc_cmdline_status_error = False
            self._parse_proc_cmdline_facts_status_error = False
            self._get_proc_cmdline_return_value = ''
            self._parse_proc_cmdline_return_value = ''
            self._parse_proc_cmdline_facts_retuen_value = ''

        def _get_proc_cmdline(self):
            if self._get_proc_cmdline_status_error:
                raise OSError
            else:
                return

# Generated at 2022-06-13 02:34:44.058118
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:34:48.639399
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Test CmdLineFactCollector.collect"""

    # Arrange
    #
    # Patch out the shlex.split method.
    #
    # We need a function that starts with `split_` and takes the same
    # parameters as shlex.split.
    def split_extended_module_list(module_list):
        if len(module_list) == 2:
            return [module_list[1]]
        return [module_list[2]]

    patch_cmd = 'ansible.module_utils.facts.collectors.cmd_line.shlex.split'
    patch_target = 'ansible.module_utils.facts.collectors.cmd_line.split'
    with patch(patch_cmd, autospec=True, side_effect=split_extended_module_list) as patch_split:
        cmd

# Generated at 2022-06-13 02:34:49.775367
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFactCollector = CmdLineFactCollector()
    assert cmdLineFactCollector is not None


# Generated at 2022-06-13 02:34:50.969394
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    a = CmdLineFactCollector()
    assert a is not None
    assert a.name == 'cmdline'

# Generated at 2022-06-13 02:34:52.924081
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    theCollector = CmdLineFactCollector()
    assert theCollector.collect() == None

# Generated at 2022-06-13 02:35:32.485526
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector is not None
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:35:34.071948
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
  cmdlinefactcollector = CmdLineFactCollector()
  assert cmdlinefactcollector.name == 'cmdline'


# Generated at 2022-06-13 02:35:35.343382
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    base = BaseFactCollector(None)
    assert isinstance(base.collect(), dict)

# Generated at 2022-06-13 02:35:39.692129
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_constructor = CmdLineFactCollector()

    # If the constructor fails to initialize its variables, then the
    # how_to_check attribute will be set to an empty string. If the
    # how_to_check attribute is set to a non-empty string, then the
    # constructor has correctly initialized its variables.
    #
    # @see <a href="https://stackoverflow.com/a/530767">Stackoverflow</a>
    assert cmdline_fact_constructor.name != ''

# Generated at 2022-06-13 02:35:40.820664
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert isinstance(CmdLineFactCollector._fact_ids, set)


# Generated at 2022-06-13 02:35:44.982372
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Arrange
    test_cmdline = 'BOOT_IMAGE=/vmlinuz-3.10.0-229.el7.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap  rhgb quiet LANG=en_US.UTF-8'
    test_cmdline_parser = CmdLineFactCollector()

    # Act
    result = test_cmdline_parser._parse_proc_cmdline(test_cmdline)

    # Assert
    assert result['BOOT_IMAGE'] == '/vmlinuz-3.10.0-229.el7.x86_64'
    assert result['root'] == '/dev/mapper/centos-root'

# Generated at 2022-06-13 02:35:48.169504
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fact_collector = CmdLineFactCollector()
    assert cmd_line_fact_collector.name == 'cmdline'
    assert cmd_line_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:35:48.678312
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    pass

# Generated at 2022-06-13 02:35:57.797563
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'
    assert CmdLineFactCollector()._fact_ids == set()
    assert len(CmdLineFactCollector()._parse_proc_cmdline("root=/dev/mapper/vg_system-lv_root rd_NO_LUKS  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_MD rd_LVM_LV=vg_system/lv_swap SYSFONT=latarcyrheb-sun16 crashkernel=auto rd_NO_DM LANG=en_US.UTF-8  rhgb quiet").keys()) == 16

# Generated at 2022-06-13 02:36:04.341119
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = "BOOT_IMAGE=/boot/vmlinuz-3.10.0-327.18.2.el7.x86_64\n" \
           "root=/dev/mapper/cl-root\n" \
           "ro crashkernel=auto rhgb quiet LANG=en_US.UTF-8\n" \
           "rd.lvm.lv=cl/root\n" \
           "rd.lvm.lv=cl/swap\n" \
           "vt.handoff=7\n"
    collector = CmdLineFactCollector()
    cmdline_facts = collector._parse_proc_cmdline(data)

# Generated at 2022-06-13 02:37:31.392789
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:37:33.788038
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()

    collected_facts = {'ansible_fact_cmdline' : {'cmdline':{}, 'proc_cmdline':{}}}

    # Method get_file_content should return a string in this case
    assert collect_neuros() == collected_facts


# Generated at 2022-06-13 02:37:36.157546
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 02:37:37.193030
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert isinstance(obj.collect(), dict)

# Generated at 2022-06-13 02:37:38.598595
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:37:41.399531
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts.name == 'cmdline'
    assert cmdline_facts._fact_ids == set()


# Generated at 2022-06-13 02:37:48.566834
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # mock class
    class MockCmdLineFactCollector(CmdLineFactCollector):
        def _get_proc_cmdline(self):
            content = """console=ttyS0,9600n8  pcie_pme=off acpi=off root=/dev/ram0 rw  selinux=0 acpi=ht"""
            return content

    cmdline_collector = MockCmdLineFactCollector()
    results = cmdline_collector.collect()

    assert results['cmdline']
    assert results['cmdline'] == {'console': 'ttyS0,9600n8', 'pcie_pme': 'off',
                                  'acpi': 'off', 'root': '/dev/ram0', 'rw': True,
                                  'selinux': '0', 'acpi': 'ht'}

# Generated at 2022-06-13 02:37:49.386463
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector(None).name == 'cmdline'


# Generated at 2022-06-13 02:37:52.488155
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    protected_s = 'protected'
    c = CmdLineFactCollector(protected_s)
    assert c.protected == protected_s
    assert c._fact_ids == set()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:37:53.672265
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == "cmdline"