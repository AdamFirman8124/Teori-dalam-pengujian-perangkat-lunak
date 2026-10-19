

# Generated at 2022-06-13 02:40:48.579746
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Unit test for method collect of class DateTimeFactCollector
    """
    date_time_facts = DateTimeFactCollector().collect()
    assert 'date_time' in date_time_facts
    assert 'minute' in date_time_facts['date_time']
    assert '20' == date_time_facts['date_time']['minute']

# Generated at 2022-06-13 02:40:58.221705
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    data = dtf.collect()
    assert type(data) is dict
    assert 'date_time' in data
    assert data['date_time']
    assert type(data['date_time']) is dict
    date_time_dict = data['date_time']
    assert 'year' in date_time_dict
    assert type(date_time_dict['year']) is str
    assert 'month' in date_time_dict
    assert type(date_time_dict['month']) is str
    assert 'weekday' in date_time_dict
    assert type(date_time_dict['weekday']) is str
    assert 'weekday_number' in date_time_dict
    assert type(date_time_dict['weekday_number']) is str

# Generated at 2022-06-13 02:40:59.269415
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector.collect()

# Generated at 2022-06-13 02:41:05.959271
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    from ansible.module_utils.facts.collector import add_collector, list_collectors

    DateTimeFactCollector_instance = DateTimeFactCollector()

    # Add the instance to the list of collectors
    add_collector(DateTimeFactCollector_instance)

    # list_collectors should contain the new Collector
    assert DateTimeFactCollector_instance.name in list_collectors()

    # The collect method should return a dictionary 
    assert isinstance(DateTimeFactCollector_instance.collect(), dict)

# Generated at 2022-06-13 02:41:06.461709
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    pass

# Generated at 2022-06-13 02:41:06.972361
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    pass

# Generated at 2022-06-13 02:41:14.014023
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create a DateTimeFactCollector object to test and create a datetime object to test against
    date_time_testobj = DateTimeFactCollector()
    now_testobj = datetime.datetime.now()

    # Collect the facts from the object
    facts_dict = date_time_testobj.collect()
    # Compare the test object datetime to the datetime facts collected in facts_dict
    assert facts_dict['date_time']['year'] == str(now_testobj.year)
    assert facts_dict['date_time']['month'] == str(now_testobj.month).zfill(2)
    assert facts_dict['date_time']['weekday'].lower() == now_testobj.strftime('%A').lower()

# Generated at 2022-06-13 02:41:16.917751
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    c = DateTimeFactCollector()
    date_time_facts = c.collect()
    assert date_time_facts['date_time']['iso8601'] == '1970-01-01T00:00:00Z'

# Generated at 2022-06-13 02:41:25.624964
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:41:34.682393
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''date_time_facts.py: test_DateTimeFactCollector_collect'''
    datetime_facts = DateTimeFactCollector()
    result = datetime_facts.collect()

    # test to see if the method returns a datatype of dict
    assert type(result) is dict

    # test to see if the method returns a dictionary with the key 'date_time'
    assert 'date_time' in result

    # test to see if the method returns a dictionary with the key 'epoch'
    assert 'epoch' in result['date_time']

    # test to see if the method returns a dictionary with the key 'epoch_int'
    assert 'epoch_int' in result['date_time']

    # test to see if the method returns a dictionary with the key 'iso8601'
    assert 'iso8601'

# Generated at 2022-06-13 02:41:46.500001
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    now = datetime.datetime.now()
    epoch = time.time()
    UTC = datetime.datetime.fromtimestamp(epoch)

    # In this test we will use a 1 second window to check time facts.
    # This is because there is a chance that another second may pass during the test.
    # - The checks for all fields should be within 1 second of the epoch.

    # This is a total hack, but it's a good way to prevent test from being too slow
    # and also from it failing from a second passing during the test.
    result = DateTimeFactCollector().collect()
    if abs(float(result['date_time']['epoch']) - epoch) > 1.0:
        raise AssertionError()

# Generated at 2022-06-13 02:41:55.309942
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_collector = DateTimeFactCollector({})
    result = dt_collector.collect()

    assert type(result) == dict
    assert 'date_time' in result

    assert type(result['date_time']) == dict
    assert 'year' in result['date_time']
    assert result['date_time']['year']==time.strftime("%Y")
    assert 'month' in result['date_time']
    assert result['date_time']['month']==time.strftime("%m")
    assert 'weekday' in result['date_time']
    assert result['date_time']['weekday']==time.strftime("%A")
    assert 'weekday_number' in result['date_time']

# Generated at 2022-06-13 02:42:02.798240
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_data = DateTimeFactCollector().collect()
    assert test_data['date_time']['year']
    assert test_data['date_time']['month']
    assert test_data['date_time']['weekday']
    assert test_data['date_time']['weekday_number']
    assert test_data['date_time']['weeknumber']
    assert test_data['date_time']['day']
    assert test_data['date_time']['hour']
    assert test_data['date_time']['minute']
    assert test_data['date_time']['second']
    assert test_data['date_time']['epoch']
    assert test_data['date_time']['epoch_int']

# Generated at 2022-06-13 02:42:05.495637
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc.collect()


if __name__ == '__main__':
    test_DateTimeFactCollector_collect()

# Generated at 2022-06-13 02:42:15.334979
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts_dict = date_time_fact_collector.collect()
    assert isinstance(date_time_facts_dict, dict)
    assert 'date_time' in date_time_facts_dict, "Missing 'date_time' key in return data."
    assert isinstance(date_time_facts_dict['date_time'], dict)


# Generated at 2022-06-13 02:42:28.267449
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:42:39.089208
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''Unit test for method collect of class DateTimeFactCollector'''

    # Define module input parameters
    module_params = { }

    # Define module return values

# Generated at 2022-06-13 02:42:41.504729
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    ansible_date_time = DateTimeFactCollector()
    ret = ansible_date_time.collect()
    assert 'date_time' in ret

# Generated at 2022-06-13 02:42:46.934921
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    facts = fact_collector.collect()

    # Assert that some specific fields exist
    assert('date_time' in facts)
    assert('iso8601' in facts['date_time'])
    assert('tz' in facts['date_time'])
    assert('iso8601_basic_short' in facts['date_time'])
    assert('date' in facts['date_time'])
    assert('time' in facts['date_time'])

    # Assert that the returned dictionary is not empty
    assert(facts['date_time'])

# Generated at 2022-06-13 02:42:52.036439
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    df = DateTimeFactCollector()
    results = df.collect()
    assert 'epoch' in results['date_time']
    assert 'year' in results['date_time']
    assert 'day' in results['date_time']

# Test whether attribute name exists

# Generated at 2022-06-13 02:43:03.317003
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import ansible_collections
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collectors.base import Collector, FactsCollector

    ansible_collections.init_collections()
    fact_collector = DateTimeFactCollector(Collector)
    fact_collector.collect()
    facts = Facts()
    facts_collector = FactsCollector(facts, [fact_collector])
    facts_collector.collect()
    assert facts.get('date_time') is not None
    assert facts.get('date_time').get('year') is not None
    assert facts.get('date_time').get('month') is not None

# Generated at 2022-06-13 02:43:04.074544
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    pass

# Generated at 2022-06-13 02:43:06.396369
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    # ToDo: What should be the return value?
    retval = dtfc.collect()
    assert retval != None

# Generated at 2022-06-13 02:43:08.446398
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    c = DateTimeFactCollector()
    result = c.collect()
    assert result['date_time']['epoch_int'] == result['date_time']['epoch']

# Generated at 2022-06-13 02:43:12.677748
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    assert isinstance(date_time_facts, dict)
    assert isinstance(date_time_facts['date_time'], dict)
    assert type(date_time_facts['date_time']['epoch']) == str
    assert type(date_time_facts['date_time']['epoch_int']) == str


# Generated at 2022-06-13 02:43:14.769717
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc.collect()


# Generated at 2022-06-13 02:43:25.336257
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    result = date_time_fact_collector.collect()

    assert isinstance(result['date_time']['year'], str)
    assert isinstance(result['date_time']['month'], str)
    assert isinstance(result['date_time']['weekday'], str)
    assert isinstance(result['date_time']['weekday_number'], str)
    assert isinstance(result['date_time']['weeknumber'], str)
    assert isinstance(result['date_time']['day'], str)
    assert isinstance(result['date_time']['hour'], str)
    assert isinstance(result['date_time']['minute'], str)

# Generated at 2022-06-13 02:43:31.824871
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test1 = DateTimeFactCollector()
    result = test1.collect(None, None)

    # Should return 1 entry since it's not filtered
    assert len(result) == 1

    # Check if date_time exists in result
    assert result.keys() == ['date_time']

    # Check if date_time has 20 entries
    assert len(result['date_time']) == 20

# Generated at 2022-06-13 02:43:41.059811
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    date_time = dt.collect()
    assert 'date_time' in date_time
    date_time_dict = date_time['date_time']
    assert 'year' in date_time_dict
    assert 'month' in date_time_dict
    assert 'weekday' in date_time_dict
    assert 'weekday_number' in date_time_dict
    assert 'weeknumber' in date_time_dict
    assert 'day' in date_time_dict
    assert 'hour' in date_time_dict
    assert 'minute' in date_time_dict
    assert 'second' in date_time_dict
    assert 'iso8601_micro' in date_time_dict
    assert 'iso8601' in date_time_dict

# Generated at 2022-06-13 02:43:53.068301
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:44:08.887097
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector(None).collect()
    assert date_time_facts['date_time']['year'] == '2020'
    assert date_time_facts['date_time']['month'] == '08'
    assert date_time_facts['date_time']['weekday'] == 'Friday'
    assert date_time_facts['date_time']['weekday_number'] == '5'
    assert date_time_facts['date_time']['weeknumber'] == '32'
    assert date_time_facts['date_time']['day'] == '28'
    assert date_time_facts['date_time']['hour'] == '07'
    assert date_time_facts['date_time']['minute'] == '27'

# Generated at 2022-06-13 02:44:12.720872
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    a = DateTimeFactCollector()
    b = a.collect()
    assert b != {}
    assert b.get("date_time")


# Generated at 2022-06-13 02:44:15.256825
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()

    assert isinstance(dt.collect(None, {}), dict)

# Generated at 2022-06-13 02:44:25.194301
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Import here - top level imports make modules reload
    # every time facts are collected
    import datetime
    import time
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)
    date_time_facts_return = {}
    date_time_facts = {}
    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
    date_time_facts['weekday_number'] = now.strftime('%w')

# Generated at 2022-06-13 02:44:35.393216
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    now = datetime.datetime.utcnow()
    epoch_ts = now.strftime("%s")
    date_time_facts = date_time_fact_collector.collect()
    assert isinstance(date_time_facts['date_time']['epoch_int'], str)
    assert int(date_time_facts['date_time']['epoch_int']) == int(epoch_ts)
    assert date_time_facts['date_time']['month'] == now.strftime("%m")
    assert date_time_facts['date_time']['year'] == now.strftime("%Y")

# Generated at 2022-06-13 02:44:43.282887
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    facts = dtfc.collect()
    assert 'date_time' in facts
    date_time = facts['date_time']
    assert date_time['month'] != ''
    assert date_time['day'] != ''
    assert date_time['weekday_number'] != ''
    assert date_time['weeknumber'] != ''
    assert date_time['hour'] != ''
    assert date_time['minute'] != ''
    assert date_time['second'] != ''
    assert date_time['epoch'] != ''
    assert date_time['epoch_int'] != ''
    assert date_time['date'] != ''
    assert date_time['time'] != ''
    assert date_time['iso8601_micro'] != ''

# Generated at 2022-06-13 02:44:49.586715
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    assert 'date_time' in date_time_facts, 'date_time key must be present'
    assert 'year' in date_time_facts['date_time'], 'year key must be present'
    assert 'month' in date_time_facts['date_time'], 'month key must be present'
    assert 'weekday' in date_time_facts['date_time'], 'weekday key must be present'
    assert 'weekday_number' in date_time_facts['date_time'], 'weekday_number key must be present'
    assert 'weeknumber' in date_time_facts['date_time'], 'weeknumber key must be present'

# Generated at 2022-06-13 02:45:00.344100
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    # Generate a fake time for testing
    EDUTC = datetime.datetime(2042, 3, 5, 9, 52, 3)
    # Set the given fake time as current system time
    date_time_fact_collector.get_datetime = lambda: EDUTC
    # Call the collect method of DateTimeFactCollector
    facts = date_time_fact_collector.collect()

    assert facts['date_time']['year'] == '2042'
    assert facts['date_time']['month'] == '03'
    assert facts['date_time']['weekday'] == 'Sunday'
    assert facts['date_time']['weekday_number'] == '0'

# Generated at 2022-06-13 02:45:10.659511
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_dict = date_time_collector.collect()
    assert isinstance(date_time_dict, dict)
    assert len(date_time_dict) == 1
    assert 'date_time' in date_time_dict
    assert isinstance(date_time_dict['date_time'], dict)
    assert 'month' in date_time_dict['date_time']
    assert isinstance(date_time_dict['date_time']['month'], str)
    assert 'day' in date_time_dict['date_time']
    assert isinstance(date_time_dict['date_time']['day'], str)
    assert 'year' in date_time_dict['date_time']

# Generated at 2022-06-13 02:45:11.460005
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:45:35.381429
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_collector = DateTimeFactCollector(None)
    time_now = time.time()
    time_now_rounded = round(time_now)
    time_now_utc = datetime.datetime.utcfromtimestamp(time_now_rounded)
    time_now_local = datetime.datetime.fromtimestamp(time_now_rounded)

    fact_dict = test_collector.collect()

    assert fact_dict['date_time']['hour'] == time_now_local.strftime('%H')
    assert fact_dict['date_time']['month'] == time_now_local.strftime('%m')
    assert fact_dict['date_time']['tz'] == time.strftime("%Z")

# Generated at 2022-06-13 02:45:41.205007
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Test DateTimeFactCollector.collect"""
    dt = DateTimeFactCollector()
    date_time = dt.collect()['date_time']

    # e.g. {'date': '2016-10-28', 'iso8601': '2016-10-28T17:34:05Z', ...}
    assert 'date' in date_time
    assert 'iso8601' in date_time

