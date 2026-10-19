

# Generated at 2022-06-13 01:27:31.690488
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    # test the fact_collector name and fact_ids
    assert fact_collector.name == 'fibre_channel_wwn'
    assert fact_collector._fact_ids == set(['fibre_channel_wwn'])

# Generated at 2022-06-13 01:27:33.392267
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:27:37.568320
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'
    assert fc_collector._fact_ids == set()


# Generated at 2022-06-13 01:27:47.256838
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test of the method FcWwnInitiatorFactCollector.collect
    """
    from ansible.module_utils.facts.collector import Collector

    # Create instance of FcWwnInitiatorFactCollector
    fc_fact_collector = FcWwnInitiatorFactCollector()
    # Create an instance of Collector
    # Note: The Collector class is only used with Ansible 2.6.x or higher
    fact_collector = Collector(None, None)
    # Get a dictionary with fibre_channel_wwn fact (dictionary is empty)
    facts = fc_fact_collector.collect(collected_facts=fact_collector)
    assert 'fibre_channel_wwn' in facts, "Expected 'fibre_channel_wwn' in facts"

# Generated at 2022-06-13 01:27:51.172433
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn = FcWwnInitiatorFactCollector()
    assert fcwwn.name == 'fibre_channel_wwn'
    assert fcwwn._fact_ids == set()


# Generated at 2022-06-13 01:27:52.892967
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts is not None

# Generated at 2022-06-13 01:28:00.103208
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys
    sys.modules['ansible'] = type('AnsibleModule', (), {'get_bin_path': lambda self, x, opt_dirs=[]: '/bin/'+x})()
    import ansible.module_utils.facts.collector.fibre_channel_wwn_initiator
    from ansible.module_utils.facts.collector.fibre_channel_wwn_initiator import FcWwnInitiatorFactCollector
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils.facts.collector import BaseFactCollector
    sys.modules['ansible.module_utils.facts.collector.base'] = type('AnsibleModule', (), {'BaseFactCollector': BaseFactCollector})()
    

# Generated at 2022-06-13 01:28:04.883933
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.network.fibre_channel_wwn import FcWwnInitiatorFactCollector
    fc = FcWwnInitiatorFactCollector()
    assert isinstance(fc, Collector)


# Generated at 2022-06-13 01:28:07.156155
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    p = FcWwnInitiatorFactCollector()
    assert p.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:28:10.503623
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector.collect()
    assert 'fibre_channel_wwn' in fc
    # Example output: ['0x21000014ff52a9bb']

# Generated at 2022-06-13 01:28:36.123146
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    module_args = {}
    res = FcWwnInitiatorFactCollector.getset_module_parameter(module_args)
    assert res == (module_args, 'fibre_channel_wwn')

# Generated at 2022-06-13 01:28:38.236600
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn = FcWwnInitiatorFactCollector()
    assert fc_wwn.name == 'fibre_channel_wwn'
    assert fc_wwn._fact_ids == set()

# Generated at 2022-06-13 01:28:41.538483
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    assert FcWwnInitiatorFactCollector.collect(None, None) == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:28:43.905550
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # Verify that all instance attributes were properly initialized.
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:52.837995
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collectors import FcWwnInitiatorFactCollector
    fact_collector = FactCollector()
    fact_collector.collectors['fibre_channel_wwn'] = FcWwnInitiatorFactCollector()
    facts = fact_collector.collect(module=None)
    assert type(facts) == dict, 'Expected dict, received %s' % type(facts)
    #if we are at this point then test is successful
    return True

# Generated at 2022-06-13 01:29:00.845824
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import os
    import json
    import tempfile
    from ansible.module_utils.facts import collector
    f = tempfile.NamedTemporaryFile(delete=False)
    fact_name = 'fibre_channel_wwn'
    fact_collector_name = '%s_%s' % (collector.collector_name, fact_name)
    fc_fact_collector = collector.get_collector(fact_collector_name)
    # Test for Linux
    if sys.platform.startswith('linux'):
        f.write(b'0x21000014ff52a9bb')
    # Test for Solaris
    elif sys.platform.startswith('sunos'):
        f.write(b'HBA Port WWN: 10000090fa1658de')
    #

# Generated at 2022-06-13 01:29:04.430849
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_fac = FcWwnInitiatorFactCollector()
    facts = fc_fac.collect()
    assert type(facts) is dict
    assert 'fibre_channel_wwn' in facts
    assert type(facts['fibre_channel_wwn']) is list

# Generated at 2022-06-13 01:29:07.719103
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    facts = FcWwnInitiatorFactCollector()
    assert facts.name == 'fibre_channel_wwn'
    assert facts._fact_ids == set()

# Generated at 2022-06-13 01:29:17.082949
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.network.fc_wwn import FcWwnInitiatorFactCollector

    class FakeModule(object):
        def __init__(self):
            pass

        def get_bin_path(self, arg1='', opt_dirs=''):
            return 'fake_path'

        def run_command(self, arg1='', check_rc=False):
            if arg1 == 'fake_path hba-port':
                return (0, 'HBA Port WWN: 10000090fa1658de', None)

# Generated at 2022-06-13 01:29:27.714390
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    from ansible.module_utils.facts import FactsCollector
    from ansible.module_utils.facts.collectors.fc_wwn_init import (
        FcWwnInitiatorFactCollector)
    from ansible.module_utils.facts.utils import get_file_content

    with open("/tmp/fibre_channel_wwn_0", "w+") as file:
        file.write("0x21000014ff57a9bb")
        file.write("0x22000014ff57a9bb")

    with open("/tmp/fibre_channel_wwn_1", "w+") as file:
        file.write("0x23000014ff57a9bb")
        file.write("0x24000014ff57a9bb")

    # test for linux

# Generated at 2022-06-13 01:29:59.093733
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """ validate if the function returns correct wwns from test file """

    # setup facts to be collected
    fact_collector = FcWwnInitiatorFactCollector()
    collected_facts = {}
    collected_facts['fibre_channel_wwn'] = []

    # execute the method and check if the result contains the expected wwn
    fact_collector.collect(collected_facts=collected_facts)
    assert len(collected_facts['fibre_channel_wwn']) == 1
    assert '21000014ff52a9bb' == collected_facts['fibre_channel_wwn'][0]


# Generated at 2022-06-13 01:30:08.116229
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import os

    collector = FcWwnInitiatorFactCollector()
    module = os.path.realpath(__file__)
    module = os.path.split(module)[0]
    module = os.path.split(module)[0]
    module = os.path.join(module, "..", "..", "lib", "ansible", "module_utils")
    module = os.path.abspath(module)
    sys.path.insert(0, module)
    from ansible.module_utils.common.collections import ImmutableDict
    sys.path.pop(0)
    module = ImmutableDict()
    printed_facts = collector.collect(module)
    assert isinstance(printed_facts, dict)
    assert printed_facts['fibre_channel_wwn'] != []

# Generated at 2022-06-13 01:30:18.468186
# Unit test for method collect of class FcWwnInitiatorFactCollector

# Generated at 2022-06-13 01:30:20.829347
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:30:23.124646
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert fc_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:23.616519
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    assert False

# Generated at 2022-06-13 01:30:25.846207
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc.collect() == {}

# Generated at 2022-06-13 01:30:28.200834
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == 'fibre_channel_wwn'
    assert not fc_facts._fact_ids

# Generated at 2022-06-13 01:30:31.219906
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():

    facts_collector = FcWwnInitiatorFactCollector()
    assert facts_collector.name == 'fibre_channel_wwn'
    assert 'fibre_channel_wwn' in facts_collector._fact_ids

# Generated at 2022-06-13 01:30:33.668789
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWWN = FcWwnInitiatorFactCollector()
    Facts = FcWWN.collect()
    assert Facts['fibre_channel_wwn']

# Generated at 2022-06-13 01:31:24.576435
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Test module FcWwnInitiatorFactCollector
    """
    module = AnsibleModule(argument_spec={})
    fc_facts = FcWwnInitiatorFactCollector.collect(module)
    assert fc_facts
    assert 'fibre_channel_wwn' in fc_facts
    #assert fc_facts['fibre_channel_wwn'][0] == ''

