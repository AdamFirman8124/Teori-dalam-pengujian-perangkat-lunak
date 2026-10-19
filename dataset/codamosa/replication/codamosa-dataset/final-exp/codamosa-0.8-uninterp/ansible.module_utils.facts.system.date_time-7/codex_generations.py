

# Generated at 2022-06-13 02:40:44.863438
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    assert DateTimeFactCollector.collect({})

# Generated at 2022-06-13 02:40:54.777373
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf_collector = DateTimeFactCollector()
    datetime_dict = dtf_collector.collect()
    assert 'date_time' in datetime_dict
    assert 'year' in datetime_dict['date_time']
    assert 'month' in datetime_dict['date_time']
    assert 'weekday' in datetime_dict['date_time']
    assert 'weekday_number' in datetime_dict['date_time']
    assert 'weeknumber' in datetime_dict['date_time']
    assert 'day' in datetime_dict['date_time']
    assert 'hour' in datetime_dict['date_time']
    assert 'minute' in datetime_dict['date_time']
    assert 'second' in datetime_dict['date_time']
    assert 'epoch' in dat

# Generated at 2022-06-13 02:41:02.089801
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # arrange
    c = DateTimeFactCollector
    t = time.gmtime()
    t2 = time.time()
    module = None
    collected_facts = None
    # act
    r = c.collect(module, collected_facts)

    # assert
    assert r['date_time']['year'] == time.strftime('%Y')
    assert r['date_time']['month'] == time.strftime('%m')
    assert r['date_time']['weekday'] == time.strftime('%A')
    assert r['date_time']['weekday_number'] == time.strftime('%w')
    assert r['date_time']['weeknumber'] == time.strftime('%W')

# Generated at 2022-06-13 02:41:12.029692
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test that a "date_time" dict is returned with expected keys
    collector = DateTimeFactCollector()
    assert isinstance(collector.collect(), dict)
    assert 'date_time' in collector.collect()
    assert isinstance(collector.collect()['date_time'], dict)
    assert 'year' in collector.collect()['date_time']
    assert 'month' in collector.collect()['date_time']
    assert 'weekday' in collector.collect()['date_time']
    assert 'weekday_number' in collector.collect()['date_time']
    assert 'weeknumber' in collector.collect()['date_time']
    assert 'day' in collector.collect()['date_time']
    assert 'hour' in collector.collect()['date_time']
    assert 'minute' in collector.collect()

# Generated at 2022-06-13 02:41:22.095385
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts_collector = DateTimeFactCollector()
    date_time_facts = date_time_facts_collector.collect()
    assert type(date_time_facts) is dict
    assert 'date_time' in date_time_facts
    assert type(date_time_facts['date_time']) is dict
    assert 'year' in date_time_facts['date_time']
    assert type(date_time_facts['date_time']['year']) is str
    assert 'month' in date_time_facts['date_time']
    assert type(date_time_facts['date_time']['month']) is str
    assert 'weekday' in date_time_facts['date_time']
    assert type(date_time_facts['date_time']['weekday']) is str

# Generated at 2022-06-13 02:41:24.591151
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    ansible_collector.collect()
    assert ansible_collector.get_collection('date_time').has_key('date_time')

# Generated at 2022-06-13 02:41:30.814042
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    module = ansible.module_utils.facts.module

    dtfc = DateTimeFactCollector(module, {})
    collected_facts = {}
    collected_facts['date_time'] = dtfc.collect(module, collected_facts)

    assert collected_facts['date_time']['year']
    assert int(collected_facts['date_time']['year']) > 1970
    assert collected_facts['date_time']['month']
    assert int(collected_facts['date_time']['month']) > 0
    assert collected_facts['date_time']['weekday']
    assert collected_facts['date_time']['weekday_number']
    assert int(collected_facts['date_time']['weekday_number']) >= 0

# Generated at 2022-06-13 02:41:34.189440
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect(None)
    assert isinstance(date_time_facts, dict) and 'date_time' in date_time_facts
    assert isinstance(date_time_facts['date_time'], dict)

