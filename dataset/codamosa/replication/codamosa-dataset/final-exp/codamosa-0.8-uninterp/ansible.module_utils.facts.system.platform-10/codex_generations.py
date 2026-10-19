

# Generated at 2022-06-13 03:13:10.650115
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
  """
  Unit test for constructor of class PlatformFactCollector
  """
  import platform

  pfc = PlatformFactCollector()
  assert pfc.name == 'platform'
  assert pfc._fact_ids == {'system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture',
                           'machine_id'}



# Generated at 2022-06-13 03:13:12.472905
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'


# Generated at 2022-06-13 03:13:17.603121
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_fact_collector = PlatformFactCollector()
    platform_facts = platform_fact_collector.collect()
    assert platform_facts.get('system') is not None
    assert platform_facts.get('kernel') is not None
    assert platform_facts.get('machine') is not None
    assert platform_facts.get('architecture') is not None
    assert platform_facts.get('python_version') is not None

# Generated at 2022-06-13 03:13:20.179928
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    instance = PlatformFactCollector()
    assert isinstance(instance, PlatformFactCollector)


# Generated at 2022-06-13 03:13:29.379178
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    module_path = os.path.join(current_dir, '../fixtures/fake_ansible_module.py')

    # Fake module
    module = imp.load_source('module', module_path)

    # Fake facts
    collected_facts = {}

    # Fake platform
    def fake_platform_system():
        return "Linux"

    def fake_platform_release():
        return "2.6.18-164.el5"

    def fake_platform_version():
        return "#1 SMP Tue Aug 18 15:51:48 EDT 2009"

    def fake_platform_machine():
        return "x86_64"


# Generated at 2022-06-13 03:13:30.257013
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()

# Generated at 2022-06-13 03:13:38.761028
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create dict with some values of fact keys
    fact_data = {'kernel': 'Linux',
                 'kernel_version': '3.13.0-53-generic',
                 'machine': 'x86_64',
                 'architecture': 'x86_64',
                 'python_version': '2.7.6',
                 'system': 'Linux',
                 'fqdn': 'test-ansible-host.example.com',
                 'domain': 'example.com',
                 'hostname': 'test-ansible-host',
                 'nodename': 'test-ansible-host.example.com',
                 'userspace_bits': '64'}
    #Get the values of fact keys collected
    platform_fact_collector = PlatformFactCollector()
    platform_facts = platform_fact_collector.collect

# Generated at 2022-06-13 03:13:42.239726
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector()
    assert obj.name == 'platform'
    assert 'system' in obj._fact_ids
    assert 'architecture' in obj._fact_ids
    assert 'machine_id' in obj._fact_ids
    assert len(obj._fact_ids) == 6

# Generated at 2022-06-13 03:13:46.228993
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    assert fact_collector.name == 'platform'
    assert fact_collector._fact_ids == set(['system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id'])

# Generated at 2022-06-13 03:13:48.463314
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    assert True

# Generated at 2022-06-13 03:14:12.512931
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector(None)
    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == set(['system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id'])

# Unit test to test the function collect() in class PlatformFactCollector

# Generated at 2022-06-13 03:14:17.949025
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert collector._fact_ids == set(['system',
                                       'kernel',
                                       'kernel_version',
                                       'machine',
                                       'python_version',
                                       'architecture',
                                       'machine_id'])

# Generated at 2022-06-13 03:14:21.700558
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])



# Generated at 2022-06-13 03:14:29.132904
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert set(platform_collector.collect()) == {'architecture', 'machine_id', 'kernel', 'domain', 'python_version', 'fqdn', 'system', 'machine', 'nodename', 'kernel_version', 'hostname', 'userspace_bits'}
    assert set(platform_collector._fact_ids) == {'system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'}

# Generated at 2022-06-13 03:14:41.063400
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """Check if the PlatformFactCollector class can collect its own facts"""

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import callback_facts

    # FactCollector will call callback_facts.populate() to populate collected_facts
    # with the facts it collects
    collected_facts = dict()  # dict() is necessary instead of {}
    callback_facts.populate(collected_facts)
    # Instantiation of PlatformFactCollector with empty module
    # since it's not necessary
    fact_collector = PlatformFactCollector(module=None)
    fact_collector._collect_platform_subset = lambda x: 'fake_system'
    fact_collector._collect_distribution_facts = lambda x: {'distribution': 'fake_distribution'}
    fact_collect

# Generated at 2022-06-13 03:14:42.593404
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = AnsibleModuleMock({})
    platform_facts = PlatformFactCollector().collect(module=module)
    assert 'system' in platform_facts

