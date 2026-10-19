

# Generated at 2022-06-13 02:30:20.641553
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    CmdLineFactCollector().collect()


# Generated at 2022-06-13 02:30:21.924786
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fc = CmdLineFactCollector()
    assert cmdline_fc.name == 'cmdline'
    assert cmdline_fc._fact_ids == set()


# Generated at 2022-06-13 02:30:23.754593
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()


# Generated at 2022-06-13 02:30:25.818615
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():

    cmd = CmdLineFactCollector()
    assert cmd.name == 'cmdline'
    assert cmd._fact_ids == set()


# Generated at 2022-06-13 02:30:27.045121
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:30:29.084796
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()

# Generated at 2022-06-13 02:30:37.711144
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Mock class object
    class object:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    # Mock method
    def _get_proc_cmdline(self):
        return 'foo=1 bar=2 baz=3'

    # Assign object methods to mock methods
    CmdLineFactCollector._get_proc_cmdline = _get_proc_cmdline

    # Execute method collect
    c = CmdLineFactCollector()
    assert c.collect() == {'cmdline': {'foo': '1', 'bar': '2', 'baz': '3'},
                           'proc_cmdline': {'foo': '1', 'bar': '2', 'baz': '3'}}

# Generated at 2022-06-13 02:30:43.330772
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = lambda: 'foo bar'
    assert collector.collect() == {'cmdline': {'foo': True, 'bar': True}, 'proc_cmdline': {'foo': True, 'bar': True}}

    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = lambda: 'foo=bar'
    assert collector.collect() == {'cmdline': {'foo': 'bar'}, 'proc_cmdline': {'foo': 'bar'}}

    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = lambda: 'foo=bar baz'

# Generated at 2022-06-13 02:30:46.193693
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == "cmdline"

# Generated at 2022-06-13 02:30:47.626914
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:30:59.290162
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()



# Generated at 2022-06-13 02:31:07.179540
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = {}
    data = "root=UUID=f9c9a379-b1ed-4fe3-b768-a8f12dc03c60 ro console=tty0 console=ttyS0,115200n8"

    cmdline_facts['cmdline'] = {'console': 'ttyS0,115200n8', 'root': 'UUID=f9c9a379-b1ed-4fe3-b768-a8f12dc03c60', 'ro': True}
    cmdline_facts['proc_cmdline'] = {'console': ['tty0', 'ttyS0,115200n8'], 'root': 'UUID=f9c9a379-b1ed-4fe3-b768-a8f12dc03c60', 'ro': True}

    assert Cmd

# Generated at 2022-06-13 02:31:08.467599
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert isinstance(c._fact_ids, set)

# Generated at 2022-06-13 02:31:10.594474
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Just testing if we can instantiate this class
    assert CmdLineFactCollector()

# Generated at 2022-06-13 02:31:11.958055
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()
    assert x.name == 'cmdline'

# Generated at 2022-06-13 02:31:15.183712
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:31:24.951837
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:31:35.114902
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    import mock
    import pytest

    from ansible.module_utils.facts.collector import BaseFactCollector

    runner_mock = mock.MagicMock()
    runner_mock.run.return_value = (1, '', '')

    # Creates the class under test.
    c = CmdLineFactCollector(runner_mock)
    # Checks if class is a subclass of BaseFactCollector.
    assert isinstance(c, BaseFactCollector)

    with pytest.raises(NotImplementedError) as excinfo:
        c.collect()
    assert str(excinfo.value) == 'CmdLineFactCollector.collect() is not implemented'
    with pytest.raises(NotImplementedError) as excinfo:
        c.__call__()

# Generated at 2022-06-13 02:31:35.954759
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:31:43.476907
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Create CmdLineFactCollector object
    cmdline = CmdLineFactCollector()

    # Create dictionary to contain cmdline facts
    cmdline_facts = {}

    # Populate dictionary with expected cmdline facts

