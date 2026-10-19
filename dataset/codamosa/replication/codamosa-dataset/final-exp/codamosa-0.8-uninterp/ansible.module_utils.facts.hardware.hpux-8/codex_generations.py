

# Generated at 2022-06-13 00:45:32.404265
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    """
    Test method populate of class HPUXHardware
    """

    module = AnsibleModule(argument_spec=dict())

    # Create a dummy class with fixed methods/attributes
    class DummyClass(object):
        def __init__(self, params):
            self.params = params
            self.module = module

        def get_memory_facts(self):
            return {
                'memfree_mb': 8704,
                'swaptotal_mb': 8192,
                'swapfree_mb': 8192
            }

        def get_cpu_facts(self):
            return {
                'processor': 'Intel(R) Xeon(R) CPU X5550 @ 2.67GHz',
                'processor_cores': 4,
                'processor_count': 4
            }


# Generated at 2022-06-13 00:45:35.055534
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h_c = HPUXHardwareCollector()
    assert isinstance(h_c, HPUXHardwareCollector)
    assert isinstance(h_c._fact_class, HPUXHardware)
    assert h_c._platform == 'HP-UX'
    assert h_c.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:45:47.561850
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    facts = {}
    facts['ansible_architecture'] = '9000/800'
    # load collected facts
    hw = HPUXHardware.init_module(facts)
    collected_facts = hw.populate()
    assert collected_facts.get('processor_count') == 2
    facts['ansible_architecture'] = 'ia64'
    # load collected facts
    facts['ansible_distribution_version'] = "B.11.23"
    hw = HPUXHardware.init_module(facts)
    collected_facts = hw.populate()
    assert collected_facts.get('processor') == 'Intel(r) Itanium(r) processor 9000 series'
    assert collected_facts.get('processor_cores') == 2
    # load collected facts

# Generated at 2022-06-13 00:45:50.393917
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardwareCollector = HPUXHardwareCollector()
    assert hardwareCollector._platform == 'HP-UX'
    assert hardwareCollector._fact_class == HPUXHardware

# Generated at 2022-06-13 00:45:56.153325
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    facts_dict = {
        'platform': 'HP-UX',
        'distribution': 'HP-UX',
        'architecture': 'ia64'
    }
    l = list(HPUXHardwareCollector.detect(facts_dict, None))
    assert len(l) == 1
    assert l[0].platform == 'HP-UX'
    assert l[0]._fact_class == HPUXHardware

# Generated at 2022-06-13 00:46:00.598981
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(argument_spec=dict())
    hw = HPUXHardware(module)
    hw_facts = hw.get_hw_facts(collected_facts=dict(ansible_architecture='ia64'))
    assert hw_facts['firmware_version'] == 'C.7.17.0'



# Generated at 2022-06-13 00:46:04.277315
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    """Unit test for constructor of class HPUXHardwareCollector."""

    # Construct and destroy the class
    obj = HPUXHardwareCollector()
    obj.post_proc_facts()



# Generated at 2022-06-13 00:46:13.374954
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware()
    collected_facts = {'ansible_distribution_version': 'B.11.23',
                       'ansible_architecture': 'ia64'}
    cpu_facts = hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor'] == 'Intel(r) Itanium 2 9100 series processor'
    assert cpu_facts['processor_cores'] == 2

    collected_facts = {'ansible_distribution_version': 'B.11.31',
                       'ansible_architecture': 'ia64'}
    cpu_facts = hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 2

# Generated at 2022-06-13 00:46:15.763834
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    hardware = HPUXHardware(dict(module=dict(run_command=_run_command)))
    hardware.get_memory_facts()



# Generated at 2022-06-13 00:46:17.811850
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
  hpux_hardware_collector = HPUXHardwareCollector()

  assert hpux_hardware_collector._platform == 'HP-UX'
  assert hpux_hardware_collector.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:46:47.849941
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    #create a class instance
    hphw = HPUXHardware(dict())

    # get movic version
    rc, out, err = hphw.module.run_command("model")
    movie_id = out.strip()

    # check if current machine is an ia64
    rc, out, err = hphw.module.run_command("/usr/contrib/bin/machinfo")
    if "ia64" in out:
        ansible_architecture = "ia64"
    else:
        ansible_architecture = "9000/800"

    # get ia64 hardware facts
    hphw_facts = hphw.get_hw_facts(collected_facts={"ansible_architecture": ansible_architecture})

