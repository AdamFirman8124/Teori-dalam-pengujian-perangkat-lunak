

# Generated at 2022-06-13 04:20:41.854043
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc_assert = SunOSVirtualCollector()
    assert vc_assert.platform == 'SunOS', "Expected 'SunOS' but got " + vc_assert.platform
    assert isinstance(vc_assert.fact_class(), SunOSVirtual), 'Expected fact class to be SunOSVirtual'

# Generated at 2022-06-13 04:20:44.839914
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """
    Test the constructor of the class SunOSVirtual
    """
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    sun_virtual = SunOSVirtual({})

    assert sun_virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:20:46.591734
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos_virtual = SunOSVirtual(None)
    assert(sunos_virtual.platform == 'SunOS')

# Generated at 2022-06-13 04:20:55.004693
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict()
    )

    module.params['gather_subset'] = ['!all', 'virtual']
    module.params['gather_timeout'] = 0

    facts = AnsibleModule(
        argument_spec = dict(
            ansible_facts=dict(required=True, type='dict')
        )
    )

    mocker = mocker_factory(module, facts)
    virtual_mocker = mocker.patch('ansible_collections.ansible.community.plugins.modules.facts.virtual.sunos.SunOSVirtual')
    virtual_ins = SunOSVirtual(module=module)
    virtual_ins.get_virtual_facts()
    virtual_ins.get_virtual_facts.assert_called_once_with()

    virtual_mocker.reset_m

# Generated at 2022-06-13 04:20:56.239685
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos = SunOSVirtual()
    assert sunos
    assert sunos.platform == 'SunOS'


# Generated at 2022-06-13 04:20:59.325536
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Create empty class
    instance = SunOSVirtualCollector()
    assert instance.platform == 'SunOS'

# Generated at 2022-06-13 04:21:10.798333
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    class ModuleMock(object):

        def run_command(self, command):
            rc = 1
            out = ''
            err = ''

            if command == 'zonename':
                rc = 0
                out = 'global'

            if command == 'zonename':
                rc = 0
                out = 'somezone'

            if command == 'modinfo':
                rc = 0
                out = 'id   0    ffffffff    53a2f18a    name VMware'

            if command == 'smbios':
                rc = 0
                out = 'VMware'

            if command == '/usr/sbin/virtinfo -p':
                rc = 0
                out = 'DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false'

            return rc, out, err

       

# Generated at 2022-06-13 04:21:13.317040
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtual_collector = SunOSVirtualCollector()
    assert sunos_virtual_collector.platform == 'SunOS'



# Generated at 2022-06-13 04:21:24.328171
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    SunOSVirtual._run_exit_methods = False

    def return_exit_code(rc, *args):
        return rc
    SunOSVirtual._exit = return_exit_code

    # SunOSVirtual._run_exit_methods = False
    # SunOSVirtual._exit = return_exit_code

    # Case 1: It is a guest in a zone
    # Run: zonename
    #       rc = 0
    #       out = "some-zone"
    #       err = ""
    def run_output_rc_0_zonename(args, *kwargs):
        return 0, "some-zone", ""

    # Case 1-A: It is a

# Generated at 2022-06-13 04:21:25.452720
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:21:49.756924
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    cmd = "virtinfo -p"
    rc = 0

# Generated at 2022-06-13 04:21:51.799544
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = SunOSVirtualCollector.get_module()
    print("Virtual facts for SunOS platform")
    print("================================")
    SunOSVirtualCollector.get_virtual_facts(module)

# Generated at 2022-06-13 04:21:55.463481
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})
    assert virtual.facts['virtualization_type'] == 'zone'
    assert virtual.facts['virtualization_role'] == 'host'
    assert 'zone' in virtual.facts['virtualization_tech_host']
    assert virtual.facts['virtualization_tech_guest'] == set()
    assert virtual.facts['container'] == 'zone'


# Generated at 2022-06-13 04:21:59.440866
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual()
    assert virtual.platform == "SunOS"
    assert virtual.get_virtual_facts() is not None

# Generated at 2022-06-13 04:22:01.764280
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc.platform == 'SunOS'


# Generated at 2022-06-13 04:22:04.889334
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_fact_collector = SunOSVirtualCollector()
    assert virtual_fact_collector._platform == 'SunOS'
    assert virtual_fact_collector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 04:22:06.180068
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:22:08.362049
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeModule()
    virtual_facts = SunOSVirtual(module)
    assert virtual_facts.platform == 'SunOS'


# Generated at 2022-06-13 04:22:10.173402
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    facts = SunOSVirtualCollector()
    assert facts.__class__.__name__ == 'SunOSVirtualCollector'

# Generated at 2022-06-13 04:22:13.964800
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    if os.name != 'posix':
        return
    facts = SunOSVirtual({})
    assert facts.platform == 'SunOS'
    assert facts.virtualization_type is None
    assert facts.virtualization_role is None
    assert facts.container is None



