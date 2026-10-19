

# Generated at 2022-06-13 02:51:17.339273
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fake_module = type('module', (object,), {'run_command': lambda _: ('1', '')})()
    fips_fact_collector = FipsFactCollector()
    facts = fips_fact_collector.collect(module=fake_module, collected_facts=None)
    assert facts['fips']

# Generated at 2022-06-13 02:51:21.234195
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Initialization
    FipsFactCollector.run()
    # Collect facts
    result = FipsFactCollector.collect(None, None)
    content = get_file_content('/proc/sys/crypto/fips_enabled')
    if content and content == '1':
        assert result['fips'] == True
    else:
        assert result['fips'] == False

# Generated at 2022-06-13 02:51:24.711930
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector = FipsFactCollector()
    FipsFactCollector._get_file_content = lambda self, file: '1' if file == '/proc/sys/crypto/fips_enabled' else ''
    ret = FipsFactCollector.collect()
    assert ret['fips']
    FipsFactCollector._get_file_content = lambda self, file: ''
    ret = FipsFactCollector.collect()
    assert ret['fips'] == False

# Generated at 2022-06-13 02:51:28.802684
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collected_facts_1 = dict(ansible_facts=dict(fips=False))
    collected_facts_2 = dict(ansible_facts=dict(fips=True))
    # Create a instance of FipsFactCollector class
    fips_collector = FipsFactCollector()
    # Call method collect
    facts_1 = fips_collector.collect()
    facts_2 = fips_collector.collect()
    # Check if fips is set
    assert(facts_1 == collected_facts_1)
    assert(facts_2 == collected_facts_2)

# Generated at 2022-06-13 02:51:30.181924
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector.collect() == {'fips': False}


# Generated at 2022-06-13 02:51:32.983467
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    fips_facts=f.collect(collected_facts=None)
    assert 'fips' in fips_facts
    assert not fips_facts['fips']

# Generated at 2022-06-13 02:51:37.792614
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    # create an empty class as collector.module
    collector.module = type('', (object,), dict(check_mode=False))
    assert collector.collect() == {'fips': False}


# Local variables:
# mode: python
# tab-width: 4
# indent-tabs-mode: nil
# End:

# Generated at 2022-06-13 02:51:40.716827
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fact_collector = FipsFactCollector()
    facts = fact_collector.collect()
    assert facts['fips'] == False or facts['fips'] == True

# Generated at 2022-06-13 02:51:49.224021
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    expected_fips_facts = {}
    expected_fips_facts['fips'] = True
    try:
        f = open('/proc/sys/crypto/fips_enabled', 'w')
        f.write('1\n')
    except:
        pass
    actual_fips_facts = {}
    actual_fips_facts = FipsFactCollector.collect()
    assert(actual_fips_facts)
    for fact in actual_fips_facts:
        assert(fact in expected_fips_facts)
        assert(actual_fips_facts[fact] == expected_fips_facts[fact])
    try:
        f = open('/proc/sys/crypto/fips_enabled', 'w')
        f.write('0\n')
    except:
        pass
    expected_

