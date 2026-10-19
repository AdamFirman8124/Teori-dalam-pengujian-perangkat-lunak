

# Generated at 2022-06-13 04:20:46.812159
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    import sys
    import os
    import tempfile
    import json

    # Create module mock and setup AnsibleModule mock
    module_mock = basic.AnsibleModule(argument_spec={})
    module_mock.run_command = os.system
    module_mock.get_bin_path = os.path.basename

    # Create virtualization mock
    virtualization_mock = SunOSVirtual(module_mock)

    # Run the get_virtual_facts method with various cases
    def get_virtual_facts(zone, modinfo):
        # Create a temporary file to be used as the output of modinfo
        fd, modinfo_file = tempfile.mkstemp()
        os.write(fd, bytes(modinfo.encode('UTF-8')))
       

# Generated at 2022-06-13 04:20:55.186923
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = SunOSVirtual(dict())
    module.module.get_bin_path = lambda x: '/path/%s' % x
    module.module.run_command = lambda x: (0, '', '')
    module.os.path.exists = lambda x: False
    assert 'virtualization_type' not in module.get_virtual_facts()

    module.os.path.exists = \
        lambda x: True if x in ('/.SUNWnative', '/proc/vz') else False
    facts = module.get_virtual_facts()
    assert 'container' in facts
    assert facts['container'] == 'zone'
    assert 'virtualization_type' in facts
    assert facts['virtualization_type'] == 'virtuozzo'
    assert facts['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:21:00.788970
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Testing in a vmware guest
    module = FakeModule({})
    v = SunOSVirtual(module)
    virtual_facts = v.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'vmware'
    assert virtual_facts['virtualization_role'] == 'guest'
    # Testing in a virtualbox guest
    module = FakeModule({})
    v = SunOSVirtual(module)
    v.virtinfo = "VirtualBox\n"
    virtual_facts = v.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'
    # Testing in a global zone
    module = FakeModule({})
    v = SunOSVirtual(module)

# Generated at 2022-06-13 04:21:07.011346
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = DummyModule()
    facts = SunOSVirtual(module).get_virtual_facts()
    assert facts == {'virtualization_role': 'guest',
        'virtualization_type': 'xen',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
        'container': 'zone'}

# Generated at 2022-06-13 04:21:17.905204
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    mocker = MockRunner(failed=False, rc=0, stdout="", stderr="")
    mocker.add_command(command="/usr/sbin/zonename", stdout="global\n")

# Generated at 2022-06-13 04:21:19.659056
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    SunOSVirtual(dict())

# Generated at 2022-06-13 04:21:29.621951
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    class Module():
        def get_bin_path(self, filename):
            return '/usr/sbin/' + filename
        def run_command(self, command):
            if command.endswith('/usr/sbin/zonename'):
                if command == '/usr/sbin/zonename':
                    return 0, 'non-global', ''
                elif command == '/usr/sbin/zonename global':
                    return 0, 'global', ''
            elif command.endswith('/usr/sbin/modinfo'):
                return 0, '3 fffffff004fb3070 5 1 vmm rtld 64 \tVMware Virtual CPU version', ''

# Generated at 2022-06-13 04:21:33.263807
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    v = SunOSVirtualCollector()
    assert 'SunOS' == v._platform
    assert 'SunOSVirtual' == v._fact_class.__name__
    assert 'ansible.module_utils.facts.virt.solaris.solaris_virtual' == v._fact_class.__module__

# Generated at 2022-06-13 04:21:40.153305
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:21:45.262002
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector(None)

    # Test if we got valid object
    assert isinstance(vc, SunOSVirtualCollector)

    # Test if our class has platform 'SunOS'
    assert vc._platform == 'SunOS'

# Generated at 2022-06-13 04:22:01.806927
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = open('/dev/null', 'w')
    module.get_bin_path = lambda x: x
    module.run_command = lambda x: (0, '', '')
    os.listdir = lambda x: []
    os.access = lambda x, y: True
    m = SunOSVirtual(module)
    m.get_virtual_facts()

# Generated at 2022-06-13 04:22:03.728425
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """
    Constructor of class SunOSVirtualCollector
    """
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:22:07.746880
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    fc = SunOSVirtualCollector()
    assert fc.platform == 'SunOS'
    assert fc.fact_class == SunOSVirtual
    assert fc.collector == SunOSVirtualCollector
    assert fc.virtual_facts is None


# Generated at 2022-06-13 04:22:09.623367
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict())
    assert virtual.platform == 'SunOS'


# Generated at 2022-06-13 04:22:12.126005
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc._fact_class == SunOSVirtual
    assert vc._platform == 'SunOS'


