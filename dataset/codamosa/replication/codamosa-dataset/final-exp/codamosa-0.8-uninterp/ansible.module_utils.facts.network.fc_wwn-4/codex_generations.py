

# Generated at 2022-06-13 01:27:34.783025
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fact_collector = FcWwnInitiatorFactCollector()
    facts = fact_collector.collect()
    assert 'fibre_channel_wwn' in facts
    assert isinstance(facts['fibre_channel_wwn'], list)

    assert len(facts['fibre_channel_wwn']) > 0

# Generated at 2022-06-13 01:27:37.606850
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc = FcWwnInitiatorFactCollector()
    assert fc.name == 'fibre_channel_wwn'
    assert fc._fact_ids == set()


# Generated at 2022-06-13 01:27:47.359704
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    class MockModule(object):
        """ mock AnsibleModule for FcWwnInitiatorFactCollector """

        class MockRunCommand(object):
            """ mock run_command method for ansible module """
            def __init__(self, out_str, err_str, exit_code):
                self.out = out_str
                self.err = err_str
                self.rc = exit_code

        def __init__(self, out_str, err_str, exit_code):
            self.run_command = self.MockRunCommand(out_str, err_str, exit_code)

        def run_command(self, cmd):
            return self.run_command

        def get_bin_path(self, cmd, opt_dirs=['']):
            return '/usr/bin/' + cmd


# Generated at 2022-06-13 01:27:56.954017
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    import sys
    from ansible.module_utils.facts.collector import BaseFactCollector
    sys.modules['ansible.module_utils.facts.collector'] = BaseFactCollector

    import pytest
    from ansible.module_utils.facts.system.fibre_channel_wwn import FcWwnInitiatorFactCollector

    test_object = FcWwnInitiatorFactCollector()

    # Create a class object to be used as a fake AnsibleModule
    class FakeAnsibleModule():
        def __init__(self, **kwargs):
            self.params = kwargs
        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('FAIL')

    # Create a class object

# Generated at 2022-06-13 01:28:04.045801
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import *
    from ansible.module_utils.facts.utils import get_file_content
    import os
    import tempfile
    import shutil
    import unittest

    class TestModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, **kwargs):
            pass

        def get_bin_path(self, executable, required=True, opt_dirs=[]):
            return executable

        def run_command(self, cmd):
            return (0, '', '')

    class TestCollector(object):
        def __init__(self):
            self.platform = 'linux'


# Generated at 2022-06-13 01:28:05.156331
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    o = FcWwnInitiatorFactCollector()
    assert o.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:28:07.747873
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    result = FcWwnInitiatorFactCollector()
    assert result.name == 'fibre_channel_wwn'
    assert result._fact_ids is not None

# Generated at 2022-06-13 01:28:13.814463
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_fact_collector = FcWwnInitiatorFactCollector()
    assert fc_fact_collector.name == 'fibre_channel_wwn', \
        'fibre_channel_wwn collector has an incorrect name'
    assert fc_fact_collector._fact_ids == set(), \
        'fact ids are not empty'

# Generated at 2022-06-13 01:28:19.872739
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """Unit test for method collect of class FcWwnInitiatorFactCollector"""
    # instantiate a FcWwnInitiatorFactCollector object
    fc_initiator_facts = FcWwnInitiatorFactCollector()
    # test method collect with valid input
    facts = fc_initiator_facts.collect()
    assert isinstance(facts, dict)
    assert 'fibre_channel_wwn' in facts
    assert isinstance(facts['fibre_channel_wwn'], list)

# Generated at 2022-06-13 01:28:30.589302
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # test on linux
    # create mock module
    class MockModule:
        def __init__(self):
            self.params = {}
        def get_bin_path(self, name):
            return name

    # create mock facts
    class MockFacts:
        def __init__(self):
            self.facts = {}

    # create mock commands
    class MockCommand:
        def __init__(self):
            self.rc = 0
            self.stdout = '0x21000014ff52a9bb'
            self.stderr = ''

    mock = MockModule()
    mock.run_command = MockCommand()

    # collect fc facts
    fc = FcWwnInitiatorFactCollector()
    fc.collect(mock, MockFacts())

    # check facts