# Generated at 2022-06-13 02:32:08.670708
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content

    STATIC_CMDLINE = 'console=ttyS0 cciss/c0d0=1G_root-cciss,0x31100'
    STATIC_CMDLINE_EXPECTED = {
        'console': 'ttyS0',
        'cciss/c0d0': '1G_root-cciss,0x31100'
    }
    STATIC_CMDLINE_EXPECTED_FACTS = {
        'console': 'ttyS0',
        'cciss/c0d0': ['1G_root-cciss', '0x31100']
    }

    # Create a stub for method get_file_content

# Generated at 2022-06-13 02:32:13.498425
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts.name == 'cmdline'
    assert not cmdline_facts.collect()['proc_cmdline']
    assert not cmdline_facts.collect()['cmdline']


# Generated at 2022-06-13 02:32:17.856840
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Test for method CmdLineFactCollector.collect"""

    c = CmdLineFactCollector()
    result = c.collect()

    assert type(result) == dict
    assert type(result['cmdline']) == dict

# Generated at 2022-06-13 02:32:20.011466
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert fact_collector.name == 'cmdline'
    assert fact_collector.collect_method != None


# Generated at 2022-06-13 02:32:25.632236
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.params = {}

    class MockFactCollector(object):
        def __init__(self):
            self.collected_facts = []

    def get_file_content_mock(mocked_content):
        return mocked_content

    # Test for normal /proc/cmdline content
    # Let's mock the /proc/cmdline file content
    mocked_content = "root=UUID=3d6ffd0a-ea39-4da2-b2e6-9e6c5c8fbe4c ro quiet splash " \
                     "vga=0x317 loglevel=3"
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector._get_proc_cmdline = get_file_content

# Generated at 2022-06-13 02:32:30.586414
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # GIVEN
    cmdlineFactCollector = CmdLineFactCollector()

    # WHEN
    collected_facts = cmdlineFactCollector.collect()

    # THEN
    assert collected_facts

    assert 'cmdline' in collected_facts, \
        "Expected collected_facts['cmdline'] to be available"
    assert 'proc_cmdline' in collected_facts, \
        "Expected collected_facts['proc_cmdline'] to be available"

# Generated at 2022-06-13 02:32:40.089909
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # expected data to test
    cmdline = get_file_content('/proc/cmdline')
    cmdline_dict = {}
    try:
        for piece in shlex.split(cmdline, posix=False):
            item = piece.split('=', 1)
            if len(item) == 1:
                cmdline_dict[item[0]] = True
            else:
                cmdline_dict[item[0]] = item[1]
    except ValueError:
        pass
    cmdline_facts = {}

# Generated at 2022-06-13 02:32:41.358248
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()
    assert x.name == 'cmdline'
    assert x._fact_ids == set()


# Generated at 2022-06-13 02:32:49.082062
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    # given

    # when
    collector = Collector()
    cmdline_facts = collector.collect(CmdLineFactCollector())
    # then


# Generated at 2022-06-13 02:32:51.792094
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdlinefactcollector = CmdLineFactCollector()
    assert isinstance(cmdlinefactcollector, CmdLineFactCollector)


# Generated at 2022-06-13 02:33:35.169421
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    empty_collector = CmdLineFactCollector()
    assert empty_collector.collect() == {}

    sample_data = 'root=/dev/sda1 rw console=ttyS0,9600n8'
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector._get_proc_cmdline = lambda: sample_data
    assert cmdline_collector.collect() == {
        'cmdline': {
            'root': '/dev/sda1',
            'rw': True,
            'console': 'ttyS0,9600n8',
        },
        'proc_cmdline': {
            'root': '/dev/sda1',
            'rw': True,
            'console': 'ttyS0,9600n8',
        },
    }


# Generated at 2022-06-13 02:33:36.882282
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:33:44.021130
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Preparing mock data
    data = b'key=value another_key=another_value'

    # Preparing mocks
    class CmdLineFactCollectorMocked(CmdLineFactCollector):
        name = 'cmdline'

        def _get_proc_cmdline(self):
            return data

    # Call method being tested
    cmdline_facts = CmdLineFactCollectorMocked().collect()

    # Asserting
    # Asserting cmdline
    assert len(cmdline_facts['cmdline']) == 2
    assert 'key' in cmdline_facts['cmdline']
    assert 'value' == cmdline_facts['cmdline']['key']
    assert 'another_key' in cmdline_facts['cmdline']

# Generated at 2022-06-13 02:33:48.582021
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """Test constructor of class CmdLineFactCollector.
    """
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()
    c = CmdLineFactCollector(name='cmd_line')
    assert c.name == 'cmd_line'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:33:50.509358
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fact_collector = CmdLineFactCollector()
    cmdline_facts = fact_collector.collect()
    assert cmdline_facts is not None



# Generated at 2022-06-13 02:33:53.483773
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert 'cmdline' == cmdline.name
    assert cmdline._fact_ids == set()

# Generated at 2022-06-13 02:33:58.082717
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Create CmdLineFactCollector object
    module = AnsibleModuleFake()
    cmdline_fact_collector = CmdLineFactCollector()

    # Assert that name attribute of CmdLineFactCollector object is equal to cmdline
    assert cmdline_fact_collector.name == 'cmdline'


# Generated at 2022-06-13 02:34:05.218037
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    def fake_get_file_content(file_name):
        if file_name == '/proc/cmdline':
            return 'root=/dev/mapper/container-root ro quiet splash vt.handoff=1'
        else:
            return None

    collector = CmdLineFactCollector()
    collector.get_file_content = fake_get_file_content

    collected_facts = collector.collect()

    assert len(collected_facts) == 2


# Generated at 2022-06-13 02:34:06.432736
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Get instance of class CmdLineFactCollector
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert set() == collector._fact_ids


# Generated at 2022-06-13 02:34:08.147169
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert fact_collector.name == 'cmdline'
    assert fact_collector.priority == 6
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:35:32.245657
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    print("Checking constructor of class CmdLineFactCollector")
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:35:33.839939
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():

    # Create object of class CmdLineFactCollector
    obj = CmdLineFactCollector()

    assert obj.name == 'cmdline'

# Generated at 2022-06-13 02:35:35.369984
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    a = CmdLineFactCollector(None)
    assert a.name == 'cmdline'

# Generated at 2022-06-13 02:35:36.937510
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:35:38.749127
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector._fact_ids == set()
    assert cmdline_collector.name == 'cmdline'

# Generated at 2022-06-13 02:35:39.900182
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()

# Generated at 2022-06-13 02:35:41.748301
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Run collect
    collector = CmdLineFactCollector()
    ansible_facts = collector.collect()

    # Should have collected cmdline and proc_cmdline
    assert 'cmdline' in ansible_facts
    assert 'proc_cmdline' in ansible_facts

# Generated at 2022-06-13 02:35:50.933663
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # create a FakeModule
    module = FakeModule()
    # create an instance of the CmdLineFactCollector
    ccmdline_collector = CmdLineFactCollector(module=module)
    # get the instance of CmdLineFactCollector.collect
    cmdline_collector_collect = ccmdline_collector.collect
    # call the instance of CmdLineFactCollector.collect with a FakeModule
    ansible_facts = cmdline_collector_collect(module=module)
    # check the result of ansible_facts
    assert 'cmdline' in ansible_facts
    assert 'proc_cmdline' in ansible_facts
    # call the instance of CmdLineFactCollector.collect without a FakeModule
    ansible_facts = cmdline_collector_collect()
    # check the result of ansible_

# Generated at 2022-06-13 02:35:56.285610
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Test method collect of class CmdLineFactCollector"""
    cmdline_facts = CmdLineFactCollector().collect()
    cmdline = cmdline_facts.get('cmdline')
    proc_cmdline = cmdline_facts.get('proc_cmdline')
    assert isinstance(cmdline, dict)
    assert isinstance(proc_cmdline, dict)

