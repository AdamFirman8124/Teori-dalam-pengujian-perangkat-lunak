

# Generated at 2022-06-13 03:02:01.807357
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = AnsibleModuleMock()
    module.get_bin_path = Mock(return_value='/usr/bin')
    module.run_command = Mock(return_value=(0, 'LSB Version:\tcore-2.0-amd64:core-2.0-noarch', ''))

    lsb_collector = LSBFactCollector()
    result = lsb_collector.collect(module=module)
    assert result is not None
    assert result['lsb'] is not None
    assert result['lsb']['release'] is not None
    assert result['lsb']['major_release'] is not None

# Testing class LSBFactCollector without lsb_release command

# Generated at 2022-06-13 03:02:03.008493
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'

# Generated at 2022-06-13 03:02:04.647868
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert lsb_collector.name == 'lsb'
    assert 'lsb' in lsb_collector.__dict__
    assert lsb_collector._fact_ids == set()

# Generated at 2022-06-13 03:02:06.882460
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    collector = LSBFactCollector()
    assert(collector.collect()['lsb'] == {})


# Generated at 2022-06-13 03:02:08.040212
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'

# Generated at 2022-06-13 03:02:09.410749
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert hasattr(LSBFactCollector, 'collect')

# Generated at 2022-06-13 03:02:21.469226
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import get_file_content
    mock_module = AnsibleCollector(None, None, None)
    mock_module.run_command = run_command_mock
    LSBFactCollector._get_file_content = get_file_content_mock
    LSBFactCollector._get_file_lines = get_file_lines_mock
    os.path.exists = path_exists_mock

# Generated at 2022-06-13 03:02:34.247879
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    class ModuleDouble(object):
        def __init__(self, rc, stdout):
            self._rc = rc
            self._stdout = stdout

        def run_command(self, command, errors='surrogate_then_replace'):
            return self._rc, self._stdout, ''

        def get_bin_path(self, executable, required=False):
            return '/usr/bin/' + executable

    collector = LSBFactCollector()
    stdout = '''
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04.3 LTS
Release:	14.04
Codename:	trusty
'''
    module = ModuleDouble(0, stdout)
    result = collector.collect(module=module,
                               collected_facts={})


# Generated at 2022-06-13 03:02:42.643509
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    """
    Unit test for method collect of class LSBFactCollector
    """
    lsb_file = '/etc/lsb-release'
    lsb_facts_file = {'id': 'Ubuntu', 'codename': 'bionic', 'description': 'Ubuntu 18.04.1 LTS', 'release': '18.04'}
    lsb_facts_bin = {'codename': 'xenial', 'description': 'Ubuntu 16.04.5 LTS', 'id': 'Ubuntu', 'release': '16.04'}

    lsb_fact_collector = LSBFactCollector()

    # test the _lsb_release_file method of class LSBFactCollector
    # case 1: lsb_file exists and is not empty

# Generated at 2022-06-13 03:02:44.452598
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x
    assert x.name == 'lsb'
    assert x._fact_ids == set()
    assert x.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:02:59.095911
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    class Platform:
        def __init__(self):
            self.dist = ['Ubuntu']
            self.lsb_distrib_codename = 'Leopard'
            self.lsb_distrib_id = 'Ubuntu'
            self.lsb_distrib_release = '18.04'
            self.lsb_distrib_description = 'Ubuntu 18.04'
            self.uname = ['Linux']
            self.uname_machine = ['x86_64']
            self.arch = 'x86_64'
            self.system = 'Linux'
            self.machine = 'x86_64'
            self.kernel = 'Linux'
    class Module:
        def get_bin_path(self, path):
            return path
        def run_command(self, path, errors):
            return 0,

# Generated at 2022-06-13 03:03:01.679858
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    """Test LSBFactCollector constructor"""
    lsb_fact_collector = LSBFactCollector()
    print(lsb_fact_collector)


# Generated at 2022-06-13 03:03:04.968512
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    """Test the method collect
    """
    lsb_fact_collector = LSBFactCollector()
    lsb_fact_collector.collect()


# Generated at 2022-06-13 03:03:12.388242
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Setup
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/lsb_release'

    from ansible.module_utils.facts import ansible_lsb
    lsb_facts = ansible_lsb.LSBFactCollector().collect(module)

    # Test
    assert lsb_facts['lsb']['major_release'] == "14"
    assert lsb_facts['lsb']['release'] == "14.04"
    assert lsb_facts['lsb']['id'] == "Ubuntu"
    assert lsb_facts['lsb']['description'] == "Ubuntu 14.04.3 LTS"
    assert lsb_facts['lsb']['codename'] == "trusty"


