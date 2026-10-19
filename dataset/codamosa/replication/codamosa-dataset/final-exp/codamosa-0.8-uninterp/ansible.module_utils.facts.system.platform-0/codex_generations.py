

# Generated at 2022-06-13 03:13:13.967089
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create a test object
    platform_fact_collector = PlatformFactCollector()
    # Collect facts
    platform_facts = platform_fact_collector.collect(collected_facts=None)

    # Assert that the platform facts returned match the expected facts
    assert set(platform_facts.keys()).issuperset(set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id']))

# Generated at 2022-06-13 03:13:18.067990
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == "platform"
    assert platform_collector._fact_ids == set([
        'system', 'kernel', 'kernel_version', 'machine',
        'python_version', 'architecture', 'machine_id'])


# Generated at 2022-06-13 03:13:28.109123
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Pretend the platform is Linux x86_64 or Linux x86
    module_mock = type('', (), dict(get_bin_path=lambda self, executable: None))()

# Generated at 2022-06-13 03:13:33.732812
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert set(platform_fact_collector._fact_ids) == set(['system',
                                                          'kernel',
                                                          'kernel_version',
                                                          'machine',
                                                          'python_version',
                                                          'architecture',
                                                          'machine_id'])

# Generated at 2022-06-13 03:13:43.266838
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids is not None
    assert len(pfc._fact_ids) == 10
    assert 'system' in pfc._fact_ids
    assert 'kernel' in pfc._fact_ids
    assert 'kernel_version' in pfc._fact_ids
    assert 'machine' in pfc._fact_ids
    assert 'python_version' in pfc._fact_ids
    assert 'architecture' in pfc._fact_ids
    assert 'machine_id' in pfc._fact_ids
    assert 'userspace_bits' in pfc._fact_ids
    assert 'userspace_architecture' in pfc._fact_ids
    assert 'fqdn' in pfc._fact_ids

# Generated at 2022-06-13 03:13:46.422813
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()

    # TODO: Add real unit tests here
    assert pfc is not None

# Generated at 2022-06-13 03:13:51.949402
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'
    assert PlatformFactCollector._fact_ids == set(['system',
                                                   'kernel',
                                                   'kernel_version',
                                                   'machine',
                                                   'python_version',
                                                   'architecture',
                                                   'machine_id'])


# Generated at 2022-06-13 03:13:52.628502
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'

# Generated at 2022-06-13 03:13:57.314058
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()

    assert platform_fact_collector.name == 'platform'

    # Test whether all the supported fact names are present in PlatformFactCollector
    assert set(platform_fact_collector.fact_names()) == platform_fact_collector._fact_ids

# Generated at 2022-06-13 03:14:03.424295
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    flavor = 'linux'
    platform = PlatformFactCollector(flavor)
    assert platform.name == 'platform'
    assert platform._fact_ids == {'system',
                                  'kernel',
                                  'kernel_version',
                                  'machine',
                                  'python_version',
                                  'architecture',
                                  'machine_id'}

# Generated at 2022-06-13 03:14:55.975972
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Set up mock facts
    collected_facts = {
        "machine_id": "FF91D4BC-0F03-4E5F-9B75-D5C794E546F8",
        "machine": "x86_64",
        "fqdn": "test.host",
        "system": "Linux"
    }

    # Set up the instance to test
    pfc = PlatformFactCollector()

    # Set up the mock module
    fake_module = type('fake_module', (object,), {})()
    fake_module.get_bin_path = lambda x: None

    # Test the method
    result = pfc.collect(module=fake_module, collected_facts=collected_facts)
    assert result["system"] == "Linux"

# Generated at 2022-06-13 03:15:06.252050
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, arg):
            return '/bin/%s' % arg

        def run_command(self, args):
            # return rc, out, err
            if args == ['/bin/getconf', 'MACHINE_ARCHITECTURE']:
                return (0, 'powerpc', '')
            elif args == ['/bin/bootinfo', '-p']:
                return (0, 'powerpc', '')
            elif args == ['/bin/uname', '-m']:
                return (0, 'amd64', '')
            else:
                raise NotImplementedError()

    module = TestModule()

