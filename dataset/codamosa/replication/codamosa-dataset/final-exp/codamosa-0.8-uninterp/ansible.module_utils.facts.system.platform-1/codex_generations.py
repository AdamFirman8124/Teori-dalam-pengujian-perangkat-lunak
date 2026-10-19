

# Generated at 2022-06-13 03:13:10.999095
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert set(['system',
                'kernel',
                'kernel_version',
                'machine',
                'python_version',
                'architecture',
                'machine_id']) == PlatformFactCollector()._fact_ids

# Generated at 2022-06-13 03:13:13.903313
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert p._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:13:15.086830
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector().name == 'platform'

# Generated at 2022-06-13 03:13:21.209216
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    plat_fc = PlatformFactCollector()
    assert(set([ 'system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id']) == plat_fc._fact_ids)
    assert('platform' == plat_fc.name)

# Generated at 2022-06-13 03:13:26.555224
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    mock_module = MockModule()
    platform_collector = PlatformFactCollector()

# Generated at 2022-06-13 03:13:28.622995
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x.collect()

# Generated at 2022-06-13 03:13:33.610690
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == set(['system',
                     'kernel',
                     'kernel_version',
                     'machine',
                     'python_version',
                     'architecture',
                     'machine_id'])
    assert platform_collector.__doc__ is None

# Generated at 2022-06-13 03:13:39.694493
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id',
                               'fqdn',
                               'hostname',
                               'nodename',
                               'domain'])
    assert not x.collect()

# Generated at 2022-06-13 03:13:40.934756
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    facts = PlatformFactCollector()
    print(facts)


# Generated at 2022-06-13 03:13:48.530863
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    from ansible.module_utils.facts import __file__ as facts_file
    import os
    import sys
    import imp

    # find the path of ansible/module_utils/facts
    facts_path = os.path.realpath(os.path.dirname(facts_file))

    # find the path of ansible/module_utils/facts/collector
    collector_path = os.path.realpath(os.path.dirname(os.path.dirname(facts_path)))

    # modify sys.path to include the path of collector
    sys.path.append(collector_path)

    # import BaseFactCollector
    fh, filename, desc = imp.find_module('BaseFactCollector')
    imp.load_module('BaseFactCollector', fh, filename, desc)

    # create a PlatformFact

# Generated at 2022-06-13 03:14:19.638445
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:14:29.337972
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    class MockModule(object):
        def __init__(self):
            self.run_command_calls = []

        def get_bin_path(self, name, required=True):
            if name == 'getconf':
                return '/usr/bin/getconf'
            elif name == 'bootinfo':
                return '/usr/sbin/bootinfo'
            else:
                return None


    def run_command_fn(*args, **kwargs):
        mock_module.run_command_calls.append((args, kwargs))
        return (0, '', '')

    mock_module = MockModule()
    mock_module.run_command = run_command_fn
    platform_collector = PlatformFactCollector()
    collected_facts = platform_collector.collect(mock_module)


# Generated at 2022-06-13 03:14:33.996682
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Test setting of module_name and fact_ids
    pf = PlatformFactCollector("foo")
    assert pf.module_name == "foo"
    assert pf._fact_ids == PlatformFactCollector._fact_ids


# Generated at 2022-06-13 03:14:43.282738
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts.name == 'platform', 'Test Failed: could not get right collector name'
    assert 'system' in platform_facts._fact_ids, 'Test Failed: platform_facts does not have "system" in fact'
    assert 'kernel' in platform_facts._fact_ids, 'Test Failed: platform_facts does not have "kernel" in fact'
    assert 'kernel_version' in platform_facts._fact_ids, 'Test Failed: platform_facts does not have "kernel_version" in fact'
    assert 'python_version' in platform_facts._fact_ids, 'Test Failed: platform_facts does not have "python_version" in fact'

# Generated at 2022-06-13 03:14:51.353093
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()
    assert pf.name == 'platform'
    assert 'system' in pf._fact_ids
    assert 'kernel' in pf._fact_ids
    assert 'kernel_version' in pf._fact_ids
    assert 'machine' in pf._fact_ids
    assert 'python_version' in pf._fact_ids
    assert 'architecture' in pf._fact_ids
    assert 'machine_id' in pf._fact_ids

