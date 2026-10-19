

# Generated at 2022-06-13 02:40:45.473540
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Make sure that we can collect the facts
    """
    dtfc = DateTimeFactCollector()
    facts = dtfc.collect()
    assert facts['date_time']['epoch']

# Generated at 2022-06-13 02:40:53.821433
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector

    temp_fact_collector = FactCollector()
    temp_fact_collector.collectors = [DateTimeFactCollector()]

    assert not temp_fact_collector.get_facts()['date_time'].has_key('epoch')
    assert int(temp_fact_collector.get_facts()['date_time']['epoch_int']) > 0


DateTimeCollector = DateTimeFactCollector  # used in Ansible 2.5+

# Generated at 2022-06-13 02:41:01.372341
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Arrange
    # Act
    dtfc = DateTimeFactCollector()

    # Act
    result = dtfc.collect()
    assert result is not None
    assert result.get('date_time') is not None

    s = result.get('date_time')
    assert s.get('year') != ''
    assert s.get('month') != ''
    assert s.get('weekday') != ''
    assert s.get('weekday_number') != ''
    assert s.get('weeknumber') != ''
    assert s.get('day') != ''
    assert s.get('hour') != ''
    assert s.get('minute') != ''
    assert s.get('second') != ''
    assert s.get('epoch') != ''
    assert s.get('epoch_int') != ''
   

# Generated at 2022-06-13 02:41:11.580473
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_factory = DateTimeFactCollector()
    all_date_time_facts = date_time_factory.collect()
    current_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    assert all_date_time_facts['date_time']['iso8601'] == current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert all_date_time_facts['date_time']['iso8601_micro'] == current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# Generated at 2022-06-13 02:41:21.589635
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:41:25.130208
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create an instance of DateTimeFactCollector
    d = DateTimeFactCollector()
    # Call method collect of DateTimeFactCollector
    a = d.collect()
    # Test results
    assert (type(a) is dict)
#     assert (len(a['date_time']) > 0)

# Generated at 2022-06-13 02:41:34.189363
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact = DateTimeFactCollector()

    date_time = fact.collect()

    assert date_time['date_time']['epoch_int']
    assert date_time['date_time']['epoch']
    assert date_time['date_time']['year']
    assert date_time['date_time']['month']
    assert date_time['date_time']['weekday']
    assert date_time['date_time']['weekday_number']
    assert date_time['date_time']['weeknumber']
    assert date_time['date_time']['day']
    assert date_time['date_time']['hour']
    assert date_time['date_time']['minute']
    assert date_time['date_time']['second']
    assert date_time

# Generated at 2022-06-13 02:41:43.972867
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    collected_facts = collector.collect()
    # If we have collected local time-related facts and their values are not
    # empty, then the unit test collects these facts successfully
    assert 'date_time' in collected_facts
    # The following list contains all time-related facts that will be collected
    # in the function collect
    date_time_facts = ['year', 'month', 'weekday', 'weekday_number',
                       'weeknumber', 'day', 'hour', 'minute', 'second',
                       'epoch', 'epoch_int', 'date', 'time', 'iso8601_micro',
                       'iso8601', 'iso8601_basic', 'iso8601_basic_short', 'tz',
                       'tz_dst', 'tz_offset']

# Generated at 2022-06-13 02:41:48.459341
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Arrange
    module = None
    collected_facts = None

    #
    expected = {
        'date_time': {
        }
    }

    # Act
    dtf =  DateTimeFactCollector()
    actual = dtf.collect(module, collected_facts)

    # Assert
    assert actual == expected

# Generated at 2022-06-13 02:41:56.818885
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    d = DateTimeFactCollector()
    mytime = d.collect()
    # Assign the first digit of epoch to test whether epoch returns integer
    epoch_digit_test = mytime['date_time']['epoch'][0]
    # Assign the first digit of epoch to test whether epoch returns integer
    epoch_int_digit_test = mytime['date_time']['epoch_int'][0]
    assert epoch_digit_test == '1' or epoch_digit_test == '2' or epoch_digit_test == '3' or epoch_digit_test == '4' or epoch_digit_test == '5' or epoch_digit_test == '6' or epoch_digit_test == '7' or epoch_digit_test == '8' or epoch_digit_test == '9'
    assert epoch_int_

# Generated at 2022-06-13 02:42:01.815080
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    datetime_facts_dict = date_time_fact_collector.collect()
    assert datetime_facts_dict is not None
    assert 'date_time' in datetime_facts_dict
    assert 'day' in datetime_facts_dict['date_time']

# Generated at 2022-06-13 02:42:12.636893
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()
    assert date_time_facts['date_time']['year'] == datetime.datetime.now().strftime('%Y')
    assert date_time_facts['date_time']['month'] == datetime.datetime.now().strftime('%m')
    assert date_time_facts['date_time']['weekday'] == datetime.datetime.now().strftime('%A')
    assert date_time_facts['date_time']['weekday_number'] == datetime.datetime.now().strftime('%w')
    assert date_time_facts['date_time']['weeknumber'] == datetime.datetime.now().strftime('%W')
    assert date_time_facts['date_time']['day'] == dat

# Generated at 2022-06-13 02:42:26.558601
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import os
    import ansible.module_utils.facts.collector

    # Create instance of class DateTimeFactCollector
    test_fact_collector = DateTimeFactCollector()

    # Get every possible fact from DateTimeFactCollector 
    AnsibleModule = ansible.module_utils.facts.collector.get_ansible_module_mock()
    collected_facts = test_fact_collector.collect(AnsibleModule, collected_facts={})

    # Assert the epoch fact is not blank
    assert collected_facts['date_time']['epoch'] is not None
    assert collected_facts['date_time']['epoch'] is not ''

    # Assert the epoch fact is not blank
    assert collected_facts['date_time']['epoch_int'] is not None

# Generated at 2022-06-13 02:42:32.854835
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # get the result of DateTimeFactCollector.collect
    result = DateTimeFactCollector().collect()

    # assert that required keys are in result
    assert 'ansible_date_time' in result
    assert 'date_time' in result

    # assert that values under 'date_time' key are not empty
    for value in result['date_time'].values():
        assert len(value) > 0

# Generated at 2022-06-13 02:42:36.768458
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()
    assert isinstance(date_time_facts, dict)
    keys = ['date_time']
    for key in keys:
        assert key in date_time_facts

# Generated at 2022-06-13 02:42:45.053153
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Test method collect of class DateTimeFactCollector
    """
    dt_fact_collector = DateTimeFactCollector()
    res = dt_fact_collector.collect()
    assert res['date_time']['iso8601_basic'].startswith('201')
    assert res['date_time']['iso8601'].startswith('201')
    assert res['date_time']['year'].startswith('201')
    assert res['date_time']['iso8601_micro'].startswith('201')
    assert res['date_time']['iso8601_basic_short'].startswith('201')

