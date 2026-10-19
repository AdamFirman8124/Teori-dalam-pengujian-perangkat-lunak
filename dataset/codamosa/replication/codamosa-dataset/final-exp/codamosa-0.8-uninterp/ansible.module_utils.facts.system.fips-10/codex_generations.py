

# Generated at 2022-06-13 02:51:17.344727
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector().collect(None, None)
    assert type(fips_facts) is dict
    assert set(['fips']) == set(fips_facts.keys())

# Generated at 2022-06-13 02:51:20.016981
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_fact_collector.collect()
    assert fips_fact_collector.name == 'fips'
    assert fips_fact_collector._fact_ids == set()

# Generated at 2022-06-13 02:51:25.823860
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    import os
    import yaml

    from ansible.module_utils._text import to_bytes

    FipsFactCollector._fact_ids = set()
    collector = FipsFactCollector()

    my_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_fixture = os.path.join(my_dir, 'fixtures/fips_enabled')

    with open(path_to_fixture, 'rb') as fips_fd:
        data = fips_fd.read()
        fips_fd.seek(0)
        yaml.safe_load(fips_fd)

    with open('/proc/sys/crypto/fips_enabled', 'w') as fips_fd:
       fips_fd.write('1')
       fips

# Generated at 2022-06-13 02:51:28.636222
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Arrange
    collect = FipsFactCollector()
    # Act
    result = collect.collect()
    # Assert
    assert result['fips'] == False

# Generated at 2022-06-13 02:51:36.299444
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    collected_facts = None
    fips_module_mock = flexmock(__name__='fips_module_mock')
    flexmock(fips_module_mock.ansible.module_utils).should_receive('facts.utils').and_return(
        flexmock(get_file_content=lambda x: '1'))
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector.collect(module, collected_facts) == {'fips': True}

# Generated at 2022-06-13 02:51:38.287898
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector().collect()
    assert type(fips_facts['fips']) == bool, "Fact fips must be a boolean"

# Generated at 2022-06-13 02:51:39.359850
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert FipsFactCollector().collect()['fips'] == False

# Generated at 2022-06-13 02:51:42.909745
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector.collect() == {'fips': False}

# Generated at 2022-06-13 02:51:44.119570
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert FipsFactCollector.collect(None, None) == {'fips': False}


# Generated at 2022-06-13 02:51:47.054338
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    fact_collector = FipsFactCollector()
    detected_facts = fact_collector.collect()

    # Set of keys expected for the detected_facts dict
    detected_facts_keys = { 'fips' }

    assert detected_facts.keys() == detected_facts_keys

# Generated at 2022-06-13 02:51:51.076180
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_instance = FipsFactCollector()
    assert FipsFactCollector_instance is not None
    assert FipsFactCollector_instance.collect() is not None

# Generated at 2022-06-13 02:51:54.417612
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    collected_facts = {}
    fips_collected_facts = {'fips': False}
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector.collect(module, collected_facts) == fips_collected_facts

# Generated at 2022-06-13 02:51:58.105054
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fact_collector_mock = FipsFactCollector()
    fips_val = fact_collector_mock.collect()
    assert type(fips_val) == dict
    assert 'fips' in fips_val


# Generated at 2022-06-13 02:52:03.327037
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test FipsFactCollector.collect"""

    # Create fixture
    FipsFactCollectorObject = FipsFactCollector()

    # Create mock
    get_file_contentMock = lambda x: '1'

    # Execute method
    result = FipsFactCollectorObject.collect(get_file_content=get_file_contentMock)

    # Verify result
    assert result == { 'fips': True }


# Generated at 2022-06-13 02:52:13.807835
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # given
    import os
    import tempfile
    test_FipsFactCollector = FipsFactCollector()
    test_module = None
    test_FipsFactCollector_collect_collected_facts = None
    temp_file = tempfile.TemporaryFile()
    test_fips_enabled = "A\n"
    temp_file.write(test_fips_enabled.encode('utf-8'))
    temp_file.seek(0)
    temp_file.name = "/proc/sys/crypto/fips_enabled"

    # when

# Generated at 2022-06-13 02:52:17.534711
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fact_collector = FipsFactCollector()

    def mock_get_file_content(file_name):
        if file_name == '/proc/sys/crypto/fips_enabled':
            return '1'
        return None

    fact_collector.get_file_content = mock_get_file_content

    # Call the collect method
    result = fact_collector.collect()

    assert result == {'fips': True}, \
        "The output should contain only one item with key as 'fips' and value as 'True'"

# Generated at 2022-06-13 02:52:20.325777
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_test_obj = FipsFactCollector()
    assert fips_test_obj.collect() == {u'fips': False}

# Generated at 2022-06-13 02:52:22.584239
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    vector_out = {
        'fips': False,
    }
    collector = FipsFactCollector()
    assert collector.collect() == vector_out

# Generated at 2022-06-13 02:52:26.144027
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Test FipsFactCollector.collect
    """
    fips_fact_collector = FipsFactCollector()
    collected_facts = fips_fact_collector.collect()
    assert collected_facts['fips'] is False