# Generated at 2022-06-13 02:41:43.973192
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_collector = DateTimeFactCollector()
    test_result = test_collector.collect()
    assert(isinstance(test_result, dict))
    assert(len(test_result) == 1)
    assert('date_time' in test_result)
    assert(isinstance(test_result['date_time'], dict))

    # year
    assert('year' in test_result['date_time'])
    assert(isinstance(test_result['date_time']['year'], str))

    # month
    assert('month' in test_result['date_time'])
    assert(isinstance(test_result['date_time']['month'], str))

    # weekday
    assert('weekday' in test_result['date_time'])

# Generated at 2022-06-13 02:41:46.011613
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fc = DateTimeFactCollector()
    facts = fc.collect()
    assert 'date_time' in facts

# Generated at 2022-06-13 02:41:51.904320
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector.collect()
    date_time_facts = date_time_fact_collector.collect(None, None)
    assert (date_time_facts['date_time']['epoch'] != '')

# Generated at 2022-06-13 02:41:58.924126
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # arrange
    facts_collector = DateTimeFactCollector()

    # act
    result = facts_collector.collect()

    # assert
    assert result is not None
    assert 'date_time' in result
    assert result['date_time'] is not None
    assert result['date_time']['second'] is not None
    assert result['date_time']['minute'] is not None
    assert result['date_time']['hour'] is not None
    assert result['date_time']['day'] is not None
    assert result['date_time']['weeknumber'] is not None
    assert result['date_time']['weekday'] is not None
    assert result['date_time']['weekday_number'] is not None
    assert result['date_time']['month'] is not None
   

# Generated at 2022-06-13 02:42:09.673428
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    date_time_facts = fact_collector.collect()
    assert date_time_facts.get('date_time') is not None, 'There should be date_time facts.'
    date_time = date_time_facts.get('date_time')
    assert date_time.get('year') is not None, 'There should be a year fact.'
    assert date_time.get('month') is not None, 'There should be a month fact.'
    assert date_time.get('weekday') is not None, 'There should be a weekday fact.'
    assert date_time.get('weekday_number') is not None, 'There should be a weekday_number fact.'
    assert date_time.get('weeknumber') is not None, 'There should be a weeknumber fact.'

# Generated at 2022-06-13 02:42:16.780357
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dc = DateTimeFactCollector()
    result = dc.collect()
    assert result.get('date_time') is not None
    date_time = result.get('date_time')
    assert date_time.get('year') is not None
    assert date_time.get('month') is not None
    assert date_time.get('weekday') is not None
    assert date_time.get('weekday_number') is not None
    assert date_time.get('weeknumber') is not None
    assert date_time.get('day') is not None
    assert date_time.get('hour') is not None
    assert date_time.get('minute') is not None
    assert date_time.get('second') is not None
    assert date_time.get('epoch') is not None
    assert date_time.get

# Generated at 2022-06-13 02:42:28.267885
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    datetime_collector = DateTimeFactCollector()

    # check that all keys are set correctly
    datetime_facts = datetime_collector.collect()
    assert isinstance(datetime_facts, dict)
    assert len(datetime_facts.keys()) == 1
    assert isinstance(datetime_facts['date_time'], dict)
    assert len(datetime_facts['date_time'].keys()) == 15

    # check that the epoch timestamp has increased since the last test
    current_epoch_timestamp = datetime_facts['date_time']['epoch_int']
    assert int(current_epoch_timestamp) > 1407415870
    # check that epoch_int returns an integer
    assert isinstance(int(current_epoch_timestamp), int)

# Generated at 2022-06-13 02:42:31.540831
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    my_collector = DateTimeFactCollector()
    my_facts = my_collector.collect()
    assert 'date_time' in my_facts

# Generated at 2022-06-13 02:42:33.618529
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    col = DateTimeFactCollector()
    assert 'date_time' in col.collect()
    assert 'year' in col.collect()['date_time']

