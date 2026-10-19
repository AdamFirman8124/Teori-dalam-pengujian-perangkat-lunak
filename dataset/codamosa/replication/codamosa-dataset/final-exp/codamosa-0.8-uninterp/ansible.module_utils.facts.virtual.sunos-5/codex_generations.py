

# Generated at 2022-06-13 04:20:40.655557
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    p = SunOSVirtualCollector()
    assert p.platform == 'SunOS'
    assert issubclass(p._fact_class, Virtual)


# Generated at 2022-06-13 04:20:42.834852
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    facts = collector.collect()
    for fact in facts:
        assert type(fact) == SunOSVirtual

# Generated at 2022-06-13 04:20:49.388616
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.run_command = Mock(return_value=(0, '', ''))
            self.get_bin_path = Mock(return_value='/sbin/modinfo')
        def fail_json(self, **kwargs):
            pass

    class MockZone(object):
        def __init__(self):
            self.run_command = Mock(return_value=(0, '', ''))
            self.get_bin_path = Mock(return_value='/usr/bin/zonename')

    class MockZone2(object):
        def __init__(self):
            self.run_command = Mock(return_value=(0, 'global', ''))

# Generated at 2022-06-13 04:20:50.369951
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_facts = SunOSVirtualCollector()
    assert virtual_facts._platform == 'SunOS'

# Generated at 2022-06-13 04:20:51.973570
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtual_collector = SunOSVirtualCollector()
    assert sunos_virtual_collector.platform == "SunOS"
    assert sunos_virtual_collector.fact_class.platform == "SunOS"

# Generated at 2022-06-13 04:20:58.688319
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    import os
    import re
    import subprocess

    class MockModule(object):
        """ Minimal implementation of AnsibleModule for testing purposes """
        def __init__(self, **kwargs):
            self.params = kwargs
        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')
        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
        @staticmethod
        def get_bin_path(name, *args, **kwargs):
            pattern = "^/.+/%s$" % (name,)
            matcher = re.compile(pattern)

# Generated at 2022-06-13 04:21:10.608892
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual_sunos import SunOSVirtual
    # Create an instance of SunOSVirtual class with the minimal input values
    virtual = SunOSVirtual({})
    # Assume the minimal conditions for a zone
    virtual.module.run_command = lambda x: (0, "global", "")
    virtual.module.get_bin_path = lambda x: None
    # Call the method get_virtual_facts of class SunOSVirtual
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['container'] == 'zone'
    assert 'virtualization_type' not in virtual_facts
    assert 'virtualization_role' not in virtual_facts
    assert virtual_facts['virtualization_tech_host'] == set(['zone'])
    assert virtual_facts['virtualization_tech_guest']

# Generated at 2022-06-13 04:21:13.614774
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = DummyAnsibleModule()
    virt = SunOSVirtual(module)
    assert virt.platform == 'SunOS'
    assert virt.module == module


# Generated at 2022-06-13 04:21:15.328431
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual({})
    assert facts.__class__ == SunOSVirtual

# Generated at 2022-06-13 04:21:22.181341
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeAnsibleModule()
    funit = SunOSVirtual(module)

    # Make sure all expected values are actually set
    assert 'platform' in funit.facts

    assert 'virtualization_type' in funit.facts
    assert 'virtualization_role' in funit.facts
    assert 'virtualization_tech_host' in funit.facts
    assert 'virtualization_tech_guest' in funit.facts
    assert 'container' in funit.facts

# Class to mimic AnsibleModule

# Generated at 2022-06-13 04:21:38.336033
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    data = {'ansible_facts':
            {'virtualization_type': 'zone',
             'virtualization_role': 'guest',
             'container': 'zone',
             'virtualization_tech_guest': ['zone'],
             'virtualization_tech_host': ['zone']},
            'changed': False}
    v = SunOSVirtual({}, data)
    assert v.get_virtual_facts() == data['ansible_facts']

