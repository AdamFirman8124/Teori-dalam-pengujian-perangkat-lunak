

# Generated at 2022-06-13 03:01:55.148552
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lfc = LSBFactCollector()
    assert lfc.name == 'lsb'
    assert lfc.collect() == {}

# Generated at 2022-06-13 03:01:56.374037
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == 'lsb'

# Generated at 2022-06-13 03:01:58.809776
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()

    assert lsb_fact_collector is not None

# Unit test of _lsb_release_bin method of class LSBFactCollector

# Generated at 2022-06-13 03:02:05.164285
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # inputs and test setup
    LSB = LSBFactCollector()
    module = FakeModule()

    LSB_PATH = 'lsb_path'

    lsb_path_real = '/usr/bin/lsb_release'
    lsb_path_fake = '/bin/lsb_release_not_exist'
    lsb_path_fake2 = '/bin/lsb_release_not_exist2'
    lsb_release = """
    Distributor ID: Ubuntu
    Description:    Ubuntu 14.04.3 LTS
    Release:    14.04
    Codename:   trusty
    """


# Generated at 2022-06-13 03:02:18.085123
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # test that lsb data is gathered
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector

    test_data = [
        ('LSB Version: 1.2\n', ''),
        ('Distributor ID: Ubuntu\n', ''),
        ('Description: Ubuntu 10.04\n', ''),
        ('Release: 10.04\n', ''),
        ('Codename: lucid\n', ''),
    ]

    def test_bs_run_command(cmd, errors='surrogate_then_replace'):
        stdout = os.linesep.join([x[0] for x in test_data])
        stderr = os.linesep.join([x[1] for x in test_data])
        return (0, stdout, stderr)

# Generated at 2022-06-13 03:02:24.175594
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.utils import facts_to_dict
    from ansible.module_utils.facts.collectors import collector_module

    collected_facts = {}
    LSBFactCollector().collect(collector_module, collected_facts)

    assert 'lsb' in collected_facts

    lsb = collected_facts['lsb']

    assert lsb['id']
    assert lsb['release']

    if lsb['id'] == 'Debian':
        assert lsb['codename']


# Generated at 2022-06-13 03:02:26.185604
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'
    assert lsb.collect() is None

# Generated at 2022-06-13 03:02:27.252168
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    pass


# Generated at 2022-06-13 03:02:28.296358
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector

# Generated at 2022-06-13 03:02:33.249390
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()

    lsb_loader = LSBFactCollector()
    lsb_loader._lsb_release_bin('/usr/bin/lsb_release')
    lsb_loader._lsb_release_file('/etc/lsb-release')

# Generated at 2022-06-13 03:02:41.934109
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact = LSBFactCollector()

    assert lsb_fact.name == 'lsb'
    assert lsb_fact._fact_ids == set()
    assert lsb_fact.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:02:42.404993
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    pass

# Generated at 2022-06-13 03:02:46.826842
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector().name == 'lsb'
    assert not LSBFactCollector()._fact_ids
    assert LSBFactCollector.STRIP_QUOTES == r'\'\"\\'


# Generated at 2022-06-13 03:02:52.846182
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    import ansible.module_utils.facts.lsb as lsb

    module = FakeAnsibleModule(lsb=lsb)
    lsb = LSBFactCollector()
    results = lsb.collect(module=module, collected_facts=None)
    assert ('lsb' in results)
    assert ('id' in results['lsb'])
    assert ('release' in results['lsb'])
    assert ('description' in results['lsb'])
    assert ('codename' in results['lsb'])



# Generated at 2022-06-13 03:02:54.774114
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == 'lsb'
    assert x._fact_ids == set()
    assert x.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:03:05.358731
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_dict = {
        'release': '6.7',
        'id': 'RedHatEnterpriseWorkstation',
        'codename': 'OEL7',
        'description': 'Oracle Enterprise Linux Server release 7.7 (Oracle 7)',
    }
    lsb_fact_collector = LSBFactCollector()
    lsb_fact_collector.lsb_release_bin = lambda lsb_path, module: lsb_dict
    lsb_fact_collector.lsb_release_file = lambda etc_lsb_release_location: lsb_dict
    collected_facts = lsb_fact_collector.collect()