# Generated at 2022-06-13 02:52:28.282354
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

   content = b'1\n'
   f = FipsFactCollector()
   result = f.collect({}, {})

   assert result['fips']

# Generated at 2022-06-13 02:52:39.873293
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Test collect function for FipsFactCollector.
    """
    from ansible.module_utils.facts.utils import FactsFiles
    from ansible.module_utils.facts.collector import FactCollector

    caller_instance = FactCollector()
    FipsFactCollector().collect(caller_instance)
    fact = {}
    fact['fips'] = False
    assert caller_instance.get_fact('fips') == fact

# Generated at 2022-06-13 02:52:41.257836
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert FipsFactCollector().collect() == {'fips': False}


# Generated at 2022-06-13 02:52:47.199591
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Unit test for method collect of class FipsFactCollector
    """
    fips_collector = FipsFactCollector()
    fips_facts = fips_collector.collect()

    # Check valid keys
    assert set(fips_facts.keys()) == set('fips')

    # Check fips key
    assert isinstance(fips_facts['fips'], bool)

# Generated at 2022-06-13 02:52:48.083815
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector.collect()

# Generated at 2022-06-13 02:52:49.186512
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fipsFactCollector = FipsFactCollector()
    assert fipsFactCollector.collect()

# Generated at 2022-06-13 02:52:52.122851
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    print('Testing FipsFactCollector')
    fips_collector = FipsFactCollector()
    facts = fips_collector.collect()
    print('Facts for FipsFactCollector: %s' % facts)

# Generated at 2022-06-13 02:52:56.179004
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect()
    assert 'fips' in fips_facts
    assert isinstance(fips_facts['fips'], bool)

# Generated at 2022-06-13 02:52:58.741502
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    fips_collector.collect()
    assert len(fips_collector.collect()) == 1

