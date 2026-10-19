

# Generated at 2022-06-13 03:01:57.081880
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsbinfo = LSBFactCollector()
    lsbinfo.collect()

# Generated at 2022-06-13 03:02:08.520042
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    lsb_path = '/usr/bin/lsb_release'
    etc_lsb_release_location = '/etc/os-release'
    test_fact = LSBFactCollector()
    class ModuleData:
        def __init__(self):
            self.module_name = 'FacterUtilsTest'
            self.params = dict()
            self.params['gather_subset'] = ['all']

        def setup(self):
            self.setup_return = 'setup_return'

        def get_bin_path(self, bin_name):
            if bin_name == 'lsb_release':
                return lsb_path
            else:
                return None


# Generated at 2022-06-13 03:02:11.618352
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    """Test case for constructor of class LSBFactCollector"""
    collector = LSBFactCollector()
    assert 'lsb' == collector.name

# Generated at 2022-06-13 03:02:22.591237
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    #
    # Force the _lsb_release_file method to return the specified dict
    #
    def _lsb_release_file(etc_lsb_release_location):
        lsb_facts = {}
        lsb_facts['id'] = 'test_id'
        lsb_facts['release'] = 'test_release'
        lsb_facts['description'] = 'test_description'
        lsb_facts['codename'] = 'test_codename'
        return lsb_facts

    #
    # Force the _lsb_release_bin method to return the specified dict
    #
    def _lsb_release_bin(lsb_path):
        lsb_facts = {}
        lsb_facts['id'] = 'test_id'
        lsb_facts['release'] = 'test_release'


# Generated at 2022-06-13 03:02:26.184374
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == 'lsb'
    assert x.STRIP_QUOTES == '\'\"\\'
    assert x._fact_ids == set()

# Generated at 2022-06-13 03:02:37.019840
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    test_lsb_release = """\
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=14.04
DISTRIB_CODENAME=trusty
DISTRIB_DESCRIPTION="Ubuntu 14.04.4 LTS"
""".encode()
    test_lsb_release_bin = """\
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04.4 LTS
Release:	14.04
Codename:	trusty
""".encode()

    class TestModule(object):
        def __init__(self, lsb_path):
            self.lsb_path = lsb_path

        def get_bin_path(self, prog):
            return self.lsb_path


# Generated at 2022-06-13 03:02:47.627902
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    s = LSBFactCollector()
    assert s.collect({'path': {'bin': ['/bin']},
                      'run_command':
                      lambda x, errors: (0, '', '')}) == {'lsb': {}}

    assert s.collect({'path': {'bin': ['/bin']},
                      'run_command':
                      lambda x, errors: (1, '', '')}) == {'lsb': {}}

    assert s.collect({'path': {'bin': ['/bin']},
                      'run_command':
                      lambda x, errors: (0, '', '')}) == {'lsb': {}}


# Generated at 2022-06-13 03:02:48.427897
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:02:51.172457
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'
    assert lsb._fact_ids == set()
    assert lsb.STRIP_QUOTES == r'\'\"\\'


# Generated at 2022-06-13 03:02:52.219081
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact = LSBFactCollector()
    assert lsb_fact


# Generated at 2022-06-13 03:03:08.881743
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    test_lsb_facts = {
        'codename': 'xenial',
        'description': 'Ubuntu 16.04.2 LTS',
        'distributor_id': 'Ubuntu',
        'major_release': '16',
        'release': '16.04',
        'id': 'Ubuntu',
    }

    # test with lsb script
    base_lsb_path = '/usr/bin/lsb_release'

    # test with lsb file
    base_lsb_file_path = '/etc/lsb-release'


# Generated at 2022-06-13 03:03:09.891407
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:03:10.499712
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    pass

# Generated at 2022-06-13 03:03:15.807479
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    """
    Unit test for the LSBFactCollector class. This is essentially
    a sanity test and should be expanded in the future.
    """
    lsb_collector = LSBFactCollector()
    assert lsb_collector.name == 'lsb'
    assert lsb_collector._fact_ids == set()
    assert lsb_collector.STRIP_QUOTES == '\'\"\\'

# Generated at 2022-06-13 03:03:17.694911
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'


# Generated at 2022-06-13 03:03:23.572078
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec = dict()
    )
    module.run_command = lambda *args: (0, '', '')
    lsb_facts = LSBFactCollector().collect(module=module)['lsb']
    assert lsb_facts['major_release'] == '7'

    module.run_command = lambda *args, **kwargs: (1, '', '')
    lsb_facts = LSBFactCollector().collect(module=module)['lsb']
    assert 'major_release' not in lsb_facts


