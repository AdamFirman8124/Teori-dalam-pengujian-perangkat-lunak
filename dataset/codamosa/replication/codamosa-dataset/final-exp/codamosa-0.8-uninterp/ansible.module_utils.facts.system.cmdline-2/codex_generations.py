

# Generated at 2022-06-13 02:30:20.339722
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert not collector._fact_ids


# Generated at 2022-06-13 02:30:22.282964
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """
    Test class CmdLineFactCollector constructor
    """

    assert CmdLineFactCollector().name == 'cmdline'


# Generated at 2022-06-13 02:30:24.716181
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()

# Generated at 2022-06-13 02:30:27.829392
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    a = CmdLineFactCollector()
    assert a.name == 'cmdline'
    assert a._fact_ids == set()

# Unit test method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:30:33.549906
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert fact_collector.name == 'cmdline'
    assert fact_collector._fact_ids == set()
    assert fact_collector._get_proc_cmdline() == 'BOOT_IMAGE=/boot/vmlinuz-4.4.0-38-generic.efi.signed root=UUID=2f85ab84-d724-41ed-b59e-a9a8a640a1f1 ro console=tty1 console=ttyS0'

# Generated at 2022-06-13 02:30:35.281696
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert set(CmdLineFactCollector._fact_ids) == set()


# Generated at 2022-06-13 02:30:37.459442
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fc = CmdLineFactCollector()
    assert cmdline_fc.name == 'cmdline'
    assert cmdline_fc._fact_ids == set()


# Generated at 2022-06-13 02:30:42.036638
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    module = MockModule()

    cmdline_facts = CmdLineFactCollector(module).collect()

    assert cmdline_facts['cmdline']['ro'] == True
    assert cmdline_facts['cmdline']['root'] == '/dev/sda1'
    assert cmdline_facts['cmdline']['quiet'] == True
    assert cmdline_facts['proc_cmdline']['ro'] == True
    assert cmdline_facts['proc_cmdline']['root'] == '/dev/sda1'
    assert cmdline_facts['proc_cmdline']['quiet'] == True


# Generated at 2022-06-13 02:30:51.984639
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os
    import pytest
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes

    class DummyCmdLineFactCollector(CmdLineFactCollector):
        name = 'cmdline'
        _fact_ids = set()

        def _get_proc_cmdline(self):
            return get_file_content(os.path.join(os.path.dirname(__file__), 'fixtures', 'cmdline'))

    cmdline = DummyCmdLineFactCollector()
    data = cmdline.collect()
    assert 'cmdline' in data
    assert 'proc_cmdline' in data

# Generated at 2022-06-13 02:31:01.382934
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockFactCollector(BaseFactCollector):
        name = 'cmdline'
        _fact_ids = set()

    # Test 1: get_file_content returns a string
    collector = CmdLineFactCollector()
    mock_get_file_content = get_file_content
    mock_get_file_content.return_value = '/proc/cmdline'
    module_parameters = {}

    cmdline_facts = collector.collect(module_parameters)
    assert cmdline_facts['cmdline'] == {'/proc/cmdline': True}
    assert cmdline_facts['proc_cmdline'] == {'/proc/cmdline': True}

    # Test

# Generated at 2022-06-13 02:31:06.060766
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:31:08.571520
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fact_collector = CmdLineFactCollector()
    assert cmd_line_fact_collector.name == 'cmdline'
    assert not cmd_line_fact_collector._fact_ids

# Generated at 2022-06-13 02:31:11.511092
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:31:15.141041
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts.name == 'cmdline'
    assert 'cmdline' not in cmdline_facts._fact_ids
    assert 'proc_cmdline' not in cmdline_facts._fact_ids
#

# Generated at 2022-06-13 02:31:17.061036
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids

# Generated at 2022-06-13 02:31:18.458080
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:31:20.078506
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    test_dict = CmdLineFactCollector()
    assert test_dict.name == 'cmdline'


# Generated at 2022-06-13 02:31:23.738267
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cfg = 'e1000 debug=1'
    cmdline_facts = CmdLineFactCollector()._parse_proc_cmdline_facts(cfg)
    assert cmdline_facts == {'e1000': True, 'debug': '1'}


# Generated at 2022-06-13 02:31:26.866183
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert isinstance(cmdline_collector._fact_ids, set)
    assert len(cmdline_collector._fact_ids) == 0