# Generated at 2022-06-13 02:42:49.186263
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """date_time.collect"""
    c = DateTimeFactCollector()
    d = c.collect()
    assert isinstance(d,dict)
    assert 'date_time' in d
    assert isinstance(d['date_time'],dict)


# Generated at 2022-06-13 02:42:50.423728
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:42:59.580878
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Test if the DateTimeFactCollector.collect method returns datetime.datetime objects."""
    fact_collector = DateTimeFactCollector()
    # collect() returns a dictionary with the key 'date_time'
    result = fact_collector.collect()
    assert isinstance(result['date_time']['year'], str)
    assert isinstance(result['date_time']['month'], str)
    assert isinstance(result['date_time']['weekday'], str)
    assert isinstance(result['date_time']['weekday_number'], str)
    assert isinstance(result['date_time']['weeknumber'], str)
    assert isinstance(result['date_time']['day'], str)

# Generated at 2022-06-13 02:43:04.952733
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    result = date_time_fact_collector.collect()
    assert result['date_time'] is not None
    assert type(result['date_time']) is dict
    assert result['date_time']['epoch_int'] is not None
    assert type(result['date_time']['epoch_int']) is str

    epoch_now = int(time.time())
    assert int(result['date_time']['epoch_int']) - epoch_now < 5

# Generated at 2022-06-13 02:43:13.906594
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    FactCollector = FactsCollector("DateTimeFactCollector", {}, [], [])
    fact = FactCollector.collect()['ansible_date_time']
    # List of keys to check if the content of them is int
    ints = [
        'weekday_number',
        'weeknumber',
        'epoch_int',
        'day',
        'hour',
        'minute',
        'second',
    ]
    # List of keys to check if the content of them is str

# Generated at 2022-06-13 02:43:24.641304
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test empty facts data
    test_date_time_collector = DateTimeFactCollector()
    facts_dict = {}
    collected_facts = {}
    empty_answer = test_date_time_collector.collect(None, collected_facts)
    # Check if empty facts data is returned
    assert(empty_answer == facts_dict)

    # Test not empty facts data (can't set facts data directly, as facts are read only)
    # Do a collect() on date_time, which updates date_time facts, then test the date_time facts
    test_date_time_collector = DateTimeFactCollector()
    collected_facts = {}
    test_date_time_collector.collect(None, collected_facts)
    test_date_time_data = collected_facts['date_time']

# Generated at 2022-06-13 02:43:26.921572
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    tsf = DateTimeFactCollector()
    results = tsf.collect()
    assert results['date_time']['epoch_int'].isdigit()
    assert results['date_time']['epoch'].isdigit()

# Generated at 2022-06-13 02:43:28.716664
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    assert isinstance(DateTimeFactCollector().collect(), dict)

# Generated at 2022-06-13 02:43:39.280279
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:43:46.445515
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
        import ansible.module_utils.facts.collectors.date_time as date_time_collector

        print('Testing collect of DateTimeFactCollector')
        collector = date_time_collector.DateTimeFactCollector()
        result = collector.collect()
        assert result['date_time']['year'] == str(datetime.datetime.now().year)

# Generated at 2022-06-13 02:43:56.168912
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts_dict = {}
    date_time_facts = {}

    # Store the timestamp once, then get local and UTC versions from that
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
    date_time_facts['weekday_number'] = now.strftime('%w')
    date_time_facts['weeknumber'] = now.strftime('%W')

# Generated at 2022-06-13 02:44:07.237877
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Initialize an instance of DateTimeFactCollector
    datetime_facts_collector = DateTimeFactCollector()

    # call method collect of DateTimeFactCollector instance
    datetime_facts = datetime_facts_collector.collect()

    # Assert values of facts
    assert datetime_facts is not None
    assert 'date_time' in datetime_facts
    assert 'year' in datetime_facts['date_time']
    assert 'month' in datetime_facts['date_time']
    assert 'weekday' in datetime_facts['date_time']
    assert 'weekday_number' in datetime_facts['date_time']
    assert 'weeknumber' in datetime_facts['date_time']
    assert 'day' in datetime_facts['date_time']
    assert 'hour' in datetime

# Generated at 2022-06-13 02:44:10.466008
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    C = DateTimeFactCollector()
    result_dict = C.collect()
    assert result_dict

# Unit test:
#   - AnsibleModule arguments definitions
#   - AnsibleModule instantiation
#   - ModuleParameters instantiation
#   - ModuleManagerList instantiation
#   - ModuleManager instantiation
#   - ModuleManager run method

# Generated at 2022-06-13 02:44:15.005819
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Run method collect of class DateTimeFactCollector
    result = DateTimeFactCollector.collect()

    # Check result
    assert isinstance(result, dict) and result['date_time']['tz'] == time.strftime("%Z")

# Generated at 2022-06-13 02:44:31.364372
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    time_now = datetime.datetime.now()
    time_str = (str(time_now.year) + '-' +
                str(time_now.month) + '-' +
                str(time_now.day) + 'T' +
                str(time_now.hour) + ':' +
                str(time_now.minute) + ':' +
                str(time_now.second) + '.' +
                str(time_now.microsecond) + 'Z')

# Generated at 2022-06-13 02:44:41.465482
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    current_module_value = AnsibleModule.module_utils.facts.collector.module
    AnsibleModule.module_utils.facts.collector.module = {}

    date_time_fact_collector = DateTimeFactCollector()
    results = date_time_fact_collector.collect()
    assert results['date_time']['year']
    assert results['date_time']['month']
    assert results['date_time']['weekday']
    assert results['date_time']['weekday_number']
    assert results['date_time']['weeknumber']
    assert results['date_time']['day']
    assert results['date_time']['hour']
    assert results['date_time']['minute']
    assert results['date_time']['second']

# Generated at 2022-06-13 02:44:51.976578
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector(None)
    dt_facts = dtf.collect()
    import time, datetime

    date_time_facts = dt_facts['date_time']
    now = datetime.datetime.fromtimestamp(time.time())
    utcnow = datetime.datetime.utcfromtimestamp(time.time())
    now_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')
    utcnow_str = utcnow.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    epoch_str = now.strftime('%s')
    tz_str = time.strftime('%Z')
    offset

# Generated at 2022-06-13 02:44:57.464360
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Validates if the 'date_time' key is present in ansible_facts
    """
    from ansible.module_utils.facts import FactCollector

    dtfc = DateTimeFactCollector()
    assert 'date_time' in dtfc.collect()['ansible_facts']