# Generated at 2022-06-13 01:28:51.252441
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # parameters for instantiating the class
    module = None
    collected_facts = None

    # Instantiate the class
    fcwwn_collector = FcWwnInitiatorFactCollector()

    # Call the method
    fcwwn_facts = fcwwn_collector.collect(module=module, collected_facts=collected_facts)

    # Test the method
    assert 'fibre_channel_wwn' in fcwwn_facts
    assert fcwwn_facts['fibre_channel_wwn'] != []

# Generated at 2022-06-13 01:28:59.839393
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """ Unit test: test_FcWwnInitiatorFactCollector_collect """

    # pylint: disable=W0212
    # Access to a protected member of a client class

    import os

    class MockModule(object):
        """ class MockModule: mocks class `ansible.module_utils.basic.AnsibleModule` """

        def __init__(self, **kwargs):
            """ constructor """

            self.params = kwargs

        def run_command(self, command):
            """ run_command: mock method """

            output = self.params['output']
            return self.params['rc'], output, self.params['err']

        @staticmethod
        def get_bin_path(prog, opt_dirs=[]):
            """ get_bin_path: mock method """


# Generated at 2022-06-13 01:29:00.799975
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    pass

# Generated at 2022-06-13 01:29:02.156368
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    FcWwnInitiatorFactCollector.collect(None)



# Generated at 2022-06-13 01:29:04.663412
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fw = FcWwnInitiatorFactCollector()
    assert fw.name == 'fibre_channel_wwn'
    assert fw._fact_ids

# Generated at 2022-06-13 01:29:15.553045
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # define and import module (name is 'ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.f5.facts.fibre_channel_wwn')
    sys.modules["ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.f5.facts.fibre_channel_wwn"] = AnsibleModuleMock
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.f5.facts.fibre_channel_wwn import FcWwnInitiatorFactCollector
    # define some parameters for AnsibleModuleMock.run_command
    cmd = "/sbin/ioscan"

# Generated at 2022-06-13 01:29:18.074124
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts = FcWwnInitiatorFactCollector()
    assert facts.name == 'fibre_channel_wwn'
    assert facts.priority == 10

# Generated at 2022-06-13 01:29:26.092913
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    test_collector = FcWwnInitiatorFactCollector()
    fc_facts = test_collector.collect()
    if fc_facts:
        if fc_facts['fibre_channel_wwn']:
            # do something with fc_facts
            print(fc_facts)
        else:
            print('no fibre_channel_wwn facts collected')
    else:
        print('no fibre_channel_wwn facts collected')

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector_collect()

# Generated at 2022-06-13 01:29:35.703887
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = {}
    fc_facts['fibre_channel_wwn'] = ['21000014ff0ccff7']
    class MockModule:
        def __init__(self):
            self.run_command = lambda cmd, module: (0, '', '')
            self.get_bin_path = lambda name, opt_dirs=[] : ''
    module = MockModule()
    fc_collector = FcWwnInitiatorFactCollector(module=module)
    fc_collector.collect(module=module)
    assert fc_facts == fc_collector.collect(module=module)

# Generated at 2022-06-13 01:29:39.666998
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert obj._fact_ids == set()

# Generated at 2022-06-13 01:30:05.801449
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fc_wwn_facts = FcWwnInitiatorFactCollector()
    assert fc_wwn_facts.name == 'fibre_channel_wwn'


# Generated at 2022-06-13 01:30:12.556356
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    import platform
    import pprint
    sys.modules['ansible.module_utils.facts.collector'] = mock.Mock()
    sys.modules['ansible.module_utils.facts.utils'] = mock.Mock()

    # first mock sys.platform return value
    sys.platform = "linux2"
    fc_facts = FcWwnInitiatorFactCollector()
    fc_facts.collect()

    sys.platform = "solaris2"
    fc_facts = FcWwnInitiatorFactCollector()
    fc_facts.collect()

    sys.platform = "aix7"
    fc_facts = FcWwnInitiatorFactCollector()
    fc_facts.collect()

    sys.platform = "hp-ux11"
    fc_facts = F

# Generated at 2022-06-13 01:30:15.271006
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    results = FcWwnInitiatorFactCollector()
    assert results.name == 'fibre_channel_wwn'
    assert results.collect() == {}

