

# Generated at 2022-06-13 02:30:24.554029
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
      Test class CmdLineFactCollector
      Args:
        None
      Returns:
        None
    """
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    fact_collector = CmdLineFactCollector()
    collected_facts = fact_collector.collect()
    for key in collected_facts['proc_cmdline']:
        assert key
    for key in collected_facts['cmdline']:
        assert key

# Generated at 2022-06-13 02:30:29.412071
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector

    # No idea how to inject a fake /proc/cmdline, so just confirm that return value is expected
    cmdline_fact = CmdLineFactCollector()
    assert cmdline_fact.collect() == {
        'cmdline': {},
        'proc_cmdline': {}
    }

# Generated at 2022-06-13 02:30:37.252394
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Given
    data = '''
    BOOT_IMAGE=/vmlinuz-3.10.0-327.10.1.el7.x86_64 root=/dev/mapper/rhel-root ro crashkernel=auto  resume=/dev/mapper/rhel-swap rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet LANG=en_US.UTF-8
    '''
    with open('/proc/cmdline', 'w') as f:
        f.write(data)

    cmdline_fact_collector = CmdLineFactCollector()

    # When
    collected_facts = cmdline_fact_collector.collect()

    # Then
    assert 'cmdline' in collected_facts
    assert 'proc_cmdline' in collected

# Generated at 2022-06-13 02:30:43.017697
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fact = CmdLineFactCollector()

# Generated at 2022-06-13 02:30:46.141791
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    facts = collector.collect()
    assert 'cmdline' in facts
    assert 'proc_cmdline' in facts

# Generated at 2022-06-13 02:30:49.436138
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:30:58.066783
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = CmdLineFactCollector().collect()
    assert cmdline_facts['cmdline']['root'] == '/dev/sda1'
    assert cmdline_facts['cmdline']['ro'] is True
    assert cmdline_facts['cmdline']['console'] == 'console=tty1'
    assert cmdline_facts['proc_cmdline']['root'] == '/dev/sda1'
    assert cmdline_facts['proc_cmdline']['ro'] == 'ro'
    assert cmdline_facts['proc_cmdline']['console'] == 'console=tty1'


# Generated at 2022-06-13 02:30:59.653015
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'

# Generated at 2022-06-13 02:31:07.452271
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    import sys
    import ansible.module_utils.facts.collectors.command_line as command_line
    facts = command_line.CmdLineFactCollector().collect()
    assert type(facts) == dict, 'Returned: {}'.format(type(facts))
    assert 'cmdline' in facts, 'Returned: {}'.format(facts)
    assert 'proc_cmdline' in facts, 'Returned: {}'.format(facts)
    assert type(facts['cmdline']) == dict, 'Returned: {}'.format(type(facts['cmdline']))
    assert type(facts['proc_cmdline']) == dict, 'Returned: {}'.format(type(facts['proc_cmdline']))

# Generated at 2022-06-13 02:31:18.173681
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    mod_name = 'ansible.module_utils.facts.collectors.cmdline.CmdLineFactCollector'
    mod = __import__(mod_name, fromlist=[''])
    cmdline = mod.CmdLineFactCollector()

    def get_file_content_mock(path):
        data = '''root=/dev/sda2 rw
                  quiet

                  splash=0'''
        return data

    def shlex_split_mock(data, posix):
        return data.split()

    mod.get_file_content = get_file_content_mock
    mod.shlex.split = shlex_split_mock


# Generated at 2022-06-13 02:31:24.746348
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_collector.collect()
    assert cmdline_facts is not None

# Generated at 2022-06-13 02:31:31.963361
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Test method collect of class CmdLineFactCollector
    """
    cmdline_collector = CmdLineFactCollector()
    data = cmdline_collector._get_proc_cmdline()
    expected_cmdline = "/bin/docker-current --add-runtime docker-runc=/usr/libexec/docker/docker-runc-current --default-runtime=docker-runc --authorization-plugin=rhel-push-plugin --exec-opt native.cgroupdriver=systemd --selinux-enabled --signature-verification=false --init-path=/usr/libexec/docker/docker-init-current --userland-proxy-path=/usr/libexec/docker/docker-proxy-current --graph=/var/lib/docker"