# Generated at 2022-06-13 02:45:04.070411
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    col = DateTimeFactCollector()
    col_facts = col.collect()
    assert 'date_time' in col_facts.keys()
    date_time_facts = col_facts['date_time']
    assert isinstance(date_time_facts, dict)
    assert 'year' in date_time_facts.keys()
    assert isinstance(date_time_facts['year'], str)
    assert 'month' in date_time_facts.keys()
    assert isinstance(date_time_facts['month'], str)
    assert 'weekday' in date_time_facts.keys()
    assert isinstance(date_time_facts['weekday'], str)
    assert 'weekday_number' in date_time_facts.keys()

# Generated at 2022-06-13 02:45:07.168608
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Returns the right date time facts"""
    date_time_facts = DateTimeFactCollector().collect()
    assert date_time_facts['date_time']['iso8601']
    assert date_time_facts['date_time']['tz']

# Generated at 2022-06-13 02:45:13.367211
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts_module = DateTimeFactCollector()
    result = facts_module.collect()
    assert 'date_time' in result
    assert 'epoch' in result['date_time']
    assert 'epoch_int' in result['date_time']
    assert 'iso8601_micro' in result['date_time']
    assert 'iso8601' in result['date_time']
    assert 'iso8601_basic' in result['date_time']
    assert 'iso8601_basic_short' in result['date_time']
    assert 'tz_dst' in result['date_time']

# Generated at 2022-06-13 02:45:23.675433
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    # Wording note: date_time_facts are the structure collected by the method collect of class DateTimeFactCollector, not the returned structure
    # of the method collect of class DateTimeFactCollector
    date_time_facts = dtfc.collect()['date_time']
    # Test structure
    assert isinstance(date_time_facts, dict)
    assert isinstance(date_time_facts['date'], basestring)
    assert isinstance(date_time_facts['day'], basestring)
    assert isinstance(date_time_facts['epoch'], basestring)
    assert isinstance(date_time_facts['epoch_int'], basestring)
    assert isinstance(date_time_facts['hour'], basestring)
    assert isinstance

# Generated at 2022-06-13 02:45:29.885953
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create DateTimeFactCollector instance
    dt_fc = DateTimeFactCollector()
    
    # Call method collect on instance dt_fc
    dt_fc.collect()
    
    # Check that it returns at least the keys in dt_fc._fact_ids (the keys are
    # date_time and date_time_utc)
    assert set(dt_fc._fact_ids).issubset(dt_fc.collect().keys())

# Generated at 2022-06-13 02:45:36.949077
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Init DateTimeFactCollector obj
    dt_collector = DateTimeFactCollector()

    # Get current time by time.time()
    now_time = time.time()

    # Get current time by datetime.datetime.fromtimestamp
    now = datetime.datetime.fromtimestamp(now_time)

    # Get current utc time by datetime.datetime.utcfromtimestamp
    utcnow = datetime.datetime.utcfromtimestamp(now_time)

    # Init date_time_facts dict
    date_time_facts = {}

    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
   

# Generated at 2022-06-13 02:45:52.749586
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:45:57.214850
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    d = DateTimeFactCollector()
    dt_facts = d.collect()
    assert dt_facts['date_time']['tz'] == time.strftime('%Z')
    assert dt_facts['date_time']['tz_dst'] == time.tzname[1]

# Generated at 2022-06-13 02:46:01.111396
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    datetime_fc = DateTimeFactCollector()
    datetime_fc.collect()
    collected_facts = datetime_fc.collect()

    assert collected_facts['date_time']['year'][0:4] == '2017'
    assert collected_facts['date_time']['month'][0:2] == '11'
    assert collected_facts['date_time']['weekday'][0:3] == 'Tue'
    assert collected_facts['date_time']['weekday_number'][0:1] == '2'
    assert collected_facts['date_time']['weeknumber'][0:2] == '45'
    assert collected_facts['date_time']['day'][0:2] == '14'

# Generated at 2022-06-13 02:46:10.992929
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    c = DateTimeFactCollector()
    r = c.collect()
    assert 'date_time' in r
    assert 'iso8601' in r['date_time']
    assert 'tz_dst' in r['date_time']
    assert 'day' in r['date_time']
    assert 'year' in r['date_time']
    assert 'weekday_number' in r['date_time']
    assert 'tz_offset' in r['date_time']
    assert 'time' in r['date_time']
    assert 'tz' in r['date_time']
    assert 'weeknumber' in r['date_time']
    assert 'epoch_int' in r['date_time']
    assert 'epoch' in r['date_time']
    assert 'month' in r['date_time']


# Generated at 2022-06-13 02:46:15.188715
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector._module = None
    date_time_fact_collector._collected_facts = None

    result = date_time_fact_collector.collect()

    assert result['date_time']['year'] != ''
    assert result['date_time']['month'] != ''
    assert result['date_time']['weekday'] != ''
    assert result['date_time']['weekday_number'] != ''
    assert result['date_time']['weeknumber'] != ''
    assert result['date_time']['day'] != ''
    assert result['date_time']['hour'] != ''
    assert result['date_time']['minute'] != ''

# Generated at 2022-06-13 02:46:25.486250
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fc = DateTimeFactCollector()
    facts_dict = fc.collect()

# Generated at 2022-06-13 02:46:31.068284
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fake_module = object()
    fake_collected_facts = object()
    dtfc = DateTimeFactCollector()
    dtf_dict = dtfc.collect(fake_module, fake_collected_facts)
    try:
        assert(dtf_dict['date_time'] is not None)
    except AssertionError:
        raise

# Generated at 2022-06-13 02:46:39.907732
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()
    assert 'date_time' in date_time_facts
    assert 'year' in date_time_facts['date_time']
    assert 'month' in date_time_facts['date_time']
    assert 'date' in date_time_facts['date_time']
    assert 'weekday' in date_time_facts['date_time']
    assert 'weekday_number' in date_time_facts['date_time']
    assert 'weeknumber' in date_time_facts['date_time']
    assert 'day' in date_time_facts['date_time']
    assert 'time' in date_time_facts['date_time']
    assert 'hour' in date_time_facts['date_time']
    assert 'minute' in date_time_facts

# Generated at 2022-06-13 02:46:43.611125
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    assert dtfc.name == 'date_time'
    assert dtfc.collect()['date_time']

# Generated at 2022-06-13 02:46:51.733195
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create data structure to pass to method
    collected_facts = {}
    expected_output = {}
    date_time_facts = {}

    # Store the timestamp once, then get local and UTC versions from that
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
    date_time_facts['weekday_number'] = now.strftime('%w')

# Generated at 2022-06-13 02:47:26.081612
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector.collect()

# Generated at 2022-06-13 02:47:37.714235
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    res = dtfc.collect()
    assert 'date_time' in res
    assert 'epoch_int' in res['date_time']
    assert 'epoch' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res['date_time']
    assert 'time' in res

# Generated at 2022-06-13 02:47:47.616910
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Generator for unit testing method DateTimeFactCollector.collect
    """
    d = DateTimeFactCollector()
    d_result = d.collect()

