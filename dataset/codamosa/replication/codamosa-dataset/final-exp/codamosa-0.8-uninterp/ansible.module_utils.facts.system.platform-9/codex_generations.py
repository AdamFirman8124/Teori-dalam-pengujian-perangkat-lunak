

# Generated at 2022-06-13 03:13:09.383283
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    plat = PlatformFactCollector()
    assert plat.name == 'platform'
    assert plat._fact_ids == set(['system',
                                  'kernel',
                                  'kernel_version',
                                  'machine',
                                  'python_version',
                                  'architecture',
                                  'machine_id'])


# Generated at 2022-06-13 03:13:12.548665
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector().collect()
    assert platform_facts
    assert platform_facts['system'] == 'Linux'
    assert platform_facts['machine'] == 'x86_64'


if __name__ == '__main__':
    test_PlatformFactCollector_collect()

# Generated at 2022-06-13 03:13:13.647662
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector().name == 'platform'


# Generated at 2022-06-13 03:13:17.564186
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts.name == 'platform'
    assert platform_facts._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:13:26.368981
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = None
    platform_facts = PlatformFactCollector().collect(module)
    assert(platform_facts['system'] == 'Linux')
    assert(platform_facts['kernel'] == '4.4.0-28-generic')
    assert(platform_facts['machine'] == 'x86_64')
    assert(platform_facts['architecture'] == 'x86_64')
    assert(platform_facts['fqdn'] == 'myhostname.mydomain.com')
    assert(platform_facts['hostname'] == 'myhostname')
    assert(platform_facts['nodename'] == 'myhostname.mydomain.com')
    assert(platform_facts['domain'] == 'mydomain.com')

# Generated at 2022-06-13 03:13:30.888070
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

# Generated at 2022-06-13 03:13:39.121818
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = object()
    collected_facts = object()

    platform_fact_collector = PlatformFactCollector()

    # Injecting methods and attributes that don't exist in "platform" module
    def getfqdn_return_value():
        return "test_fqdn"
    platform.getfqdn = getfqdn_return_value
    def split_return_value():
        return ["test_hostname"]
    platform.node.split = split_return_value
    def listdir_return_value():
        return ["system", "kernel", "kernel_version", "machine",
                "python_version", "architecture", "machine_id"]
    platform.listdir = listdir_return_value
    def getconf_bin_return_value():
        return True
    module.get_bin_path = get

# Generated at 2022-06-13 03:13:41.015997
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()

    assert pf.name == 'platform'
    assert 'system' in pf.collect().keys()

# Generated at 2022-06-13 03:13:45.815527
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """
        Returns true on success and false on failure.
    """
    def _make_instance(collected_facts=None):
        """Return an instance of PlatformFactCollector with a set of fake
        collected_facts.
        """
        if collected_facts is None:
            collected_facts = dict()
        return PlatformFactCollector(collected_facts=collected_facts)
    instance = _make_instance()
    assert instance is not None

# Generated at 2022-06-13 03:13:48.358135
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector()

# Generated at 2022-06-13 03:14:16.964440
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    # Create fake module object
    class FakeModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, name, required=False):
            return self.params[name]

        def run_command(self, cmd):
            return (self.params[cmd[0]], '', '')

    # test data for unit test of collect function
    test_data = dict(platform=dict(system='Linux',
                                   kernel='2.6.32-504.3.3.el6.x86_64',
                                   machine='x86_64'))

    # getconf should return architecture returned by uname -m
    test_data['getconf'] = test_data['platform']['machine']

    # test data for bootinfo -p (AIX)
   

# Generated at 2022-06-13 03:14:26.696694
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = FakeAnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    platform_fact_collector = PlatformFactCollector()