# Generated at 2022-06-13 01:31:28.993491
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc = FcWwnInitiatorFactCollector()
    fc_facts = fc.collect()
    assert fc_facts['fibre_channel_wwn']

# Generated at 2022-06-13 01:31:31.126020
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts_collector = FcWwnInitiatorFactCollector()
    assert facts_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:42.471091
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    class MockModule(object):
        def __init__(self, name, bin_dirs):
            self._name = name
            self._bin_dirs = bin_dirs
        def get_bin_path(self, name, opt_dirs=[]):
            return self._bin_dirs[name]
        def run_command(self, cmd):
            if self._name == 'cmd':
                self._content = 'lscfg_content'
                return (0, 'lscfg_out', '')
            if self._name == 'ioscan':
                self._content = 'ioscan_content'
                return (0, 'ioscan_out', '')
            else:
                self._content = 'fcmsutil_content'
                return (0, 'fcmsutil_out', '')


# Generated at 2022-06-13 01:31:46.332266
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    ffc = FcWwnInitiatorFactCollector()
    assert ffc.name == 'fibre_channel_wwn'
    assert ffc._fact_ids == set()

# Generated at 2022-06-13 01:31:48.591937
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:50.957903
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts_collector = FcWwnInitiatorFactCollector()
    assert fc_facts_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:53.785512
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collected_facts = {}
    FcWwnInitiatorFactCollector().collect(collected_facts=collected_facts)
    assert 'fibre_channel_wwn' in collected_facts


