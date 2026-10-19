

# Generated at 2022-06-13 01:27:41.331565
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import mock, sys
    module = mock.Mock()
    module.run_command.return_value = 0, 'fcinfo output', None
    module.get_bin_path.return_value = 'fcinfo'
    sys.platform = 'sunos'

    fc = FcWwnInitiatorFactCollector(module)
    fc_facts = fc.collect(module)
    assert isinstance(fc_facts, dict)
    assert isinstance(fc_facts['fibre_channel_wwn'], list)
    assert 'Port WWN' in fc_facts['fibre_channel_wwn'][0]

# Generated at 2022-06-13 01:27:52.224396
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test function of class FcWwnInitiatorFactCollector using __main__
    """
    print('Starting unit test of FcWwnInitiatorFactCollector class')
    fc_facts = FcWwnInitiatorFactCollector().collect()
    if not fc_facts:
        print('Failed to collect facts from FcWwnInitiatorFactCollector')
        print('Ending unit test of FcWwnInitiatorFactCollector class')
        exit(1)
    print('Fibre Channel WWN initiator facts collected : \n{}'.format(fc_facts))
    print('Ending unit test of FcWwnInitiatorFactCollector class')
    exit(0)


if __name__ == '__main__':
    test_FcWwnInitiator

# Generated at 2022-06-13 01:27:53.556978
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    instance = FcWwnInitiatorFactCollector()
    assert instance is not None

# Generated at 2022-06-13 01:27:55.116300
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    FcWwnInitiatorFactCollector.collect(None, collector)

# Generated at 2022-06-13 01:28:01.686491
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    # _fact_ids will not be empty list
    assert bool(fc._fact_ids) == True
    # collect method will return dictionary
    assert isinstance(fc.collect(), dict)

# Generated at 2022-06-13 01:28:04.766987
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    c = FcWwnInitiatorFactCollector()
    assert c.name == 'fibre_channel_wwn'
    assert c._fact_ids is not None
    assert c._fact_ids == set()

# Generated at 2022-06-13 01:28:07.015301
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()
    FcWwnInitiatorFactCollector.collect()

# Generated at 2022-06-13 01:28:08.674407
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    my_fc_collector = FcWwnInitiatorFactCollector()
    assert my_fc_collector.collect() == {'fibre_channel_wwn': []}


# Generated at 2022-06-13 01:28:10.977300
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    collector = FcWwnInitiatorFactCollector()
    results = collector.collect()

    assert ('fibre_channel_wwn' in results)

# Generated at 2022-06-13 01:28:15.284485
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcFC = FcWwnInitiatorFactCollector()
    assert fcFC
    assert fcFC.name == 'fibre_channel_wwn'
    assert fcFC.platforms == set(['Linux', 'SunOS', 'AIX', 'HP-UX'])

# Generated at 2022-06-13 01:28:30.932700
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    c = Collector()
    fc = FcWwnInitiatorFactCollector()
    facts = c.collect(fc)
    assert 'fibre_channel_wwn' in facts
    assert len(facts['fibre_channel_wwn']) > 0


# Generated at 2022-06-13 01:28:33.045785
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'
    assert x._fact_ids is not None

# Generated at 2022-06-13 01:28:35.283062
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    assert FcWwnInitiatorFactCollector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:36.893407
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwn = FcWwnInitiatorFactCollector()
    assert fcwwn.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:38.371923
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    # default constructor
    FcWwnInitiatorFactCollector()


# Generated at 2022-06-13 01:28:41.645417
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:28:45.735817
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()

    assert fc_facts.name == 'fibre_channel_wwn'
    assert fc_facts.priority == 90
    assert fc_facts._fact_ids == set()

# Generated at 2022-06-13 01:28:49.941991
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    my_obj = FcWwnInitiatorFactCollector()
    assert my_obj
    assert my_obj.name == 'fibre_channel_wwn'
    assert my_obj._fact_ids == set()

# Generated at 2022-06-13 01:28:54.192692
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    import sys

    fc = FcWwnInitiatorFactCollector()
    assert fc
    assert fc.name == 'fibre_channel_wwn'
    if sys.platform.startswith('linux'):
        assert fc.collect() == {'fibre_channel_wwn': []}

# Generated at 2022-06-13 01:28:57.557549
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = FcWwnInitiatorFactCollector()
    assert fc_facts.name == "fibre_channel_wwn"
    assert isinstance(fc_facts._fact_ids, set)
    assert fc_facts.collect() == {}

# Generated at 2022-06-13 01:29:18.373407
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import module_utils.basic
    import os
    # create dummy file contents
    fc_fact = """0x21000014ff52a9bb
                    0x21000014ff52a9bb
                    0x21000014ff52a9bb
                    0x21000014ff52a9bb
                    """
    fc_facts = [i.strip() for i in fc_fact.splitlines()]
    # create dummy module object
    class DummyModule(object):
        def __init__(self):
            self.run_command_calls = dict()
            self.params = dict()

        def fail_json(self, **args):
            pass


# Generated at 2022-06-13 01:29:28.808998
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []
    fact_collector = FcWwnInitiatorFactCollector()
    fc_facts = fact_collector.collect()

    if fc_facts:
        count = 0
        for line in fc_facts['fibre_channel_wwn']:
            count += 1
        print("%s" % count)
    else:
        print("none")

# NOTE: use the following shell command to test the code in this file
# python -c "import ansible_facts.fibre_channel_wwn; ansible_facts.fibre_channel_wwn.test_FcWwnInitiatorFactCollector()"
#
# expected output:
#
# 0
#


# Generated at 2022-06-13 01:29:38.101294
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform

    if platform.system() == "Linux":
        fc_facts = {'fibre_channel_wwn': ['210000e08b9714a1']}
        collector = FcWwnInitiatorFactCollector()
        collected_facts = collector.collect()
        assert collected_facts == fc_facts
    elif platform.system() == "SunOS":
        fc_facts = {'fibre_channel_wwn': ['10000090fa1658de']}
        collector = FcWwnInitiatorFactCollector()
        collected_facts = collector.collect()
        assert collected_facts == fc_facts


# Generated at 2022-06-13 01:29:44.668315
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_collector_obj = FcWwnInitiatorFactCollector()
    assert fc_collector_obj.name == 'fibre_channel_wwn', 'Name of collector is not what expected'
    assert len(fc_collector_obj._fact_ids) == 0, 'The fact IDs per default should be empty'

# Generated at 2022-06-13 01:29:47.148214
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()
    assert x.name == 'fibre_channel_wwn'
    assert x._fact_ids == set()

# Generated at 2022-06-13 01:29:49.871156
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    test = FcWwnInitiatorFactCollector()
    assert test.name == 'fibre_channel_wwn'
    assert test._fact_ids == set()
    assert test.collect() == {}

# Generated at 2022-06-13 01:29:56.418132
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = _test_FcWwnInitiatorFactCollector_dict()
    test_module = _test_FcWwnInitiatorFactCollector_module()
    fc_fact_collector = FcWwnInitiatorFactCollector()
    fc_fact_collector.collect()
    assert fc_facts == fc_fact_collector.collect(test_module)


# Generated at 2022-06-13 01:29:58.718259
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:29:59.792744
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:02.493336
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_collector = FcWwnInitiatorFactCollector()
    assert 'fibre_channel_wwn' == fc_fact_collector.name

# Generated at 2022-06-13 01:30:29.889649
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for constructor of class FcWwnInitiatorFactCollector
    """
    from ansible.module_utils.facts.collector import BaseFactCollector
    fc_collector = FcWwnInitiatorFactCollector()
    assert type(fc_collector) == type(BaseFactCollector())
    assert fc_collector.name == 'fibre_channel_wwn'