# Generated at 2022-06-13 03:03:12.631181
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module, klass = mock_module_and_collector()

    # Run the collect method with a mocked lsb_release binary
    collector = klass['lsb']
    collector.module = module
    lsb_bin = 'lsb_release'
    module.get_bin_path.return_value = lsb_bin
    stdout = '''
    Distributor ID:	Ubuntu
    Description:	Ubuntu 16.04.3 LTS
    Release:	16.04
    Codename:	xenial
    '''
    stderr = ''
    rc = 0
    module.run_command.return_value = (rc, stdout, stderr)
    facts = collector.collect()

    # Verify that the module.run_command was called as expected

# Generated at 2022-06-13 03:03:21.796852
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    '''
    Unit test for method collect of class LSBFactCollector

    The first test is with system information of a RedHat 7 Linux
    The second test is with system information of a SUSE Linux
    The third test is with system information of a Debian Linux
    '''

    # First test
    module = get_module_mock({'get_bin_path': lambda x: x})
    expected_lsb_facts_dict = {
        'id': 'RedHatEnterpriseServer',
        'release': '7.3',
        'codename': 'Maipo',
        'major_release': '7',
        'description': 'Red Hat Enterprise Linux Server release 7.3 (Maipo)'
    }

    lsbfact = LSBFactCollector()

# Generated at 2022-06-13 03:03:29.625368
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    ansible_facts = {}
    lsb_facts = {}
    lsb_facts['id'] = 'Ubuntu'
    lsb_facts['release'] = '14.04.3 LTS'
    lsb_facts['major_release'] = '14.04'
    lsb_facts['description'] = 'Ubuntu 14.04.3 LTS'
    lsb_facts['codename'] = 'trusty'

    assert LSBFactCollector().collect(module=None) == ansible_facts

    assert LSBFactCollector().collect(module='test')['lsb'] == lsb_facts

# Generated at 2022-06-13 03:03:39.856543
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_path = '/bin/lsb_release'
    mocked_module = MockModule({'bin_path': lsb_path})
    mocked_module.run_command = MagicMock(return_value=(0, '''
         LSB Version:\t1.0
         Distribution ID:\tneatOs
         Description:\tneatOs0 release 0.1 (NeatOS)
         Release:\t0.1
         Codename:\tNeatOS
    '''.lstrip(), ''))
    collector = LSBFactCollector({})
    facts_dict = collector.collect(module=mocked_module)

# Generated at 2022-06-13 03:04:01.371612
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    os_release_distribution = 'Debian'
    os_release_major_version = '8'

    os_release_path = '/etc/os-release'
    os_release_facts = {
        'DISTRIB_ID': 'Debian',
        'DISTRIB_RELEASE': '8.0',
        'DISTRIB_DESCRIPTION': 'Debian GNU/Linux 8.0 (jessie)',
    }

    ls_bin_path = '/usr/bin/ls'

# Generated at 2022-06-13 03:04:04.099070
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_obj = LSBFactCollector()
    expected_result = {'lsb': {}}
    assert (lsb_obj.collect() == expected_result)

# Generated at 2022-06-13 03:04:09.111826
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = MockModule()
    lsb_fact = LSBFactCollector()
    result = lsb_fact.collect(module=module)
    assert result == {'lsb': {'codename': 'test',
                              'description': 'test',
                              'id': 'test',
                              'major_release': 'test',
                              'release': 'test'}}


# Generated at 2022-06-13 03:04:19.737515
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    try:
        from ansible.module_utils.facts.collector.lsb import LSBFactCollector
    except ImportError:
        return {}

    # Testing the existence of lsb_release file
    lsb_facts = LSBFactCollector(None, None).collect()
    assert 'lsb' in lsb_facts
    assert 'release' in lsb_facts['lsb']
    assert 'major_release' in lsb_facts['lsb']
    assert 'id' in lsb_facts['lsb']
    assert 'description' in lsb_facts['lsb']
    assert 'codename' in lsb_facts['lsb']

# Generated at 2022-06-13 03:04:27.540010
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    # Test with an empty module_util, just to make sure that the _lsb_release_file() method is called
    test_collector = LSBFactCollector()
    test_collector.collect(None)
    test_collector.collect(None)

    # Test with a full module_util, just to make sure that the _lsb_release_bin() method is called
    test_collector = LSBFactCollector()
    full_module = type('module', (object,), dict(get_bin_path = lambda s, p: ''))()
    test_collector.collect(full_module)

# Generated at 2022-06-13 03:04:30.910450
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'
    assert lsb_fact_collector.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:04:38.058448
# Unit test for method collect of class LSBFactCollector

