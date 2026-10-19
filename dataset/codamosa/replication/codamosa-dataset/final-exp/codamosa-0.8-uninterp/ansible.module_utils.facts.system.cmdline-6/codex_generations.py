

# Generated at 2022-06-13 02:30:19.235176
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cfac = CmdLineFactCollector()
    assert cfac.name == 'cmdline'
    assert cfac._fact_ids == set()


# Generated at 2022-06-13 02:30:21.027387
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == "cmdline"


# Generated at 2022-06-13 02:30:27.024919
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os

    data = 'root=UUID=b79caaa0-3e10-4b68-88a1-99bff5d5dc5e ro radar=none quiet console=ttyS0,38400n8'
    cmdline_data = {'root': 'UUID=b79caaa0-3e10-4b68-88a1-99bff5d5dc5e',
                    'ro': True,
                    'radar': 'none',
                    'quiet': True,
                    'console': 'ttyS0,38400n8'
                    }

# Generated at 2022-06-13 02:30:28.069797
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:30:28.588611
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:30:37.960042
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    import os

    cmdline_facts = CmdLineFactCollector().collect()
    cmdline_facts_dict = cmdline_facts['cmdline']
    proc_cmdline_facts_dict = cmdline_facts['proc_cmdline']
    assert '/sbin/init' in cmdline_facts_dict['init']
    assert 'ro' in cmdline_facts_dict['root']
    assert '/dev/mapper/centos-root' in cmdline_facts_dict['root']
    assert cmdline_facts_dict['console'] == 'tty0'
    assert cmdline_facts_dict['console'] == 'tty0'
    assert cmdline_facts_dict['console'] == '/dev/tty0'
    assert cmdline_

# Generated at 2022-06-13 02:30:41.548412
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()

    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:30:49.102698
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Create an instance of TestModuleRouter
    mr = TestModuleRouter()

    # Create an instance of CmdLineFactCollector
    cfc = CmdLineFactCollector(mr)

    # Create an instance of TestAnsibleModule
    tam = TestAnsibleModule()

    # Call method collect of class CmdLineFactCollector
    results = cfc.collect(tam)

    # Check assertions
    assert results == {'cmdline': {}, 'proc_cmdline': {}}


# Generated at 2022-06-13 02:30:51.694275
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:31:01.146042
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collector import FactsCache
    facts_cache = FactsCache()
    facts_cache['cmdline'] = ""
    fact_collector = FactCollector(facts_cache)
    third_party_collector = CmdLineFactCollector(fact_collector)
    data = "ro boot=live persistence persistence-label=live-rw quiet splash vga=current --"
    third_party_collector._get_proc_cmdline = lambda: data
    result = third_party_collector.collect()

# Generated at 2022-06-13 02:31:15.547411
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """ Unit test for method collect of class CmdLineFactCollector """

    # Unit test for method collect of class CmdLineFactCollector
    # with first_seen = True
    mod_2 = {
        "COLLECTOR_FIRST_SEEN": True
    }
    mod_3 = {
        "COLLECTOR_FIRST_SEEN": True
    }
    mod_4 = {
        "COLLECTOR_FIRST_SEEN": True
    }

    # Unit test for method collect of class CmdLineFactCollector
    # with first_seen = False
    mod_1 = {
        "COLLECTOR_FIRST_SEEN": False
    }
    mod_8 = {
        "COLLECTOR_FIRST_SEEN": True
    }

# Generated at 2022-06-13 02:31:17.930971
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 02:31:19.263531
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    assert CmdLineFactCollector.collect(None, None)

# Generated at 2022-06-13 02:31:28.099799
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    test_obj = CmdLineFactCollector()
    test_obj._get_proc_cmdline = lambda :'vmlinuz-3.10.0-327.36.3.el7.x86_64 root=/dev/mapper/rhel-root ro rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet nvme.default_ps_max_latency_us=5500'
    test_obj._parse_proc_cmdline = lambda x: test_obj._parse_proc_cmdline_facts(x)
    test_obj._parse_proc_cmdline_facts = lambda x: dict(map(lambda y: y.split('=', 1), shlex.split(x, posix=False)))