# Generated at 2022-06-13 02:53:06.573173
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test for `FipsFactCollector.collect` method"""

    #set up test environment
    fips_content = '1'
    fips_content_b = b'1'
    non_fips_content = '0'
    non_fips_content_b = b'0'

    import pytest

    # First test with fips enabled
    facts_collector = FipsFactCollector()
    fips_facts = facts_collector.collect(
        module=None,
        collected_facts=None,
    )
    assert fips_facts['fips'] == True

test_FipsFactCollector_collect()

# Generated at 2022-06-13 02:53:08.029627
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_fact_collector.collect()

# Generated at 2022-06-13 02:53:24.489397
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    ffc = FipsFactCollector()
    ans = str(ffc.collect)
    assert ans == '<bound method FipsFactCollector.collect of <ansible.module_utils.facts.fips.FipsFactCollector object at 0x7f36c3d2e358>>'


# Generated at 2022-06-13 02:53:26.086534
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    facts = fips.collect()
    assert facts["fips"] == False

# Generated at 2022-06-13 02:53:28.836900
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    r = FipsFactCollector()
    assert 'crypto/fips_enabled' in r.collect()
    assert 'fips' in r.collect()

# Generated at 2022-06-13 02:53:31.352433
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    data = fips.collect()
    assert data == {'fips': True}

# Generated at 2022-06-13 02:53:34.806396
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect(None, None)
    assert fips_facts == {}

# Generated at 2022-06-13 02:53:40.182911
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    from ansible.module_utils.facts.collector import Collector
    collector = Collector()
    fips_facts_collector = FipsFactCollector()
    collected_facts = fips_facts_collector.collect(collected_facts=collector.collected_facts)
    assert "fips" in collected_facts
    assert collected_facts["fips"] == False
    assert "module" not in collected_facts

# Generated at 2022-06-13 02:53:43.889897
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = get_module()
    collected_facts = dict()
    module.exit_json = dict()
    FipsFactCollector(module).collect(module, collected_facts)

# Mock module

# Generated at 2022-06-13 02:53:50.760714
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    mock_module = type('module', (object,), {'fail_json': lambda msg: msg})()
    mock_module.params = {}

    results = FipsFactCollector().collect(module=mock_module, collected_facts=None)
    assert type(results) == type({}), results
    assert 'fips' in results, results

    # Verify that the value is a boolean
    expected = True if results['fips'] else False
    assert results['fips'] == expected, results

# Generated at 2022-06-13 02:53:52.674086
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    facts = fips_collector.collect()
    assert not facts['fips']

# Generated at 2022-06-13 02:53:55.960561
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    res = fips_fact_collector.collect()
    assert res == {'fips': False}

# Generated at 2022-06-13 02:54:09.715189
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # create FipsFactCollector instance
    fips_collector = FipsFactCollector()
    # call method collect of class FipsFactCollector
    fips_collector.collect()

# Generated at 2022-06-13 02:54:15.876878
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Setup fixture
    sys_fips_enabled_fixture = './unit/ansible/data/system/fips/fips_enabled'
    fips_fact_collector = FipsFactCollector()

    # Test case #1: Check that if fips is not enabled, function returns False
    # Mock module
    module = Mock()
    module.get_bin_path.side_effect = lambda x, required=False: '/bin/' + x
    module.run_command.side_effect = lambda x, check_rc=True, close_fds=True: \
        ({'stdout_lines': [None]}, None)

    # Call method collect
    result = fips_fact_collector.collect(module)

    # Verify function return
    assert result['fips'] is False

    # Test case #2:

# Generated at 2022-06-13 02:54:19.427372
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    if fips_fact_collector.collect().get('fips'):
        assert get_file_content('/proc/sys/crypto/fips_enabled') == '1'



# Generated at 2022-06-13 02:54:26.541701
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    ''' Test for _FipsFactCollector._collect_file '''
    from ansible.module_utils.facts.collectors.system.fips import FipsFactCollector

    with open('unittest_data/proc_sys_crypto_fips_enabled_1', 'r') as fips_test_file:
        fips_test_data = fips_test_file.read()
        test_fips_collector = FipsFactCollector({}, {}, {})
        fips_facts = test_fips_collector.collect()
        assert fips_facts['fips']

# Generated at 2022-06-13 02:54:32.487493
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = {}
    fips_facts['fips'] = False
    data = get_file_content('/proc/sys/crypto/fips_enabled')
    if data and data == '1':
        fips_facts['fips'] = True
    fips_test = FipsFactCollector().collect()
    assert(fips_test == fips_facts)

# Generated at 2022-06-13 02:54:40.157431
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import os
    import tempfile
    test_collector = FipsFactCollector()

    # When the file 'fips_enabled' is not found
    # Then No value is returned
    os.unlink = lambda *args: None
    assert test_collector.collect() == {}

    # When the file 'fips_enabled' is found but is empty
    # Then False is returned
    os.unlink = lambda *args: None
    os.path.exists = lambda *args: True
    os.open = lambda *args: None
    test_collector.get_file_content = lambda *args: None
    assert test_collector.collect() == {'fips': False}

    # When the file 'fips_enabled' is found but its content is not '1'
    # Then False is returned
    os.un

# Generated at 2022-06-13 02:54:40.745014
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector().collec

# Generated at 2022-06-13 02:54:44.397259
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact = FipsFactCollector()
    with open('/proc/sys/crypto/fips_enabled', 'w') as fp:
        fp.write('0')

    fips_facts = fips_fact.collect()
    assert isinstance(fips_facts, dict)
    assert fips_facts['fips'] == False

    with open('/proc/sys/crypto/fips_enabled', 'w') as fp:
        fp.write('1')

    fips_facts = fips_fact.collect()
    assert isinstance(fips_facts, dict)
    assert fips_facts['fips'] == True

# Generated at 2022-06-13 02:54:53.859214
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from io import StringIO

    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector

    # When /proc/sys/crypto/fips_enabled exists and contains '1',
    # fips_facts['fips'] should be True
    def mock_get_file_content_with_fips_enabled(f, default=None):
        return '1'
    get_file_content.side_effect = mock_get_file_content_with_fips_enabled

    cf = FipsFactCollector()
    test_data = cf.collect()
    assert test_data['fips'] is True

    # When /proc/sys/crypto/fips_enabled exists and contains '0',
    # fips_facts['f

# Generated at 2022-06-13 02:54:55.191923
# Unit test for method collect of class FipsFactCollector

# Generated at 2022-06-13 02:55:31.018001
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()

    with open('/proc/sys/crypto/fips_enabled', 'w') as fips_file:
        fips_file.write('1')
    facts = fips_collector.collect()
    assert facts['fips'] == True

    # If fips_enabled file does not exist, it's False, that's the default
    with open('/proc/sys/crypto/fips_enabled', 'w') as fips_file:
        fips_file.write('0')
    facts = fips_collector.collect()
    assert facts['fips'] == False

# Generated at 2022-06-13 02:55:32.343862
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    assert 'fips' in f.collect().keys()

# Generated at 2022-06-13 02:55:41.698149
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    f = FipsFactCollector()
    # Verify that if file is empty, we get False
    content = ''
    result = f.collect(get_file_content=lambda x: content)
    assert result == {'fips': False}
    # Verify that if file contains "0", we get False
    content = '0'
    result = f.collect(get_file_content=lambda x: content)
    assert result == {'fips': False}
    # Verify that if file contains "1", we get True
    content = '1'
    result = f.collect(get_file_content=lambda x: content)
    assert result == {'fips': True}
    # Verify that if file contains corrupted data, we get False
    content = '2'

# Generated at 2022-06-13 02:55:48.170485
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():

    # Test the FIPS not enabled case
    test_fact_collector = FipsFactCollector()
    test_data = "0\n"
    fips_facts = test_fact_collector.collect(collected_facts=None,
                                             data=test_data)
    assert fips_facts['fips'] == False

    # Test the FIPS enabled case
    test_data = "1\n"
    fips_facts = test_fact_collector.collect(collected_facts=None,
                                             data=test_data)
    assert fips_facts['fips'] == True

# Generated at 2022-06-13 02:55:50.105576
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fipsFactCollector = FipsFactCollector()
    fips_facts = fipsFactCollector.collect()
    assert isinstance(fips_facts, dict)

# Generated at 2022-06-13 02:55:55.318394
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    mocker = Mocker()
    sut = FipsFactCollector()
    fips_facts = {}
    fips_facts['fips'] = False
    mock_data = mocker.mock()
    expect(mock_data == '1').result(False).count(1)
    expect(mock_data == '0').result(True).count(1)
    get_file_content('/proc/sys/crypto/fips_enabled').result(None).count(1)
    get_file_content('/proc/sys/crypto/fips_enabled').result(mock_data).count(1)
    mocker.replay()
    result = sut.collect()
    assert result == fips_facts
    result = sut.collect()
    fips_facts['fips'] = True


# Generated at 2022-06-13 02:56:02.417335
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    # Test that the fips fact is true when fips_enabled is 1
    fips_fact_collector.fetch_file_from_device = lambda x: b'1'
    assert fips_fact_collector.collect() == { 'fips': True }
    # Test that the fips fact is false when fips_enabled is blank
    fips_fact_collector.fetch_file_from_device = lambda x: b''
    assert fips_fact_collector.collect() == { 'fips': False }

# Generated at 2022-06-13 02:56:06.442604
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # return value of collect method when fips is disabled in Linux
    assert FipsFactCollector.collect() == {'fips': False}

# Generated at 2022-06-13 02:56:08.616544
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact = FipsFactCollector()
    fips_facts = fips_fact.collect()
    assert 'fips' in fips_facts.keys()

# Generated at 2022-06-13 02:56:14.335624
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = {}
    fips_facts['fips'] = True
    fips = FipsFactCollector()
    f = open('/proc/sys/crypto/fips_enabled', 'w')
    f.write('1')
    f.close()
    assert fips.collect() == fips_facts

# Generated at 2022-06-13 02:57:20.727577
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    result = fips_collector.collect()

    assert 'fips' in result.keys()

# Generated at 2022-06-13 02:57:29.136398
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()

    # Set fips to False, if file does not exist
    fips_facts = {'fips': False}
    data = {}
    assert(collector.collect(collected_facts=data) == fips_facts)

    # Set fips to True, if data is 1
    fips_facts = {'fips': True}
    data = {'ansible_fips': False}
    get_file_content_mock = lambda x: '1'
    collector.files = {'fips': '/proc/sys/crypto/fips_enabled'}
    collector.get_file_content = get_file_content_mock
    assert(collector.collect(collected_facts=data) == fips_facts)

# Generated at 2022-06-13 02:57:32.228724
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    mock_module = 'AnsibleModule'
    collected_facts = {}

    fips = FipsFactCollector()
    result = fips.collect(module=mock_module,
                          collected_facts=collected_facts)
    assert result == {'fips': False}

# Generated at 2022-06-13 02:57:41.346797
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import inspect
    import sys
    import os
    import collections
    import stat

    class MockModule(object):
        def __init__(self, args=None, tmpfile=None):
            self.params = args
            self.tmpfile = tmpfile

        def fail_json(self, **kwargs):
            pass

        def add_cleanup_file(self, path):
            pass

    class MockCollectedFacts(object):
        def __init__(self, facts={}):
            self.facts = facts

        def add_facts(self, facts):
            self.facts.update(facts)

    class MockFile(object):
        def __init__(self, name):
            self.name = name
            self.content = ''

        def read(self):
            return self.content


# Generated at 2022-06-13 02:57:46.387342
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    collected_facts = {}
    collected_facts['fips'] = False
    data = get_file_content('/proc/sys/crypto/fips_enabled')
    if data and data == '1':
        collected_facts['fips'] = True
    assert fips_fact_collector.collect() == collected_facts



# Generated at 2022-06-13 02:57:48.152574
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_instance = FipsFactCollector()
    FipsFactCollector_instance.collect()
    assert isinstance(FipsFactCollector_instance.collect(), dict)

# Generated at 2022-06-13 02:57:55.379834
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collectors.fips import FipsFactCollector
    from ansible.module_utils.facts.collectors.fips import get_file_content
    import pytest
    from ansible.module_utils._text import to_bytes, to_native

    class MockGetFileContent:
        def __init__(self, data):
            self._data = data
        def __call__(self, f):
            return self._data

    # no file
    get_file_content_orig = get_file_content
    get_file_content = MockGetFileContent(None)
    fact_collector = FipsFactCollector()
    assert fact_collector.collect() == {'fips': False}
    get_file_content = get_file_content_orig

    # empty file


# Generated at 2022-06-13 02:57:56.977030
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_inst = FipsFactCollector()
    assert FipsFactCollector_inst.collect() == { 'fips': False }

# Generated at 2022-06-13 02:57:58.613003
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert get_FipsFactCollector_collect_return_value() == {'fips': False}



# Generated at 2022-06-13 02:58:01.220912
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    result = fips_fact_collector.collect()
    assert result['fips'] == False

# Generated at 2022-06-13 02:59:18.944389
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Unit test for method collect of class FipsFactCollector
    """
    fact_collector = FipsFactCollector()
    mock_module = object()
    assert fact_collector.collect(module=mock_module)

