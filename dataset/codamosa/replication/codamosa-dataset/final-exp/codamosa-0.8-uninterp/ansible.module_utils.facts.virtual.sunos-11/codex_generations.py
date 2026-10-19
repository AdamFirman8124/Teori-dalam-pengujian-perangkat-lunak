

# Generated at 2022-06-13 04:20:38.054024
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({})
    assert virtual_facts.facts == {}

# Generated at 2022-06-13 04:20:40.329637
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec=dict())
    result = SunOSVirtual(module).get_virtual_facts()
    assert result == dict()

# Generated at 2022-06-13 04:20:46.248955
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create a fake module
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    # Create a SunOSVirtual object
    sunos_virtual = SunOSVirtual(module)
    result = sunos_virtual.get_virtual_facts()
    assert result['virtualization_tech_guest'] == set()
    assert result['virtualization_tech_host'] == set()
    assert result['virtualization_type'] == None
    assert result['virtualization_role'] == None
    assert result['container'] == None

# Generated at 2022-06-13 04:20:54.777365
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import os

    # create a test instance of SunOSVirtual
    test_SunOSVirtual = SunOSVirtual(dict())
    test_SunOSVirtual.module = MockModule()

    # fake the isfile method
    def fake_isfile(filename):
        if filename == '/.SUNWnative':
            return True
        else:
            return False

    # fake the method run_command

# Generated at 2022-06-13 04:20:57.572277
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector
    sunosvirtual_collector = SunOSVirtualCollector()
    assert sunosvirtual_collector.platform == 'SunOS'
    assert sunosvirtual_collector._fact_class == SunOSVirtual

# Unit tests for constructor of class SunOSVirtual

