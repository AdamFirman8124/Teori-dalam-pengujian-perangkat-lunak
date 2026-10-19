

# Generated at 2022-06-13 02:30:21.741393
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    tester = CmdLineFactCollector()
    assert tester
    assert tester.name == 'cmdline'
    assert tester.collect()

# Generated at 2022-06-13 02:30:25.908794
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from importlib import import_module

    from ansible.module_utils.facts import FactCollector

    module = import_module('ansible.module_utils.facts.collectors.cmdline')
    collector = FactCollector('cmdline', module)

    assert collector.collect()


# Generated at 2022-06-13 02:30:34.681422
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:30:40.926495
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()

    assert cmdline_facts['cmdline']['ansible_managed'] == "### Ansible managed ###"
    assert cmdline_facts['cmdline']['rd.systemd.show_status'] == "true"
    assert cmdline_facts['cmdline']['rhgb'] == "quiet"

    assert cmdline_facts['proc_cmdline']['ansible_managed'] == "### Ansible managed ###"
    assert cmdline_facts['proc_cmdline']['rd.systemd.show_status'] == "true"
    assert cmdline_facts['proc_cmdline']['rhgb'] == "quiet"



# Generated at 2022-06-13 02:30:45.142899
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline_fact_collector = CmdLineFactCollector()
    assert cmdline_fact_collector.name == 'cmdline'
    assert len(cmdline_fact_collector._fact_ids) == 0


# Generated at 2022-06-13 02:30:46.891394
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()
    assert cmdline is not None


# Generated at 2022-06-13 02:30:49.144599
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()
    assert x.name == 'cmdline'
    assert x._fact_ids == set()

# Generated at 2022-06-13 02:30:52.746183
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """
    Test for constructor of class CmdLineFactCollector
    """
    assert CmdLineFactCollector.name == 'cmdline'
    assert CmdLineFactCollector._fact_ids == set()

# Generated at 2022-06-13 02:31:02.101539
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class mock_get_file_content(object):
        """ Mock get_file_content method of utils.py module """
        return_value = 'BOOT_IMAGE=/vmlinuz-3.10.0-327.el7.x86_64 root=/dev/mapper/rhel-root ro crashkernel=auto rhgb quiet LANG=en_US.UTF-8'

    # override module function to mock get_file_content
    CmdLineFactCollector._get_proc_cmdline = mock_get_file_content

    collector = CmdLineFactCollector()
    cmdline_facts = collector.collect()

    assert cmdline_facts['cmdline']['BOOT_IMAGE'] == '/vmlinuz-3.10.0-327.el7.x86_64'

# Generated at 2022-06-13 02:31:03.285149
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    x = CmdLineFactCollector()


# Generated at 2022-06-13 02:31:21.517287
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # https://stackoverflow.com/questions/14824163/how-to-simulate-sys-argv-in-python
    import sys

# Generated at 2022-06-13 02:31:23.281468
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c1 = CmdLineFactCollector()
    assert c1.name == 'cmdline'

# Generated at 2022-06-13 02:31:26.218207
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    try:
        obj = CmdLineFactCollector()
        print("%s successfully created" % obj.name)
    except Exception as e:
        print("Error occurred: %s" % str(e))


# Generated at 2022-06-13 02:31:27.017055
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:31:31.791367
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    CmdLineFactCollector._get_proc_cmdline = lambda x: 'ro root=UUID=aaaa-aaaa-aaaa-aaaa-aaaaaaaaa'
    test_dict = {'cmdline': {'ro': True, 'root': 'UUID=aaaa-aaaa-aaaa-aaaa-aaaaaaaaa'}, 'proc_cmdline': {'ro': True, 'root': 'UUID=aaaa-aaaa-aaaa-aaaa-aaaaaaaaa'}}
    assert test_dict == c.collect()


# Generated at 2022-06-13 02:31:32.258178
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass

# Generated at 2022-06-13 02:31:41.693930
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    data = "BOOT_IMAGE=/boot/vmlinuz-3.10.0-327.el7.x86_64 root=/dev/mapper/rhel-root ro crashkernel=auto rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet LANG=en_US.UTF-8"
    o = CmdLineFactCollector()
    o._get_proc_cmdline = lambda: data

# Generated at 2022-06-13 02:31:42.414394
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    CmdLineFactCollector()

# Generated at 2022-06-13 02:31:45.259460
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    # Check that the constructor creates an object with the correct attributes
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'
    assert c._fact_ids == set()