# Generated at 2022-06-13 03:04:39.942353
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    collector = LSBFactCollector()
    assert collector.name == "lsb"
    assert collector.name in collector._fact_ids

# Generated at 2022-06-13 03:04:45.616228
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts = LSBFactCollector().collect()
    assert 'lsb' in lsb_facts
    assert lsb_facts['lsb']
    assert 'id' in lsb_facts['lsb']
    assert 'release' in lsb_facts['lsb']
    assert 'codename' in lsb_facts['lsb']
    assert 'description' in lsb_facts['lsb']
    assert 'major_release' in lsb_facts['lsb']

# Generated at 2022-06-13 03:04:46.124328
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    pass

# Generated at 2022-06-13 03:05:10.317708
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    obj = LSBFactCollector()


# Generated at 2022-06-13 03:05:15.080676
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert lsb_collector
    assert lsb_collector.name == 'lsb'
    assert lsb_collector._fact_ids == set()



# Generated at 2022-06-13 03:05:16.649960
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_instance = LSBFactCollector()
    assert lsb_instance.name == 'lsb'

# Generated at 2022-06-13 03:05:19.953336
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    fact_collector = LSBFactCollector()
    facts = fact_collector.collect()

    assert facts['lsb']
    assert 'id' in facts['lsb']
    assert 'description' in facts['lsb']
    assert 'release' in facts['lsb']

# Generated at 2022-06-13 03:05:21.216797
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == 'lsb'
    assert 'lsb' in x._fact_ids

# Generated at 2022-06-13 03:05:29.729380
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name):
            return False

        def run_command(self, cmd, errors="surrogate_or_strict"):
            return 0, "", ""

    # Test when etc_lsb_release_location is None
    module = MockModule()
    lsb_fact_collector = LSBFactCollector()
    lsb_facts_dict = lsb_fact_collector.collect(module)
    assert not lsb_facts_dict

    # Test when get_bin_path is None

# Generated at 2022-06-13 03:05:35.893233
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    import sys
    from os.path import dirname, realpath

    sys.path.append(dirname(dirname(realpath(__file__))))

    from ansible.module_utils.facts.utils.fake import FakeModule

    fake_module = FakeModule()

    test_fact_collector = LSBFactCollector()

    # Run the method collect of LSBFactCollector
    actual_result = test_fact_collector.collect(fake_module)

    # Assert the result
    assert actual_result is not None

# Generated at 2022-06-13 03:05:43.053506
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    import pytest
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import CommandExecutionError
    from ansible.module_utils.facts.collector.lsb import LSBFactCollector

    with pytest.raises(TypeError):
        LSBFactCollector.collect(None)

    facts_collector = FactCollector()
    module = facts_collector.module
    fs = module._fs

    with pytest.raises(CommandExecutionError):
        LSBFactCollector.collect(module=module, collected_facts=None)

    fs.create_file('/bin/lsb_release', contents='#!/usr/bin/env python\n')
    fs.chmod('/bin/lsb_release', 0o755)


# Generated at 2022-06-13 03:05:47.227309
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts = LSBFactCollector().collect()
    assert 'id' in lsb_facts['lsb']
    assert 'release' in lsb_facts['lsb']
    assert 'description' in lsb_facts['lsb']
    assert 'codename' in lsb_facts['lsb']

# Generated at 2022-06-13 03:05:49.925273
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'
    assert LSBFactCollector.STRIP_QUOTES == '\'\"\\'

# Generated at 2022-06-13 03:06:49.392611
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:07:00.031326
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
  fc = LSBFactCollector()
  assert fc.name == 'lsb'
  assert fc._fact_ids == set()
  assert fc.STRIP_QUOTES == r'\'\"\\'


# Generated at 2022-06-13 03:07:01.834204
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb is not None


# Generated at 2022-06-13 03:07:03.466263
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_str = LSBFactCollector()
    assert lsb_str.name == 'lsb'

# Generated at 2022-06-13 03:07:21.202213
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Test empty case, when path to lsb_release is None
    assert LSBFactCollector().collect() == {'lsb': {}}

    # Test LSB info collection with path to lsb_release
    class Module(object):
        def get_bin_path(self, unneeded_param):
            return 'path'

        def run_command(self, argv, errors):
            if argv == ['path', '-a']:
                return 0, "", ""
            else:
                return 1, "", ""

    assert LSBFactCollector().collect(module=Module()) == {'lsb': {}}

    # Test LSB info collection with path to /etc/lsb-release
    class FileModule(object):
        def get_bin_path(self, unneeded_param):
            return None

    assert L