# Generated at 2022-06-13 04:21:09.995583
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Test the SunOSVirtual.get_virtual_facts() method.
    """

    # Need to be root to run this test
    if os.getuid() != 0:
        print("Need to be root to run this test")
        exit(1)

    # Test code for SunOSVirtual.get_virtual_facts()
    module = None # The module object will be assigned here
    os_facts = dict() # Fake facts for os
    virtual = SunOSVirtual(module, os_facts)
    facts = virtual.get_virtual_facts()

    # Expected result
    expected = dict()

    # Check if the returned dictionary is equal to the expected dictionary
    assert facts == expected, "Expected result:\n" + str(expected) + "\nGot:\n" + str(facts)

    # Check if the "virtualization_type"

# Generated at 2022-06-13 04:21:19.558072
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    # Create a SunOSVirtual instance
    sunos_virtual = SunOSVirtual()

    # Create a test module
    module = type('AnsibleModule', (object,), dict(
        EXEC_MODULE=False,
        get_bin_path=lambda x: 'bin_path',
        run_command=lambda x: (0, '', ''),
        fail_json=lambda x: True,
        exit_json=lambda x, y: True
    ))()

    # Create an instance of SunOSVirtualCollector
    sunos_virtual_collector = SunOSVirtualCollector(module=module)

    # Create a SunOSVirtual instance
    sunos_virtual = sunos_virtual_collector.collect()

    # Call get_virtual_facts
    result = sunos_virtual.get_virtual_facts()

    # Check the

# Generated at 2022-06-13 04:21:21.530471
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({})
    assert isinstance(virtual_facts, SunOSVirtual)

# Generated at 2022-06-13 04:21:24.461030
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    v = SunOSVirtual()

    # We expect to get a subclass of Virtual with correct attributes
    assert isinstance(v, Virtual)
    assert v.platform == 'SunOS'

# Generated at 2022-06-13 04:21:26.327077
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    instance = SunOSVirtualCollector()
    assert isinstance(instance, SunOSVirtualCollector)

# Generated at 2022-06-13 04:21:50.330069
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    import json
    import sys
    import unittest

    class TestModule(object):
        def __init__(self, **kwargs):
            if 'params' in kwargs:
                self.params = kwargs['params']
            else:
                self.params = {}
            if 'mock_command' in kwargs:
                self.mock_command = kwargs['mock_command']
            else:
                self.mock_command = None

        def fail_json(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 04:21:56.748804
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand()

    def_test = {}
    def_test['vmware'] = {'command': "modinfo | grep -i vmware", 'out': '', 'rc': 1}
    def_test['virtualbox'] = {'command': "modinfo | grep -i virtualbox", 'out': '', 'rc': 1}
    def_test['zonename'] = {'command': "zonename", 'out': 'global', 'rc': 0}
    def_test['modinfo'] = {'command': "modinfo", 'out': '', 'rc': 1}
    def_test['virtinfo'] = {'command': "virtinfo", 'out': 'foo', 'rc': 0}

# Generated at 2022-06-13 04:21:59.989471
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    test_SunOSVirtualCollector = SunOSVirtualCollector()
    assert test_SunOSVirtualCollector._platform == 'SunOS'



# Generated at 2022-06-13 04:22:02.808897
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({}, {})
    assert virtual_facts.platform == 'SunOS'
    assert virtual_facts.__class__.__name__ == 'SunOSVirtual'

# Generated at 2022-06-13 04:22:06.369692
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    my_SunOSVirtual = SunOSVirtual()
    assert my_SunOSVirtual is not None

    # Assert that the object is a subclass of Virtual
    assert issubclass(type(my_SunOSVirtual), Virtual)

# Generated at 2022-06-13 04:22:08.535726
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(dict(module=dict()))
    assert virtual.get_virtual_facts() is None


# Generated at 2022-06-13 04:22:14.736395
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual.base import Virtual

    vc = SunOSVirtualCollector()
    assert vc._platform == "SunOS"
    assert vc._fact_class == SunOSVirtual
    assert isinstance(vc._fact_class(dict()), Virtual)

# Generated at 2022-06-13 04:22:24.548940
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Define virtualization facts (e.g. returned by run_command)
    module_mock = {
        'get_bin_path': lambda x: 'bin/' + x,  # Return the default path
        'run_command': lambda x: ('', '', ''),  # Don't run any command
    }
    sunos_virtual_host = SunOSVirtual(module_mock)
    facts = sunos_virtual_host.get_virtual_facts()

    assert dict(
        virtualization_type=None,
        virtualization_role=None,
        container=None,
        virtualization_tech_guest=set(),
        virtualization_tech_host=set(),
    ) == facts


# Generated at 2022-06-13 04:22:27.258577
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    redhat_virtual = SunOSVirtual(dict(module=None), dict())
    assert redhat_virtual.get_virtual_facts() == {}
    assert redhat_virtual.output == {}

# Generated at 2022-06-13 04:22:35.160586
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual({'module': None})
    assert facts._platform == 'SunOS'
    assert isinstance(facts._fact_class, SunOSVirtual)
    assert SunOSVirtual.__name__ in facts._fact_class.__name__
    assert SunOSVirtual.__module__ in facts._fact_class.__module__
    assert facts._supported_asfacts == ['virtualization_type', 'virtualization_role', 'container']

# Generated at 2022-06-13 04:22:55.670963
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = fake_ansible_module()
    module.run_command = run_command
    module.get_bin_path = get_bin_path

    virtual = SunOSVirtual(module=module)
    virtual_facts = virtual.get_virtual_facts()

    assert virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts


# Define fake AnsibleModule

# Generated at 2022-06-13 04:23:03.934561
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    """
    Unit test of method get_virtual_facts of class SunOSVirtual
    """
    virtual_instance = SunOSVirtual()
    assert virtual_instance.get_virtual_facts() == {}

    # Test on a host with only zones enabled
    import ansible.module_utils.facts.virtual.sunos
    ansible.module_utils.facts.virtual.sunos.zonename = lambda: '/bin/zonename'
    ansible.module_utils.facts.virtual.sunos.zonename.return_value = (0, 'global', '')
    os.path.isdir = lambda path: False
    assert 'zone' in virtual_instance.get_virtual_facts()['virtualization_tech_host']
    assert virtual_instance.get_virtual_facts()['virtualization_role'] == 'host'

# Generated at 2022-06-13 04:23:06.104701
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x.platform == 'SunOS'
    assert x._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:23:08.338088
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtualcollector = SunOSVirtualCollector()
    assert sunos_virtualcollector.platform == 'SunOS'

# Generated at 2022-06-13 04:23:11.186836
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert SunOSVirtualCollector._fact_class == SunOSVirtual
    assert SunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:23:15.457376
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    v = SunOSVirtual()
    facts = v.get_virtual_facts()
    assert facts['virtualization_role'] == 'guest', "Cannot find virtualisation_type in %s" % facts
    assert facts['virtualization_role'] == 'guest', "Cannot find virtualization_role in %s" % facts

# Generated at 2022-06-13 04:23:22.086184
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # A simple but complete example that can be later extended
    module = FakeAnsibleModule()

    # If not installed, virtinfo exits with rc = 1
    # If installed and machine is not a LDoms host, virtinfo exits with rc = 0 but output is a string: 'virtinfo can only be run from the global zone'
    # If installed and machine is a LDoms host, virtinfo exits with rc = 0 and output is format like this:
    #   DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=true
    module.run_command = lambda x: (0, 'DOMAINROLE|impl=LDoms|control=true|io=true|service=true|root=false', None)

    virtual_facts = SunOSVirtual(module).get_virtual_facts()

# Generated at 2022-06-13 04:23:26.295089
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Create object of SunOSVirtualCollector
    SunOSVirtualCollectorObj = SunOSVirtualCollector()
    assert SunOSVirtualCollectorObj._fact_class == SunOSVirtual
    assert SunOSVirtualCollectorObj._platform == 'SunOS'


# Generated at 2022-06-13 04:23:27.898849
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    v = SunOSVirtualCollector()
    assert v.platform == 'SunOS'

# Generated at 2022-06-13 04:23:28.811206
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # tested in the virtual.py
    pass

# Generated at 2022-06-13 04:24:11.062990
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    '''Unit test for constructor of class SunOSVirtualCollector'''
    import sys
    import os
    import unittest
    sys.modules['ansible'] = type('AnsibleMockModule', (), {'AnsibleModule': type('AnsibleMockClass', (), {'params': type('AnsibleMockClass', (), {'host': 'host', 'port': 'port'})})})
    sys.modules['ansible.module_utils.facts.virtual.sunos'] = type('AnsibleMockModule', (), {'SunOSVirtual': type('SunOSVirtualMockClass', (), {'get_virtual_facts': type('AnsibleMockClass', (), {'return_value': 'return_value'}), 'platform': 'platform'})})

# Generated at 2022-06-13 04:24:11.632172
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    SunOSVirtual(dict())

# Generated at 2022-06-13 04:24:12.520983
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({}, {})
    assert virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:24:14.849643
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert isinstance(collector, SunOSVirtualCollector)

# Generated at 2022-06-13 04:24:21.881079
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create an instance of module
    module = DummyModule()

    # Create an instance of class SunOSVirtual
    sunos_virtual = SunOSVirtual(module)

    # Set the module.run_command return values
    module.run_command_values["zonename"] = (0, "global", "")
    module.run_command_values["modinfo"] = (0, "/usr/kernel/misc/vmm:vmm_dev@0,0", "")

    # Get virtual facts
    facts = sunos_virtual.get_virtual_facts()

    # Check if virtual facts are set
    assert facts["virtualization_tech_guest"] == set()
    assert facts["virtualization_tech_host"] == set(["zone"])

# Generated at 2022-06-13 04:24:34.412132
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create a dummy module, so we can call get_bin_path
    # and run_command.
    module = DummyModule()

    # Create a SunOSVirtual instance.
    facts = SunOSVirtual(module=module)

    # Create a dictionary that contains the expected output of the
    # get_virtual_facts method.
    expected_output = dict(
        virtualization_type='xen',
        virtualization_role='guest',
        virtualization_tech_guest={
            'xen',
        },
        virtualization_tech_host=set(),
    )

    # Create a mock module.run_command method.
    def mock_run_command(command):
        rc = 0
        out = 'Intel(r) Xeon(r) CPU E5640 @ 2.67GHz\n'

# Generated at 2022-06-13 04:24:36.886386
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})
    assert virtual.virtualization_type == ''
    assert virtual.virtualization_role == ''
    assert not virtual.container

# Generated at 2022-06-13 04:24:38.425959
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    coll = SunOSVirtualCollector()
    assert coll.platform == 'SunOS'
    assert coll.fact_class == SunOSVirtual

# Generated at 2022-06-13 04:24:39.900879
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector.__platform__ == 'SunOS', "Platform set to %s" % SunOSVirtualCollector.__platform__

# Generated at 2022-06-13 04:24:44.440122
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    '''Test constructor of class SunOSVirtualCollector'''
    # Test with an empty argument
    virtual_collector = SunOSVirtualCollector()
    assert virtual_collector.__class__.__name__ == 'SunOSVirtualCollector'

# Generated at 2022-06-13 04:25:37.303803
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModule(argument_spec={})
    inv_obj = SunOSVirtual(module)
    assert inv_obj.platform == 'SunOS'

# Generated at 2022-06-13 04:25:43.612129
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = DummyAnsibleModule()
    iface_obj = SunOSVirtual(module)

    # Prepare get_virtual_facts to simulate a global zone.
    module.run_command = custom_run_command(zone_output='global')
    module.get_bin_path = custom_get_bin_path(zone_exists=True)
    virtual_facts = iface_obj.get_virtual_facts()
    assert 'zone' in virtual_facts['virtualization_tech_host']
    assert 'zone' not in virtual_facts['virtualization_tech_guest']

    # Prepare get_virtual_facts to simulate a non-global zone.
    module.run_command = custom_run_command(zone_output='testzone')

# Generated at 2022-06-13 04:25:46.050347
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModule({})
    virt_inst = SunOSVirtual(module)
    assert isinstance(virt_inst, SunOSVirtual)
    assert isinstance(virt_inst,Virtual)

# Generated at 2022-06-13 04:25:48.266005
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.get_fact_class() == SunOSVirtual

# Generated at 2022-06-13 04:25:50.320821
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModule(dict())
    SunOsVirtual(module)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:25:58.200366
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    module.params['gather_subset'] = ['!all', 'virtual']
    module.params['gather_timeout'] = 1
    virtual_fact = SunOSVirtual(module=module)

    # Test initialisation
    assert virtual_fact.platform == 'SunOS'
    assert module == virtual_fact.module
    assert virtual_fact.facts == {}
    assert virtual_fact.subsets == ['!all', 'virtual']
    assert virtual_fact.legacy_facts == {}

    # Test get_virtual_facts
    facts = virtual_fact.get_virtual_facts()
    assert facts['virtualization_role'] == 'guest'
    assert facts['container'] == 'zone'
    assert facts['virtualization_type'] == 'zone'

    # Test get_all_

# Generated at 2022-06-13 04:26:07.112107
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    class MockModule():
        def __init__(self, out_z=None, err_z=None, rc_z=0, out_modinfo=None,
                     err_modinfo=None, rc_modinfo=0, out_smbios=None,
                     err_smbios=None, rc_smbios=0, out_virtinfo=None,
                     err_virtinfo=None, rc_virtinfo=0):
            self.params = {}
            self.run_command_values = [(rc_z, out_z, err_z),
                                       (rc_modinfo, out_modinfo, err_modinfo),
                                       (rc_smbios, out_smbios, err_smbios),
                                       (rc_virtinfo, out_virtinfo, err_virtinfo)]
            self.run

# Generated at 2022-06-13 04:26:09.442748
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule('/bin/true', {})
    facts = SunOSVirtual(module).get_virtual_facts()

    assert facts['virtualization_tech_guest'] == set()
    assert facts['virtualization_tech_host'] == set()
    assert facts['container'] is None

# Generated at 2022-06-13 04:26:10.270230
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:26:14.551193
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    module = AnsibleModuleMock(
        params={
            'gather_subset': ['!all', 'virtual'],
            'filter': '*'
        }
    )
    obj = SunOSVirtualCollector(module)
    assert obj.platform == 'SunOS'
    assert isinstance(obj, VirtualCollector)
    assert isinstance(obj, SunOSVirtualCollector)


# Unit test class for testing SunOSVirtual class

# Generated at 2022-06-13 04:28:15.032103
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import sys
    if sys.version_info[0] == 2:
        from ansible.module_utils.facts import virtual

        module_mock = type('module_mock', (object,), {
            'debug': False,
            'get_bin_path': lambda x: True,
            'run_command': lambda x, check_rc=True: (0, 'VMware', ''),
        })()

        virtual_facts = SunOSVirtual(module=module_mock).get_virtual_facts()
        assert 'zone' in virtual_facts['virtualization_tech_guest']
        assert 'vmware' in virtual_facts['virtualization_tech_guest']
        assert 'virtualization_type' in virtual_facts and virtual_facts['virtualization_type'] == 'vmware'

# Generated at 2022-06-13 04:28:19.807823
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Create a SunOSVirtual object.
    sunos_virtual = SunOSVirtual(dict())
    # Check that the SunOSVirtual object is an instance of the SunOSVirtual class and of the Virtual class.
    assert isinstance(sunos_virtual, SunOSVirtual)
    assert isinstance(sunos_virtual, Virtual)

# Generated at 2022-06-13 04:28:29.629598
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils import basic

    loader = basic.AnsibleModule(argument_spec=dict())
    options = {'hostname': 'localhost'}
    # Call the get_virtual_facts method with a mocked AnsibleModule and check if:
    # - the correct dictionary with the virtualization facts is returned
    # - the method terminates without errors
    virtual_facts = SunOSVirtual(loader, options).get_virtual_facts()
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_tech_guest'] == set()
    assert virtual_facts['virtualization_type'] == 'zone'
    assert virtual_facts['virtualization_role'] == 'guest'
    assert virtual_facts['container'] == 'zone'

# Generated at 2022-06-13 04:28:37.628743
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    mod_obj = FakeModule()
    sunos_virtual_facts = SunOSVirtual(mod_obj)
    # Cause get_virtual_facts to return True for is_zone
    sunos_virtual_facts._is_zone = True

    # Make run_command return the contents of the provided file
    def run_command(self, cmd, check_rc=True, close_fds=True, data=None):
        rc = 0
        out = ''
        err = ''
        if cmd == "zonename":
            out = "global"

# Generated at 2022-06-13 04:28:38.883286
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Create a new instance
    assert SunOSVirtualCollector()


# Generated at 2022-06-13 04:28:40.229367
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert isinstance(vc, SunOSVirtualCollector)

# Generated at 2022-06-13 04:28:41.129118
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual(None)
    assert virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:28:45.850747
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    import ansible.module_utils.facts.virtual
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector
    _SunOSVirtualCollector = SunOSVirtualCollector(ansible.module_utils.facts.virtual.BaseVirtual())
    assert isinstance(_SunOSVirtualCollector, SunOSVirtualCollector)
    assert isinstance(_SunOSVirtualCollector._fact_class, SunOSVirtual)


# Generated at 2022-06-13 04:28:50.097634
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virt_facts = {'virtualization_type': 'ldom', 'virtualization_tech_guest': set(['ldom']),
                  'virtualization_role': 'guest', 'virtualization_tech_host': set(['zone'])}
    sunos_virtual = SunOSVirtual(None)
    assert sunos_virtual._facts == virt_facts

# Generated at 2022-06-13 04:28:51.471035
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """
    Test SunOSVirtual
    """
    virtual = SunOSVirtual({})
    assert virtual.virtualization_type == 'unknown'

