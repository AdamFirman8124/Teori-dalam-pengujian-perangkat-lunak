

# Generated at 2022-06-13 03:01:54.602440
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert LSBFactCollector.name == 'lsb'

# Generated at 2022-06-13 03:01:56.521009
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'
    assert len(lsb.collect()) >= 0

# Generated at 2022-06-13 03:01:57.705927
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert lsb_collector

# Generated at 2022-06-13 03:02:00.451957
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == "lsb"
    assert x._fact_ids == set()
    assert x.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:02:04.604777
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fc = LSBFactCollector()
    assert lsb_fc.name == 'lsb'
    assert lsb_fc._fact_ids == set()
    assert lsb_fc.STRIP_QUOTES == '\'\"\\'

# Generated at 2022-06-13 03:02:07.757790
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fc = LSBFactCollector()
    assert lsb_fc.name == 'lsb'
    assert type(lsb_fc._fact_ids) == set

# Generated at 2022-06-13 03:02:11.085406
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb['lsb'] == {}
    assert lsb.name == 'lsb'

# Generated at 2022-06-13 03:02:18.809934
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb', 'LSBFactCollector.name != lsb'
    assert lsb_fact_collector._fact_ids == set(), 'LSBFactCollector._fact_ids != set()'
    assert lsb_fact_collector.STRIP_QUOTES == r'\'\"\\', 'LSBFactCollector.STRIP_QUOTES != r\'\"\\\''

# Generated at 2022-06-13 03:02:22.703030
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    from ansible.module_utils import basic
    m = basic.AnsibleModule(
        argument_spec={},
    )
    lsb = LSBFactCollector()
    l = lsb.collect(module=m)
    assert 'lsb' in l
    assert 'release' in l['lsb']

# Generated at 2022-06-13 03:02:34.293860
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts_commands = {
        'release': 'Debian',
        'id': 'Debian',
        'description': 'Debian GNU/Linux 8.10 (jessie)',
        'release': '8.10',
        'codename': 'jessie',
        'major_release': '8'
    }
    lsb_facts_file = {
        'id': 'Debian',
        'release': '8.10',
        'codename': 'jessie',
        'major_release': '8',
        'description': 'Debian GNU/Linux 8.10 (jessie)'
    }
    args = {'module': MagicMock(), 'collected_facts': None}

# Generated at 2022-06-13 03:02:43.553670
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    col = LSBFactCollector()
    assert col.name == 'lsb'
    assert col.fact_class == 'hardware'
    assert col._fact_ids == set()

    col = LSBFactCollector(fact_class='software')
    assert col.fact_class == 'software'

# Generated at 2022-06-13 03:02:50.344287
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    """
    test_LSBFactCollector_collect: Unit test method collect of LSBFactCollector
    """

    import ansible_collections.ansible.community.plugins.module_utils.facts.collectors.lsb

    # Create an instance of the LSBFactCollector class
    test_LSB = ansible_collections.ansible.community.plugins.module_utils.facts.collectors.lsb.LSBFactCollector()

    # test_LSB.collect() by unit testing the collect method
    assert test_LSB.collec() == {}


# Generated at 2022-06-13 03:02:54.431933
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector(None)

    assert lsb_fact_collector.name == 'lsb'
    assert lsb_fact_collector._fact_ids == set()
    assert lsb_fact_collector.STRIP_QUOTES == r'\'\"\\'


# Generated at 2022-06-13 03:02:56.238289
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector
    assert lsb_fact_collector.name == "lsb"

# Generated at 2022-06-13 03:03:07.090462
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    """Unit test for method collect of class LSBFactCollector."""
    import subprocess

    class FakeModule(object):
        def __init__(self):
            self.params = None
            self.exit_json = None
            self.fail_json = None
            self.run_command = None

        class MockRunCommand(object):
            RC_OK = 0
            RC_NOT_EXISTS = 1

            def __init__(self, rc, out, err):
                self.rc = rc
                self.out = out
                self.err = err

            def __call__(self, args, **kwargs):
                if not args[0]:
                    return self.RC_NOT_EXISTS, self.out, self.err
                return self.rc, self.out, self.err