# Generated at 2022-06-13 02:59:23.408464
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Module mock
    class ModuleMock:
        def __init__(self):
            self.params = None
            self.exit_json = None

    # Class instance
    fips_facts = FipsFactCollector()

    # Module instance
    module_mock = ModuleMock()
    module_mock.params = {}

    # Collect
    result = fips_facts.collect(module_mock)

    assert isinstance(result, dict)
    assert 'fips' in result

# Generated at 2022-06-13 02:59:30.112775
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = {}
    fips_facts['fips'] = False
    data = '0'
    if data and data == '1':
        fips_facts['fips'] = True
    assert fips_facts['fips'] == False

    fips_facts = {}
    fips_facts['fips'] = False
    data = '1'
    if data and data == '1':
        fips_facts['fips'] = True
    assert fips_facts['fips'] == True

# Generated at 2022-06-13 02:59:36.469818
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_file_content = '1'
    fips_file_content_empty = ''
    fips_file_content_zero = '0'
    fips_file_content_not_fips = '2'
    fips_file_content_invalid = 'not valid'
    fips_file_content_not_found = None
    fips_facts = {
        'fips': True
    }
    fips_facts_invalid = {
        'fips': False
    }
    
    # create mock objects 
    mock_module = MagicMock()
    mock_collected_facts = MagicMock()
    mock_method = MagicMock(return_value=fips_file_content)
    
    # create mock module and class