# Generated at 2022-06-13 00:46:52.938236
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    x = HPUXHardware()
    x.module = Mock()
    x.module.run_command.return_value = (0, " ", " ")
    assert x.get_memory_facts() == {}
    x.module.run_command.return_value = (0, "     9", " ")
    x.get_memory_facts() == {}


# Generated at 2022-06-13 00:46:57.045145
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():

    # Create an HPUXHardware instance
    collector = HPUXHardwareCollector()

    # Assert that the HPUXHardwareCollector constructor has created the
    # collector correctly.
    assert collector.platform == 'HP-UX'
    assert collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:47:07.428998
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Setup
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = MagicMock(return_value=(0, 'ok', ''))
    module.exit_json = MagicMock()

    facter_module = HPUXHardware(module)
    facter_module.module.exit_json = MagicMock()

    rc, out, err = facter_module.get_hw_facts({'ansible_architecture': 'ia64'})
    output = {"model": "ok", "firmware_version": "ok", "product_serial": "ok"}
    assert rc == output

# Generated at 2022-06-13 00:47:12.951120
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    basic_module = AnsibleModule(
        argument_spec=dict()
    )
    hardware = HPUXHardware(basic_module)
    facts = hardware.get_hw_facts()
    assert facts['model'] == 'HP-UX', "Incorrect model for HP-UX"
    assert 'firmware_version' in facts, "No firmware_version key for HP-UX"
    assert 'product_serial' in facts, "No product_serial key for HP-UX"



# Generated at 2022-06-13 00:47:17.832095
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.hardware.hpe import HPUXHardware
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text

    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    fact_collector = FactCollector(module,
                                   gather_subset=['all'],
                                   gather_timeout=5,
                                   loader=module._loader,
                                   spool_dir=None,
                                   # and then the list of supported platforms for our Networking Facts class
                                   supported_platforms=HPUXHardware.platform)

# Generated at 2022-06-13 00:47:23.681412
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    import platform
    import pytest
    facts = {'platform': 'HP-UX',
             'distribution': platform.mac_ver()[0]}

    hw = HPUXHardwareCollector(facts)
    assert isinstance(hw, HPUXHardwareCollector)
    assert isinstance(hw.platform, str)
    assert hw.platform == "HP-UX"
    assert isinstance(hw.required_facts, set)
    assert facts['platform'] in hw.required_facts
    assert facts['distribution'] in hw.required_facts


if __name__ == '__main__':
    pytest.main([__file__, '-vvv'])

# Generated at 2022-06-13 00:47:31.344472
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    # Arrange
    module = MockModule()
    module.run_command = Mock(return_value=(0, "4\n", ""))
    hw = HPUXHardware(module)
    hw.populate_from_file('')

    # Act
    result = hw.get_cpu_facts(collected_facts={'ansible_architecture': '9000/800'})

    # Assert
    assert result == {'processor': None, 'processor_count': 4, 'processor_cores': None}, "Failed to parse cpu facts"


# Generated at 2022-06-13 00:47:40.227962
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """
    Unit test of method HPUXHardware.get_cpu_facts
    """
    # Make fake class for testing
    class FakeModule:
        def __init__(self, params):
            pass

        def run_command(self, cmd, use_unsafe_shell=None):
            return 0, '', ''

    params = {}
    h = HPUXHardware(FakeModule(params))

    def _run_get_cpu_facts(architecture, distribution_version, res):
        collected_facts = {'ansible_architecture': architecture, 'ansible_distribution_version': distribution_version}
        cpu_facts = h.get_cpu_facts(collected_facts=collected_facts)
        assert cpu_facts['processor_count'] == res
        #i = 0
        #for key,value in

# Generated at 2022-06-13 00:47:46.756328
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    """Unit test for method get_hw_facts of class HPUXHardware
    This test verifies that fact dict contains model and firmware."""
    module = AnsibleModule(argument_spec=dict())
    fact_list = HPUXHardwareCollector(module).collect()
    assert('model' in fact_list)
    assert('firmware_version' in fact_list)



