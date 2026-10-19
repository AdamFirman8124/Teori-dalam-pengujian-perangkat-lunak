

# Generated at 2022-06-13 02:51:19.150137
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = False
    collected_facts = False
    ffc = FipsFactCollector()
    facts = ffc.collect(module, collected_facts)
    assert isinstance(facts, dict)
    assert 'fips' in facts
    assert isinstance(facts['fips'], bool)

# Generated at 2022-06-13 02:51:20.490107
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test_collector = FipsFactCollector()
    test_collector.collect()


# Generated at 2022-06-13 02:51:23.054444
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    obj = FipsFactCollector()
    obj.collect()
    # This can't be asserted, because if you run the test in a VM,
    # the method will always return False
    # assert obj.collect() == False

# Generated at 2022-06-13 02:51:33.826472
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    import mock
    import os

    module = mock.MagicMock()
    module.params = mock.MagicMock()
    module.params.get = mock.MagicMock(return_value=None)

    collected_facts = mock.MagicMock()
    collected_facts.data = {}

    with mock.patch.object(os.path, 'isfile', return_value=False):
        fact_collector = FipsFactCollector(module=module)
        facts = fact_collector.collect(module=module, collected_facts=collected_facts)
        assert facts['fips'] is False


# Generated at 2022-06-13 02:51:40.773134
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Create a temporary file /proc/sys/crypto/fips_enabled
    import tempfile
    f = tempfile.NamedTemporaryFile(mode='w')
    f.write('1')
    f.flush()
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import FactsFilesLookup
    facts_collector = Collector()
    facts_collector._lookup = FactsFilesLookup('/proc/sys/crypto/fips_enabled', root_dir=f.name)
    fips_fact = FipsFactCollector(facts_collector)
    fips_facts = fips_fa

# Generated at 2022-06-13 02:51:44.367053
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Mock the dependencies and test the method
    ffc = FipsFactCollector()
    assert ffc.name == 'fips'
    assert ffc.collect(collected_facts=dict()) == {'fips': False}

# Generated at 2022-06-13 02:51:47.267614
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    expected_fips = {
        'fips': True
    }
    fips_fc = FipsFactCollector()
    fips_facts = fips_fc.collect()
    assert fips_facts['fips'] == expected_fips['fips']

# Generated at 2022-06-13 02:51:49.303718
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    expected_facts = dict(fips=False)
    fips_collector = FipsFactCollector()
    facts_actual = fips_collector.collect()
    assert facts_actual == expected_facts

# Generated at 2022-06-13 02:51:51.260830
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    # NOTE: this is populated even if it is not set
    fips._read_file = lambda x: '1'
    assert fips.collect()['fips']

# Generated at 2022-06-13 02:51:53.291513
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact = FipsFactCollector()
    fips_facts = fips_fact.collect()
    assert fips_facts['fips'] is False

# Generated at 2022-06-13 02:51:57.590193
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector.collect() == {'fips': False}

# Generated at 2022-06-13 02:52:02.532801
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_obj = FipsFactCollector()
    # NOTE: this is populated even if it is not set
    fips_facts = {'fips': False}
    fips_facts['fips'] = False
    data = '1'
    if data and data == '1':
        fips_facts['fips'] = True
    assert fips_obj.collect() == fips_facts

# Generated at 2022-06-13 02:52:04.658427
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollectorTest = FipsFactCollector(None)
    assert FipsFactCollectorTest.collect() == {'fips': False}

# Generated at 2022-06-13 02:52:14.770840
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    data = b'1'
    # mock the get_file_content method
    def mock_get_file_content(path):
        return data
    FipsFactCollector.is_supported = lambda *args: True
    FipsFactCollector.get_file_content = mock_get_file_content
    # collect facts
    fips_facts = FipsFactCollector().collect()
    # assert results
    assert isinstance(fips_facts, dict)
    assert 'fips' in fips_facts
    assert fips_facts['fips'] is True
    # test with data == b'0'
    data = b'0'
    fips_facts = FipsFactCollector().collect()
    assert fips_facts['fips'] is False
    # test with data == b'not_an_integer'


# Generated at 2022-06-13 02:52:19.572002
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_obj = FipsFactCollector()
    fips_obj._read_file = lambda x: "1"
    assert fips_obj.collect() == {"fips":True}
    fips_obj._read_file = lambda x: "0"
    assert fips_obj.collect() == {"fips":False}
    fips_obj._read_file = lambda x: "2"
    assert fips_obj.collect() == {"fips":False}
    fips_obj._read_file = lambda x: ""
    assert fips_obj.collect() == {"fips":False}

