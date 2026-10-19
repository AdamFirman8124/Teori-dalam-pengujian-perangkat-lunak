

# Generated at 2022-06-13 02:30:20.589864
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    module = None
    collected_facts = None
    c = CmdLineFactCollector(module, collected_facts)
    # call method
    result = c.collect()
    assert isinstance(result, dict)

# Generated at 2022-06-13 02:30:28.015791
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Test object initialization with empty object
    cmdline_obj = CmdLineFactCollector()
    assert cmdline_obj != None

    # Test object initialization with empty object
    cmdline_obj = CmdLineFactCollector({})
    assert cmdline_obj != None

    # Test method collect() with empty data
    ret_val = cmdline_obj.collect()
    assert len(ret_val) == 0

    # Test method collect() with data
    ret_val = cmdline_obj.collect('/proc/cmdline')
    assert len(ret_val) != 0


# Generated at 2022-06-13 02:30:29.801767
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
  cmdline_facts = CmdLineFactCollector()
  assert cmdline_facts is not None


# Generated at 2022-06-13 02:30:31.333270
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()


# Generated at 2022-06-13 02:30:33.162520
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    result = CmdLineFactCollector().collect()
    assert result.get('cmdline')
    assert result.get('proc_cmdline')

# Generated at 2022-06-13 02:30:34.949745
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cf = CmdLineFactCollector()
    assert cf.name == 'cmdline'
    assert cf._fact_ids == set()

# Generated at 2022-06-13 02:30:38.140872
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector is not None
    assert cmdline_fact_collector.name == 'cmdline'
    assert isinstance(cmdline_fact_collector._fact_ids, set)

# Generated at 2022-06-13 02:30:41.290682
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()
    assert x.name == 'cmdline'
    assert 'cmdline' in x._fact_ids
    assert 'proc_cmdline' in x._fact_ids

# Generated at 2022-06-13 02:30:51.541869
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    module = AnsibleModule(
        argument_spec=dict()
    )
    # Test case no. 1:
    # File "/proc/cmdline" is empty, collect() should return empty dict

    f_module = AnsibleModule(
        argument_spec=dict()
    )

    f_collector = CmdLineFactCollector()
    f_collector._get_proc_cmdline = lambda: ''

    assert f_collector.collect(module=f_module) == {}

    # Test case no. 2:
    # File "/proc/cmdline" has at least 1 key/value pair, dict returned by
    # method collect() should contain also key 'cmdline' and
    # key 'proc_cmdline'

    s_module = AnsibleModule(
        argument_spec=dict()
    )

    s_collector

# Generated at 2022-06-13 02:30:59.085691
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    class CmdLineFactCollectorMock(CmdLineFactCollector):
        def _get_proc_cmdline(self):
            return 'foo=bar bar=foo baz=qux'
    c = Collector(CmdLineFactCollectorMock)
    assert c.collect() == {'cmdline': {'foo': 'bar', 'bar': 'foo', 'baz': 'qux'}, 'proc_cmdline': {'foo': ['bar', 'bar'], 'bar': 'foo', 'baz': 'qux'}}

# Generated at 2022-06-13 02:31:09.122898
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:31:12.004939
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    stuff = CmdLineFactCollector()
    assert stuff
    assert stuff.name == 'cmdline'
    assert not stuff._fact_ids

# Generated at 2022-06-13 02:31:21.739031
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    '''Unit test for method collect of class CmdLineFactCollector'''

    output={}
    output['cmdline']={'BOOT_IMAGE':'/@/boot/vmlinuz-4.12.9-300.fc26.x86_64', 'BOOTIF':'01-54-a2-af-b9-22-9f', 'crashkernel':'auto', 'rd.driver.blacklist':'nouveau', 'rhgb':'quiet', 'ro':'', 'root':'/dev/mapper/fedora-root', 'rootflags':'rw', 'rootfstype':'ext4', 'uuid':'d139bdc0-e5ab-48e5-811c-da1f6b9a6e09'}