# Generated at 2022-06-13 02:31:29.364138
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert 'cmdline' == cmdline_fact_collector.name
    assert cmdline_fact_collector._fact_ids == set(['cmdline','proc_cmdline'])

# Generated at 2022-06-13 02:31:34.533029
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'


# Generated at 2022-06-13 02:31:35.683614
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'

# Generated at 2022-06-13 02:31:36.823938
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:31:40.255159
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    cmdline_result = cmdline_fact_collector.collect()

    assert isinstance(cmdline_result, dict) is True
    assert 'cmdline' in cmdline_result
    assert 'proc_cmdline' in cmdline_result

# Generated at 2022-06-13 02:31:41.725895
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    test_collector = CmdLineFactCollector()
    assert test_collector.name == 'cmdline'
    assert test_collector.priority == 6
    assert test_collector._fact_ids == set()

# Generated at 2022-06-13 02:31:51.811932
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import collector

    # Initializing fact collector
    fact_collector = CmdLineFactCollector()

    # Getting collected facts
    collected_facts = fact_collector.collect()

    # Getting the facts supported by this fact collector
    fact_ids = fact_collector.get_supported_facts()

    for fact_id in fact_ids:
        # Checking if the fact is defined in the collected facts
        assert fact_id in collected_facts

    # Checking if the facts are properly formed
    assert isinstance(collected_facts['cmdline'], dict)
    assert isinstance(collected_facts['proc_cmdline'], dict)

    # Making sure that the facts collected can be accessed using the
    # method get_fact_at_path of class FactManager

# Generated at 2022-06-13 02:31:55.639040
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    from ansible.module_utils.facts.collector import MockModule


# Generated at 2022-06-13 02:32:00.700190
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    test_opts = {'option1': 'value1',
                 'option2': 'value2',
                 'option3': 'value3',
                 'option4': 'value4',
                 'option5': 'value5',
                 'option6': 'value6'}

    test_opts_line = " option1=value1 option2=value2 option3=value3 option4=value4 option5=value5 option6=value6 "
    cmdline = CmdLineFactCollector()
    cmdline.collect()

# Generated at 2022-06-13 02:32:08.795918
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    proc_cmdline_file_content = '''rd.lvm.lv=centos/swap rd.lvm.lv=centos/root rhgb quiet LANG=en_US.UTF-8
'''

    # The `set` function is not available in Python 3.4
    try:
        set
    except NameError:
        from sets import Set
        set = Set


# Generated at 2022-06-13 02:32:13.265912
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:32:32.319735
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline = "ro root=LABEL=/ crashkernel=auto rhgb quiet initcall_debug"
    file_handle = open('/proc/cmdline', "w")
    file_handle.write(cmdline)
    file_handle.close()

    data = get_file_content('/proc/cmdline')
    if not data:
        assert()

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


# Generated at 2022-06-13 02:32:34.904221
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()

    assert fact_collector.name == 'cmdline'

# Generated at 2022-06-13 02:32:36.135663
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector is not None

test_CmdLineFactCollector()

# Generated at 2022-06-13 02:32:36.993152
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'


# Generated at 2022-06-13 02:32:39.827966
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.collect() == {}

# Generated at 2022-06-13 02:32:42.326146
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_fact_collector.collect()

    assert cmdline_facts  # cmdline_facts should not be empty

# Generated at 2022-06-13 02:32:45.502210
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """ Test the constructor of class CmdLineFactCollector """

    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert type(cmdline_fact_collector._fact_ids) == set

# Generated at 2022-06-13 02:32:46.592176
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'

# Generated at 2022-06-13 02:32:51.121866
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Create an empty object of class CmdLineFactCollector
    cmd_line_fact_collector = CmdLineFactCollector()

    # Mock method _get_proc_cmdline
    cmd_line_fact_collector._get_proc_cmdline = lambda: 'BOOT_IMAGE=vmlinuz-3.10.0-229.1.2.el7.x86_64 root=/dev/mapper/SystemVG-root ro crashkernel=auto rd.lvm.lv=SystemVG/root rd.lvm.lv=SystemVG/swap rhgb quiet/'

    # Check the result of calling method collect
    result = cmd_line_fact_collector.collect()

# Generated at 2022-06-13 02:32:55.346659
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # create obj
    collector = CmdLineFactCollector()

    # assert name
    assert collector.name == 'cmdline'
    # assert fact ids
    assert len(collector._fact_ids) == 0

# Generated at 2022-06-13 02:33:13.695823
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert isinstance(obj, CmdLineFactCollector)

