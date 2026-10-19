

# Generated at 2022-06-13 02:51:14.448802
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_collect = FipsFactCollector()
    assert FipsFactCollector_collect.collect()

# Generated at 2022-06-13 02:51:16.191725
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact = FipsFactCollector()
    assert fips_fact.collect()['fips'] is False

# Generated at 2022-06-13 02:51:17.833463
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector = FipsFactCollector()
    assert FipsFactCollector.collect() == {'fips': False}

# Generated at 2022-06-13 02:51:20.490352
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Create an instance of FipsFactCollector class
    fips_fact_collector = FipsFactCollector()
    #Collector returns dictionary of fips facts
    assert isinstance(fips_fact_collector.collect(), dict)

# Generated at 2022-06-13 02:51:24.300786
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fact_collector_obj = FipsFactCollector()
    # If fips mode is enabled
    fips_enabled_facts = fact_collector_obj.collect(collected_facts=None)
    assert fips_enabled_facts['fips'] is True
    # If fips mode is disabled
    fips_disabled_facts = fact_collector_obj.collect(collected_facts=None)
    assert fips_disabled_facts['fips'] is False

# Generated at 2022-06-13 02:51:26.569029
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    fips_facts = fips.collect()
    assert fips_facts == {
        'fips': False
    }

# Generated at 2022-06-13 02:51:37.317920
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import os
    import tempfile

    # Create a temporary file
    fd, filename = tempfile.mkstemp(prefix='ansible-fips-tests')

    # Create an instance of FipsFactCollector
    collector = FipsFactCollector()

    # Check that facts are not collected
    facts = collector.collect()
    assert len(facts) == 0

    # Check that facts are collected
    os.write(fd, '1')
    facts = collector.collect()
    assert len(facts) == 1 and facts["fips"] is True

    # Check that facts are collected
    os.write(fd, '0')
    facts = collector.collect()
    assert len(facts) == 1 and facts["fips"] is False

    # Check that facts are collected
    os.write(fd, 'foo')
    facts = collector

# Generated at 2022-06-13 02:51:39.106634
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    result = collector.collect()
    assert result == {'fips': False}


# Generated at 2022-06-13 02:51:44.874474
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    # Unit test function member variables
    fips_facts = {}
    file_content = '0'

    # Call method
    fips_facts['fips'] = False
    if file_content and file_content == '1':
        fips_facts['fips'] = True

    # Assert the results
    assert fips_facts['fips']

# Generated at 2022-06-13 02:51:47.991912
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    fips_facts = fips_collector.collect()
    print(json.dumps(fips_facts))

# Run the collect method in the module
if __name__ == '__main__':
    test_FipsFactCollector_collect()

# Generated at 2022-06-13 02:51:54.561295
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Create a FipsFactCollector() object
    FipsFactCollectorObj = FipsFactCollector()

    # Test the method collect() of class FipsFactCollector
    result = FipsFactCollectorObj.collect()

    assert result
    assert type(result) is dict
    assert 'fips' in result

# Generated at 2022-06-13 02:51:56.165140
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    result = fips_collector.collect()
    assert 'fips' in result
    if result['fips']:
        assert result['fips'] == True
    else:
        assert result['fips'] == False

# Generated at 2022-06-13 02:52:00.962434
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    # Initialize class instance
    fips_fc = FipsFactCollector()

    # Define expected results
    result = {
        'fips': False,
    }

    # Run method
    fips_fc.collect()

    # Check results
    assert fips_fc.ansible_facts == result

# Generated at 2022-06-13 02:52:03.495233
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    collected_facts = {}
    collected_facts.update(fips_fact_collector.collect())
    assert collected_facts['fips'] == False

# Generated at 2022-06-13 02:52:04.855047
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    F = FipsFactCollector()
    assert F.collect()['fips'] == False

