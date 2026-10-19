

# Generated at 2022-06-13 04:20:46.312706
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec=dict())
    myzone = SunOSVirtual(module)
    res = myzone.get_virtual_facts()
    assert res['container'] == 'zone'
    assert 'virtualization_role' in res
    assert 'virtualization_type' in res
    assert res['virtualization_role'] == 'guest'
    assert res['virtualization_type'] == 'zone'
    assert 'virtualization_tech_guest' in res
    assert 'virtualization_tech_host' in res
    assert 'zone' in res['virtualization_tech_guest']
    assert 'zone' in res['virtualization_tech_host']

    module = AnsibleModule(argument_spec=dict())
    mypvm = SunOSVirtual(module)
    res = mypvm.get_virtual_facts()

# Generated at 2022-06-13 04:20:54.808992
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = DummyModule()
    cmds = {
        'zonename': '/usr/bin/zonename',
        'modinfo': '/usr/kernel/drv/amd64/vmmon',
        'virtinfo': '/usr/sbin/virtinfo',
        'smbios': '/usr/sbin/smbios'
    }

# Generated at 2022-06-13 04:20:56.544411
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # run constructor test on class SunOSVirtual
    facts = SunOSVirtual({})
    assert facts.__class__.__name__ == 'SunOSVirtual'


# Generated at 2022-06-13 04:21:09.648558
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Test if we correctly detect a zone
    module = FakeModule(dict(zone_name='global'))
    sunos_virtual_instance = SunOSVirtual(module)
    assert 'zone' in sunos_virtual_instance.get_virtual_facts()['virtualization_tech_host']
    module = FakeModule(dict(zone_name='notglobal'))
    sunos_virtual_instance = SunOSVirtual(module)
    assert 'zone' in sunos_virtual_instance.get_virtual_facts()['virtualization_tech_guest']
    # Test if we correctly detect branded zones
    module = FakeModule()
    sunos_virtual_instance = SunOSVirtual(module)
    assert 'zone' in sunos_virtual_instance.get_virtual_facts()['virtualization_tech_guest']
    # Test if we correctly detect a

# Generated at 2022-06-13 04:21:11.235346
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    s = SunOSVirtual({})
    assert s.platform == 'SunOS'

# Generated at 2022-06-13 04:21:20.118022
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec=dict())

    # Setup mocked module
    v = SunOSVirtual()
    v.module = module
    v.module.run_command = run_mocked_command
    v.module.get_bin_path = lambda x: "/usr/sbin/%s" % x

    # Run the code to test
    facts = v.get_virtual_facts()

    assert facts['virtualization_tech'] == set(['kvm'])
    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_type'] == 'kvm'

    # Test zone

# Generated at 2022-06-13 04:21:23.567245
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, 'global', '')
    sunos_virtual = SunOSVirtual(module)
    assert sunos_virtual is not None

# Generated at 2022-06-13 04:21:27.705883
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtual_collector = SunOSVirtualCollector()

    assert sunos_virtual_collector._platform == 'SunOS'
    assert sunos_virtual_collector._fact_class.__name__ == 'SunOSVirtual'
    assert sunos_virtual_collector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 04:21:36.238407
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    class TestModule:
        def __init__(self, *args):
            self.runs = []
            self.run_responses = []

        def get_bin_path(self, name):
            return '.'

        def run_command(self, command):
            self.runs.append(command)
            return self.run_responses.pop(0)

    class TestModuleNoVirtInfo(TestModule):
        def __init__(self, *args):
            TestModule.__init__(self, *args)

        def get_bin_path(self, name):
            if name == 'virtinfo':
                return None
            return TestModule.get_bin_path(self, name)

    class TestModuleNoSmbios(TestModule):
        def __init__(self, *args):
            TestModule.__