# Generated at 2022-06-13 02:45:48.595154
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Unit test method collect of DateTimeFactCollector"""
    d = DateTimeFactCollector()
    result = d.collect()

# Generated at 2022-06-13 02:46:00.078949
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Setup
    date_time_fact = DateTimeFactCollector()
    date_time = date_time_fact.collect()['date_time']

    # Test conditions
    assert 'year' in date_time
    assert len(date_time['year']) == 4
    assert date_time['year'].isdigit()
    assert 'month' in date_time
    assert len(date_time['month']) == 2
    assert date_time['month'].isdigit()
    assert 'weekday' in date_time
    assert 'weekday_number' in date_time
    assert len(date_time['weekday_number']) == 1
    assert date_time['weekday_number'].isdigit()
    assert 'weeknumber' in date_time
    assert 'day' in date_time

# Generated at 2022-06-13 02:46:03.330871
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc.collect()
    assert dtfc.fact_ids() == set(['date_time'])

# Generated at 2022-06-13 02:46:05.833661
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    facts = fact_collector.collect()
    assert isinstance(facts['date_time'], dict)

# Generated at 2022-06-13 02:46:06.444457
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    pass

# Generated at 2022-06-13 02:46:09.261532
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    epoch_ts = time.time()
    dtf = DateTimeFactCollector()
    res = dtf.collect()
    assert res['date_time']['epoch'] == str(int(epoch_ts))

# Generated at 2022-06-13 02:46:20.823521
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:46:31.806408
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    now = datetime.datetime.now()
    epoch_ts = time.time()
    facts_dict = fact_collector.collect()
    assert facts_dict["date_time"]["year"] == now.strftime('%Y')
    assert facts_dict["date_time"]["month"] == now.strftime('%m')
    assert facts_dict["date_time"]["weekday"] == now.strftime('%A')
    assert facts_dict["date_time"]["weekday_number"] == now.strftime('%w')
    assert facts_dict["date_time"]["weeknumber"] == now.strftime('%W')
    assert facts_dict["date_time"]["day"] == now.strftime('%d')

# Generated at 2022-06-13 02:47:07.622028
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collectors import collector_module
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
        
    result = DateTimeFactCollector.collect()
    assert result
    assert type(result) is dict
    assert result['date_time']['second'] == '%S'

# Generated at 2022-06-13 02:47:15.823532
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:47:16.660120
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:47:22.235883
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create an instance of class DateTimeFactCollector
    fact_collector = DateTimeFactCollector()

    # Get the fact using method collect
    fact = fact_collector.collect()

    # Verifies fact
    assert fact['date_time']['day'] == '31'
    assert fact['date_time']['hour'] == '12'
    assert fact['date_time']['minute'] == '48'
    assert fact['date_time']['month'] == '12'
    assert fact['date_time']['second'] == '50'
    assert fact['date_time']['weekday'] == 'Monday'
    assert fact['date_time']['weekday_number'] == '1'
    assert fact['date_time']['weeknumber'] == '51'

# Generated at 2022-06-13 02:47:28.169874
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    dtf_factory = DateTimeFactCollector()
    dtf_collector = FactsCollector([], [dtf_factory])
    dtf_collector.collect()
    result = dtf_factory.collect()
    assert result['date_time']['year'] is not None
    assert result['date_time']['month'] is not None
    assert result['date_time']['weekday'] is not None
    assert result['date_time']['weekday_number'] is not None
    assert result['date_time']['weeknumber'] is not None
    assert result['date_time']['day'] is not None
    assert result['date_time']['hour'] is not None

# Generated at 2022-06-13 02:47:29.048598
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    pass

# Generated at 2022-06-13 02:47:35.518017
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    assert date_time_facts is not None
    assert 'date_time' in date_time_facts
    assert 'year' in date_time_facts['date_time']
    assert 'epoch' in date_time_facts['date_time']
    assert 'epoch_int' in date_time_facts['date_time']

# Generated at 2022-06-13 02:47:45.913283
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
    from ansible.module_utils.facts.collectors.system import SystemFactCollector

    # We always want the DateTimeFactCollector to be the first one
    # so that any other collectors can use the date_time information
    wanted_collectors = [DateTimeFactCollector]
    wanted_collectors.extend([x for x in FactCollector.get_collectors() if x.name != 'date_time'])

    with FactCollector.override_default_collectors(wanted_collectors):
        facts = FactCollector().collect(module=None, collected_facts=None)

    date_time_facts = facts.get('date_time')

# Generated at 2022-06-13 02:47:49.614834
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Unit test for method collect of class DateTimeFactCollector
    """
    # Test a successful return.
    collector = DateTimeFactCollector()
    res = collector.collect()
    assert 'date_time' in res
    assert 'epoch' in res['date_time']
    assert res['date_time']['epoch'] != ''