# Generated at 2022-06-13 01:30:24.667279
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Test the constructor of class FcWwnInitiatorFactCollector
    """
    if sys.platform.startswith('linux'):
        fc_facts = {'fibre_channel_wwn': ['21000014ff52a9bb']}
    elif sys.platform.startswith('sunos'):
        fc_facts = {'fibre_channel_wwn': ['10000090fa1658de']}
    elif sys.platform.startswith('hp-ux'):
        fc_facts = {'fibre_channel_wwn': ['50060b00006975ec']}
    elif sys.platform.startswith('aix'):
        fc_facts = {'fibre_channel_wwn': ['10000090FA551509']}


# Generated at 2022-06-13 01:30:27.602413
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # The linux platform should give at least 1 WWN
    module = FakeAnsibleModule()
    collector = FcWwnInitiatorFactCollector()
    fc_facts = collector.collect(module=module)
    assert len(fc_facts['fibre_channel_wwn']) > 0


# Generated at 2022-06-13 01:30:30.267393
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fci = FcWwnInitiatorFactCollector()
    assert fci.name == 'fibre_channel_wwn'
    assert fci._fact_ids == set()


# Generated at 2022-06-13 01:30:37.917084
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    tests = [
        { 'platform': 'SunOS'},
        { 'platform': 'Linux'},
        { 'platform': 'AIX'},
        { 'platform': 'HP-UX'},
    ]
    for test in tests:
        collector = FcWwnInitiatorFactCollector(None, test)
        assert collector.name == 'fibre_channel_wwn'
        assert collector._fact_ids == set()

# Generated at 2022-06-13 01:30:40.287057
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:30:43.981684
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector is not None

if __name__ == '__main__':
    test_FcWwnInitiatorFactCollector()

# Generated at 2022-06-13 01:30:49.283161
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """ Unit test for constructor of class FcWwnInitiatorFactCollector """
    collected_facts = {}
    test_object = FcWwnInitiatorFactCollector(collected_facts)
    assert test_object.name == 'fibre_channel_wwn'
    assert not test_object._fact_ids
    assert not test_object._platforms

# Generated at 2022-06-13 01:31:44.416129
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector

    class FakeModule():
        def get_bin_path(self, arg, opt_dirs=None):
            return '/bin/false'
        def run_command(self, arg):
            return 0, 'foo', 'bar'

    module = FakeModule()
    fc_facts = FcWwnInitiatorFactCollector().collect(module=module, collected_facts={})

    assert(fc_facts['fibre_channel_wwn'] == [])

# Generated at 2022-06-13 01:31:47.596043
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    t = FcWwnInitiatorFactCollector()
    assert t.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:31:53.793477
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    method collect of class FcWwnInitiatorFactCollector:

    Testcase 1:
    input:
    on solaris 11
    output:
    {'fibre_channel_wwn': ['10000090fa1658de']}

    Testcase 2:
    input:
    on AIX
    output:
    {'fibre_channel_wwn': [u'10000090FA551509']}

    Testcase 3:
    input:
    on HP-UX
    output:
    {'fibre_channel_wwn': [u'0x50060b00006975ec']}
    """

    # Testcase 1: solaris
    import sys
    sys.platform = 'sunos'
    import ansible.module_utils.facts.collector

# Generated at 2022-06-13 01:31:57.487505
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    """
    Test method collect of class FcWwnInitiatorFactCollector
    """
    FcWwnInitiatorFactCollector._create_dirs = lambda: True
    FcWwnInitiatorFactCollector._remove_dirs = lambda: True
    fcwwn = FcWwnInitiatorFactCollector()
    fc_facts = fcwwn.collect()
    assert isinstance(fc_facts.get('fibre_channel_wwn'), list)
    assert len(fc_facts.get('fibre_channel_wwn')) > 0

# Generated at 2022-06-13 01:32:00.375443
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'
    assert isinstance(obj._fact_ids, set)
    assert obj.collect() == {}

# Generated at 2022-06-13 01:32:03.394826
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    """
    Constructor of class FcWwnInitiatorFactCollector
    """
    fcfacts = FcWwnInitiatorFactCollector()
    assert fcfacts.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:32:09.200843
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    class ModuleMock(object):
        def get_bin_path(self, arg1, opt_dirs=None):
            # test if get_bin_path() is called at all
            assert arg1, 'test failed'
            return True

    module = ModuleMock()
    result = FcWwnInitiatorFactCollector().collect(module)
    assert result == { 'fibre_channel_wwn': [] }, 'test failed'

# Generated at 2022-06-13 01:32:15.093183
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    collector = FcWwnInitiatorFactCollector()
    ans_vars = {'ansible_facts': {'fibre_channel_wwn': ['21000014ff52a9bb']}}
    fc_vars = collector.collect(module=None, collected_facts=None)
    assert ans_vars['ansible_facts']['fibre_channel_wwn'] == fc_vars['fibre_channel_wwn']

