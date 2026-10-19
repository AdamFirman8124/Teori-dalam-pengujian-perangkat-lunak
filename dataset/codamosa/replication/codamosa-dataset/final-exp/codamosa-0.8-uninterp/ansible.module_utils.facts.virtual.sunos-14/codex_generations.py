

# Generated at 2022-06-13 04:20:47.588816
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts.virtual.base import Virtual

    m = ModuleStub()
    virtual = SunOSVirtual(m)

    # Test in a non-virtualized environment
    m.run_command.return_value = (0, 'global', '')
    virtual_facts = virtual.get_virtual_facts()

    assert virtual_facts == {'virtualization_tech_host': {'zone'}, 'virtualization_tech_guest': set(), 'virtualization_role': 'guest', 'virtualization_type': 'xen'}

    # Test in a virtualized environment
    m.run_command.return_value = (1, '', '')
    virtual_

# Generated at 2022-06-13 04:20:55.789282
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.facts.virtual.sun import SunOSVirtual
    module = SunOSVirtual._get_module()
    sun_virtual = SunOSVirtual()

    # Test if method _get_module returns correct module
    assert module.__class__.__name__ == "AnsibleModule"
    assert module.params == {}

    # Test if method _get_bin_path returns correct path
    assert sun_virtual._get_bin_path('ls') == '/bin/ls'

    # Test if method _run_command returns proper results
    rc, out, err = sun_virtual._run_command('ls')
    assert rc == 0
    assert len(out) > 0
    assert err is None

    # Test if method _run_command returns proper results when

# Generated at 2022-06-13 04:21:08.672429
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual.base import Virtual
    from ansible.module_utils.facts.virtual.base import VirtualCollector
    from ansible.module_utils.facts.virtual.base import VirtualMounts
    from ansible import module_utils
    from ansible.module_utils.six import PY3
    import types

    class Mock_module(types.ModuleType):
        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            self.exit_called = True

    # Create a mock module
    mock_module = Mock_module()

    # Make sure some

# Generated at 2022-06-13 04:21:11.383100
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    p = SunOSVirtual({})
    assert isinstance(p, Virtual)
    assert p.get_virtual_facts() is None

# Generated at 2022-06-13 04:21:15.525235
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert VirtualCollector.__name__ == 'VirtualCollector'
    assert SunOSVirtualCollector.__name__ == 'SunOSVirtualCollector'
    assert SunOSVirtualCollector._platform == 'SunOS'
    assert SunOSVirtualCollector._fact_class.__name__ == 'SunOSVirtual'

# Generated at 2022-06-13 04:21:17.384549
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x.platform == 'SunOS'
    assert x._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:21:28.284153
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # mock sunos virtual object
    sunos_virtual = SunOSVirtual()

    # mock methods of sunos virtual object
    sunos_virtual.module.get_bin_path = Mock(return_value='/sbin/zonename')
    sunos_virtual.module.run_command = Mock(return_value=(0, 'global', ''))
    sunos_virtual.module.get_bin_path = Mock(side_effect=['/usr/sbin/virtinfo', '/usr/sbin/modinfo', None])

# Generated at 2022-06-13 04:21:36.719953
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    import os
    import stat
    import tempfile
    module = basic.AnsibleModule(argument_spec={})
    module.get_bin_path = lambda x: '/usr/sbin/zoneadm' if x == 'zoneadm' else '/usr/sbin/virtinfo' if x == 'virtinfo' else None

    # Create the path to access to some files like '/proc/vz'
    if not os.path.exists('/proc/vz'):
        os.mkdir('/proc/vz')

    # Create a temporal file in /proc/vz
    vz_file = tempfile.NamedTemporaryFile

# Generated at 2022-06-13 04:21:38.250563
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    facts = {}
    collector = SunOSVirtualCollector(facts, None)
    assert isinstance(collector._virtual_facts_class, SunOSVirtual)

# Generated at 2022-06-13 04:21:41.122469
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    vc = SunOSVirtualCollector()
    assert vc.platform == 'SunOS'
    assert vc.fact_class == SunOSVirtual