# Generated at 2022-06-13 04:21:48.062863
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Imports
    import os
    from ansible.module_utils.facts.virtual.sunos.SunOSVirtual import SunOSVirtual
    # Mocks
    class MockModule():
        def run_command(self, cmd):
            if cmd == "zonename":
                if os.path.isdir('/.SUNWnative'):
                    return 0, "foo", ""
                else:
                    return 0, "global", ""
            if cmd == "virtinfo -p":
                if os.path.isdir('/.SUNWnative'):
                    return 0, "", ""
                else:
                    return 0, "DOMAINROLE|impl=LDoms|control=true|io=false|service=false|root=false", ""

# Generated at 2022-06-13 04:22:08.448858
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    loader, inventory, _variable_manager = init_module_arguments()
    host_vars = SunOSVirtual(loader=loader, variables=inventory._hosts["localhost"]).get_virtual_facts()
    assert host_vars['container'] == 'zone'
    assert host_vars['virtualization_type'] == 'vmware'
    assert host_vars['virtualization_role'] == 'guest'
    assert host_vars['virtualization_tech_guest'] == {'vmware', 'zone'}
    assert host_vars['virtualization_tech_host'] == {'zone'}

# Generated at 2022-06-13 04:22:11.528946
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos_virt_obj = SunOSVirtual(None)
    assert isinstance(sunos_virt_obj, SunOSVirtual)
    assert sunos_virt_obj.platform == 'SunOS'


# Generated at 2022-06-13 04:22:12.420572
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:22:14.314726
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = SunOSVirtual(dict())
    assert module.platform == 'SunOS'


# Generated at 2022-06-13 04:22:25.191747
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, cmd):
            return 'fake_bin_path'

        def run_command(self, cmd):
            if cmd == 'fake_bin_path':
                return 0, 'fake_command_output', ''
        def fail_json(self, *args, **kwargs): pass

    class MockSys(object):
        def __init__(self, platform='SunOS'):
            self.platform = platform

    class MockOS(object):
        def __init__(self, path=None):
            if path:
                self.path = path
            else:
                self.path = MockOSpath()


# Generated at 2022-06-13 04:22:27.326214
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    '''
    Unit test of SunOSVirtualCollector.
    '''
    facts = {}
    module = type('MockAnsibleModule', (object,), {'ansible_facts': facts, 'fail_json': Mock()})()
    SunOSVirtualCollector(module)

# Generated at 2022-06-13 04:22:32.026853
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector()
    assert isinstance(obj, VirtualCollector)
    assert obj._fact_class is SunOSVirtual
    assert obj._platform is 'SunOS'

# Generated at 2022-06-13 04:22:33.481535
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({})


# Generated at 2022-06-13 04:22:37.011563
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module = DummyModule()
    virtual_collector = SunOSVirtualCollector(module)
    assert virtual_collector._fact_class.platform == 'SunOS'

# Unit tests of class SunOSVirtual


# Generated at 2022-06-13 04:22:40.570408
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()
    assert virtual_collector.platform == 'SunOS'
    assert virtual_collector._fact_class == SunOSVirtual
    assert virtual_collector._platform == 'SunOS'


# Generated at 2022-06-13 04:23:11.609798
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    '''
    Unit test for method get_virtual_facts of class SunOSVirtual
    '''
    # Test 1: global zone
    with open('/proc/cpuinfo', 'r') as cpuinfo:
        proc_cpuinfo = cpuinfo.read()
    with open('/proc/meminfo', 'r') as meminfo:
        proc_meminfo = meminfo.read()
    module = type('module', (object,), {})()
    try:
        module.run_command = lambda cmd: (0, '/tmp', '')
    except AttributeError:
        def run_command(cmd):
            return (0, '/tmp', '')
    module.get_bin_path = lambda cmd: '/usr/sbin/' + cmd
    module.run_command = run_command