if __name__ == '__main__':
    print('Only allowed to be used as a module')

# Generated at 2022-06-13 01:30:34.180825
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_collector = FcWwnInitiatorFactCollector()
    fc_collector.collect()

# Generated at 2022-06-13 01:30:36.817506
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Unit test for method collect of class FcWwnInitiatorFactCollector
    """

    # TODO: write unit test
    print("TODO: write unit test")

# Generated at 2022-06-13 01:30:47.584653
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # no unittest module loaded, exit
    if not sys.modules.get('unittest'):
        return
    if sys.version_info < (2, 7):
        return

    from ansible.module_utils.facts.collector import BaseFactCollector
    import unittest

    class FcWwnInitiatorFactCollectorTestCase(unittest.TestCase):
        """
        Test case for method collect of class
        FcWwnInitiatorFactCollector
        """

        def test_collect_no_glob(self):
            """
            Test collect method of class FcWwnInitiatorFactCollector
            """
            import platform
            import os
            import errno

            class MockModule(object):
                def __init__(self, name):
                    self.name = name
                    self

# Generated at 2022-06-13 01:30:57.623419
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Unit test for collect method of class FcWwnInitiatorFactCollector"""

    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = []

    fc_facts['fibre_channel_wwn'].append("10000090fa1658de")
    fc_facts['fibre_channel_wwn'].append("10000090fa1658df")
    fc_facts['fibre_channel_wwn'].append("10000090fa1658d0")

    fcwwnfactcollector = FcWwnInitiatorFactCollector()

    data = fcwwnfactcollector.collect()
    assert data == fc_facts