# Generated at 2022-06-13 02:47:54.977477
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_collector = DateTimeFactCollector()

    assert 'date_time' in dt_collector.collect()
    assert 'date' in dt_collector.collect()['date_time']
    assert 'date' in dt_collector.collect(collected_facts={})['date_time']
    assert 'date' in dt_collector.collect(collected_facts={}, module={})['date_time']
    assert 'date' in dt_collector.collect(module={})['date_time']

# Generated at 2022-06-13 02:48:03.799073
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import pytest
    import datetime

    # Create an instance of the DateTimeFactCollector class
    DateTimeFactCollector_instance = DateTimeFactCollector()

    # Read in the current time from the system
    now = datetime.datetime.now()

    # Get the current time from the collect method
    # of the DateTimeFactCollector class
    DateTimeFactCollector_current_time = DateTimeFactCollector_instance.collect()['date_time']

    # Test if the current time created by the
    # collect method of the DateTimeFactCollector class
    # is equal to the current time now

# Generated at 2022-06-13 02:48:06.615274
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    result = date_time_fact_collector.collect()
    assert result['date_time'].get('epoch') == str(int(time.time()))

# Generated at 2022-06-13 02:48:16.443373
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dc = DateTimeFactCollector()
    facts = dc.collect()
    for fact in facts:
        assert fact in ['date_time']
        for item in facts[fact]:
            assert item in ['date', 'day', 'epoch', 'epoch_int', 'hour', 'iso8601', 'iso8601_basic', 'iso8601_basic_short', 'iso8601_micro', 'minute', 'month', 'second', 'time', 'tz', 'tz_dst', 'tz_offset', 'weekday', 'weekday_number', 'weeknumber', 'year']

