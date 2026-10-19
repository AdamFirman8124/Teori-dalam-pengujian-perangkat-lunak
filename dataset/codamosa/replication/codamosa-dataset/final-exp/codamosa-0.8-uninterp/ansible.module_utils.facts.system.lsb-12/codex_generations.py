

# Generated at 2022-06-13 03:02:05.021658
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.system.lsb import LSBFactCollector
    from ansible.module_utils.facts.utils import mock
    import ansible_collections.ansible.os_family.os_debian
    import ansible_collections.ansible.os_family.os_redhat

    import pytest

    module = mock.MagicMock()
    lsb_facts_collector = pytest.importorskip("ansible_collections.ansible.os_family.os_debian.plugins.module_utils.facts.system.lsb")
    lsb_facts_collector = pytest.importorskip("ansible_collections.ansible.os_family.os_redhat.plugins.module_utils.facts.system.lsb")


# Generated at 2022-06-13 03:02:17.938266
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Test when lsb_release file not available
    lsb_fact_collector = LSBFactCollector(None)
    result = lsb_fact_collector.collect()
    assert result['lsb'] == {}

    # Test when lsb_release is available and lsb_release file is not
    result = lsb_fact_collector.collect(module=get_mocked_module())
    assert result['lsb'] == {
        'release': '7.1',
        'codename': 'wheezy',
        'description': 'Debian GNU/Linux 7.1 (wheezy)',
        'id': 'Debian'
    }

    # Test when lsb_release is available and lsb_release file is also available

# Generated at 2022-06-13 03:02:18.951457
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:02:24.954020
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_dict = {'codename': 'Bionic Beaver', 'description': 'Ubuntu 18.04.1 LTS', 'distributor_id': 'Debian',
                'lsb_release': '/usr/bin/lsb_release', 'major_release': '18.04', 'release': '18.04.1 LTS (Bionic Beaver)',
                'id': 'Ubuntu'}
    lsb_dict_1 = {}
    test1 = LSBFactCollector(True, lsb_dict_1)
    assert test1.collect() == lsb_dict

# Generated at 2022-06-13 03:02:32.020919
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_command_output = """
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.1 LTS
Release:        18.04
Codename:       bionic
    """
    lsb_file_output = """
DISTRIB_ID="Ubuntu"
DISTRIB_RELEASE="18.04"
DISTRIB_DESCRIPTION="Ubuntu 18.04.1 LTS"
DISTRIB_CODENAME="bionic"
    """

# Generated at 2022-06-13 03:02:33.059955
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:02:34.744458
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_collector = LSBFactCollector()
    assert isinstance(lsb_collector.collect(), dict)

# Generated at 2022-06-13 03:02:37.494565
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:02:38.049817
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    pass

# Generated at 2022-06-13 03:02:40.630636
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'
    assert LSBFactCollector.STRIP_QUOTES == '\'\"\\'


# Generated at 2022-06-13 03:02:49.612458
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert hasattr(LSBFactCollector, "name")
    assert hasattr(LSBFactCollector, "_fact_ids")
    assert hasattr(LSBFactCollector, "STRIP_QUOTES")

# Generated at 2022-06-13 03:02:51.028291
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    fact_collector = LSBFactCollector()
    assert fact_collector.name == 'lsb'

# Generated at 2022-06-13 03:02:56.783285
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    '''
    Unit test for method collect of class LSBFactCollector
    '''
    lsb_fact_collector = LSBFactCollector()
    lsb = {'release': '7.1',
           'major_release': '7',
           'id': 'CentOS',
           'description': 'CentOS Linux release 7.1.1503 (Core)',
           'codename': 'Core'}
    assert lsb_fact_collector.collect(collected_facts={}).get('lsb') == lsb

# Generated at 2022-06-13 03:03:06.289543
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.lsb import LSBFactCollector
    from ansible.modules.system.setup import get_bin_path

    bin_path = get_bin_path('lsb_release')
    if not bin_path:
        return

    facts_dict = collector.collect(None, LSBFactCollector)

    assert facts_dict['lsb'] == {'description': 'Debian GNU/Linux 10 (buster)',
                                 'id': 'Debian',
                                 'release': '10',
                                 'codename': 'buster',
                                 'major_release': '10'}