# Generated at 2022-06-13 03:03:18.157600
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    import mock

    # create mock for module
    # module.run_command
    # module.get_bin_path
    lsb_release_file_content = "DISTRIB_ID=Ubuntu\nDISTRIB_RELEASE=14.04\nDISTRIB_CODENAME=trusty\nDISTRIB_DESCRIPTION=\"Ubuntu 14.04.1 LTS\"\n"
    lsb_release_bin_content = """
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.2 LTS
Release:        14.04
Codename:       trusty
    """
    with mock.patch('ansible.module_utils.facts.collector.get_file_lines') as get_file_lines:
        get_file_lines.return_value = lsb_release_file_content.splitlines()

# Generated at 2022-06-13 03:03:20.669091
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == 'lsb'
    assert x._fact_ids == set()
    assert x.STRIP_QUOTES == '\'\"\\'


# Generated at 2022-06-13 03:03:24.679528
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'
    assert lsb._fact_ids == set()
    assert lsb.STRIP_QUOTES == r'\'\"\\'


# Generated at 2022-06-13 03:03:33.427578
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = MockModule()
    lsb_path = module.get_bin_path('lsb_release')
    lsb_path_out = module.run_command(['lsb_release', '-a'])
    module.run_command = Mock(return_value=lsb_path_out)
    lsb_collector = LSBFactCollector()
    lsb_facts = lsb_collector.collect(module=module)
    module.run_command = Mock(return_value=(1, '', 'Surrogate then replace'))
    lsb_collector = LSBFactCollector()
    lsb_facts_empty = lsb_collector.collect(module=module)
    assert lsb_facts['lsb']['release'] == '2.0'

# Generated at 2022-06-13 03:03:38.089350
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    """
    Test the constructor of ``LSBFactCollector``
    """
    lsb_facts = LSBFactCollector()
    assert lsb_facts.name == 'lsb'
    assert lsb_facts._fact_ids == set()
    assert lsb_facts.STRIP_QUOTES == "\\'\"\\\\"


# Generated at 2022-06-13 03:03:53.794783
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()

# Generated at 2022-06-13 03:03:57.422036
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsbfc = LSBFactCollector()
    assert lsbfc is not None
    assert lsbfc.name == 'lsb'

if __name__ == '__main__':
    test_LSBFactCollector()

# Generated at 2022-06-13 03:04:08.145307
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_bin_path = '/usr/bin/lsb_release'
    test_module = MagicMock(spec=dict)
    test_module.run_command.side_effect = [
        (0, '''LSB Version:\tcore-9.20170808ubuntu1-noarch:security-9.20170808ubuntu1-noarch
Distributor ID:\tUbuntu
Description:\tUbuntu 18.04.1 LTS
Release:\t18.04
Codename:\tbionic''', ''),
        (1, '', '')
    ]
    test_module.get_bin_path.return_value = lsb_bin_path

    lsb = LSBFactCollector()

# Generated at 2022-06-13 03:04:10.723091
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'
    assert lsb_fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:04:14.262834
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_collector = LSBFactCollector()
    assert set(['lsb']) == lsb_collector._fact_ids

# Generated at 2022-06-13 03:04:15.901823
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsbFactCollector = LSBFactCollector()

    assert lsbFactCollector
    assert lsbFactCollector.name == 'lsb'
    assert 'lsb' in lsbFactCollector._fact_ids

# Generated at 2022-06-13 03:04:17.794957
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    module = None
    lsb_fact_collector = LSBFactCollector(module)

    assert lsb_fact_collector is not None

# Generated at 2022-06-13 03:04:18.561412
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb
    assert lsb.name == 'lsb'

# Generated at 2022-06-13 03:04:28.493637
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.lsb import LSBFactCollector
    from ansible.module_utils.facts.utils import fetch_file_lines
    from ansible.module_utils.facts.utils import get_file_lines

    class AnsibleModuleMock:
        def __init__(self):
            self.run_command_count = 0
            self.run_command_called = []
            self.run_command_rc = 0
            self.run_command_out = ''
            self.run_command_err = None

        def get_bin_path(self, bin):
            rc = self.run_command_rc
            out = self.run_command_out
            err = self.run_command_err

            self.run_command_

# Generated at 2022-06-13 03:04:30.480611
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert 'lsb' == lsb_fact_collector.name

# Generated at 2022-06-13 03:04:58.059488
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x
    assert x.name == 'lsb'