# Generated at 2022-06-13 00:48:18.142665
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_coll = HPUXHardwareCollector()
    assert hardware_coll._fact_class == HPUXHardware
    assert hardware_coll._platform == 'HP-UX'
    assert hardware_coll.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:48:25.609742
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    # Creating instance of class HPUXHardwareCollector
    collector = HPUXHardwareCollector()

    # Testing the instance of class HPUXHardwareCollector
    assert isinstance(collector, HPUXHardwareCollector)
    assert isinstance(collector._fact_class, HPUXHardware)
    assert collector._platform == 'HP-UX'
    assert collector.required_facts == set(['platform', 'distribution'])
    assert collector.optional_facts == set([])
    assert collector.init_required_facts == set([])
    assert collector.init_optional_facts == set(['ansible_architecture', 'ansible_distribution_version'])


# Generated at 2022-06-13 00:48:35.749414
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware()
    hw.module = MockModule()
    hw.module.run_command = Mock()
    hw.module.run_command.return_value = ('0', '16', '')
    os.access = Mock()
    os.access.return_value = False

    # Test with 9000/800
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 16

    # Test with 9000/785
    collected_facts = {'ansible_architecture': '9000/785'}
    cpu_facts = hw.get_cpu_facts(collected_facts=collected_facts)
   

# Generated at 2022-06-13 00:48:45.651183
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware()
    hardware.module = MockModule()
    hardware.module.run_command.return_value = (0, 'B.11.31 U ia64', '')
    hardware.module.get_bin_path.return_value = '/usr/contrib/bin/machinfo'
    hardware.module.run_command.return_value = (0, '', '')
    hardware.module.run_command.return_value = (0, 'B.11.31 U ia64', '')
    hardware.module.get_bin_path.return_value = '/usr/contrib/bin/machinfo'
    hardware.module.run_command.return_value = (0, '', '')

# Generated at 2022-06-13 00:48:59.294679
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    target_inst = HPUXHardware({})
    collected_facts = {'ansible_architecture': '9000/800',
                       'ansible_distribution_version': 'B.11.23',
                       'ansible_facts': {}}
    ret = target_inst.get_cpu_facts(collected_facts=collected_facts)
    assert 'processor_count' in ret
    assert 'processor' not in ret
    assert 'processor_cores' not in ret
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    ret = target_inst.get_cpu_facts(collected_facts=collected_facts)
    assert 'processor_count' in ret
    assert 'processor' in ret

# Generated at 2022-06-13 00:49:04.530714
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    test_obj = HPUXHardware(dict())
    # Test for ia64/B.11.31 (machinfo return cores strings release B.11.31 > 1204
    test_obj.module.run_command = (lambda *_, **__: (0, '', None))
    test_obj.module.run_command = (lambda *_, **__: (0, '  B.11.31', None))
    test_obj.module.run_command = (lambda *_, **__: (0, '0', None))
    test_obj.module.run_command = (lambda *_, **__: (0, '48 Intel(R) Xeon(R) CPU E7-4830 v2 @ 2.00GHz', None))

# Generated at 2022-06-13 00:49:13.712317
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    # Testing HP-UX Itanium
    # case 01: more than 1 entry in machinfo output
    collected_facts = dict()
    collected_facts['ansible_distribution_version'] = "B.11.31"
    collected_facts['ansible_architecture'] = 'ia64'
    hw = HPUXHardware()
    out = "Firmware revision                    : VxWorks 6.8 Core OS / DR-DOS"
    rc = 0
    hw.module.run_command.return_value = rc, out, ''
    out = "Machine serial number                : US12345678"
    rc = 0
    hw.module.run_command.return_value = rc, out, ''
    result = hw.get_hw_facts(collected_facts)

# Generated at 2022-06-13 00:49:23.886344
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = AnsibleModule(argument_spec={})
    test_module.run_command = MagicMock(return_value=(0, "", ""))
    test_module.run_command.return_value = (0, "     133     886     598     598    2195", "")
    test_module.run_command.return_value = (0, "     744", "")
    test_module.run_command.return_value = (0, "     744", "")
    test_module.run_command.return_value = (0, "     744", "")
    test_module.run_command.return_value = (0, "     744", "")

# Generated at 2022-06-13 00:49:34.267695
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec=dict())
    hw = HPUXHardware(module)
    collected_facts = dict(ansible_facts=dict(ansible_architecture='ia64', ansible_distribution_version='B.11.23'))
    hw_facts = hw.populate(collected_facts)
    assert hw_facts['processor'] != None
    assert hw_facts['processor_cores'] != None
    assert hw_facts['processor_count'] != None
    assert hw_facts['memtotal_mb'] != None
    assert hw_facts['memfree_mb'] != None
    assert hw_facts['swaptotal_mb'] != None
    assert hw_facts['swapfree_mb'] != None
    assert hw_facts['model'] != None


