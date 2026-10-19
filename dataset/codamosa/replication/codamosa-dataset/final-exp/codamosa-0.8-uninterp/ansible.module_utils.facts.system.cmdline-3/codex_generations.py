

# Generated at 2022-06-13 02:30:18.455012
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    try:
        CmdLineFactCollector()
        assert True
    except:
        assert False

# Generated at 2022-06-13 02:30:19.749842
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    instance = CmdLineFactCollector()
    assert instance.name == 'cmdline'

# Generated at 2022-06-13 02:30:24.382630
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import Collector

    all_facts = {};
    Collector._callback({'ansible_facts': all_facts, 'failed': True}, [], 0)
    col = CmdLineFactCollector()
    col.collect(collected_facts=all_facts)
    assert col.name in all_facts

# Generated at 2022-06-13 02:30:29.880110
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Test without any argument
    fact_collector = CmdLineFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts == {'cmdline': {}, 'proc_cmdline': {}}

    # Test with an None argument
    collected_facts = fact_collector.collect(None, None)
    assert collected_facts == {'cmdline': {}, 'proc_cmdline': {}}


# Generated at 2022-06-13 02:30:31.820796
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    ansible_fact_module = CmdLineFactCollector()
    assert ansible_fact_module.name == 'cmdline'
    assert ansible_fact_module._fact_ids == set()


# Generated at 2022-06-13 02:30:32.660481
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:30:35.642225
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    obj = CmdLineFactCollector()
    result = obj.collect()

    assert isinstance(result, dict)
    assert 'cmdline' in result
    assert isinstance(result['cmdline'], dict)
    assert isinstance(result['proc_cmdline'], dict)

# Generated at 2022-06-13 02:30:37.251721
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    result = collector.collect()
    assert isinstance(result, dict)


# Generated at 2022-06-13 02:30:39.390487
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    obj = CmdLineFactCollector()
    result = obj.collect()
    assert result is not None
    assert 'cmdline' in result
    assert 'proc_cmdline' in result

# Generated at 2022-06-13 02:30:40.663427
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:30:48.735425
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert 'cmdline' in cmdline_fact_collector.name
    assert 'proc_cmdline' in cmdline_fact_collector._fact_ids
    assert 'cmdline' in cmdline_fact_collector._fact_ids

# Generated at 2022-06-13 02:30:59.251901
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    test_collector = CmdLineFactCollector()
    combined_cmdline = 'command1=value1 command2 command3=value2'

    test_collector._get_proc_cmdline = lambda: combined_cmdline

    cmdline_facts = test_collector.collect()
    assert cmdline_facts['cmdline']['command1'] == 'value1'
    assert cmdline_facts['cmdline']['command2'] == True
    assert cmdline_facts['cmdline']['command3'] == 'value2'
    assert cmdline_facts['proc_cmdline']['command1'] == 'value1'
    assert cmdline_facts['proc_cmdline']['command2'] == True
    assert cmdline_facts['proc_cmdline']['command3'] == 'value2'

    combined_cmd

# Generated at 2022-06-13 02:31:01.063345
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    node = CmdLineFactCollector()
    assert node.name == 'cmdline'
    assert node._fact_ids == set()


# Generated at 2022-06-13 02:31:02.561310
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    

# Generated at 2022-06-13 02:31:04.041841
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:31:10.207526
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.utils import FactsCollector
    from ansible.module_utils.facts.utils.fake_collector import FakeCmdLineFactCollector
    fake_cmdline_fact_collector = FakeCmdLineFactCollector()
    fake_cmdline_fact_collector.cmdline_data = "cmdline1=value1 cmdline2=true cmdline3 cmdline4=value2 cmdline4=value3"
    fake_cmdline_fact_collector.proc_cmdline_data = "proc_cmdline1=value1 proc_cmdline2=true proc_cmdline3 proc_cmdline4=value2 proc_cmdline4=value3"

# Generated at 2022-06-13 02:31:11.192429
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:31:12.530684
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert isinstance(CmdLineFactCollector().collect(), dict)

# Generated at 2022-06-13 02:31:22.244252
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector._get_proc_cmdline = lambda: 'arg1 arg2=val2'
    cmdline_facts = cmdline_collector.collect()

    assert ('cmdline' in cmdline_facts)
    assert ('arg1' in cmdline_facts['cmdline'])
    assert ('arg2' in cmdline_facts['cmdline'])
    assert (cmdline_facts['cmdline']['arg1'] is True)
    assert (cmdline_facts['cmdline']['arg2'] == 'val2')

    assert ('proc_cmdline' in cmdline_facts)
    assert (cmdline_facts['proc_cmdline']['arg1'] == 'True')

