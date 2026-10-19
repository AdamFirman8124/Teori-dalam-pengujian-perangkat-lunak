

# Generated at 2022-06-13 02:30:28.769318
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Test with empty data
    cf = CmdLineFactCollector()
    data = cf._get_proc_cmdline()
    assert data is None
    assert cf.collect() == {}

    # Test with sample data
    cf = CmdLineFactCollector()
    data = "BOOT_IMAGE=/vmlinuz.old root=UUID=e9f5d39f-9db5-41f7-8b0a-0c13fa0c5b7b ro quiet splash vt.handoff=7"
    cf.test_data = data

# Generated at 2022-06-13 02:30:31.004926
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()

# Generated at 2022-06-13 02:30:34.102599
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()
    assert cmdline_fact_collector.collect() == {}


# Generated at 2022-06-13 02:30:34.910848
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector()

# Generated at 2022-06-13 02:30:40.898613
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmd = CmdLineFactCollector()

    # Call collect without calling '_get_proc_cmdline' which returns None
    cmdline_facts = cmd.collect()

    assert cmdline_facts == {}

    # Make '_get_proc_cmdline' return some data
    cmd._get_proc_cmdline = lambda: 'key1="value 1" key2=value2 key3'

    cmdline_facts = cmd.collect()

    assert cmdline_facts == {'cmdline': {'key1': 'value 1', 'key2': 'value2', 'key3': True},
                             'proc_cmdline': {'key1': 'value 1', 'key2': 'value2', 'key3': True}}

# Generated at 2022-06-13 02:30:44.748669
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector.valid == True

# Generated at 2022-06-13 02:30:47.348391
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()


# Generated at 2022-06-13 02:30:53.800367
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts import timeout
    import ansible.module_utils.facts

    with timeout.single_timeout(2):
        ansible.module_utils.facts.get_file_content = get_file_content
        ansible.module_utils.facts.timeout = timeout

        a_collector = Collector()

        c_cmdline_fact_collector = CmdLineFactCollector()
        c_cmdline_fact_collector.collect()

        a_collector._add_fact_collector(c_cmdline_fact_collector)

        result = a_collector.collect(module=None, collected_facts=None)

        a_collector._

# Generated at 2022-06-13 02:31:02.966104
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Test function for method collect of class CmdLineFactCollector"""
    test_class = CmdLineFactCollector()
    test_proc_cmdline = ' console=ttyS0,115200 crashkernel=256M root=UUID=d35a07b0-c1a9-3ad3-e054-64a89e7a8baf rhgb quiet'
    test_result = test_class._parse_proc_cmdline_facts(test_proc_cmdline)
    assert test_result['console'] == 'ttyS0,115200'
    assert test_result['crashkernel'] == '256M'
    assert test_result['root'] == 'UUID=d35a07b0-c1a9-3ad3-e054-64a89e7a8baf'
    assert test_

# Generated at 2022-06-13 02:31:03.900158
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()


# Generated at 2022-06-13 02:31:13.462475
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'

# Generated at 2022-06-13 02:31:20.453571
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    mock_module_util = get_file_content
    mock_module_util.return_value = "ansible_playbook_python=/usr/bin/python3"
    cmd_line_fact_collector = CmdLineFactCollector()
    output = cmd_line_fact_collector.collect()
    assert output == {'cmdline': {'ansible_playbook_python': '/usr/bin/python3'}, 'proc_cmdline': {'ansible_playbook_python': '/usr/bin/python3'}}
    mock_module_util.return_value = ""
    output = cmd_line_fact_collector.collect()
    assert output == {}

# Generated at 2022-06-13 02:31:21.061938
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:31:22.757984
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector is not None

# Generated at 2022-06-13 02:31:24.868186
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdlineFactCollector = CmdLineFactCollector()
    assert cmdlineFactCollector.name == "cmdline"



# Generated at 2022-06-13 02:31:27.244884
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
        cmd_line = CmdLineFactCollector()
        output = cmd_line.collect(None, None)
        assert output['cmdline']
        assert output['proc_cmdline']


# Generated at 2022-06-13 02:31:33.617301
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    This function test if function collect of class CmdLineFactCollector
    returns the expected values
    """
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    def get_file_content_mock(path):
        content = ''

        if path == '/proc/cmdline':
            content = 'foo=1 bar root=UUID=f9a6959f-d00e-4077-b2e2-8a8a2a5ae7d5'

        return content

    def get_file_content_mock_valueerror(path):
        content = ''