# Generated at 2022-06-13 03:15:14.635134
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import socket
    import re
    import os
    import platform
    import sys

    class MockModule():
        def __init__(self, params = None):
            self.params = params

        def get_bin_path(self, module_name, required=True):
            if module_name == 'getconf':
                return None
            if module_name == 'bootinfo':
                return "fake_path"

        def run_command(self, command):
            if command[-1] == 'MACHINE_ARCHITECTURE':
                return (0, 'powerpc64le', '')
            if command[-1] == '-p':
                return (0, 'powerpc64le', '')

    class MockModuleUtils():
        def __init__(self, params = None):
            self.params

# Generated at 2022-06-13 03:15:19.376439
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == \
           set(['system', 'kernel', 'kernel_version', 'machine',
                'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:15:23.665600
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


# Generated at 2022-06-13 03:15:28.858773
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils import basic
    import  platform
    platform_facts = {}
    # platform.system() can be Linux, Darwin, Java, or Windows
    platform_facts['system'] = platform.system()
    platform_facts['kernel'] = platform.release()
    platform_facts['kernel_version'] = platform.version()
    platform_facts['machine'] = platform.machine()

    platform_facts['python_version'] = platform.python_version()

    platform_facts['fqdn'] = socket.getfqdn()
    platform_facts['hostname'] = platform.node().split('.')[0]
    platform_facts['nodename'] = platform.node()

    platform_facts['domain'] = '.'.join(platform_facts['fqdn'].split('.')[1:])


# Generated at 2022-06-13 03:15:33.488436
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PF = PlatformFactCollector()
    assert 'system' in PF._fact_ids
    assert 'kernel' in PF._fact_ids
    assert 'kernel_version' in PF._fact_ids
    assert 'machine' in PF._fact_ids
    assert 'python_version' in PF._fact_ids
    assert 'architecture' in PF._fact_ids
    assert 'machine_id' in PF._fact_ids

# Generated at 2022-06-13 03:15:35.950010
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Initialize the class PlatformFactCollector
    PlatformFactCollector_obj = PlatformFactCollector()
    # Call method collect of class PlatformFactCollector
    PlatformFactCollector_obj.collect(collected_facts=None)


# Generated at 2022-06-13 03:15:39.552179
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert isinstance(pfc, PlatformFactCollector)
    assert pfc.name == 'platform'
    assert pfc._fact_ids == {'system',
                             'kernel',
                             'kernel_version',
                             'machine',
                             'python_version',
                             'architecture',
                             'machine_id'}


# Generated at 2022-06-13 03:15:43.992941
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()

    assert platform_collector.name == "platform"
    assert platform_collector._fact_ids == set(['system',
                                                'kernel',
                                                'kernel_version',
                                                'machine',
                                                'python_version',
                                                'architecture',
                                                'machine_id'])

# Generated at 2022-06-13 03:17:06.085543
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])



# Generated at 2022-06-13 03:17:15.268387
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """
    Returns collected_facts to be used for unittests.
    Method collect of class PlatformFactCollector returns the
    facts for the platform using the python module platform.
    """
    # Create a dummy module object
    class DummyModule():
        def __init__(self):
            self.params = {}
        def get_bin_path(self, arg):
            return '/bin/' + arg
        def run_command(self, arg):
            return (0, '1', '')
    module = DummyModule()
    # Create a dummy ansible_facts object with an empty ansible_platform variable
    ansible_facts = {}
    ansible_facts['ansible_platform'] = {}
    # Instantiate PlatformFactCollector object
    PlatformFactCollector_obj = PlatformFactCollector()
    # Call method collect of Platform

# Generated at 2022-06-13 03:17:17.266116
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_fc = PlatformFactCollector()
    platform_fc.collect()