# Generated at 2022-06-13 02:31:41.531479
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = lambda a, **b: None

    collected_facts = {}

    cmdline_fact_collector = CmdLineFactCollector()

    def test_get_proc_cmdline(self):
        return 'a=b c d'

    cmdline_fact_collector._get_proc_cmdline = test_get_proc_cmdline

    cmdline_facts = cmdline_fact_collector.collect(TestModule(), collected_facts)

    assert cmdline_facts['cmdline'] == {'a': 'b', 'c': True, 'd': True}
    assert cmdline_facts['proc_cmdline'] == {'a': 'b', 'c': True, 'd': True}

# Generated at 2022-06-13 02:31:43.147055
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert fact_collector.name == 'cmdline'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:31:43.924888
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:31:50.573297
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()

    assert cmdline_facts['cmdline']['console'] == 'ttyS0,115200n8'
    assert cmdline_facts['cmdline']['console'] != 'ttyS0'
    assert cmdline_facts['proc_cmdline']['vga'] == '0x318'


# Generated at 2022-06-13 02:31:58.898062
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    # Arrange:
    #
    # Create a test instance of class CmdLineFactCollector
    # and a class mock, set up with a method side_effect
    from ansible.module_utils.facts.collector import CmdLineFactCollector
    from ansible.module_utils.facts import collector
    test_collector = CmdLineFactCollector()
    mockcollector = collector.Collector()
    mockcollector.get_file_content = lambda x, y=None: 'param1=value1 param2=value2'
    collector.Collector = lambda: mockcollector

    # Act:
    #
    # Invoke the subject method
    #
    result = test_collector.collect()

    # Assert:
    #
    # Check that the expected result was returned
    #

# Generated at 2022-06-13 02:32:00.499003
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 02:32:02.533007
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()

    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()



# Generated at 2022-06-13 02:32:05.483065
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts.name == 'cmdline'
    assert 'cmdline' in cmdline_facts._fact_ids
    assert 'proc_cmdline' in cmdline_facts._fact_ids


# Generated at 2022-06-13 02:32:14.651746
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == "cmdline"