# Generated at 2022-06-13 04:23:19.873355
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = DummyAnsibleModule()
    SunOSVirtual_instance = SunOSVirtual(module)
    SunOSVirtual_instance.module.run_command = DummyRunCommand()
    SunOSVirtual_instance.module.get_bin_path = DummyGetBinPath()
    SunOSVirtual_instance.module.run_command.set_output({'/usr/sbin/virtinfo -p': """DOMAINROLE|impl=LDoms|control=true|io=false|service=false|root=false
"""})

    SunOSVirtual_instance.get_virtual_facts()
    assert SunOSVirtual_instance.facts['virtualization_type'] == 'ldom'
    assert 'guest' in SunOSVirtual_instance.facts['virtualization_role']

# Generated at 2022-06-13 04:23:21.814327
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual(dict())
    assert virtual_facts is not None


# Generated at 2022-06-13 04:23:33.304935
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create a mock module
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    module = MockModule()
    mod = SunOSVirtual(module)
    # Test in a zone
    mod.module.run_command = Mock(return_value=(0, "global", ""))
    mod.module.get_bin_path = Mock(return_value="/usr/bin/zonename")
    mod.module.os.path.isdir = Mock(return_value=False)
    mod.module.os.path.exists = Mock(return_value=False)
    mod.module.get_bin_path = Mock(return_value=False)

# Generated at 2022-06-13 04:23:34.380569
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunosv = SunOSVirtualCollector()
    assert sunosv is not None

# Generated at 2022-06-13 04:23:37.850349
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()

    assert x.__class__.__name__ == 'SunOSVirtualCollector'
    assert x._fact_class.__name__ == 'SunOSVirtual'
    assert x._platform == 'SunOS'

# Generated at 2022-06-13 04:23:40.522242
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeModule()
    sunos_virtual = SunOSVirtual(module)
    assert sunos_virtual.platform == 'SunOS'
    assert sunos_virtual.module == module

# Generated at 2022-06-13 04:23:42.624471
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    if os.name == 'nt':
        raise unittest.SkipTest("Only applicable to posix systems")
    si = SunOSVirtualCollector()
    assert si is not None

# Generated at 2022-06-13 04:23:43.468397
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:23:44.765445
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt = SunOSVirtual(None)
    assert virt.platform == 'SunOS'

# Generated at 2022-06-13 04:24:43.023985
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import platform
    import unittest

    if platform.system() != 'SunOS':
        raise unittest.SkipTest('Test applies to SunOS only')

    class Module(object):

        def __init__(self):
            self.facts = {}

        def run_command(self, command):
            test_index = 0

# Generated at 2022-06-13 04:24:45.461279
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    s = SunOSVirtual(None)
    assert s.platform == 'SunOS'



# Generated at 2022-06-13 04:24:55.388256
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import SunOSVirtual
    module = AnsibleModule(
        argument_spec=dict()
    )
    SunOSVirtual.module = module
    SunOSVirtual.module.run_command = lambda *_, **kwargs: (0, '', '')
    SunOSVirtual.module.get_bin_path = lambda *_, **kwargs: '/sbin/zonename'

    # When fact gathering is called, we should have the following facts:
    #   virtualization_tech_guest is set to set()
    #   virtualization_tech_host is set to {'zone'}
    #   virtualization_type is set to None
    #   virtualization_role is set to None


# Generated at 2022-06-13 04:24:57.713177
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.platform == "SunOS"
    assert collector.fact_class == SunOSVirtual

# Generated at 2022-06-13 04:25:04.789796
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    v = SunOSVirtual({})
    v.module = MockModule()
    facts = v.get_virtual_facts()
    assert facts['virtualization_tech_host'] == set()
    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_type'] is None
    assert facts['virtualization_role'] is None
    assert facts['container'] is None

    v.module.run_command.return_value = (0, 'foo', '')
    facts = v.get_virtual_facts()
    assert facts['container'] == 'zone'
    assert facts['virtualization_type'] == 'vmware'
    assert facts['virtualization_role'] == 'guest'

    v.module.run_command.return_value = (1, '', '')
    facts = v.get_virtual_

# Generated at 2022-06-13 04:25:06.020199
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Nothing to test here.
    pass