# Generated at 2022-06-13 03:05:04.328716
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_facts = {}
    lsb_facts['id'] = 'Debian'
    lsb_facts['description'] = 'Debian GNU/Linux 8.0 (jessie)'
    lsb_facts['release'] = '8.0'
    lsb_facts['major_release'] = '8'
    lsb_facts['codename'] = 'jessie'

    lsb_facts_bin = {'codename': 'jessie',
                     'id': 'Debian',
                     'release': '8.0',
                     'major_release': '8',
                     'description': 'Debian GNU/Linux 8.0 (jessie)'}


# Generated at 2022-06-13 03:05:08.073731
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    # Empty case
    LSBFactCollector().collect()

    # Typical case
    lsb_path = os.path.realpath('tests/module_utils/facts/lsb/lsb_release')
    module = MockModule(lsb_path)
    LSBFactCollector().collect(module)

# Generated at 2022-06-13 03:05:09.499828
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector

# Generated at 2022-06-13 03:05:15.344865
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    set_module_args(dict(
        ansible_facts={}
    ))

    class MockModule:
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, executable, required=False, opt_dirs=None):
            if executable == 'lsb_release':
                return '/usr/bin/lsb_release'
            else:
                return None


# Generated at 2022-06-13 03:05:17.950977
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    fact_collector = LSBFactCollector()
    name = fact_collector.name
    fact_ids = fact_collector._fact_ids
    assert name == 'lsb'
    assert fact_ids == set()

# Generated at 2022-06-13 03:05:19.578962
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fc = LSBFactCollector()
    assert lsb_fc.name == 'lsb'

# Generated at 2022-06-13 03:05:20.730937
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
  assert LSBFactCollector.name == 'lsb'
  assert LSBFactCollector.STRIP_QUOTES == r'\'\"\\'

# Generated at 2022-06-13 03:05:22.478864
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector.name == 'lsb'

# Generated at 2022-06-13 03:05:24.055387
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBFactCollector()


# Generated at 2022-06-13 03:06:29.877293
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == 'lsb'
    assert x._fact_ids is not None
    assert len(x._fact_ids) == 0

# Generated at 2022-06-13 03:06:31.800081
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector = LSBFactCollector()
    assert lsb_fact_collector is not None


# Generated at 2022-06-13 03:06:35.375732
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert hasattr(LSBFactCollector, "name")
    assert hasattr(LSBFactCollector, "_fact_ids")
    assert hasattr(LSBFactCollector, "STRIP_QUOTES")
    assert hasattr(LSBFactCollector, "_lsb_release_bin")
    assert hasattr(LSBFactCollector, "_lsb_release_file")
    assert hasattr(LSBFactCollector, "collect")

# Generated at 2022-06-13 03:06:44.028264
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    import sys
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_collector_names

    # Set up a mock object for a module to use for command execution.
    class MockModule(object):
        def __init__(self):
            self.run_command_count = 0
            self.run_command_lsb_paths = ['/usr/bin/lsb_release', '/bin/lsb_release', '/usr/sbin/lsb_release', '/sbin/lsb_release']

        def get_bin_path(self, binary):
            binary_paths = {'lsb_release': self.run_command_lsb_paths}


# Generated at 2022-06-13 03:06:52.003246
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb_bin = '/bin/lsb_release'
    lsb_file = 'spec/lsb-fake'
    module = FakeModule(bin_path=lsb_bin, file=lsb_file)
    result = LSBFactCollector().collect(module=module)

    assert result['lsb']['id'] == 'Ubuntu'
    assert result['lsb']['release'] == '16.04'
    assert result['lsb']['description'] == 'Ubuntu 16.04.1 LTS'
    assert result['lsb']['codename'] == 'xenial'
    assert result['lsb']['major_release'] == '16'



# Generated at 2022-06-13 03:06:57.460600
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    # Testing with lsb_release and etc/lsb-release
    lsb_path = "/usr/bin/lsb_release"
    lsb_facts_script = {
        'description': 'CentOS Linux release 7.3.1611 (Core)',
        'codename': 'Core',
        'id': 'CentOS',
        'release': '7.3.1611'
    }

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.bin_path = lsb_path

        def get_bin_path(self, *args, **kwargs):
            return self.bin_path


# Generated at 2022-06-13 03:07:00.388002
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    lsb = LSBFactCollector()
    lsb_facts = lsb.collect()
    assert (lsb_facts['lsb'])


# Generated at 2022-06-13 03:07:00.868666
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    pass