# Generated at 2022-06-13 02:52:27.595819
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    mod = module_mock()
    # prepare
    fips_facts = {'fips': True}
    get_file_content_mock = function_mock(get_file_content)
    get_file_content_mock.return_value = '1'
    # call the method
    fips_fact_collector = FipsFactCollector()
    result = fips_fact_collector.collect(module=mod, collected_facts={})
    # assert
    assert result == fips_facts
    # cleanup
    get_file_content_mock.restore()

# Generated at 2022-06-13 02:52:32.801267
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Returns the facts for the given module
    """
    module = "FipsFactCollector"
    collected_facts = "FipsFactCollector"
    fips_facts = FipsFactCollector()
    assert fips_facts.collect(module, collected_facts)

# Generated at 2022-06-13 02:52:37.684024
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Initialize FipsFactCollector class
    fips = FipsFactCollector()
    # Execute collect method
    fips_facts = fips.collect()
    # Check fips key exists
    assert 'fips' in fips_facts
    # Check fips value is boolean
    assert isinstance(fips_facts['fips'], bool)

# Generated at 2022-06-13 02:52:40.147192
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    assert fips_collector  # Just to avoid flakes error
    assert fips_collector.collect() == {'fips': False}

# Generated at 2022-06-13 02:52:41.765359
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    output = {'fips': False}
    fips_fc = FipsFactCollector()
    assert fips_fc.collect() == output

# Generated at 2022-06-13 02:52:46.385834
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector.collect()
    assert 'fips' in fips_facts

# Generated at 2022-06-13 02:52:49.149916
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector()
    fs = {'/proc/sys/crypto/fips_enabled': "1"}
    assert fips_facts.collect(None, None, file_system=fs)['fips'] is True

# Generated at 2022-06-13 02:52:51.494061
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    assert fips_collector.collect()
    assert 'fips' in fips_collector.collect().keys()

# Generated at 2022-06-13 02:52:56.127701
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collectors.system.fips import FipsFactCollector
    fips_collector = FipsFactCollector()
    facts_collector = FactsCollector(
        module=None,
        collected_facts=Facts(module_name='test'),
        collectors=[fips_collector])
    facts_collector.collect()
    assert 'fips' in fips_collector.collected_facts
    assert 'fips' in facts_collector.collected_facts

# Generated at 2022-06-13 02:53:03.896100
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test FipsFactCollector.collect"""

    # create object of FipsFactCollector
    testobj = FipsFactCollector(module=None, collected_facts=None)
    # get fipsfacts
    fipsfacts = testobj.collect()
    # assert fips is false
    assert fipsfacts == {u'fips': False}
    # get fipsfacts
    fipsfacts1 = testobj.collect(
        {"fips": True}, None)
    # assert fips is true
    assert fipsfacts1 == {u'fips': True}

# Generated at 2022-06-13 02:53:05.916344
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    assert f.collect() == {'fips': False}

# Generated at 2022-06-13 02:53:08.320406
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    data = '0'
    fips = FipsFactCollector()
    fips_facts = fips.collect(module, data)
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:53:10.132717
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector.collect(module=None, collected_facts=None)
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:53:11.060113
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert 'fips' in FipsFactCollector().collect()

# Generated at 2022-06-13 02:53:14.401037
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()

    # Data is not set
    f.collect()

    # Data is set but not '1'
    f.get_file_content = lambda path: '2'
    f.collect()

# Generated at 2022-06-13 02:53:24.542980
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    # Test for method collect of class FipsFactCollector
    # Return a dict with 'fips' key

    # A class for a fact collector of type 'fips'
    fips = FipsFactCollector()

    # A class representing a module without argument
    module = None
    collected_facts = {}
    assert fips.collect(module=module, collected_facts=collected_facts) == {'fips': False}

    # A class representing a module with argument
    module = None
    collected_facts = {'fips': True}
    assert fips.collect(module=module, collected_facts=collected_facts) == {'fips': True}

# Generated at 2022-06-13 02:53:32.968818
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """ Unit test for method collect of class FipsFactCollector. """
    # set default value for parameters: module and collected_facts
    module = None
    collected_facts = None
    # set expected return value
    expected = {
        'fips': False
    }
    # instantiate object under test
    fips_fact_collector = FipsFactCollector()
    # invoke method under test
    actual = fips_fact_collector.collect(module, collected_facts)
    # assert that method returns expected value
    assert expected == actual