# Generated at 2022-06-13 02:47:54.664046
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    dt_facts = dt.collect()
    assert isinstance(dt_facts, dict) == True
    assert dt_facts['date_time']['year'].isdigit()
    assert dt_facts['date_time']['month'].isdigit()
    assert dt_facts['date_time']['day'].isdigit()
    assert dt_facts['date_time']['hour'].isdigit()
    assert dt_facts['date_time']['minute'].isdigit()
    assert dt_facts['date_time']['second'].isdigit()
    assert dt_facts['date_time']['epoch'].isdigit()

# Generated at 2022-06-13 02:49:00.248585
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create an instance of DateTimeFactCollector
    obj = DateTimeFactCollector()

    # Test that collect method returns a nested dictionary of fact entries.
    # Test that the keys of the nested dictionary are 'date_time', 'date_time.year',
    # 'date_time.month', 'date_time.weekday', 'date_time.weekday_number',
    # 'date_time.weeknumber', 'date_time.day', 'date_time.hour',
    # 'date_time.minute', 'date_time.second', 'date_time.epoch',
    # 'date_time.epoch_int', 'date_time.date', 'date_time.time', 'date_time.iso8601_micro',
    # 'date_time.iso8601', 'date_time.iso8601_basic',

# Generated at 2022-06-13 02:49:11.153254
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import collector_registry
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import get_facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    import ansible.module_utils.facts.collectors.date_time
    import datetime
    import time
    all_facts = get_all_facts(dict(gather_subset=['all']))
    all_collectors = list(collector_registry.values())
    all_collectors_names = [c.name for c in all_collectors]
    BaseFactCollector._fact_cache = dict()
    DateTimeFactCollector._fact_ids = set()
    assert 'date_time' in all_collectors_