# Generated at 2022-06-13 02:31:36.260094
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """Unit test for constructor of class CmdLineFactCollector"""
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'

# Generated at 2022-06-13 02:31:38.215045
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fact = CmdLineFactCollector()
    assert(cmd_line_fact.name == 'cmdline')


# Generated at 2022-06-13 02:31:39.298065
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'

# Generated at 2022-06-13 02:31:49.903196
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj is not None

# Generated at 2022-06-13 02:31:51.806302
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cf = CmdLineFactCollector()
    assert cf.name == 'cmdline'
    assert cf._fact_ids == set()


# Generated at 2022-06-13 02:31:53.579917
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:31:55.324304
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
  facts = CmdLineFactCollector()
  assert facts.name == 'cmdline'
  assert facts._fact_ids == set()


# Generated at 2022-06-13 02:31:57.221882
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert not cmdline._fact_ids

# Generated at 2022-06-13 02:32:06.380854
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import CmdLineFactCollector
    from ansible.module_utils.facts.utils import get_file_content

     # create an instance of CmdLineFactCollector
    c = CmdLineFactCollector()

    # create a fake module object
    class FakeModule:
        def __init__(self):
            self.params = ""
            self.exit_json = ""
            self.fail_json = ""

        def fail_json_if_missing(self, **kwargs):
            pass

    # create a FakeModule object
    fake_module = FakeModule()

    # create a fake collector object
    class FakeCollector:
        def __init__(self):
            self.collectors = []


# Generated at 2022-06-13 02:32:10.154822
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """ Test parse cmdline facts """
    fact_collector = CmdLineFactCollector()

    data = fact_collector._get_proc_cmdline()
    cmdline_facts = fact_collector.collect()
    assert isinstance(cmdline_facts, dict)
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)

# Generated at 2022-06-13 02:32:13.457470
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()
    assert cmdline_facts['cmdline']
    assert cmdline_facts['proc_cmdline']

# Generated at 2022-06-13 02:32:14.736875
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj=CmdLineFactCollector()
    assert obj == None


# Generated at 2022-06-13 02:32:23.655008
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()

    # if no data to collect, return empty dict
    assert cmdline_collector.collect() == {}

    # if empty content, also return empty dict
    cmdline_collector._get_proc_cmdline = lambda: ''
    assert cmdline_collector.collect() == {}

    # if content is not parsable, return empty dict
    cmdline_collector._get_proc_cmdline = lambda: 'abc def ghij'
    assert cmdline_collector.collect() == {}

    # if content is parsable, return normal result
    cmdline_collector._get_proc_cmdline = lambda: 'a b c=d'

# Generated at 2022-06-13 02:32:47.838009
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fixture = 'BOOT_IMAGE=/vmlinuz-3.10.0-327.el7.x86_64 root=UUID=3e3d3c1a-7f02-4d96-b62c-a9e9ce0cbe8a ro crashkernel=auto resume=UUID=ff2b0c38-d7c5-4a9a-8b8c-31db24540d0f LANG=en_US.UTF-8 rhgb quiet'
    test_collector = CmdLineFactCollector()
    result = test_collector.collect()
    assert 'cmdline' in result
    assert 'proc_cmdline' in result

# Generated at 2022-06-13 02:32:50.916360
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd = CmdLineFactCollector()
    assert cmd.name == 'cmdline'


# Generated at 2022-06-13 02:32:51.975398
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector()

# Generated at 2022-06-13 02:32:55.305755
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()
    assert len(c._fact_ids) == 0

# Generated at 2022-06-13 02:33:06.090150
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils._text import to_bytes

    fact_list = list(Collector.get_collection_list())
    assert "CmdLineFactCollector" in fact_list

    proc_cmdline = to_bytes('root=/dev/sda1 console=tty0 console=ttyS0 '
                            'rootfstype=ext4')

    class MockParser(object):

        def __init__(self, cmdline):
            self._cmdline = cmdline

        def _get_proc_cmdline(self):
            return self._cmdline


# Generated at 2022-06-13 02:33:13.701750
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    module = None
    collected_facts = None


# Generated at 2022-06-13 02:33:14.533366
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_col = CmdLineFactCollector()
    assert fact_col is not None

# Generated at 2022-06-13 02:33:15.317348
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'

