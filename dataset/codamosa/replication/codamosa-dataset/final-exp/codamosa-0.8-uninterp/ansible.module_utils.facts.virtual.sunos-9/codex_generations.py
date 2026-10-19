

# Generated at 2022-06-13 04:20:44.801247
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    _test_data = dict(
        ldom_guest_output="""
DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false
DOMAINUUID|6107b407-55c1-48da-8bdf-9b0d0c33a4a7
CAPACITY|cpu=4|mem=524288|cpu-cap=100|cpu-shares=0
DOMAINNAME|testme
HOSTNAME|t81
CPUSPEED|1165
CPUNUM|4
CPUTYPE|Niagara2
"""
    )

# Generated at 2022-06-13 04:20:49.424533
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = SunOSVirtualCollector.factory()
    virtual_facts = module.get_virtual_facts()
    assert 'container' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_tech_guest' in virtual_facts
    assert 'virtualization_tech_host' in virtual_facts

# Generated at 2022-06-13 04:20:52.759415
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module = {}
    virtual_collector = SunOSVirtualCollector(module)
    assert virtual_collector.__class__ == SunOSVirtualCollector
    assert virtual_collector._fact_class == SunOSVirtual
    assert virtual_collector._platform == 'SunOS'

# Generated at 2022-06-13 04:20:54.630394
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector()
    assert isinstance(obj, VirtualCollector)
    assert obj.platform == 'SunOS'
    assert isinstance(obj.facts, SunOSVirtual)

# Generated at 2022-06-13 04:20:55.315733
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:20:57.001777
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc._fact_class == SunOSVirtual
    assert vc._platform == 'SunOS'


# Generated at 2022-06-13 04:20:59.576144
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({},{})
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:21:01.929597
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:21:13.029809
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test case 1: host is a global zone
    module = MockAnsibleModule()
    module.run_command.return_value = (0, "global", "")
    module.get_bin_path.side_effect = [None, None, None, None, None, None, None]
    modinfo = "/usr/sbin/modinfo"
    module.get_bin_path.return_value = modinfo
    module.run_command.side_effect = [
        (0, "VBoxGuestAdditions:  Installed: 4.3.0_OSE", ""),
        (0, " id   0x844a    compat    \"VMware   \",\"VMXNET\",\"VMMouse\"", "")
    ]
    virtual_facts = SunOSVirtual(module).get_virtual_facts()
    assert len

# Generated at 2022-06-13 04:21:21.632615
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import sys
    sys.path.append('/usr/share/ansible')

    from ansible.module_utils.facts import gather_subset
    from ansible.module_utils.facts.collector.sunos import SunOSVirtualCollector
    from ansible.module_utils.facts.virtual import SunOSVirtual

    collector = SunOSVirtualCollector()
    list_result = gather_subset(collector, 'virtual')
    assert type(list_result) == list

    virtual = SunOSVirtual(collector=collector)
    dict_result = virtual.get_virtual_facts()
    assert type(dict_result) == dict