# Generated at 2022-06-13 02:31:46.577549
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
	cmdline_fact_collector = CmdLineFactCollector()

# Generated at 2022-06-13 02:31:58.554107
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    module = AnsibleModule(argument_spec={})
    collected_facts = AnsibleFactsCollector(module)
    cmdline = CmdLineFactCollector(module, collected_facts)
    assert cmdline.name == "cmdline"
    assert cmdline._fact_ids == set()


# Generated at 2022-06-13 02:31:59.909860
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()

    assert collector.collect() == {'cmdline': {}, 'proc_cmdline': {}}

# Generated at 2022-06-13 02:32:01.570696
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
  c = CmdLineFactCollector()
  assert c.name == "cmdline"

# Generated at 2022-06-13 02:32:07.202715
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    cmdline_facts = collector._get_proc_cmdline()
    #print(cmdline_facts)
    #assert cmdline_facts == 'my_test_string'
    assert cmdline_facts == 'BOOT_IMAGE=/vmlinuz-4.15.0-33-generic root=UUID=5d5a5a1b-2949-4c69-b3c9-b5a570155a47 ro quiet splash vt.handoff=1'
    cmdline_facts = collector._parse_proc_cmdline(cmdline_facts)
    #print(cmdline_facts)

# Generated at 2022-06-13 02:32:17.812336
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # sample file content for /proc/cmdline
    data = 'BOOT_IMAGE=/boot/vmlinuz-4.4.0-21-generic root=UUID=71a6b820-6d15-4b86-8e19-6c3a6a8b1e4d ro console=ttyS0,19200n8'

    # create a CmdLineFactCollector instance
    cmdlineFactCollector = CmdLineFactCollector()

    cmdline_facts = cmdlineFactCollector.collect(collected_facts=None)

    # expected results