# Generated at 2022-06-13 02:33:17.893018
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector

    # Arrange

    # Act
    mf = ModuleFacts(collectors=[CmdLineFactCollector()])
    facts = mf.collect()

    # Assert
    assert 'cmdline' in facts
    assert 'proc_cmdline' in facts

# Generated at 2022-06-13 02:33:18.726398
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    processor = CmdLineFactCollector()
    assert processor

# Generated at 2022-06-13 02:34:01.567407
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    passed_dict = {'ansible_cmdline': {'ansible_check_mode': True, 'ansible_host': '10.10.10.10', 'ansible_user': 'test_user'}, 'ansible_proc_cmdline': {'ansible_check_mode': ['True'], 'ansible_host': ['10.10.10.10'], 'ansible_user': ['test_user']}}
    
    data = 'ansible_user=test_user ansible_host=10.10.10.10 ansible_check_mode'
    cmdline_facts = CmdLineFactCollector()
    cmdline_facts._parse_proc_cmdline = lambda self: data

    returned_value = cmdline_facts.collect()

    assert passed_dict == returned_value

# Generated at 2022-06-13 02:34:06.997742
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = "BOOT_IMAGE=/vmlinuz-3.10.0-957.el7.x86_64" \
           " root=/dev/mapper/cl-root ro crashkernel=auto" \
           " rd.lvm.lv=cl/root rd.lvm.lv=cl/swap" \
           " rhgb quiet LANG=en_US.UTF-8"

    cmdline = CmdLineFactCollector()

    cmdline_facts = cmdline.collect()

    assert 'cmdline' in cmdline_facts
    assert 'proc_cmdline' in cmdline_facts


# Generated at 2022-06-13 02:34:17.579224
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    col = CmdLineFactCollector()
    collected_facts = col.collect()

    assert 'cmdline' in collected_facts
    assert 'proc_cmdline' in collected_facts

    actual_key_set = set(collected_facts['proc_cmdline'].keys())
    expected_key_set = set(collected_facts['cmdline'].keys())
    assert actual_key_set == expected_key_set

    assert isinstance(collected_facts['proc_cmdline']['BOOT_IMAGE'], str)
    assert isinstance(collected_facts['cmdline']['BOOT_IMAGE'], str)

    assert collected_facts['cmdline']['BOOT_IMAGE'] == collected_facts['proc_cmdline']['BOOT_IMAGE']


# Generated at 2022-06-13 02:34:27.463637
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    res = c.collect()
    assert 'cmdline' in res
    assert 'proc_cmdline' in res
    for key in res['cmdline']:
        assert(res['proc_cmdline'][key] == res['cmdline'][key] or
               res['proc_cmdline'][key] == [res['cmdline'][key]])
    for key in res['proc_cmdline']:
        if isinstance(res['proc_cmdline'][key], list):
            assert(res['cmdline'][key] in res['proc_cmdline'][key])
        else:
            assert(res['cmdline'][key] == res['proc_cmdline'][key])


# Generated at 2022-06-13 02:34:30.100834
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:34:39.995029
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os
    global file_data
    class AnsibleModule():
        '''AnsibleModule stub'''
        def __init__(self):
            self.params = dict()
    global ansible_module_stub
    ansible_module_stub = AnsibleModule()
    global file_mock
    global module_mock
    global get_file_content_mock
    global os_mock
    global open_mock
    global file_data
    file_data = ''
    open_mock = mock_open()
    get_file_content_mock = Mock(return_value = file_data)

    class mock_file():
        '''mock_file stub'''
        def __init__(self):
            pass

        def read(self):
            return file_data

# Generated at 2022-06-13 02:34:41.290490
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline is not None


# Generated at 2022-06-13 02:34:43.674235
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts.name == 'cmdline'
    assert 'cmdline' in cmdline_facts._fact_ids
    assert 'proc_cmdline' in cmdline_facts._fact_ids


# Generated at 2022-06-13 02:34:45.449232
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()

# test if the cmdline facts are being collected if content in proc cmdline file

# Generated at 2022-06-13 02:34:47.474214
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_collector.collect()

    assert cmdline_facts['cmdline']
    assert cmdline_facts['proc_cmdline']

# Generated at 2022-06-13 02:36:09.839964
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.collect()

# Generated at 2022-06-13 02:36:12.115208
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector is not None
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()