# Generated at 2022-06-13 02:52:14.370838
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test_class = FipsFactCollector()

    assert test_class != None
    assert test_class.name() == "fips"

    # check fips not enabled
    assert test_class.collect()['fips'] == False

    # check fips enabled
    def mock_get_file_content(data):
        if data == '/proc/sys/crypto/fips_enabled':
            return "1"
    import __builtin__
    old_get_file_content = __builtin__.get_file_content
    __builtin__.get_file_content = mock_get_file_content
    assert test_class.collect()['fips'] == True
    __builtin__.get_file_content = old_get_file_content

# Generated at 2022-06-13 02:52:15.403148
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert len(FipsFactCollector().collect().keys()) == 1

# Generated at 2022-06-13 02:52:17.175068
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    result = collector.collect()
    assert result == {'fips': False}
    assert result.keys() == {'fips'}

# Generated at 2022-06-13 02:52:19.989064
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    # create test data
    desired_fips_facts = {'fips': True}
    fips_fact_collector.read_file = lambda _: "1"
    # call the method collect of the object
    res = fips_fact_collector.collect()
    assert res == desired_fips_facts

# Generated at 2022-06-13 02:52:23.546721
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    failed, collected_facts = fips_collector.collect()
    assert not failed
    assert 'fips' in collected_facts
    assert collected_facts['fips'] == False

# Generated at 2022-06-13 02:52:30.990655
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector().collect()

# Generated at 2022-06-13 02:52:35.139065
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    collector = FipsFactCollector()
    facts_collected = collector.collect()

    assert 'fips' in facts_collected

    assert isinstance(facts_collected['fips'], bool)

# Generated at 2022-06-13 02:52:41.859228
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Dictionary that will be populated
    collected_facts = {}

    # Populate the dictionary "collected_facts" with method collect of class FipsFactCollector
    FipsFactCollector().collect(collected_facts=collected_facts)

    # Testing branch used when fips is set to True
    data = '1'
    fips_facts = {}
    fips_facts['fips'] = False
    if data and data == '1':
        fips_facts['fips'] = True

    assert fips_facts == collected_facts


# Generated at 2022-06-13 02:52:43.021382
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector.collect()

# Generated at 2022-06-13 02:52:47.118724
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Arrange
    module = object
    collected_facts = {}
    fips_fact_collector = FipsFactCollector()

    # Act
    actual_result = fips_fact_collector.collect(module, collected_facts)

    # Verify
    assert actual_result['fips'] == False

# Generated at 2022-06-13 02:52:50.515618
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # GIVEN a FipsFactCollector.
    ffc = FipsFactCollector()

    # WHEN running the collect method.
    facts = ffc.collect()

    # THEN the fips fact should be defined
    assert facts.get('fips') is not None

# Generated at 2022-06-13 02:52:51.905041
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector().collect()
    assert fips_facts['fips'] is False

# Generated at 2022-06-13 02:52:55.552254
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector._fact_ids == set()
    assert isinstance(fips_fact_collector.collect(), dict)

# Generated at 2022-06-13 02:53:01.329816
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = MagicMock()
    collected_facts = {}
    fips = FipsFactCollector(module=module, collected_facts=collected_facts)
    assert fips.collect() == {'fips': False}
    fips_data = "1"
    fips.get_file_content = MagicMock(return_value=fips_data)
    assert fips.collect() == {'fips': True}

# Generated at 2022-06-13 02:53:05.419689
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    assert fips_collector.name == 'fips'
    assert fips_collector._fact_ids == set()
    fips_facts = fips_collector.collect()
    assert fips_facts['fips']

# Generated at 2022-06-13 02:53:25.624656
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    cachedir = '/var/cache/ansible'
    m_collector = FipsFactCollector(None, cachedir)
    m_get_file_content = m_collector.get_file_content
    m_collector.get_file_content = lambda x: '1'
    assert m_collector.collect() == {'fips': True}

    m_collector.get_file_content = lambda x: '0'
    assert m_collector.collect() == {'fips': False}

    m_collector.get_file_content = lambda x: None
    assert m_collector.collect() == {'fips': False}
    m_collector.get_file_content = m_get_file_content