# Generated at 2022-06-13 02:49:14.600165
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collected_facts = {}
    results = DateTimeFactCollector().collect(collected_facts=collected_facts)
    assert isinstance(results, dict)
    assert 'date_time' in results
    assert results['date_time'] is not None

# Generated at 2022-06-13 02:49:25.650556
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect()
    date_time_facts['date_time']
    assert 'date_time' in date_time_facts
    assert 'epoch_int' in date_time_facts['date_time']
    assert 'epoch' in date_time_facts['date_time']
    assert 'iso8601' in date_time_facts['date_time']
    assert 'iso8601_basic' in date_time_facts['date_time']
    assert 'iso8601_basic_short' in date_time_facts['date_time']
    assert 'iso8601_micro' in date_time_facts['date_time']
    assert 'month' in date_time_facts['date_time']

# Generated at 2022-06-13 02:49:29.566956
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    dtfc = DateTimeFactCollector()

    # Test collect with empty
    assert  dtfc.collect({}, {}) != {}

    # Test collect with data
    assert  dtfc.collect({}, {'datetime': {}}) != {}

# Generated at 2022-06-13 02:49:39.505010
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()

# Generated at 2022-06-13 02:49:50.715992
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Create an instance of the DateTimeFactCollector
    dateTimeFactCollector = DateTimeFactCollector()

    # Make a call to the collect() method of the DateTimeFactCollector instance created above
    collectedFacts = dateTimeFactCollector.collect()

    # Validate that the collectedFacts dictionary contains a dictionary named as 'date_time'
    assert 'date_time' in collectedFacts

    # Validate that the collectedFacts dictionary contains the following keys in the 'date_time' dictionary
    assert len(collectedFacts['date_time']) == 16
    assert 'day' in collectedFacts['date_time']
    assert 'epoch' in collectedFacts['date_time']
    assert 'epoch_int' in collectedFacts['date_time']
    assert 'date' in collectedFacts['date_time']


# Generated at 2022-06-13 02:50:01.102662
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:50:11.273371
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Setup the instance
    test_inst = DateTimeFactCollector()

    # Run the code
    ansible_facts = test_inst.collect()

    # Assertions
    assert 'date_time' in ansible_facts
    assert 'weekday' in ansible_facts['date_time']
    assert 'date' in ansible_facts['date_time']
    assert 'time' in ansible_facts['date_time']
    assert 'tz' in ansible_facts['date_time']
    assert 'tz_offset' in ansible_facts['date_time']
    assert 'iso8601' in ansible_facts['date_time']

    # Cleanup
    del test_inst

# Generated at 2022-06-13 02:50:19.872526
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    utc_now = datetime.datetime.utcnow()
    utc_now_micro = utc_now.strftime("%Y-%m-%dT%H:%M:%S.%f")

    mock_module = type('mock_module', (object,), {'ansible_facts': {}})
    mock_module.ansible_facts = {'date_time': {}}

    dt_fact_collector = DateTimeFactCollector()
    date_time_facts = dt_fact_collector.collect(mock_module)
    assert date_time_facts['date_time'] is not None
    assert date_time_facts['date_time']['year']
    assert date_time_facts['date_time']['month']