# Generated at 2022-06-13 02:32:23.606611
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Unit test for collect method of CmdLineFactCollector"""
    # Initialize
    cmdline_fact_collector = CmdLineFactCollector()
    data = "BOOT_IMAGE=/vmlinuz-4.4.0-36-generic root=UUID=b3a4d4a4-c4c1-4c1f-8d86-64c1639e9f34 ro console=tty"

    # Execute
    result = cmdline_fact_collector._parse_proc_cmdline_facts(data)

    # Verify

# Generated at 2022-06-13 02:32:25.224679
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:32:35.199456
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content

    # Mock get_file_content
    def mock_get_file_content(path, default=None):
        if path.endswith('/proc/cmdline'):
            return 'ansible_test=test_value'

    original_get_file_content = get_file_content
    get_file_content = mock_get_file_content

    fact_collector = CmdLineFactCollector()
    # Collect facts
    facts = fact_collector.collect()
    assert facts['cmdline'] == {'ansible_test': 'test_value'}
    assert facts['proc_cmdline'] == {'ansible_test': 'test_value'}

    # Clean up
    get_file_content = original_get_file_content

# Generated at 2022-06-13 02:32:37.061084
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:32:39.624898
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert(CmdLineFactCollector().name == 'cmdline')


# Generated at 2022-06-13 02:32:47.740646
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import mock

    m_BaseFactCollector = mock.MagicMock()

    m_BaseFactCollector.return_value.collect.return_value = {
        'cmdline': {'foo': 'Foo', 'bar': 'Bar'},
        'proc_cmdline': {'foo': 'Foo', 'bar': ['Bar', 'Baz']},
    }

    m_get_file_content = mock.MagicMock()
    m_get_file_content.return_value = 'foo=Foo bar=Bar bar=Baz'


# Generated at 2022-06-13 02:32:50.907566
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFactCollector = CmdLineFactCollector()
    assert cmdLineFactCollector


# Generated at 2022-06-13 02:32:54.638323
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert 'cmdline' in collector._fact_ids
    assert 'proc_cmdline' in collector._fact_ids

# Generated at 2022-06-13 02:33:04.778656
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    with open("/proc/cmdline", "w+") as fd:
        fd.write("root=/dev/mapper/vg_test-lv_test ro rd.lvm.lv=vg_test/lv_test rd.dm.uuid=CRYPT-LUKS1-295be7fcabf1408e819425b70913c23f-vg_test-lv_test LANG=en_US.UTF-8 rhgb quiet SYSFONT=latarcyrheb-sun16 crashkernel=auto KEYBOARDTYPE=pc KEYTABLE=uk")

    c = CmdLineFactCollector()
    x = c.collect()
    assert x['proc_cmdline']['root'] == '/dev/mapper/vg_test-lv_test'

# Generated at 2022-06-13 02:33:21.418980
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.collectors.cmdline import CmdLineFactCollector
    from ansible.module_utils.facts import FactManager
    FakeFactManager = FactManager()
    FakeFactManager.add_collection(CmdLineFactCollector)

    test_cmdline = "BOOT_IMAGE=/vmlinuz-3.13.0-55-generic root=UUID=3d3f9c17-7e62-4cbd-8e07-c98e985e5747 ro quiet splash vt.handoff=7"
    cmdline_collector = CmdLineFactCollector()
    result = cmdline_collector._parse_proc_cmdline_facts(test_cmdline)

# Generated at 2022-06-13 02:33:24.121840
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:33:25.986060
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:33:27.922413
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == "cmdline"
    assert cmdline_collector._fact_ids == set()

# Generated at 2022-06-13 02:33:30.149888
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()

# Generated at 2022-06-13 02:33:32.632791
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == "cmdline"
    assert obj._fact_ids == set()

    assert isinstance(obj, BaseFactCollector)

# Generated at 2022-06-13 02:33:41.171030
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    result = CmdLineFactCollector.collect()
    assert result['cmdline']['ro'] is True
    assert result['cmdline']['root'] == '/dev/sda1'
    assert result['cmdline']['rhgb'] is True
    assert result['cmdline']['quiet'] is True
    assert result['cmdline']['console'] == 'ttyS0,115200'
    assert result['cmdline']['noinitrd'] is True
    assert result['cmdline']['boot'] == 'boot'
    assert result['cmdline']['ip'] == '192.168.1.1:::192.168.1.2:255.255.255.0:myhost:eth0:none'

# Generated at 2022-06-13 02:33:44.637200
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    class_inst = CmdLineFactCollector()
    assert class_inst.name == "cmdline"
    assert class_inst._fact_ids == set([])


# Generated at 2022-06-13 02:33:47.842367
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    result = CmdLineFactCollector().collect(collected_facts={})
    cmdline_expected_keys = ['cmdline', 'proc_cmdline']
    assert set(result.keys()) == set(cmdline_expected_keys)

# Generated at 2022-06-13 02:33:49.080170
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():

    x = CmdLineFactCollector()
    assert x.name == 'cmdline'

# Generated at 2022-06-13 02:34:09.425207
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:34:10.930044
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector is not None

# Generated at 2022-06-13 02:34:13.503170
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()
    assert x.name == 'cmdline'
    assert x._fact_ids == set()

# Generated at 2022-06-13 02:34:23.598063
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # mock /proc/cmdline content
    temp_file = open("/proc/cmdline", "w")
    temp_file.write("foo bar=baz abcd=efgh=12345 ijkl=mno pqr\n")
    temp_file.close()
    # make a collector
    cmdline = CmdLineFactCollector()
    # collect results
    results = cmdline.collect()
    # validate our data
    assert results['cmdline']['foo'] == True
    assert results['cmdline']['bar'] == 'baz'
    assert 'abcd' not in results['cmdline']
    assert 'efgh' not in results['cmdline']
    assert results['cmdline']['12345'] == True
    assert results['cmdline']['ijkl'] == 'mno'
   

# Generated at 2022-06-13 02:34:24.209925
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert hasattr(CmdLineFactCollector, 'collect')

# Generated at 2022-06-13 02:34:31.652492
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import ansible.utils.context_objects as context_objects
    CmdLineFactCollectorTestObj = CmdLineFactCollector()
    context_objects.ansible_collector_obj = CmdLineFactCollectorTestObj
    assert(CmdLineFactCollectorTestObj.collect() == {})
    CmdLineFactCollectorTestObj._get_proc_cmdline = lambda : "facts.dummy_key=dummy_value"
    assert(CmdLineFactCollectorTestObj.collect() == {'cmdline': {'facts.dummy_key': 'dummy_value'},
                                                                               'proc_cmdline': {'facts.dummy_key': 'dummy_value'}})

# Generated at 2022-06-13 02:34:37.822167
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cf = CmdLineFactCollector()
    assert cf.name == 'cmdline'
    assert cf._fact_ids == set()
    assert cf._get_proc_cmdline()
    assert cf._parse_proc_cmdline('ro root=/dev/sda2 acpi=off')
    assert cf._parse_proc_cmdline_facts('ro root=/dev/sda2 acpi=off')
    assert cf.collect()

# Generated at 2022-06-13 02:34:44.396117
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Mock the module and collected facts
    module = mock.Mock()
    collected_facts = {}

    # Mock the content of cmdline file
    get_file_content = mock.Mock(
        return_value='foo=bar baz=qux root=/dev/sda1',
    )

    # Set the mocked functions in fact collector
    fact_collector = CmdLineFactCollector()
    fact_collector._get_proc_cmdline = get_file_content

    # Get the output of collect
    result = fact_collector.collect(module, collected_facts)

    # Test the output
    assert result['cmdline'] == {
        'foo': 'bar',
        'baz': 'qux',
        'root': '/dev/sda1',
    }
    assert result['proc_cmdline']

# Generated at 2022-06-13 02:34:46.059366
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_obj = CmdLineFactCollector()
    assert isinstance(cmdline_obj, BaseFactCollector)


# Generated at 2022-06-13 02:34:51.769084
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:35:33.033780
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = collect_cmdline_facts()
    assert cmdline_facts['cmdline']
    assert cmdline_facts['proc_cmdline']


# Generated at 2022-06-13 02:35:35.029479
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts.name == 'cmdline'
    assert cmdline_facts._fact_ids == set()


# Generated at 2022-06-13 02:35:35.548242
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:35:36.565788
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert issubclass(CmdLineFactCollector, BaseFactCollector)


# Generated at 2022-06-13 02:35:38.908941
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # create an instance of class CmdLineFactCollector
    my_obj = CmdLineFactCollector()

    # check if my_obj is an instance of CmdLineFactCollector
    assert isinstance(my_obj, CmdLineFactCollector)

# Generated at 2022-06-13 02:35:39.983386
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector_class = CmdLineFactCollector()
    assert collector_class.name == 'cmdline'

# Generated at 2022-06-13 02:35:40.362780
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    pass

# Generated at 2022-06-13 02:35:44.690296
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()
    cmdline_dict = cmdline_facts.get("cmdline")
    proc_cmdline_dict = cmdline_facts.get("proc_cmdline")
    assert cmdline_dict
    assert proc_cmdline_dict
    assert cmdline_dict["rhgb"] == True
    assert cmdline_dict["quiet"] == True
    assert cmdline_dict["rd.lvm.lv=cl/root"] == True
    assert cmdline_dict["rd.lvm.lv=cl/swap"] == True
    assert cmdline_dict["boot"] == "/dev/mapper/cl-root"
    assert cmdline_dict["resume"] == "/dev/mapper/cl-swap"

# Generated at 2022-06-13 02:35:48.499433
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert fact_collector.name == 'cmdline'
    assert fact_collector._fact_ids == set()

    # CmdLineFactCollector should inherit BaseFactCollector
    assert issubclass(CmdLineFactCollector, BaseFactCollector)


# Generated at 2022-06-13 02:35:49.007630
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:37:24.485284
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    results = cmdline_collector.collect()
    assert isinstance(results, dict)
    assert isinstance(results['cmdline'], dict)
    assert isinstance(results['proc_cmdline'], dict)

# Generated at 2022-06-13 02:37:31.274544
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()

    facts = c.collect(module=None, collected_facts=None)

    assert facts['cmdline']
    assert 'quiet' in facts['cmdline']
    assert facts['cmdline']['quiet'] is True
    assert 'root' in facts['cmdline']
    assert facts['cmdline']['root'] == 'LABEL=cloudimg-rootfs'

    assert facts['proc_cmdline']
    assert 'root' in facts['proc_cmdline']
    assert facts['proc_cmdline']['root'] == 'LABEL=cloudimg-rootfs'



# Generated at 2022-06-13 02:37:35.409829
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    data_in = 'ansible_facts={"ansible_proc_cmdline": "foo=bar", "ansible_cmdline": {"foo": "bar"}}'
    data_expected = {'ansible_facts': {'ansible_proc_cmdline': 'foo=bar', 'ansible_cmdline': {'foo': 'bar'}}}

    collector._get_proc_cmdline = lambda: data_in
    collector._parse_proc_cmdline = lambda x: {}
    collector._parse_proc_cmdline_facts = lambda x: {}
    assert collector.collect() == data_expected


# Generated at 2022-06-13 02:37:36.851095
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'

# Generated at 2022-06-13 02:37:38.900273
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector.collect()

# Generated at 2022-06-13 02:37:41.954146
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFactCollector = CmdLineFactCollector()
    assert cmdLineFactCollector.name == "cmdline"
    assert cmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:37:43.203105
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    module = None
    collected_facts = None
    x = CmdLineFactCollector(module=module, collected_facts=collected_facts)
    assert(x != None)

# Generated at 2022-06-13 02:37:50.041950
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    module = mock.Mock()
    collected_facts = {'cmdline': {'elevator': 'deadline', 'quiet': 'True',
                                   'root': '/dev/sda1', 'boot': 'knoppix_dir',
                                   'newc': 'True', 'ro': 'True', 'break': 'True'},
                       'proc_cmdline': {'elevator': 'deadline', 'quiet': True,
                                        'root': '/dev/sda1', 'boot': 'knoppix_dir',
                                        'newc': True, 'ro': True, 'break': True}}
    cmdline_collector = CmdLineFactCollector(module=module)

    content = 'elevator=deadline quiet root=/dev/sda1 boot=knoppix_dir newc ro break'

# Generated at 2022-06-13 02:37:53.001581
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fc = CmdLineFactCollector()
    cmdline_facts = fc.collect()

    # Test 'cmdline'
    assert cmdline_facts['cmdline'] != {}

    # Test 'proc_cmdline'
    assert cmdline_facts['proc_cmdline'] != {}


# Generated at 2022-06-13 02:37:56.390272
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    fact_ids_of_cmdline = CmdLineFactCollector()._fact_ids
    assert len(fact_ids_of_cmdline) == 0