# Generated at 2022-06-13 02:53:37.623088
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    if FipsFactCollector_may_be_available():
        fc = FipsFactCollector()
        fips_facts = fc.collect(None, None)
        assert fips_facts['fips'] == os.path.exists('/proc/sys/crypto/fips_enabled')
        with open('/proc/sys/crypto/fips_enabled', 'w') as f:
            f.write('1')
        fips_facts = fc.collect(None, None)
        assert fips_facts['fips'] == True
        with open('/proc/sys/crypto/fips_enabled', 'w') as f:
            f.write('0')
        fips_facts = fc.collect(None, None)
        assert fips_facts['fips'] == False


# Generated at 2022-06-13 02:53:42.359269
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_data = {
            'fips-enabled': '1'
            }
    def nop(module=None, collected_facts=None):
        return
    ffc = FipsFactCollector(nop, nop)
    ffc.read_file = lambda x: fips_data.get(x)
    assert ffc.collect() == {'fips': True}

# Generated at 2022-06-13 02:53:49.710763
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Test that FipsFactCollector works at all.
    from ansible.module_utils.facts.collector import FipsFactCollector
    class MockModule(object):
        pass
    fips_collector = FipsFactCollector()
    fips_facts = fips_collector.collect(module=MockModule())

    assert isinstance(fips_facts, dict)
    assert 'fips' in fips_facts

# Generated at 2022-06-13 02:53:53.817619
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    paths = ['/proc/sys/crypto/fips_enabled']
    results = ['1']
    data = {}
    for path in paths:
        data[path] = results.pop()
    collector = FipsFactCollector(None, data)
    result = collector.collect()
    assert (result['fips'] == True)

# Generated at 2022-06-13 02:53:56.246022
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector().collect()
    assert fips_facts['fips'] == True

# Generated at 2022-06-13 02:54:00.315897
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Arrange
    module = object()
    collected_facts = object()

    # Act
    fact_collector = FipsFactCollector()
    collected_facts = fact_collector.collect(module, collected_facts)

    # Assert
    assert collected_facts is not None

# Generated at 2022-06-13 02:54:01.798384
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test_fips = FipsFactCollector()
    test_fips.collect()


# Generated at 2022-06-13 02:54:05.352965
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict)
    assert 'fips' in facts
    assert isinstance(facts['fips'], bool)

# Generated at 2022-06-13 02:54:13.221428
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Unit test: method collect of class FipsFactCollector
    # Argument module not provided
    # Return value of get_file_content is None
    collector = FipsFactCollector()
    result = collector.collect()
    assert result['fips'] == False

    # Argument module not provided
    # Return value of get_file_content is not None
    # Return value of get_file_content is not 1
    collector = FipsFactCollector()
    result = collector.collect()
    assert result['fips'] == False

    # Argument module not provided
    # Return value of get_file_content is not None
    # Return value of get_file_content is 1
    collector = FipsFactCollector()
    result = collector.collect()
    assert result['fips'] == True

# Generated at 2022-06-13 02:54:43.459184
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect()
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:54:47.194268
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_obj = FipsFactCollector()
    fips_obj._module = {'run_command': lambda *args, **kwargs: ('1', None)}
    result = fips_obj.collect()
    assert result.get('fips') is True

# Generated at 2022-06-13 02:54:48.137762
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector().collect()

# Generated at 2022-06-13 02:54:54.268809
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    Module = collections.namedtuple('Module', ['params'])
    Facts = collections.namedtuple('Facts', ['fips'])
    module = Module(params={})
    fact_collector = FipsFactCollector()
    collected_facts = fact_collector.collect(module)
    assert collected_facts and isinstance(collected_facts, dict)
    assert 'fips' in collected_facts
    fips_facts = collected_facts.get('fips')
    assert fips_facts and isinstance(fips_facts, dict)