# Generated at 2022-06-13 03:14:53.343326
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    module = PlatformFactCollector.AnsibleModuleMock()

    test_hostname = "testhostname"

    def get_bin_path(path):
        if path == 'getconf':
            return '/bin/getconf'
        elif path == 'bootinfo':
            return '/usr/bin/bootinfo'

    test_module_get_bin_path = lambda path: get_bin_path(path)

    module.run_command = lambda command: (0, test_hostname, '')
    module.get_bin_path = test_module_get_bin_path

    facts = PlatformFactCollector.collect(module=module)
    assert facts['hostname'] == test_hostname

# Generated at 2022-06-13 03:15:04.329636
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils import basic
    m = basic.AnsibleModule(
        argument_spec = dict()
    )
    platform_facts = PlatformFactCollector().collect(module=m)

    # check for keys 
    for fact in ('system','kernel','kernel_version','machine','python_version','fqdn','hostname','nodename','domain', 'userspace_bits','architecture','userspace_architecture'):
        assert fact in platform_facts, "Missing %s in collected platform facts" % fact

    # sanity checks
    assert platform_facts['system'] == platform.system()
    assert platform_facts['kernel'] == platform.release()
    assert platform_facts['kernel_version'] == platform.version()
    assert platform_facts['machine'] == platform.machine()

# Generated at 2022-06-13 03:15:12.712933
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts_collector = PlatformFactCollector()

    assert platform_facts_collector.collect(None, None)