# Generated at 2022-06-13 00:49:44.750235
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():

    from ansible.module_utils.facts.hardware.hpux import HPUXHardware

    hw = HPUXHardware(dict(platform='HP-UX', ansible_architecture='9000/800'))
    test_mem_facts = hw.get_memory_facts(dict(platform='HP-UX', ansible_architecture='9000/800', path='/path'))
    assert test_mem_facts['memfree_mb']
    assert test_mem_facts['memtotal_mb']
    assert test_mem_facts['swaptotal_mb']
    assert test_mem_facts['swapfree_mb']
    hw = HPUXHardware(dict(platform='HP-UX', ansible_architecture='ia64'))

# Generated at 2022-06-13 00:50:10.417397
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hardware = HPUXHardware(dict(distribution='HP-UX'))
    collected_facts = dict(ansible_architecture='9000/800')
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 1
    collected_facts = dict(ansible_architecture='ia64')
    collected_facts['ansible_distribution_version'] = 'B.11.31'
    cpu_facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert cpu_facts['processor_count'] == 1 and cpu_facts['processor_cores'] == 1 and cpu_facts['processor'] == 'Intel(R) Itanium(R) 2 processor'

# Generated at 2022-06-13 00:50:12.784639
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware({'ansible_architecture': 'ia64',
                             'ansible_distribution_version': 'B.11.23'}, None)
    hardware.module = MagicMock()
    hardware.module.run_command = MagicMock(return_value=(0, 'HP Server rp5450', ''))
    hardware.populate()



# Generated at 2022-06-13 00:50:17.182536
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    instance = HPUXHardware()

    # list contain expected and actual output of method get_cpu_facts

# Generated at 2022-06-13 00:50:24.319140
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec=dict(gather_subset=dict(type='list', default=['!all'])))
    collected_facts = dict(
        ansible_architecture='ia64',
        ansible_distribution='HP-UX',
        ansible_distribution_major_version='B.11.23',
        ansible_distribution_version='B.11.23',
        ansible_os_family='UNIX',
        ansible_system='HP-UX',
    )
    hp = HPUXHardware(module=module)
    rc, out, err = module.run_command("echo 'Intel(R) Itanium(R) Processor 9350'")
    hp.cpu_facts = dict(processor=out.strip())

# Generated at 2022-06-13 00:50:29.474397
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware()
    hardware.module = FakeAnsibleModule()
    hardware.module.run_command = MagicMock(return_value=(0, 'HP-UX B.11.31 ia64  1049685090', ''))
    hardware.get_hw_facts()



# Generated at 2022-06-13 00:50:34.300202
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector_object = HPUXHardwareCollector({'platform': 'HP-UX', 'distribution': 'B.11.23'})
    assert hardware_collector_object._platform == 'HP-UX'
    assert hardware_collector_object.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:50:43.173736
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    module = type
    setattr(module, 'run_command', lambda *args, **kwargs: (0, '', ''))
    setattr(module, 'get_bin_path', lambda *args, **kwargs: '/bin/test')
    hardware_collector = HPUXHardwareCollector(module=module, collected_facts={'platform': 'HP-UX',
                                                                               'distribution': 'HP-UX'})
    assert hardware_collector.platform == 'HP-UX'
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector._platform == 'HP-UX'
    assert hardware_collector.collected_facts == {'platform': 'HP-UX', 'distribution': 'HP-UX'}

# Generated at 2022-06-13 00:50:53.585314
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule({})
    hardware_obj = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.23"}
    hardware_facts = hardware_obj.get_hw_facts(collected_facts=collected_facts)
    assert hardware_facts['firmware_version'] == 'P89 08/18/2012'
    assert hardware_facts['product_serial'] == 'CHXXXXXXX'

    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.31"}
    hardware_facts = hardware_obj.get_hw_facts(collected_facts=collected_facts)

# Generated at 2022-06-13 00:51:04.397890
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    """Unit test for HPUXHardware get_cpu_facts method"""
    module = type('', (), {'run_command':_mock_run_command})()
    hpux_hw_obj = HPUXHardware(module)

    # Test with no collected facts
    facts = hpux_hw_obj.get_cpu_facts()
    assert facts['processor_count'] == 1
    assert facts['processor'] == ''
    assert facts['processor_cores'] == 0

    # Test with collected facts
    facts = hpux_hw_obj.get_cpu_facts({'ansible_architecture': '9000/800', 'ansible_distribution_version': 'B.11.31'})
    assert facts['processor_count'] == 2
    assert facts['processor'] == 'Intel Xeon'