# Generated at 2022-06-13 03:14:55.491282
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == "platform"
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:14:58.899184
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # create instance of PlatformFactCollector class
    platform_fact_collector = PlatformFactCollector()

    # test variables
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:15:02.568877
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
   """Test PlatformFactCollector.collect()."""
   fact_collector = PlatformFactCollector()
   fact_collector.collect()

# Generated at 2022-06-13 03:15:09.983161
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pc = PlatformFactCollector()
    assert pc.collect() == {'system': platform.system(), 'kernel': platform.release(), 'kernel_version': platform.version(), 'machine': platform.machine(), 'python_version': platform.python_version(), 'fqdn': socket.getfqdn(), 'hostname': socket.getfqdn().split('.')[0], 'nodename': platform.node(), 'domain': socket.getfqdn().split('.')[1:], 'userspace_bits': platform.architecture()[0].replace('bit',''), 'architecture': platform.machine(), 'userspace_architecture': platform.architecture()[0].replace('bit','')}

# Generated at 2022-06-13 03:15:11.864333
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector().collect()
    for fact_name in PlatformFactCollector._fact_ids:
        assert fact_name in platform_facts

# Generated at 2022-06-13 03:15:24.423991
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()
    assert 'platform' == pf.name
    assert 'system' in pf._fact_ids
    assert 'architecture' in pf._fact_ids
    assert 'machine_id' in pf._fact_ids

# Generated at 2022-06-13 03:15:26.749006
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert type(x) == PlatformFactCollector


# Generated at 2022-06-13 03:15:35.894839
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import json
    import re
    from ansible.module_utils.facts import FactCollector

    class MockModule(object):
        def __init__(self):
            self.run_command_calls = 0
            self.run_command_rcs = []
            self.run_command_outs = []
            self.run_command_errs = []
            self.run_command_expect_calls = {}
            self.run_command_expect_rcs = {}
            self.run_command_expect_outs = {}
            self.run_command_expect_errs = {}
            self.get_bin_path_calls = 0
            self.get_bin_path_returns = {}
        def get_bin_path(self, arg, opt_dirs=[]):
            self.get_

# Generated at 2022-06-13 03:15:39.290269
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == set(['system',
                                                'kernel',
                                                'kernel_version',
                                                'machine',
                                                'architecture',
                                                'python_version',
                                                'machine_id'])

# Generated at 2022-06-13 03:15:41.279777
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector_obj = PlatformFactCollector()
    assert type(collector_obj) == PlatformFactCollector

# Generated at 2022-06-13 03:15:47.321731
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """Test PlatformFactCollector instantiation"""

    platform_fact_collector = PlatformFactCollector()

    assert platform_fact_collector
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])

# Generated at 2022-06-13 03:15:57.259722
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pc = PlatformFactCollector()


# Generated at 2022-06-13 03:15:58.597328
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # All methods of this class are private and should not be tested directly
    pass

# Generated at 2022-06-13 03:15:59.174924
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()

# Generated at 2022-06-13 03:16:13.032876
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

# Generated at 2022-06-13 03:16:58.316463
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x

# Generated at 2022-06-13 03:17:03.739330
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # platform.system() can be Linux, Darwin, Java, or Windows
    ohai_facts = {}
    ohai_facts['kernel'] = dict(release="3.10.0-693.el7.x86_64")
    ohai_facts['kernel_osrelease'] = "3.10.0-693.el7.x86_64"
    ohai_facts['kernel_name'] = "Linux"
    ohai_facts['id'] = "centos"
    ohai_facts['os'] = "linux"
    ohai_facts['kernel_osrelease_major'] = "3.10.0-693.el7.x86_64"
    ohai_facts['hostname'] = "test.test.test"
    ohai_facts['fqdn'] = "test.test.test"
    ohai

# Generated at 2022-06-13 03:17:10.826922
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert 'system' in p._fact_ids
    assert 'kernel' in p._fact_ids
    assert 'kernel_version' in p._fact_ids
    assert 'machine' in p._fact_ids
    assert 'python_version' in p._fact_ids
    assert 'architecture' in p._fact_ids
    assert 'machine_id' in p._fact_ids
    assert len(p._fact_ids) == 7
    assert p.name == 'platform'

# Generated at 2022-06-13 03:17:17.101450
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_collector = PlatformFactCollector()
    platform_facts = platform_collector.collect()
    assert 'system' in platform_facts
    assert 'kernel' in platform_facts
    assert 'kernel_version' in platform_facts
    assert 'machine' in platform_facts
    assert 'python_version' in platform_facts
    assert 'architecture' in platform_facts
    assert 'machine_id' in platform_facts