# Generated at 2022-06-13 02:53:35.786785
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    ffc = FipsFactCollector()
    collected_facts = {}
    collected_facts = ffc.collect(collected_facts)
    assert 'fips' in collected_facts

# Generated at 2022-06-13 02:53:38.056816
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fipsFactCollector = FipsFactCollector()
    fipsFact = fipsFactCollector.collect()
    assert 'fips' in fipsFact

# Generated at 2022-06-13 02:53:38.661345
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    pass

# Generated at 2022-06-13 02:53:48.247051
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    FipsFactCollector.collect = test_FipsFactCollector_collect.original_method
    get_file_content = test_FipsFactCollector_collect.original_get_file_content
    fips_facts = FipsFactCollector().collect()

    # Check if the collect method is returning the dictionary with
    # the fips key, containing the right value
    assert fips_facts['fips'] == True


test_FipsFactCollector_collect.original_method = FipsFactCollector.collect
test_FipsFactCollector_collect.original_get_file_content = get_file_content


# Generated at 2022-06-13 02:53:50.634789
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    assert fips_collector.collect()['fips'] == False

# Generated at 2022-06-13 02:53:53.607335
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_obj = FipsFactCollector()
    if isinstance(FipsFactCollector_obj, FipsFactCollector):
        print("Instance is created")
    print(FipsFactCollector_obj.collect())

# Generated at 2022-06-13 02:54:03.171175
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test_data = dict(
        module_name='test_ansible_module',
        module_args=dict(),
        module_kwargs=dict()
    )
    fips_facts = dict(
        fips=False
    )

    # mock get_file_content
    def mock_get_file_content(path):
        return '0'

    fips_factCollector = FipsFactCollector()
    fips_factCollector._module = test_data['module_name']
    fips_factCollector._module_args = test_data['module_args']
    fips_factCollector._module_kwargs = test_data['module_kwargs']
    fips_factCollector.get_file_content = mock_get_file_content

# Generated at 2022-06-13 02:54:06.204575
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect()
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:54:10.274127
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    result = f.collect()
    assert result.keys() == ['fips']