# Generated at 2022-06-13 02:31:29.995998
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = 'BOOT_IMAGE=/vmlinuz-3.10.0-327.28.3.el7.x86_64 root=/dev/mapper/rhel-root ro crashkernel=auto rd.lvm.lv=rhel/swap vconsole.font=latarcyrheb-sun16 rd.lvm.lv=rhel/root vconsole.keymap=us rhgb quiet'

    cmdline_fact_collector = CmdLineFactCollector(module=None, collected_facts=None)

    assert cmdline_fact_collector._get_proc_cmdline() == data


# Generated at 2022-06-13 02:31:34.998595
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_fact_collector.collect()
    assert isinstance(cmdline_facts, dict)
    assert cmdline_facts.get('cmdline') is not None
    assert cmdline_facts.get('proc_cmdline') is not None

# Generated at 2022-06-13 02:31:37.095210
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()

    assert cmdline_collector.collect() == {'cmdline': {}, 'proc_cmdline': {}}

# Generated at 2022-06-13 02:31:38.997882
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cf = CmdLineFactCollector()
    if cf.collect(None, None) is not None:
        assert True
    else:
        assert False

# Generated at 2022-06-13 02:31:42.053009
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj1 = CmdLineFactCollector()
    obj2 = CmdLineFactCollector()
    assert obj1._name == obj2._name and obj1._fact_ids == obj2._fact_ids and obj1._collected_facts == obj2._collected_facts 


# Generated at 2022-06-13 02:31:46.244048
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()
    assert collector._get_proc_cmdline is not None
    assert collector._parse_proc_cmdline is not None
    assert collector._parse_proc_cmdline_facts is not None
    assert collector.collect is not None

# Generated at 2022-06-13 02:31:56.074077
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils._text import to_bytes

    CmdLineFactCollector._get_proc_cmdline = lambda self: to_bytes('foo=bar # test\n')

    assert CmdLineFactCollector._parse_proc_cmdline_facts(None) == {}
    assert CmdLineFactCollector._parse_proc_cmdline_facts('') == {}
    assert CmdLineFactCollector._parse_proc_cmdline(' ') == {}
    assert CmdLineFactCollector._parse_proc_cmdline('foo=') == {'foo': True}
    assert CmdLineFactCollector._parse_proc_cmdline('foo=bar') == {'foo': 'bar'}

# Generated at 2022-06-13 02:32:21.364330
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class CmdLineFactCollector_under_test(CmdLineFactCollector):
        def _get_proc_cmdline(self):
            return "aaa=bbb quiet ccc=ddd=eee fff=ggg=hhh=iii"

    expected_cmdline_facts = {'cmdline': {'aaa': 'bbb',
                                          'ccc': 'ddd=eee',
                                          'fff': 'ggg=hhh=iii',
                                          'quiet': True},
                              'proc_cmdline': {'aaa': 'bbb',
                                               'ccc': ['ddd=eee'],
                                               'fff': ['ggg=hhh=iii'],
                                               'quiet': True}}

    collector = CmdLineFactCollector_under_test()

    actual_cmdline

# Generated at 2022-06-13 02:32:25.716965
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fc = CmdLineFactCollector()

    result = cmdline_fc.get_fact_names()

    assert result == {'cmdline', 'proc_cmdline'}

# Generated at 2022-06-13 02:32:26.569351
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector()


# Generated at 2022-06-13 02:32:30.855834
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    '''
    Constructor must:
    * set attribute `name`
    * set attribute `_fact_ids` with empty set
    '''
    cmd_line_fact_collector = CmdLineFactCollector()
    assert cmd_line_fact_collector.name == 'cmdline'
    assert cmd_line_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:32:33.949522
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    '''Unit test for method collect of class CmdLineFactCollector'''
    CmdLineFactCollector().collect()


# Generated at 2022-06-13 02:32:34.860413
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:32:37.659297
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()


# Generated at 2022-06-13 02:32:40.222582
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert fact_collector is not None

# Generated at 2022-06-13 02:32:46.005178
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert isinstance(collector._fact_ids, set)
    assert collector.collect() == {'cmdline': {}, 'proc_cmdline': {}}
    assert isinstance(collector._get_proc_cmdline(), str)
    assert isinstance(collector._parse_proc_cmdline('/proc/cmdline'), dict)
    assert isinstance(collector._parse_proc_cmdline_facts('/proc/cmdline'), dict)