# Generated at 2022-06-13 02:42:42.301598
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    input = dict()
    input['module'] = None
    input['collected_facts'] = None
    expect = dict()
    expect['date_time'] = dict()
    expect['date_time']['year'] = datetime.datetime.now().strftime('%Y')
    expect['date_time']['month'] = datetime.datetime.now().strftime('%m')
    expect['date_time']['day'] = datetime.datetime.now().strftime('%d')
    expect['date_time']['hour'] = datetime.datetime.now().strftime('%H')
    expect['date_time']['minute'] = datetime.datetime.now().strftime('%M')
    expect['date_time']['second'] = datetime.datetime.now().strftime

# Generated at 2022-06-13 02:42:44.794258
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_fact = date_time_collector.collect()
    assert date_time_fact['date_time']

# Generated at 2022-06-13 02:42:48.596303
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector_obj = DateTimeFactCollector()
    setattr(DateTimeFactCollector_obj, "collect", DateTimeFactCollector_obj.collect)
    print(DateTimeFactCollector_obj.collect())


# Generated at 2022-06-13 02:43:03.159455
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    date_time = dtf.collect()
    assert 'date_time' in date_time
    assert 'year' in date_time['date_time']
    assert 'month' in date_time['date_time']
    assert 'weekday' in date_time['date_time']
    assert 'weekday_number' in date_time['date_time']
    assert 'weeknumber' in date_time['date_time']
    assert 'day' in date_time['date_time']
    assert 'hour' in date_time['date_time']
    assert 'minute' in date_time['date_time']
    assert 'second' in date_time['date_time']
    assert 'epoch' in date_time['date_time']

# Generated at 2022-06-13 02:43:05.346816
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector.collect()


# Generated at 2022-06-13 02:43:12.466620
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:43:13.371912
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    facts = fact_collector.collect()
    assert 'date_time' in facts

# Generated at 2022-06-13 02:43:24.241711
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:43:29.859071
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect()
    assert 'date_time' in date_time_facts
    expected_entries = [
        'year',
        'month',
        'day',
        'weekday',
        'weekday_number',
        'weeknumber',
        'hour',
        'minute',
        'second',
        'epoch',
        'epoch_int',
        'iso8601',
        'iso8601_basic',
        'iso8601_basic_short',
        'tz',
        'tz_dst'
    ]
    for key in expected_entries:
        assert key in date_time_collector.collect()['date_time']

# Generated at 2022-06-13 02:43:33.653409
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert result.get('date_time') is not None
    assert result.get('date_time').get('epoch') is not None

# Generated at 2022-06-13 02:43:42.080292
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    d = datetime.datetime(2016, 2, 4, 9, 30, 2, 0)
    epoch_ts = 1454591002
    result = DateTimeFactCollector().collect(collected_facts=None)

# Generated at 2022-06-13 02:43:52.030106
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Arrange
    module = None
    collected_facts = None

    # Act
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector.collect(module, collected_facts)

    # Assert
    assert date_time_fact_collector.name == 'date_time', \
        "Module name should be 'date_time' but was %s" % date_time_fact_collector.name
    assert len(date_time_fact_collector._fact_ids) == 0, \
        "Number of fact ids should be 0 but was %s" % len(date_time_fact_collector._fact_ids)

# Generated at 2022-06-13 02:43:56.379489
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    This method is used to test if data is collected and returned
    for the 'date_time' section of ansible_facts.

    Returns:
        A dictionary that contains the collected data.
    """
    collector = DateTimeFactCollector()
    return collector.collect()

# vim: expandtab:tabstop=2:shiftwidth=2

# Generated at 2022-06-13 02:44:10.996790
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Determine if the DateTimeFactCollector can be instantiated.
    We don't check all the facts, just that it is a dictionary
    and that right number of factoids are the right types
    """

    df = DateTimeFactCollector()
    test_facts = df.collect()
    assert isinstance(test_facts['date_time'], dict)
    for k, v in test_facts['date_time'].items():
        assert isinstance(k, str)
        assert isinstance(v, str)