# Generated at 2022-06-13 03:03:07.255450
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert lsb_collector.name == "lsb"
    assert lsb_collector._fact_ids == set()

# Generated at 2022-06-13 03:03:13.762240
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    ansible_module = AnsibleModule(argument_spec={})
    #
    # mock_module:
    #
    def mock_run_command(args, errors='surrogate_then_replace'):
        if '/bin/lsb_release' in args:
            if args[1] == '-a':
                return 0, get_file_content(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                             'output/lsb_release_a')), ''

# Generated at 2022-06-13 03:03:18.073645
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_obj = LSBFactCollector()
    assert lsb_obj.name == 'lsb'
    assert lsb_obj._fact_ids == set()
    assert lsb_obj.STRIP_QUOTES == r'\'\"\\'

# Load the module and test it

# Generated at 2022-06-13 03:03:21.179972
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact = LSBFactCollector()

    assert lsb_fact.name == 'lsb'
    assert isinstance(lsb_fact._fact_ids, set)
    assert lsb_fact.STRIP_QUOTES == '\'\"\\'

# Generated at 2022-06-13 03:03:26.911366
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    from ansible.module_utils.facts import Facts

    module = None
    collected_facts = {'ansible_lsb': None}
    target_collector = LSBFactCollector()
    target_collector.collect(module=module, collected_facts=collected_facts)

    assert 'lsb' in collected_facts
    assert collected_facts['lsb'] is not None


# Generated at 2022-06-13 03:03:35.716528
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    import ansible.module_utils
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.lsb
    import ansible.module_utils.facts.system.base

    # Test with lsb_release binary

    lsb_path = ansible.module_utils.which('lsb_release')
    if lsb_path:

        lsb_output = """
      Distributor ID:	Ubuntu
      Description:	Ubuntu 18.04.1 LTS
      Release:	18.04
      Codename:	bionic
      """

        class MockModule():
            def __init__(self):
                self.fail_json = ansible.module_utils.facts.collector.fail_json

# Generated at 2022-06-13 03:03:53.893194
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    import pytest
    from ansible.module_utils.facts.collector import collector_registry
    fact_collector = LSBFactCollector()
    assert fact_collector.name == 'lsb'
    assert fact_collector._fact_ids == set()
    assert collector_registry['lsb'] is LSBFactCollector

# Generated at 2022-06-13 03:03:57.147728
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'
    assert lsb_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:04:07.843719
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    class TestModule():
        def get_bin_path(self, arg):
            if arg == 'lsb_release':
                return '/usr/bin/lsb_release'
            return None

        def run_command(self, args, errors):
            if args:
                if args[0] == '/usr/bin/lsb_release':
                    return 0, '''
LSB Version:    :core-3.1-amd64:core-3.1-noarch
Distributor ID: CentOS
Description:    CentOS Linux release 8.2.2004 (Core)
Release:        8.2.2004
Codename:       Core
''', ''
                else:
                    return 1, '', ''
            else:
                return 1, '', ''

    lsb_fact_collector = LSBFactCollector()

    local_ls

# Generated at 2022-06-13 03:04:14.547956
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    test_module = type('test module', (object,), {
            'run_command': run_command_mock
        })
    test_module_instance = test_module()
    test_module_instance.get_bin_path = lambda x: '/bin/lsb_release'
    test_facts_dict = {'lsb': {'release': '12.04', 'description': 'Ubuntu 12.04.5 LTS', 'id': 'Ubuntu', 'major_release': '12', 'codename': 'precise'}}
    test_LSBFactCollector = LSBFactCollector()
    collected_facts = test_LSBFactCollector.collect(module=test_module_instance)
    assert(collected_facts == test_facts_dict)