# Generated at 2022-06-13 02:54:58.580861
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    '''
    Test method collect of class FipsFactCollector
    '''
    fips_fact_collector = FipsFactCollector()
    test_data = ('1') #fips module on
    fips_facts = fips_fact_collector.collect(collected_facts={}, module='ut')
    assert fips_facts == {'fips': True}



# Generated at 2022-06-13 02:55:00.163415
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector({})
    facts = collector.collect()

    assert isinstance(facts['fips'], bool)

# Generated at 2022-06-13 02:55:01.593821
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test_obj = FipsFactCollector()
    data = test_obj.collect()
    assert data['fips'] == False

# Generated at 2022-06-13 02:55:05.827128
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    path = 'ansible.module_utils.facts.collectors.fips.FipsFactCollector'
    ffc = FipsFactCollector()
    fips = ['fips = False']
    fips_facts = ffc.collect()
    assert (fips_facts['fips'] == False)
    fips = ['fips = True']
    fips_facts = ffc.collect()
    assert (fips_facts['fips'] == True)

# Generated at 2022-06-13 02:55:09.524677
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    '''Unit test for method collect of class FipsFactCollector
       This is not a true unit test because the method collect of
       class FipsFactCollector depends on get_file_content of utils.py
       which we cannot mock easily.
       For now, we're just checking that it returns the correct keys
       and not the value.
       '''
    fips_facts = {}
    fips_facts['fips'] = False
    fips_fc = FipsFactCollector()

    # should return fips_facts['fips'] = False
    assert fips_fc.collect()['fips'] == fips_facts['fips']



# Generated at 2022-06-13 02:55:11.976779
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Unit test of method FipsFactCollector.collect."""

    # Create a FipsFactCollector object
    fips_fact_collector = FipsFactCollector()

    # TODO: add unit test here

# Generated at 2022-06-13 02:56:16.893210
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    facts = f.collect(collected_facts={}, module=None)
    assert facts['fips'] == False


# Generated at 2022-06-13 02:56:18.791406
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    assert(fips.collect())

# Generated at 2022-06-13 02:56:23.291405
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collector import collector_registry
    assert 'fips' in collector_registry._collectors
    assert 'fips' in collector_registry.enabled_collectors
    try:
        FipsFactCollector().collect()
    except Exception:
        assert False

# Generated at 2022-06-13 02:56:24.755080
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    fips_collector.collect()

# Generated at 2022-06-13 02:56:32.594946
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import Collector

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

    module = MockModule()
    fips_fact_collector = Collector.collectors['fips_fact']
    fips_fact_collector.get_file_content = lambda path: to_bytes('1')
    fips_facts = fips_

# Generated at 2022-06-13 02:56:34.298782
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    facts = {'fips': False}
    fips_fact_collector.collect(collected_facts=facts)
    assert facts['fips'] == False


# Generated at 2022-06-13 02:56:38.199750
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import sys
    collector = FipsFactCollector()
    collected_facts = {}
    test_module = sys.modules[__name__]
    assert collector.collect(test_module, collected_facts) \
        == {'fips': False}

# Generated at 2022-06-13 02:56:39.348596
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test if FipsFactCollector.collect returns expected results"""
    FipsFactCollector.collect()

# Generated at 2022-06-13 02:56:40.928146
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Creating an instance of FipsFactCollector
    inst_FipsFactCollector = FipsFactCollector()
    # Calling collect of FipsFactCollector class
    inst_FipsFactCollector.collect()

# Generated at 2022-06-13 02:56:44.918463
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector = FipsFactCollector()
    fipsFacts = FipsFactCollector.collect()
    if fipsFacts:
        if fipsFacts['fips']:
           print("fips is enabled")
        else:
           print("fips is not enabled")

# Generated at 2022-06-13 02:57:57.925536
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # create an instance of the FipsFactCollector
    ffc = FipsFactCollector()

    # create an instance of the mock_module class for testing
    mm = MockModule()

    # create an instance of the mock_collected_facts class for testing
    mock_cf = MockCollectedFacts()

    # get the facts
    ffc.collect(module=mm, collected_facts=mock_cf)

    # check that the collected_facts dictionary
    # was updated as expected
    assert mm.exit_args == {'changed': False}
    assert mock_cf.populated_facts == {'fips': False}