# Generated at 2022-06-13 04:22:47.642536
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Test if the output of method "get_virtual_facts" is as expected
    def execute_mock(command, *args, **kwargs):
        if command == '/usr/sbin/smbios':
            return 0, 'This is a VMware from ESXi 6.5 server', ''
        elif command == '/usr/sbin/virtinfo -p':
            return 0, '''
This is a global zone
DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false''', ''
        else:
            return 1, '', ''
    module_mock = Mock()
    module_mock.run_command = Mock(wraps=execute_mock)
    module_mock.get_bin_path = Mock(side_effect=lambda x: x)
    fact = Sun

# Generated at 2022-06-13 04:22:51.164915
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc._fact_class == SunOSVirtual
    assert vc._platform == 'SunOS'

# Generated at 2022-06-13 04:23:00.117531
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    dummy_module = type('MockModule', (object,), {'get_bin_path': lambda self, arg: arg})()
    dummy_module.run_command = lambda cmd: (0, "DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false", "")

    sunos_virtual = SunOSVirtual(dummy_module)
    assert sunos_virtual.get_virtual_facts() == {
        'virtualization_role': 'guest',
        'virtualization_type': 'ldom',
        'virtualization_tech_guest': set(['ldom']),
        'virtualization_tech_host': set(),
        'container': 'zone'
    }

# Generated at 2022-06-13 04:23:09.976200
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    import tempfile
    import textwrap

    results = {}


# Generated at 2022-06-13 04:23:11.923727
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual({}, {}, {}, {})
    assert virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:23:14.014956
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector.platform == 'SunOS'
    assert collector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 04:23:17.666013
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    myFacts = SunOSVirtualCollector()
    assert myFacts.__class__.__name__ == 'SunOSVirtualCollector'
    assert myFacts.platform == 'SunOS'
    assert myFacts._fact_class.__name__ == 'SunOSVirtual'


# Generated at 2022-06-13 04:23:19.307455
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_sun = SunOSVirtual()
    assert virtual_sun is not None

# Generated at 2022-06-13 04:23:20.301374
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:23:23.722787
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = MockModule()

    tc = SunOSVirtual(module)
    fct = tc.get_virtual_facts()
    assert fct['virtualization_type'] == 'xen'
    assert fct['virtualization_role'] == 'guest'



# Generated at 2022-06-13 04:24:23.783745
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import SunOSVirtual
    from ansible.module_utils.facts import ModuleFacts
    # Create a subclass of SunOSVirtual with stubbed method get_file_content

# Generated at 2022-06-13 04:24:36.755098
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts.collector import VirtualCollectorParams
    module = VirtualCollectorParams(
        ansible_module=None,
        subprocess=None,
        platform=None,
        FileUtils=None,
        virt_type=None,
        virt_what=None,
        lspci=None,
        IsContainer=None,
        sysctl=None,
        GetLsb=None,
        Virtual=SunOSVirtual
    )
    module.IsContainer = (lambda: False)
    module.GetLsb = lambda: {}
    module.sysctl = (lambda x: (0, '', ''))
    module.lspci = (lambda x: (0, '', ''))
    module.virt_what = None
    module.virt_type = None

    collector = SunOS

# Generated at 2022-06-13 04:24:42.600456
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Test for a Solaris zone host
    module = 'ansible.module_utils.facts.virtual.sunos.SunOSVirtual'
    zone_host_os_virtual = SunOSVirtualCollector(module)
    os_virtual = zone_host_os_virtual._fact_class(module, zone_host_os_virtual._platform)
    assert os_virtual.platform == 'SunOS'



# Generated at 2022-06-13 04:24:45.098656
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual(dict())
    assert virtual_facts.platform == 'SunOS'

if __name__ == '__main__':
    # Unit test for constructor of class SunOSVirtualCollector
    test_SunOSVirtual()

# Generated at 2022-06-13 04:24:47.064735
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos_virtual = SunOSVirtual(dict(module=dict()))
    assert sunos_virtual.platform == 'SunOS'

# Generated at 2022-06-13 04:24:57.361515
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = MockModule()
    sunosvirt = SunOSVirtual(module=module)

    # Test LDOM
    module.run_command.return_value = ('DOMAINROLE|impl=LDoms|control=false|io=false|service=false|root=false', '', 0)
    module.get_bin_path.return_value = 1
    assert sunosvirt.get_virtual_facts() == {'virtualization_role': 'guest', 'virtualization_type': 'ldom', 'virtualization_tech_guest': {'ldom'}, 'virtualization_tech_host': set()}

    # Test non-LDOM
    module.run_command.return_value = ('smbios: WARNING - virtinfo not present.  Does not look like ldoms.', '', 1)

# Generated at 2022-06-13 04:25:00.375463
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = AnsibleModule(
        argument_spec=dict()
    )
    result = {}
    result['failed'] = False
    module.exit_json(**result)