# Generated at 2022-06-13 02:31:38.103105
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils import basic
    import collections
    import pytest
    from ansible.module_utils.facts.collector.cmdline import CmdLineFactCollector
    import mock
    import ansible.module_utils.facts.collector

    with mock.patch.object(CmdLineFactCollector, '_get_proc_cmdline') as get_proc_cmdline:
        get_proc_cmdline.return_value = "root=/dev/sda1 quiet ip=192.168.56.10::192.168.56.1:255.255.255.0:ipa-centos-7:enp0s8:none nameserver=192.168.1.1 nameserver=8.8.8.8"
        collected_facts = {}

# Generated at 2022-06-13 02:31:44.744521
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    base_obj = BaseFactCollector()

    CmdLine_obj = CmdLineFactCollector()

    def _get_proc_cmdline():
        return get_file_content('/proc/cmdline')

    base_obj._parse_proc_cmdline = CmdLine_obj._parse_proc_cmdline
    base_obj._parse_proc_cmdline_facts = CmdLine_obj._parse_proc_cmdline_facts
    base_obj._get_proc_cmdline = _get_proc_cmdline

    cmdline_facts = base_obj.collect(module=None, collected_facts=None)


# Generated at 2022-06-13 02:31:46.614306
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert isinstance(collector, CmdLineFactCollector)

# Generated at 2022-06-13 02:31:56.423830
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline = CmdLineFactCollector()

    cmdline._get_proc_cmdline = lambda: 'memtest=test quiet loglevel=3 audit=0 numa=off'

    cmdline_facts = cmdline.collect()

    assert cmdline_facts['cmdline'] == {'memtest': 'test', 'quiet': True, 'loglevel': '3', 'audit': '0', 'numa': 'off'}
    assert cmdline_facts['proc_cmdline'] == {'memtest': 'test', 'quiet': True, 'loglevel': '3', 'audit': '0', 'numa': 'off'}

    cmdline._get_proc_cmdline = lambda: 'memtest=test memtest=memtest1 quiet loglevel=3 audit=0 numa=off'

    cmdline_facts

# Generated at 2022-06-13 02:31:57.914186
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'

# Generated at 2022-06-13 02:32:04.628337
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class CmdLineFactCollectorTest:

        def __init__(self):
            self.content = 'root=/dev/mapper/vg00-lv_root rw no_timer_check console=ttyS0,38400n8 console=tty0'

        def _get_proc_cmdline(self):
            return self.content

    collector_test = CmdLineFactCollectorTest()

    cmdline_collector = CmdLineFactCollector()
    cmdline_collector.collector = collector_test.__class__

    cmdline_results = cmdline_collector.collect()
    cmdline_dict = cmdline_results['cmdline']
    proc_cmdline_dict = cmdline_results['proc_cmdline']

    assert len(cmdline_dict) == len(proc_cmdline_dict)


# Generated at 2022-06-13 02:32:12.015870
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()