# Generated at 2022-06-13 02:54:13.141199
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    c = FipsFactCollector()
    collected_facts = {}
    result = c.collect(collected_facts=collected_facts)
    assert result == {'fips': False}
    assert collected_facts == {'fips': False}
    del result['fips']
    result = c.collect(collected_facts=collected_facts)
    assert result == {}

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:54:15.598112
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Test the method FipsFactCollector.collect
    """
    pass

# Generated at 2022-06-13 02:54:18.231237
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    result = fips.collect()
    assert result['fips'] == False or result == None or result['fips'] == True

# Generated at 2022-06-13 02:54:23.835715
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_get_file_content = get_file_content

    def test_data():
        return '1'
    get_file_content = test_data
    collector = FipsFactCollector()
    # test normal call with no exception
    collector.collect()
    # test with exception
    get_file_content = None
    collector.collect()
    # reset the callable
    get_file_content = FipsFactCollector_get_file_content

# Generated at 2022-06-13 02:54:28.233481
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    module = None
    collected_facts = {}
    ans = {'fips': False}
    result = collector.collect(module=module, collected_facts=collected_facts)
    assert type(result) == dict
    assert result == ans
    assert 'fips' in result
    assert type(result['fips']) == bool

# Generated at 2022-06-13 02:54:34.611060
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    base_fact_collector = BaseFactCollector()
    fips_fact_collector = FipsFactCollector()
    assert isinstance(base_fact_collector, BaseFactCollector)
    assert isinstance(fips_fact_collector, FipsFactCollector)
    assert fips_fact_collector.name == 'fips'
    assert not fips_fact_collector.get_fact_ids()

# Generated at 2022-06-13 02:54:36.391271
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    
    collector = FipsFactCollector()
    result = collector.collect()
    assert result == {'fips': False}

# Generated at 2022-06-13 02:54:37.932588
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collectFips = FipsFactCollector()
    collected_facts = collectFips.collect()
    assert collected_facts == {'fips': False}

# Generated at 2022-06-13 02:54:39.145827
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    assert fips.collect() == {'fips': False}

# Generated at 2022-06-13 02:54:49.856875
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    c = FipsFactCollector()
    # Set fact fips to True
    data = '1'
    assert c.collect(None, None)['fips']
    # Set fact fips to False
    data = '0'
    assert not c.collect(None, None)['fips']
    # Set fact fips to False
    data = None
    assert not c.collect(None, None)['fips']

# Generated at 2022-06-13 02:54:51.740219
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    fips_collector.collect()
    assert fips_collector.name == 'fips'

# Generated at 2022-06-13 02:54:56.140192
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    facts = {}
    fact_collector = FipsFactCollector()
    fact_collector.collect(None, facts)
    assert 'fips' in facts
    assert isinstance(facts['fips'], bool)
    assert facts['fips'] == False
    facts['ansible_processor'] = ['Intel(R) Core(TM) i5 CPU       M 460  @ 2.53GHz']

# Generated at 2022-06-13 02:55:00.783163
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import pytest

    mod = pytest.Mock()
    fips_fc = FipsFactCollector(mod)
    data = ('1')
    mod.get_file_content.return_value = data
    fips_fc.collect()
    mod.get_file_content.assert_called_once_with('/proc/sys/crypto/fips_enabled')

# Generated at 2022-06-13 02:55:03.254921
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect()
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:55:04.329811
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    result = collector.collect()

    assert(result == {'fips':False})

# Generated at 2022-06-13 02:55:09.019985
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collectors.fips import FipsFactCollector
    from ansible.module_utils._text import to_bytes

    my_obj = FipsFactCollector()

    data = b'0'
    result = {'fips': False}
    with Collector._mocked_open_file('/proc/sys/crypto/fips_enabled', data):
        result_obj = my_obj.collect(None, None)

    assert result_obj == result

    data = b'1'
    result = {'fips': True}

# Generated at 2022-06-13 02:55:17.011950
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.fips import FipsFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    facts_dict = dict()
    fp = FipsFactCollector()
    fp.collect(module=None, facts=facts_dict)
    if 'fips' not in facts_dict:
        raise RuntimeError("No fips fact present in facts_dict")
    if facts_dict['fips'] != get_file_content('/proc/sys/crypto/fips_enabled'):
        raise RuntimeError("fips fact collector returned wrong value")
    facts_dict = dict()
    fp = FipsFactCollector()

# Generated at 2022-06-13 02:55:27.625813
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    def get_file_content_mock(f_path=None):
        return '1'
    FipsFactCollector._get_file_content = get_file_content_mock
    fips_fct = FipsFactCollector()
    collected_facts = {}
    collected_facts = fips_fct.collect(collected_facts=collected_facts)
    assert collected_facts['fips'] == True

    def get_file_content_mock(f_path=None):
        return '0'
    FipsFactCollector._get_file_content = get_file_content_mock
    fips_fct = FipsFactCollector()
    collected_facts = {}
    collected_facts = fips_fct.collect(collected_facts=collected_facts)
    assert collected_facts

# Generated at 2022-06-13 02:55:28.993665
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    facts = collector.collect()
    assert facts == {"fips": True}

# Generated at 2022-06-13 02:55:46.502927
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    c = FipsFactCollector(None)
    c.collect()

# Generated at 2022-06-13 02:55:47.657344
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    FipsFactCollector._fact_ids.add('fips')
    fips_facts = collector.collect()
    assert fips_facts
    assert 'fips' in fips_facts

# Generated at 2022-06-13 02:55:48.986453
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    obj = FipsFactCollector()
    fact = obj.collect()
    assert fact['fips'] == False

# Generated at 2022-06-13 02:55:49.759838
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector.collect()

# Generated at 2022-06-13 02:55:54.509974
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Unit test for method 'collect' of class FipsFactCollector"""
    from ansible.module_utils.facts.collector import Collector

    fips_fact_collector = FipsFactCollector()
    collector = Collector()
    collector.collect(fips_fact_collector)
    assert collector._collected_facts == {'fips': False}

    fips_fact_collector = FipsFactCollector()
    collector = Collector()
    collector.add_fact('/proc/sys/crypto/fips_enabled', b'1\n')
    collector.collect(fips_fact_collector)
    assert collector._collected_facts == {'fips': True}

# Generated at 2022-06-13 02:56:01.313564
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Create new instance of FipsFactCollector
    fips_fact_collector = FipsFactCollector()

    # Create an object that mimics the anstible module object
    module = None

    # Create an object that mimics the anstible collected facts object
    collected_facts = None

    # Call the 'collect' method on our object
    result = fips_fact_collector.collect(module, collected_facts)

    # Check the values of the expected fields in the collected facts
    assert result['fips'] is False or result['fips'] is True

# Generated at 2022-06-13 02:56:03.483917
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    collected_fips_facts = fips_fact_collector.collect()
    assert collected_fips_facts == {'fips':False}

