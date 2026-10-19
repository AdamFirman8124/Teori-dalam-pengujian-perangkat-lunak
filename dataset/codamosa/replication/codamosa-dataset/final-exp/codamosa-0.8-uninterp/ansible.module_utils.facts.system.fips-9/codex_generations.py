

# Generated at 2022-06-13 02:51:16.324292
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    assert fips_collector.collect()['fips'] is True

# Generated at 2022-06-13 02:51:17.375117
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert FipsFactCollector().collect() == {'fips': True}

# Generated at 2022-06-13 02:51:20.051997
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    test_data = b'1'
    f = FipsFactCollector()
    result = f.collect({}, {})
    assert result == {'fips':True}

# Generated at 2022-06-13 02:51:21.926024
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    content = "0\n"
    f = FipsFactCollector()
    result = f.collect(collected_facts=None)
    assert result == {'fips': False}

# Generated at 2022-06-13 02:51:23.708096
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_obj = FipsFactCollector()
    fips_data = fips_obj.collect()
    assert 'fips' in fips_data
    assert type(fips_data['fips']) == bool

# Generated at 2022-06-13 02:51:25.671386
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Arrange
    FakeFipsFactCollector = FipsFactCollector()

    # Act
    data = FakeFipsFactCollector.collect()

    # Assert
    assert 'fips' in data

# Generated at 2022-06-13 02:51:27.531132
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    obj = FipsFactCollector()
    result = obj.collect()
    assert result['fips'] == True

# Generated at 2022-06-13 02:51:38.042098
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = mock.MagicMock()
    collected_facts = mock.MagicMock()

    fips_collector = FipsFactCollector()
    facts = fips_collector.collect(module, collected_facts)
    assert facts == {'fips': False}

    fips_collector.file_exists = lambda file_name: True
    fips_collector.get_file_content = lambda file_name: False
    facts = fips_collector.collect(module, collected_facts)
    assert facts == {'fips': False}

    fips_collector.get_file_content = lambda file_name: '2'
    facts = fips_collector.collect(module, collected_facts)
    assert facts == {'fips': False}

    fips_collector.get_file_content

# Generated at 2022-06-13 02:51:39.435601
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_Collect = FipsFactCollector()
    FipsFactCollector_Collect.collect()

# Generated at 2022-06-13 02:51:43.220627
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    facts = {
        'fips': False,
    }
    FipsFactCollector().collect(facts)
    assert facts == {'fips': False}

# Generated at 2022-06-13 02:51:48.085953
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    facts = fips.collect()
    assert facts['fips'] == False


# Generated at 2022-06-13 02:51:50.117504
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    mock_module = MagicMock()
    fips_fact_collector = FipsFactCollector(mock_module)
    assert fips_fact_collector.collect() == {'fips': False}

# Generated at 2022-06-13 02:51:58.020932
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_test = FipsFactCollector()
    collected_facts = {}
    collected_facts['fips'] = False

    # Test fips_enabled is 1
    fips_test._module.get_file_content = lambda path: '1'
    fips_test.collect(collected_facts=collected_facts)
    assert collected_facts['fips'] is True

    # Test fips_enabled is 0
    fips_test._module.get_file_content = lambda path: '0'
    fips_test.collect(collected_facts=collected_facts)
    assert collected_facts['fips'] is False

    # Test fips_enabled does not exist
    fips_test._module.get_file_content = lambda path: None

# Generated at 2022-06-13 02:51:59.872927
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector = FipsFactCollector()
    FipsFactCollector.collect()
    FipsFactCollector.salts

# Generated at 2022-06-13 02:52:03.161117
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    json_str = '{"fips": false}'
    _FipsFactCollector = FipsFactCollector()
    _FipsFactCollector.collect()
    assert json_str == _FipsFactCollector.get_facts()

# Generated at 2022-06-13 02:52:10.730571
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    with open('/proc/sys/crypto/fips_enabled', 'w+') as fips:
        fips.write('0\n')
    fips_facts = FipsFactCollector().collect()
    assert fips_facts['fips'] == False
    with open('/proc/sys/crypto/fips_enabled', 'w+') as fips:
        fips.write('1\n')
    fips_facts = FipsFactCollector().collect()
    assert fips_facts['fips'] == True

# Generated at 2022-06-13 02:52:12.585754
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    ffc = FipsFactCollector()
    assert ffc.collect() == {'fips': True}

# Generated at 2022-06-13 02:52:15.472190
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert FipsFactCollector().collect() == {'fips': False}
    with open('/proc/sys/crypto/fips_enabled', 'w') as file:
        file.write('1')
    assert FipsFactCollector().collect() == {'fips': True}