# Generated at 2022-06-13 03:04:19.687156
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_path = 'fake_lsb_path'
    lsb_facts = { 'id': 'id', 'release': 'release', 'description': 'description' }
    args = [lsb_path, '-a']
    run_command_args = {'args': args}
    mock_module = MagicMock()
    mock_module.run_command.return_value = (0, 'output', '')
    mock_module.get_bin_path.return_value = lsb_path

    lsb_fact_collector = LSBFactCollector()

    assert lsb_fact_collector._lsb_release_file('/etc/lsb-release') == {}
    assert lsb_fact_collector._lsb_release_bin(lsb_path, mock_module) == lsb_facts
   

# Generated at 2022-06-13 03:04:20.152397
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()


# Generated at 2022-06-13 03:04:22.076645
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    obj = LSBFactCollector()
    assert obj.name == 'lsb'
    assert obj._fact_ids == set()


# Generated at 2022-06-13 03:04:23.575700
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert lsb_collector.name == 'lsb'

# Generated at 2022-06-13 03:04:24.745427
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert 'lsb' == lsb.name

# Generated at 2022-06-13 03:04:30.910625
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    """ Test class constructors and methods with a variety of inputs
    """

    # Test with a module
    module = AnsibleModule(argument_spec={})
    lsb = LSBFactCollector(module)

    # Test with a collected_facts
    collected_facts = dict()
    lsb = LSBFactCollector(collected_facts=collected_facts)



# Generated at 2022-06-13 03:04:57.365594
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    collecter = LSBFactCollector()

# Generated at 2022-06-13 03:04:59.735321
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    c = LSBFactCollector()
    assert c.name == 'lsb'
    assert c._fact_ids == set()
    assert c.STRIP_QUOTES == '\'\"\\'

# Generated at 2022-06-13 03:05:08.932737
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    """
    Method 'collect' test.
    """
    # testing standard run case
    module = MockModule()
    lsbfc = LSBFactCollector()
    lsb_facts = {
            'id':'test1',
            'release':'test2',
            'description':'test3',
            'codename':'test4',
            'major_release':'test2',
            }
    lsbfc.collect(module=module)
    assert lsbfc.name == 'lsb'
    assert lsbfc.lsb_path == '/path/to/lsb_release'
    assert lsbfc.etc_lsb_release_location == '/etc/lsb-release'
    assert lsbfc.lsb_facts == lsb_facts

    # testing when 'lsb_release' is not present

# Generated at 2022-06-13 03:05:10.353126
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    test = LSBFactCollector()
    assert test
    assert test.name == 'lsb'


# Generated at 2022-06-13 03:05:20.852994
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    import os
    import tempfile
    import shutil

    # Make a temporary work directory
    test_dir = tempfile.mkdtemp(dir=".")
    test_lsb_release_file = os.path.join(test_dir, 'lsb-release')

    test_lsb_release_content = '''
DISTRIB_ID=Debian
DISTRIB_RELEASE=7.1
DISTRIB_DESCRIPTION="Debian GNU/Linux 7.1 (wheezy) \\"with Backports\\""
DISTRIB_CODENAME=wheezy
'''
    # Test with lsb_release file only
    lsb_facts = None

    with open(test_lsb_release_file, 'w') as f:
        f.write(test_lsb_release_content)


# Generated at 2022-06-13 03:05:25.423603
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = None
    lsb_facts = LSBFactCollector().collect(module=module)
    assert lsb_facts['lsb']['major_release'] == '8'
    assert lsb_facts['lsb']['description'] == 'Debian GNU/Linux 9.7 (stretch)'
    assert lsb_facts['lsb']['release'] == '9.7'
    assert lsb_facts['lsb']['id'] == 'Debian'
    assert lsb_facts['lsb']['codename'] == 'stretch'

# Generated at 2022-06-13 03:05:27.619158
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    collector = LSBFactCollector()
    assert collector.name == 'lsb'
    assert len(collector._fact_ids) == 0