# Generated at 2022-06-13 02:32:51.714262
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdfac = CmdLineFactCollector()
    data = '''BOOT_IMAGE=/vmlinuz-3.12.0-5-amd64 root=UUID=72bb93b0-a566-48c8-a5e9-ffd1c5a5a350 ro resolvconf=off'''
    cmdfac._get_proc_cmdline = lambda: data
    cmdline_facts = cmdfac.collect()


# Generated at 2022-06-13 02:33:26.627115
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert 'cmdline' in cmdline_fact_collector.name
    assert 'cmdline' in cmdline_fact_collector.__class__.__name__

# Generated at 2022-06-13 02:33:29.649562
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    test_cmdline = 'cmdline1=True cmdline2=value'
    cmdline_collector = CmdLineFactCollector()
    cmdline_collector._get_proc_cmdline = lambda: test_cmdline
    cmdline_collector.collect()

# Generated at 2022-06-13 02:33:32.400075
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == "cmdline"
    assert collector._fact_ids == {"cmdline", "proc_cmdline"}


# Generated at 2022-06-13 02:33:34.441467
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'


# Generated at 2022-06-13 02:33:37.875130
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    '''
    Constructor of class CmdLineFactCollector should be working after
    the creation of an instance of this variable
    '''
    cmdline_fact_collector = CmdLineFactCollector()
    assert isinstance(cmdline_fact_collector,BaseFactCollector)


# Generated at 2022-06-13 02:33:38.368862
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:33:41.000872
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline = CmdLineFactCollector()
    result = cmdline.collect()
    assert isinstance(result, dict)
    assert isinstance(result['cmdline'], dict)
    assert isinstance(result['proc_cmdline'], dict)

# Generated at 2022-06-13 02:33:46.844503
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import ModuleArgsParser

    # Test data
    ArgParser = ModuleArgsParser()
    args = ArgParser.parse_kv(None)
    module = args.pop('module', None)
    collected_facts = args.pop('collected_facts', None)

    # Testing
    CmdLineFactCollectorObj = CmdLineFactCollector()
    result = CmdLineFactCollectorObj.collect(module=module, collected_facts=collected_facts)
    assert result['proc_cmdline']['root'] == '/dev/mapper/centos-root ro'
    assert result['proc_cmdline']['rd.lvm.lv'] == ['/dev/centos/root', '/dev/centos/swap']
    assert result['proc_cmdline']['removable']

# Generated at 2022-06-13 02:33:53.559177
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    module = 'ansible_facts.cmdline.CmdLineFactCollector'
    cmdline_facts_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_facts_collector.collect(module)

    assert isinstance(cmdline_facts, dict)
    assert isinstance(cmdline_facts['cmdline'], dict)
    assert isinstance(cmdline_facts['proc_cmdline'], dict)
    assert cmdline_facts['cmdline']['ro']
    assert cmdline_facts['proc_cmdline']['ro'] == [True]
    assert cmdline_facts['cmdline']['root'] == '/dev/mapper/centos-root'
    assert cmdline_facts['proc_cmdline']['root'] == '/dev/mapper/centos-root'

# Generated at 2022-06-13 02:33:56.435980
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()

    actual_facts = collector.collect()
    assert isinstance(actual_facts, dict)
    assert actual_facts['cmdline']
    assert actual_facts['proc_cmdline']

# Generated at 2022-06-13 02:34:34.647825
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdLineFactCollector = CmdLineFactCollector()
    assert(cmdLineFactCollector.name == 'cmdline')

# Generated at 2022-06-13 02:34:35.720577
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
  assert CmdLineFactCollector._get_proc_cmdline() != "None"

# Generated at 2022-06-13 02:34:43.557118
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import FactCache, utils
    from ansible.module_utils.facts._text import to_text

    # Get required command line options
    base_dir = os.path.dirname(os.path.realpath(__file__))
    opts_file = os.path.join(base_dir, 'cmdline.opts')

    my_collector = Collector

    # Playbook uses 'cmdline' as fact name
    my_collector.add_collector(CmdLineFactCollector)

    # Mock AnsibleModule
    mymodule = type('module', (object,), {})
    mymodule.params = utils.safe_load(get_file_content(opts_file))

    # This