# Generated at 2022-06-13 04:21:39.533122
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector

# Generated at 2022-06-13 04:21:45.801715
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    virt = SunOSVirtual({})
    facts = virt.get_virtual_facts()
    assert facts == {
        'virtualization_type': 'xen',
        'virtualization_role': 'guest',
        'virtualization_tech_guest': {'xen'},
        'virtualization_tech_host': set(),
        'container': None
    }

# Generated at 2022-06-13 04:21:51.462041
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    '''Unit test for method get_virtual_facts of class SunOSVirtual'''
    # Read the virtual facts
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    virt = SunOSVirtual(module)
    facts = virt.get_virtual_facts()
    assert len(facts) == 2
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert facts['virtualization_type'] == 'kvm'
    assert facts['virtualization_role'] == 'guest'


# Generated at 2022-06-13 04:21:53.241549
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
  # Test if the class can be instantiated
  obj = SunOSVirtualCollector()
  assert obj != None


# Generated at 2022-06-13 04:21:59.481732
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeModule()

    # If the zone name command returns "global"
    module.run_command.side_effect = [
        (0, "global", ""),
    ]
    virtual = SunOSVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_role'] == 'host'
    assert virtual_facts['virtualization_type'] == 'zone'
    assert virtual_facts['virtualization_tech_host'] == set(['zone'])

    # If the zone name command returns a non-empty string
    module.run_command.side_effect = [
        (0, "non-global", ""),
    ]
    virtual = SunOSVirtual(module)
    virtual_facts = virtual.get_virtual_facts()
    assert virtual_facts['virtualization_role']

# Generated at 2022-06-13 04:22:03.960559
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # set up object SunOS
    sys_v = SunOSVirtual({})

    # Assert that sys_v is an object of class SunOSVirtual
    assert isinstance(sys_v, SunOSVirtual)

    # Get virtual facts
    sys_v.get_virtual_facts()

# Generated at 2022-06-13 04:22:06.510114
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x
    assert str(x) == "<SunOSVirtualCollector: fact_class='SunOSVirtual'>"

# Generated at 2022-06-13 04:22:17.491854
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand(rc=0, out='global', err='')
    v = SunOSVirtual(module)
    virtual_facts = v.get_virtual_facts()
    if not virtual_facts['virtualization_type'] == 'zone':
        raise AssertionError("virtualization_type is not 'zone', but '{0}'".format(virtual_facts['virtualization_type']))
    if not virtual_facts['virtualization_role'] == 'host':
        raise AssertionError("virtualization_role is not 'host', but '{0}'".format(virtual_facts['virtualization_role']))

# Generated at 2022-06-13 04:22:19.719041
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert issubclass(SunOSVirtualCollector, VirtualCollector)
    # create object of SunOSVirtualCollector
    obj = SunOSVirtualCollector()
    # check type of object created
    assert isinstance(obj, SunOSVirtualCollector)
    # check value of _fact_class variable
    assert SunOSVirtualCollector._fact_class == SunOSVirtual
    # check value of _platform variable
    assert SunOSVirtualCollector._platform == 'SunOS'


# Generated at 2022-06-13 04:22:48.955959
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Call constructor
    obj = SunOSVirtualCollector()

    # Check class of object
    assert isinstance(obj, SunOSVirtualCollector)

    # Check class of object
    assert isinstance(obj, VirtualCollector)

    # Check instance of class FactCollector
    assert isinstance(obj._fact_class, SunOSVirtual)

    # Check platform
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 04:22:59.853463
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import unittest
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual

    class TestSunOSVirtualGetVirtualFacts(unittest.TestCase):
        def setUp(self):
            self.module = AnsibleModuleMock()
            self.suut = SunOSVirtual(self.module)

        def tearDown(self):
            pass

        def test_get_virtual_facts_physical(self):
            self.module.run_command.return_value = (0, '', '')
            self.module.get_bin_path.side_effect = lambda x: ('zonename' if x == 'zonename' else None)
            self.suut.get_virtual_facts()
            self.assertEqual(self.module.params, dict())