# Generated at 2022-06-13 02:32:14.466983
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Unit test for method collect of class CmdLineFactCollector"""
    
    # Can't test collect as it depends on reading a file (/proc/cmdline)
    pass

# Generated at 2022-06-13 02:32:15.374885
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    return CmdLineFactCollector()

# Generated at 2022-06-13 02:32:19.650923
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:32:23.751891
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = 'foo=bar baz=quux'
    fact_collector = CmdLineFactCollector()

    cmdline_facts = fact_collector.collect(collected_facts={})

    assert cmdline_facts == {'cmdline': {'foo': 'bar', 'baz': 'quux'}, 'proc_cmdline': {'foo': 'bar', 'baz': 'quux'}}
    assert isinstance(cmdline_facts, dict)


# Generated at 2022-06-13 02:32:25.313067
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    print(c)


# Generated at 2022-06-13 02:32:35.240836
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Creating instance of class CmdLineFactCollector
    cmdline_fact_collector = CmdLineFactCollector()
    assert isinstance(cmdline_fact_collector, CmdLineFactCollector)

    # Creating dummy /proc/cmdline file
    proc_cmdline_file = open("/proc/cmdline", "w")
    proc_cmdline_file.write("ro root=UUID=1e6cd52d-7d17-4ee2-8c20-cebbc6f9086d systemd.log_color=0 quiet")
    proc_cmdline_file.close()

    # Executing method collect of class CmdLineFactCollector
    collected_facts = cmdline_fact_collector.collect()

    # Removing dummy /proc/cmdline file
    import os

# Generated at 2022-06-13 02:32:39.593601
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible_collections.ansible.community.plugins.module_utils.facts import collector

    cmd_line_collector = CmdLineFactCollector()
    cmd_line_dict = cmd_line_collector.collect()

    assert isinstance(cmd_line_dict, dict)
    assert 'cmdline' in cmd_line_dict
    assert 'proc_cmdline' in cmd_line_dict

# Generated at 2022-06-13 02:32:41.780319
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector is not None
    assert collector.name == 'cmdline'
    assert len(collector._fact_ids) == 0

# Generated at 2022-06-13 02:32:47.459051
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """
    Unit test for method collect of class CmdLineFactCollector.
    """
    test_input = 'root=UUID=a07d70df-9e6d-496a-80fa-cc7f1cacd6ff ro root=UUID=e930f291-1821-4f91-b11f-1d0a35c905d8 rhgb quiet audit=1 KEYTABLE=us'
    test_data = 'root=UUID=a07d70df-9e6d-496a-80fa-cc7f1cacd6ff ro root=UUID=e930f291-1821-4f91-b11f-1d0a35c905d8 rhgb quiet audit=1 KEYTABLE=us'

    collector = CmdLineFactCollector()
    collector._get_proc

# Generated at 2022-06-13 02:32:59.681874
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    def _get_proc_cmdline():
        return "A=x B C=y"

    def _get_proc_cmdline_empty():
        return ""

    cmdline_facts = {'cmdline': {'A': 'x', 'B': True, 'C': 'y'},
                     'proc_cmdline': {'A': 'x', 'B': True, 'C': ['y']}}
    empty_cmdline_facts = {'cmdline': {},
                           'proc_cmdline': {}}

    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = _get_proc_cmdline
    collector_result = collector.collect()
    assert collector_result == cmdline_facts

    collector = CmdLineFactCollector()
    collector._get_proc_cmdline = _get_

# Generated at 2022-06-13 02:33:09.547273
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector import CmdLineFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    module = Collector()
    module.params = {}
    module.collected_facts = {}
    module.collector = CmdLineFactCollector(module=module)
    get_file_content.clear_cache()

    get_file_content.cache_data['/proc/cmdline'] = 'key1=1 value1 key2=2 value2'
    result = module.collector._parse_proc_cmdline(get_file_content('/proc/cmdline'))

# Generated at 2022-06-13 02:33:18.690551
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    file = '../tests/unit/module_utils/facts/output/proc/cmdline'
    f = open(file)
    cmdline = f.read().strip('\n')
    f.close()
    cmdline = cmdline.splitlines()
    cmdline_list = []
    # Add an empty string in the beginning to compare with output of shlex
    cmdline_list.append('')
    for line in cmdline:
        cmdline_list.append(line)
    cmdline_facts = {}
    cmdline_facts['cmdline'] = {}
    cmdline_facts['proc_cmdline'] = {}
    for i in cmdline_list:
        cmdline_facts['cmdline'][i.split('=')[0]] = i.split('=',1)[1]

# Generated at 2022-06-13 02:33:19.768654
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:33:22.627164
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 02:33:26.520655
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector
    cmdline_fact_collector = CmdLineFactCollector()
    result = {'cmdline': {'quiet': True},
              'proc_cmdline': {'quiet': True}}
    assert cmdline_fact_collector.collect() == result

# Generated at 2022-06-13 02:33:29.494465
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    testobj = CmdLineFactCollector()
    cmdline_facts = testobj.collect()
    assert cmdline_facts is not None
    assert cmdline_facts['cmdline'] is not None
    assert cmdline_facts['proc_cmdline'] is not None

# Generated at 2022-06-13 02:33:31.745079
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert CmdLineFactCollector.name == 'cmdline'

# Generated at 2022-06-13 02:33:35.045080
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    assert isinstance(fact_collector, CmdLineFactCollector)
    assert fact_collector._fact_ids is not None

test_CmdLineFactCollector()

# Generated at 2022-06-13 02:33:36.873638
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:33:49.064869
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmd_fact = CmdLineFactCollector()
    cmd_fact._get_proc_cmdline = lambda: 'a b=c d e=f g=h i=j k'
    facts = cmd_fact.collect()

    assert len(facts) == 2
    assert facts['cmdline'] == {'a': True, 'b': 'c', 'd': True, 'e': 'f', 'g': 'h', 'i': 'j', 'k': True}
    assert facts['proc_cmdline'] == {'a': True, 'b': 'c', 'd': True, 'e': 'f', 'g': 'h', 'i': ['j', 'k']}

# Generated at 2022-06-13 02:33:50.550262
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    t = CmdLineFactCollector()
    assert t.name == 'cmdline'
    assert t._fact_ids == set()


# Generated at 2022-06-13 02:33:54.159119
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_obj = CmdLineFactCollector()
    assert cmdline_obj.name == 'cmdline'
    assert not cmdline_obj._fact_ids


# Generated at 2022-06-13 02:34:01.720158
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_facts = CmdLineFactCollector()
    data = "ansible_facts=ansible_different_facts ansible_facts=ansible_facts ansible_facts=ansible_more_facts"
    collect_result = cmdline_facts._parse_proc_cmdline_facts(data)
    assert collect_result['ansible_facts'] == ['ansible_different_facts', 'ansible_facts', 'ansible_more_facts']
    assert isinstance(collect_result['ansible_facts'], list)
    assert collect_result['ansible_facts'] == ['ansible_different_facts', 'ansible_facts', 'ansible_more_facts']

# Generated at 2022-06-13 02:34:03.441413
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector(None, None)
    assert cmdline_facts.name == 'cmdline'
    assert cmdline_facts._fact_ids == set()


# Generated at 2022-06-13 02:34:04.084486
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:34:05.124802
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    print(c.name)


# Generated at 2022-06-13 02:34:09.643112
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    # Mimic the return value of read_file.
    cmdline_collector._get_proc_cmdline = lambda: "rd.lvm.vg=rhel rd.lvm.lv=root_lv ro rhgb rd.md.imsm=0 rd.md.dd=0"
    cmdline_facts = cmdline_collector.collect()
    assert 'cmdline' in cmdline_facts
    cmdline = cmdline_facts['cmdline']
    assert 'rd.lvm.vg' in cmdline
    assert cmdline['rd.lvm.vg'] == 'rhel'
    assert 'ro' in cmdline
    assert cmdline['ro'] == True


# Generated at 2022-06-13 02:34:13.466257
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fact_collector = CmdLineFactCollector()
    assert fact_collector.collect()['cmdline']['console'] == 'ttyS0'
    assert fact_collector.collect()['proc_cmdline']['console'] == 'ttyS0'

# Generated at 2022-06-13 02:34:15.614761
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    from ansible.module_utils.facts.collector import Collector
    my_object = CmdLineFactCollector()

    assert isinstance(my_object, Collector)

# Generated at 2022-06-13 02:34:36.058815
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdlinefc = CmdLineFactCollector()
    assert cmdlinefc.collect() == {}

# Generated at 2022-06-13 02:34:38.054539
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    testCollector = CmdLineFactCollector()
    testCollector.collect()

# Generated at 2022-06-13 02:34:39.056953
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    CmdLineFactCollector().collect()

# Generated at 2022-06-13 02:34:41.159025
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fact = CmdLineFactCollector()
    assert cmd_line_fact.name == 'cmdline'
    assert len(cmd_line_fact._fact_ids) == 0


# Generated at 2022-06-13 02:34:42.261675
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fact_collector = CmdLineFactCollector()
    assert cmd_line_fact_collector

# Generated at 2022-06-13 02:34:49.086911
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import inspect
    from ansible.module_utils.facts.collector import FactCollector

    def get_file_content(path):
        return "root=/dev/mapper/vg_main-lv_root rd_NO_LUKS  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_MD  " \
               "SYSFONT=latarcyrheb-sun16 rd_LVM_LV=vg_main/lv_swap LANG=en_US.UTF-8 rd_LVM_LV=vg_main/lv_root " \
               "rd_NO_DM rhgb quiet net.ifnames=0 biosdevname=0 selinux=0"

    FactCollector.get_file_content = get_file_content

    cmdline_collector = CmdLineFactCollector()
   

# Generated at 2022-06-13 02:34:58.816062
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_data = ' root=/dev/mapper/hdd1-root ro vga=0x317 rd.lvm.lv=hdd1/root rd.lvm.lv=hdd1/swap rhgb quiet systemd.journald.forward_to_console=0'


# Generated at 2022-06-13 02:35:01.099842
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    instance = CmdLineFactCollector()
    assert instance.name == 'cmdline'
    assert instance._fact_ids == set()


# Generated at 2022-06-13 02:35:09.414999
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import collections
    import sys
    import unittest

    class mock_module():
        def __init__(self):
            self.params = {}
    module = mock_module()

    class mock_collector1(CmdLineFactCollector):
        def _get_proc_cmdline(self):
            return 'a=1 b=2 c=3'

    class mock_collector2(CmdLineFactCollector):
        def _get_proc_cmdline(self):
            return None

    fact_collector = mock_collector1()
    result = fact_collector.collect(module=module)
    assert(isinstance(result, dict))
    assert(result['cmdline']['a'] == '1')
    assert(result['cmdline']['b'] == '2')

# Generated at 2022-06-13 02:35:10.117290
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    CmdLineFactCollector().collect()

# Generated at 2022-06-13 02:35:38.917880
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    expected = {'cmdline': {'BOOT_IMAGE': 'vmlinuz-4.8.0-52-generic',
                            'console': 'console=ttyS0',
                            'console=ttyS0': True,
                            'quiet': True,
                            'ro': True},
                'proc_cmdline': {'BOOT_IMAGE': ['vmlinuz-4.8.0-52-generic'],
                                 'console': ['ttyS0', 'ttyS0'],
                                 'quiet': [True],
                                 'ro': [True]}}

    assert c.collect() == expected

# Generated at 2022-06-13 02:35:39.713157
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert issubclass(CmdLineFactCollector, BaseFactCollector)

# Generated at 2022-06-13 02:35:40.231399
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:35:47.265706
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fake_proc_cmdline = """
    root=/dev/sda1 ro console=ttyS0,115200n8 console=tty0
    selinux=0
    """
    
    collector = CmdLineFactCollector('/proc/cmdline', 'proc_cmdline')
    cmdline_facts = collector.collect()
    
    assert cmdline_facts['cmdline'] == {
        'root': '/dev/sda1',
        'ro': True,
        'console': 'ttyS0,115200n8',
        'selinux': '0'
    }

# Generated at 2022-06-13 02:35:49.198521
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmd_line_fact_collector = CmdLineFactCollector()
    assert cmd_line_fact_collector != None, "Failed to instantiate CmdLineFactCollector"

# Generated at 2022-06-13 02:35:52.653412
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert cmdline_fact_collector._fact_ids == set()


# Generated at 2022-06-13 02:35:57.610595
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Setup
    cmdline_facts = {'cmdline': {'rhgb': True, 'quiet': True}, 'proc_cmdline': {'rhgb': True, 'quiet': True}}
    c = CmdLineFactCollector()
    c._get_proc_cmdline = lambda: 'rhgb quiet'
    # Exercise
    collected_facts = c.collect()
    # Verify
    assert cmdline_facts == collected_facts

# Generated at 2022-06-13 02:35:59.641064
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_facts = CmdLineFactCollector()
    assert cmdline_facts is not None
    assert cmdline_facts.name is not None
    assert cmdline_facts._fact_ids is not None


# Generated at 2022-06-13 02:36:01.007200
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_object = CmdLineFactCollector()
    assert cmdline_object.name == 'cmdline'


# Generated at 2022-06-13 02:36:06.329020
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = get_file_content('/proc/cmdline')
    cmdline_facts = {}
    cmdline_facts['cmdline'] = CmdLineFactCollector()._parse_proc_cmdline(data)
    cmdline_facts['proc_cmdline'] = CmdLineFactCollector()._parse_proc_cmdline_facts(data)
    assert CmdLineFactCollector().collect() == cmdline_facts

# Generated at 2022-06-13 02:36:33.020756
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()



# Generated at 2022-06-13 02:36:41.092140
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_collector = CmdLineFactCollector()
    assert cmdline_collector.name == 'cmdline'
    assert cmdline_collector._fact_ids == set()
    assert cmdline_collector._get_proc_cmdline() == b''
    cmdline_collector.collect() == {}
    assert cmdline_collector._parse_proc_cmdline('') == {}
    assert cmdline_collector._parse_proc_cmdline_facts('') == {}
    assert cmdline_collector._parse_proc_cmdline('arg1 arg2=val2') == {
        'arg1': True,
        'arg2': 'val2'
    }

# Generated at 2022-06-13 02:36:42.725467
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert set() == CmdLineFactCollector._fact_ids

# Generated at 2022-06-13 02:36:49.549090
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_data = '''
    BOOT_IMAGE=/boot/vmlinuz-3.10.0-957.el7.x86_64 root=/dev/mapper/cl-root ro crashkernel=auto rd.lvm.lv=cl/root rd.lvm.lv=cl/swap rhgb quiet LANG=en_US.UTF-8
    '''
    cmdline_collector = CmdLineFactCollector()
    cmdline_facts = cmdline_collector.collect(collected_facts={})


# Generated at 2022-06-13 02:36:50.973507
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()
    assert hasattr(x, 'name') and hasattr(x, 'collect')

# Generated at 2022-06-13 02:36:52.826609
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdlinefactcollector_instance = CmdLineFactCollector()
    assert cmdlinefactcollector_instance.name == 'cmdline'
    assert cmdlinefactcollector_instance._fact_ids == set()

# Generated at 2022-06-13 02:36:54.026601
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert isinstance(CmdLineFactCollector().collect(), dict)

# Generated at 2022-06-13 02:36:55.339428
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline.name == 'cmdline'
    assert cmdline._fact_ids == set()


# Generated at 2022-06-13 02:36:58.386520
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c.collect() == {'cmdline': {}, 'proc_cmdline': {}}

# Generated at 2022-06-13 02:37:07.882256
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()

    # cmdline_facts should be empty
    cmdline_facts = collector.collect()
    assert not cmdline_facts

    # cmdline_facts should have 2 keys: cmdline and proc_cmdline
    cmdline_facts = collector._collect()
    assert len(cmdline_facts) == 2
    assert 'cmdline' in cmdline_facts
    assert 'proc_cmdline' in cmdline_facts

    # cmdline_facts should have the same value
    assert cmdline_facts['cmdline'] == cmdline_facts['proc_cmdline']

    # cmdline_facts has kernel key:
    # { 'cmdline': {'kernel': True} }

# Generated at 2022-06-13 02:37:57.331785
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert 'cmdline' == obj.name
    assert isinstance(obj._fact_ids, set)
    assert not obj._fact_ids


# Generated at 2022-06-13 02:38:01.969222
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:38:10.899138
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():

    test_source = "arg_one=value_one arg_two arg_three=value_three"
    t_module = lambda x: None
    t_fact_data = {}
    t_collector = CmdLineFactCollector(t_module, t_fact_data)

    t_collector._get_proc_cmdline = lambda: test_source

    facts = t_collector.collect()
    expected = {
        "cmdline": {
            "arg_one": "value_one",
            "arg_two": True,
            "arg_three": "value_three"
        },
        "proc_cmdline": {
            "arg_one": "value_one",
            "arg_two": True,
            "arg_three": "value_three"
        }
    }

    assert facts == expected

# Generated at 2022-06-13 02:38:12.777335
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:38:17.219109
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    fact_collector = CmdLineFactCollector()
    fname = 'cmdline'
    assert fact_collector.name == fname, 'test_CmdLineFactCollector: FactCollector name is not %s' % fname
    assert fact_collector._fact_ids == set(), 'test_CmdLineFactCollector: FactCollector _fact_ids is not set()'


# Generated at 2022-06-13 02:38:18.098141
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector().name == 'cmdline'

# Generated at 2022-06-13 02:38:24.793085
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    module_mock = None
    collected_facts_mock = None


# Generated at 2022-06-13 02:38:29.962292
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    collected_facts = {}
    from ansible.module_utils.facts.collector import collector_module
    c.collect(module=collector_module, collected_facts=collected_facts)
    assert collected_facts['cmdline'] == {}
    assert collected_facts['proc_cmdline'] == {}

# Generated at 2022-06-13 02:38:39.944512
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:38:43.782432
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """Test Case to check if CmdLineFactCollector loads properly"""
    expected_results = {
        'name': 'cmdline',
    }
    collector = CmdLineFactCollector()

    assert collector._fact_ids == set()
    assert collector.name == expected_results['name']