# Generated at 2022-06-13 02:51:55.083335
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test case for method collect of class FipsFactCollector.

    Checks if the method collects the facts correctly for both the cases -
    when FIPS mode is enabled and disabled.

    Args:
        None.

    Returns:
        None.

    Raises:
        None.
    """
    collector = FipsFactCollector()
    collected_facts = {}
    # when FIPS mode is enabled
    collector._module.get_file_content = mock.Mock(return_value='1')
    collector.collect(module=collector._module,
                      collected_facts=collected_facts)
    assert collected_facts['fips'] is True
    # when FIPS mode is disabled
    collector._module.get_file_content = mock.Mock(return_value='0')

# Generated at 2022-06-13 02:51:59.575350
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector()
    assert fips_facts.collect() == {'fips': False}

# Generated at 2022-06-13 02:52:01.515743
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fc = FipsFactCollector()
    # TODO: Add unit test for method collect of class FipsFactCollector

# Generated at 2022-06-13 02:52:04.987195
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    test_facts = dict()
    test_facts = fips.collect()
    assert 'fips' in test_facts.keys()
    assert type(test_facts['fips']) is bool



# Generated at 2022-06-13 02:52:07.714396
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    ff = FipsFactCollector()
    f = ff.collect()
    assert f == {'fips': False}

# Generated at 2022-06-13 02:52:15.789424
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils._text import to_bytes

    def mock_get_file_content(path):
        if path == "/proc/sys/crypto/fips_enabled":
            return to_bytes("1")
        return to_bytes("")

    try:
        get_file_content_orig = Collector.get_file_content
        Collector.get_file_content = mock_get_file_content
        fips_collector = FipsFactCollector()
        fips_facts = fips_collector.collect()
        assert fips_facts['fips']
    finally:
        Collector.get_file_content = get_file_content_orig

# Generated at 2022-06-13 02:52:24.142317
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Example data from a file in /proc
    fipsData = '1'
    # Mock the get_file_content function using the unittest.mock library
    with mock.patch('ansible.module_utils.facts.collector.FipsFactCollector.get_file_content') as mock_get_file_content:
        mock_get_file_content.return_value = fipsData
        fips_facts_collector = FipsFactCollector()
        # Test collect function of FipsFactCollector class
        assert fips_facts_collector.collect() == {'fips': True}

# Generated at 2022-06-13 02:52:28.375338
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    # Fake file content
    collector.get_file_content = lambda x: b'0'
    assert not collector.collect()['fips']
    collector.get_file_content = lambda x: b'1'
    assert collector.collect()['fips']

# Generated at 2022-06-13 02:52:34.330107
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test method FipsCollector.collect()"""

    fips_facts = FipsFactCollector()
    collected_facts = fips_facts.collect()

    # collected_facts is a dict
    assert (isinstance(collected_facts, dict))

    # collected_facts has the expected values
    assert (collected_facts['fips'])

# Generated at 2022-06-13 02:52:36.869929
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector()
    data = fips_facts.collect()
    assert 'fips' in data

# Generated at 2022-06-13 02:52:38.083715
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Test method collect of class FipsFactCollector
    """
    fips_obj = FipsFactCollector()
    assert fips_obj.collect() == {'fips': False}

# Generated at 2022-06-13 02:52:45.553265
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    result = FipsFactCollector().collect()
    assert result

# Generated at 2022-06-13 02:52:49.264146
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fc = FipsFactCollector()
    res = fc.collect()
    assert isinstance(res, dict)
    assert 'fips' in res.keys()
    assert res['fips'] == False
    assert '_fact_ids' in res.keys()
    assert res['_fact_ids'] == {'fips'}

# Generated at 2022-06-13 02:52:50.705145
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector()
    assert fips_facts.collect()

# Generated at 2022-06-13 02:52:53.429066
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # test data
    data = dict()

    module = AnsibleModule(argument_spec=dict())
    fips_facts = FipsFactCollector().collect(module=module, collected_facts=data)
    assert fips_facts['fips'] == False



# Generated at 2022-06-13 02:52:57.857807
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test_cases = [
        {
            "expected_fips_facts": {
                "fips": True
            },
            "content_of_file_fips_enabled": "1"
        },
        {
            "expected_fips_facts": {
                "fips": False
            },
            "content_of_file_fips_enabled": "0"
        },
        {
            "expected_fips_facts": {
                "fips": False
            }
        },
    ]

    def get_file_content_side_effect(filename):
        if filename == '/proc/sys/crypto/fips_enabled':
            return _content_of_file_fips_enabled

    collector = FipsFactCollector()
    for test_case in test_cases:
        _content_of_

# Generated at 2022-06-13 02:53:00.535909
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    collected_facts = None

    fips_facts = FipsFactCollector()
    result = fips_facts.collect(module, collected_facts)
    assert result['fips'] is False

# Generated at 2022-06-13 02:53:03.851016
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts_collector = FipsFactCollector()
    fips_facts = fips_facts_collector.collect()
    assert fips_facts == {'fips': False}

# Generated at 2022-06-13 02:53:06.185613
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test method collect of class FipsFactCollector."""
    ffc = FipsFactCollector()
    assert ffc.collect()['fips'] is False

# Generated at 2022-06-13 02:53:07.035256
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
  pass


# Generated at 2022-06-13 02:53:11.430660
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.processors import Processor

    processor = Processor()

    collected_facts = FactsCollector()

    fips_fact = FipsFactCollector()
    fips_fact.collect()
    processor.process(fips_fact.get_fact_ids(), collected_facts, None)

    assert collected_facts.get('fips') == False

# Generated at 2022-06-13 02:53:21.093206
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Test no fips mode
    collector = FipsFactCollector()
    data = b'0'
    assert collector.collect(collected_facts={'ansible_fips': False}) == {'fips': False}
    print("Test passed")

    # Test fips mode
    collector = FipsFactCollector()
    data = b'1'
    assert collector.collect(collected_facts={'ansible_fips': True}) == {'fips': True}
    print("Test passed")