# Generated at 2022-06-13 03:14:34.046554
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    class TestPlatform(object):
        def __init__(self):
            self.system = "Linux"
            self.release = "3.10.0-327.el7.x86_64"
            self.version = "#1 SMP Thu Nov 19 22:10:57 UTC 2015"
            self.machine = "x86_64"
            self.node = "test-node"
            self.python_version = "2.7.5"
            self.architecture = "64bit"
            self.fqdn = "test-node"

        def uname(self):
            return [self.system, self.node, self.release, self.version, self.machine]

    class TestModule(object):
        def get_bin_path(self, filename):
            return "/usr/bin/" + filename


# Generated at 2022-06-13 03:14:38.633916
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

# Generated at 2022-06-13 03:14:40.867807
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.collect()["system"] == platform.system()


# Generated at 2022-06-13 03:14:42.534701
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert len(x._fact_ids) == 8

# Generated at 2022-06-13 03:14:54.292286
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collectors.platform import PlatformFactCollector
    from ansible.module_utils.facts import Facts
    import platform

    class ModuleMock(object):
        def get_bin_path(self, binary):
            return binary if binary in ['bootinfo', 'getconf'] else None

        def run_command(self, args):
            if args[0] == "bootinfo":
                return 0, "powerpc", ""
            elif args[0] == "getconf":
                return 0, "powerpc", ""
            else:
                return 0, "", ""

    class PlatformMock(object):

        @staticmethod
        def uname():
            return "OpenBSD", "", "", "", "amd64"

        @staticmethod
        def system():
            return "OpenBSD"



# Generated at 2022-06-13 03:14:57.991371
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



# Generated at 2022-06-13 03:15:08.403605
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    # Testing if method collect of PlatformFactCollector class
    # returns a dict of facts
    def mock_platform_system():
        return 'Linux'

    def mock_platform_release():
        return '3.13.0-43-generic'

    def mock_platform_version():
        return '#72-Ubuntu SMP Mon Dec 8 19:35:06 UTC 2014'

    def mock_platform_machine():
        return 'i686'

    def mock_platform_python_version():
        return '2.7.6'

    def mock_getfqdn():
        return 'myhost.domain'

    def mock_platform_node():
        return 'myhost.domain'

    def mock_platform_architecture():
        return ('64bit', 'ELF')


# Generated at 2022-06-13 03:15:12.095952
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == "platform"
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:15:23.898115
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()
    assert collector.name == 'platform'
    assert sorted(collector._fact_ids) == sorted([
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id'
    ])

# Generated at 2022-06-13 03:15:26.933560
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()
    assert pf.name == 'platform'
    assert isinstance(pf.collect(), dict)

# Generated at 2022-06-13 03:15:31.348428
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()

    assert p.name == 'platform'
    assert p._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:15:46.797036
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import socket
    import re
    from ansible.module_utils.facts.collector import BaseFactCollector

    class PlatformFactCollector(BaseFactCollector):
        name = 'platform'
        _fact_ids = set(['system',
                         'kernel',
                         'kernel_version',
                         'machine',
                         'python_version',
                         'architecture',
                         'machine_id'])
        def __init__(self, *args, **kwargs):
            self.platform = platform
            self.socket = socket
            self.re = re
            self.collect = self.collect()

    x = PlatformFactCollector()
    result = x.collect()
    platform_facts = {}
    platform_facts['system'] = platform.system()
    platform_facts['kernel'] = platform.release()


# Generated at 2022-06-13 03:15:49.938275
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    obj = PlatformFactCollector()
    assert set(obj.collect()) == set(["system", "kernel", "kernel_version", "machine", "python_version", "architecture"])

# Generated at 2022-06-13 03:15:58.291094
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import json
    import sys
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector

    myFacts = PlatformFactCollector()
    myFacts.collect()

    assert(myFacts.name == "platform")
    assert(len(myFacts._fact_ids) == 8)
    assert("system" in myFacts._fact_ids)
    assert("kernel" in myFacts._fact_ids)
    assert("kernel_version" in myFacts._fact_ids)
    assert("machine" in myFacts._fact_ids)
    assert("python_version" in myFacts._fact_ids)
    assert("architecture" in myFacts._fact_ids)