# Generated at 2022-06-13 01:31:56.335679
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector = FcWwnInitiatorFactCollector()
    assert "fibre_channel_wwn" == fc_collector.name

# Generated at 2022-06-13 01:32:08.084512
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # pylint: disable=import-error
    from ansible.module_utils.facts import ansible_collections
    # pylint: enable=import-error
    # mock the module that it is called from
    module_mock = ansible_collections.ansible.misc.plugins.module_utils.facts.module_utils.Module()
    # define return values for module mock
    module_mock.run_command.return_value = (0, '', '')
    module_mock.get_bin_path.side_effect = lambda x: x
    # create FcWwnInitiatorFactCollector instance
    fcFactCollector = FcWwnInitiatorFactCollector()
    # run collect method
    facts = fcFactCollector.collect(module_mock)
    # make sure that the

# Generated at 2022-06-13 01:33:38.613813
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc == FcWwnInitiatorFactCollector
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 01:33:41.933798
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:33:43.732007
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test_obj = FcWwnInitiatorFactCollector()
    assert test_obj

# Generated at 2022-06-13 01:33:48.105699
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import FactCollector
    fcwwn_fc = FcWwnInitiatorFactCollector()
    fc_facts = fcwwn_fc.collect()
    assert fc_facts['fibre_channel_wwn'] == ['2a0000144ffbe6e1','2a0000144ffbe6e2']

# Generated at 2022-06-13 01:33:56.100197
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    '''
    Run test_FcWwnInitiatorFactCollector_collect against
    dummy data.
    '''

    # setup
    sys.modules['ansible'] = type("FakeAnsibleModule", (object,),
                                  {'run_command': run_command})
    sys.modules['ansible.module_utils.facts.collector'] = type("FakeFactCollector", (object,),
                                  {'FcWwnInitiatorFactCollector': FcWwnInitiatorFactCollector})
    sys.modules['ansible.module_utils.facts.utils'] = type("FakeUtils", (object,),
                                  {'get_file_lines': get_file_lines})
    from ansible.module_utils.facts.collector.network.fibre_channel_wwn import Fc

# Generated at 2022-06-13 01:34:00.471388
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_c = FcWwnInitiatorFactCollector()
    assert fact_c.name == "fibre_channel_wwn"
    assert fact_c.platform == "all"
    assert fact_c._fact_ids == set()

# Generated at 2022-06-13 01:34:06.565233
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector

    collector = FcWwnInitiatorFactCollector()

    # test the behaviour on an unsupported system
    facts = collector.collect()

    assert type(facts).__name__ == 'dict'
    assert 'fibre_channel_wwn' in facts
    assert len(facts['fibre_channel_wwn']) == 0

# Generated at 2022-06-13 01:34:13.489020
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """ Unit test for method collect
        of class FcWwnInitiatorFactCollector"""

    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import Collector

    facts = Collector.fetch_facts(get_collector_instance(FcWwnInitiatorFactCollector))
    assert 'fibre_channel_wwn' in facts

# Generated at 2022-06-13 01:34:15.223771
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector
    assert isinstance(obj, object)

# Generated at 2022-06-13 01:34:19.531067
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    module = AnsibleModule()
    fact_collector = FcWwnInitiatorFactCollector()
    result = fact_collector.collect(module=module)
    print(result)
    assert result['fibre_channel_wwn']

# Unit test to check if method exists