# Generated at 2022-06-13 02:33:19.590017
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import get_collector_instance

    cmdline_fact_collector = get_collector_instance(CmdLineFactCollector, Collector)

    collected_facts = cmdline_fact_collector.collect()
    assert collected_facts['cmdline']
    assert collected_facts['proc_cmdline']
    assert collected_facts['cmdline'] == collected_facts['proc_cmdline']

# Generated at 2022-06-13 02:33:22.864826
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    c = Collector()
    assert c.collect_cmdline_facts() == CmdLineFactCollector().collect()

# Generated at 2022-06-13 02:33:24.114044
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:33:26.556330
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()

    m = {}
    c.collect(m, None)
    assert m['cmdline'] == dict()
    assert m['proc_cmdline'] == dict()

# Generated at 2022-06-13 02:33:29.492640
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector.priority == 50
    assert cmdline_fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:33:31.744663
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'

# Generated at 2022-06-13 02:33:34.688758
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    facts = c.collect()
    assert 'cmdline' in facts
    assert 'proc_cmdline' in facts
    
# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:33:37.498916
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector(None)
    assert fact_collector is not None
    assert fact_collector.name == 'cmdline'
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:33:38.289971
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    assert True


# Generated at 2022-06-13 02:34:13.686078
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:34:21.410740
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    #
    # Populate necessary data
    #
    # AnsibleModule mock
    class AnsibleModuleMock():
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.params['gather_subset'] = ['all']
            
    #
    # Collect data
    #
    # Collect data
    obj = CmdLineFactCollector()
    collected_facts = obj.collect(AnsibleModuleMock())
    
    #
    # Check
    #
    assert collected_facts['cmdline'] != {}
    assert collected_facts['proc_cmdline'] != {}

# Generated at 2022-06-13 02:34:31.389182
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Setup
    input_data = 'BOOT_IMAGE=/vmlinuz-3.10.0-327.el7.x86_64 root=UUID=b0cc064d-22c1-42d6-8f30-129083b5d6e5 ro crashkernel=auto rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet LANG=en_US.UTF-8'


# Generated at 2022-06-13 02:34:38.400113
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Unit test for empty constructor of class CmdLineFactCollector
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert not collector._fact_ids

    # Unit test for constructor of class CmdLineFactCollector with arguments
    collector = CmdLineFactCollector(name='testcmdline', fact_ids=['testcmdline'])
    assert collector.name == 'testcmdline'
    assert len(collector._fact_ids) == 1
    assert collector._fact_ids == set(['testcmdline'])

# Generated at 2022-06-13 02:34:44.773841
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # monkey patching get_file_content so as to only return read data
    CmdLineFactCollector._get_proc_cmdline = lambda x: 'foo=bar baz sss'
    # testing collection of facts
    cmd_line_fact = CmdLineFactCollector()
    # assert cmd_line_fact.collect(module=None, collected_facts=None) == {'cmdline': {'foo': 'bar', 'baz': True, 'sss': True}, 'proc_cmdline': {'foo': 'bar', 'baz': True, 'sss': True}}

# Generated at 2022-06-13 02:34:46.526631
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()

#

# Generated at 2022-06-13 02:34:51.820739
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Initialization
    CmdLineFactCollector.init()
    collector = CmdLineFactCollector()

    # Test function collect
    cmdline_content = 'foo=bar baz=bam'
    cmdline_facts = {
        'cmdline': {
            'foo': 'bar',
            'baz': 'bam',
        },
        'proc_cmdline': {
            'foo': 'bar',
            'baz': 'bam',
        },
    }
    CmdLineFactCollector._get_proc_cmdline = lambda x: cmdline_content
    assert collector.collect() == cmdline_facts


# Generated at 2022-06-13 02:35:02.676149
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    '''
    Unit test of method collect of class CmdLineFactCollector
    '''
    # result = CmdLineFactCollector().collect()
    # assert result == {'cmdline': {'console': 'ttyS0', 'ip': '192.168.122.49::192.168.122.1:255.255.255.0:localhost.localdomain:eth0:none', 'nofb': True, 'root': '/dev/mapper/VolGroup-lv_root', 'ro': True, 'selinux': '0', 'S': 'rhl-base-4.4.6-5.el7.x86_64', 'vga': '0x314'}, 'proc_cmdline': {'console': 'ttyS0', 'ip': '192.168.122.49::192.168.122

# Generated at 2022-06-13 02:35:04.253366
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line = CmdLineFactCollector()