# Generated at 2022-06-13 00:51:08.277561
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.platform == 'HP-UX'
    assert HPUXHardware in hardware_collector._fact_class
    assert hardware_collector._fact_class == HPUXHardware
    assert hardware_collector.required_facts == {'platform', 'distribution'}



# Generated at 2022-06-13 00:51:27.283270
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule
    module.run_command = run_command
    module.run_command.side_effect = side_effect
    input_hw_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.23"
    }
    hw = HPUXHardware(module)
    output_hw_facts = hw.get_hw_facts(collected_facts=input_hw_facts)
    assert output_hw_facts['firmware_version'] == 'B.11.23'
    assert output_hw_facts['product_serial'] == '123456789'
    assert output_hw_facts['model'] == 'ia64 HP 9000 rp8400'

# Generated at 2022-06-13 00:51:31.466376
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware()
    data = hardware.get_hw_facts()

    assert data['model'] == 'Integrity Superdome 2'
    assert data['firmware_version'] == '02.55.14'
    assert data['product_serial'] == 'ABCD12345678'



# Generated at 2022-06-13 00:51:35.930621
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware()
    hardware.module = MockModule()
    hardware.module.run_command.return_value = (0, 'HP-UX B.11.31 ia64    060914144464', '')
    hardware.populate()
    hardware.get_hw_facts()

# Generated at 2022-06-13 00:51:44.742586
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():

    mod_args = {'ANSIBLE_MODULE_ARGS': {}}

    hardware_facts = {
        'ansible_architecture': '9000/800',
        'ansible_distribution_version': 'B.11.11'
    }
    h = HPUXHardware(module=FakeModule(mod_args, hardware_facts))
    res = h.get_cpu_facts()

    assert res['processor_count'] == 2
    assert res['processor_cores'] is None

    hardware_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }

    h = HPUXHardware(module=FakeModule(mod_args, hardware_facts))
    res = h.get_cpu_facts()

    assert res

# Generated at 2022-06-13 00:51:50.041143
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    module = AnsibleModule(argument_spec={})
    hardware = HPUXHardware(module=module)
    facts = hardware.populate()

    assert type(facts) == dict

    fields = [
        'memfree_mb', 'memtotal_mb', 'swapfree_mb', 'swaptotal_mb',
        'processor', 'processor_cores', 'processor_count',
        'model', 'firmware'
    ]

    for field in fields:
        assert field in facts

# Generated at 2022-06-13 00:51:54.524443
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    class CollectedFacts:
        def __init__(self, ansible_architecture=None, ansible_distribution_version=None):
            self.ansible_all_ipv4_addresses = []
            self.ansible_architecture = ansible_architecture
            self.ansible_distribution_version = ansible_distribution_version

    def run_command(cmd, use_unsafe_shell=False):
        class Out:
            def __init__(self, out, err=None):
                self.out = out
                self.err = err

        if cmd == "ioscan -FkCprocessor | wc -l":
            return rc, Out(out=2), err


# Generated at 2022-06-13 00:51:57.506151
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector.platform == 'HP-UX'

# Generated at 2022-06-13 00:52:03.584136
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    obj = HPUXHardware(module=module)
    out = obj.get_memory_facts()
    assert out.get('memtotal_mb') is not None
    assert out.get('memfree_mb') is not None
    assert out.get('swaptotal_mb') is not None
    assert out.get('swapfree_mb') is not None


# Generated at 2022-06-13 00:52:15.272663
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    hw = HPUXHardware(dict(ansible_facts=dict(ansible_distribution_version="B.11.31", ansible_architecture="ia64")))
    rc, out, err = hw.module.run_command("grep processor /proc/cpuinfo")
    if rc == 0:
        data = 0
        for line in out.splitlines():
            line_data = re.search('processor.+: (.*)', line).groups()[0]
            data = max(data, int(line_data))
        data += 1
        assert hw.get_cpu_facts()['processor_count'] == data, "processor_count incorrect"