# Generated at 2022-06-13 04:21:55.776651
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_facts = SunOSVirtualCollector().collect()
    assert virtual_facts['virtualization'] == 'SunOS'

# Generated at 2022-06-13 04:22:04.160146
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    import sys
    import unittest

    class TestSunOSVirtual_get_virtual_facts(unittest.TestCase):

        class ModuleStub(object):
            """A stub of AnsibleModule"""

            class RunCommandResult(object):
                """A stub of the result of AnsibleModule.run_command"""

                def __init__(self, returncode, out, err):
                    self.rc = returncode
                    self.stdout = out
                    self.stderr = err


# Generated at 2022-06-13 04:22:08.270475
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    module = FakeModule({})
    vitual = SunOSVirtual(module)
    assert vitual.platform == 'SunOS'
    assert vitual.module == module
    assert vitual.distribution == ''
    assert vitual.distribution_version == ''



# Generated at 2022-06-13 04:22:11.355225
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Create an instance of class SunOSVirtual
    virtual_facts = SunOSVirtual()
    res = virtual_facts.get_virtual_facts()
    print("%s" % res)


# Generated at 2022-06-13 04:22:14.690754
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Unit test for constructor of class SunOSVirtualCollector
    x = SunOSVirtualCollector()
    assert x._platform == x._fact_class.platform
    assert x._fact_class.platform == 'SunOS'


# Generated at 2022-06-13 04:22:16.586485
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:22:19.213604
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()
    assert virtual_collector._platform == 'SunOS'
    assert virtual_collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:22:28.249362
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # fixture
    from ansible.module_utils.facts.virtual.SunOS import SunOSVirtual as SunOSVirtualFixture


# Generated at 2022-06-13 04:22:33.226847
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Load module
    module = AnsibleModule(
        argument_spec=dict()
    )

    # Initialize system facts
    SunOSVirtual.init(module)

    # Run get_virtual_facts and return result
    return SunOSVirtual.get_virtual_facts()


# Generated at 2022-06-13 04:22:35.791448
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sc = SunOSVirtualCollector()
    assert sc._platform == 'SunOS'
    assert sc._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 04:23:06.083341
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # Fake data
    module = FakeModule({'zonename': "/usr/bin/zonename",
                         'zonename output': "global"})
    # Test a zone host
    output = SunOSVirtual(module).get_virtual_facts()
    assert "virtualization_tech_guest" in output
    assert "virtualization_tech_host" in output
    assert "virtualization_role" in output
    assert "virtualization_type" not in output
    assert "container" not in output
    assert output["virtualization_tech_guest"] == set()
    assert output["virtualization_tech_host"] == set(["zone"])
    assert output["virtualization_role"] == "host"
    # Test a branded zone
    module = FakeModule({'zonename': None,
                         'zonename output': None})
    module.facts

# Generated at 2022-06-13 04:23:16.489902
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    v = SunOSVirtual({})
    v.module = AnsibleModule(argument_spec = dict())
    # Assume that our global zone is not itself virtualized
    v.module.run_command = MagicMock(return_value=(0, '', ''))
    facts = v.get_virtual_facts()
    assert facts['virtualization_type'] == 'zone'
    assert facts['virtualization_role'] == 'guest'
    assert 'zone' in facts['virtualization_tech_guest']
    # Now we assume our global zone is virtualized
    v.module.run_command = MagicMock(return_value=(0, '/usr/kernel/drv/vmmon:  VMware Virtual Machine Monitor\n', ''))
    facts = v.get_virtual_facts()

# Generated at 2022-06-13 04:23:17.654828
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    facts = SunOSVirtual(dict(), dict())
    assert facts.platform == 'SunOS'
    # This is just a constructor so we can't assert any virtualization facts


# Generated at 2022-06-13 04:23:18.603742
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector(None)

# Generated at 2022-06-13 04:23:20.819764
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    assert SunOSVirtualCollector._fact_class == SunOSVirtual
    assert SunOSVirtualCollector._platform == 'SunOS'

# Generated at 2022-06-13 04:23:23.006398
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector()
    assert obj.platform == 'SunOS'