# Generated at 2022-06-13 03:07:29.186102
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    import mock
    from ansible.module_utils import basic

    module = mock.Mock()
    module.get_bin_path.return_value = '/path/to/lsb_release'
    module.run_command.return_value = (
        0,
        '''
        LSB Version:    :core-4.1-amd64:core-4.1-noarch
        :
        Distributor ID: Fedora
        Description:    Fedora release 25 (Twenty Five)
        Release:        25
        Codename:       TwentyFive
        ''',
        ''
    )
    collected_facts = {}
    LSBFactCollector().collect(module, collected_facts)

# Generated at 2022-06-13 03:07:32.595403
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    """This is a test of the LSBFactCollector constructor"""
    l = LSBFactCollector()
    assert l.name == "lsb"
    assert l._fact_ids == set()
    assert l.STRIP_QUOTES == r'\'\"\\'


# Generated at 2022-06-13 03:07:37.698056
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert lsb_collector.name == 'lsb'
    assert type(lsb_collector._fact_ids) is set
    assert len(lsb_collector._fact_ids) == 0
    assert lsb_collector.STRIP_QUOTES == r'\'\"\\'

# Unit tests for lsb_release_bin

# Generated at 2022-06-13 03:07:38.895132
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb is not None


# Generated at 2022-06-13 03:07:43.348160
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name is 'lsb'
    assert lsb._fact_ids is not None
    assert lsb.STRIP_QUOTES is not None

# Generated at 2022-06-13 03:10:20.767726
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    # mock the module object
    class AnsibleModuleMock():
        def __init__(self):
            self.params = {}
            self.run_command_environ_update = {}

        def get_bin_path(self, program):
            return None


# Generated at 2022-06-13 03:10:22.303696
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector().name == 'lsb'

# Generated at 2022-06-13 03:10:28.612178
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    import sys
    import tempfile
    import ansible.module_utils.basic

    result = {}
    result['ansible_facts'] = {}
    test_content = """DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=14.04
DISTRIB_CODENAME=trusty
DISTRIB_DESCRIPTION="Ubuntu 14.04.3 LTS"
"""
    test_content_lsb_release = """Description:    Ubuntu 14.04.3 LTS
Release:        14.04
Codename:       trusty
"""
    test_module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )
    # We write lsb_release to a temp

# Generated at 2022-06-13 03:10:30.994596
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == "lsb"
    assert LSBFactCollector._fact_ids == set()
    assert LSBFactCollector.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:10:32.938437
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'
    assert LSBFactCollector().name == 'lsb'
    assert LSBFactCollector.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:10:36.343207
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.utils import gather_subset

    fact_collector = FactsCollector()

    # Test with only module and no parameter
    LSBFactCollector(fact_collector)

    # Test with module and subset
    subset = ["lsb"]
    gather_subset(fact_collector, subset, module=dict())


# Generated at 2022-06-13 03:10:37.468808
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == 'lsb'

# Generated at 2022-06-13 03:10:39.712702
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert isinstance(lsb_fact_collector, LSBFactCollector)

# Generated at 2022-06-13 03:10:45.505915
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.collectors import collector_exception
    from ansible.module_utils.facts.collectors.lsb import LSBFactCollector
    from ansible.module_utils.facts.utils import MockModule

    class MockModule:
        def run_command(self, parameters=[], errors='surrogate_then_replace'):
            return (0, """
LSB Version:    :core-4.1-amd64:core-4.1-noarch
Distributor ID: RedHatEnterpriseServer
Description:    Red Hat Enterprise Linux Server release 7.0 (Maipo)
Release:        7.0
Codename:       Maipo
""", '')

    def get_bin_path(self, executable):
        return '/usr/bin/lsb_release'

    module = MockModule()

# Generated at 2022-06-13 03:10:53.213448
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts = {
        "id": "Ubuntu",
        "description": "Ubuntu 15.04",
        "release": "15.04",
        "codename": "vivid",
        "major_release": "15"
    }
    module = MockModule()
    module.get_bin_path.return_value = 'temp_lsb_release_bin'
    module.run_command.return_value = (0, 'a\nLSB Version:    :temp_lsb_version\nDistributor ID: temp_distributor_id\nDescription:    temp_description\nRelease:    temp_release\nCodename:    temp_codename\n', '')
    os.path.exists.return_value = False
    lsb_collector = LSBFactCollector()