# Generated at 2022-06-13 01:31:01.026991
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Unit test for constructor of class FcWwnInitiatorFactCollector
    """
    fc_wwn_init = FcWwnInitiatorFactCollector()
    assert fc_wwn_init.name == 'fibre_channel_wwn'
    assert fc_wwn_init._fact_ids == set()

# Generated at 2022-06-13 01:31:12.291349
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import sys

    # initialize the test environment
    module_args = dict(
        gather_subset=["all"]
    )

    from ansible.compat.tests import unittest

    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.fibre_channel_wwn import FcWwnInitiatorFactCollector

    # initialize the test class
    class TestFcWwnInitiatorFactCollector(unittest.TestCase):
        def setUp(self):
            self.collector = FcWwnInitiatorFactCollector()

    # set up and initialize the test object
    setUp = TestFcWwnInitiatorFactCollector()
    setUp.setUp()

    # assert that the fact module returns a dictionary
    result = setUp

# Generated at 2022-06-13 01:31:22.971324
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import os
    m = type('module', (object, ), {})
    m.run_command = lambda x: (0, os.linesep.join(('HBA Port WWN: 10000090fa1658de',
                                                    'HBA Port WWN: 10000090fa1658df',
                                                    'HBA Port WWN: 21000014ff52a9bb')), '')
    m.get_bin_path = lambda x, opt_dirs=None: '/usr/bin/fcinfo'
    fc_facts = FcWwnInitiatorFactCollector().collect(m)
    assert len(fc_facts['fibre_channel_wwn']) == 3

# Generated at 2022-06-13 01:31:29.015253
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils import basic

    # create a dummy module and a mock object for module class
    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    # create a mock get_bin_path method in module
    module.get_bin_path = lambda executable, required=False, opt_dirs=[] : executable

    # get FcWwnInitiatorFactCollector instance for unit test
    fact_collector = get_collector_instance(FcWwnInitiatorFactCollector)

    # check if it is a instance of BaseFactCollector

# Generated at 2022-06-13 01:31:30.785000
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc = FcWwnInitiatorFactCollector()
    # placeholder for future unit test
    assert False

# Generated at 2022-06-13 01:32:19.052381
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    my_object = FcWwnInitiatorFactCollector()
    assert my_object.name == "fibre_channel_wwn"

# Generated at 2022-06-13 01:32:20.541971
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """Unit test for constructor of class FcWwnInitiatorFactCollector"""
    factCollector = FcWwnInitiatorFactCollector()
    assert factCollector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:31.901240
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    test_collector = Collector()
    test_collector.collect_facts = dict()
    test_collector.collect_facts['module_setup'] = True
    test_collector.collect_facts['ansible_facts']= dict()
    test_collector.collect_facts['ansible_facts']['ansible_fibre_channel_wwn']=[]
    test_collector.collect_facts['ansible_facts']['ansible_fibre_channel_wwn'].append("21000014ff52a9bb")

    fc_wwn_initiator_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_wwn_initiator_fact_collector.collect

# Generated at 2022-06-13 01:32:33.406644
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    c = FcWwnInitiatorFactCollector()
    assert c

# Generated at 2022-06-13 01:32:40.830714
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    mock_module = MockModule()
    mock_module.run_command.return_value = (0, '', '')
    mock_module.get_bin_path.return_value = True
    mock_module.get_file_lines.return_value = ['0x21000014ff52a9bb\n', '0x21000014ff52a9bc']
    fc_facts = FcWwnInitiatorFactCollector(mock_module).collect()
    assert fc_facts == {u'fibre_channel_wwn': [u'21000014ff52a9bb', u'21000014ff52a9bc']}

# This mock class provides a minimal implementation required to
# instantiate and run the class being tested.

# Generated at 2022-06-13 01:32:43.032538
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:47.662055
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fcn = FcWwnInitiatorFactCollector()
    assert fc_fcn.name == 'fibre_channel_wwn'
    assert isinstance(fc_fcn._fact_ids, set)
    assert 'ansible_' + fc_fcn.name in fc_fcn._fact_ids
    assert repr(fc_fcn) == 'None'

# Generated at 2022-06-13 01:32:50.468728
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Returns a test object of the FcWwnInitiatorFactCollector class.
    """
    return FcWwnInitiatorFactCollector()