# Generated at 2022-06-13 04:23:25.242607
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    d = SunOSVirtualCollector()

    assert d._platform == 'SunOS'


# Generated at 2022-06-13 04:23:35.564564
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = AnsibleModule(argument_spec={})
    # The module argument 'module' does not support writing. This is a little hack to get the module instance
    SunOSVirtual._module = module

    # module.run_command() returns a tuple which can be extended as Python list
    # this is a hack to use a fake command
    def fake_run_command(cmd, check_rc=True):
        if cmd == 'zonename':
            return [0, 'global', '']

# Generated at 2022-06-13 04:23:45.276488
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    m = AnsibleModule({})
    v = SunOSVirtual(m)
    v.module.get_bin_path = mock.Mock(return_value='/usr/bin/zonename')
    v.module.run_command = mock.Mock(return_value=(0,'sys','sys'))
    result = v.get_virtual_facts()
    assert result['container'] == 'zone'

    v.module.get_bin_path = mock.Mock(return_value='/usr/bin/zonename')
    v.module.run_command = mock.Mock(return_value=(0,'global','global'))
    result = v.get_virtual_facts()
    assert not result['container'] == 'zone'


# Generated at 2022-06-13 04:23:51.123734
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    # This test assumes that:
    #   SunOSVirtual.platform is 'SunOS'
    #   SunOSVirtual._platform is 'SunOS'
    #   SunOSVirtualCollector._platform is 'SunOS'
    c = SunOSVirtualCollector()
    assert isinstance(c._all_virtual_classes[0], SunOSVirtual)

    v = c._all_virtual_classes[0]
    assert v.platform == 'SunOS'
    assert v._platform == 'SunOS'
    assert v._fact_class.__name__ == 'SunOSVirtual'
    assert v._fact_class.platform == 'SunOS'
    assert v._fact_class._platform == 'SunOS'

# Generated at 2022-06-13 04:24:45.273889
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Test with valid platform
    o = SunOSVirtualCollector()
    assert hasattr(o, 'platform')
    assert hasattr(o, '_fact_class')
    assert 'SunOS' == o.platform
    assert SunOSVirtual == o._fact_class
    # Test with invalid platform assigned
    o = SunOSVirtualCollector('redhat_7')
    assert hasattr(o, 'platform')
    assert hasattr(o, '_fact_class')
    assert 'SunOS' == o.platform
    assert SunOSVirtual == o._fact_class


# Generated at 2022-06-13 04:24:48.219427
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    # Test the SunOSVirtualCollector constructor
    # The collector should have a set of SunOSVirtual facts
    # The collectors '_platform' attribute should be set to 'SunOS'
    # No Exception should be raised
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:24:49.392210
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    SunOSVirtualCollector()

# Generated at 2022-06-13 04:24:52.615168
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    virtual_collector = SunOSVirtualCollector()
    assert isinstance(virtual_collector, SunOSVirtualCollector)
    assert virtual_collector._platform == 'SunOS'
    assert virtual_collector._fact_class == SunOSVirtual

# Generated at 2022-06-13 04:24:54.115270
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    assert isinstance(SunOSVirtual({}), dict)



# Generated at 2022-06-13 04:24:56.726028
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """Test SunOSVirtualCollector
    """

    facts = {'kernel': 'SunOS'}
    SunOSVirtualCollector(facts, None)

# Generated at 2022-06-13 04:24:58.727616
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    c = SunOSVirtualCollector()
    assert isinstance(c, SunOSVirtualCollector)
    assert c.platform == 'SunOS'

# Generated at 2022-06-13 04:25:00.417267
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    sunos_virtual_collector = SunOSVirtualCollector()
    assert sunos_virtual_collector._platform == 'SunOS'

# Generated at 2022-06-13 04:25:02.529232
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    virtual_facts = SunOSVirtual()
    assert virtual_facts.platform == 'SunOS'