# Generated at 2022-06-13 02:35:05.102836
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:36:34.265262
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj1 = CmdLineFactCollector()
    assert obj1.name == "cmdline"
    assert obj1._fact_ids == set()

# Generated at 2022-06-13 02:36:42.344525
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    try:
        from ansible.module_utils.facts.utils.get_file_content import get_file_content
        from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector
    except ImportError:
        import pytest
        pytest.skip("ansible.module_utils.facts.utils.get_file_content "
                    "or CmdLineFactCollector module is not imported")

    class TestModule(object):
        def __init__(self):
            pass

    cmdline_fact_collector = CmdLineFactCollector()

    get_file_content_orig = get_file_content

    def mock_get_file_content(file_path):
        assert file_path == '/proc/cmdline'

# Generated at 2022-06-13 02:36:44.178353
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFactCollector = CmdLineFactCollector()
    assert cmdLineFactCollector.name == 'cmdline'
    assert cmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:36:51.182210
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Patch get_file_content
    def fake_get_file_content(path):
        return 'console=ttyS0,38400n8 net.ifnames=0 biosdevname=0 root=/dev/mapper/CentOS-root ro rd.lvm.lv=CentOS/root rd.lvm.lv=CentOS/swap rhgb quiet'

    get_file_content_original = CmdLineFactCollector._get_proc_cmdline
    CmdLineFactCollector._get_proc_cmdline = fake_get_file_content

    data = CmdLineFactCollector().collect()

    CmdLineFactCollector._get_proc_cmdline = get_file_content_original


# Generated at 2022-06-13 02:36:52.335723
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    result = isinstance(CmdLineFactCollector(), CmdLineFactCollector)
    assert result == True

# Generated at 2022-06-13 02:37:01.973731
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    class FakeClass(BaseFactCollector):
        name = 'fake'
        _fact_ids = set()

        def __init__(self):
            self.test_data_1 = 'fake_data_1'
            self.test_data_2 = 'fake_data_2'

        def collect(self, module=None, collected_facts=None):
            pass

    class FakeClass2(FakeClass):
        name = 'fake2'

    class FakeClass3(FakeClass):
        name = 'fake3'

    obj = CmdLineFactCollector()

    obj._get_proc_cmdline = lambda: 'fake_1=fake_data_1 fake_2=fake_data_2'
    actual = obj.collect()

# Generated at 2022-06-13 02:37:02.838689
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:37:12.388383
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_content = 'debug panic=1 quiet apic=debug console=ttyS0,115200n8'
    cmdline_facts = {'cmdline': {'debug': True, 'panic': '1', 'quiet': True, 'apic': 'debug', 'console': 'ttyS0,115200n8'},
                     'proc_cmdline': {'debug': True, 'panic': '1', 'quiet': True, 'apic': 'debug', 'console': 'ttyS0,115200n8'}}

    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = lambda: cmdline_content
    result = collector.collect()

    assert result == cmdline_facts

# Generated at 2022-06-13 02:37:22.014408
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector(None)

    cmdline_collector._get_proc_cmdline = lambda : "BOOT_IMAGE=/vmlinuz-4.15.0-20-generic root=/dev/mapper/ubuntu--vg-root ro"
    cmdline_collector._parse_proc_cmdline = lambda x: dict(x.split())
    cmdline_collector._parse_proc_cmdline_facts = lambda x: dict(x.split())

    cmdline_facts = cmdline_collector.collect()
    assert cmdline_facts['cmdline'] == {'BOOT_IMAGE': '/vmlinuz-4.15.0-20-generic',
                                        'root': '/dev/mapper/ubuntu--vg-root',
                                        'ro': True}
    assert cmdline_

# Generated at 2022-06-13 02:37:30.285104
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()

    # Test command line dictionary
    cmdline_dict = fact_collector._parse_proc_cmdline('foo bar=baz x=y')
    assert 'foo' in cmdline_dict
    assert cmdline_dict['foo'] is True
    assert 'bar' in cmdline_dict
    assert cmdline_dict['bar'] == 'baz'
    assert 'x' in cmdline_dict
    assert cmdline_dict['x'] == 'y'
    assert 'cmdline' in cmdline_dict
    assert cmdline_dict['cmdline'] is False

    # Test command line facts dictionary
    # Test duplicate keys
    cmdline_facts = fact_collector._parse_proc_cmdline_facts('foo bar=baz bar=baz2')
    assert 'foo'