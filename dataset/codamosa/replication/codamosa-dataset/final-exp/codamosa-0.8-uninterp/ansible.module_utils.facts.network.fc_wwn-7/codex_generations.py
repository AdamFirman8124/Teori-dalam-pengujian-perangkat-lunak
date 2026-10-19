

# Generated at 2022-06-13 01:27:37.425609
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
        Unit test to check FcWwnInitiatorFactCollector works correctly

        :return: tuple with passed test results (total, passed)
    """
    module = type('Module', (object,), {})()
    module.run_command = lambda x, shell=True: ['', '', 0]
    fc = FcWwnInitiatorFactCollector()
    result = fc.collect(module)
    assert 'fibre_channel_wwn' in result
    assert isinstance(result['fibre_channel_wwn'], list)
    assert len(result['fibre_channel_wwn']) == 0

if __name__ == "__main__":
    tot = 0
    passed = 0

    tot, passed = test_FcWwnInitiatorFactCollector_collect()



# Generated at 2022-06-13 01:27:47.120930
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collectors.network import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.collectors.network import BaseFactCollector
    from mock import MagicMock
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils._text import to_bytes

    def get_file_lines_mock(filename, encoding='utf-8'):
        if filename == '/sys/class/fc_host/host3/port_name':
            return [to_bytes('0x21000014ff52a9bb', encoding=encoding), to_bytes('0x21000014ff52a9bc', encoding=encoding)]
        else:
            return None

    module = MagicMock()

# Generated at 2022-06-13 01:27:49.434101
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj1 = FcWwnInitiatorFactCollector()
    assert isinstance(obj1, FcWwnInitiatorFactCollector)


if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:27:50.794212
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:57.334471
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for constructor of class FcWwnInitiatorFactCollector
    """

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.network.fibre_channel_wwn import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.utils import AnsibleFactCollector

    fcwwncollector_obj = FcWwnInitiatorFactCollector()
    assert isinstance(fcwwncollector_obj, FcWwnInitiatorFactCollector) == True

# Generated at 2022-06-13 01:27:58.641110
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    facts = FcWwnInitiatorFactCollector()
    assert facts.name == 'fibre_channel_wwn'
    assert sorted(facts._fact_ids) == ['fibre_channel_wwn']

# Generated at 2022-06-13 01:28:04.113337
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors.system.fc_wwn_initiator import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector

    import sys
    import os
    

# Generated at 2022-06-13 01:28:15.193490
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # define module_mock
    class ModuleMock(object):
        def get_bin_path(self, bin_path, opt_dirs=[]):
            return bin_path
    # define module_opts_mock
    module_opts_mock = { 'gather_subset': ['all'] }
    # define ansible_facts_mock
    ansible_facts_mock = { 'ansible_facts': {} }
    # create instance of FcWwnInitiatorFactCollector
    FcWwnInitiatorFactCollector_ins = FcWwnInitiatorFactCollector()
    # call method collect of instance
    FcWwnInitiatorFactCollector_ins.collect(module=ModuleMock(), collected_facts=ansible_facts_mock)
    # check if fibre_

# Generated at 2022-06-13 01:28:16.927778
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcFactCollector = FcWwnInitiatorFactCollector()
    assert fcFactCollector.name == "fibre_channel_wwn"
    assert fcFactCollector._fact_ids == set()

# Generated at 2022-06-13 01:28:21.227870
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn = FcWwnInitiatorFactCollector()
    assert fcwwn.name == 'fibre_channel_wwn'
    assert fcwwn.priority == 20

# Generated at 2022-06-13 01:28:38.519085
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    # test if name and _fact_ids are defined
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids == set()


# Generated at 2022-06-13 01:28:51.515989
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class FakeFcWwnInitiatorFactCollector():
        def __init__(self):
            self._fact_ids = set()

        def collect(self):
            data = []
            data.append("0x21000014ff52a9bb")
            data.append("0x21000014ff52a9bc")
            return data

    class FakeLinux():
        def __init__(self):
            self.platform = 'linux'
            self.os = FakeLinuxOS()

    class FakeLinuxOS():
        def __init__(self):
            self.distribution = ['redhat', 'el', '7']

    fact_collector = FcWwnInitiatorFactCollector()
    fact_collector.collect
    fc_facts = fact_collector.collect()
    assert sys.platform.startsw

# Generated at 2022-06-13 01:28:59.969848
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class TestModule:
        def get_bin_path(self, bin, opt_dirs=None):
            return bin

    test_module = TestModule()

    class TestFcWwnInitiatorFactCollector(FcWwnInitiatorFactCollector):
        def __init__(self):
            self.facts = {}

        def run_command(self, cmd, *args, **kwargs):
            return 0, """\
HBA Port WWN: 10000090fa1658de
HBA Port WWN: 10000090fa1658df""", ""

    result = TestFcWwnInitiatorFactCollector().collect(test_module)

    assert result['fibre_channel_wwn'] == ['10000090fa1658de', '10000090fa1658df']