# Generated at 2022-06-13 04:25:13.639709
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():

    module = object()

    # The following methods must be mocked because they depend on the
    # environment:
    #   - run_command

    def get_bin_path(name, opts=None):
        if name == 'smbios':
            return '/usr/sbin/smbios'
        elif name == 'zonename':
            return '/bin/zonename'
        elif name == 'virtinfo':
            return '/usr/sbin/virtinfo'
        elif name == 'modinfo':
            return '/sbin/modinfo'
        else:
            return None

    class RunCommandReturn:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err


# Generated at 2022-06-13 04:27:07.943435
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import SunOSVirtual
    result = {
        'virtualization_role': 'guest',
        'container': 'zone',
    }
    assert SunOSVirtual(dict()).get_virtual_facts() == result

# Generated at 2022-06-13 04:27:11.631221
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    from ansible.module_utils.facts.collector.virtual.sunos import SunOSVirtualCollector
    from ansible.module_utils.facts.collector import VirtualCollector

    a = SunOSVirtualCollector()
    assert isinstance(a, SunOSVirtualCollector)
    assert isinstance(a, VirtualCollector)

# Generated at 2022-06-13 04:27:14.496821
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    instance = SunOSVirtualCollector()
    assert isinstance(instance, SunOSVirtualCollector)
    assert issubclass(SunOSVirtualCollector, VirtualCollector)


# Generated at 2022-06-13 04:27:21.624207
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    module = get_module_mock()
    module.get_bin_path.return_value = '/usr/bin/zonename'

    module.run_command.return_value = (0, 'global', '')
    assert SunOSVirtual(module).get_virtual_facts() == {}
    module.run_command.assert_called_with('/usr/bin/zonename')

    module.run_command.return_value = (0, 'somezone', '')
    assert SunOSVirtual(module).get_virtual_facts() == {'container': 'zone'}
    module.run_command.assert_called_with('/usr/bin/zonename')

    os.path.isdir.return_value = True
    assert SunOSVirtual(module).get_virtual_facts() == {'container': 'zone'}

    os

# Generated at 2022-06-13 04:27:23.397159
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    x = SunOSVirtualCollector()
    assert x._platform == 'SunOS'
    assert x._fact_class is SunOSVirtual

# Generated at 2022-06-13 04:27:25.654990
# Unit test for constructor of class SunOSVirtual
def test_SunOSVirtual():
    sunos = SunOSVirtual()
    assert sunos.platform == 'SunOS'

# Generated at 2022-06-13 04:27:34.185276
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    from ansible.module_utils.facts.virtual import Virtual, VirtualCollector
    import copy
    import sys

    def run_command(self, cmd, tmp_path, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
        if cmd == 'zonename':
            return 0, 'global', ''
        elif cmd == 'modinfo':
            return 0, '', ''
        elif cmd == 'smbios':
            return 0, '', ''
        else:
            return 255, '', ''
    # Mock run_command for testing purposes
    orig_run_command = Virtual._run_command
    Virtual._run_command = run_command


# Generated at 2022-06-13 04:27:36.893935
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    """This is a useless test.  It doesn't do any validation,
    it just makes sure the constructor doesn't throw an exception.
    """
    x = SunOSVirtualCollector(None)

# Generated at 2022-06-13 04:27:41.833421
# Unit test for method get_virtual_facts of class SunOSVirtual
def test_SunOSVirtual_get_virtual_facts():
    # prepare an instance of MockModule
    # mixin: _load_platform_subclass
    facts_module = FakeAnsibleModule('ansible.module_utils.facts.virtual.sunos.SunOSVirtual')
    # initialize the instance with fake args, so the module thinks it's initialized
    facts_module.params = {}
    # mixin: load_collector
    SunOSVirtualCollector.load_collector(facts_module)
    # call the method under test
    sunos_virtual = SunOSVirtualCollector(facts_module)
    virtual_facts = sunos_virtual.get_virtual_facts()

# Generated at 2022-06-13 04:27:43.966250
# Unit test for constructor of class SunOSVirtualCollector
def test_SunOSVirtualCollector():
    obj = SunOSVirtualCollector('dummy')
    assert obj._platform == 'SunOS'
    assert obj._fact_class == SunOSVirtual