# Generated at 2022-06-13 02:44:16.561759
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts = DateTimeFactCollector()
    result = facts.collect()
    assert result['date_time']['time']
    assert result['date_time']['tz']
    assert result['date_time']['tz_offset']
    assert result['date_time']['tz_dst']

# Generated at 2022-06-13 02:44:23.273931
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # pylint: disable=protected-access

    # setup
    date_time_fact = DateTimeFactCollector()
    mock_module = None
    mock_collected_facts = None

    # run
    actual_return = date_time_fact.collect(mock_module, mock_collected_facts)

    # assert
    assert isinstance(actual_return, dict)
    # noinspection PyUnresolvedReferences
    assert actual_return['date_time']['tz'] is not None

# Generated at 2022-06-13 02:44:31.940685
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test when no args given
    facts = DateTimeFactCollector()

# Generated at 2022-06-13 02:44:41.806046
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect()
    # It's hard to do an assertTrue on the values of a dict without a lot of code
    # I'm therefore just verifying that a good number of the keys are there
    assert( len(date_time_facts) == 1 )
    assert( 'date_time' in date_time_facts )
    date_time_dict = date_time_facts[ 'date_time']
    assert( len(date_time_dict) >= 10 )
    assert( 'year' in date_time_dict )
    assert( 'month' in date_time_dict )
    assert( 'weekday' in date_time_dict )
    assert( 'weekday_number' in date_time_dict )

# Generated at 2022-06-13 02:44:43.723610
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts = DateTimeFactCollector().collect()
    assert isinstance(facts, dict)

# Generated at 2022-06-13 02:44:50.131171
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_info = DateTimeFactCollector().collect()
    assert date_time_info['date_time']['year'] is not None
    assert date_time_info['date_time']['month'] is not None
    assert date_time_info['date_time']['weekday'] is not None
    assert date_time_info['date_time']['weekday_number'] is not None
    assert date_time_info['date_time']['weeknumber'] is not None
    assert date_time_info['date_time']['day'] is not None
    assert date_time_info['date_time']['hour'] is not None
    assert date_time_info['date_time']['minute'] is not None

# Generated at 2022-06-13 02:45:00.653727
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import datetime
    import time
    current_time = datetime.datetime.now()
    current_epoch = time.time()
    current_epoch_int = int(current_epoch)
    obj = DateTimeFactCollector()
    facts = obj.collect()
    assert current_time.strftime('%Y') == facts['date_time']['year']
    assert current_time.strftime('%m') == facts['date_time']['month']
    assert current_time.strftime('%A') == facts['date_time']['weekday']
    assert current_time.strftime('%w') == facts['date_time']['weekday_number']
    assert current_time.strftime('%W') == facts['date_time']['weeknumber']

# Generated at 2022-06-13 02:45:10.698664
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    datetime_fact_collector = DateTimeFactCollector()
    result = datetime_fact_collector.collect()
    assert isinstance(result, dict)
    assert 'date_time' in result
    assert isinstance(result['date_time'], dict)
    assert 'date' in result['date_time']
    assert isinstance(result['date_time']['date'], str)
    assert 'time' in result['date_time']
    assert isinstance(result['date_time']['time'], str)
    assert 'year' in result['date_time']
    assert isinstance(result['date_time']['year'], str)
    assert 'month' in result['date_time']
    assert isinstance(result['date_time']['month'], str)
    assert 'weekday'

# Generated at 2022-06-13 02:45:14.009813
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    d = datetime.datetime.utcnow()
    f = DateTimeFactCollector()
    assert f.collect()['date_time']['month'] == d.strftime('%m')


# Generated at 2022-06-13 02:45:37.140626
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['date_time']['year'][0] == '2'
    assert collected_facts['date_time']['month'][0] == '0'
    assert collected_facts['date_time']['weekday'][0] in ['M', 'T', 'W', 'T', 'F', 'S', 'S']
    assert collected_facts['date_time']['weekday_number'][0] in ['0', '1', '2', '3', '4', '5', '6']
    assert collected_facts['date_time']['weeknumber'][0] == '0'