# Generated at 2022-06-13 04:23:05.342411
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """
    Sanity check on constructor of SunOSVirtual
    """
    virtual_facts = SunOSVirtual({})
    assert virtual_facts._platform == 'SunOS'
    assert virtual_facts.guests == set()
    assert virtual_facts.hypervisors == set()
    assert virtual_facts.virtual == {}

# Generated at 2022-06-13 04:23:06.633000
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    s = SunOSVirtual(None)
    assert s.platform == 'SunOS'


# Generated at 2022-06-13 04:23:10.361660
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    virt = SunOSVirtual(module)

    assert virt.get_virtual_facts() is None or isinstance(virt.get_virtual_facts(), dict)

# Generated at 2022-06-13 04:23:13.298735
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector.platform == 'SunOS'
    assert SunOSVirtualCollector.virtual.platform == 'SunOS'
    assert SunOSVirtualCollector.virtual.get_virtual_facts() is None

# Generated at 2022-06-13 04:23:20.911753
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # The module run_command() function returns a tuple (rc, out, err)
    # the mock_module's run_command() function returns a dict:
    #  { 'rc': 0, 'out': 'zonename: global\n', 'err': '' }
    def mock_run_command(cmd, check_rc=True, close_fds=True,
                         executable=None, data=None, binary_data=False):
        if cmd == 'zonename':
            return { 'rc': 0, 'out': 'zonename: global\n', 'err': '' }

# Generated at 2022-06-13 04:23:23.339255
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x.platform == 'SunOS'
    assert x.fact_class == SunOSVirtual



# Generated at 2022-06-13 04:23:27.281111
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    """
    This test creates an instance of class SunOSVirtual and checks some of its properties
    """
    sunos_virtual = SunOSVirtual()
    assert sunos_virtual.platform == 'SunOS'



# Generated at 2022-06-13 04:23:37.713832
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts import FactModule
    from ansible.module_utils.facts import ModuleArgsParser
    from ansible.module_utils.facts import BaseFactCollector
    from ansible.module_utils import basic

    import pytest

    # Simple test where the method doesn't fail
    def test_method_does_not_fail(mocker):
        mocker.patch.object(SunOSVirtual, 'get_virtual_facts')
        mocker.patch.object(FactModule, 'exit_json')
        mocker.patch.object(ModuleArgsParser, 'get_facts_params')
        mocker.patch.object(ModuleArgsParser, 'run')
        mocker.patch.object(BaseFactCollector, 'collect')
       

# Generated at 2022-06-13 04:24:34.757514
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    facts = SunOSVirtual({}, {}).get_virtual_facts()
    assert 'virtualization_type' in facts
    assert 'virtualization_role' in facts
    assert 'container' in facts
    assert 'virtualization_tech_guest' in facts
    assert 'virtualization_tech_host' in facts

# Generated at 2022-06-13 04:24:36.818083
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert isinstance(SunOSVirtualCollector(None), SunOSVirtualCollector)

# Generated at 2022-06-13 04:24:40.019335
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    collector = SunOSVirtualCollector()
    assert collector._platform == 'SunOS'
    assert collector._fact_class == SunOSVirtual


# Generated at 2022-06-13 04:24:51.027461
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    #####################################
    # Test get_virtual_facts() on global zone
    #####################################
    # Case 1: host is running a vmware guest
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    import os

    module_mock = FakeAnsibleModule()

# Generated at 2022-06-13 04:24:54.410047
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    mod = MockModule()
    virtual = SunOSVirtual(module=mod)
    assert virtual.platform == "SunOS"
    assert virtual.get_virtual_facts.__doc__ == "Get virtualization related facts for SunOS"


# Generated at 2022-06-13 04:24:57.759581
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class == SunOSVirtual
    assert isinstance(SunOSVirtualCollector._fact_class({}), SunOSVirtual)