# Generated at 2022-06-13 03:15:17.887690
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set([
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id'])


# Generated at 2022-06-13 03:15:36.140022
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == "platform"
    assert PlatformFactCollector._fact_ids == {'system', 'kernel', 'kernel_version',
                                               'machine', 'python_version',
                                               'architecture', 'machine_id'}

# Generated at 2022-06-13 03:15:38.988934
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector()
    assert obj.name == 'platform'
    assert obj._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:15:47.577148
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Inject a mock `platform` to be able to control the return values of
    # calls to `platform.*`
    import sys
    if sys.version_info >= (3, 3):
        import unittest.mock as mock
    else:
        import mock
    mock_platform = mock.Mock()
    mock_platform.machine.return_value = 'x86_64'
    mock_platform.system.return_value = 'Linux'
    mock_platform.architecture.return_value = ('64bit', 'ELF')
    mock_platform.release.return_value = '4.4.0-31-generic'
    mock_platform.version.return_value = '#50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016'

# Generated at 2022-06-13 03:15:50.888788
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fc = PlatformFactCollector()
    assert fc.name == 'platform'
    assert isinstance(fc.collect(), dict)

# Generated at 2022-06-13 03:16:01.908033
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    ModuleData = type('ModuleData', (object,), dict())

    module = ModuleData()

    module.run_command = lambda *args, **kwargs: (0, "test_hostname.test_domain.example.com", "")
    module.get_bin_path = lambda *args, **kwargs: "/sbin/getconf"

    module.exit_json = lambda *args, **kwargs: 0
    module.fail_json = lambda *args, **kwargs: 0

    setattr(platform, "system", lambda: 'AIX')
    setattr(platform, "release", lambda: '7.1.0.0')
    setattr(platform, "node", lambda: 'test_hostname.test_domain.example.com')

# Generated at 2022-06-13 03:16:06.420801
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system', 'kernel', 'kernel_version',
                               'machine', 'python_version', 'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:16:13.603462
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pfc = PlatformFactCollector()
    result = pfc.collect()
    assert result
    assert result.has_key('fqdn')
    assert result.has_key('hostname')
    assert result.has_key('nodename')
    assert result.has_key('domain')
    assert result.has_key('architecture')


# Generated at 2022-06-13 03:16:22.364376
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import sys
    import platform

    class MockModule(object):
        def __init__(self, facts):
            self.params = {}
            self.facts = facts

        def get_bin_path(self, arg):
            return "/bin/%s" % arg

        def run_command(self, arg):
            stdout = stderr = ""

            if isinstance(arg, str):
                arg = arg.split()

            if arg[0] == '/bin/getconf':
                stdout = "64-bit\n"
            elif arg[0] == '/bin/bootinfo':
                stdout = "64-bit\n"
            elif arg[0] == 'uname':
                stdout = "amd64"

            return (0, stdout, stderr)


# Generated at 2022-06-13 03:16:31.134869
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """
    Test PlatformFactCollector.collect method
    """

    parsed_platform_facts = {
        'system': 'Linux',
        'kernel': '3.10.0-327.22.2.el7.x86_64',
        'kernel_version': '#1 SMP Wed Jun 8 19:27:00 UTC 2016',
        'machine': 'x86_64',
        'python_version': '2.7.5',
        'architecture': 'x86_64',
        'userspace_bits': '64',
        'userspace_architecture': 'x86_64'
    }

    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector.platform import PlatformFactCollector

# Generated at 2022-06-13 03:16:38.431763
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platformFactCollector = PlatformFactCollector()

    assert platformFactCollector.name == 'platform'
    assert 'system' in platformFactCollector._fact_ids
    assert 'kernel' in platformFactCollector._fact_ids
    assert 'kernel_version' in platformFactCollector._fact_ids
    assert 'machine' in platformFactCollector._fact_ids
    assert 'python_version' in platformFactCollector._fact_ids
    assert 'architecture' in platformFactCollector._fact_ids
    assert 'machine_id' in platformFactCollector._fact_ids
    assert 'userspace_bits' in platformFactCollector._fact_ids
    assert 'userspace_architecture' in platformFactCollector._fact_ids
    assert 'fqdn' in platformFactCollector._fact_ids
    assert 'hostname'

# Generated at 2022-06-13 03:19:28.418899
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    with open('test/unit/ansible_collections/ansible/community/plugins/facts/platform/ansible_collections/ansible/community/plugins/vars/PlatformFacts.yaml') as f:
        collected_facts = yaml.load(f, Loader=yaml.SafeLoader)
    PlatformFactCollector = PlatformFactCollector()
    platform_facts = PlatformFactCollector.collect(collected_facts=collected_facts)

    assert platform_facts['system'] == 'Linux'
    assert platform_facts['kernel'] == '4.15.0-45-generic'
    assert platform_facts['kernel_version'] == '#48~16.04.1-Ubuntu SMP Tue Jan 29 18:03:48 UTC 2019'
    assert platform_facts['machine'] == 'x86_64'

# Generated at 2022-06-13 03:19:30.898070
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Arrange
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collectors.platform import PlatformFactCollector

    module_facts = ModuleFacts()
    platform_fact_collector = PlatformFactCollector(module_facts)

    # Act
    platform_fact_collector.collect()

    # Assert
    assert platform_fact_collector.name == 'platform'

# Generated at 2022-06-13 03:19:41.301866
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector.platform import PlatformFactCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector

    module = ModuleFacts(connection='local')
    pfc = PlatformFactCollector(module=module)

    def setUpModule():
        BaseFactCollector._FACT_CACHE = {}

    platform_facts = pfc.collect()

    assert 'name' in platform_facts and platform_facts['name'] == 'platform'
    assert 'ansible_facts' in platform_facts
    assert '_fact_ids' in platform_facts
    assert 'system' in platform_facts['ansible_facts']
    assert 'kernel' in platform_facts['ansible_facts']

# Generated at 2022-06-13 03:19:44.970045
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    c = PlatformFactCollector()
    for k in c._fact_ids:
        try:
            getattr(c, k)
        except:
            assert False, "Cannot find fact: %s" % k

# Generated at 2022-06-13 03:19:51.765709
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # construction of representation of a PlatformFactCollector method's invocation
    PlatformFactCollector = PlatformFactCollector()
    result = PlatformFactCollector.collect()
    assert 'system' in result
    assert 'kernel' in result
    assert 'kernel_version' in result
    assert 'machine' in result
    assert 'architecture' in result
    assert 'fqdn' in result
    assert 'hostname' in result
    assert 'nodename' in result
    assert 'domain' in result
    assert 'userspace_bits' in result
    assert 'python_version' in result
    assert 'machine_id' in result

# Generated at 2022-06-13 03:19:53.608171
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect()

# Generated at 2022-06-13 03:20:03.232502
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():  # pylint: disable=invalid-name
    """
    Test the claims made in the docstring of the collect method

    Collect facts about the host platform as reported by the python standard
    library module called platform.
    """
    from ansible.module_utils.facts import ModuleFacts
    import ansible.utils.platform as _platform
    from ansible.module_utils.facts.collector.platform import PlatformFactCollector
    import sys
    import platform

    module = ModuleFacts()
    facts_obj = ModuleFacts()

    # Provide mock values for the python builtins called
    # by the platform module since we can't rely on
    # the values to be consistent across platforms and
    # python versions.
    def os_name(exec_path):
        return "SunOS"

# Generated at 2022-06-13 03:20:04.848720
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platformCollector = PlatformFactCollector()
    assert 'kernel' in platformCollector._fact_ids

# Generated at 2022-06-13 03:20:06.222135
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'

# Generated at 2022-06-13 03:20:10.648130
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """
    PlatformFactCollector - test for constructor of class PlatformFactCollector
    """
    assert PlatformFactCollector.name == 'platform', "PlatformFactCollector's name is not platform"
    assert PlatformFactCollector._fact_ids == set(['system',
                                                   'kernel',
                                                   'kernel_version',
                                                   'machine',
                                                   'python_version',
                                                   'architecture',
                                                   'machine_id']), "PlatformFactCollector's _fact_ids is not as expected"