# Generated at 2022-06-13 02:56:07.319504
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect()
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:56:08.503130
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    facts = collector.collect()
    assert('fips' in facts)
    assert(not facts['fips'])

# Generated at 2022-06-13 02:56:12.195923
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    t = FipsFactCollector()
    fips_facts = t.collect(module=None, collected_facts={'kernel': 'Linux'})
    assert fips_facts['fips'] == False


# Generated at 2022-06-13 02:56:47.992742
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Unit test for method collect of class FipsFactCollector.
    """
    fips_facts = {
        'fips': False
    }
    fips_collector = FipsFactCollector()
    assert fips_collector.name == 'fips'
    assert fips_collector.collect() == fips_facts

# Generated at 2022-06-13 02:56:52.690726
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector.name == 'fips'
    assert fips_fact_collector._fact_ids == set()
    
    fips_facts = fips_fact_collector.collect()
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:56:54.582823
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector()
    assert isinstance(fips_facts.collect(), dict)
    return


# Generated at 2022-06-13 02:56:55.836676
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fc = FipsFactCollector()
    assert 'fips' in fc.collect()

# Generated at 2022-06-13 02:56:59.428241
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # arrange
    module_mock = None
    collected_facts_mock = None
    expected_return_value = {'fips': True}

    # act
    actual_return_value = FipsFactCollector.collect(module_mock, collected_facts_mock)

    # assert
    assert expected_return_value == actual_return_value

# Generated at 2022-06-13 02:57:05.117352
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Patch get_file_content to return data from directory.
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.collector.fips import FipsFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    old_get_file_content = get_file_content
    _module = None
    _collected_facts = None
    def _test_get_file_content(path):
        if path == '/proc/sys/crypto/fips_enabled':
            return '1\n'
        return old_get_file_content(path)
    get_file_content = _test_get_file_content

    # Create a new FipsFactCollector object.
    x = FipsFactCollector()

    # Check the facts for

# Generated at 2022-06-13 02:57:06.950390
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    collected_facts = {}
    collected_facts['fips'] = True
    assert collector.collect(None, collected_facts)
    assert collected_facts['fips'] == True

# Generated at 2022-06-13 02:57:08.625673
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test = FipsFactCollector()
    assert test

# Generated at 2022-06-13 02:57:10.175370
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    collected_facts = {}
    assert fips_fact_collector.collect(collected_facts=collected_facts) == {'fips': False}

# Generated at 2022-06-13 02:57:11.331556
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    facts = {}
    f.collect(None, facts)
    assert 'fips' in facts

# Generated at 2022-06-13 02:58:25.503921
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # NOTE: the output is captured only if a file exists, in
    # the test environment it will not exist
    fips_facts = FipsFactCollector().collect()
    assert not fips_facts['fips']

# Generated at 2022-06-13 02:58:26.745713
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    assert fips.collect() == {'fips': True}

# Generated at 2022-06-13 02:58:28.970756
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    content = fips_fact_collector.collect()
    assert(content == {'fips': False})

# Generated at 2022-06-13 02:58:34.173396
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    fake_module = 'a fake module'
    fake_facts = 'some fake facts'

    with open('/proc/sys/crypto/fips_enabled', 'w') as f:
        f.write('1')

    assert FipsFactCollector.collect(None, None) == { 'fips': True }

    with open('/proc/sys/crypto/fips_enabled', 'w') as f:
        f.write('0')

    assert FipsFactCollector.collect(None, None) == { 'fips': False }

# Generated at 2022-06-13 02:58:35.618509
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector.collect() == {'fips': False}

# Generated at 2022-06-13 02:58:37.045794
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fact_collector = FipsFactCollector()
    assert(fact_collector.collect() == {'fips': False})

# Generated at 2022-06-13 02:58:37.658008
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # the method cannot be tested in unit tests
    pass

# Generated at 2022-06-13 02:58:40.132721
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collected_facts = dict()
    result = FipsFactCollector().collect(collected_facts=collected_facts)
    assert 'fips' in result


# Generated at 2022-06-13 02:58:42.950880
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test that collect method of FipsFactCollector works.

    """
    f = FipsFactCollector()
    collected_facts = dict()
    f.collect(collected_facts=collected_facts)
    assert collected_facts['fips'] == False

# Generated at 2022-06-13 02:58:47.209193
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    collected_facts = None
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect(module=module, collected_facts=collected_facts)
    assert len(fips_facts.keys()) == 1
    assert fips_facts['fips'] == False