# Unit test: To test the collect function of FcWwnInitiatorFactCollector.

# Generated at 2022-06-13 01:32:52.177706
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcWwnInitiatorFactCollector = FcWwnInitiatorFactCollector()
    assert fcWwnInitiatorFactCollector.collect()

# Generated at 2022-06-13 01:32:55.110534
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == "fibre_channel_wwn"
    assert fc.collect() is not None

# Generated at 2022-06-13 01:34:33.184964
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    o = FcWwnInitiatorFactCollector()
    assert o.name == 'fibre_channel_wwn'
    assert isinstance(o.collect(), dict)

# Generated at 2022-06-13 01:34:35.835304
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    x = FcWwnInitiatorFactCollector()

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:34:40.556873
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    ffcv = FcWwnInitiatorFactCollector()
    assert ffcv is not None
    assert ffcv.name == 'fibre_channel_wwn'
    assert set('fibre_channel_wwn') == ffcv._fact_ids


# Generated at 2022-06-13 01:34:50.607229
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    fc_facts = collector.collect()
    assert len(fc_facts['fibre_channel_wwn']) >= 1
    assert '500a0b80001b3aec' in fc_facts['fibre_channel_wwn']
    assert '0000090fa1658de' in fc_facts['fibre_channel_wwn']
    assert '21000014ff52a9bb' in fc_facts['fibre_channel_wwn']
    assert '10000090FA551509' in fc_facts['fibre_channel_wwn']
    assert '50060b00006975ec' in fc_facts['fibre_channel_wwn']


# Generated at 2022-06-13 01:34:52.007682
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector is not None
    assert fact_collector.name == "fibre_channel_wwn"

# Generated at 2022-06-13 01:34:55.169901
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    
    facts = FcWwnInitiatorFactCollector()
    data = facts.collect()
    # test data should be a hash
    assert type(data) is dict, \
        "Test data should be of type dict, got '%s' instead" % type(data)
    # test data should contain 'fibre_channel_wwn' key
    assert 'fibre_channel_wwn' in data, \
        "'fibre_channel_wwn' key not found in test data"

# Generated at 2022-06-13 01:34:58.621217
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:35:07.200025
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # setup module args
    module_args = {}

    # setup module object
    mock_module = type('module', (object,), module_args)
    mock_module.run_command = MagicMock(return_value=(0, '', ''))
    mock_module.get_bin_path = MagicMock(return_value=True)

    # instantiate FcWwnInitiatorFactCollector class
    fc_wwn_fc = FcWwnInitiatorFactCollector(mock_module)

    # collect FcWwnInitiator facts
    fc_wwn_facts = fc_wwn_fc.collect(mock_module, {})

    # check if expected results are in the facts
    assert fc_wwn_facts['fibre_channel_wwn']

# Generated at 2022-06-13 01:35:11.178003
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fixture_data = {
        '/sys/class/fc_host/host0/port_name': """0x21000014ff52a9bb""",
        '/sys/class/fc_host/host1/port_name': """0x21000014ff52a9bb""",
    }

    for k, v in fixture_data.items():
        collector = FcWwnInitiatorFactCollector(file_name=k)
        assert collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:35:13.749499
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fw = FcWwnInitiatorFactCollector()
    assert fw.name == 'fibre_channel_wwn'
    assert fw._fact_ids == set()