# Generated at 2022-06-13 03:16:02.052267
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])


# Generated at 2022-06-13 03:16:04.742165
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():

    x = PlatformFactCollector()
    assert x
    assert x.name == "platform"

    for fact in x._fact_ids:
        assert fact in x.collect()

# Generated at 2022-06-13 03:16:06.737860
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # unit tests for the PlatformFactCollector will be written in the future
    return

# Generated at 2022-06-13 03:16:17.889633
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import sys
    from ansible_collections.community.general.plugins.module_utils.facts.collectors.platform import PlatformFactCollector

    class MockModule:
        def __init__(self):
            self._paths = {'bin': '/bin'}
            self._result = {'bin': True}

        def get_bin_path(self, path):
            return self._paths[path] if path in self._result else None

        def run_command(self, cmd):
            return (0, '', '')

    class MockPlatform:
        def __init__(self):
            self.system = 'OS'
            self.release = 'Release'
            self.version = 'Version'
            self.machine = 'Machine'
            self.python_version = 'PythonVersion'

# Generated at 2022-06-13 03:17:46.672330
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():

    # Expected values
    fact_ids = set(['system',
                    'kernel',
                    'kernel_version',
                    'machine',
                    'python_version',
                    'architecture',
                    'machine_id'])

    # Create a PlatformFactCollector object by calling constructor
    platform_fact_collector_obj = PlatformFactCollector()

    # Verify members of PlatformFactCollector class
    assert platform_fact_collector_obj.name == 'platform'
    assert platform_fact_collector_obj._fact_ids == fact_ids

# Generated at 2022-06-13 03:17:52.578149
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    class MockModule(object):
        def __init__(self, ansible_facts):
            self.ansible_facts = ansible_facts

        def get_bin_path(self, name):
            return "/bin/{0}".format(name)

        def run_command(self, cmd):
            if cmd[0] == '/bin/bootinfo':
                 return 0, "pSeries\n", ""
            elif cmd[0] == '/bin/getconf':
                if cmd[1] == 'MACHINE_ARCHITECTURE':
                    return 0, "powerpc\n", ""
                else:
                    return 0, "", ""
            elif cmd[0] == '/bin/uname':
                return 0, "amd64\n", ""
            else:
                return 0, "", ""

    platform_facts

# Generated at 2022-06-13 03:18:01.442198
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    try:
        import platform
        import socket
        import re
    except ImportError:
        # These modules are not available on Windows
        raise ImportError
    else:
        c = PlatformFactCollector({}, {})
        res = c.collect()
        assert res['system'] == platform.system()
        assert res['fqdn'] == socket.getfqdn()
        assert res['nodename'] == platform.node()
        assert res['hostname'] == platform.node().split('.')[0]
        assert res['domain'] == '.'.join(res['fqdn'].split('.')[1:])
        assert res['architecture'] == platform.machine()
        assert res['kernel_version'] == platform.version()
        assert res['kernel'] == platform.release()

# Generated at 2022-06-13 03:18:02.859322
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector().name == 'platform'



# Generated at 2022-06-13 03:18:11.214228
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    sys_platform = platform.system()
    kernel_release = platform.release()
    kernel_version = platform.version()
    machine_architecture = platform.machine()
    python_version = platform.python_version()

    platform_collector = PlatformFactCollector()

    fake_module = class_fixture(name='AnsibleModule', base_class=object).AnsibleModule
    platform_facts = platform_collector.collect(module=fake_module, collected_facts=None)

    assert isinstance(platform_facts, dict)
    assert platform_facts['system'] == sys_platform
    assert platform_facts['kernel'] == kernel_release
    assert platform_facts['kernel_version'] == kernel_version
    assert platform_facts['machine'] == machine_architecture
    assert platform_facts['python_version'] == python

# Generated at 2022-06-13 03:18:11.609439
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()

# Generated at 2022-06-13 03:18:12.229347
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'