# Generated at 2022-06-13 02:35:59.641180
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == "cmdline"
    assert obj._fact_ids == set()
    assert obj._get_proc_cmdline() == ''
    assert obj._parse_proc_cmdline('') == {}
    assert obj._parse_proc_cmdline_facts('') == {}

    assert obj.collect() == {}

# Generated at 2022-06-13 02:37:45.513442
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector
    cmdline_fact_collector = CmdLineFactCollector()
    collected_facts = {}
    ansible_facts.set_module_cache_option(True)
    ansible_facts.set_cache_location("/var/lib/ansible/facts_cache")
    collected_facts = cmdline_fact_collector.collect(module=None, collected_facts=collected_facts)
    assert "cmdline" in collected_facts
    assert "proc_cmdline" in collected_facts

# Generated at 2022-06-13 02:37:50.687822
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Set up
    collector = CmdLineFactCollector()

    # Check returns None when the file does not exist
    collector._get_proc_cmdline = lambda: None
    assert collector.collect() == {}

    # Check returns an empty dict when the file exists but is empty
    collector._get_proc_cmdline = lambda: ''
    assert collector.collect() == {}

    # Check returns a dictionary when the file exists and contains data
    collector._get_proc_cmdline = lambda: 'first=second third=fourth'
    assert collector.collect() == {'cmdline': {'first': 'second', 'third': 'fourth'},
                                   'proc_cmdline': {'first': 'second', 'third': 'fourth'}}