# Generated at 2022-06-13 03:03:27.805935
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'
    assert lsb_fact_collector._fact_ids == set()
    assert lsb_fact_collector.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:03:29.678305
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    collector = LSBFactCollector()
    assert collector.name == 'lsb'

    assert LSBFactCollector._fact_ids == set()

# Generated at 2022-06-13 03:03:37.636411
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # no params
    collector = LSBFactCollector()

    # no lsb_command
    lsb_facts = collector._lsb_release_bin(None, None)
    assert lsb_facts == {}

    # no /etc/lsb-release
    lsb_facts = collector._lsb_release_file('/etc/non/exist/file')
    assert lsb_facts == {}

    # no lsb_command, no /etc/lsb-release
    lsb_facts = collector.collect()
    assert lsb_facts == {}


# Generated at 2022-06-13 03:03:40.466096
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'
    assert len(lsb_fact_collector._fact_ids) == 0


# Generated at 2022-06-13 03:03:55.925185
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_facts = LSBFactCollector()
    assert lsb_facts

# Generated at 2022-06-13 03:04:06.320368
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # mock module
    module = MagicMock()
    module.get_bin_path = Mock()
    module.run_command = Mock()
    m = module.run_command.return_value = (0, '', '')

    m.splitlines.return_value = ["a", "", "b"]

    # mock facts
    collected_facts = MagicMock()
    collected_facts.get = Mock()

    # Collect LSB facts into facts dictionary
    lsb_fact_collector = LSBFactCollector()
    facts_dict = lsb_fact_collector.collect(module=module, collected_facts=collected_facts)
    assert "lsb" in facts_dict
    assert sorted(facts_dict["lsb"]) == sorted(["b"])


# Generated at 2022-06-13 03:04:13.906915
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    # Create an instance of AnsibleModule
    from ansible.module_utils.facts import ModuleFacts
    module = ModuleFacts()

    # Define the path where the file lsb-release is located
    etc_lsb_release_location = "./etc_lsb_release"

    # Define the content of the file lsb-release
    etc_lsb_release_content = """
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.1 LTS"
"""

    # Create and fill the file lsb-release
    with open(etc_lsb_release_location, "w") as f:
        f.write(etc_lsb_release_content)
        f.close

# Generated at 2022-06-13 03:04:22.986196
# Unit test for method collect of class LSBFactCollector

# Generated at 2022-06-13 03:04:33.619199
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    import os
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import DictMerge
    from ansible.module_utils.facts.collector import FactCollector

    # create a host
    found_host = FakeHost()

    # create a module
    module_mock = FakeAnsibleModule(host=found_host)

    # create LSBFactCollector
    tmp_LSBFactCollector = LSBFactCollector()

    # create FactCollector
    tmp_fact_collector = FactCollector(module=module_mock,
                                       host=found_host,
                                       fact_collectors=[tmp_LSBFactCollector],
                                       )

    # call collect
    fact_dict = tmp_fact_collector.collect

# Generated at 2022-06-13 03:04:36.379137
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fc = LSBFactCollector()
    assert lsb_fc.name == 'lsb'
    assert lsb_fc.STRIP_QUOTES == '\'\"\\'
    assert lsb_fc._fact_ids == set()

# Generated at 2022-06-13 03:04:45.509334
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_collector = LSBFactCollector()
    # Test with 'lsb_release' binary on path
    m = MagicMock()
    mock_out = """LSB Version:    :base-4.0-amd64:base-4.0-noarch:core-4.0-amd64:core-4.0-noarch:graphics-4.0-amd64:graphics-4.0-noarch:printing-4.0-amd64:printing-4.0-noarch
Distributor ID: Fedora
Description:    Fedora release 19 (Schr\xF6dinger's Cat)
Release:        19
Codename:       Schrodinger"""
    m.run_command.return_value = (0, mock_out, None)
    lsb_facts = lsb_collector._lsb

# Generated at 2022-06-13 03:04:46.631735
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'

# Generated at 2022-06-13 03:04:47.653033
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    obj = LSBFactCollector()
    assert obj.name == 'lsb'

# Generated at 2022-06-13 03:04:53.061792
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Given
    test_collector = LSBFactCollector()
    test_data = {'DISTRIB_ID': "Ubuntu", 'DISTRIB_RELEASE': "16.04",
                 'DISTRIB_DESCRIPTION': "Ubuntu 16.04.3 LTS",
                 'DISTRIB_CODENAME': "xenial",
                 'LSB_VERSION': "1.4"}
    # When
    result = test_collector._lsb_release_file(test_data)
    # Then
    assert result == {'id': "Ubuntu", 'release': "16.04",
                      'description': "Ubuntu 16.04.3 LTS",
                      'codename': "xenial"}