if __name__ == '__main__':
    test_FipsFactCollector_collect()

# Generated at 2022-06-13 02:53:27.247743
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fipsFactCollector = FipsFactCollector()
    data = get_file_content('/proc/sys/crypto/fips_enabled')
    fips_facts = fipsFactCollector.collect()
    assert isinstance(fips_facts['fips'], bool)
    if data == '1':
        assert fips_facts == {'fips': True }
    else:
        assert fips_facts == {'fips': False }

# Generated at 2022-06-13 02:53:28.738572
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    fips_facts = fips.collect(collected_facts={})
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:53:34.473648
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # NOTE: this is populated even if it is not set
    fips_facts = {}
    fips_facts['fips'] = False
    data = get_file_content('/proc/sys/crypto/fips_enabled')
    if data and data == '1':
        fips_facts['fips'] = True
    return fips_facts

# Generated at 2022-06-13 02:53:36.422094
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    assert f.collect() == {'fips': False}

# Generated at 2022-06-13 02:53:38.659534
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    assert(fips_fact_collector.collect() == { 'fips': False })

# Generated at 2022-06-13 02:53:48.248019
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_data1 = get_file_content('/proc/sys/crypto/fips_enabled')
    fips_data2 = get_file_content('/proc/sys/crypto/fips_enabled')
    fips_facts1 = FipsFactCollector().collect()
    fips_facts2 = FipsFactCollector().collect()
    assert isinstance(fips_facts1, dict)
    assert isinstance(fips_facts2, dict)
    assert fips_facts1 == fips_facts2
    assert fips_facts1['fips'] == (fips_data1 == '1')
    assert fips_facts2['fips'] == (fips_data2 == '1')

# Generated at 2022-06-13 02:53:52.093923
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import utils
    fips_facts = {'fips': True}
    fips_facts1 = {'fips': False}
    ffs_obj = FipsFactCollector()
    utils.get_file_content = lambda x : '1'
    assert ffs_obj.collect() == fips_facts
    utils.get_file_content = lambda x : '0'
    assert ffs_obj.collect() == fips_facts1

# Generated at 2022-06-13 02:53:58.049969
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    loaded_module = BaseFactCollector.get_module()
    setattr(loaded_module, 'gather_subset', ['all'])
    setattr(loaded_module, 'gather_network_resources', [])
    test_collector = FipsFactCollector()
    collected_facts = test_collector.collect(module=loaded_module)
    assert collected_facts['fips'] is True

# Generated at 2022-06-13 02:54:01.091189
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fact_collector = FipsFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['fips'] == False
    #This system should not be in 'fips' mode

# Generated at 2022-06-13 02:54:17.369298
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    collected_facts = None
    obj = FipsFactCollector()
    result = obj.collect(module, collected_facts)
    assert result['fips'] == True

# Generated at 2022-06-13 02:54:22.144719
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()

    # Test the typical case where data is present
    data = "1"
    result = collector.collect({}, {'fips': False})

    assert result['fips'] == True

    # Test the case where data is absent
    data = ""
    result = collector.collect({}, {'fips': False})
    
    assert result['fips'] == False

# Generated at 2022-06-13 02:54:25.247843
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()

    fips_facts = {}
    fips_facts['fips'] = False
    assert collector.collect(collected_facts=fips_facts) == {
        'fips': False
    }

# Generated at 2022-06-13 02:54:31.465136
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    data = b'1'
    def mock_get_file_content(file_name):
        return data
    FipsFactCollector._get_file_content = mock_get_file_content
    f = FipsFactCollector()
    collected_facts = {}
    new_facts = f.collect(collected_facts=collected_facts)
    assert new_facts['fips'] is True

# Generated at 2022-06-13 02:54:37.707734
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    with open('/proc/sys/crypto/fips_enabled', 'wb') as f:
        f.write('1'.encode('utf-8'))
    fips = FipsFactCollector()
    res = fips.collect()
    assert res['fips'] == True

    with open('/proc/sys/crypto/fips_enabled', 'wb') as f:
        f.write('0'.encode('utf-8'))
    fips = FipsFactCollector()
    res = fips.collect()
    assert res['fips'] == False

# Generated at 2022-06-13 02:54:44.366386
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    # Create a mock module
    fips_module = MockModule()

    # Create and instance of FipsFactCollector
    fips_collector = FipsFactCollector()

    # Call the collect method
    fact_data = fips_collector.collect(module=fips_module)

    # Assert that the method returned the correct result
    assert fact_data['fips'] == True