# Generated at 2022-06-13 02:31:25.111154
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFactCollector = CmdLineFactCollector()
    assert cmdLineFactCollector.name == 'cmdline'

if __name__ == "__main__":
    test_CmdLineFactCollector()

# Generated at 2022-06-13 02:31:35.537806
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:31:37.287053
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    ''' Return an object of CmdLineFactCollector class '''
    obj = CmdLineFactCollector()
    return obj


# Generated at 2022-06-13 02:31:41.793683
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector(None, None)
    data = collector._get_proc_cmdline()

    if data:
        cmdline_facts = collector._parse_proc_cmdline(data)
        assert cmdline_facts

        cmdline_facts = collector._parse_proc_cmdline_facts(data)
        assert cmdline_facts

        cmdline_facts = collector.collect()
        assert cmdline_facts



# Generated at 2022-06-13 02:31:43.806409
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    collected_facts = cmdline_collector.collect()
    assert collected_facts['cmdline']
    assert collected_facts['proc_cmdline']

# Generated at 2022-06-13 02:31:47.872599
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    assert CmdLineFactCollector().collect()
    assert CmdLineFactCollector().collect() == {
        'cmdline': {'BOOT_IMAGE': '/kernel'},
        'proc_cmdline': {'BOOT_IMAGE': '/kernel'},
    }

# Generated at 2022-06-13 02:31:54.822995
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == "cmdline"
    assert CmdLineFactCollector._fact_ids == set()
    assert CmdLineFactCollector.__doc__ == "Fact class for /proc/cmdline facts"
    assert CmdLineFactCollector.__module__ == "ansible.module_utils.facts.cmdline"
    assert CmdLineFactCollector.__name__ == "CmdLineFactCollector"
    assert CmdLineFactCollector.__init__.__doc__ == "Fact class for /proc/cmdline facts"

# Generated at 2022-06-13 02:31:56.773802
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'
    assert CmdLineFactCollector()._fact_ids == set()

# Generated at 2022-06-13 02:31:57.232788
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:32:06.379691
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # _get_proc_cmdline mock.
    class Collector():
        def _get_proc_cmdline(self):
            return "BOOT_IMAGE=/boot/vmlinuz-3.16.0-5-amd64 root=UUID=a42560b8-d9fb-4f61-b5f5-03c6e4dd0e0c ro"

    # _parse_proc_cmdline mock.
    class Collector():
        def _parse_proc_cmdline(self, data):
            return {u'BOOT_IMAGE': u'/boot/vmlinuz-3.16.0-5-amd64', u'root': u'UUID=a42560b8-d9fb-4f61-b5f5-03c6e4dd0e0c', u'ro': True}

# Generated at 2022-06-13 02:32:14.860555
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Setup test fixtures
    class TestCollector(CmdLineFactCollector):
        name = 'cmdline'
        _fact_ids = set()

        def _get_proc_cmdline(self):
            return "ansible_python_interpreter=/usr/bin/python3 ansible_user=ansible ansible_become_pass=ansible"

        def _parse_proc_cmdline(self, data):
            return self._parse_proc_cmdline_facts(data)

    # Invoke the method under test
    testFacts = TestCollector().collect()

    # Verify the results
    assert testFacts['cmdline'] == testFacts['proc_cmdline']
    assert testFacts['cmdline']['ansible_python_interpreter'] == "/usr/bin/python3"
    assert testFacts

# Generated at 2022-06-13 02:32:32.608362
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()

# Generated at 2022-06-13 02:32:35.155690
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'