# Generated at 2022-06-13 02:45:46.156493
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    collection = DateTimeFactCollector({})
    # Now
    now = datetime.datetime.now().timetuple()

    # Generate test facts and expected result
    epoch_ts = time.time()
    test_facts = {}
    test_facts['year'] = str(now.tm_year)
    test_facts['month'] = str(now.tm_mon).zfill(2)
    test_facts['weekday'] = time.strftime("%A")
    test_facts['weekday_number'] = str(now.tm_wday)
    test_facts['weeknumber'] = str(now.tm_yday/7 + 1).zfill(2)
    test_facts['day'] = str(now.tm_mday).zfill(2)

# Generated at 2022-06-13 02:45:50.547125
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect(None, None)
    assert date_time_facts['date_time'] is not None

# Generated at 2022-06-13 02:46:02.518910
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    result = DateTimeFactCollector().collect()
    assert type(result['date_time']) is dict, "date_time fact must be a dict"
    assert 'year' in result['date_time'], "year fact does not exist in date_time dict"
    assert 'month' in result['date_time'], "month fact does not exist in date_time dict"
    assert 'weekday' in result['date_time'], "weekday fact does not exist in date_time dict"
    assert 'weekday_number' in result['date_time'], "weekday_number fact does not exist in date_time dict"
    assert 'weeknumber' in result['date_time'], "weeknumber fact does not exist in date_time dict"

# Generated at 2022-06-13 02:46:05.402355
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    my_obj = DateTimeFactCollector()
    my_result = my_obj.collect()
    assert my_result['date_time']['year'] == '2'

# Generated at 2022-06-13 02:46:13.629155
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()
    assert isinstance(date_time_facts, dict) and isinstance(date_time_facts['date_time'], dict)
    assert isinstance(date_time_facts['date_time']['epoch'], str)
    assert isinstance(date_time_facts['date_time']['epoch_int'], str)
    assert isinstance(date_time_facts['date_time']['second'], str)
    assert isinstance(date_time_facts['date_time']['tz_dst'], str)
    assert isinstance(date_time_facts['date_time']['tz'], str)
    assert isinstance(date_time_facts['date_time']['tz_offset'], str)

# Generated at 2022-06-13 02:46:23.860665
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Define a mock datetime object
    test_ts = 1562785511
    test_dt = datetime.datetime.fromtimestamp(test_ts)

    # Define test dict for required collector
    required_collector = {
        'kernel': 'Linux',
        'python': 2.7
    }

    # Define test dict for collected facts

# Generated at 2022-06-13 02:46:34.887957
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    basefact = DateTimeFactCollector()
    collected_facts = {}
    collected_facts = basefact.collect(collected_facts)
    assert isinstance(collected_facts, dict)
    assert collected_facts.get('date_time')
    assert collected_facts['date_time'].get('epoch')
    assert collected_facts['date_time'].get('epoch_int')
    assert collected_facts['date_time'].get('iso8601_micro')
    assert collected_facts['date_time'].get('iso8601')
    assert collected_facts['date_time'].get('iso8601_basic')
    assert collected_facts['date_time'].get('iso8601_basic_short')
    assert collected_facts['date_time'].get('tz')

# Generated at 2022-06-13 02:46:42.226523
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fc = DateTimeFactCollector()
    date_time_facts = fc.collect()['date_time']
    assert date_time_facts.has_key('year')
    assert date_time_facts.has_key('month')
    assert date_time_facts.has_key('weekday')
    assert date_time_facts.has_key('weekday_number')
    assert date_time_facts.has_key('weeknumber')
    assert date_time_facts.has_key('day')
    assert date_time_facts.has_key('hour')
    assert date_time_facts.has_key('minute')
    assert date_time_facts.has_key('second')
    assert date_time_facts.has_key('epoch')

# Generated at 2022-06-13 02:46:51.298179
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    res = DateTimeFactCollector().collect(collected_facts={})