# Generated at 2022-06-13 02:48:27.540881
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dc = DateTimeFactCollector()
    date_time_obj = dc.collect()
    assert date_time_obj.get('date_time')
    dt = date_time_obj.get('date_time')
    assert dt.get('year') != ""
    assert dt.get('month') != ""
    assert dt.get('weekday') != ""
    assert dt.get('weekday_number') != ""
    assert dt.get('weeknumber') != ""
    assert dt.get('day') != ""
    assert dt.get('hour') != ""
    assert dt.get('minute') != ""
    assert dt.get('second') != ""
    assert dt.get('epoch') != ""
    assert dt.get('epoch_int') != ""
    assert dt

# Generated at 2022-06-13 02:48:38.540936
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    try:
        from ansible.module_utils.facts import ansible_date_time_facts
    except:
        # Placeholder for Ansible 2.8 support
        module = basic.AnsibleModule(argument_spec={})
        module.exit_json = lambda x: x
        ansible_date_time_facts = {}
        ansible_date_time_facts['date_time'] = {}

    collector = DateTimeFactCollector(module=module)
    result = collector.collect(module=module, collected_facts=ansible_date_time_facts)

    assert isinstance(result, dict)
    assert isinstance(result['date_time'], dict)

    # Ensure that epoch is a (integer) timestamp


