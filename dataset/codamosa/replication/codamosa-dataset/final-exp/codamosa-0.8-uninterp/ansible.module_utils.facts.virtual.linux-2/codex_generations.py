

# Generated at 2022-06-13 04:05:45.547622
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModuleMock()
    virtual_collector = LinuxVirtualCollector(module=module)
    assert virtual_collector._fact_class == LinuxVirtual
    assert virtual_collector._platform == 'Linux'


# Generated at 2022-06-13 04:05:47.747476
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    module = AnsibleModule(
        argument_spec = dict(
        ),
    )
    module.exit_json(changed=False, ansible_facts=dict(
        virtual=LinuxVirtual.get_virtual_facts(module)
    ))



# Generated at 2022-06-13 04:05:50.086001
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    fact_collector = LinuxVirtualCollector(module)
    assert fact_collector._fact_class == LinuxVirtual
    assert fact_collector._platform == 'Linux'


# Generated at 2022-06-13 04:05:50.987887
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    res = LinuxVirtual(dict())
    return res.get_virtual_facts()

# Generated at 2022-06-13 04:05:52.689276
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    coll = LinuxVirtualCollector(None)
    assert coll._platform == 'Linux'
    assert coll._fact_class == LinuxVirtual

# Generated at 2022-06-13 04:06:02.021296
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    class TestModule:
        def get_bin_path(name=None, opt_dirs=[]):
            return name

        def run_command(*args, **kw):
            return (0, '', '')
    class TestAnsibleModule:
        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            raise AssertionError(msg)

        def exit_json(self, **kw):
            pass

        def get_bin_path(self, name=None, opt_dirs=[]):
            return TestModule.get_bin_path(name, opt_dirs)

        def run_command(self, *args, **kw):
            return TestModule.run_command(*args, **kw)

        def __getitem__(self, item):
            return self

# Generated at 2022-06-13 04:06:03.938397
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    facts = LinuxVirtualCollector()
    assert facts == {'virtualization_type': None,
                     'virtualization_role': None,
                     'virtualization_tech_guest': None,
                     'virtualization_tech_host': None }


# Generated at 2022-06-13 04:06:05.146475
# Unit test for constructor of class LinuxVirtualCollector
def test_LinuxVirtualCollector():
    x = LinuxVirtualCollector()
    assert x._fact_class == LinuxVirtual
    assert x._platform == 'Linux'



# Generated at 2022-06-13 04:06:16.383393
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch


# Generated at 2022-06-13 04:06:21.268306
# Unit test for method get_virtual_facts of class LinuxVirtual
def test_LinuxVirtual_get_virtual_facts():
    """Unit test for method get_virtual_facts"""
    host_facts = dict()
    virtual = LinuxVirtual(dict(), host_facts)
    host_facts = dict()
    assert virtual.get_virtual_facts() == dict(virtualization_role='NA', virtualization_type='NA',
                                               virtualization_tech_guest=set(), virtualization_tech_host=set())
