

# Generated at 2022-06-13 03:13:14.256647
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector('/etc/ansible/facts.d')
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system',
                                                      'kernel',
                                                      'kernel_version',
                                                      'machine',
                                                      'python_version',
                                                      'architecture',
                                                      'machine_id'])

# Generated at 2022-06-13 03:13:18.424097
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


# Generated at 2022-06-13 03:13:20.575129
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert 'kernel_version' in PlatformFactCollector()._fact_ids

# Generated at 2022-06-13 03:13:25.524357
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    instance = PlatformFactCollector()
    assert isinstance(instance, PlatformFactCollector)
    assert instance.__class__.__name__ == 'PlatformFactCollector'

    assert instance.name == 'platform'
    assert instance._fact_ids == set(['system',
                                      'kernel',
                                      'kernel_version',
                                      'machine',
                                      'python_version',
                                      'architecture',
                                      'machine_id'])

# Generated at 2022-06-13 03:13:35.192629
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    platform_platform = platform.platform()
    platform_system = platform.system()


# Generated at 2022-06-13 03:13:40.602480
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    Collector = PlatformFactCollector()
    assert Collector.name == 'platform'
    assert Collector.platform == 'all'
    assert Collector.depends == []
    assert Collector._fact_ids == set(['system',
                          'kernel',
                          'kernel_version',
                          'machine',
                          'python_version',
                          'architecture',
                          'machine_id'])


# Generated at 2022-06-13 03:13:46.264559
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert 'system' in x._fact_ids
    assert 'kernel' in x._fact_ids
    assert 'kernel_version' in x._fact_ids
    assert 'machine' in x._fact_ids
    assert 'python_version' in x._fact_ids
    assert 'architecture' in x._fact_ids
    assert 'machine_id' in x._fact_ids
    assert len(x._fact_ids) == 8


# Generated at 2022-06-13 03:13:52.673775
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


# Generated at 2022-06-13 03:13:59.018006
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pfc = PlatformFactCollector()
    facts = pfc.collect()
    assert ('architecture' in facts)
    assert ('machine' in facts)
    assert ('kernel' in facts)
    assert ('system' in facts)
    assert ('userspace_bits' in facts)
    assert ('python_version' in facts)
    assert ('hostname' in facts)
    assert ('domain' in facts)
    assert ('fqdn' in facts)
    assert ('machine_id' in facts)

# Generated at 2022-06-13 03:14:05.624055
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    p = PlatformFactCollector()
    retval = p.collect()
    assert(type(retval) is dict)
    assert('system' in retval)
    assert(type(retval['system']) is str)
    assert('kernel' in retval)
    assert(type(retval['kernel']) is str)
    assert('kernel_version' in retval)
    assert(type(retval['kernel_version']) is str)
    assert('machine' in retval)
    assert(type(retval['machine']) is str)
    assert('python_version' in retval)
    assert(type(retval['python_version']) is str)
    assert('fqdn' in retval)
    assert(type(retval['fqdn']) is str)

# Generated at 2022-06-13 03:15:13.384354
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


# Generated at 2022-06-13 03:15:16.582283
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pf = PlatformFactCollector()
    assert pf.name == 'platform'
    assert pf._fact_ids is not None
    assert len(pf._fact_ids) == 9

# Generated at 2022-06-13 03:15:20.868443
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert set(x._fact_ids) == set(['system',
                                    'kernel',
                                    'kernel_version',
                                    'machine',
                                    'python_version',
                                    'architecture',
                                    'machine_id'])


# Generated at 2022-06-13 03:15:25.903139
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    facts_collector = PlatformFactCollector()
    assert facts_collector and type(facts_collector) == PlatformFactCollector
    assert facts_collector.name == 'platform'
    assert facts_collector._fact_ids == set(['system',
                                             'kernel',
                                             'kernel_version',
                                             'machine',
                                             'python_version',
                                             'architecture',
                                             'machine_id'])