# Generated at 2022-06-13 02:34:44.749295
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector



# Generated at 2022-06-13 02:34:47.281390
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """Test the environment fact collector."""
    assert(CmdLineFactCollector.name == 'cmdline')
    assert(CmdLineFactCollector._fact_ids == set())
    assert(isinstance(CmdLineFactCollector._fact_ids, set))


# Generated at 2022-06-13 02:34:52.602917
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert set(c.collect().keys()) == c._fact_ids
    assert c._get_proc_cmdline() == get_file_content('/proc/cmdline')
    assert c._parse_proc_cmdline('foo') == { 'foo': True }
    assert c._parse_proc_cmdline('foo=bar') == { 'foo': 'bar' }
    assert c._parse_proc_cmdline('foo=bar baz=qux') == { 'foo': 'bar', 'baz': 'qux' }
    assert c._parse_proc_cmdline_facts('foo') == { 'foo': True }
    assert c._parse_proc_cmdline_facts('foo=bar') == { 'foo': 'bar' }
   

# Generated at 2022-06-13 02:35:02.865123
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Test case for method collect of class CmdLineFactCollector.
    :return:
    """
    collector = CmdLineFactCollector()

    # read the cmdline file
    collector._get_proc_cmdline = lambda: 'root=UUID=7ca21a6c-0c58-4dab-a7b9-2e838d342cc6 ro rootflags=subvol=__active/root quiet'

    cmdline_facts = collector.collect()

    assert cmdline_facts['cmdline'] == {
        'root': 'UUID=7ca21a6c-0c58-4dab-a7b9-2e838d342cc6',
        'ro': True,
        'rootflags': 'subvol=__active/root',
        'quiet': True,
    }

# Generated at 2022-06-13 02:35:03.802206
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()
    assert collector.collect() == {}


# Generated at 2022-06-13 02:35:04.458783
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    r = CmdLineFactCollector()
    assert r.name == 'cmdline'

# Generated at 2022-06-13 02:35:05.911145
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'


# Generated at 2022-06-13 02:36:31.855001
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector(None)
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()


# Generated at 2022-06-13 02:36:33.051582
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector.priority == 60

# Generated at 2022-06-13 02:36:41.089307
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()

    # Test cmdline parsing
    cmdline_proc_content = "BOOT_IMAGE=/vmlinuz-4.4.0-92-generic root=/dev/mapper/vg_np1-lv_root ro console=tty1 console=ttyS0,115200n8"
    cmdline_dict_proc_content = {
        'BOOT_IMAGE': '/vmlinuz-4.4.0-92-generic',
        'root': '/dev/mapper/vg_np1-lv_root',
        'ro': True,
        'console': ['tty1', 'ttyS0,115200n8'],
    }

# Generated at 2022-06-13 02:36:45.055423
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():

    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()
    assert isinstance(CmdLineFactCollector._fact_ids, set)

    c = CmdLineFactCollector()
    assert c
    assert c.name == 'cmdline'
    assert c._fact_ids == set()
    assert isinstance(c._fact_ids, set)



# Generated at 2022-06-13 02:36:47.564369
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
   # Testing normal constructor
   test_CmdLineFactCollector = CmdLineFactCollector()
   if test_CmdLineFactCollector:
      print("Pass")


if __name__ == '__main__':
   test_CmdLineFactCollector()

# Generated at 2022-06-13 02:36:49.752614
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()

    assert cmdline_facts and 'cmdline' in cmdline_facts and 'proc_cmdline' in cmdline_facts

# Generated at 2022-06-13 02:36:51.923223
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()
    assert c._command == 'cat /proc/cmdline'


# Generated at 2022-06-13 02:36:52.588948
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector

# Generated at 2022-06-13 02:36:53.816896
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()


# Generated at 2022-06-13 02:37:03.748824
# Unit test for method collect of class CmdLineFactCollector