# Generated at 2022-06-13 02:52:20.415086
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Unit test for method collect of class FipsFactCollector"""
    fips_collector = FipsFactCollector()

# Generated at 2022-06-13 02:52:30.855095
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.facts.utils import Facts
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import FipsFactCollector

    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all', 'min'], type='list'),
            'gather_timeout': dict(default=10, type='int')
        },
        supports_check_mode=True
    )
    if module._name == 'setup':
        module.exit_json(ansible_facts=Facts(dict()).serialize())

    facts_dict = dict()
    collector = Collector()
    fips_fact_collector = FipsFactCollector(module=module)

# Generated at 2022-06-13 02:52:42.420558
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    file_mock = {
        '/proc/sys/crypto/fips_enabled': '1',
    }

    mock_get_file_content = lambda x: file_mock.get(x, '')
    fips_fact = FipsFactCollector()
    fips_fact.get_file_content = mock_get_file_content
    assert fips_fact.collect() == {'fips': True}

# vim: set et ts=4 sw=4 sts=4

# Generated at 2022-06-13 02:52:46.073665
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Unit test for method collect of class FipsFactCollector."""
    fips_fact_collector = FipsFactCollector()
    assert fips_fact_collector.collect() == {'fips': False}

# Generated at 2022-06-13 02:52:49.519214
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    assert fips.collect() == {'fips': False}
    assert fips.collect(collected_facts={}) == {'fips': False}
    assert fips.collect(collected_facts={'fips': True}) == {'fips': True}

# Generated at 2022-06-13 02:52:51.831148
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    ff = FipsFactCollector()
    result = ff.collect()
    assert result
    assert 'fips' in result
    assert result['fips'] is False

# Generated at 2022-06-13 02:52:53.887253
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    collected_facts = None
    fips_facts = FipsFactCollector().collect(module, collected_facts)
    assert 'fips' in fips_facts.keys()

# Generated at 2022-06-13 02:53:04.592623
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """
    Unit test for the method FipsFactCollector.collect of the
    class FipsFactCollector.
    """

    # Patch method get_file_content() to return the
    # correct value when the path /proc/sys/crypto/fips_enabled
    # is given as argument.
    def mock_get_file_content(file_path):
        if file_path == "/proc/sys/crypto/fips_enabled":
            return "1"
        return None
    get_file_content_org = FipsFactCollector.get_file_content
    FipsFactCollector.get_file_content = mock_get_file_content

    # Create a new instance of the FipsFactCollector class.
    fips_fact_collector = FipsFactCollector()

    # Collect the facts.


# Generated at 2022-06-13 02:53:06.494352
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_collector = FipsFactCollector()
    result = fips_collector.collect()
    assert result['fips'] == False

# Generated at 2022-06-13 02:53:08.285549
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector().collect()
    assert isinstance(fips_facts, dict)
    assert fips_facts['fips']

# Generated at 2022-06-13 02:53:10.379461
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    ffc = FipsFactCollector()
    try:
        ffc.collect()
    except Exception:
        assert False
    else:
        assert True


# Generated at 2022-06-13 02:53:13.578299
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_factcollector = FipsFactCollector()
    data = get_file_content('/proc/sys/crypto/fips_enabled')
    assert fips_factcollector.collect()['fips'] == data

# Generated at 2022-06-13 02:53:39.052252
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    mock_module = MagicMock()
    mock_collected_facts = {}

    # Mock the file content with '0'
    fips_data_zero = get_file_content('/proc/sys/crypto/fips_enabled')
    mock_content = MagicMock()
    mock_content.return_value = fips_data_zero
    mocked_get_file_content = patch.object(FipsFactCollector, 'get_file_content', mock_content)
    mocked_get_file_content.start()
    fips_result = FipsFactCollector().collect(mock_module, mock_collected_facts)
    assert fips_result['fips'] == False
    mocked_get_file_content.stop()

    # Mock the file content with '1'

# Generated at 2022-06-13 02:53:45.875282
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collectors.fips import FipsFactCollector

    def get_file_content(path):
        if path == '/proc/sys/crypto/fips_enabled':
            return True
        else:
            return False

    FipsFactCollector.collect()
    assert FipsFactCollector.collect() == {'fips': True}

# Generated at 2022-06-13 02:53:46.880874
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector().collect()

# Generated at 2022-06-13 02:53:50.440563
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_obj = FipsFactCollector()
    collected_facts = set()
    fips_obj.collect(collected_facts=collected_facts)
    assert len(collected_facts) == 1