# Generated at 2022-06-13 03:15:31.388659
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert set(pfc._fact_ids) == set(['system',
                                      'kernel',
                                      'kernel_version',
                                      'machine',
                                      'python_version',
                                      'architecture',
                                      'machine_id'])


# Generated at 2022-06-13 03:15:39.317344
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector()
    assert obj.name == 'platform'

# Generated at 2022-06-13 03:15:43.018218
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x is not None
    assert x.name == 'platform'
    assert set(x.fact_ids()) == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture'])


# Generated at 2022-06-13 03:15:44.698984
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Assert that instance of PlatformFactCollector was created
    PlatformFactCollector()


# Generated at 2022-06-13 03:15:47.256269
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert p._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])


# Generated at 2022-06-13 03:15:49.524457
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fc = PlatformFactCollector()
    assert set(fc.collect()) == set(['system',
                                     'kernel',
                                     'kernel_version',
                                     'machine',
                                     'python_version',
                                     'architecture',
                                     'machine_id'])

# Generated at 2022-06-13 03:18:27.785829
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == {'system',
                           'kernel',
                           'kernel_version',
                           'machine',
                           'python_version',
                           'architecture',
                           'machine_id'}

# Generated at 2022-06-13 03:18:36.579935
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    def get_file_content(path):
        if path=="/var/lib/dbus/machine-id":
            return "15c8bfb9-0b3c-4d34-b76a-2cc6e5d7ad81\n"

    # create a mock module object
    module = type('ansible.module_utils.facts.platform.module')
    module.get_bin_path = lambda x: None
    module.run_command = lambda x: (0,"","")
    module.get_file_content = lambda x: get_file_content(x)

    platform_fact_collector = PlatformFactCollector()
    expected = "15c8bfb9-0b3c-4d34-b76a-2cc6e5d7ad81"
    assert platform_fact_collect

# Generated at 2022-06-13 03:18:40.337990
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


# Generated at 2022-06-13 03:18:43.244296
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()

    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == {'system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'}

# Generated at 2022-06-13 03:18:49.982066
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    pfc = PlatformFactCollector()
    import platform
    platform.system = lambda: 'Linux'
    platform.release = lambda: '3.11.0-15-generic'
    platform.version = lambda: '#25~precise1-Ubuntu SMP Thu Jan 30 17:37:01 UTC 2014'
    platform.machine = lambda: 'x86_64'
    platform.architecture = lambda: ['64bit', 'ELF']
    platform.python_version = lambda: '2.7.3'
    platform.uname = lambda: ['Linux', 'hostname00.domain00.com', '3.11.0-15-generic', '#25~precise1-Ubuntu SMP Thu Jan 30 17:37:01 UTC 2014', 'x86_64', 'x86_64']

    result = pfc.collect()

# Generated at 2022-06-13 03:18:55.469149
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

# Generated at 2022-06-13 03:19:05.095376
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

        # Create a mock object which is a subclass of BaseFactCollector
        class MockFactCollector(BaseFactCollector):
            name = 'dummy'

        # Create a new BaseModule object
        mock_module = base_builtin()

        # The following return values are standard for platform module
        # so we will use them for testing.

# Generated at 2022-06-13 03:19:08.164918
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    assert fact_collector.name == 'platform'
    assert set(fact_collector._fact_ids) == set(['system',
                                                 'kernel',
                                                 'kernel_version',
                                                 'machine',
                                                 'python_version',
                                                 'architecture',
                                                 'machine_id'])

# Generated at 2022-06-13 03:19:13.799908
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform = PlatformFactCollector()

# Generated at 2022-06-13 03:19:19.836895
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == {'architecture', 'fqdn', 'machine', 'machine_id', 'domain', 'kernel_version', 'userspace_architecture', 'system', 'python_version', 'nodename', 'hostname', 'userspace_bits', 'kernel'}