# Generated at 2022-06-13 04:21:45.935425
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class SunOSVirtual'''
    import shutil
    import tempfile
    import platform

    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    # This test is only valid on a SunOS system
    if platform.system() != 'SunOS':
        return


# Generated at 2022-06-13 04:21:47.408615
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc.platform == 'SunOS'
    assert vc.fact_class._platform == 'SunOS'

# Generated at 2022-06-13 04:21:55.595725
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:21:59.033384
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:22:00.957732
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    v = SunOSVirtualCollector(None)
    assert v.platform == 'SunOS'

# Generated at 2022-06-13 04:22:07.286187
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    virtual_facts = SunOSVirtual().get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_host'] == set()
    assert not 'virtualization_type' in virtual_facts
    assert not 'virtualization_role' in virtual_facts
    assert not 'container' in virtual_facts

# Generated at 2022-06-13 04:22:09.671976
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc._platform == 'SunOS'
    assert vc.collect() is not None

# Generated at 2022-06-13 04:22:20.931267
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # make sure OS module is loaded
    module = AnsibleModule(argument_spec=[], supports_check_mode=False)
    # make sure we can use the run_command mock
    m = module.run_command

    # create instance of SunOSVirtual
    class_instance = SunOSVirtual(module)

    # make sure method get_virtual_facts is empty
    assert class_instance.get_virtual_facts() == {}

    # mock module
    class_instance.module.run_command = m
    module.run_command.return_value = (0, 'global', '')
    assert class_instance.get_virtual_facts() == {'virtualization_tech_host': {'zone'}}
    module.run_command.return_value = (0, 'non-global', '')
    assert class_instance.get_virtual_

# Generated at 2022-06-13 04:22:29.194943
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # test static load of collector
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    facts_dict = dict()
    obj = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False,
        facts=facts_dict,
    )
    obj.exit_json = lambda **kwargs: True
    obj.exit_json.__self__ = obj
    c = SunOSVirtualCollector(obj)
    assert c._platform == 'SunOS'
    assert c._fact_class == SunOSVirtual
    assert c.platform == 'SunOS'
    assert c._fact_class.platform == 'SunOS'
    assert obj.exit_json.called is False
    assert obj.exit_json.call_count == 0
    assert obj

# Generated at 2022-06-13 04:22:31.426385
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtual_collector = SunOSVirtualCollector()
    assert sunos_virtual_collector is not None

# Generated at 2022-06-13 04:22:58.690066
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module = FakeModule()
    fact_class = SunOSVirtual
    platform = 'SunOS'

    collector = SunOSVirtualCollector(module, fact_class, platform)
    assert collector._module == module
    assert collector._fact_class == fact_class
    assert collector._platform == platform

# Generated at 2022-06-13 04:22:59.602070
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:23:00.786202
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert isinstance(SunOSVirtualCollector(), VirtualCollector)

# Generated at 2022-06-13 04:23:04.454968
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = fake_run_command
    module.get_bin_path = lambda x: x

    collector = SunOSVirtualCollector(module=module)

    assert collector.get_virtual_facts() == {
        'container': 'zone',
        'virtualization_type': 'vmware',
        'virtualization_role': 'guest'
    }

# Generated at 2022-06-13 04:23:07.346016
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sv = SunOSVirtualCollector()
    assert sv._platform == 'SunOS'
    assert sv._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:23:17.321129
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    v = SunOSVirtual()
    v.module.run_command = lambda *a, **kw: (0, "", "")
    v.module.get_bin_path = lambda *a: "/sbin/somecommand"
    v.facts = {}
    v.get_virtual_facts()

    assert v.facts['virtualization_type'] == 'zone'
    assert v.facts['virtualization_role'] == 'guest'
    assert v.facts['container'] == 'zone'
    assert v.facts['virtualization_tech_guest'] == set(['zone'])
    assert v.facts['virtualization_tech_host'] == set()

    # test if we can parse the output of virtinfo

# Generated at 2022-06-13 04:23:19.487550
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sv = SunOSVirtual(dict())
    assert sv.platform == 'SunOS'

# Generated at 2022-06-13 04:23:22.133737
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual()
    assert v.platform == 'SunOS'
    assert v.virtualization_type is None
    assert v.virtualization_role is None


# Generated at 2022-06-13 04:23:23.993630
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x.platform == 'SunOS'
    assert x._fact_class == SunOSVirtual


# Generated at 2022-06-13 04:23:35.166217
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # TODO: Use a mock module
    # module = AnsibleModuleMock(
    #    argument_spec=dict(
    #        gather_subset=dict(default=['!all', '!min'], type='list')
    #    ),
    #    check_invalid_arguments=False,
    #    bypass_checks=True
    #)

    # facts = ansible_collector.get_facts(module)
    # virtual_facts = ansible_collector.get_virtual_facts(module, facts)
    # assert 'virtualization_type' in virtual_facts
    # assert 'virtualization_role' in virtual_facts
    # assert 'virtualization_tech_guest' in virtual_facts
    # assert 'virtualization_tech_host' in virtual_facts
    pass

# Generated at 2022-06-13 04:24:38.220841
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # A unit test implementation to test get_virtual_facts() of class SunOSVirtual

    # Mock module and class objects
    class MockModule:
        def __init__(self):
            self.fake_bin_path = '/bin'
            self.fake_rc = 0
            self.fake_out = None
            self.fake_err = None

        def get_bin_path(self, arg):
            return self.fake_bin_path

        def run_command(self, arg):
            return (self.fake_rc, self.fake_out, self.fake_err)

    class MockSunOSVirtual(SunOSVirtual):
        def __init__(self, module):
            self.module = module

    # Test data for testing virtual facts with zone
    # in_data will be sent to get_virtual_facts() as argument and


# Generated at 2022-06-13 04:24:39.663685
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:24:42.834726
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module = AnsibleModule(argument_spec={})
    virtual = SunOSVirtualCollector(module)
    assert isinstance(virtual, SunOSVirtualCollector)
    assert virtual._platform == 'SunOS'
    assert virtual._fact_class == SunOSVirtual


# Generated at 2022-06-13 04:24:53.131849
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Run unit tests for method get_virtual_facts of class SunOSVirtual.
    """

    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    # define expected values for method get_virtual_facts
    facts = {}

    # initialize class
    sunos_virtual = SunOSVirtual(facts)

    # obtain virtual facts
    sunos_virtual_facts = sunos_virtual.get_virtual_facts()

    # test for virtualization_type
    if 'virtualization_type' in sunos_virtual_facts:
        print("Virtualization type is %s" % sunos_virtual_facts['virtualization_type'])
    else:
        print("Virtualization type is physical machine")
    print("")

    # test for virtualization_role

# Generated at 2022-06-13 04:24:57.879047
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Create a test instance of class SunOSVirtualCollector
    sunos_vc = SunOSVirtualCollector()
    # Test if the instance of class SunOSVirtualCollector is correctly initialized
    assert sunos_vc.facts_class == SunOSVirtual
    assert sunos_vc.platform == 'SunOS'

# Generated at 2022-06-13 04:24:59.693528
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual



# Generated at 2022-06-13 04:25:05.945645
# Unit test for method get_virtual_facts of class SunOSVirtual

# Generated at 2022-06-13 04:25:16.784819
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos.get_virtual_facts import SunOSVirtual

    if os.path.exists('/proc/vz'):
        virtual_facts = SunOSVirtual().get_virtual_facts()
        assert virtual_facts['virtualization_type'] == 'virtuozzo'
        assert virtual_facts['virtualization_role'] == 'guest'

    if os.path.isdir('/.SUNWnative'):
        virtual_facts = SunOSVirtual().get_virtual_facts()
        assert 'zone' in virtual_facts['virtualization_tech_guest']
        assert virtual_facts['container'] == 'zone'

    if os.path.exists('/etc/vmware-tools/'):
        virtual_facts = SunOSVirtual().get_virtual_facts()

# Generated at 2022-06-13 04:25:18.165883
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()

# Generated at 2022-06-13 04:25:21.702664
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})
    assert virtual.platform == 'SunOS'
    assert virtual.virtualization_type == {}
    assert virtual.virtualization_role == {}
    assert virtual.container == {}



# Generated at 2022-06-13 04:27:17.922573
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Calling method SunOSVirtual.get_virtual_facts()
    # with module args kwargs={'ANSIBLE_MODULE_ARGS': {'gather_subset': ['all'], 'module_name': 'setup', 'gather_timeout': 10}}
    # and module_name='setup' and gather_timeout=10
    # and module_args={'gather_subset': ['all']}
    setup_module_args = dict(gather_subset=['all'])
    module_name = 'setup'
    gather_timeout = 10
    import mock
    import ansible.module_utils.facts.virtual.sunos as sunos
    module = mock.Mock()
    module.get_bin_path.side_effect = lambda p: p
    module.run_command.side_effect = sunos._run

# Generated at 2022-06-13 04:27:19.964116
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt = SunOSVirtual()
    assert hasattr(virt, 'vendor')
    assert hasattr(virt, 'hypervisor')
    assert hasattr(virt, 'product')

# Generated at 2022-06-13 04:27:23.009513
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({})
    assert virtual_facts.platform == 'SunOS'
    assert virtual_facts.virtualization_type is None
    assert not hasattr(virtual_facts, 'container')
    assert not hasattr(virtual_facts, 'virtualization_role')

# Generated at 2022-06-13 04:27:24.909589
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    s = SunOSVirtual({})

# Generated at 2022-06-13 04:27:26.463133
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = None
    virt = SunOSVirtual(module)
    assert virt.platform == 'SunOS'

# Generated at 2022-06-13 04:27:34.894309
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    import sys
    import os.path
    import argparse
    from ansible.module_utils.facts import ModuleArgsParser

    cwd = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(cwd, '../../..'))
    from ansible.module_utils.facts import Collector

    parser = ModuleArgsParser()
    parser.add_argument('gather_subset', nargs='+', action='append')
    args = parser.parse_args(['all'])

    collector = Collector(args=args,
                          supported_os=[SunOSVirtualCollector._platform],
                          timeout=0.01)

    assert collector.platform in collector._fact_classes
    assert len(collector._fact_classes) == 1
    assert collector._host == 'localhost'


# Generated at 2022-06-13 04:27:42.646928
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # GIVEN: A SunOSVirtual object
    sunos_virtual = SunOSVirtual()

    # WHEN: get_virtual_facts() is called
    result = sunos_virtual.get_virtual_facts()

    # THEN: The result should be a dict containing the expected data
    result.pop('module', None)
    assert result == {
        'container': 'zone',
        'virtualization_role': 'guest',
        'virtualization_type': 'vmware',
        'virtualization_tech_guest': {'vmware', 'zone'},
        'virtualization_tech_host': {'zone'}
    }



# Generated at 2022-06-13 04:27:46.385188
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    runner_mock = Mock()
    runner_mock.run_command.return_value = (1, '', '')
    runner_mock.get_bin_path.return_value = False
    facts = runner_mock.collect_facts()
    assert facts['virtualization_type'] == 'zone'
    assert facts['virtualization_role'] == 'guest'
    assert facts['container'] == 'zone'

# Generated at 2022-06-13 04:27:57.345090
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    # test for a solaris global zone
    module = FakeAnsibleModule({
        'command': 'smbios'
    }, tags=['always', 'collector'])
    virtual_facts_inspector = SunOSVirtual(module)
    result = virtual_facts_inspector.get_virtual_facts()
    assert 'virtualization_type' in result
    assert 'virtualization_role' in result
    assert 'virtualization_tech_host' in result
    assert 'virtualization_tech_guest' in result
    assert 'container' not in result

    # test for a solaris zone
    module = FakeAnsibleModule({
        'command': 'zonename'
    }, stdout='solaris_zone', tags=['always', 'collector'])

# Generated at 2022-06-13 04:27:58.250446
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    SunOSVirtual(None)