# Generated at 2022-06-13 03:18:16.057553
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert 'system' in pfc._fact_ids
    assert 'kernel' in pfc._fact_ids
    assert 'kernel_version' in pfc._fact_ids
    assert 'machine' in pfc._fact_ids
    assert 'architecture' in pfc._fact_ids
    assert 'fqdn' in pfc._fact_ids
    assert 'hostname' in pfc._fact_ids
    assert 'domain' in pfc._fact_ids
    assert 'machine_id' in pfc._fact_ids


# Generated at 2022-06-13 03:18:22.402952
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


# Generated at 2022-06-13 03:18:24.855008
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector()
    assert obj.name == 'platform'
    assert obj._fact_ids == set(['system', 'kernel', 'kernel_version',
                                 'machine', 'python_version',
                                 'architecture', 'machine_id'])


# Generated at 2022-06-13 03:21:23.362201
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()
    assert set(['system', 'kernel', 'kernel_version',
                'machine', 'python_version', 'architecture',
                'machine_id']) == pf.fact_ids

# Generated at 2022-06-13 03:21:31.729980
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """
    Unit test for method collect of class PlatformFactCollector
    """

    # Setup dict of required platform facts
    class FakeModule(object):
        def get_bin_path(self, command):
            """
            Return fake bin_path
            """
            return '/usr/bin/%s' % command

        def run_command(self, command):
            """
            Return fake run_command data
            """
            return 0, '', ''

    class FakePlatformFacts(object):
        def __init__(self, data):
            """
            Setup FakePlatformFacts object to return platform data
            """
            self._data = data

        def system(self):
            """
            Return fake platform data
            """
            return self._data

        def release(self):
            """
            Return fake platform data
            """
           

# Generated at 2022-06-13 03:21:32.748271
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x


# Generated at 2022-06-13 03:21:36.802467
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    assert fact_collector.name == 'platform'
    assert fact_collector._fact_ids == set(['system', 'kernel',
                                            'kernel_version', 'machine',
                                            'python_version', 'architecture',
                                            'machine_id'])

# Generated at 2022-06-13 03:21:43.382792
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    fact_collector = FactCollector()
    fact_collector.collect_platform_facts()

    # The variables collected platform facts should be present and not empty
    for fact in PlatformFactCollector._fact_ids:
        assert fact_collector.ansible_facts[fact] is not None
        assert fact_collector.ansible_facts[fact] != ""

    # The system, kernel and machine variable should not be the same
    assert fact_collector.ansible_facts['system'] != fact_collector.ansible_facts['kernel']
    assert fact_collector.ansible_facts['system'] != fact_collector.ansible_facts['machine']

# Generated at 2022-06-13 03:21:49.521058
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    class MockModule:
        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'getconf':
                return '/usr/bin/getconf'
            elif name == 'bootinfo':
                return '/usr/bin/bootinfo'
            else:
                return None

        def run_command(self, command):
            if command == ['/usr/bin/getconf', 'MACHINE_ARCHITECTURE']:
                return (0, 'powerpc64\n', '')
            elif command == ['/usr/bin/bootinfo', '-p']:
                return (0, 'rs6k\n', '')
            else:
                return (0, '', '')

    c = PlatformFactCollector()
    a = c.collect(MockModule())

# Generated at 2022-06-13 03:21:51.260327
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = AnsibleModule(argument_spec=dict())

    x = PlatformFactCollector()
    print("test: x.collect()")
    x.collect(module)

# Generated at 2022-06-13 03:21:52.090496
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x

# Generated at 2022-06-13 03:21:58.987666
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector != None
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == ['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id']
    assert platform_fact_collector.collect() != None


# Generated at 2022-06-13 03:22:03.492458
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collect_obj = PlatformFactCollector()
    assert collect_obj.name == 'platform'
    assert collect_obj._fact_ids == set(['system',
                                         'kernel',
                                         'kernel_version',
                                         'machine',
                                         'python_version',
                                         'architecture',
                                         'machine_id'])