# Generated at 2022-06-13 03:17:19.935310
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set([
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id'])


# Generated at 2022-06-13 03:17:20.894590
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    instance = PlatformFactCollector()
    assert instance.name == 'platform'

# Generated at 2022-06-13 03:17:26.829543
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert len(platform_fact_collector._fact_ids) == 8
    assert 'system' in platform_fact_collector._fact_ids
    assert 'kernel' in platform_fact_collector._fact_ids
    assert 'kernel_version' in platform_fact_collector._fact_ids
    assert 'machine' in platform_fact_collector._fact_ids
    assert 'python_version' in platform_fact_collector._fact_ids
    assert 'architecture' in platform_fact_collector._fact_ids
    assert 'machine_id' in platform_fact_collector._fact_ids
    # assert 'fqdn' in platform_fact_collector._fact_ids

# Generated at 2022-06-13 03:17:29.695486
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == "platform"
    assert 'fqdn' in p._fact_ids
    assert p.name not in p._fact_ids



# Generated at 2022-06-13 03:17:36.100778
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    facts = PlatformFactCollector().collect()
    assert 'system' in facts
    assert facts['system'] == platform.system()
    assert 'kernel' in facts
    assert facts['kernel'] == platform.release()
    assert 'kernel_version' in facts
    assert facts['kernel_version'] == platform.version()
    assert 'machine' in facts
    assert facts['machine'] == platform.machine()
    assert 'python_version' in facts
    assert facts['python_version'] == platform.python_version()
    assert 'fqdn' in facts
    assert facts['fqdn'] == socket.getfqdn()
    assert 'hostname' in facts
    assert facts['hostname'] == platform.node().split('.')[0]
    assert 'nodename' in facts
    assert facts['nodename'] == platform.node()

# Generated at 2022-06-13 03:17:40.088257
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x._fact_ids == {
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id'
    }
    assert x.name == 'platform'

# Generated at 2022-06-13 03:17:49.801223
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import mock


# Generated at 2022-06-13 03:21:10.377860
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert set(platform_collector._fact_ids) == set(['system', 'kernel', 'kernel_version', 'machine', 'architecture'])

# Generated at 2022-06-13 03:21:18.811497
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector.platform import PlatformFactCollector
    import platform
    import socket
    import os
    import re
    import sys

    class TestModule:
        def __init__(self):
            self.params = None

        def get_bin_path(self, application):
            app_map = {
                'bootinfo': '/usr/bin/bootinfo',
                'getconf': '/usr/bin/getconf',
            }

            if application in app_map:
                return app_map[application]
            else:
                return None

        def run_command(self, cmd):
            return (0, '', '')

    test_module = TestModule()
    test_collector = PlatformFactCollector(test_module)
    test_facts = test_collector.collect()



# Generated at 2022-06-13 03:21:24.842488
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_data = {}
    platform_data['system'] = 'Linux'
    platform_data['kernel'] = '3.10.0-123.el7.x86_64'
    platform_data['kernel_version'] = '#1 SMP Wed Sep 10 12:42:42 EDT 2014'
    platform_data['machine'] = 'x86_64'
    platform_data['python_version'] = '2.7.5'
    platform_data['fqdn'] = 'local-machine.localdomain'
    platform_data['hostname'] = 'local-machine'
    platform_data['nodename'] = 'local-machine'
    platform_data['domain'] = 'localdomain'
    platform_data['userspace_bits'] = '64'

# Generated at 2022-06-13 03:21:33.345686
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = mock.MagicMock()
    module.run_command.return_value = "test_command", "test_output", "test_error"
    platform_fact_collector = PlatformFactCollector()
    output = platform_fact_collector.collect(module=module)

# Generated at 2022-06-13 03:21:36.866249
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts.name == "platform"
    assert set(platform_facts._fact_ids) == set(['system',
                                                 'kernel',
                                                 'kernel_version',
                                                 'machine',
                                                 'python_version',
                                                 'architecture',
                                                 'machine_id'])

# Generated at 2022-06-13 03:21:39.434970
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()

    assert pfc.name == 'platform'
    assert 'system' in pfc._fact_ids
    assert pfc.collect()
    assert "system" in pfc.collect()


# Generated at 2022-06-13 03:21:43.203497
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(0, 'x86_64', ''))
    mock_module.get_bin_path = Mock(return_value=True)
    mock_module.get_file_content = Mock(return_value='abc123')

    fact_collector = PlatformFactCollector()
    fact_collector.collect(module=mock_module)

# Generated at 2022-06-13 03:21:46.737729
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])

# Generated at 2022-06-13 03:21:49.845668
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                     'kernel',
                     'kernel_version',
                     'machine',
                     'python_version',
                     'architecture',
                     'machine_id'])

# Generated at 2022-06-13 03:21:52.922226
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platformFactCollector = PlatformFactCollector()
    assert platformFactCollector.name == 'platform'
    assert platformFactCollector._fact_ids == set(['system',
                                                   'kernel',
                                                   'kernel_version',
                                                   'machine',
                                                   'python_version',
                                                   'architecture',
                                                   'machine_id'])