# Generated at 2022-06-13 02:59:38.215299
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert FipsFactCollector().collect() == {'fips': True}

# Generated at 2022-06-13 02:59:39.490410
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fact_collector = FipsFactCollector()
    fact_collector.collect()
    assert 'fips' in fact_collector.fact_ids

# Generated at 2022-06-13 02:59:40.537187
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    result = FipsFactCollector().collect()
    assert result['fips'] is False


# Generated at 2022-06-13 02:59:46.628943
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # The proc file /proc/sys/crypto/fips_enabled does not exist
    fips_collector = FipsFactCollector()
    fips_facts = fips_collector.collect()
    assert type(fips_facts['fips']) is bool
    assert fips_facts['fips'] == False

    # The proc file /proc/sys/crypto/fips_enabled exists
    # but the file is empty
    fips_collector = FipsFactCollector()
    fips_facts = fips_collector.collect()
    assert type(fips_facts['fips']) is bool
    assert fips_facts['fips'] == False

    # The proc file /proc/sys/crypto/fips_enabled exists
    # and the file is not empty

# Generated at 2022-06-13 02:59:47.861829
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector().collect()
    assert type(fips_facts['fips']) is bool

# Generated at 2022-06-13 02:59:49.654897
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """ Test collect function of FipsFactCollector class
    """
    # Test case 1:
    set_module_args({})

    # Test case 2:
    set_module_args(dict(gather_subset='!all'))