# Generated at 2022-06-13 04:25:09.528017
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    y = x.collect()
    assert y.keys() == ['virtualization_tech_guest', 'virtualization_tech_host', 'virtualization_type',
                        'virtualization_role', 'container']

# Generated at 2022-06-13 04:25:11.791193
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c=SunOSVirtualCollector()
    assert c._platform == 'SunOS'
    assert isinstance(c._fact_class, SunOSVirtual)

# Generated at 2022-06-13 04:25:13.809216
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    mud = SunOSVirtual(dict())
    assert mud is not None


# Generated at 2022-06-13 04:25:25.530191
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    SunOSVirtual.get_virtual_facts(module)

    assert 'virtualization_type' in module.exit_json['ansible_facts']['virtualization']
    assert module.exit_json['ansible_facts']['virtualization']['virtualization_type'] is not None

    assert 'virtualization_role' in module.exit_json['ansible_facts']['virtualization']
    assert module.exit_json['ansible_facts']['virtualization']['virtualization_role'] is not None

    assert 'virtualization_tech_host' in module.exit_json['ansible_facts']['virtualization']
    assert module.exit_json['ansible_facts']['virtualization']['virtualization_tech_host'] is not None


# Generated at 2022-06-13 04:27:19.171970
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """Basic Unit test for SunOSVirtual"""
    class DummyModule(object):
        def __init__(self):
            self.run_command = lambda x: None
            self.get_bin_path = lambda x: x
            self.exit_json = lambda x: None

    print("Testing class constructor")
    obj = SunOSVirtual(DummyModule())
    assert(obj.virtualization_type == "")
    assert(obj.virtualization_role == "")
    assert(obj.virtualization_tech_guest == set())
    assert(obj.virtualization_tech_host == set())

# Generated at 2022-06-13 04:27:20.245773
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    o = SunOSVirtualCollector()
    assert o.platform == 'SunOS'

# Generated at 2022-06-13 04:27:30.177058
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test on an OpenSolaris zone
    module = FakeModule({
        "zone_name": "ansible",
        "zone_path": "/export/zones/ansible",
        "zone_uuid": "e7e44977-86e9-9776-bf8c-7a41a2d962d7",
        "zone_brand": "joyent",
        "zone_state": "installed",
        "zone_ip": "10.10.3.51",
        "zone_status": "running",
        "zone_status_changed": "2014-11-14T14:53:54.853945Z",
        "zone_boot": "2014-11-14T14:53:54.853945Z",
        "zone_bootargs": ""
    })

# Generated at 2022-06-13 04:27:33.216064
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    '''
    This is a test function to ensure that the constructor of the class
    SunOSVirtualCollector works properly
    '''
    virtual_collector = SunOSVirtualCollector()
    assert isinstance(virtual_collector._fact_class, SunOSVirtual)

# Generated at 2022-06-13 04:27:37.466820
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x._platform == 'SunOS'
    assert x._fact_class == SunOSVirtual
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:27:45.889964
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create a mini module object
    class MyModule(object):
        def __init__(self):
            self.run_command = lambda x: (0, "", "")
            self.params = {}

    class SunOSVirtualModule(SunOSVirtual):
        def __init__(self):
            self.module = MyModule()

    def myrun_command(cmd):
        if cmd == "zonename":
            return True, "global", ""
        elif cmd == "/usr/sbin/virtinfo -p":
            return True, "DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false", ""
        elif cmd == "virtinfo":
            return True, "", "virtinfo can only be run from the global zone"

# Generated at 2022-06-13 04:27:49.172709
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.platform == 'SunOS'
    assert collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:27:50.460983
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert isinstance(SunOSVirtualCollector(), SunOSVirtualCollector)


# Generated at 2022-06-13 04:27:52.593086
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 04:27:56.476750
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = type('MockModule', (object,), {'run_command': lambda x: (0, "", "")})()
    module.get_bin_path = lambda s: '/usr/bin/%s' % s
    v = SunOSVirtual(module)
    assert v.get_virtual_facts() == {}