# Generated at 2022-06-13 01:32:22.898384
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    from ansible.module_utils.facts import ini_to_dict
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.system.fibre_channel_wwn import FcWwnInitiatorFactCollector

    fakedevs_dict = ('[device]\n'
                     'fibre_channel_wwn = [ \'0x21000014ff52a9bb\' ]\n')
    ini_file = ini_to_dict(fakedevs_dict)
    if sys.platform.startswith('linux'):
        fcwwn_module = FcWwnInitiatorFactCollector()
        fcwwn_module.collect()
        result_dict = FactCollector().collect(ini_file=ini_file)


# Generated at 2022-06-13 01:32:27.473965
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fcwwninitiator = FcWwnInitiatorFactCollector()
    assert fcwwninitiator.name == "fibre_channel_wwn"
    assert fcwwninitiator.collect() == {}

# Generated at 2022-06-13 01:34:09.129560
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    # create an instance of class FcWwnInitiatorFactCollector
    fcwwn = FcWwnInitiatorFactCollector()
    # create an instance of class Facts with name and empty dict
    facts_object = Facts(FcWwnInitiatorFactCollector.name, {})
    # call collect method
    facts = fcwwn.collect(facts_object)
    # at least expect an empty dict for fibre_channel_wwn
    assert isinstance(facts, dict)
    if 'fibre_channel_wwn' in facts:
        assert isinstance(facts['fibre_channel_wwn'], list)
    # TODO: write a unit test that mocks the OS and the interface to os.py


# Generated at 2022-06-13 01:34:12.995543
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    collector = FcWwnInitiatorFactCollector()
    facts_list = collector.collect()
    assert 'fibre_channel_wwn' in facts_list

# Generated at 2022-06-13 01:34:19.926171
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    def get_fake_file_lines(*args, **kwargs):
        return ['0x21000014ff52a9bb']

    mod_obj = _get_fake_module_obj()
    mod_obj.get_bin_path = _get_fake_bin_path
    fci = FcWwnInitiatorFactCollector()
    res = fci.collect(module=mod_obj)

    assert res == {
        'fibre_channel_wwn': ['21000014ff52a9bb']
    }



# Generated at 2022-06-13 01:34:23.075427
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    object = FcWwnInitiatorFactCollector()
    assert object.name == 'fibre_channel_wwn'
    assert object._fact_ids == set()

# Generated at 2022-06-13 01:34:27.903668
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():
    fc_facts = FcWwnInitiatorFactCollector().collect()
    assert 'fibre_channel_wwn' in fc_facts
    assert fc_facts['fibre_channel_wwn'] != []

if __name__ == '__main__':
    my_test = FcWwnInitiatorFactCollector()
    print(my_test.collect())

# Generated at 2022-06-13 01:34:30.214962
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fci = FcWwnInitiatorFactCollector()
    assert fci.name == 'fibre_channel_wwn'
    assert not fci._fact_ids

# Generated at 2022-06-13 01:34:33.185874
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    fact_collector = FcWwnInitiatorFactCollector()
    assert fact_collector.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:35.477442
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    obj = FcWwnInitiatorFactCollector()
    assert obj.name == 'fibre_channel_wwn'

# Generated at 2022-06-13 01:34:37.438052
# Unit test for constructor of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector():
    facts = FcWwnInitiatorFactCollector()
    assert facts.collect() == {}


# unit test for this module.
if __name__ == "__main__":
    import pytest
    test_FcWwnInitiatorFactCollector()

    pytest.main([__file__])

# Generated at 2022-06-13 01:34:45.291717
# Unit test for method collect of class FcWwnInitiatorFactCollector
def test_FcWwnInitiatorFactCollector_collect():

    class TestModule:
        def __init__(self):
            self.test_value = ''
            self.result = {'rc': 0, 'out': '', 'err': ''}

        def get_bin_path(self, item, opt_dirs=[]):
            if item == 'fcmsutil':
                return 'fcmsutil'
            if item == 'fcinfo':
                return 'fcinfo'
            if item == 'ioscan':
                return 'ioscan'
            if item == 'lscfg':
                return 'lscfg'
            if item == 'lsdev':
                return 'lsdev'
            return ''

        def run_command(self, cmd):
            return self.result['rc'], self.result['out'], self.result['err']