# Generated at 2022-06-13 02:32:21.547672
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Test case for the function collect of class CmdLineFactCollector"""
    # Create a fake CmdLineFactCollector object
    cmdline_fact_collector = CmdLineFactCollector()

    # Check the collect
    assert cmdline_fact_collector.collect() == {'cmdline': {}, 'proc_cmdline': {}}

# Generated at 2022-06-13 02:32:32.320054
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    test_content = """root=/dev/sda3 user=root console=ttyS0,9600n8 console=tty0 init=/sbin/init selinux=0"""
    mock_get_file_content = lambda *args, **kwargs: test_content

    collector = CmdLineFactCollector()
    collector.get_file_content = mock_get_file_content

    facts = collector.collect(collected_facts=None)

# Generated at 2022-06-13 02:32:41.120044
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    def mock_get_file_content(path):
        return data

    data = 'ip=127.0.0.1 ::1 iburst foo=bar'
    test_cmdline_facts = {
        'cmdline': {'foo': 'bar', 'ip': '127.0.0.1 ::1 iburst'},
        'proc_cmdline': {'foo': 'bar', 'ip': ['127.0.0.1', '::1 iburst']}
    }
    test_collect_facts = {
        'ansible_cmdline': {'foo': 'bar', 'ip': '127.0.0.1 ::1 iburst'},
        'ansible_proc_cmdline': {'foo': 'bar', 'ip': ['127.0.0.1', '::1 iburst']}
    }

   

# Generated at 2022-06-13 02:32:43.009997
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cf = CmdLineFactCollector()
    assert cf.name == 'cmdline'
    assert isinstance(cf._fact_ids, set)

# Generated at 2022-06-13 02:32:45.070142
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    cmdline = CmdLineFactCollector()

    # Check that the constructor for class CommandLineFactCollector creates a
    # CommandLineFactCollector object named cmdline.
    assert type(cmdline) == CmdLineFactCollector
    assert cmdline.name == 'cmdline'

# Generated at 2022-06-13 02:33:07.142270
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids == set()

    assert isinstance(obj._get_proc_cmdline, object)
    assert isinstance(obj._parse_proc_cmdline, object)
    assert isinstance(obj._parse_proc_cmdline_facts, object)
    assert isinstance(obj.collect, object)

# Generated at 2022-06-13 02:33:14.279975
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()

# Generated at 2022-06-13 02:33:15.015435
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector

# Generated at 2022-06-13 02:33:15.762680
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    assert CmdLineFactCollector() is not None

# Generated at 2022-06-13 02:33:16.990862
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c
    assert c.name == 'cmdline'
    assert c._fact_ids == set()

# Generated at 2022-06-13 02:33:18.579489
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    c = CmdLineFactCollector()
    f = c.collect()
    print(f)

# Generated at 2022-06-13 02:33:21.561161
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    """Unit test for method collect of class CmdLineFactCollector."""
    collector = CmdLineFactCollector()
    facts = collector.collect()
    assert 'cmdline' in facts and 'proc_cmdline' in facts

# Generated at 2022-06-13 02:33:26.822041
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    proc_cmdline = "BOOT_IMAGE=/vmlinuz-2.6.32-431.el6.x86_64 root=/dev/mapper/rhel_rhel-root ro crashkernel=auto rhgb quiet LANG=en_US.UTF-8"

    fact_collector = CmdLineFactCollector()
    fact_collector.file_exists = lambda file_name: True
    fact_collector.get_file_content = lambda file_name: proc_cmdline

    cmdline_facts = fact_collector.collect()

    assert isinstance(cmdline_facts, dict)
    assert 'proc_cmdline' in cmdline_facts
    assert isinstance(cmdline_facts['proc_cmdline'], dict)
    assert 'cmdline' in cmdline_facts

# Generated at 2022-06-13 02:33:35.672582
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()

    data = "root=LABEL=work rhgb quiet"
    cmdline_facts = {"cmdline": {'root': 'LABEL=work',
                                 'rhgb': True,
                                 'quiet': True},
                     "proc_cmdline": {'root': 'LABEL=work',
                                      'rhgb': True,
                                      'quiet': True}}

    assert cmdline_collector._parse_proc_cmdline_facts(data) == cmdline_facts["proc_cmdline"]
    assert cmdline_collector._parse_proc_cmdline(data) == cmdline_facts["cmdline"]
    assert cmdline_collector.collect() == cmdline_facts

# Generated at 2022-06-13 02:33:43.136197
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    fake_data = "foo=bar baz quux=yes"
    cmdline_facts = CmdLineFactCollector().collect(collected_facts={})
    assert isinstance(cmdline_facts, dict), 'CmdLineFactCollector.collect did not return a dictionary'
    assert 'proc_cmdline' in cmdline_facts, 'proc_cmdline not in CmdLineFactCollector return value'
    assert 'cmdline' in cmdline_facts, 'cmdline not in CmdLineFactCollector return value'
    assert isinstance(cmdline_facts['proc_cmdline'], dict), 'proc_cmdline is not a dictionary'
    assert isinstance(cmdline_facts['cmdline'], dict), 'cmdline is not a dictionary'

    # test 1 param

# Generated at 2022-06-13 02:34:29.770149
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    class module:
        def exit_json(self, **kwargs):
            return
        def fail_json(self, *args, **kwargs):
            return

    cmdline_facts_collector = CmdLineFactCollector()
    cmdline_facts_collector._get_proc_cmdline = lambda: "a=b c=d e f=g=h"
    collected_facts = {}
    module_mock = module()
    cmdline_facts = cmdline_facts_collector.collect(module=module_mock, collected_facts=collected_facts)
    assert cmdline_facts['cmdline']['a'] == 'b'
    assert cmdline_facts['cmdline']['c'] == 'd'
    assert cmdline_facts['cmdline']['e'] == True
    assert cmdline_

# Generated at 2022-06-13 02:34:39.407131
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    # Get instance of CmdLineFactCollector without 'self'
    CmdLineFactCollector_instance = CmdLineFactCollector()
    # Get collect method from CmdLineFactCollector instance
    collect_method = CmdLineFactCollector_instance.collect

    # Unit test for collect method with absolute_import, division, print_function

# Generated at 2022-06-13 02:34:42.389208
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import collect_facts

    c = CmdLineFactCollector()
    c.collect()

    assert Collector.has_fact('cmdline')
    assert Collector.has_fact('proc_cmdline')

    collect_facts.clear_facts()

# Generated at 2022-06-13 02:34:46.189661
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_fact_collector = CmdLineFactCollector()
    with open('/proc/cmdline') as file_handle:
        data = file_handle.read()
    cmdline_fact_collector._get_proc_cmdline = lambda: data
    cmdline_facts = cmdline_fact_collector.collect()
    assert cmdline_facts.keys() == {'cmdline', 'proc_cmdline'}

# Generated at 2022-06-13 02:34:47.085567
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    collector = CmdLineFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict)

# Generated at 2022-06-13 02:34:55.088029
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import os
    import tempfile

    # Create temp file to emulate /proc/cmdline
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as cmdline:
        cmdline.write('BOOT_IMAGE=/vmlinuz-3.10.0-327.el7.x86_64 root=/dev/mapper/rhel-root ro crashkernel=auto rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet rootfstype=xfs rd.lvm.lv=cl/root rd.lvm.lv=cl/home rd.lvm.lv=cl/swap')
        cmdline.close()

    # Collect facts
    cmdline_fc = CmdLineFactCollector()
    collected

# Generated at 2022-06-13 02:35:04.451263
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    from ansible.module_utils.facts import constant

    collector = CmdLineFactCollector()
    with open('/proc/cmdline', 'r') as file_fd:
        cmdline = collector._parse_proc_cmdline(file_fd.read())
        assert isinstance(cmdline, dict)

    output = collector.collect()
    assert isinstance(output, dict)

    assert 'proc_cmdline' in output
    assert output['proc_cmdline'] == constant.SETTINGS.cmdline_facts
    assert 'cmdline' in output
    assert output['cmdline'] == cmdline

# Generated at 2022-06-13 02:35:05.293298
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    pass
    # No unit test for this method

# Generated at 2022-06-13 02:35:06.826118
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    """Unit test for constructor of class CmdLineFactCollector"""
    CmdLineFactCollector(None)



# Generated at 2022-06-13 02:35:07.849236
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    c = CmdLineFactCollector()
    assert c.name == 'cmdline'

# Generated at 2022-06-13 02:36:44.707880
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    myCmdLineFactCollector = CmdLineFactCollector()
    assert myCmdLineFactCollector.name == 'cmdline'
    assert myCmdLineFactCollector._fact_ids == set()
    assert myCmdLineFactCollector._get_proc_cmdline() == b'BOOT_IMAGE=(hd0,gpt4)/vmlinuz-4.2.0-23-generic root=UUID=d6f2ce50-a0a7-4c46-8ea7-76c14e74a766 ro console=tty1 console=ttyS0'

# Generated at 2022-06-13 02:36:51.873239
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import sys
    sys.modules['ansible'] = type('ansible', (), {'__version__': '2.8.5'})
    sys.modules['ansible.module_utils'] = type('ansible.module_utils', (), {'facts': type('facts', (), {'utils': type('utils', (), {'get_file_content': get_file_content})})})
    from AnsibleModule import AnsibleModule
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.cmdline import CmdLineFactCollector
    cmdline_fact_collector = CmdLineFactCollector()
    assert(cmdline_fact_collector.name == 'cmdline')
    ansible_module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 02:36:53.145904
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    obj = CmdLineFactCollector()
    assert obj.name == 'cmdline'
    assert obj._fact_ids  == set()


# Generated at 2022-06-13 02:36:58.617540
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    import json

    with open ('test/unittests/fixtures/facts/CmdLineFactCollector/collect.json') as json_file:
        expected_results = json.load(json_file)

    cmdline_collector = CmdLineFactCollector()
    collected_facts = cmdline_collector.collect()

    assert expected_results == collected_facts


# Generated at 2022-06-13 02:37:00.394393
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    o = CmdLineFactCollector()
    assert o._fact_ids == set()
    assert o.name == 'cmdline'

# Generated at 2022-06-13 02:37:04.892277
# Unit test for method collect of class CmdLineFactCollector
def test_CmdLineFactCollector_collect():
    cmdline_collector = CmdLineFactCollector()
    cmdline_facts = {}

    data = cmdline_collector._get_proc_cmdline()

    cmdline_facts['cmdline'] = cmdline_collector._parse_proc_cmdline(data)
    cmdline_facts['proc_cmdline'] = cmdline_collector._parse_proc_cmdline_facts(data)

    return cmdline_facts

# Generated at 2022-06-13 02:37:07.913406
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    collector = CmdLineFactCollector()
    assert collector._fact_ids == 'cmdline'
    assert collector.name == 'cmdline'

# Generated at 2022-06-13 02:37:10.147702
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    o = CmdLineFactCollector()
    assert o.name == 'cmdline'
    assert o._fact_ids == set()



# Generated at 2022-06-13 02:37:19.052168
# Unit test for method collect of class CmdLineFactCollector

# Generated at 2022-06-13 02:37:23.154221
# Unit test for constructor of class CmdLineFactCollector
def test_CmdLineFactCollector():
    TestCmdLineFactCollector = CmdLineFactCollector()
    assert TestCmdLineFactCollector.name == 'cmdline'
    assert TestCmdLineFactCollector._fact_ids == set()