# Generated at 2022-06-13 03:05:30.463540
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'
    assert lsb_fact_collector._fact_ids == set()
    assert lsb_fact_collector.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:05:39.406907
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Mock module and class LSBFactCollector
    mock_module = MagicMock()
    mock_module.get_bin_path.return_value = '/bin/lsb_release'
    mock_module.run_command.return_value = 0, '', ''
    mock_input_lines = [
        'LSB Version: 1.2',
        'Distributor ID: RedHat',
        'Description: RedHat description',
        'Release: 7.2',
        'Codename: RedHat-7.2',
    ]
    mock_open = mock_open()
    mock_open.return_value = mock_input_lines
    with patch('ansible.module_utils.facts.collector.open', mock_open, create=True):
        collector = LSBFactCollector()

# Generated at 2022-06-13 03:05:41.856164
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert lsb_collector
    assert lsb_collector.name == 'lsb'
    assert lsb_collector._fact_ids == set()


# Generated at 2022-06-13 03:06:47.310434
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert hasattr(LSBFactCollector, "collect")
    assert hasattr(LSBFactCollector, "_fact_ids")
    assert hasattr(LSBFactCollector, "name")
    assert hasattr(LSBFactCollector, "_lsb_release_bin")
    assert hasattr(LSBFactCollector, "_lsb_release_file")
    assert hasattr(LSBFactCollector, "STRIP_QUOTES")
    assert len(LSBFactCollector._fact_ids) == 0
    assert LSBFactCollector.name == "lsb"

# Generated at 2022-06-13 03:06:54.072729
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    '''
    Test running the LSBFactCollector.collect() method.
    '''

    # Check returns empty lsb_facts if no module object provided
    lsb_facts = LSBFactCollector().collect()
    assert lsb_facts == {}, 'lsb_facts should be empty, instead found {}'.format(lsb_facts)

    # Check returns empty lsb_facts if module does not have get_bin_path
    lsb_facts = LSBFactCollector().collect(MockModule())
    assert lsb_facts == {}, 'lsb_facts should be empty, instead found {}'.format(lsb_facts)

    # Check returns empty lsb_facts if module.get_bin_path returns None
    module = MockModule(bin_path=None)

# Generated at 2022-06-13 03:06:55.614029
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = AnsibleModule({})
    lsb = LSBFactCollector()
    result = lsb.collect(module)

    assert result is not None

# Generated at 2022-06-13 03:07:00.103595
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    # Load lsb collector instance
    lsb_col = LSBFactCollector()

    assert lsb_col.name == 'lsb'
    assert lsb_col.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:07:04.260645
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsbF = LSBFactCollector()
    assert lsbF.name == "lsb"
    assert lsbF._fact_ids == set()
    assert lsbF.STRIP_QUOTES == r'\'\"\\'

# Unit Test for method _lsb_release_bin of class LSBFactCollector

# Generated at 2022-06-13 03:07:06.538303
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    p = LSBFactCollector()
    assert p.name == 'lsb'
    assert not p._fact_ids
    assert p.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:07:08.528801
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    collector = LSBFactCollector()
    assert collector.name == "lsb"
    assert collector._fact_ids == set()

# Generated at 2022-06-13 03:07:09.289052
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:07:15.029986
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_def = dict(
        id=None,
        description=None,
        release=None,
        codename=None,
        major_release=None
    )

    lsb_release_bin = "ID=\ndescription='blah blah blah'\nrelease='16.04'\nCodename=Xenial"
    lsb_release_file = "DISTRIB_ID='Ubuntu'\nDISTRIB_RELEASE='16.04'\nDISTRIB_CODENAME='Xenial'\nDISTRIB_DESCRIPTION='blah blah blah'"

    lsb_bin = dict(
        id='ID',
        description='blah blah blah',
        release='16.04',
        codename='Xenial',
        major_release='16'
    )

    lsb_