# Generated at 2022-06-13 04:25:06.381713
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # Initialize the virtualization fact class
    fact = SunOSVirtual({
        'ansible_facts': {
            'features': {
            }
        }
    })
    # Initialize SunOSVirtual and bind it to the fact
    fact.collect()
    # Initialize the SunOSVirtualCollector class
    vc = SunOSVirtualCollector()
    # Get the virtualization fact
    v_fact = vc.get_virtual_facts(fact)
    # Check if the virtualization fact returned is of the right type
    assert isinstance(v_fact, SunOSVirtual)


if __name__ == '__main__':
    test_SunOSVirtual()

# Generated at 2022-06-13 04:25:07.746382
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    SunOSVirtual(dict())

# Generated at 2022-06-13 04:25:09.445849
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = MockModule()
    virtual = SunOSVirtual(module)
    assert virtual.module == module

# Generated at 2022-06-13 04:25:10.593716
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()


# Generated at 2022-06-13 04:26:56.601577
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:26:58.272094
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeAnsibleModule()
    facts = SunOSVirtual(module)
    assert facts.platform == 'SunOS'
    assert facts.gather_subset == ['all']

# Generated at 2022-06-13 04:27:01.860463
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc.platform == 'SunOS'
    assert vc._fact_class == SunOSVirtual


# Generated at 2022-06-13 04:27:02.904669
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    SunOSVirtual(dict(module=dict()))

# Generated at 2022-06-13 04:27:13.222721
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = FakeModule()
    virtual = SunOSVirtual(module=module)

    module.run_command_output['/usr/sbin/smbios'] = ("Vendor: Parallels\n"
                                                     "Vendor: Parallels\n"
                                                     "Vendor: Parallels\n")
    expected_result = {'virtualization_type': 'parallels',
                       'virtualization_role': 'guest',
                       'virtualization_tech_guest': set(['parallels']),
                       'virtualization_tech_host': set()}
    result = virtual.get_virtual_facts()
    assert(result == expected_result)


# Generated at 2022-06-13 04:27:15.129377
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """Check if a SunOSVirtualCollector is created or not"""
    assert SunOSVirtualCollector is not None

# Generated at 2022-06-13 04:27:21.234913
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts.virtual import SunOSVirtual
    from ansible.module_utils.facts.virtual.sunos import *  # noqa
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector

    module = ModuleStub()
    virtual = SunOSVirtual(module)
    assert virtual.get_virtual_facts() == {'virtualization_tech_host': set(),
                                           'virtualization_tech_guest': set(['zone']),
                                           'virtualization_role': 'guest',
                                           'container': 'zone',
                                           'virtualization_type': 'zone'}

# Generated at 2022-06-13 04:27:24.875620
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    import platform
    import ansible.module_utils.facts.virtual.sunos as sunos
    sunos_virtual = sunos.SunOSVirtualCollector()
    assert sunos_virtual._platform == platform.system()

# Generated at 2022-06-13 04:27:28.359734
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtual_collector = SunOSVirtualCollector()
    assert sunos_virtual_collector._fact_class is None, '_fact_class should be None'
    assert sunos_virtual_collector._platform == 'SunOS', '_platform should be SunOS'


# Generated at 2022-06-13 04:27:35.708072
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create a dummy module
    module = type('', (object,), {})
    module.run_command = lambda *_, **__: (0, "", "")
    module.get_bin_path = lambda *_: ""
    module.params = {'gather_subset': [], 'gather_timeout': 10}
    module.exit_json = lambda _: False

    # Create an instance of a dummy class that implements
    # _get_virtual_facts
    class Dummy(SunOSVirtual):
        def _get_virtual_facts(self):
            pass

    # Create an instance of the SunOSVirtual class
    facts = SunOSVirtual(module)

    # Call the get_virtual_facts method
    facts.get_virtual_facts()