

# Generated at 2022-06-13 04:20:37.591889
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # No need to test. This class is just a wrapper class of class Virtual.
    # The test cases for class Virtual are enough.
    pass

# Generated at 2022-06-13 04:20:40.330087
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    my_test_virtual = SunOSVirtualCollector()
    assert my_test_virtual._fact_class.platform == 'SunOS'
    assert my_test_virtual._platform == 'SunOS'

# Generated at 2022-06-13 04:20:50.336441
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleMock()

    zone_files_dir = {}
    zone_files_dir['exist'] = SunOSVirtual(module)
    zone_files_dir['exist'].get_bin_path = return_value_true('/bin/zonename')
    zone_files_dir['exist'].run_command = return_value_true('global','','',0)
    zone_files_dir['exist'].os.path.isdir = return_value_true(True)

    zone_files_dir['not_exist'] = SunOSVirtual(module)
    zone_files_dir['not_exist'].get_bin_path = return_value_true('/bin/zonename')
    zone_files_dir['not_exist'].run_command = return_value_true('global','','',0)
    zone

# Generated at 2022-06-13 04:20:54.091434
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    vm = SunOSVirtual(module)
    fake_out = {'container': 'zone',
                'virtualization_role': 'guest',
                'virtualiation_type': 'vmware'}

    assert vm.get_virtual_facts() == fake_out
    del module


# Generated at 2022-06-13 04:21:05.630729
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.virtual import SunOSVirtual
    import os
    import shutil
    import tempfile

    # We use a temporary directory and this function to create a temporary directory
    # and return the path of that temporary directory.
    temp_dir = tempfile.mkdtemp()

    # We create our SunOSVirtual object
    m = SunOSVirtual(module=None)

    # We build a temporary directory
    test_root_dir = tempfile.mkdtemp(dir=temp_dir)

    # We mock some methods of our SunOSVirtual object
    m.get_bin_path = lambda x: os.path.join(test_root_dir, 'usr', 'bin', x)

# Generated at 2022-06-13 04:21:16.038149
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:21:26.968681
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual.test.test_get_virtual_facts import TestGetVirtualFacts, FakeModule

    sysinfo_dict = {
        'System Model:': 'Oracle Corporation SUN FIRE X2270 SERVER',
        'System Serial Number:': '',
        'BIOS Configuration:': '',
        'Language:': 'en',
        'domain': '',
        'Current Processor Clock Speed:': '2533 MHz',
        'Detected Processor Clock Speed:': '2533 MHz',
        'Memory Size:': '36664 Megabytes'
    }
    sysinfo_string = '\n'.join(['%s %s' % (k, v) for k, v in sysinfo_dict.items()])

    test