# Generated at 2022-06-13 03:03:14.408825
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    _test_lsb_collector = LSBFactCollector()
    assert _test_lsb_collector is not None

# Generated at 2022-06-13 03:03:22.902952
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from lxml import etree
    from unittest import TestCase

    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collectors.lsb import LSBFactCollector
    from ansible.module_utils.facts.utils import get_file_lines

    class ModuleStub(object):
        def get_bin_path(self, path):
            return '/usr/bin/lsb_release'


# Generated at 2022-06-13 03:03:32.094675
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    # Test with correct and not correct bin path
    class MockedModule:

        def __init__(self):
            self.lsb_path = '/bin/lsb_release'

        def get_bin_path(self, command):
            return self.lsb_path

        def run_command(self, args, errors):
            if args[0] == '/bin/lsb_release':
                return 0, '/bin/lsb_release -a', ''
            return 1, 'lsb_release -a', ''

    # Test without correct bin path
    lsb_fact_collector = LSBFactCollector()
    lsb_facts = lsb_fact_collector.collect(MockedModule())
    assert 'lsb' in lsb_facts, 'lsb not in facts array !'

# Generated at 2022-06-13 03:03:41.606757
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    import os
    import json
    import tempfile
    from ansible.module_utils.facts.collector import DictFactsCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors import lsb as lsb_module

    # create the facts collector object
    lsb = LSBFactCollector()
    # create a mock object for the ansible module class
    class AnsiModuleMock(object):
        def __init__(self):
            self.params = {}
            self.run_command_environ_update = {}
            self.run_command_stdout_lines = []
            self.run_command_stdout = ""
            self.run_command_rc = 0

# Generated at 2022-06-13 03:03:43.181910
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'

# Generated at 2022-06-13 03:03:51.068146
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.collector import add_collector
    from ansible.module_utils.facts.collector.lsb import LSBFactCollector
    from ansible.module_utils.facts.utils import AnsibleFactCollector

    # Setup a fake module and some global variables that are normally set by the module

    class FakeModule:
        def __init__(self, name):
            self.PATH = "/bin:/usr/bin"
            self.name = name

        def get_bin_path(self, name):
            if self.name == "lsb_release":
                return "/bin/lsb_release"
            else:
                return None


# Generated at 2022-06-13 03:04:10.607394
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb = LSBFactCollector()

    # lsb_path = module.get_bin_path('lsb_release')
    lsb_path = '/usr/bin/lsb_release'

    module = {'get_bin_path': lambda x: lsb_path if x == 'lsb_release' else None,
              'run_command': lambda x, y=None: (0, None, None) if x[0] == lsb_path else (1, None, None)
              }

    lsb._lsb_release_bin(lsb_path, module)

# Generated at 2022-06-13 03:04:14.279569
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'

# Generated at 2022-06-13 03:04:18.117895
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts import Collector

    LSBFactCollector.collect()
    module_mock = type('ModuleMock', (object,), {'run_command':run_command_mock})()
    Collector.collect(module_mock)



# Generated at 2022-06-13 03:04:19.694650
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    m = LSBFactCollector()
    assert m.name == 'lsb'

# Generated at 2022-06-13 03:04:22.343306
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    testobj = LSBFactCollector()
    assert testobj
    assert testobj.name == 'lsb'
    assert testobj._fact_ids == set()
    assert testobj.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:04:32.965618
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = mock.MagicMock()
    module.get_bin_path = mock.MagicMock()
    module.run_command = mock.MagicMock()

    # 1) test when lsb_release is available on path, /etc/lsb-release does not exist
    module.get_bin_path.return_value = '/usr/bin/lsb_release'
    module.run_command.return_value = (0, '''\
Distributor ID:		Ubuntu
Description:		Ubuntu 15.10
Release:		15.10
Codename:		wily
''', '')
    lsb = LSBFactCollector()
    actual = lsb.collect()

# Generated at 2022-06-13 03:04:35.290491
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    LSBFC = LSBFactCollector()

    LSBFC._lsb_release_file('/etc/lsb-release')
    LSBFC._lsb_release_bin('/bin/lsb_release')

# Generated at 2022-06-13 03:04:37.574621
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_collector = LSBFactCollector()
    lsb_collector.collect()

# Generated at 2022-06-13 03:04:45.861704
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    if HAS_HOST_DATA:
        lsb_facts = host_data['lsb']
    else:
        from ansible.module_utils._text import to_text
        from ansible.module_utils.facts.collectors.lsb.test_lsb import _OUT
        lsb_facts = to_text(_OUT)

    # Create a namedtuple object
    hostvars = {'ansible_mounts': ""}

    # Create the mock module
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False,
    )

    lsb_collector = LSBFactCollector(module=module)
    assert lsb_collector.collect(module) == lsb_facts