# Generated at 2022-06-13 02:47:37.571064
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test that collector returns a dict key date_time
    date_time_collector = DateTimeFactCollector()
    result = date_time_collector.collect()
    assert('date_time' in result)

    # Test that values returned are of the correct type
    date_time_dict = result['date_time']
    assert('year' in date_time_dict)
    assert('month' in date_time_dict)
    assert('weekday' in date_time_dict)
    assert('weekday_number' in date_time_dict)
    assert('weeknumber' in date_time_dict)
    assert('day' in date_time_dict)
    assert('hour' in date_time_dict)
    assert('minute' in date_time_dict)
    assert('second' in date_time_dict)

# Generated at 2022-06-13 02:47:47.443832
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    data_time_fact_collector = DateTimeFactCollector()
    data_time_facts = data_time_fact_collector.collect()

    assert isinstance(data_time_facts, dict)
    assert 'date_time' in data_time_facts

    data_time_dict = data_time_facts['date_time']

    assert 'year' in data_time_dict
    assert 'month' in data_time_dict
    assert 'weekday' in data_time_dict
    assert 'weekday_number' in data_time_dict
    assert 'weeknumber' in data_time_dict
    assert 'day' in data_time_dict
    assert 'hour' in data_time_dict
    assert 'minute' in data_time_dict
    assert 'second' in data_time_dict

# Generated at 2022-06-13 02:47:51.542072
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    # Since we can't test this, we just make sure it returns a non-zero data set
    assert date_time_facts['date_time']['year'] == ''

# Generated at 2022-06-13 02:47:55.463213
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    temp = DateTimeFactCollector()
    result = temp.collect()
    assert result is not None
    assert result['date_time'] is not None
    assert result['date_time']['date'] is not None


# Generated at 2022-06-13 02:48:03.787831
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create an instance of the class DateTimeFactCollector
    fact_collector = DateTimeFactCollector()
    # Call method collect of class DateTimeFactCollector
    collected_facts = fact_collector.collect()
    # Test if the collected facts are equal to the expected facts

# Generated at 2022-06-13 02:48:15.867139
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    assert len(date_time_facts) == 1
    date_time_facts = date_time_facts['date_time']
    assert len(date_time_facts) == 18
    assert date_time_facts['year'] is not None
    assert date_time_facts['month'] is not None
    assert date_time_facts['weekday'] is not None
    assert date_time_facts['weekday_number'] is not None
    assert date_time_facts['weeknumber'] is not None
    assert date_time_facts['day'] is not None
    assert date_time_facts['hour'] is not None
    assert date_time_facts['minute'] is not None

# Generated at 2022-06-13 02:48:22.389708
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import DictFactsCollector
    from ansible.module_utils.facts import BaseFactCollector

    assert isinstance(DateTimeFactCollector.collect(DictFactsCollector()), dict)
    assert isinstance(DateTimeFactCollector.collect(DictFactsCollector()), dict)
    assert isinstance(DateTimeFactCollector.collect(BaseFactCollector()), dict)

# Generated at 2022-06-13 02:48:26.727872
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()

    # get facts as a dict
    result = date_time_fact_collector.collect()
    assert isinstance(result, dict)
    assert 'date_time' in result
    assert isinstance(result['date_time'], dict)

    # test if values have a non-zero length
    assert len(result['date_time']['year']) > 0
    assert len(result['date_time']['month']) > 0
    assert len(result['date_time']['weekday']) > 0
    assert len(result['date_time']['weekday_number']) > 0
    assert len(result['date_time']['weeknumber']) > 0
    assert len(result['date_time']['day']) > 0

# Generated at 2022-06-13 02:48:29.839058
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Setup
    collector = DateTimeFactCollector()

    # Test
    facts = collector.collect()

    # Assert
    assert facts['date_time'] != {}

# Generated at 2022-06-13 02:48:40.266607
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
    date_time_facts['day'] = now.str

# Generated at 2022-06-13 02:49:14.043544
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()