# Generated at 2022-06-13 03:05:30.762055
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Create a Mock to replace the AnsibleModule class
    class AnsibleModuleMock(object):
        def __init__(self, module_name, **kwargs):
            # Fill in what we need for the facts module
            self.params = kwargs
            self.params['gather_subset'] = list()

        def get_bin_path(self, bin_name):
            return '/usr/bin/lsb_release'

        def run_command(self, *args, **kwargs):
            return 0, "", ""

    # Create an instance of the Mock
    ansible_module_mock = AnsibleModuleMock('AnsibleModuleMock')

    # Create an instance of LSBFactCollector and test
    lsb_fact_collector = LSBFactCollector()
    lsb_facts = lsb

# Generated at 2022-06-13 03:05:33.046397
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'
    assert LSBFactCollector._fact_ids == set()


# Generated at 2022-06-13 03:05:38.133696
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # having lsb_release will gather information from lsb_release
    module_mock = MockModule({'get_bin_path.return_value': '/usr/bin/lsb_release'})
    module_mock.run_command.return_value = (0,
            "Distributor ID:\tVendorOS\nDescription:\tVendor OS\nRelease:\t5.5\nCodename:\tVendorOS55\n", "")
    info_gathered = LSBFactCollector().collect(module_mock)
    assert info_gathered['lsb'] == {'id': 'VendorOS', 'release': '5.5',
    'description': 'Vendor OS', 'codename': 'VendorOS55', 'major_release': '5'}
    # no lsb_release, but /etc/

# Generated at 2022-06-13 03:05:43.669169
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts = {}
    lsb_facts['id'] = "CentOS"
    lsb_facts['release'] = "7.1.1503"
    lsb_facts['description'] = "CentOS Linux release 7.1.1503 (Core)"
    lsb_facts['codename'] = "Core"

    for k, v in lsb_facts.items():
        try:
            if v:
                lsb_facts[k] = v.strip(LSBFactCollector.STRIP_QUOTES)
        except AttributeError:
            pass

    lsb_facts['major_release'] = "7"
    print("lsb:")
    print(lsb_facts)

# Generated at 2022-06-13 03:05:53.942566
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = mock.Mock()
    module.get_bin_path.return_value = '/bin/lsb_release'
    module.run_command.return_value = 0, "LSB Version:\tdistro\nDistributor ID:\tDistro\nDescription:\tLinux\nRelease:\t2.1\nCodename:\tdev\n", ''
    lsb_fact_collector = LSBFactCollector()

    lsb_facts = lsb_fact_collector.collect(module=module, collected_facts=None)

    module.get_bin_path.assert_called_once_with('lsb_release')
    module.run_command.assert_called_once_with(['/bin/lsb_release', "-a"], errors='surrogate_then_replace')

# Generated at 2022-06-13 03:05:58.795206
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    #  Run the collect method of LSBFactCollector
    lsb = LSBFactCollector().collect()

    assert type(lsb) is dict
    
    assert 'lsb' in lsb
    assert type(lsb['lsb']) is dict

    assert 'id' in lsb['lsb']
    id_valid_values = ['Ubuntu', 'RedHatEnterpriseServer', 'CentOS', 'Debian', 'SUSE LINUX', 'Fedora', 'openSUSE project', 'GentooBaseSystem']
    assert lsb['lsb']['id'] in id_valid_values

    # TODO: add more asserts when method collect is implemented

# Generated at 2022-06-13 03:06:00.916063
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_fact_collector = LSBFactCollector()
    lsb_fact_collector.collect()

# Generated at 2022-06-13 03:06:03.241521
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector. STRIP_QUOTES == r'\'\"\\'


# Generated at 2022-06-13 03:06:04.167394
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    pass

# Generated at 2022-06-13 03:06:09.109916
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts = LSBFactCollector()
    LSBFactCollector._fact_ids = set()
    lsb_facts._lsb_release_file = lambda x: {'id': 'FooOS'}
    lsb_facts._lsb_release_bin = lambda x, y: {'id': 'FooOS', 'release': '0.1'}
    lsb_facts.collect()
    assert lsb_facts._fact_ids == {'lsb'}


# Generated at 2022-06-13 03:07:30.702848
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsbfact_collector_ob = LSBFactCollector()
    assert(lsbfact_collector_ob.name == 'lsb')
    assert(lsbfact_collector_ob._fact_ids == set())
    assert(lsbfact_collector_ob.STRIP_QUOTES == '\'\"\\')