# Generated at 2022-06-13 00:52:22.532537
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():

    class MockModule(object):
        def __init__(self):
            self.facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
            self.run_command_calls = []

        def run_command(self, cmd, use_unsafe_shell=False):
            self.run_command_calls.append(cmd)
            if cmd == "/usr/contrib/bin/machinfo | grep 'Number of CPUs'":
                return (0, 'Number of CPUs = 8', None)
            elif cmd == "/usr/contrib/bin/machinfo | grep 'processor family'":
                return (0, 'Number of processors = 8', None)

# Generated at 2022-06-13 00:52:42.022317
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    assert HPUXHardwareCollector()._platform == 'HP-UX'
    assert HPUXHardwareCollector()._fact_class == HPUXHardware
    assert HPUXHardwareCollector().required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:52:45.564651
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModule(argument_spec={})

    hpuxhw = HPUXHardware(module)
    hpuxhw.get_cpu_facts()


# Generated at 2022-06-13 00:52:53.802831
# Unit test for method populate of class HPUXHardware
def test_HPUXHardware_populate():
    # Initializing the class
    class_HPUXHardware = HPUXHardware()
    # Initializing the module
    class_HPUXHardware.module = AnsibleModule(argument_spec={})
    class_HPUXHardware.module.run_command = lambda x: (0, 'HPUX_Test_11', '')
    # Create a dictionary for collecting facts
    collected_facts = {}
    # Populate the collected_facts dictionary
    collected_facts = class_HPUXHardware.populate(collected_facts)
    assert collected_facts['processor'] == 'Intel(R) Itanium(R) Processor'
    assert collected_facts['processor_cores'] == 1
    assert collected_facts['processor_count'] == 8
    assert collected_facts['memtotal_mb'] == 16384

# Generated at 2022-06-13 00:52:56.305595
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hc = HPUXHardwareCollector(None, None)
    assert hc._fact_class.platform == 'HP-UX'
    assert hc._platform == 'HP-UX'

# Generated at 2022-06-13 00:53:05.047456
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():

    hpu = HPUXHardware()

    setattr(hpu.module, 'run_command',
                                lambda *args, **kwargs: (0, '    PA-RISC', None))
    setattr(hpu.module, 'run_command',
                                lambda *args, **kwargs: (0, 'Firmware revision: C.01.05', None))
    setattr(hpu.module, 'run_command',
                                lambda *args, **kwargs: (0, 'Machine serial number: SER12345', None))

    hw_facts = hpu.get_hw_facts()

    assert hw_facts['model'] == 'PA-RISC'
    assert hw_facts['firmware_version'] == 'C.01.05'

# Generated at 2022-06-13 00:53:08.331864
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    hardware = HPUXHardware(dict(), dict())

    hardware.module.run_command = lambda *args, **kwargs: (0, 'HP9000/785', '')
    hw_facts = hardware.get_hw_facts()
    assert hw_facts.get('model') == 'HP9000/785'

# Generated at 2022-06-13 00:53:15.127532
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collector import BaseFileCollector
    from ansible.module_utils.facts.collector import BaseFileWriteCollector

    # test default required facts
    required_facts_set = set(['platform', 'distribution'])
    test_obj = Facts(None, None, None)
    test_obj._cache = {'ansible_architecture': 'ia64', 'ansible_distribution': 'HP-UX', 'ansible_distribution_version': 'B.11.23'}

    # test default output
    result = HPUXHardware(test_obj).get_hw_facts()

# Generated at 2022-06-13 00:53:24.231855
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    facts = HPUXHardware().get_cpu_facts({'ansible_architecture': '9000/800'})
    assert facts['processor_count'] == 512
    facts = HPUXHardware().get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'})
    assert facts['processor'] == 'Intel(R) Itanium(R) Processor'
    facts = HPUXHardware().get_cpu_facts({'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'})
    assert facts['processor'] == 'Intel(R) Itanium(R) Processor'
    assert facts['processor_cores'] == 8


# Generated at 2022-06-13 00:53:32.346843
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    module = AnsibleModuleMock()
    module.run_command = run_command
    collected_facts = {}
    collected_facts['platform'] = 'HP-UX'
    collected_facts['distribution'] = 'HP-UX'
    collected_facts['ansible_architecture'] = 'ia64'
    collected_facts['ansible_distribution_version'] = 'B.11.23'
    hardware = HPUXHardware(module)
    facts = hardware.get_cpu_facts(collected_facts=collected_facts)
    assert(facts['processor_count'] == 16)
    assert(facts['processor_cores'] == 1)
    assert(facts['processor'] == 'Intel(R) Itanium(R) Family')