# Generated at 2022-06-13 03:17:20.025790
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:17:23.543174
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platformFacts = PlatformFactCollector()
    assert platformFacts.name == "platform"
    assert platformFacts._fact_ids == set(['system',
                                           'kernel',
                                           'kernel_version',
                                           'machine',
                                           'python_version',
                                           'architecture',
                                           'machine_id'])

# Generated at 2022-06-13 03:17:32.724300
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    import ansible.module_utils.facts.collector

    collector = Collector()
    platform_fact_collector = PlatformFactCollector()

    new_collector_list = [
        {'platform': platform_fact_collector},
        {'network': None},
        {'facter': None},
    ]

    # Adding PlatformFactCollector to Collector
    collector._collectors = new_collector_list

    # Collecting Facts
    ansible.module_utils.facts.collector.collect(collector)

    print("Facts: {}".format(collector.facts))

if __name__ == '__main__':
    test_PlatformFactCollector_collect()

# Generated at 2022-06-13 03:17:34.878809
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    names = set()
    names.update(pfc._fact_ids)
    names.add(pfc.name)
    assert  names == pfc.names

# Generated at 2022-06-13 03:17:38.086736
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])
    assert pfc._platform == 'posix'
    assert pfc._file_path == '/etc/ansible/facts.d'


# Generated at 2022-06-13 03:17:40.179076
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'
    assert PlatformFactCollector._fact_ids == {'system', 'kernel', 'kernel_version',
                                               'machine', 'python_version', 'architecture',
                                               'machine_id'}

# Generated at 2022-06-13 03:19:04.411536
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
    assert type(platform_fact_collector._fact_ids) == set

# Generated at 2022-06-13 03:19:10.686002
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    def get_bin_path(bin_path):
        return '/usr/bin/' + bin_path

    def run_command(args):
        if args[0] == '/usr/bin/getconf':
            return 0, 'amd64', ''
        if args[0] == '/usr/sbin/bootinfo':
            return 0, 'powerpc', ''

    module = type('AnsibleModule', (object, ),
                  {'get_bin_path': get_bin_path, 'run_command': run_command})()
    collector = PlatformFactCollector()
    facts = collector.collect(module=module)
    assert facts['architecture'] == 'amd64'
    assert facts['machine_id'] == ''

# Generated at 2022-06-13 03:19:17.185768
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert p._fact_ids == {'system',
                           'kernel',
                           'kernel_version',
                           'machine',
                           'python_version',
                           'architecture',
                           'machine_id'}


# Generated at 2022-06-13 03:19:23.953594
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = MagicMock()
    machine_id = "machine_id"
    module.get_bin_path = MagicMock(return_value = "bin_path")
    module.run_command = MagicMock(return_value = [0, "out", "err"])
    platform_facts = PlatformFactCollector().collect(module, "collected_facts")
    assert platform_facts["system"] == "Linux"
    assert platform_facts["machine"] == "x86_64"
    assert platform_facts["machine_id"] == "machine_id"

# Generated at 2022-06-13 03:19:32.069057
# Unit test for method collect of class PlatformFactCollector

# Generated at 2022-06-13 03:19:37.664235
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    import pytest
    collector = PlatformFactCollector()
    assert not collector.collect_fn
    assert collector.name == 'platform'
    assert collector._fact_ids == {'system',
                                   'kernel',
                                   'kernel_version',
                                   'machine',
                                   'python_version',
                                   'architecture',
                                   'machine_id'}
    assert collector.platforms == set()

# Generated at 2022-06-13 03:19:43.006779
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

# Generated at 2022-06-13 03:19:47.402469
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert(platform_facts.name == 'platform')
    assert(platform_facts._fact_ids == set(['system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id']))

# Generated at 2022-06-13 03:19:51.262197
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    """This will work only for python2.7"""
    platform_obj = PlatformFactCollector()
    print("Name of object ", platform_obj.name)
    print("Facts ids of object ", platform_obj._fact_ids)
    platform_obj.collect()

if __name__ == "__main__":
    test_PlatformFactCollector()

# Generated at 2022-06-13 03:19:56.634677
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])
    assert getattr(x, 'collect')
    assert getattr(x, '__doc__')