# Generated at 2022-06-13 02:36:19.172321
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    class MockModule(object):
        pass

    cmdline_dict = {'ansible_extravar': '1', 'ansible_retryvar': '1', 'ansible_retryvar': '2'}
    proc_cmdline_dict = {'ansible_extravar': '1', 'ansible_retryvar': ['1', '2']}
    mock_module = MockModule()
    mock_collector = CmdLineFactCollector()
    mock_collector.populate(mock_module)
    mock_collector.facts = {'cmdline': cmdline_dict, 'proc_cmdline': proc_cmdline_dict}
    cmdline_facts = mock_collector.collect(mock_module)
    assert cmdline_facts['cmdline'] == cmdline_dict
    assert cmdline_

# Generated at 2022-06-13 02:36:20.757891
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:36:22.133485
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline.collect() == {}

# Generated at 2022-06-13 02:36:23.486880
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = CmdLineFactCollector().collect()
    assert isinstance(cmdline_facts, dict)

# Generated at 2022-06-13 02:36:25.986948
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert isinstance(collector._fact_ids, set)
    assert collector._fact_ids == set()


# Generated at 2022-06-13 02:36:27.259180
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Unit test for constructor of class CmdLineFactCollector
    assert CmdLineFactCollector

# Generated at 2022-06-13 02:36:29.300072
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """Test of constructor"""
    my_fact_collector = CmdLineFactCollector()
    assert isinstance(my_fact_collector, CmdLineFactCollector)


# Generated at 2022-06-13 02:36:32.087015
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_name = 'cmdline'
    cmdline_fact_id = set()

    cmdline_collector = CmdLineFactCollector()

    assert cmdline_collector.name == cmdline_fact_name
    assert cmdline_collector._fact_ids == cmdline_fact_id

# Generated at 2022-06-13 02:39:53.303500
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Test with empty content /proc/cmdline
    fc = CmdLineFactCollector()
    fc.get_file_content = lambda *args: ''
    cmdline_facts = fc.collect()
    assert cmdline_facts == {'cmdline': {}, 'proc_cmdline': {}}

    # Test with content /proc/cmdline // normal
    fc = CmdLineFactCollector()
    fc.get_file_content = lambda *args: 'foo=1 bar=2'
    cmdline_facts = fc.collect()
    assert cmdline_facts == {'cmdline': {'foo': '1', 'bar': '2'}, 'proc_cmdline': {'foo': '1', 'bar': '2'}}

    # Test with content /proc/cmdline // repeated keys, list values


# Generated at 2022-06-13 02:39:54.895864
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFactCollector = CmdLineFactCollector()
    assert 'cmdline' == cmdLineFactCollector.name
    assert set() == cmdLineFactCollector._fact_ids

# Generated at 2022-06-13 02:39:56.560786
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_fact_collector.collect()
    print(cmdline_facts)

# Generated at 2022-06-13 02:39:59.836693
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    result = collector.collect()
    assert result['cmdline']['BOOT_IMAGE'] == '/vmlinuz-2.6.32-358.123.2.openstack.el6.x86_64'
    assert result['proc_cmdline']['BOOT_IMAGE'] == ['/vmlinuz-2.6.32-358.123.2.openstack.el6.x86_64']

# Generated at 2022-06-13 02:40:07.031785
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    test_cmdline = "console=tty1 console=ttyS0 quiet rd.udev.log_priority=3 vga=0x318"
    proc_cmdline = cmdline_collector._parse_proc_cmdline(test_cmdline)
    proc_cmdline_facts = cmdline_collector._parse_proc_cmdline_facts(test_cmdline)
    assert proc_cmdline == {'console': ['tty1', 'ttyS0'], 'quiet': True, 'rd.udev.log_priority': '3', 'vga': '0x318'}

# Generated at 2022-06-13 02:40:10.098405
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert hasattr(CmdLineFactCollector, 'name')
    assert hasattr(CmdLineFactCollector, '_fact_ids')
    assert hasattr(CmdLineFactCollector, '_get_proc_cmdline')
    assert hasattr(CmdLineFactCollector, '_parse_proc_cmdline')
    assert hasattr(CmdLineFactCollector, '_parse_proc_cmdline_facts')
    assert hasattr(CmdLineFactCollector, 'collect')

# Generated at 2022-06-13 02:40:14.124465
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # TODO: Change test to use the correct class
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'