# Generated at 2022-06-13 02:48:41.194224
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    factobj = DateTimeFactCollector()
    factobj.collect()

if __name__ == '__main__':
    test_DateTimeFactCollector_collect()

# Generated at 2022-06-13 02:49:52.203975
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collectors import collector_module
    from ansible.module_utils.facts.collectors.other.date_time import DateTimeFactCollector

    DateTimeFactCollector._load_platform_subclass = lambda *args, **kwargs: None
    DateTimeFactCollector.CollectorMethod = lambda *args, **kwargs: None
    collector = DateTimeFactCollector(collector_module)
    result = collector.collect()

    assert result is not None
    assert 'date_time' in result
    assert result['date_time'] is not None
    assert len(result['date_time']) > 12

    date_time_facts = result['date_time']
    year = date_time_facts['year']
    assert year is not None
    assert len(year) == 4

    month

# Generated at 2022-06-13 02:50:02.033148
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    collected_facts = {}
    now = datetime.datetime.now()
    epoch_ts = time.time()
    facts = dt.collect()
    for fact, value in facts['date_time'].items():
        if fact == 'epoch' or fact == 'epoch_int':
            assert value == str(int(epoch_ts))
        elif fact == 'hour':
            assert value == now.strftime('%H')
        elif fact == 'minute':
            assert value == now.strftime('%M')
        elif fact == 'second':
            assert value == now.strftime('%S')
        elif fact == 'weekday':
            assert value.lower() == now.strftime('%A').lower()