# Generated at 2022-06-13 03:04:48.382963
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert(lsb_fact_collector.name == 'lsb')
    assert(lsb_fact_collector.STRIP_QUOTES == r'\'\"\\')

# Generated at 2022-06-13 03:05:22.514529
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    os.environ['LSB_RELEASE_BIN'] = 'test_lsb_release_bin'
    os.environ['LSB_RELEASE_FILE'] = 'test_lsb_release_file'
    lsb_fc = LSBFactCollector()
    assert lsb_fc._lsb_release_bin('test_lsb_release_bin', '') == {}
    assert lsb_fc._lsb_release_file('test_lsb_release_file') == {}
    assert lsb_fc.collect('', '') == {'lsb': {}}
    del os.environ['LSB_RELEASE_BIN']
    del os.environ['LSB_RELEASE_FILE']

# Generated at 2022-06-13 03:05:24.366919
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    """
    Test LSBFactCollector constructor
    """
    LSBFactCollector()

# Generated at 2022-06-13 03:05:25.826499
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    fact_collector = LSBFactCollector()
    assert 'lsb' == fact_collector.name

# Generated at 2022-06-13 03:05:28.328296
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    collector = LSBFactCollector()
    assert collector.name == 'lsb'
    assert collector._fact_ids == set()
    assert collector.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:05:37.891704
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts.collector import BaseFactCollector

    def _lsb_release_file_return(etc_lsb_release_location):
        return {
            'description': 'Ubuntu 14.04.5 LTS',
            'id': 'Ubuntu',
            'release': '14.04',
            'codename': 'trusty'
        }

    def _lsb_release_bin_return(lsb_path, module):
        return {}

    LSBFactCollector._lsb_release_file = _lsb_release_file_return
    LSBFactCollector._lsb_release_bin = _lsb_release_bin_return

    module = ModuleStub()
    collected_facts = {}
    lsb_

# Generated at 2022-06-13 03:05:39.948603
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector(None)
    assert lsb_fact_collector.name == 'lsb'


# Generated at 2022-06-13 03:05:41.551964
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'

# Generated at 2022-06-13 03:05:48.675519
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    LSBFactCollector._fact_ids = set()
    LSBFactCollector.STRIP_QUOTES = r'\'\"\\'
    lsb_facts = LSBFactCollector.collect()
    assert lsb_facts['lsb']
    assert lsb_facts['lsb']['release']
    assert lsb_facts['lsb']['id']
    assert lsb_facts['lsb']['description']
    assert lsb_facts['lsb']['codename']
    assert lsb_facts['lsb']['major_release']

# Generated at 2022-06-13 03:05:57.220542
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    test_lsb_facts = {
        'lsb': {
            'id': 'RedHatEnterpriseServer',
            'major_release': '7',
            'description': 'Red Hat Enterprise Linux Server 7.4 (Maipo)',
            'codename': 'Maipo',
            'release': '7.4'
        }
    }

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes

    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['all']


# Generated at 2022-06-13 03:06:07.191504
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    facts_dict = {}
    lsb_facts = {
        'id': 'Ubuntu',
        'release': '12.04',
        'codename': 'precise',
        'description': 'Ubuntu 12.04.5 LTS',
        'major_release': '12'
    }

    # test lsb_release_bin
    # read_from_file: can't be tested
    # run_command: tested in test_facts.py
    # _lsb_release_file: can't be tested
    # _lsb_release_file: can't be tested

    # test _lsb_release_file
    lsb_facts_2 = LSBFactCollector()._lsb_release_file('/etc/lsb-release')

    # test collect
    result = LSBFactCollector().collect()



# Generated at 2022-06-13 03:07:08.913891
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    pass

# Generated at 2022-06-13 03:07:14.619819
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    """Unit test for LSBFactCollector.collect method."""
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.six import PY3

    collected_facts = dict()

    c = LSBFactCollector()

    # Test if collect method return info
    # of 'lsb' section of collected_facts
    c.collect(collected_facts=collected_facts)
    assert 'lsb' in collected_facts

    # Test if collect method return info
    # of 'lsb' section of collected_facts
    c.collect(collected_facts=collected_facts)
    assert 'lsb' in collected_facts


# Generated at 2022-06-13 03:07:17.019514
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    test_obj = LSBFactCollector()
    assert test_obj

if __name__ == '__main__':
    test_LSBFactCollector()