# Generated at 2022-06-13 02:58:02.912167
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Arrange
    fips_facts_data = """
    1
    """

    # Act
    fips_facts_collector = FipsFactCollector()
    fips_facts = fips_facts_collector.collect()

    # Assert
    fips_result = {
        'fips': True
    }

    assert fips_facts['fips'] == fips_result['fips']

# Generated at 2022-06-13 02:58:05.057211
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    obj = FipsFactCollector()
    assert type(obj.collect()) == dict
    obj.fact_ids()
    obj.get_vars()
    obj.get_valid_vars()

# Generated at 2022-06-13 02:58:11.266235
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # first try
    raw_result = {'fips': False}
    # second try
    raw_result1 = {'fips': True}
    # third try
    raw_result2 = {}

    # create instance of FipsFactCollector
    fips_collector = FipsFactCollector()
    # mock get_file_content to return valid fips data
    fips_collector.get_file_content = lambda filename: raw_result
    # execute collect method
    result = fips_collector.collect()
    # check if we get expected values
    assert result == {'ansible_fips': False}

    # mock get_file_content to return valid fips data
    fips_collector.get_file_content = lambda filename: raw_result1
    # execute collect method
    result = fips

# Generated at 2022-06-13 02:58:14.025619
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    assert f.collect() == {'fips': True}

# Generated at 2022-06-13 02:58:19.447847
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    _module = {}
    _collected_facts = {}
    _system_facts = {}
    _FipsFactCollector = FipsFactCollector()
    _fact_list = _FipsFactCollector.collect(_module, _collected_facts)
    _fips_facts = {}
    _fips_facts['fips'] = False
    data = get_file_content('/proc/sys/crypto/fips_enabled')
    if data and data == '1':
        _fips_facts['fips'] = True
    else:
        _fips_facts['fips'] = False
    if _fact_list != _fips_facts :
        raise Exception('Unit test for method collect of class FipsFactCollector has failed.')

# Generated at 2022-06-13 02:58:22.997403
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_collect = FipsFactCollector.collect
    FipsFactCollector_collect.func_code = test_FipsFactCollector_collect.func_code
    assert FipsFactCollector_collect(
        None,
        {'kernel': 'Linux'}
    ) == {'fips': False}

# Generated at 2022-06-13 02:58:26.159638
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    passed_facts = {}
    result = FipsFactCollector().collect(collected_facts=passed_facts)
    assert passed_facts['fips'] == result['fips']
    assert 'fips' in result
    assert type(result['fips']) == bool

# Generated at 2022-06-13 02:58:32.073653
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    # Unit test case 1:
    #   module_utils.facts.collector.BaseFactCollector.collect(module=None, collected_facts=None)
    #   -> return a hash
    # Eventually, collected_facts is a hash(see in https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/facts/collector.py)

    # No need to fake any file or to change any configuration on the system to run this unit test.
    # Create a FipsFactCollector object
    collector = FipsFactCollector()
    # Run the collect method
    collected_facts = collector.collect()
    assert type(collected_facts) is dict
    assert 'fips' in collected_facts

# Generated at 2022-06-13 02:58:34.175848
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module_mock = Mock()
    fips_facts_collector = FipsFactCollector()
    facts = fips_facts_collector.collect()
    assert facts == {'fips': False}

# Generated at 2022-06-13 03:01:16.949063
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.facts import Facts
    test_data = {'ansible_fips': True}
    test_data_fips_enable = {'ansible_fips': True, 'fips': True}
    test_data_fips_disable = {'ansible_fips': True, 'fips': False}

    Facts.fips_collector = get_collector_instance('fips')
    results = Facts.fips_collector.collect()
    assert test_data_fips_enable == results

    results['ansible_fips'] = False
    assert test_data_fips_disable == results

    # This should fail