# Generated at 2022-06-13 03:07:32.529759
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    """This will test the constructor of class LSBFactCollector"""

    lsb = LSBFactCollector()
    assert lsb


# Generated at 2022-06-13 03:07:46.639787
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # dict returned by LSBFactCollector
    lsb_dict = LSBFactCollector().collect()
    # value of lsb_dict
    lsb_value = lsb_dict['lsb']
    # test keys in lsb_dict
    assert_keys = set(['codename', 'id', 'release', 'description', 'major_release'])
    if 'lsb' in lsb_dict:
        assert_keys.update(lsb_dict['lsb'].keys())
    assert set(lsb_value.keys()) == assert_keys, 'lsb_dict returned by LSBFactCollector is changed'

# Generated at 2022-06-13 03:07:48.149564
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:07:51.423639
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector is not None
    assert lsb_fact_collector.name == 'lsb'
    assert lsb_fact_collector.STRIP_QUOTES == r'\'\"\\'
    assert lsb_fact_collector._fact_ids == set()


# Generated at 2022-06-13 03:08:09.804763
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    mock_module = type('module')
    mock_module.run_command = lambda x, **kwargs: \
        (0, 'LSB Version:\tyes\n' +
         'Distributor ID:\tDebian\n' +
         'Description:\tDebian GNU/Linux 9.8 \n' +
         'Release:\t9.8\n' +
         'Codename:\tstretch', None)
    mock_module.get_bin_path = lambda x: '/bin/lsb_release'

    LSBFactCollector_test = LSBFactCollector()
    result = LSBFactCollector_test.collect(mock_module)

    # Result should contain a dictionary with lsb keys
    assert 'lsb' in result
    assert 'release' in result['lsb']

# Generated at 2022-06-13 03:08:14.178749
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from . import AnsibleModuleMock
    from . import RunCommandMock

    module = AnsibleModuleMock()
    module.run_command = RunCommandMock()

    LSBFactCollector._lsb_release_bin(LSBFactCollector(), '/usr/bin/lsb_release', module)

# Generated at 2022-06-13 03:08:15.855686
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = AnsibleModuleMock()
    lsb_fact_collector = LSBFactCollector()
    lsb_fact_collector.collect(module)

# Generated at 2022-06-13 03:08:18.661735
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert lsb_collector.name == 'lsb'

# Generated at 2022-06-13 03:08:21.326178
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    """
    Print the output of collect method of class LSBFactCollector to stdout
    """
    print(LSBFactCollector().collect())


# Generated at 2022-06-13 03:11:27.249556
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'

# Generated at 2022-06-13 03:11:28.397277
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsbfc = LSBFactCollector()
    assert lsbfc.name == 'lsb'

# Generated at 2022-06-13 03:11:30.028615
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    class_obj = LSBFactCollector()
    assert class_obj.name == "lsb"
    assert len(class_obj._fact_ids) == 0


# Generated at 2022-06-13 03:11:34.714181
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts import ModuleDataCollector

    test_module = ModuleDataCollector()

    lsb = LSBFactCollector()
    facts = lsb.collect(module=test_module)
    assert isinstance(facts, dict)

    lsb_facts = facts.get('lsb')
    assert isinstance(lsb_facts, dict)

# Generated at 2022-06-13 03:11:36.018102
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    fc = LSBFactCollector()
    assert fc.name == 'lsb'
    assert fc._fact_ids == set()

# Generated at 2022-06-13 03:11:43.785168
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    """ Unit test for method LSBFactCollector.collect """
    module_mock = Mock()
    module_mock.get_bin_path.return_value = "lsb_release"

    module_mock.run_command.return_value = (0, """
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.3 LTS
Release:	16.04
Codename:	xenial
""", "")

    lsb_ins = LSBFactCollector()
    lsb_ins.collect(module=module_mock)

# Generated at 2022-06-13 03:11:50.337203
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts.collector import Cache
    from ansible.module_utils.facts.system.lsb import LSBFactCollector
    from ansible.module_utils.facts.system.lsb import test_LSBFactCollector_collect
    import os
    import os.path
    import pytest
    @pytest.fixture(scope='function')
    def module():
        # remove later once AnsibleModule is included in the test suite
        class AnsibleModule:
            class fail_json(Exception):
                def __init__(self, msg, **kwargs):
                    self.msg = msg
                    self.kwargs = kwargs

            def __init__(self, argument_spec, supports_check_mode=False):
                self.argument_spec = argument_spec
                self.supports_check