# Generated at 2022-06-13 03:07:21.865511
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Initialize the object
    lsb_obj = LSBFactCollector()
    # Call the collect method
    result = lsb_obj.collect()
    # Assert result
    print("==============================")
    print("Test collect method of LSBFactCollector class")
    print("==============================")
    print("result of collect method is ")
    print(result)
    print("==============================")


# Generated at 2022-06-13 03:07:24.034568
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    collector = LSBFactCollector()
    assert collector.name == 'lsb'
    assert collector._fact_ids == set()
    assert collector.STRIP_QUOTES == r"'\"\\"

# Generated at 2022-06-13 03:07:28.254511
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'
    assert type(lsb_fact_collector._fact_ids) == set
    assert lsb_fact_collector.STRIP_QUOTES == r'\'\"\\'




# Generated at 2022-06-13 03:07:30.307450
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert isinstance(lsb, LSBFactCollector)


# Generated at 2022-06-13 03:07:38.932495
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    import ansible.module_utils.facts.collectors.lsb as lsb

    class TestModule(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, path):
            if path == 'lsb_release':
                return 'lsb_release'
            return ''

        def run_command(self, cmd, errors='surrogate_then_replace'):
            return (self.rc, self.out, self.err)

    LSBFactCollector._lsb_release_bin_is_installed = True
    lsb.os = MockOS(True)

    lsb_path = 'lsb_release'
    rc = 0
    out = ''
    err = ''



# Generated at 2022-06-13 03:07:41.728363
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts = LSBFactCollector()
    assert lsb_facts.collect() == {'lsb': {}}

# Generated at 2022-06-13 03:07:44.849853
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == "lsb"
    assert lsb._fact_ids == set()
    assert lsb.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:10:35.324169
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = MockModule()
    collector = LSBFactCollector()

    module.run_command.return_value = (0, 'Distributor ID: Ubuntu\nRelease:    18.04\nDescription:    Ubuntu 18.04.3 LTS\nCodename:   bionic', '')
    collector.collect(module=module)
    module.run_command.assert_called_with(['lsb_release', '-a'], errors='surrogate_then_replace')


# Generated at 2022-06-13 03:10:37.431819
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector
    assert lsb_fact_collector.name == 'lsb'

# Generated at 2022-06-13 03:10:43.236075
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_path = "lsb_release"
    etc_lsb_release_location = "etc/lsb-release"
    lsb_facts = {}
    lsb_facts = LSBFactCollector()._lsb_release_bin(lsb_path, lsb_facts)
    lsb_facts = LSBFactCollector()._lsb_release_file(etc_lsb_release_location, lsb_facts)
    assert lsb_facts

# Generated at 2022-06-13 03:10:51.434702
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.system.lsb import LSBFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    BaseFactCollector.deprecated_names = {
        'lsb': ['lsb'],
    }
    lsbobj = LSBFactCollector()
    lsbobj_results = {
        'lsb': {
            'id': 'ansible',
            'release': '1.0',
            'major_release': '1.0',
            'description': 'ansible',
            'codename': 'ansible'
        }
    }
    assert lsbobj_results == lsbobj.collect()


# Generated at 2022-06-13 03:11:00.981890
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Test with several LSB_RELEASE files
    test_lsb_release_paths = ['/etc/lsb-release', '/etc/lsb-release-test',
                              '/etc/lsb-release-test2']
    for location in test_lsb_release_paths:
        with open(location, 'w') as f:
            f.write('DISTRIB_ID=test_id\n')
            f.write('DISTRIB_RELEASE=test_release\n')
            f.write('DISTRIB_CODENAME=test_codename\n')
            f.write('DISTRIB_DESCRIPTION=test_description\n')


# Generated at 2022-06-13 03:11:02.637025
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:11:04.808861
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_obj = LSBFactCollector()
    assert lsb_obj.name == 'lsb'
    assert not lsb_obj._fact_ids

# Generated at 2022-06-13 03:11:12.396087
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.collectors.lsb import LSBFactCollector
    from ansible.module_utils.facts.utils import mock_module
    from ansible.module_utils.facts.utils import mock_run_command
    import os

    module_facts = {}
    module = mock_module(module_facts)
    module.run_command = mock_run_command([0, '', ''])

    os.environ['LANG'] = 'C'
    collector = LSBFactCollector()
    collector.collect(module=module)
    assert module_facts['lsb'] == {}
    del os.environ['LANG']

    module.run_command = mock_run_command([1, '', ''])
    collector = LSBFactCollector()
    collector.collect(module=module)


# Generated at 2022-06-13 03:11:13.699617
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    lsb_fact_collector.collect()

# Generated at 2022-06-13 03:11:14.711407
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'