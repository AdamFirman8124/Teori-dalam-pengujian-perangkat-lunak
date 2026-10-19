

# Generated at 2022-06-13 02:30:21.438878
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Create instance
    obj = CmdLineFactCollector()

    # Check instance
    assert isinstance(obj, CmdLineFactCollector)

# Generated at 2022-06-13 02:30:27.496509
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
  # create a mock for class CmdLineFactCollector
  class MockCmdLineFactCollector:
    def _get_proc_cmdline(self):
      return '/usr/bin/python -v -F'

    def _parse_proc_cmdline(self, data):
      cmdline_dict = {}
      try:
        for piece in shlex.split(data, posix=False):
          item = piece.split('=', 1)
          if len(item) == 1:
            cmdline_dict[item[0]] = True
          else:
            cmdline_dict[item[0]] = item[1]
      except ValueError:
        pass

      return cmdline_dict

    def _parse_proc_cmdline_facts(self, data):
      cmdline_dict = {}

# Generated at 2022-06-13 02:30:28.492723
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector()

if __name__ == '__main__':
    test_CmdLineFactCollector()

# Generated at 2022-06-13 02:30:30.698889
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact = CmdLineFactCollector()
    assert cmdline_fact.name == 'cmdline'

# Generated at 2022-06-13 02:30:38.396442
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:30:40.571234
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline', 'name must be cmdline'

# Generated at 2022-06-13 02:30:42.746133
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdlinefact = CmdLineFactCollector()
    assert isinstance(cmdlinefact, BaseFactCollector)


# Generated at 2022-06-13 02:30:45.806633
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()