# Generated at 2022-06-13 04:21:36.013847
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Note: For this unittest to run, you must have a working zone configuration on your system.
    Or in other words, this test will fail if you don't have a global zone and at least one non-global zone.
    """

    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.facts import collect_facts
    import ansible.module_utils.facts.virtual.sunos as sunos_virtual

    test_module = collect_facts.AnsibleModuleMock({})

    # Inject our test output
    # For this unittest to run, you must have a working zone configuration on your system.
    # Or in other words, this test will fail if you don't have a global zone and at least one non-global zone.

# Generated at 2022-06-13 04:21:38.488679
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc  # will raise exception if initialization fails

# Generated at 2022-06-13 04:21:50.217286
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts import collector
    import sys
    import os
    import inspect
    # class VirtualCollector requires the name of the class
    fq_name = VirtualCollector.__module__ + '.' + VirtualCollector.__name__

    # create a collector with a name and parent Collector
    c = SunOSVirtualCollector("test_name", "test_parent")
    assert c.name == "test_name"
    assert c.platform == sys.platform

    # Search for the fact class of the collector
    fq_fact_class_name = c._fact_class.__module__ + '.' + c._fact_class.__name__

    # Show that the fact class is of the right type
    assert inspect.isclass(c._fact_class)

# Generated at 2022-06-13 04:22:13.334603
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """ SunOSVirtual.get_virtual_facts() Unit Test """

    from ansible.module_utils.facts.virtual.sunost import SunOSVirtual
    from ansible.module_utils.basic import AnsibleModule

    class MockModule:
        def __init__(self, run_command_args=None, run_command_rc=None):
            self.run_command_args = run_command_args
            self.run_command_rc = run_command_rc
            self.params = {'gather_subset': ['!all', 'virtual']}

        def get_bin_path(self, arg):
            if arg == 'zonename':
                return '/usr/bin/zonename'
            else:
                return None

        @staticmethod
        def fail_json(msg):
            raise Exception(msg)


# Generated at 2022-06-13 04:22:17.343096
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    import os
    from ansible.module_utils.facts.virtual import SunOSVirtual
    from ansible.module_utils.facts.collector import BaseFactCollector

# Generated at 2022-06-13 04:22:26.901829
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # It will be represented as a "global" zone on a machine that is itself virtualized.
    # We should be able to detect its virtualization technology (e.g. vmware or virtualbox) without false positives
    zonename_out = "global"
    zonename_rc = 0
    modinfo_out = "modinfo: module 'sffwdc' is not in '/etc/driver_aliases'"
    modinfo_rc = 0
    vitinfo_out = "DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false"
    virtinfo_rc = 0
    smbios_out = ''
    smbios_rc = 0

    # Initialize a dummy module
    module = AnsibleModule(argument_spec={})

    # Create a dummy module class for module_utils.

# Generated at 2022-06-13 04:22:28.318975
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual = SunOSVirtualCollector()
    assert virtual.platform == 'SunOS'
    assert isinstance(virtual.get_virtual_facts(), dict)

# Generated at 2022-06-13 04:22:31.693649
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual(dict(module=None)).get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'xen'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['container'] == 'zone'
    assert virtual_facts['virtualization_tech_guest'] == {u'xen', u'zone'}
    assert virtual_facts['virtualization_tech_host'] == {u'vmware', u'zone'}

# Generated at 2022-06-13 04:22:37.220472
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():

    # construct an object of the SunOSVirtual class
    sunos_virtual_obj = SunOSVirtual(module=None)

    # check if the object is an instance of SunOSVirtual
    assert isinstance(sunos_virtual_obj, SunOSVirtual)

    # check the value of 'platform'
    assert sunos_virtual_obj.platform == 'SunOS'



# Generated at 2022-06-13 04:22:48.223130
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector
    from ansible.module_utils.facts.virtual import VirtualFactCollector
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 04:22:51.721238
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Call the constructor unittest for the class SunOSVirtualCollector
    sunOSVirtualCollector = SunOSVirtualCollector()
    assert sunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:22:56.473888
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeModule({})
    result = SunOSVirtual(module).get_virtual_facts()

    assert "virtualization_type" in result
    assert "virtualization_role" in result
    assert "container" in result
    assert "virtualization_tech_host" in result
    assert "virtualization_tech_guest" in result

# Generated at 2022-06-13 04:23:04.425299
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = type('', (), {'run_command': fake_run_command, 'get_bin_path': fake_get_bin_path})
    class FakeSunOSVirtual():
        platform = 'SunOS'
        module = module
    sunos_virtual = FakeSunOSVirtual()
    # Test on a physical SunOS machine
    sunos_virtual.module.run_command.return_value = (0, '', '')
    assert sunos_virtual.get_virtual_facts() == {}
    # Test on a virtual SunOS machine
    sunos_virtual.module.run_command.side_effect = [
        (0, 'zone', ''),
        (0, 'VMware', ''),
    ]
    sunos_virtual.module.get_bin_path.return_value = '/usr/sbin/'
    assert sun

# Generated at 2022-06-13 04:23:38.132764
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    data_mock_zones = """
ID  NAME           STATUS  PATH                                                 BRAND  IP         NICTAGS
0   global         running /                                                     -      -          -
1   jenkins-slave  running /zones/jenkins-slave                                  -      -          -
"""

    module_mock = type('module', (object, ), {
        'run_command': classmethod(lambda cls, command: (0, data_mock_zones, ''))
    })


# Generated at 2022-06-13 04:23:40.833128
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc._platform == 'SunOS'
    assert issubclass(vc._fact_class, SunOSVirtual)

# Generated at 2022-06-13 04:23:41.684253
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:23:49.332320
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = MagicMock(return_value=('0', '', ''))
    module.get_bin_path = MagicMock(return_value='')
    module.read_file = MagicMock(return_value=' ')
    module.stat = MagicMock(return_value=' ')
    module.os_path = MagicMock(return_value=())
    module.isdir = MagicMock(return_value=False)

    # 1. Return from all the above mocked methods are empty and zonename does not return 0
    # Expected result: verified dict has no fields.
    virtual = SunOSVirtual(module=module)
    result = virtual.get_virtual_facts()
    assert(len(result) == 0)

    # 2. Return from mocked function

# Generated at 2022-06-13 04:23:51.767799
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()
    assert virtual_collector.platform == 'SunOS'

    # Test for the fact class attribute
    assert virtual_collector.fact_class == SunOSVirtual

# Generated at 2022-06-13 04:23:55.892087
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():

    # Test empty class
    sv = SunOSVirtual({})
    assert sv.data == {}
    assert 'virtualization_type' not in sv.data
    assert 'virtualization_role' not in sv.data
    assert 'virtualization_tech_guest' not in sv.data
    assert 'virtualization_tech_host' not in sv.data

# Generated at 2022-06-13 04:23:57.347574
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc.platform == vc._platform
    assert vc._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:24:00.059824
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual()
    virtual_facts.get_virtual_facts()
    assert virtual_facts.get_virtual_facts()['virtualization_type'] == 'kvm'
    assert virtual_facts.get_virtual_facts()['virtualization_role'] == 'guest'

# Generated at 2022-06-13 04:24:10.913776
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = MagicMock()

    modinfo = '/usr/sbin/modinfo'
    zonename = '/usr/sbin/zonename'
    virtinfo = '/usr/sbin/virtinfo'
    smbios = '/usr/sbin/smbios'

    module.get_bin_path.side_effect = lambda x: {
        'modinfo': modinfo,
        'zonename': zonename,
        'virtinfo': virtinfo,
        'smbios': smbios
    }.get(x)


# Generated at 2022-06-13 04:24:12.240271
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vm = SunOSVirtualCollector()
    assert SunOSVirtualCollector._fact_class == SunOSVirtual
    assert SunOSVirtualCollector._platform == 'SunOS'


# Generated at 2022-06-13 04:25:05.016699
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Because we're mocking out the module and running
    # We're not running on a real target.  So this
    # test case will only test that get_virtual_facts
    # generates a dict that has the right keys.
    #
    # TODO: add a unit test where the is_zone() method
    # returns True.
    #
    # TODO: add a unit test where the is_brand_zone()
    # method returns True.
    #
    # TODO: add a unit test where the is_vz() method
    # returns True.
    #
    # TODO: add a unit test where the is_linux_vserver()
    # method returns True.
    #
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ModuleFacts

# Generated at 2022-06-13 04:25:06.955257
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    facts, _warnings = SunOSVirtualCollector.collect()
    assert 'virtual' in facts

# Generated at 2022-06-13 04:25:18.218906
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual import Virtual
    from ansible.module_utils._text import to_bytes

    class MockModule:
        def __init__(self, return_values):
            self.params = {}
            self.return_values = return_values
            self.fail_json = lambda *args, **kwargs: self
            self.exit_json = lambda *args, **kwargs: self

        def run_command(self, *args, **kwargs):
            if self.return_values['run_command']:
                return 0, 'run_command', ''
            self.fail_json(msg='unable to run command')


# Generated at 2022-06-13 04:25:19.948385
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()



# Generated at 2022-06-13 04:25:29.791434
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    import platform
    host_facts = {'ansible_facts': {'system': platform.system()}}
    virtual_collector = SunOSVirtualCollector()
    virtual_collector.collect(host_facts)
    assert host_facts['ansible_facts']['virtualization_tech_guest'] == set()
    assert host_facts['ansible_facts']['virtualization_tech_host'] == set()
    assert not host_facts['ansible_facts']['virtualization_type']
    assert not host_facts['ansible_facts']['virtualization_role']
    assert not host_facts['ansible_facts']['container']


# Generated at 2022-06-13 04:25:38.259468
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import os
    import tempfile
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    tmpdir = tempfile.mkdtemp()


# Generated at 2022-06-13 04:25:40.393981
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict(), dict())
    assert virtual._platform == 'SunOS'


# Generated at 2022-06-13 04:25:50.841871
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test zone
    module = FakeModule(dict(command=dict(exit_status=0, stdout='global'), file='/.SUNWzone'))
    virtual = SunOSVirtual(module)
    facts = virtual.get_virtual_facts()

    assert facts['virtualization_role'] == 'host'
    assert facts['virtualization_type'] == 'zone'
    assert 'container' not in facts

    module = FakeModule(dict(command=dict(exit_status=0, stdout='non-global'), file='/.SUNWzone'))
    virtual = SunOSVirtual(module)
    facts = virtual.get_virtual_facts()

    assert facts['virtualization_role'] == 'guest'
    assert facts['virtualization_type'] == 'zone'
    assert facts['container'] == 'zone'

    # Test branded zone

# Generated at 2022-06-13 04:25:52.614614
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()

    assert vc != None
    assert vc.fact_class._platform == 'SunOS'

# Generated at 2022-06-13 04:26:01.838811
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:27:46.578257
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeModule()
    s = SunOSVirtual(module)
    assert s.module == module
    assert s.platform == 'SunOS'



# Generated at 2022-06-13 04:27:55.240462
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    test_module = AnsibleModule(argument_spec={})
    test_SunOSVirtual = SunOSVirtual(module=test_module)
    virtual_facts = test_SunOSVirtual.get_virtual_facts()

    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

    assert isinstance(virtual_facts['virtualization_tech_guest'], set)
    assert isinstance(virtual_facts['virtualization_tech_host'], set)

# Generated at 2022-06-13 04:27:57.273811
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x.platform == 'SunOS'
    assert x._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 04:28:04.449621
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts import cached

    # create a proper instance of class SunOSVirtual
    virtual = SunOSVirtual()
    virtual.get_virtual_facts = SunOSVirtual.get_virtual_facts
    module_data = {"_ansible_virtual_facts": cached(virtual.get_virtual_facts)}

    # set zone which loads /sbin in path
    os.environ["PATH"] = "{}{}{}".format(os.environ["PATH"], os.pathsep, "/sbin")

    rc = 0
    environ = {}

    class ModuleTest(object):
        def __init__(self, data):
            self.params = {}
            self.run_command_calls = []


# Generated at 2022-06-13 04:28:15.063530
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.collector.sunos import SunOSVirtualCollector
    import sys

    module = ansible_facts

    # mock values for zonename
    def get_bin_path(name):
        if name == 'zonename':
            return '/bin/zonename'
        else:
            return None
    module.get_bin_path = get_bin_path
    def run_command(cmd):
        if cmd == '/bin/zonename':
            return (0, 'global', '')
        else:
            return (0, '', '')
    module.run_command = run_command

    # mock value for virtualization_type
   

# Generated at 2022-06-13 04:28:16.484352
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert issubclass(SunOSVirtualCollector._fact_class, Virtual)

# Generated at 2022-06-13 04:28:21.199940
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    # Mocking module.run_command
    class ModuleMock(object):
        def run_command(self, cmd):
            class CommandResult(object):
                pass
            result = CommandResult()
            if cmd == '/usr/bin/zonename':
                result.rc = 0
                result.stdout = 'global'
            elif cmd.startswith('/usr/sbin/modinfo'):
                result.rc = 0
                result.stdout = 'name: vmm'
            elif cmd.startswith('/usr/sbin/virtinfo'):
                result.rc = 1
                result.stdout = 'virtinfo can only be run from the global zone'
            return (result.rc, result.stdout, result.stderr)

# Generated at 2022-06-13 04:28:23.512887
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Call constructor of class SunOSVirtualCollector
    c = SunOSVirtualCollector()
    assert c._fact_class == SunOSVirtual
    assert c._platform == 'SunOS'

# Generated at 2022-06-13 04:28:32.741646
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    SunOSVirtualObject = SunOSVirtual(dict(ANSIBLE_MODULE_ARGS={}), dict(fact_only=False))
    SunOSVirtualObject.module.exit_json = lambda x: SunOSVirtualObject.sys_exit_json(x)
    SunOSVirtualObject.module.fail_json = lambda x: SunOSVirtualObject.sys_fail_json(x)
    SunOSVirtualObject.module.run_command = lambda cmd, check_rc=False: SunOSVirtualObject.sys_run_command(cmd)
    SunOSVirtualObject.module.get_bin_path = lambda cmd: SunOSVirtualObject.sys_get_bin_path(cmd)
    virtual_facts = SunOSVirtualObject.get_virtual_facts()
    print(virtual_facts)

# Generated at 2022-06-13 04:28:33.879545
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    os = SunOSVirtualCollector()
    assert os is not None