# Generated at 2022-06-13 04:25:05.462241
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = mock_module()

    virt = SunOSVirtual(module)
    facts = virt.get_virtual_facts()

    assert facts['virtualization_type'] == 'vmware'
    assert facts['virtualization_role'] == 'guest'
    assert len(facts['virtualization_tech_host']) == 2
    assert 'zone' in facts['virtualization_tech_host']
    assert 'ldoms' in facts['virtualization_tech_host']
    assert len(facts['virtualization_tech_guest']) == 1
    assert 'vmware' in facts['virtualization_tech_guest']
    assert 'container' in facts



# Generated at 2022-06-13 04:25:08.023935
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector().populate_virtual_facts() is None

# Generated at 2022-06-13 04:25:09.994744
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # TODO: Add assert tests to check ouput of get_virtual_facts()
    virt_facts = SunOSVirtual().get_virtual_facts()

# Generated at 2022-06-13 04:26:56.649814
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    test_object = dict(
        module=dict(
            get_bin_path=lambda *args: '/bin/true'
        )
    )

    sut = SunOSVirtual(**test_object)

    result = sut.get_virtual_facts()

    assert result['virtualization_type'] == 'xen'

# Generated at 2022-06-13 04:27:02.948973
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    m_ansible_module = MockAnsibleModule()
    m_module = MockModule()
    m_sunos_virtual = SunOSVirtual(m_module)
    assert m_sunos_virtual.module is m_module
    assert m_sunos_virtual.module.run_command is m_ansible_module.run_command

# Test get_virtual_facts with real files and directories

# Generated at 2022-06-13 04:27:13.269999
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils._text import to_bytes
    input_data = {'ansible_facts': { 'distribution': 'SunOS' }}
    input_data['ansible_facts']['system_vendor'] = ''
    if 'rc' not in input_data['ansible_facts']:
        input_data['ansible_facts']['rc'] = 0
    if 'out' not in input_data['ansible_facts']:
        input_data['ansible_facts']['out'] = ''
    if 'err' not in input_data['ansible_facts']:
        input_data['ansible_facts']['err'] = ''
    module = DummyAnsibleModule(input_data)
    virtual = SunOSVirtualCollector(module).collect()[0]

    # Called from

# Generated at 2022-06-13 04:27:14.211140
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual = SunOSVirtual({})


# Generated at 2022-06-13 04:27:21.448633
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Call get_virtual_facts of class BSDVirtual
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual import VirtualCollector

    sunos_virtual = SunOSVirtual(VirtualCollector())
    ansible_module = MockAnsibleModule()
    sunos_virtual.module = ansible_module

    # Return value of zonename
    a_b_c = (0, "zone1\n", "")
    ansible_module.run_command.append(a_b_c)

    # Return value of modinfo
    a_b_c = (0, "", "")
    ansible_module.run_command.append(a_b_c)

    # Return value of virtinfo

# Generated at 2022-06-13 04:27:31.443080
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts.collector import VirtualCollector
    from ansible.module_utils.facts import virtual
    import sys
    import os

    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = Mock()
            self.fail_json = Mock()
            self.run_command = Mock(return_value=(0, '', ''))
            self.get_bin_path = Mock(return_value='')


# Generated at 2022-06-13 04:27:37.762006
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create instance of class SunOSVirtual with its constructor
    sunos_virtual = SunOSVirtual({})
    # Retrieve virtual facts
    virtual_facts = sunos_virtual.get_virtual_facts()
    assert 'virtualization_type' in virtual_facts
    assert 'virtualization_role' in virtual_facts
    assert 'container' in virtual_facts

# Generated at 2022-06-13 04:27:46.087864
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    test_module = type('test_module', (object,), dict(
        get_bin_path=lambda self, path: path,
        run_command=lambda self, cmd: (0, '', '')))
    test_obj = SunOSVirtual(test_module)
    test_data = {
        'zone': 'global',
        'modinfo': [],
        'zone_is_branded': False,
        'vz': False,
        'virtinfo': True,
        'smbios': [],
        'expected': {}
    }
    assert test_obj.get_virtual_facts() == test_data['expected']

    # Non-global zone
    test_data['zone'] = 'testzone'

# Generated at 2022-06-13 04:27:49.420944
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunosvc = SunOSVirtualCollector()
    assert sunosvc._fact_class == SunOSVirtual
    assert sunosvc._platform == 'SunOS'

# Generated at 2022-06-13 04:27:58.851672
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    os.environ['PATH'] = test_dir + os.pathsep + os.environ['PATH']

    class TestModule(object):
        def __init__(self):
            self.run_command_calls = []

        def run_command(self, args, check_rc=True):
            self.run_command_calls.append((args, check_rc))
            if args == 'zonename':
                return 0, 'global', ''
            elif args == '/usr/sbin/virtinfo -p':
                return 0, 'DOMAINROLE|impl=LDoms|control=true|io=true|service=false|root=false|', ''
            return 0, '', ''