# Generated at 2022-06-13 02:50:03.700595
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    c = DateTimeFactCollector()
    facts_dict = c.collect()
    assert 'date_time' in facts_dict

# Generated at 2022-06-13 02:50:13.798228
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()

    # call collect
    collected_facts = fact_collector.collect()['date_time']
    assert collected_facts['year'] == datetime.datetime.utcnow().strftime('%Y')
    assert collected_facts['month'] == datetime.datetime.utcnow().strftime('%m')
    assert collected_facts['weekday'] == datetime.datetime.utcnow().strftime('%A')
    assert collected_facts['weekday_number'] == datetime.datetime.utcnow().strftime('%w')
    assert collected_facts['weeknumber'] == datetime.datetime.utcnow().strftime('%W')
    assert collected_facts['day'] == datetime.datetime.utcnow().strftime('%d')

# Generated at 2022-06-13 02:50:21.635111
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    datetime_collector = DateTimeFactCollector()
    date_time_facts = datetime_collector.collect()['date_time']

    assert date_time_facts['year']
    assert date_time_facts['month']
    assert date_time_facts['weekday']
    assert date_time_facts['weekday_number']
    assert date_time_facts['weeknumber']
    assert date_time_facts['day']
    assert date_time_facts['hour']
    assert date_time_facts['minute']
    assert date_time_facts['second']
    assert date_time_facts['epoch']
    assert date_time_facts['epoch_int']
    assert date_time_facts['date']
    assert date_time_facts['time']

# Generated at 2022-06-13 02:50:25.722403
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_coll = DateTimeFactCollector()
    assert isinstance(dt_coll.collect(), dict)
    assert 'date_time' in dt_coll.collect()

# Generated at 2022-06-13 02:50:33.697358
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Tests the DateTimeFactCollector.collect method
    """
    collect_obj = DateTimeFactCollector()
    result = collect_obj.collect(module=None, collected_facts=None)
    assert type(result) == dict,\
        "Failed since result data type is not a dictionary"
    assert type(result['date_time']) == dict,\
        "Failed since date_time data type is not a dictionary"
    assert type(result['date_time']['epoch']) == str,\
        "Failed since date_time.epoch data type is not a string"
    assert type(result['date_time']['epoch_int']) == str,\
        "Failed since date_time.epoch_int data type is not a string"

# Generated at 2022-06-13 02:50:39.520013
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts = collector.collect()
    assert 'date_time' in facts
    assert facts['date_time']['year'] is not None
    assert facts['date_time']['month'] is not None
    assert facts['date_time']['day'] is not None
    assert facts['date_time']['hour'] is not None
    assert facts['date_time']['minute'] is not None
    assert facts['date_time']['second'] is not None
    assert facts['date_time']['epoch'] is not None
    assert facts['date_time']['epoch_int'] is not None
    assert facts['date_time']['date'] is not None
    assert facts['date_time']['time'] is not None