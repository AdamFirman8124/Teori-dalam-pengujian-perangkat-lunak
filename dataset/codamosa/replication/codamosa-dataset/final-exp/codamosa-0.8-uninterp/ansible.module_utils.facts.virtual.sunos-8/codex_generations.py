

# Generated at 2022-06-13 04:20:37.966452
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # TODO: implement this unit test
    pass

# Generated at 2022-06-13 04:20:47.674418
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test environment without virtualization technology
    tmp_env1 = [
        'RC=1',
        'OUT=',
        'ERR=cannot open: No such file or directory',
    ]
    results1 = {
        'virtualization_tech_guest': set(),
        'virtualization_tech_host': set(),
    }
    # Test environment with zone based virtualization technology
    tmp_env2 = [
        'RC=0',
        'OUT=global\n',
        'ERR=',
    ]
    results2 = {
        'container': 'zone',
        'virtualization_tech_guest': {'zone'},
        'virtualization_tech_host': set(),
    }
    # Test environment with branded zone based virtualization technology

# Generated at 2022-06-13 04:20:49.375966
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual(None)
    assert virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:20:52.057114
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual({})
    assert SunOSVirtual.platform == 'SunOS'
    assert facts.get_virtual_facts() == {}
    assert facts.platform == 'SunOS'


# Generated at 2022-06-13 04:20:55.254567
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos = SunOSVirtual()
    assert sunos.platform == 'SunOS'
    assert sunos.virtualization_type == ''
    assert sunos.virtualization_role == ''
    assert sunos.container == ''
    assert sunos.virtualization_tech_guest == set()
    assert sunos.virtualization_tech_host == set()

# Generated at 2022-06-13 04:21:00.002366
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():

    # create object of class SunOSVirtual
    SunOSVirtual_obj = SunOSVirtual()

    # check value of list container_facts
    assert SunOSVirtual_obj.container_facts == ['container']

    # check value of list virtual_facts
    assert SunOSVirtual_obj.virtual_facts == [
        'virtualization_type',
        'virtualization_role',
        'container',
        'virtualization_tech_guest',
        'virtualization_tech_host'
    ]

    # check value of list virtual_distros
    assert SunOSVirtual_obj.virtual_distros == []

    # check value of attribute platform
    assert SunOSVirtual_obj.platform == 'SunOS'


# Generated at 2022-06-13 04:21:01.929470
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})
    assert virtual.name == 'SunOS'

# Generated at 2022-06-13 04:21:03.104962
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:21:05.481680
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual()
    assert v.platform == 'SunOS'


# Generated at 2022-06-13 04:21:15.573717
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = get_module_mock()
    module.get_bin_path.return_value = "/usr/sbin/virtinfo"
    module.run_command.return_value = (0, "DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false", None)
    sunos_virtual = SunOSVirtual(module)
    virtual_facts = sunos_virtual.get_virtual_facts()
    assert virtual_facts['virtualization_type'] == 'ldom'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['virtualization_tech_guest'] == {'ldom'}
    assert virtual_facts['virtualization_tech_host'] == set()



# Generated at 2022-06-13 04:21:31.150275
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector(dummy_module)
    assert c.virtual._module == dummy_module


# Generated at 2022-06-13 04:21:31.992491
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:21:33.461260
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = SunOSVirtualCollector._create_module()
    assert isinstance(SunOSVirtual(module), SunOSVirtual)

# Generated at 2022-06-13 04:21:40.276698
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    import os
    import sys
    import platform
    import tempfile

    class TestJson(object):

        class ModuleExit(Exception):
            pass

        def __init__(self, params):
            self.run_command = __TestRunCommand
            self.params = params
            self.exit_args = None
            self.exit_failed = False
            self.path_exists = __TestPathExists
            self.get_bin_path = __TestGetBinPath

        def debug(self, msg):
            pass

        def fail_json(self, **kwargs):
            self.exit_failed = kwargs
            raise TestJson.ModuleExit()

        def exit_json(self, **kwargs):
            self.exit_args = kwargs
            raise TestJson.ModuleExit()


# Generated at 2022-06-13 04:21:42.964873
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector._fact_class == SunOSVirtual
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 04:21:53.445874
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    module.run_command = run_command_mock

    # We start with a common set of arguments to simulate a global zone
    # on a SunOS VM running on Vmware
    args = {
        'paths': {
            'zonename': 'EXISTING_FILE',
            'modinfo': 'EXISTING_FILE',
        },
        'commands': {
            'zonename': (0, 'global', ''),
            'modinfo': (0, 'modinfo:', ''),
        }
    }

    # Tests the case of a global zone
    args['commands']['zonename'] = (0, 'global', '')
    facts = SunOSVirtual(module, args).get_virtual_facts()

    assert facts['container'] is None