# Generated at 2022-06-13 03:07:23.279522
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    '''Test method LSBFactCollector.collect()'''

    #
    # Setup
    #

    import ansible.module_utils.facts.collector


    ansible.module_utils.facts.collector.BaseFactCollector = FakeBaseFactCollector

    from ansible.module_utils.facts.collector.lsb import LSBFactCollector

    test_obj = LSBFactCollector()
    test_obj.__class__.STRIP_QUOTES = ''

    #
    # Experiment
    #

    lsb_facts = test_obj.collect({})

    #
    # Assertions
    #


# Generated at 2022-06-13 03:09:59.536264
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb is not None

# Generated at 2022-06-13 03:10:01.654517
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    def null_function():
        pass

    assert isinstance(LSBFactCollector(null_function), BaseFactCollector)

# Generated at 2022-06-13 03:10:03.134523
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    collector = LSBFactCollector()

# Generated at 2022-06-13 03:10:12.178856
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts = {'release': '13.1', 'id': 'openSUSE', 'description': 'openSUSE 13.1 (Bottle) (x86_64)', 'codename': 'Bottle'}
    lsb_bin = '/usr/bin/lsb_release'
    lsb_argv = [lsb_bin, "-a"]
    module = FakeAnsibleModule()
    lsb_release = LSBFactCollector()
    with mock.patch.object(LSBFactCollector, '_lsb_release_bin') as lsb_release_bin:
        lsb_release_bin.return_value = lsb_facts
        with mock.patch.object(LSBFactCollector, '_lsb_release_file') as lsb_release_file:
            lsb_release_file

# Generated at 2022-06-13 03:10:14.099720
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_facts = LSBFactCollector()
    assert lsb_facts.name == "lsb"

# Generated at 2022-06-13 03:10:21.184756
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'

    # Set up a test class
    class MockModule(object):
        def __init__(self):
            self.params = {
                'lsb_path': '/bin/lsb_release'
            }

        def get_bin_path(self, executable):
            return self.params.get('lsb_path')

        def run_command(self, command, errors='surrogate_then_replace'):
            assert command[0] == self.params.get('lsb_path'), 'lsb_release executable should be lsb_path'

            if self.params.get('lsb_path') == '/bin/lsb_release':
                stdout = "LSB Version:\tv1.1\nDistributor ID: Ubuntu"
                stderr = ''

# Generated at 2022-06-13 03:10:22.064725
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    pass

# Generated at 2022-06-13 03:10:28.374787
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    if os.path.exists('/usr/bin/lsb_release'):
        lsb_path = os.path.realpath('/usr/bin/lsb_release')
    else:
        lsb_path = None

    from ansible.module_utils.facts.collector import LSBFactCollector
    from ansible.module_utils.facts import FactsModule
    from ansible.module_utils.facts.utils import FactsCollector

    facts_collector = FactsCollector()
    facts_dict = facts_collector.collect(module=FactsModule(), collected_facts=dict())
    assert facts_dict['lsb']['major_release'] == '8'
    assert facts_dict['lsb']['codename'] == 'jessie'

    # test with lsb_release missing

# Generated at 2022-06-13 03:10:35.374452
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    #####
    # This entire test is dependent on python2.
    # Python 3 breaks ansible with the following error:
    #
    #   TypeError: decoding to str: need a bytes-like object,
    #               NoneType found
    #
    # Therefore, this test cannot be run on python 3.
    #####

    # Test on POSIX system
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collectors.lsb import LSBFactCollector

    collectible_facts = {}
    module = MockModule()

    # On POSIX system, lsb_release is expected to be installed
    # and return the expected result

# Generated at 2022-06-13 03:10:43.077767
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_fact_collector = LSBFactCollector()
    lsb_fact_collector._lsb_release_bin = lambda lsb_path, module: {
        'id': 'Debian',
        'description': 'Debian GNU/Linux 9.4 (stretch)',
        'release': '9.4',
        'codename': 'stretch'
    }

    collected_facts = {}
    lsb_facts = lsb_fact_collector.collect(collected_facts)
    assert lsb_facts['lsb']['id'] == 'Debian'
    assert lsb_facts['lsb']['description'] == 'Debian GNU/Linux 9.4 (stretch)'
    assert lsb_facts['lsb']['release'] == '9.4'