# Generated at 2022-06-13 02:49:25.131959
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    results = date_time_fact_collector.collect()

    assert type(results) == dict
    assert 'date_time' in results

    date_time_facts = results['date_time']
    assert date_time_facts['year'] == now.strftime('%Y')
    assert date_time_facts['month'] == now.strftime('%m')
    assert date_time_facts['weekday'] == now.strftime('%A')

# Generated at 2022-06-13 02:49:27.009870
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()
    assert date_time_facts['date_time']['iso8601_basic_short']

# Generated at 2022-06-13 02:49:29.062419
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    f = DateTimeFactCollector()
    f.collect()

# Generated at 2022-06-13 02:49:31.974680
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact = DateTimeFactCollector()
    result = date_time_fact.collect()
    assert result['date_time']['iso8601_micro'] is not None

# Generated at 2022-06-13 02:49:40.558878
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    run_setup_module method receives module_name, tree_info and new_facts
    from AnsibleModule and calls respective collect_<module_name> methods.
    The call is made to DateTimeFactCollector.collect() method here.
    """
    # NOTE: This test is used in tox.ini to test the method collect of DateTimeFactCollector in fact_collector.py
    #       since the module DateTimeFactCollector itself doesn't have __init__ method.
    #       The python interpreter throws an error "TypeError: Cannot create a
    #       consistent method resolution order (MRO) for bases
    #       DateTimeFactCollector" when DateTimeFactCollector class is directly
    #       instantiated using class name DateTimeFactCollector.
    #       Therefore the unittest is written against the parent class BaseFactCollector and the

# Generated at 2022-06-13 02:49:51.063222
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    result = dtf.collect()

    assert result is not None
    assert result['date_time'] is not None
    assert 'year' in result['date_time']
    assert 'month' in result['date_time']
    assert 'weekday' in result['date_time']
    assert 'weekday_number' in result['date_time']
    assert 'weeknumber' in result['date_time']
    assert 'day' in result['date_time']
    assert 'hour' in result['date_time']
    assert 'minute' in result['date_time']
    assert 'second' in result['date_time']
    assert 'epoch' in result['date_time']
    assert 'epoch_int' in result['date_time']

# Generated at 2022-06-13 02:50:01.472002
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_dtfc = DateTimeFactCollector()
    res = test_dtfc.collect()
    assert 'date_time' in res
    assert 'year' in res['date_time']
    assert 'month' in res['date_time']
    assert 'weekday' in res['date_time']
    assert 'weekday_number' in res['date_time']
    assert 'weeknumber' in res['date_time']
    assert 'day' in res['date_time']
    assert 'hour' in res['date_time']
    assert 'minute' in res['date_time']
    assert 'second' in res['date_time']
    assert 'epoch' in res['date_time']
    assert 'epoch_int' in res['date_time']
    assert 'date' in res['date_time']


# Generated at 2022-06-13 02:50:11.871028
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts_dict = {}
    dtfc = DateTimeFactCollector()
    dtfc.collect(collected_facts=facts_dict)
    expected_fields = sorted(["epoch", "epoch_int", "date", "day", "hour",
                             "iso8601", "iso8601_basic", "iso8601_basic_short",
                             "iso8601_micro", "minute", "month", "second",
                             "time", "tz", "tz_dst", "tz_offset", "weekday",
                             "weekday_number", "weeknumber", "year"])
    actual_fields = sorted(facts_dict['date_time'].keys())
    assert expected_fields == actual_fields

# Generated at 2022-06-13 02:50:20.319628
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from datetime import datetime
    from time import time
    from time import strftime
    from time import tzname

    date_time_facts = {}
    epoch_ts = time()
    now = datetime.fromtimestamp(epoch_ts)
    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
    date_time_facts['weekday_number'] = now.strftime('%w')
    date_time_facts['weeknumber'] = now.strftime('%W')
    date_time_facts['day'] = now.strftime('%d')
    date_time_facts['hour'] = now.strftime('%H')