# Generated at 2022-06-13 04:22:23.327991
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    This function returns the unit test for method get_virtual_facts of class
    SunOSVirtual.
    """
    file_find = "/bin/find"
    file_smbios = "/usr/sbin/smbios"
    file_zonename = "/usr/bin/zonename"
    file_virtinfo = "/usr/sbin/virtinfo"
    file_modinfo = "/usr/sbin/modinfo"
    file_pkginfo = "/usr/bin/pkginfo"
    path_sys_devices_virtual_net = "/sys/devices/virtual/net"
    path_usr_lib_brand = "/usr/lib/brand"
    path_dev_zfs = "/dev/zfs"
    path_proc_vz = "/proc/vz"


# Generated at 2022-06-13 04:22:25.274146
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector()._fact_class is SunOSVirtual
    assert SunOSVirtualCollector()._platform == 'SunOS'

# Generated at 2022-06-13 04:22:26.023860
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector()
    assert obj.platform == 'SunOS'

# Generated at 2022-06-13 04:22:26.911218
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    v = SunOSVirtualCollector()
    assert v.get_virtual_facts() is None

# Generated at 2022-06-13 04:22:29.969616
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos_virtual = SunOSVirtual(dict())
    assert sunos_virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:23:02.324843
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.virtual import SunOSVirtual
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector

    # Create the Virtual Collector
    collector = SunOSVirtualCollector()

    # Create a fake AnsibleModule
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils._text import to_bytes
    import ansible.module_utils.facts.virtual.sunos
    _module, _exit_json, _fail_json = ansible.module_utils.facts.virtual.sunos.get_module_args()

    # Create a fake module
    class FakeModule(object):
        def __init__(self, exit_json, fail_json):
            self.exit_json

# Generated at 2022-06-13 04:23:04.276990
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.get_virtual_facts() == {}



# Generated at 2022-06-13 04:23:07.347521
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # set up test variables
    facts = {}
    facts['kernel'] = 'SunOS'

    # set up test object, run method and verify results
    o = SunOSVirtual(None)
    o.collect_facts(facts)

# Generated at 2022-06-13 04:23:17.325717
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:23:19.088530
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict())
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:23:22.132310
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    facts = SunOSVirtualCollector().collect(None, None)
    for fact in facts.keys():
        assert fact == 'virtualization_tech_guest' or fact == 'virtualization_tech_host'


# Generated at 2022-06-13 04:23:28.483005
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    V = SunOSVirtual({})
    assert V.get_virtual_facts() == { 'virtualization_type': 'xen',
                                      'virtualization_role': 'host (control,io,service,root)',
                                      'container': None,
                                      'virtualization_tech_host': set(['zone', 'ldom']),
                                      'virtualization_tech_guest': set(['zone', 'ldom', 'xen']) }

# Generated at 2022-06-13 04:23:35.930178
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ["!all", "!min"]
            self.exit_json = lambda v, **kargs: None
            self.run_command = lambda **kwargs: (0, "", "")
            self.get_bin_path = lambda **kwargs: "/usr/sbin/virtinfo"

    module = MockModule()

    if SunOSVirtualCollector.detect(module):
        vc = SunOSVirtualCollector(module)
        vc.collect()

# Generated at 2022-06-13 04:23:39.362450
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeAnsibleModule()
    virtual = SunOSVirtual(module)
    assert virtual.platform == 'SunOS'
    assert virtual.zonebin == "/usr/sbin/zonename"


# Generated at 2022-06-13 04:23:50.077021
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    to_patch_paths = ['os.path.isdir', 'os.path.exists']
    to_patch_commands = [
        ('/usr/sbin/zonename', ('global', '', 0), 1),
        ('/usr/sbin/modinfo', ('VMWare', 'VirtualBox', ''), 1),
        ('/usr/sbin/virtinfo -p', ('', '', 1), 0),
        ('/usr/sbin/smbios', ('VMWare', 'Parallels', 'VirtualBox', 'HVM domU', 'KVM'), 1),
    ]

# Generated at 2022-06-13 04:24:41.400826
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    vc = SunOSVirtualCollector()
    assert vc.platform == "SunOS"
    assert vc.fact_class == SunOSVirtual
    assert vc._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:24:43.737624
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual
    instance = SunOSVirtualCollector()
    assert isinstance(instance, SunOSVirtualCollector)

# Generated at 2022-06-13 04:24:49.012311
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Instantiate a SunOSVirtualCollector object
    sunos_vi_collector = SunOSVirtualCollector()

    # Test _fact_class
    assert sunos_vi_collector._fact_class == SunOSVirtual, "_fact_class must be equal to SunOSVirtual"
    # Test _platform
    assert sunos_vi_collector._platform == 'SunOS', "_platform must be equal to 'SunOS'"

# Generated at 2022-06-13 04:24:59.122722
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    # Construct a mock module
    import ansible.module_utils.facts.virtual.sunos.module_utils.module_base
    class MockModule(ansible.module_utils.facts.virtual.sunos.module_utils.module_base.AnsibleModule):
        pass
    mock_module = MockModule(argument_spec={}, supports_check_mode=True)

    # Construct a mock ansible module
    import ansible.module_utils.facts.virtual.sunos.ansible_module_utils.facts.base
    class MockFactsModule(ansible.module_utils.facts.virtual.sunos.ansible_module_utils.facts.base.AnsibleFactsBase):
        pass
    mock_module.ansible_module_facts = MockFactsModule(mock_module, {})

    # Construct a mock module

# Generated at 2022-06-13 04:25:02.496991
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Parameters
    module_args = {}

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # Create the class object
    test_class = SunOSVirtual(module)

    assert test_class.platform == 'SunOS'
    assert test_class.module == module

# Generated at 2022-06-13 04:25:04.967947
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert issubclass(SunOSVirtualCollector, VirtualCollector)
    flag = False
    for val in SunOSVirtualCollector.__dict__.values():
        if isinstance(val, property):
            flag = True
            break
    assert flag == True
    assert SunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:25:07.268678
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos.get_virtual_facts import SunOSVirtual
    v = SunOSVirtual()
    v._module = {
        "get_bin_path": lambda x: x,
        "run_command": lambda x: (0, "", ""),
    }
    v.get_virtual_facts()



# Generated at 2022-06-13 04:25:18.306045
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleStub()
    v = SunOSVirtual(module)
    # check when command zonename exists
    # and we are in a non global zone
    module.run_command = RunCommandStub("zonename",
            0, "non-global", "")
    assert isinstance(v.get_virtual_facts(), dict)
    assert 'virtualization_role' in v.get_virtual_facts()
    assert v.get_virtual_facts()['virtualization_role'] == 'guest'
    assert 'virtualization_type' in v.get_virtual_facts()
    assert v.get_virtual_facts()['virtualization_type'] == 'zone'
    assert 'container' in v.get_virtual_facts()
    assert v.get_virtual_facts()['container'] == 'zone'
    # check

# Generated at 2022-06-13 04:25:30.281555
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Set up
    class ModuleStub(object):
        def __init__(self):
            pass
        def get_bin_path(self, arg):
            paths = {
                'zonename': '/usr/sbin/zonename',
                'virtinfo': '/usr/sbin/virtinfo',
                'smbios': '/usr/sbin/smbios',
                'modinfo': '/usr/sbin/modinfo',
            }
            return paths.get(arg, None)
        def run_command(self, cmd):
            output = ''
            if cmd == '/usr/sbin/zonename':
                # it's a zone
                retcode = 0
            elif cmd == '/.SUNWnative':
                # it's a branded zone
                retcode = 0

# Generated at 2022-06-13 04:25:32.381090
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert isinstance(VirtualCollector._platform_to_fact_class_mapping['SunOS'](), SunOSVirtual)

# Generated at 2022-06-13 04:27:21.448877
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec={}
    )
    module.exit_json = exit_json
    set_module_args(dict())
    pc = SunOSVirtual(module)
    # create fake file to test vz case
    with mock.patch('os.path.exists') as m:
        m.return_value = False
        virtual_facts = pc.get_virtual_facts()
    # check that container is not set on non-zone system
    assert 'container' not in virtual_facts
    # check that virtualization_type is not set on non-zone system
    assert 'virtualization_type' not in virtual_facts
    # check that virtualization_role is not set on non-zone system
    assert 'virtualization_role' not in virtual_facts
    # check that virtualization_tech_guest is

# Generated at 2022-06-13 04:27:31.444331
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import os
    import sys
    import re
    import imp
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from module_utils.facts.system.distribution import DistributionFactCollector
    from module_utils.facts.virtual import SolarisVirtual
    from ansible.module_utils.facts.system import distribution as distribution_module

    class SunOSVirtual_test(SunOSVirtual):
        def __init__(self, module):
            SunOSVirtual.__init__(self, module)


# Generated at 2022-06-13 04:27:33.142445
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    v = SunOSVirtualCollector()
    assert v.platform == 'SunOS'
    assert v._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:27:35.713865
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)


# Generated at 2022-06-13 04:27:37.339623
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    v = SunOSVirtualCollector()
    assert v


# Generated at 2022-06-13 04:27:40.729974
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    my_virtual_collector = SunOSVirtualCollector()
    assert my_virtual_collector.platform == 'SunOS'
    assert my_virtual_collector.fact_class == SunOSVirtual
    assert my_virtual_collector.fact_subclass == 'virtual'


# Generated at 2022-06-13 04:27:41.897461
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    vr = SunOSVirtual(None)
    assert vr.platform == 'SunOS'

# Generated at 2022-06-13 04:27:48.558415
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """ Test that the get_virtual_facts method of the SunOSVirtual class
        returns the correct virtual facts
    """
    class MockModule:
        def run_command(self, command):
            if command == "/usr/bin/zonename":
                return 0, "global", ""

# Generated at 2022-06-13 04:27:58.409475
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = MagicMock()
    module.run_command.side_effect = [
        (0, 'global', ''),
        (0, 'vmware', ''),
        (0, 'VirtualBox', ''),
        (0, 'ESXi', ''),
        (0, 'VMware', ''),
    ]
    module.get_bin_path.side_effect = [
        '/usr/sbin/zonename',
        '/usr/sbin/modinfo',
        '/usr/sbin/virtinfo',
        '/usr/sbin/smbios'
    ]
    module.params = {'gather_subset': '!all'}
    module.config = {'gather_subset': '!all'}
    module.run_command = MagicMock()

    # First test
    sunos

# Generated at 2022-06-13 04:27:59.888288
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual({}, None)
    assert isinstance(facts, SunOSVirtual)