# Generated at 2022-06-13 00:53:40.551594
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(argument_spec={})
    module.params = {'operation': 'get_memory_facts'}
    hardware_obj = HPUXHardware(module)
    collected_facts = {'ansible_architecture': 'ia64'}
    hw_facts = {}
    hw_facts = hardware_obj.get_memory_facts(collected_facts)
    assert hw_facts['memfree_mb'] > 0
    assert hw_facts['swaptotal_mb'] > 0
    assert hw_facts['swapfree_mb'] > 0
    assert hw_facts['memtotal_mb'] > 0


# Generated at 2022-06-13 00:54:29.781861
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    h = HPUXHardwareCollector()
    assert h.fact_class == HPUXHardware
    assert h.platform == 'HP-UX'
    assert h.required_facts == {'platform', 'distribution'}

# Generated at 2022-06-13 00:54:33.189407
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector()
    assert hw_collector.fact_class == HPUXHardware
    assert hw_collector.platform == 'HP-UX'
    assert hw_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:54:37.878821
# Unit test for method get_cpu_facts of class HPUXHardware
def test_HPUXHardware_get_cpu_facts():
    from ansible.module_utils.facts.hardware.hpsux import HPUXHardware
    collected_facts={}
    collected_facts['ansible_architecture']='9000/800'
    hpu = HPUXHardware(module=None)
    cpu_facts = {}
    cpu_facts = hpu.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 6


# Generated at 2022-06-13 00:54:39.677634
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hardware_collector = HPUXHardwareCollector()
    assert hardware_collector._fact_class is not None

# Generated at 2022-06-13 00:54:44.290878
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    hw_collector = HPUXHardwareCollector()
    assert hw_collector._fact_class == HPUXHardware
    assert hw_collector._platform == 'HP-UX'
    assert hw_collector.required_facts == set(['platform', 'distribution'])

# Generated at 2022-06-13 00:54:49.437359
# Unit test for constructor of class HPUXHardwareCollector
def test_HPUXHardwareCollector():
    test_class = HPUXHardwareCollector()
    assert test_class
    assert test_class._platform == 'HP-UX'
    assert test_class._fact_class == HPUXHardware
    assert test_class.required_facts == set(['platform', 'distribution'])


# Generated at 2022-06-13 00:54:58.273780
# Unit test for method get_hw_facts of class HPUXHardware
def test_HPUXHardware_get_hw_facts():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    hw_facts = {}

    rc, out, err = module.run_command("model")
    hw_facts['model'] = out.strip()
    collected_facts = dict()
    collected_facts['ansible_distribution_version'] = "B.11.23"
    collected_facts['ansible_architecture'] = 'ia64'

    hpx_hw = HPUXHardware()
    hw_facts = hpx_hw.get_hw_facts(collected_facts=collected_facts)
    assert 'firmware_version' in hw_facts

    collected_facts['ansible_distribution_version'] = "B.11.31"
    hpx_hw = HPU

# Generated at 2022-06-13 00:55:05.482358
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    module = AnsibleModule(
        argument_spec=dict(
        )
    )

    hw_collector = HPUXHardwareCollector(module)
    hw = hw_collector.collect()[-1]

    # get_memory_facts returns a dictionary of memory facts
    memory_facts = hw.get_memory_facts()
    assert memory_facts is not None
    assert isinstance(memory_facts, dict)
    assert 'memfree_mb' in memory_facts
    assert 'memtotal_mb' in memory_facts
    assert 'swaptotal_mb' in memory_facts
    assert 'swapfree_mb' in memory_facts



# Generated at 2022-06-13 00:55:15.477714
# Unit test for method get_memory_facts of class HPUXHardware
def test_HPUXHardware_get_memory_facts():
    test_module = os.path.join(os.path.dirname(__file__), '../../../test/ansible/module_utils/facts/hardware/test_HPUXHardware.py')
    module_args = dict(
        ansible_facts=dict(
            ansible_architecture='ia64',
            ansible_distribution_version='B.11.31',
            ansible_processor_arch='ia64',
        )
    )
    hardware = HPUXHardware()
    hardware.module = AnsibleModule(argument_spec=dict())
    hardware.module.exit_json = lambda x: x
    hardware_facts = hardware.populate()
    assert hardware_facts['memtotal_mb'] == 1024
    assert hardware_facts['memfree_mb'] == 784