# Generated at 2022-06-13 01:29:02.343733
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    collector = FcWwnInitiatorFactCollector()
    assert collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:05.941754
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    # Create a new instance
    facts_module = FcWwnInitiatorFactCollector()

    # compare following attributes
    assert facts_module.name == 'fibre_channel_wwn'
    assert facts_module._fact_ids == set()

# Generated at 2022-06-13 01:29:08.426060
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:12.297001
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'
    assert len(f._fact_ids) == 0


# Generated at 2022-06-13 01:29:16.363849
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
  fc_obj = FcWwnInitiatorFactCollector()
  assert "fibre_channel_wwn" == fc_obj.name
  assert ["fibre_channel_wwn"] == fc_obj._fact_ids

# Generated at 2022-06-13 01:29:17.293110
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnInitiatorFactCollector().collect()

# Generated at 2022-06-13 01:29:21.574825
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModuleMock()
    facts = FcWwnInitiatorFactCollector().collect(module=module)
    assert 'fibre_channel_wwn' in facts
    assert isinstance(facts['fibre_channel_wwn'], list)



# Generated at 2022-06-13 01:29:46.457691
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:48.506439
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:56.727280
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    # check fact_collector class infrastructure
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()
    # check that the constructor generates no facts
    collected_facts = {}
    fact_collector.collect(collected_facts=collected_facts)
    assert 'fibre_channel_wwn' not in collected_facts


# Generated at 2022-06-13 01:30:01.087213
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_initiator_fact_collector = FcWwnInitiatorFactCollector()
    res = fc_initiator_fact_collector.collect()
    assert 'fibre_channel_wwn' in res
    assert type(res['fibre_channel_wwn']) is list

# Generated at 2022-06-13 01:30:04.708325
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModule(argument_spec={})
    fact_collector = FcWwnInitiatorFactCollector()
    facts = fact_collector.collect(module=module)
    assert facts['fibre_channel_wwn']



# Generated at 2022-06-13 01:30:05.878331
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:17.135553
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector
    class MockModule():
        def __init__(self):
            self.run_command_count = 0
            self.run_command_args = []
            self.run_command_return_values = []
            self.get_bin_path_count = 0
            self.get_bin_path_args = []
            self.get_bin_path_return_values = []

# Generated at 2022-06-13 01:30:26.145221
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import glob
    import os
    import shutil
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.network.fc_wwn_initiator import FcWwnInitiatorFactCollector
    from ansible.module_utils._text import to_bytes

# Generated at 2022-06-13 01:30:28.174417
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    f = FcWwnInitiatorFactCollector()
    assert f.name == 'fibre_channel_wwn'
    assert f._fact_ids == set()

# Generated at 2022-06-13 01:30:29.518910
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    assert collector.collect() is not None

# Generated at 2022-06-13 01:31:22.803825
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_subclass = FcWwnInitiatorFactCollector()
    assert fact_subclass.name == 'fibre_channel_wwn'
    assert sorted(fact_subclass._fact_ids) == ['fibre_channel_wwn']


# Generated at 2022-06-13 01:31:24.798602
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set()


# Generated at 2022-06-13 01:31:29.038400
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Test the constructor of class FcWwnInitiatorFactCollector
    """
    FcWwnInitiatorFactCollector()

# Unit test case for method collect

# Generated at 2022-06-13 01:31:34.534675
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc = FcWwnInitiatorFactCollector()
    from ansible.module_utils.facts.collector import AnsibleModule
    from ansible.module_utils.facts.collector import CollectedFacts
    module = AnsibleModule()
    collected = CollectedFacts()
    fc_facts = fc.collect(module, collected)
    assert 'fibre_channel_wwn' in fc_facts

# Generated at 2022-06-13 01:31:43.336829
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Takes pytest fixture as an argument
    """
    # create object to call collect method
    # argument to object is a module object which will fake an ansible module
    fact_collector = FcWwnInitiatorFactCollector(module=None)
    # call the collect method
    facts = fact_collector.collect()
    # assert if the values you expect are in facts dictionary
    assert 'fibre_channel_wwn' in facts
    assert facts['fibre_channel_wwn'] == ['500601605a4e7abf', '500601605a4e7aca']