# Generated at 2022-06-13 02:54:52.938191
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    import imp
    import sys

    # create a dummy module for testing
    module = imp.new_module('ansible_collected_facts')
    module.params = {}
    module.exit_json = lambda **kwargs: kwargs

    # collect the facts
    sys.modules['ansible_collected_facts'] = module

    # read the facts
    facts = collector.collector.get_collection_string('fips', module, [])
    collected = eval(facts)

    assert 'fips' in collected

    # clean up
    del sys.modules['ansible_collected_facts']

# Generated at 2022-06-13 02:54:57.045265
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None

    data = '1'
    mock_get_file_content = lambda path: data

    fips_fc = FipsFactCollector()
    fips_fc._get_file_content = mock_get_file_content
    fips_fc.collect(module)

    assert fips_fc.collect(module) == {'fips': True}


# Generated at 2022-06-13 02:54:58.805366
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:55:05.358878
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    read /proc/sys/crypto/fips_enabled to verify if 'fips' is enabled
    """

    from ansible.module_utils.facts.utils import get_file_content

    import pytest

    def mock_get_file_content(file):
        if file == '/proc/sys/crypto/fips_enabled':
            return '1'
        raise

    monkeypatch.setattr(FipsFactCollector, '_get_file_content', mock_get_file_content)
    fips_facts = FipsFactCollector.collect()
    assert fips_facts['fips'] is True

    def mock_get_file_content(file):
        if file == '/proc/sys/crypto/fips_enabled':
            return '0'
        raise


# Generated at 2022-06-13 02:55:40.064615
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    collected_facts = None
    fact = FipsFactCollector()
    result = fact.collect(module, collected_facts)
    #assert result['fips'] == False
    print(result)

# Generated at 2022-06-13 02:55:42.300794
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    fips_collector.file_data = {}
    fips_facts = fips_collector.collect()
    assert fips_facts["fips"] == False

# Generated at 2022-06-13 02:55:45.366481
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import pytest
    fips_collector = FipsFactCollector()
    fips_fact = fips_collector.collect(None, None)
    assert fips_fact == { 'fips': False}

# Generated at 2022-06-13 02:55:49.867094
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Set up a mock module
    module = type('module', (object,), {'params': {}})
    fipsFact = FipsFactCollector(module)
    assert(fipsFact.collect()['fips'] == False)

    # Set up another mock module
    module = type('module', (object,), {'params': {}})
    fipsFact = FipsFactCollector(module)
    assert(fipsFact.collect()['fips'] == False)

# Generated at 2022-06-13 02:55:52.490124
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """ Test case for FipsFactCollector.collect()
    """
    fips_fact_collector_obj = FipsFactCollector()
    fips_fact_collector_obj.collect()
    assert fips_fact_collector_obj.collect() == True

# Generated at 2022-06-13 02:55:58.404285
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    expected_results = {'fips': True }
    mock_get_file_content = lambda x: '1'
    mock_module = MagicMock()

    fips_collector = FipsFactCollector()
    fips_collector.get_file_content = mock_get_file_content

    assert fips_collector.collect(mock_module) == expected_results

# Generated at 2022-06-13 02:56:05.624053
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self.params = {}

    class MockCollectedFact(object):
        def __init__(self):
            self.__dict__ = {}

    # Case 1: fips_facts = True
    mock_module_1 = MockModule()
    fips_facts_1 = FipsFactCollector()

    expected_results_1 = {'fips': True}
    actual_results_1 = fips_facts_1.collect(mock_module_1, MockCollectedFact())
    for key in expected_results_1:
        assert expected_results_1[key] == actual_results_1[key]

    # Case 2: fips_facts = False
    mock_module_2 = MockModule()
    fips_facts_2 = FipsFact

# Generated at 2022-06-13 02:56:06.272754
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:56:07.838413
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    m = FipsFactCollector()
    assert m.collect() == {'fips': False}

# Generated at 2022-06-13 02:56:10.385910
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    assert(f.collect() == {'fips': False})


# Generated at 2022-06-13 02:57:16.052491
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_content = '1'
    collector = FipsFactCollector()
    fips_facts = collector.collect({'path': '/proc/sys/crypto/fips_enabled', 'content': fips_content})
    assert fips_facts['fips'] == True

# Generated at 2022-06-13 02:57:17.823083
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    facts = fips_fact_collector.collect()
    assert facts['fips'] is False

# Generated at 2022-06-13 02:57:20.969680
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    fips_collector.collect()

# Generated at 2022-06-13 02:57:22.449991
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips1 = FipsFactCollector()
    facts = fips1.collect()
    assert facts['fips'] == False


# Generated at 2022-06-13 02:57:26.457498
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fc = FipsFactCollector()
    fips_facts = fips_fc.collect()
    assert isinstance(fips_facts, dict)
    assert 'fips' in fips_facts
    assert fips_facts['fips'] is not None

# Generated at 2022-06-13 02:57:28.385133
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_collect = FipsFactCollector().collect()
    assert isinstance(FipsFactCollector_collect, dict)

# Generated at 2022-06-13 02:57:31.039990
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = AnsibleModuleMock()
    collected_facts = {}
    content = FipsFactCollector.collect(module, collected_facts)
    assert 'fips' in content
    assert content['fips'] == False


# Generated at 2022-06-13 02:57:36.991337
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # NOTE: _fact_ids is a set, but for this unit test, the order is important
    # to ensure that the unit test does not depend on the order of a set.
    assert FipsFactCollector._fact_ids == {'fips'}

    # Should always have fips
    assert FipsFactCollector.collect() == {'fips': False}

    # Fake the file location so we can test fips enabled
    FipsFactCollector._module.get_file_content = lambda filename: "1"
    assert FipsFactCollector.collect() == {'fips': True}

# Generated at 2022-06-13 02:57:40.020073
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test_obj = FipsFactCollector()
    result = test_obj.collect()
    assert 'fips' in result
    assert type(result['fips']) is bool

# Generated at 2022-06-13 02:57:46.978209
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # test module instantiation with missing args
    FipsFacts = FipsFactCollector()
    assert FipsFacts.name == 'fips'
    assert FipsFacts._fact_ids == set()

    # test module name
    assert FipsFactCollector.name == 'fips'

    # test module _fact_ids
    assert FipsFactCollector._fact_ids == set()

    # run module collect
    FipsFacts.collect()
    assert FipsFacts._fact_ids == set()

    # test module collect functionality
    assert FipsFacts.collect(None, None) == {'fips': False}

# Generated at 2022-06-13 03:00:23.103494
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    fips_collector._module = None
    fips_collector._collected_facts = {}
    assert fips_collector.collect(collected_facts={}) == {'fips': False}

# Generated at 2022-06-13 03:00:27.665545
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.utils import get_file_content
    # Mock contents of file
    get_file_content.side_effect = ['1']
    # Create instance of FipsFactCollector
    collect_fips = get_collector_instance(FipsFactCollector)
    # Invoke method collect, result is assigned to fips_facts
    fips_facts = collect_fips.collect()
    assert fips_facts['fips'] == True

# Generated at 2022-06-13 03:00:29.418739
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact = FipsFactCollector()
    assert 'fips' in fips_fact.collect().keys()

# Generated at 2022-06-13 03:00:35.225816
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_values = {'fips': False}
    m_module = Mock()

    ff = FipsFactCollector(m_module)

    # Test for fips=True
    m_module.get_file_content.return_value = '1'
    facts = ff.collect(m_module, None)
    assert facts == fips_values

    # Test for fips=False
    m_module.get_file_content.return_value = '0'
    facts = ff.collect(m_module, None)
    assert facts == fips_values

# Generated at 2022-06-13 03:00:35.781065
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector().collect()

# Generated at 2022-06-13 03:00:38.136829
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Method collect of class FipsFactCollector, if data exists and data == 1
    fips_facts['fips'] will be True.
    """
    fips_collector = FipsFactCollector()
    fips_facts = fips_collector.collect()
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 03:00:39.456172
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    ffc = FipsFactCollector()
    assert ffc.collect() == {'fips': False}

# Generated at 2022-06-13 03:00:42.392635
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    result = collector.collect()
    assert result == {'fips': False}

# Generated at 2022-06-13 03:00:47.056516
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact = FipsFactCollector()
    fips_fact.file_exists = lambda path: path == '/proc/sys/crypto/fips_enabled' or False
    fips_fact.get_file_content = lambda path: '1' if path == '/proc/sys/crypto/fips_enabled' else None
    fips_fact_value = fips_fact.collect()
    assert fips_fact_value == {'fips': True}

# Generated at 2022-06-13 03:00:48.995779
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test the functionality of FipsFactCollector.collect

    :return:
    """
    fips_obj = FipsFactCollector()
    fips_obj.collect()