# Generated at 2022-06-13 02:30:53.282928
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    class TestModule(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    class TestAnsibleModule(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)


# Generated at 2022-06-13 02:30:55.534825
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector is not None

# Generated at 2022-06-13 02:31:03.894856
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """Unit test for constructor of class CmdLineFactCollector"""
    assert hasattr(CmdLineFactCollector, 'name')
    assert hasattr(CmdLineFactCollector, '_fact_ids')
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:31:14.975854
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    input_cmdline = 'root=UUID=30c5896c-5d5d-47df-a52e-5b8c5d27e5b7 ro console=ttyS0,115200 earlyprintk=ttyS0,115200 ' \
                    'console=tty0 console=ttyS0,115200'

# Generated at 2022-06-13 02:31:24.747099
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # GIVEN a CmdLineFactCollector object and a stub for method _parse_proc_cmdline
    cmdline_facts = {}
    data = 'root=/dev/sda1 console=ttyS0'
    test_object = CmdLineFactCollector()
    test_object._parse_proc_cmdline = lambda data: {'console': 'ttyS0', 'root': '/dev/sda1'}
    test_object._parse_proc_cmdline_facts = lambda data: {'console': ['ttyS0'], 'root': '/dev/sda1'}
    test_object._get_proc_cmdline = lambda: data

    # WHEN running method collect
    cmdline_facts = test_object.collect()

    # THEN assert that a dict is returned

# Generated at 2022-06-13 02:31:26.266163
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 02:31:30.425243
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # pylint: disable=protected-access
    data = 'ipv6.disable=1'

    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = lambda: data

    res = collector.collect()

    assert res['cmdline'] == {'ipv6.disable': '1'}
    assert res['proc_cmdline'] == {'ipv6.disable': '1'}


# Generated at 2022-06-13 02:31:39.997691
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Given: an instance of CmdLineFactCollector and a valid cmdline content
    data = "rd.lvm.lv=centos/swap rd.lvm.lv=centos/root rhgb quiet BOOT_IMAGE=/vmlinuz-3.10.0-327.el7.x86_64 root=/dev/mapper/centos-root ro rd.lvm.lv=centos/swap rd.lvm.lv=centos/root rhgb quiet"
    c = CmdLineFactCollector()
    # When: call method collect
    result = c.collect(None, None)
    # Then: result contains the expected proc_cmdline and cmdline fact and cmdline fact is a list

# Generated at 2022-06-13 02:31:45.905632
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    c._get_proc_cmdline = lambda: 'ansible_check=1 ro crashkernel=auto  rhgb quiet  root=UUID=8a489d99-a9aa-432c-8f86-4ef4e4aa4d55 rd.lvm.lv=fedora/root rd.lvm.lv=fedora/swapselinux=permissive  boot_cpus='
    cmdline_facts = c.collect()
    assert len(cmdline_facts) == 2
    assert isinstance(cmdline_facts, dict)
    assert 'cmdline' in cmdline_facts
    assert 'proc_cmdline' in cmdline_facts
    assert isinstance(cmdline_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:31:50.138768
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()
    assert CmdLineFactCollector.collectors == ['CmdLineFactCollector']


# Generated at 2022-06-13 02:31:56.577961
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact = CmdLineFactCollector()
    result_cmdline = cmdline_fact.collect()
    assert result_cmdline != ''
    assert isinstance(result_cmdline, dict)
    assert result_cmdline['cmdline'] is not None
    assert result_cmdline['cmdline'] != ''
    assert isinstance(result_cmdline['cmdline'], dict)
    assert result_cmdline['proc_cmdline'] is not None
    assert result_cmdline['proc_cmdline'] != ''
    assert isinstance(result_cmdline['proc_cmdline'], dict)

# Generated at 2022-06-13 02:32:03.669135
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    This is a unit test for method collect of class CmdLineFactCollector
    """

    collector = CmdLineFactCollector()
    data = collector._get_proc_cmdline()

    assert collector._parse_proc_cmdline(data) == { 'BOOT_IMAGE': '/boot/vmlinuz-3.10.0-327.18.2.el7.x86_64' }
    assert collector._parse_proc_cmdline_facts(data) == {'BOOT_IMAGE': '/boot/vmlinuz-3.10.0-327.18.2.el7.x86_64'}

    test_result = collector.collect()


# Generated at 2022-06-13 02:32:15.018552
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    test_object = CmdLineFactCollector()

    assert test_object.name is not None
    assert test_object._fact_ids is not None
    assert test_object.collect() is not None


# Generated at 2022-06-13 02:32:18.335460
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()

# Generated at 2022-06-13 02:32:20.122145
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()

# Generated at 2022-06-13 02:32:31.424370
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    data = b'root=/dev/mapper/vg_root-lv_root ro crashkernel=auto LANG=en_US.UTF-8 rd_MD_UUID=d8c1bb6e:2575f3a6:b82d8ad0:739edaf9 rd_NO_LVM rd_NO_DM rhgb quiet SYSFONT=True KEYTABLE=us rd_DM_UUID=b78d7cc1:c2233f7c:6c9a6f8d:c0809a0c rd_LVM_LV=vg_root/lv_root rd_LVM_LV=vg_root/lv_swap'
    cmdline_facts = {}

# Generated at 2022-06-13 02:32:34.861808
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    list_of_facts = CmdLineFactCollector()
    assert list_of_facts.name == 'cmdline'
    assert list_of_facts._fact_ids == set()

# Generated at 2022-06-13 02:32:35.759589
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    CmdLineFactCollector().collect()

# Generated at 2022-06-13 02:32:45.008936
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    # Set example content to /proc/cmdline file
    set_file_content('/proc/cmdline', 'console=ttyS0,115200n8 console=tty0 console=ttyAMA0 root=/dev/hda1 rootfstype=ext4 rootwait noirqdebug pci=noearly')

    # Get expected facts

# Generated at 2022-06-13 02:32:51.127382
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    module = None
    collected_facts = None

    # Create an instance of CmdLineFactCollector
    obj = CmdLineFactCollector()

    # Create a list of dictionaries to use for normalizing different versions of
    # the output from /proc/cmdline

# Generated at 2022-06-13 02:32:55.345397
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert len(collector._fact_ids) == 0
    assert collector.supported_os.get('Linux') == {}



# Generated at 2022-06-13 02:32:58.176834
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert not collector.__dict__.get('_fact_ids')


# Generated at 2022-06-13 02:33:11.272321
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    mock_collector = CmdLineFactCollector()

    proc_cmdline = 'root=/dev/disk/by-uuid/e367f112-6113-45a3-a1b3-c89b9f2b964f' \
                   ' ro quiet splash vt.handoff=7'

    def mock_get_proc_cmdline():
        return proc_cmdline

    mock_collector._get_proc_cmdline = mock_get_proc_cmdline

    result = mock_collector.collect()

    expected = {}

# Generated at 2022-06-13 02:33:21.201149
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:33:24.751145
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'  # Should be cmdline as we are testing CmdLine class
    assert isinstance(collector._fact_ids, set)  # _fact_ids should be a set

# Generated at 2022-06-13 02:33:34.190014
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()

    cmdline_collector._get_proc_cmdline = lambda : 'foo=bar'
    assert cmdline_collector.collect() == {'cmdline': {'foo': 'bar'}, 'proc_cmdline': {'foo': 'bar'}}

    cmdline_collector._get_proc_cmdline = lambda : 'foo'
    assert cmdline_collector.collect() == {'cmdline': {'foo': True}, 'proc_cmdline': {'foo': True}}

    cmdline_collector._get_proc_cmdline = lambda : 'foo bar=baz'

# Generated at 2022-06-13 02:33:42.005718
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fact_collector = CmdLineFactCollector()

    # Test when /proc/cmdline is empty (issue #27077)
    raw_data = ''
    data = fact_collector._parse_proc_cmdline(raw_data)
    assert data == {}
    data = fact_collector._parse_proc_cmdline_facts(raw_data)
    assert data == {}

    # Test when /proc/cmdline doesn't exist (issue #27077)
    raw_data = None
    data = fact_collector._parse_proc_cmdline(raw_data)
    assert data == {}
    data = fact_collector._parse_proc_cmdline_facts(raw_data)
    assert data == {}

    # Test when /proc/cmdline contains "quiet" 

# Generated at 2022-06-13 02:33:44.449355
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    f = CmdLineFactCollector()
    assert f.name == 'cmdline'
    assert f._fact_ids == set()


# Generated at 2022-06-13 02:33:52.366112
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Unit test for method collect of class CmdLineFactCollector"""
    cmd_line_fact_collector = CmdLineFactCollector()


# Generated at 2022-06-13 02:33:54.318635
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    result = CmdLineFactCollector()
    assert result is not None

# Generated at 2022-06-13 02:33:56.582121
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts.name == 'cmdline'
    assert cmdline_facts._fact_ids == set()


# Generated at 2022-06-13 02:33:58.753235
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()
    assert x.name == 'cmdline'
    assert isinstance(x._fact_ids, set)

# Generated at 2022-06-13 02:34:29.380585
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Create a CmdLineFactCollector instance
    instance_CmdLineFactCollector = CmdLineFactCollector()

    # Test the collect method

# Generated at 2022-06-13 02:34:31.809340
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts_collector = CmdLineFactCollector()

    cmdline_facts = cmdline_facts_collector.collect()

    assert 'ansible_cmdline' in cmdline_facts
    assert 'ansible_proc_cmdline' in cmdline_facts

# Generated at 2022-06-13 02:34:34.058853
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    assert isinstance(collector.collect(), dict)

# Generated at 2022-06-13 02:34:36.404513
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()



# Generated at 2022-06-13 02:34:39.854648
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert not cmdline_fact_collector._fact_ids

# Generated at 2022-06-13 02:34:45.609073
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Unit test for method collect of class CmdLineFactCollector
    """
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content
    import ansible.module_utils.facts.__init__ as facts_init
    facts_init.COLLECTORS['CmdLineFactCollector'] = CmdLineFactCollector

    proc_cmdline_data = 'BOOT_IMAGE=/vmlinuz-4.4.0-66-generic root=UUID=b4171d85-4427-4bbe-8d70-d9aec7e06b52 ro quiet splash vt.handoff=7'

    get_file_content_original = get_file_content

# Generated at 2022-06-13 02:34:48.141615
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = CmdLineFactCollector().collect()

    assert isinstance(cmdline_facts, dict)
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:34:53.134101
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
	facts_module = CmdLineFactCollector()
	assert facts_module._get_proc_cmdline() == "BOOT_IMAGE=/boot/vmlinuz-3.16.0-4-amd64 root=UUID=7d199c14-0e8b-4b3a-a08f-c45d640a74e2 ro ipv6.disable=1 iommu=pt quiet rw"
	cmdline_dict = facts_module._parse_proc_cmdline("BOOT_IMAGE=/boot/vmlinuz-3.16.0-4-amd64 root=UUID=7d199c14-0e8b-4b3a-a08f-c45d640a74e2 ro ipv6.disable=1 iommu=pt quiet rw")

# Generated at 2022-06-13 02:35:02.790638
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # create the class
    CmdLineFactCollectorObj = CmdLineFactCollector()

    # set the /proc/cmdline content
    data = 'foo ro BOOT_IMAGE=bar selinux=1'
    CmdLineFactCollectorObj._get_proc_cmdline = lambda: data

    # call the method
    cmdline_facts = CmdLineFactCollectorObj.collect()

    # check the result
    assert cmdline_facts == {'cmdline': {'foo': True, 'ro': True, 'BOOT_IMAGE': 'bar', 'selinux': '1'}, 'proc_cmdline': {'foo': True, 'ro': True, 'BOOT_IMAGE': ['bar'], 'selinux': '1'}}

# Generated at 2022-06-13 02:35:10.745670
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector

    if not os.path.exists('/proc/cmdline'):
        raise unittest.SkipTest("Missing /proc/cmdline")

    data = get_file_content('/proc/cmdline')

    if not data:
        raise unittest.SkipTest("Missing data in /proc/cmdline")

    # Test valid data
    collector = CmdLineFactCollector()
    assert isinstance(collector, BaseFactCollector)
    assert isinstance(collector, Collector)

    cmdline_facts = collector.collect()

# Generated at 2022-06-13 02:36:03.832040
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Construct class instance
    collector = CmdLineFactCollector()

    # Create a test dictionary with command line entries

# Generated at 2022-06-13 02:36:10.017634
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Test with:
    #   /proc/cmdline data
    #   module=None
    #   collected_facts=None
    #
    # Expected:
    #   return cmdline_facts
    #
    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = lambda: 'consoleblank=0 elevator=deadline'
    assert collector.collect() == {'cmdline': {'consoleblank': '0', 'elevator': 'deadline'}, 'proc_cmdline': {'consoleblank': '0', 'elevator': 'deadline'}}

# Generated at 2022-06-13 02:36:11.763475
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    result = collector.collect()
    assert(result['cmdline'])
    assert(result['proc_cmdline'])

# Generated at 2022-06-13 02:36:14.286427
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert hasattr(cmdline,'_fact_ids') == True
    assert isinstance(cmdline._fact_ids, set)
    assert cmdline.collect() == {'cmdline': {}, 'proc_cmdline': {}}

# Generated at 2022-06-13 02:36:16.166002
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:36:22.531932
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Creating instance of CmdLineFactCollector.
    collect_cmd_line = CmdLineFactCollector()

    # Creating instance of MockFile to mock /proc/cmdline file.
    class MockFile(object):
        def __init__(self, name):
            self.name = name

        def read(self):
            return 'root=/dev/sda1 ro selinux=0 loglevel=3 cgroup_enable=memory swapaccount=1'

    # Setting up mocked open() and read() method to mock corresponding methods of class MockFile.
    # Setting up these methods as buit-in functions, so that they can be used in the method collect of class CmdLineFactCollector.
    setattr(__builtins__, 'open', MockFile)
    setattr(MockFile, 'read', MockFile.read)

    #

# Generated at 2022-06-13 02:36:28.525592
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import re
    import tempfile
    import os
    collector_test = CmdLineFactCollector()
    open(collector_test.proc_cmdline_file, 'a').close()
    content = 'ansible_test=test1=test2 ansible_test2=test3'
    with open(collector_test.proc_cmdline_file, 'w') as proc_cmdline:
        proc_cmdline.write(content)
    result = collector_test.collect()
    assert len(result) == 2, "Proc cmdline facts are correct."
    os.unlink(collector_test.proc_cmdline_file)

# Generated at 2022-06-13 02:36:29.851762
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'

# Generated at 2022-06-13 02:36:31.594239
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
   cmdline_collector = CmdLineFactCollector()

   ret = cmdline_collector.collect()

   assert 'cmdline' in ret
   assert 'proc_cmdline' in ret

# Generated at 2022-06-13 02:36:33.019764
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()



# Generated at 2022-06-13 02:38:18.629717
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == "cmdline"
    assert cmdline_collector._fact_ids is not None

# Generated at 2022-06-13 02:38:23.972041
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cfg = CmdLineFactCollector()
    assert cfg.collect() == {}

    cfg = CmdLineFactCollector()
    cfg._get_proc_cmdline = lambda: b'input.ansible_connection=local'
    assert cfg.collect() == {'cmdline': {'input.ansible_connection': 'local'}, 'proc_cmdline': {'input.ansible_connection': 'local'}}

    cfg = CmdLineFactCollector()
    cfg._get_proc_cmdline = lambda: b'input.ansible_connection=local input.ansible_connection=local'
    assert cfg.collect() == {'cmdline': {'input.ansible_connection': 'local'}, 'proc_cmdline': {'input.ansible_connection': ['local', 'local']}}



# Generated at 2022-06-13 02:38:29.070165
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fact_data = CmdLineFactCollector().collect()

    proc_cmdline = fact_data.get('cmdline')
    assert proc_cmdline.get('gpt') == '1'

    cmdline = fact_data.get('proc_cmdline')
    assert cmdline.get('gpt') == '1'



# Generated at 2022-06-13 02:38:39.194173
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    '''
    Test the collect method of class CmdLineFactCollector
    :return:
    '''
    collector = CmdLineFactCollector()

    collect_result = collector.collect()

    assert collect_result is not None
    assert 'cmdline' in collect_result
    assert 'proc_cmdline' in collect_result

    # setup dummy data for both files
    data = 'console=ttyS1,115200n8 quiet splash'
    collector.cmdline_data = data

    collect_result = collector.collect()

    assert collect_result is not None
    assert isinstance(collect_result, dict)
    assert len(collect_result) == 2
    assert 'cmdline' in collect_result
    assert 'proc_cmdline' in collect_result
    assert 'console' in collect_result['cmdline']
   

# Generated at 2022-06-13 02:38:45.792734
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cf = CmdLineFactCollector()
    df = cf._parse_proc_cmdline_facts(
        'root=LABEL=cloudimg-rootfs rw console=ttyS0 no_timer_check console=tty0 console=ttyS0,115200n8'
    )
    assert df['root'] == 'LABEL=cloudimg-rootfs'
    assert df['rw'] == True
    assert df['console'] == ['ttyS0', 'tty0', 'ttyS0,115200n8']
    assert df['no_timer_check'] == True
    assert df['bogus'] == False

# Generated at 2022-06-13 02:38:46.894694
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert isinstance(collector, BaseFactCollector)
    assert collector.name == 'cmdline'


# Generated at 2022-06-13 02:38:49.016307
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert isinstance(cmdline_collector._fact_ids, set)

# Generated at 2022-06-13 02:38:55.384058
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    try:
        from mock import Mock, patch
    except ImportError:
        return

    mock_shlex_split = Mock(return_value=['root=UUID=6e8a6b9c-5e39-4c5f-b5e5-7fbe0e2b3a0b', 'ro'])

    mock_get_file_content = Mock(return_value='root=UUID=6e8a6b9c-5e39-4c5f-b5e5-7fbe0e2b3a0b ro')

    with patch.object(shlex, 'split', mock_shlex_split):
        with patch.object(get_file_content, 'open', nullcontext(mock_get_file_content)):
            cmdline_facts = CmdLineFactCollector

# Generated at 2022-06-13 02:39:01.022435
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    _module = None
    _collected_facts = None
    _cmdline_facts = {}
    _data = "BOOT_IMAGE=/boot/vmlinuz-3.10.0-693.11.6.el7.x86_64 root=UUID=9a9dcf94-e31d-4bc8-a4f0-2f2d6497d1e8 ro crashkernel=auto resume=UUID=69b4c433-f40e-4c2b-a1d7-48b4530cf917 rhgb quiet LANG=en_US.UTF-8"

# Generated at 2022-06-13 02:39:03.565440
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fc = CmdLineFactCollector()
    fc.collect()