# Generated at 2022-06-13 02:53:56.104048
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector_obj = FipsFactCollector()
    fips_facts = {'fips': False}
    data = '1'
    assert FipsFactCollector_obj.collect(collected_facts=None)['fips'] == fips_facts['fips']
    assert FipsFactCollector_obj.collect(collected_facts=None) != fips_facts['fips']

# Generated at 2022-06-13 02:53:57.065922
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    FipsFactCollector.collect()

# Generated at 2022-06-13 02:54:03.560855
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import pytest
    import os
    # 1. Create temporary test file
    with open('/tmp/fips_enabled.test', 'w') as fd:
        fd.write("1")
    # 2. Create object
    my_obj = FipsFactCollector()
    # 3. Test the method with temporary test file
    new_facts = my_obj.collect(collected_facts=None)
    # 4. Remove test file
    if os.path.exists('/tmp/fips_enabled.test'):
        os.remove('/tmp/fips_enabled.test')
    assert new_facts['fips'] == True

# Generated at 2022-06-13 02:54:08.618465
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    """Test successful return for FipsFactCollector.collect()"""

    # pylint: disable=protected-access
    fips_fact = FipsFactCollector()
    fips_facts = {}
    fips_facts['fips'] = False
    assert(fips_fact.collect(collected_facts=fips_facts) == fips_facts)
    return

# Generated at 2022-06-13 02:54:12.558755
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Note: File /proc/sys/crypto/fips_enabled is not on the BSDs
    # and is present on some, but not all, Linux distributions.
    fips = FipsFactCollector()
    fips_facts = fips.collect()
    assert 'fips' in fips_facts
    assert isinstance(fips_facts['fips'], type(False))

# Generated at 2022-06-13 02:54:15.054404
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    result = FipsFactCollector().collect()
    assert result['fips'] == False

# Generated at 2022-06-13 02:54:44.674307
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = FipsFactCollector()
    assert fips_facts.collect() == {'fips': False}

# Generated at 2022-06-13 02:54:53.787078
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    with patch('ansible.module_utils.facts.utils.get_file_content',
               return_value='1') as get_file_content_mock:
        fact_collector = FipsFactCollector()
        fips_facts = fact_collector.collect()
        assert fips_facts == {'fips': True}
    with patch('ansible.module_utils.facts.utils.get_file_content',
               return_value='0') as get_file_content_mock:
        fact_collector = FipsFactCollector()
        fips_facts = fact_collector.collect()
        assert fips_facts == {'fips': False}

# Generated at 2022-06-13 02:54:55.442588
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    data = collector.collect()
    assert data['fips'] is False

# Generated at 2022-06-13 02:55:01.029237
# Unit test for method collect of class FipsFactCollector

# Generated at 2022-06-13 02:55:03.987770
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts = {}
    fips_facts['fips'] = False
    facts = {}
    collector = FipsFactCollector(module=None, collected_facts=facts)
    result = collector.collect()
    assert result == fips_facts

# Generated at 2022-06-13 02:55:04.866858
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fc = FipsFactCollector()
    fips_fc.collect()

# Generated at 2022-06-13 02:55:08.016802
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Test when /proc/sys/crypto/fips_enabled gives value 1
    data = '1'
    fips = FipsFactCollector()
    result = fips.collect(collected_facts=data)
    assert result == {'fips': True}
    data = '0'
    fips = FipsFactCollector()
    result = fips.collect(collected_facts=data)
    # Test when /proc/sys/crypto/fips_enabled gives value 0
    assert result == {'fips': False}

# Generated at 2022-06-13 02:55:10.087032
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    fact = fips.collect()
    assert fact == { "fips": False }

# Generated at 2022-06-13 02:55:18.474459
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import pytest
    import tempfile

    def _get_module():
        module = pytest.Mock()
        # attr:_name = 'ansible_fips'
        module.configure_mock(**{'params.get.return_value': None})
        return module

    # create temporary file to simulate /proc/sys/crypto/fips_enabled
    #
    # NOTE: mock.mock_open() does not support writing.
    fd, fname = tempfile.mkstemp()
    with open(fname, 'w') as fh:
        fh.write('1')

    def _get_collector():
        return FipsFactCollector(_get_module())

    # Verify fips is True
    fips_collector = _get_collector()
    assert fips_

# Generated at 2022-06-13 02:55:21.139939
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect()
    assert fips_facts['fips'] == False

# Generated at 2022-06-13 02:56:28.974368
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_fact_collector = FipsFactCollector()
    fips_facts = fips_fact_collector.collect()
    # Test if dict returned by collect has key 'fips'
    assert 'fips' in fips_facts

# Generated at 2022-06-13 02:56:31.183324
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips_facts_collector = FipsFactCollector()
    fips_facts = fips_facts_collector.collect()
    assert fips_facts == {'fips': False}