# Generated at 2022-06-13 03:07:03.311674
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():

    # Create a class object for testing
    lsb_fact_collector = LSBFactCollector()

    # Testing for collect function
    assert lsb_fact_collector.collect() == {}

# Generated at 2022-06-13 03:07:21.203525
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    os.environ['PATH'] = '/bin:/usr/bin'
    os.rename('/etc/lsb-release', '/etc/lsb-release.bak')
    with open('/etc/lsb-release', 'w') as f:
        f.write('DISTRIB_ID=Ubuntu\n')
        f.write('DISTRIB_RELEASE=16.04\n')
        f.write('DISTRIB_CODENAME=xenial\n')
        f.write('DISTRIB_DESCRIPTION="Ubuntu 16.04.1 LTS"\n')

    lsb_facts = LSBFactCollector.collect()
    assert lsb_facts
    assert lsb_facts['lsb']['release'] == '16.04'

# Generated at 2022-06-13 03:10:16.174756
# Unit test for method collect of class LSBFactCollector

# Generated at 2022-06-13 03:10:28.298658
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    LSBfactCollector = LSBFactCollector()
    assert LSBfactCollector.name == 'lsb'
    assert LSBfactCollector.STRIP_QUOTES == '\'\"\\'


# Generated at 2022-06-13 03:10:33.906641
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collectors.lsb import LSBFactCollector
    from ansible.module_utils.facts.utils import collect_all_facts

    facts_list = [
        'lsb',
    ]

    base_collector = FactCollector(collect_all_facts=collect_all_facts)

    assert(isinstance(base_collector.load_collector(LSBFactCollector), LSBFactCollector))

    assert(LSBFactCollector.name in facts_list)

# Generated at 2022-06-13 03:10:35.446950
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb = LSBFactCollector()
    assert lsb.name == 'lsb'
    assert lsb._fact_ids == set()



# Generated at 2022-06-13 03:10:36.646792
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    x = LSBFactCollector()
    assert x.name == 'lsb'

# Generated at 2022-06-13 03:10:41.591132
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    lsb_fact_collector_obj = LSBFactCollector()
    assert lsb_fact_collector_obj.name == 'lsb'
    assert not lsb_fact_collector_obj._fact_ids


# Generated at 2022-06-13 03:10:43.571520
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    fact_collector = LSBFactCollector()
    assert fact_collector.name == 'lsb'
    assert fact_collector._fact_ids == set()

# Generated at 2022-06-13 03:10:52.349137
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    import tempfile
    import os

    # create a temp file with lsb_release output
    tmpfile = tempfile.NamedTemporaryFile(delete=False)

    lsb_release_data = """
LSB Version:	core-9.20160110ubuntu0.2-amd64:core-9.20160110ubuntu0.2-noarch:security-9.20160110ubuntu0.2-amd64:security-9.20160110ubuntu0.2-noarch
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.4 LTS
Release:	16.04
Codename:	xenial
""".strip().splitlines()

    with open(tmpfile.name, 'w') as fp:
        fp.write("\n".join(lsb_release_data))

    # we

# Generated at 2022-06-13 03:10:58.529288
# Unit test for constructor of class LSBFactCollector
def test_LSBFactCollector():
    assert hasattr(LSBFactCollector, 'name')
    assert hasattr(LSBFactCollector, '_fact_ids')
    assert hasattr(LSBFactCollector, 'STRIP_QUOTES')
    assert hasattr(LSBFactCollector, '_lsb_release_bin')
    assert hasattr(LSBFactCollector, '_lsb_release_file')
    assert hasattr(LSBFactCollector, 'collect')
    assert hasattr(LSBFactCollector, '__doc__')

# Generated at 2022-06-13 03:11:07.345163
# Unit test for method collect of class LSBFactCollector
def test_LSBFactCollector_collect():
    module = Mock()
    module.run_command.return_value = (0, 'LSB Version:	:core-4.1-amd64:core-4.1-noarch', None)
    module.get_bin_path.return_value = '/usr/bin/lsb_release'
    lsb = LSBFactCollector()
    lsb_facts = lsb.collect(module)
    assert lsb_facts['lsb'] == {'description': ':core-4.1-amd64:core-4.1-noarch',
                                'id': 'LSB',
                                'major_release': 'core-4.1-amd64',
                                'release': ':core-4.1-amd64:core-4.1-noarch'}