# Generated at 2022-06-13 01:31:54.237378
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class mock_module():
        def get_bin_path(self, prog, opt_dirs=[]):
            if prog == 'ioscan':
                return '/sbin/ioscan'
            elif prog == 'fcmsutil':
                return '/opt/fcms/bin/fcmsutil'
            else:
                return None

        def run_command(self, cmd):
            rc = 0
            out = '\n'.join(['MACHINE_TYPE=ia64', '\n', '                N_Port Port World Wide Name = 0x50060b00006975ec', '\n'])
            return rc, out, ''

    module = mock_module()
    fc_wwn_initiator_fact_collector = FcWwnInitiatorFactCollector()
    fc_wwn_initiator

# Generated at 2022-06-13 01:31:56.444804
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class mock(object):
        def __init__(self, retval):
            self.retval = retval

        def run_command(self, args):
            return self.retval

    m = mock((0, '', ''))
    FcWwnInitiatorFactCollector().collect(m)
    return True

# Generated at 2022-06-13 01:31:59.098193
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_module = FcWwnInitiatorFactCollector()
    assert fact_module.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:01.671750
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts._fact_ids == set(['fibre_channel_wwn'])

# Generated at 2022-06-13 01:32:05.737024
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    from ansible.module_utils.facts.collector import BaseFactCollector

    # just in case, load module support for the required platform
    if platform.system() == 'Linux':
        from ansible.module_utils.facts.linux.fibre_channel_wwn import FcWwnInitiatorFactCollector
    elif platform.system() == 'SunOS':
        from ansible.module_utils.facts.sunos.fibre_channel_wwn import FcWwnInitiatorFactCollector
    elif platform.system() == 'AIX':
        from ansible.module_utils.facts.aix.fibre_channel_wwn import FcWwnInitiatorFactCollector

# Generated at 2022-06-13 01:33:49.492330
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """
    facts_collector = FcWwnInitiatorFactCollector()
    assert facts_collector.name == 'fibre_channel_wwn', \
        'test_FcWwnInitiatorFactCollector_collect: facts_collector.name="%s" expected: "fibre_channel_wwn"' % \
        facts_collector.name
    expected_fact_ids = set()
    assert facts_collector._fact_ids == expected_fact_ids, \
        'test_FcWwnInitiatorFactCollector_collect: facts_collector._fact_ids="%s" expected: "%s"' % \
        (facts_collector._fact_ids, expected_fact_ids)

   

# Generated at 2022-06-13 01:33:51.388946
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert isinstance(FcWwnInitiatorFactCollector(), FcWwnInitiatorFactCollector)


# Generated at 2022-06-13 01:33:53.789671
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'
    assert c._fact_ids == set()


# Generated at 2022-06-13 01:33:57.980799
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    '''
    Test method FcWwnInitiatorFactCollector.collect.
    '''
    # Create an instance of FcWwnInitiatorFactCollector with mocks.
    collector = FcWwnInitiatorFactCollector({})

    # run method Collect, store the result
    result = collector.collect()

    # check the result
    assert isinstance(result, dict)
    assert 'fibre_channel_wwn' in result
    assert isinstance(result['fibre_channel_wwn'], list)
    assert len(result['fibre_channel_wwn']) > 0
    assert isinstance(result['fibre_channel_wwn'][0], str)

# Generated at 2022-06-13 01:34:05.436682
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args

    def run_exit_json(self, *args, **kwargs):
        self.exit_args = args
        self.exit_kwargs = kwargs
        raise AnsibleExitJson(kwargs['changed'], kwargs['msg'], kwargs['ansible_facts'])

    def run_fail_json(self, *args, **kwargs):
        self.fail_args = args
        self.fail_kwargs = kwargs
        add_msg = kwargs.get('msg')
        if add_msg:
            self.fail_json_msg += add_msg

# Generated at 2022-06-13 01:34:12.393703
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Test constructor with None parameter.
    assert FcWwnInitiatorFactCollector(None) is not None

    # Test constructor with non existing file parameter.
    fc = FcWwnInitiatorFactCollector("/etc/not_existing_file")
    assert fc is not None

    # Test constructor with one existing file parameter.
    fc = FcWwnInitiatorFactCollector("/etc/hosts")
    assert fc is not None


# Generated at 2022-06-13 01:34:15.312266
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    dimm_fact_collector_obj = FcWwnInitiatorFactCollector()
    assert dimm_fact_collector_obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:18.447820
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert type(x.name) == str
    assert type(x._fact_ids) == set
    assert type(x.collect()) == dict

# Generated at 2022-06-13 01:34:26.697339
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    #
    # mock get_file_content
    #
    get_file_content_orig = get_file_content
    fcontent_out = '0x21000014ff52a9bb'
    fcontent_out2 = """HBA Port WWN: 10000090fa1658de
HBA Port WWN: 10000090fa1658df
"""
    get_file_content_ret = []
    get_file_content_ret.append(fcontent_out)
    get_file_content_ret.append(fcontent_out2)

# Generated at 2022-06-13 01:34:28.396232
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()