# Generated at 2022-06-13 02:56:33.772501
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import FipsFactCollector
    test_collector = Collector()
    test_collector.add_collector(FipsFactCollector())
    assert test_collector.collect() != {}

# Generated at 2022-06-13 02:56:35.833651
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fact = FipsFactCollector()
    assert fact.collect()['fips'] == False
    fact.collect()
    assert isinstance(fact.collect(),dict)

# Generated at 2022-06-13 02:56:39.070595
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fips = FipsFactCollector()
    assert fips.collect().get('fips', False) == False



# Generated at 2022-06-13 02:56:45.209787
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    mock_module = Mock()
    mock_collected_facts = {'has_fips':False}
    with patch('ansible.module_utils.facts.collectors.fips.open', mock_open(read_data='1')):
        fact_collector = FipsFactCollector()
        fact_collector.collect(mock_module, mock_collected_facts)
        assert mock_collected_facts.get('has_fips',None) is True


# Generated at 2022-06-13 02:56:47.223889
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    test_obj = FipsFactCollector()
    ret = test_obj.collect()
    assert isinstance(ret, dict)
    assert ret == {'fips': False}

# Generated at 2022-06-13 02:56:49.219846
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    assert collector.collect() == {'fips': False}

# Generated at 2022-06-13 02:56:53.924436
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import Collector

    FipsFactCollector.collect = Collector.collect
    fips_fact_collector = FipsFactCollector()
    fips_facts = {'fips': True}
    assert fips_fact_collector.collect() == fips_facts

# Generated at 2022-06-13 02:57:00.620046
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    from ansible.module_utils.facts.collectors import collector_module
    from ansible.module_utils.facts.utils import get_file_content

    def mock_get_file_content(path):
        return b'0\n'

    collector = collector_module.get_collector('FipsFactCollector')
    get_file_content_mock = get_file_content
    try:
        get_file_content = mock_get_file_content
        collector_result = collector.collect(collected_facts={})
        assert collector_result == {'fips': False}
    finally:
        get_file_content = get_file_content_mock


# Generated at 2022-06-13 02:59:45.759561
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    '''
    Verify correct fips result for:
    1. fips not enabled
    2.2 fips enabled
    '''
    class mock_module:
        params = {}
    class mock_os:
        def __init__(self, data):
            self.data = data
        def read(self):
            return self.data

    def mock_open(*args, **kwargs):
        ''' Return a mock object
        '''
        return mock_os(data)

    # 1. fips not enabled
    data = '0'
    mock_modul

# Generated at 2022-06-13 02:59:48.219284
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # Create instance of FipsFactCollector
    fips_fact_collector = FipsFactCollector()
    # Verify if collect returns a dictionary
    assert isinstance(fips_fact_collector.collect(), dict)

# Generated at 2022-06-13 02:59:49.911815
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fipsFactCollector = FipsFactCollector()
    fips_facts = fipsFactCollector.collect()
    assert 'fips' in fips_facts

# Generated at 2022-06-13 02:59:51.093216
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    fc = FipsFactCollector()
    fips_facts = fc.collect()
    assert fips_facts == {'fips': False}

# Generated at 2022-06-13 02:59:53.734949
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    assert FipsFactCollector.collect() == { 'fips': False }

# Generated at 2022-06-13 02:59:55.097275
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    collector = FipsFactCollector()
    collected_facts = collector.collect()
    assert collected_facts['fips']

# Generated at 2022-06-13 02:59:59.540417
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    def test_file_exists(path):
        file_contents = {'/proc/sys/crypto/fips_enabled': '1'}
        return file_contents.get(path, None)
    FipsFactCollector.get_file_content = test_file_exists
    fips_facts = FipsFactCollector()
    result = fips_facts.collect()
    assert result['fips'] is True

# Generated at 2022-06-13 03:00:01.461358
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    module = None
    collected_facts = None
    fips_fc = FipsFactCollector()
    fips_fc.collect(module, collected_facts)

# Generated at 2022-06-13 03:00:02.176041
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    pass
    #TODO

# Generated at 2022-06-13 03:00:08.737534
# Unit test for method collect of class FipsFactCollector
def test_FipsFactCollector_collect():
    # create a mock file that contains fips_enabled=1
    file_content = '1'
    data = get_file_content.when.called_with('/proc/sys/crypto/fips_enabled').should.return_value(file_content)
    instance = FipsFactCollector()
    facts = instance.collect()
    assert facts['fips']
    data = get_file_content.when.called_with('/proc/sys/crypto/fips_enabled').should.return_value('')
    instance = FipsFactCollector()
    facts = instance.collect()
    assert not facts['fips']