# Generated at 2022-06-13 02:32:38.203045
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = CmdLineFactCollector().collect(None, None)

    assert isinstance(cmdline_facts, dict)
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:32:44.352566
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    collected_facts = cmdline_collector.collect()
    assert "cmdline" in collected_facts
    assert "proc_cmdline" in collected_facts
    assert "ansible_cmdline" not in collected_facts
    assert "ansible_proc_cmdline" not in collected_facts

    assert isinstance(collected_facts['cmdline'], dict)
    assert isinstance(collected_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:32:45.564254
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == "cmdline" and len(c._fact_ids) == 0

# Generated at 2022-06-13 02:32:47.536274
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector_inst = CmdLineFactCollector()
    assert cmdline_fact_collector_inst.name == 'cmdline'
    assert cmdline_fact_collector_inst._fact_ids == set()


# Generated at 2022-06-13 02:32:51.625794
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cfg = CmdLineFactCollector()
    assert cfg.name == 'cmdline'
    assert cfg._fact_ids == set()


# Generated at 2022-06-13 02:32:55.180359
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector.priority == 50
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:33:05.937015
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Test method collect of class CmdLineFactCollector.

    The following assertions are made:
    * The method returns secrets_files facts.
    * The secrets_files facts are correct.

    """
    from ansible.module_utils.facts import facts

    # Initialize the system
    fact_collector = facts.FactCollector()
    system = fact_collector.collect(module=None, collected_facts={})
    system['machine_id'] = 'fake_machine_id'

    # Invoke the method under test
    cmdline_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_collector.collect(module=None, collected_facts={})

    # Check the facts

# Generated at 2022-06-13 02:33:13.965638
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # instantiate
    cmdline_instance = CmdLineFactCollector()

    # create test data
    # live test data
    # test_data = cmdline_instance._get_proc_cmdline()
    test_data = 'BOOT_IMAGE=/vmlinuz-linux initrd=\initramfs-linux.img ro root=UUID=ce938f47-8c59-4a06-af11-a4e2a8e4f4d2'

    # call method collect
    cmdline_facts = cmdline_instance.collect()
    # verify results
    # cmdline_facts['cmdline']
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['cmdline']['BOOT_IMAGE'], str)
    assert cmdline_facts

# Generated at 2022-06-13 02:33:48.734619
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd = CmdLineFactCollector()
    assert cmd.name == 'cmdline'
    assert cmd._fact_ids == set()


# Generated at 2022-06-13 02:33:55.676846
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector._get_proc_cmdline = lambda: 'a=1 b=2 c=3 d=4 e'
    cmdline_collector._parse_proc_cmdline = lambda data: {}
    cmdline_collector._parse_proc_cmdline_facts = lambda data: {}
    cmdline_facts = cmdline_collector.collect()

    assert cmdline_facts['cmdline'] == {}
    assert cmdline_facts['proc_cmdline'] == {}



# Generated at 2022-06-13 02:33:57.884944
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
  cmd = CmdLineFactCollector()
  assert cmd.name == 'cmdline'
  assert cmd._fact_ids == set()



# Generated at 2022-06-13 02:33:59.660543
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_coll = CmdLineFactCollector()
    assert cmdline_coll.name == "cmdline"


# Generated at 2022-06-13 02:34:02.097905
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert not bool(cmdline_fact_collector._fact_ids)

# Generated at 2022-06-13 02:34:03.627864
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    assert collector.collect() == {'cmdline': {}, 'proc_cmdline': {}}

# Generated at 2022-06-13 02:34:04.877653
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 02:34:09.784145
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import tempfile


# Generated at 2022-06-13 02:34:19.598990
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    #
    # Test valid /proc/cmdline content
    #
    collector = CmdLineFactCollector()
    collector.collect()
    assert(isinstance(collector.data['cmdline'], dict))
    assert(isinstance(collector.data['cmdline']['BOOT_IMAGE'], str))
    assert(isinstance(collector.data['proc_cmdline'], dict))
    assert(isinstance(collector.data['proc_cmdline']['BOOT_IMAGE'], str))

    #
    # Test /proc/cmdline content with multiple values for a single key
    #
    collector = CmdLineFactCollector()
    collector.data['cmdline'] = collector._parse_proc_cmdline('foo=bar foo=baz')
    collector.data['proc_cmdline'] = collector

# Generated at 2022-06-13 02:34:30.159867
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule

    dev_file_content = ' '
    new_cmdline_facts_dict = {'uname': 'test4'}
    new_proc_cmdline_facts_dict = {'uname': 'test3'}

    def mock_get_file_content(file_path, default=None):
        if file_path == '/proc/cmdline':
            return 'uname=test1 uname=test2 uname=test3 uname=test4'
        elif file_path == '/proc/modules':
            return dev_file_content

    def mock_parse_proc_cmdline(data):
        return new_cmdline_facts_dict

    def mock_parse_proc_cmdline_facts(data):
        return new_proc_cmdline_

# Generated at 2022-06-13 02:35:56.319665
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    c = CmdLineFactCollector()
    content = 'a=1 b=2 c= d= e=1 g="1 2"     h="1 2.2 3" '
    c._get_proc_cmdline = lambda : content
    actual = c.collect()
    expected = {'cmdline': {'a': '1', 'b': '2', 'c': True, 'd': True, 'e': '1', 'g': '1 2', 'h': '1 2.2 3'},
                'proc_cmdline': {'a': '1', 'b': '2', 'c': True, 'd': True, 'e': '1', 'g': ['1', '2'], 'h': ['1', '2.2', '3']}}

    assert actual == expected

# Generated at 2022-06-13 02:35:57.828884
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    a = CmdLineFactCollector()
    assert a.name == 'cmdline'
    assert  a._fact_ids == set()

# Generated at 2022-06-13 02:35:58.833238
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'

# Generated at 2022-06-13 02:36:01.991560
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    import pytest
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector.collectors = []
    x = CmdLineFactCollector()
    f = CmdLineFactCollector.name
    assert f == 'cmdline'

# Generated at 2022-06-13 02:36:04.724799
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fact_collector = CmdLineFactCollector()
    collected_facts = fact_collector.collect()
    assert 'ansible_cmdline' in collected_facts


# Generated at 2022-06-13 02:36:07.217213
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert isinstance(CmdLineFactCollector(), BaseFactCollector)
    assert hasattr(CmdLineFactCollector(), 'name')
    assert hasattr(CmdLineFactCollector(), '_fact_ids')

# Generated at 2022-06-13 02:36:08.000953
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    assert CmdLineFactCollector.collect()

# Generated at 2022-06-13 02:36:13.879601
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector._get_proc_cmdline = lambda: "root=/dev/mapper/lenny--vg-root ro\n"
    cmdline_collector._parse_proc_cmdline = lambda data: data.splitlines()
    cmdline_collector._parse_proc_cmdline_facts = lambda data: data.splitlines()

    result = cmdline_collector.collect()
    assert result['cmdline'] == ["root=/dev/mapper/lenny--vg-root ro"]
    assert result['proc_cmdline'] == ["root=/dev/mapper/lenny--vg-root ro"]

# Generated at 2022-06-13 02:36:18.357205
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import ListCollector
    from ansible.module_utils.facts.collector import DictCollector
    from ansible.module_utils.facts import get_collector_object

    cmdline = """
rd.lvm.lv=fedora/swap rd.lvm.lv=fedora/root rhgb quiet crashkernel=auto LANG=en_US.UTF-8
"""
    cmdline_string = cmdline.replace("\n", "")
    cmdline_list = cmdline_string.split()

# Generated at 2022-06-13 02:36:19.867382
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    test_obj = CmdLineFactCollector()

    # Call method collect without parameter
    result = test_obj.collect()

    assert result is not None
    assert isinstance(result, dict)
    assert result['proc_cmdline']
    assert result['cmdline']

# Generated at 2022-06-13 02:39:40.385667
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()

    filepath = './test/unit/ansible_collections/community/generic/plugins/module_utils/facts/test_files/proc_cmdline'
    expected = {
        'cmdline': {
            'ro': True,
            'root': '/dev/mapper/rhel-root'
        },
        'proc_cmdline': {
            'ro': True,
            'root': '/dev/mapper/rhel-root'
        }
    }

    cmdline_collector.get_file_content = lambda p: open(filepath).read()

    result = cmdline_collector.collect()
    assert result == expected

# Generated at 2022-06-13 02:39:45.844876
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_obj = CmdLineFactCollector()
    assert cmdline_obj
    assert cmdline_obj.name == "cmdline"
    assert cmdline_obj.collect(None, None)

# Generated at 2022-06-13 02:39:47.774283
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_obj = CmdLineFactCollector()
    assert isinstance(cmdline_obj, BaseFactCollector)


# Generated at 2022-06-13 02:39:54.591885
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class MockModule(object):
        pass

    class MockCollectedFacts(object):
        pass

    mock_module = MockModule()
    mock_collected_facts = MockCollectedFacts()


# Generated at 2022-06-13 02:39:55.472586
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:40:00.142393
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collectors

    collectors = Collectors()

    cmdline_data = 'console=ttyS1 root=LABEL=root-a ro rootfstype=ext4 elevator=noop init=/sbin/init ' \
                   'initrd=initramfs-a.img'

    def test_get_proc_cmdline(self):
        return cmdline_data

    CmdLineFactCollector._get_proc_cmdline = test_get_proc_cmdline

    cmdline_collector = CmdLineFactCollector('cmdline', collectors)

    results = cmdline_collector.collect()


# Generated at 2022-06-13 02:40:01.870974
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert 'cmdline' in CmdLineFactCollector.__dict__
    assert 'proc_cmdline' in CmdLineFactCollector.__dict__


# Generated at 2022-06-13 02:40:02.717075
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'

# Generated at 2022-06-13 02:40:03.064873
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:40:04.157817
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()