# Generated at 2022-06-13 02:37:52.516012
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Test if class CmdLineFactCollector exists
    cmdline_collector_class = globals()['CmdLineFactCollector']
    assert cmdline_collector_class


# Generated at 2022-06-13 02:37:54.580661
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:37:55.870291
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector is not None


# Generated at 2022-06-13 02:38:00.516048
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    assert c.collect() == {}

    c._get_proc_cmdline = lambda: '1 2 3'
    assert c.collect() == {'cmdline': {'1': True, '2': True, '3': True}, 'proc_cmdline': {'1': True, '2': True, '3': True}}

    c._get_proc_cmdline = lambda: '1="2 3"'
    assert c.collect() == {'cmdline': {'1': '2 3'}, 'proc_cmdline': {'1': '2 3'}}

    c._get_proc_cmdline = lambda: '1="2 3"'

# Generated at 2022-06-13 02:38:03.192441
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == "cmdline"

# Unit testing get_file_content

# Generated at 2022-06-13 02:38:04.859574
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:38:07.023241
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector

# Generated at 2022-06-13 02:38:09.146560
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector is not None

# Unit Test for method _get_proc_cmdline() of class CmdLineFactCollector

# Generated at 2022-06-13 02:40:05.959427
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    input = 'ansible=1.2.3.4'
    cmdline_facts = {'cmdline': {'ansible': '1.2.3.4'},
                     'proc_cmdline': {'ansible': ['1.2.3.4']}}
    assert cmdline_facts == CmdLineFactCollector().collect(cmdline=input)



# Generated at 2022-06-13 02:40:06.790873
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:40:08.128566
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    instance = CmdLineFactCollector()
    assert instance is not None
    assert instance.name == 'cmdline'
    assert instance._fact_ids == set()


# Generated at 2022-06-13 02:40:12.559380
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    cmdline_facts = CmdLineFactCollector()

    with patch('ansible.module_utils.facts.collector.get_file_content') as get_file_content_mock:
        expected_cmdline = 'BOOT_IMAGE=/vmlinuz-4.4.0-92-generic root=/dev/mapper/vg1-root ro console=ttyS0'
        get_file_content_mock.return_value = expected_cmdline

        # Test for method collect
        data = cmdline_facts.collect()
        assert data['cmdline']['BOOT_IMAGE'] == '/vmlinuz-4.4.0-92-generic'
        assert data['cmdline']['root'] == '/dev/mapper/vg1-root'
        assert data['cmdline']['ro'] is True


# Generated at 2022-06-13 02:40:20.868760
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Setup
    CmdLineFactCollector._fact_ids.clear()

    # Test
    instance = CmdLineFactCollector()
    fake_stdout = 'root=UUID=fb26e2c2-fdbc-4ed2-99d0-c518e6b37ade ro rootflags=subvol=@,ssd'
    instance._get_proc_cmdline = lambda: fake_stdout