# Generated at 2022-06-13 04:22:03.175744
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    obj = SunOSVirtual()

    # Mock subprocess.check_output
    from mock import patch
    from ansible.module_utils.facts.virtual import sunos
    sunos.subprocess = sunos.subprocess.subprocess

    def check_output(cmd, *args, **kwargs):
        if cmd == "/usr/sbin/virtinfo -p":
            output = "DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false"
            return output
        elif cmd == "smbios":
            output = "Vendor: VMware"
        else:
            output = "abc"
        return output


# Generated at 2022-06-13 04:22:06.085157
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual


# Generated at 2022-06-13 04:22:17.034367
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Test get_virtual_facts of class SunOSVirtual
    """
    # Placeholder for instantiating a virtual class for testing.
    # The class is not instantiated directly, rather an instance of
    # module_utils.facts.virtual.generic.Virtual is instantiated.
    # This test will run against the generic class and it's methods.
    # If a method is not defined in the generic class, then the
    # class will be instantiated and the underlying platform will
    # provide the implementation
    #
    # To add more tests for the SunOS platform, duplicate the following
    # block and change the params values accordingly
    #
    # Example:
    #   params = { 'platform': 'SunOS',
    #              'virtualization_type': 'kvm',
    #              'virtualization_role': 'guest' }
    #

# Generated at 2022-06-13 04:22:17.795962
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    v = SunOSVirtualCollector()
    assert repr(v) == "<SunOSVirtualCollector>"

# Generated at 2022-06-13 04:22:51.960549
# Unit test for constructor of class SunOSVirtual

# Generated at 2022-06-13 04:22:53.383678
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt = SunOSVirtual()
    assert virt.get_virtual_facts() == {}

# Generated at 2022-06-13 04:22:56.543930
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    assert SunOSVirtual({}).__class__.__name__ == 'SunOSVirtual'
    assert SunOSVirtual({}).get_virtual_facts().__class__.__name__ == 'dict'

# Generated at 2022-06-13 04:23:04.454766
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # In the case of Solaris 10, smbios command is unavailable
    module = AnsibleModule({})
    virtual_facts_obj = SunOSVirtual({}, module)

    # Test zone
    setattr(virtual_facts_obj, 'module', module)
    virtual_facts_obj.module.run_command = MagicMock(return_value=(0, 'global', ''))
    assert virtual_facts_obj.get_virtual_facts() == {}
    virtual_facts_obj.module.run_command = MagicMock(return_value=(0, '', ''))
    assert virtual_facts_obj.get_virtual_facts()['virtualization_role'] == 'guest'

    # Test branded zone
    os.path.exists = MagicMock(return_value=True)
    assert virtual_facts_obj.get_virtual_

# Generated at 2022-06-13 04:23:10.927263
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    SunOSVirtual.module = module

    module.get_bin_path.side_effect = lambda x: x
    module.run_command.side_effect = [
        # zonename
        (0, 'global', ''),
        # modinfo
        (0, '1.0 VMware\n', ''),
        # virtinfo
        (1, 'virtinfo can only be run from the global zone\n', ''),
        # smbios
        (0, '1.0 VMware\n', '')
    ]
    SunOSVirtual.get_virtual_facts()

    assert module.run_command.call_count == 4

# Generated at 2022-06-13 04:23:23.067021
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    class MockModule:
        def __init__(self):
            # simple mockup of the ansible module class
            pass

        def get_bin_path(self, name, opt_dirs=[]):
            # simple mockup of module.get_bin_path
            if name == 'zonename':
                return '/bin/zonename'
            elif name == 'modinfo':
                return '/bin/modinfo'
            elif name == 'virtinfo':
                return '/usr/sbin/virtinfo'
            elif name == 'smbios':
                return '/bin/smbios'
            else:
                return None


# Generated at 2022-06-13 04:23:34.366007
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    '''
    This is a destructive test. Do not execute it while you have a running LDOM
    '''
    vc = SunOSVirtualCollector()

    # Assume that we are not a guest
    assert vc.__class__.__name__ == 'SunOSVirtualCollector'
    assert vc.platform == 'SunOS'
    assert len(vc.get_all_facts()) == 0

    # Assume that we are a guest in a windows host
    fact_list = {
        'smbios_systemmanufacturer': 'VMware, Inc.',
        'smbios_systemproductname': 'VMware Virtual Platform',
        'smbios_systemversion': 'None',
        'smbios_systemrelease': 'None'
    }
    vc = SunOSVirtualCollector(fact_list)

# Generated at 2022-06-13 04:23:43.961196
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    # Test 1: This should return a dictionary containing guests facts
    # when executing over a Solaris 11 LDoms virtualised Solaris 11 system.
    module = AnsibleModule(argument_spec=dict())
    is_ldom_test = {
        'virtualization_type': 'ldom',
        'virtualization_role': 'host',
        'virtualization_tech_host': set(['zone', 'ldom']),
        'virtualization_tech_guest': set(['zone'])
    }
    test = SunOSVirtual(module)
    assert test.get_virtual_facts() == is_ldom_test

    # Test 2: This should return a dictionary containing guests facts
    # when executing over a Solaris 11 zone virtualised Solaris 11 system.
    module = AnsibleModule(argument_spec=dict())

# Generated at 2022-06-13 04:23:46.813884
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    from ansible.module_utils.facts import virtual

    sunOsVirtual = virtual.SunOSVirtual()

    assert sunOsVirtual.platform == 'SunOS'


# Generated at 2022-06-13 04:23:53.143108
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    import ansible.module_utils.facts.virtual.base as virtual_base
    import ansible.module_utils.facts.virtual.zone as zone

    def run_fake_command(self, cmd, check_rc=True):
        if cmd == 'zonename':
            return (0, "gc7test1\n", '')
        else:
            rc, out, err = virtual_base.run_command(cmd, check_rc)
            assert rc == 0
            return rc, out, err

    fake_module = virtual_base.FakeAnsibleModule()
    fake_module.get_bin_path = lambda command: command
    fake_module.run_command = run_fake_command
    virtual = SunOSVirtual(fake_module)


# Generated at 2022-06-13 04:24:57.241863
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModuleMock()
    module.run_command.side_effect = [
        (0, 'global', ''),
        (1, '', ''),
        (0, '/usr/sbin/modinfo\nVMware GSKit\nVirtualBox\n', ''),
    ]
    module.get_bin_path.side_effect = [
        '/bin/zonename',
        None,
        '/usr/sbin/modinfo',
    ]
    facts = SunOSVirtual(module)

# Generated at 2022-06-13 04:25:04.527127
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual.base import Virtual
    import os

    # The class SunOSVirtual is a subclass of class Virtual.
    assert issubclass(SunOSVirtual, Virtual)

    # Mocked methods run_command and get_bin_path
    def mocked_run_command(self, module, args, check_rc=True, close_fds=True, executable=None, data=None):

        if args == "/usr/sbin/zonestat":
            return (0, "global", "")

        if args == "/usr/sbin/virtinfo -p":
            return (0, "DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false", "")


# Generated at 2022-06-13 04:25:15.666563
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    def run_command(self, command, check_rc=True, close_fds=True):
        # This is a stub to replace ansible.utils.module_docs_fragments.run_command()
        # It just return the command that is running and the right return code to test rc
        return command, 0

    virtual = SunOSVirtual(None)
    virtual.module.run_command = run_command

    # Test if it's a zone
    virtual.module.run_command = lambda command, check_rc=True, close_fds=True: ('zonename', 0, "global")
    virtual_facts = {'container': 'zone'}
    assert virtual.get_virtual_facts() == virtual_facts

    # Test if it's a branded zone (i.e. Solaris 8/9 zone)
    virtual.module.run

# Generated at 2022-06-13 04:25:27.796014
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    class ModuleStub(object):

        module = None

        def get_bin_path(self, executable, required=True, opt_dirs=[]):
            if executable == 'zonename':
                return executable
            elif executable == 'modinfo':
                return executable
            elif executable == 'virtinfo':
                return executable
            elif executable == 'smbios':
                return executable
            return None

        def run_command(self, command):
            out = ""
            err = ""
            if command[0] == 'zonename':
                out = "global\n"
            elif command[0] == 'modinfo':
                out = "26    1 1e7000 c80   12      VMware, Inc.:PCI 1000:0001\n"

# Generated at 2022-06-13 04:25:29.791328
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict(module=None))
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:25:35.213265
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    x = SunOSVirtual()
    assert x.virtualization_type is None
    assert x.virtualization_role is None
    assert x.container is None
    x = SunOSVirtual({'virtualization_type': 'kvm', 'virtualization_role': 'guest', 'container': 'zone'})
    assert x.virtualization_type == 'kvm'
    assert x.virtualization_role == 'guest'
    assert x.container == 'zone'


# Generated at 2022-06-13 04:25:39.486943
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual()
    assert virtual_facts.get_platform() == 'SunOS'
    assert virtual_facts.get_virtual_facts() is None
    assert virtual_facts.get_all_virtual_facts() is None

# Generated at 2022-06-13 04:25:41.908548
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModule(
        argument_spec=dict()
    )
    v = SunOSVirtual(module)
    assert v.platform == 'SunOS'

# Generated at 2022-06-13 04:25:51.885843
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test case vars
    class TestClass:
        def get_bin_path(self, name):
            bin_paths = {'zonename': 'zonename', 'modinfo': 'modinfo', 'smbios': 'smbios' }
            if name in bin_paths:
                return bin_paths[name]
            return None

        def run_command(self, cmd):
            # Test case data for 'zone'
            if cmd == 'zonename':
                return (0, 'global', '')
            elif cmd == 'zonename':
                return (0, 'global', '')
            elif cmd == 'modinfo':
                return (0, '',  'ERROR: modinfo: could not open modinfo file /kernel/drv/virtio.conf: No such file or directory')

            # Test case

# Generated at 2022-06-13 04:25:54.152983
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    m = SunOSVirtual(module)
    facts = m.get_virtual_facts()
    assert m.virtualization_type is None

# Generated at 2022-06-13 04:27:56.751734
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    response = {
        'containers': [],
        'virtualization_role': 'guest',
        'virtualization_type': 'zone',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {'zone'}
    }
    runner = get_runner('SunOS', 'zonename global')
    result = SunOSVirtual(runner).get_virtual_facts()
    assert result == response

    response = {
        'containers': [],
        'virtualization_role': 'guest',
        'virtualization_type': 'ldom',
        'virtualization_tech_host': set(),
        'virtualization_tech_guest': {'ldom'}
    }
    runner = get_runner('SunOS', "smbios | grep 'VMware'")
    result = SunOS

# Generated at 2022-06-13 04:28:00.457538
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    x = SunOSVirtual({})
    assert x.platform == 'SunOS'
    assert x.container == 'zone'
    assert x.virtualization_type == 'zone'
    assert x.virtualization_role == 'guest'
    assert x.virtualization_type_role == 'guest'
    assert x.virtualization_technologies == ['zone']

# Generated at 2022-06-13 04:28:01.471561
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual()
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:28:06.024691
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = DummyAnsibleModule(platform='SunOS')
    facts = SunOSVirtual(module).get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'container' in facts
    assert 'virtualization_tech_guest' in facts



# Generated at 2022-06-13 04:28:08.361876
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    try:
        SunOSVirtualCollector()
    except:
        assert False, 'Test failed to create an instance of SunOSVirtualCollector'


# Generated at 2022-06-13 04:28:17.301326
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.detect import SunOSVirtual
    import json

    sunos_virtual_output = json.loads("""
    "SunOS":{
        "virtualization_type":"vmware",
        "virtualization_role":"guest",
        "virtualization_tech_host":[
            "zone"
        ],
        "virtualization_tech_guest":[

        ]
    }
    """)

    sunos_virtual = SunOSVirtual()
    sunos_virtual_facts = sunos_virtual.get_virtual_facts()

    # Removing the 'container' key as it can change based on the System/Zone
    if 'container' in sunos_virtual_facts:
        del sunos_virtual_facts['container']

    assert sunos_virtual_facts == sunos_virtual_output

# Generated at 2022-06-13 04:28:20.554758
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sv = SunOSVirtual({}, {})
    assert sv.platform == 'SunOS'
    assert sv.virtualization_type is None
    assert sv.virtualization_role is None
    assert sv.container is None

# Generated at 2022-06-13 04:28:24.133649
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector

    assert isinstance(Collector.fetch_fact_collector('SunOS'), SunOSVirtualCollector)

# Generated at 2022-06-13 04:28:26.945171
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector("foo")
    assert isinstance(vc, SunOSVirtualCollector)
    assert isinstance(vc._fact_class, SunOSVirtual)

# Generated at 2022-06-13 04:28:29.001388
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModuleMock()
    v = SunOSVirtual(module)
    assert v.platform == 'SunOS'
