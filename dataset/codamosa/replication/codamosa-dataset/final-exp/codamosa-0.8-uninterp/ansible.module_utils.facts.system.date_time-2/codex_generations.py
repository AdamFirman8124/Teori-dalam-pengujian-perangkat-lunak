

# Generated at 2022-06-13 02:40:54.408718
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    assert isinstance(DateTimeFactCollector.collect()['date_time']['tz'], str)
    assert isinstance(DateTimeFactCollector.collect()['date_time']['date'], str)
    assert isinstance(DateTimeFactCollector.collect()['date_time']['time'], str)
    assert isinstance(DateTimeFactCollector.collect()['date_time']['weekday'], str)
    assert isinstance(DateTimeFactCollector.collect()['date_time']['iso8601_micro'], str)
    assert isinstance(DateTimeFactCollector.collect()['date_time']['weekday_number'], str)
    assert isinstance(DateTimeFactCollector.collect()['date_time']['tz_dst'], str)

# Generated at 2022-06-13 02:41:01.817558
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    returned = date_time_collector.collect()

    assert isinstance(returned, dict)
    assert set(returned.keys()) == {'date_time'}
    assert isinstance(returned['date_time'], dict)

# Generated at 2022-06-13 02:41:10.371307
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    facts_dict = date_time_fact_collector.collect()
    assert facts_dict['date_time']
    assert isinstance(facts_dict['date_time'], dict)
    assert facts_dict['date_time']['date']
    assert facts_dict['date_time']['epoch']
    assert facts_dict['date_time']['year']
    assert facts_dict['date_time']['month']
    assert facts_dict['date_time']['tz']

# Generated at 2022-06-13 02:41:16.518428
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    time_format = '%Y-%m-%dT%H:%M:%SZ'

    result = dtfc.collect()
    assert result['date_time']['iso8601'] == datetime.datetime.strptime(result['date_time']['iso8601'], time_format)

# Generated at 2022-06-13 02:41:25.243358
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Setup test environment
    DateTimeFactCollector.collect(collected_facts=dict())

    # Test basic functionality
    test_epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(test_epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(test_epoch_ts)

    assert now.strftime('%Y') == DateTimeFactCollector.collect(collected_facts=dict())['date_time']['year']
    assert now.strftime('%m') == DateTimeFactCollector.collect(collected_facts=dict())['date_time']['month']
    assert now.strftime('%A') == DateTimeFactCollector.collect(collected_facts=dict())['date_time']['weekday']

# Generated at 2022-06-13 02:41:26.319302
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dc = DateTimeFactCollector()
    assert dc.collect()

# Generated at 2022-06-13 02:41:35.328274
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create an instance of class DateTimeFactCollector
    dtfc = DateTimeFactCollector()

    # Verify the instance was created and the variable name is accurate
    assert isinstance(dtfc, DateTimeFactCollector)
    assert dtfc.name == 'date_time'
    assert dtfc._fact_ids == set()

    # Create an instance of class DateTimeFactCollector
    dtfc = DateTimeFactCollector()

    # Get the date_time facts (which are a dict)
    date_time_facts = dtfc.collect()

    # Verify the instance was created and the variable name is accurate
    assert isinstance(dtfc, DateTimeFactCollector)
    assert dtfc.name == 'date_time'
    assert dtfc._fact_ids == set()


# Generated at 2022-06-13 02:41:36.955101
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import pytest

    c = DateTimeFactCollector()
    assert isinstance(c.collect(), dict)

# Generated at 2022-06-13 02:41:38.400295
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector()
    dt_facts = date_time_facts.collect()
    assert isinstance(dt_facts, dict)
    assert isinstance(dt_facts['date_time'], dict)

# Generated at 2022-06-13 02:41:45.400314
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    result = dt.collect()

    # confirm that certain fields are in the output
    assert result is not None
    assert 'date_time' in result
    assert 'date' in result['date_time']
    assert 'epoch' in result['date_time']
    assert 'time' in result['date_time']
    assert 'tz' in result['date_time']
    assert 'year' in result['date_time']
    assert 'month' in result['date_time']
    assert 'day' in result['date_time']

# Generated at 2022-06-13 02:41:52.474736
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time = DateTimeFactCollector()
    date_time_dict = date_time.collect(None, None)

    # The epoch value is returned as a float
    assert type(float(date_time_dict['date_time']['epoch'])) is float

# Generated at 2022-06-13 02:41:56.701818
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect()
    assert isinstance(date_time_facts, dict)
    assert 'date_time' in date_time_facts

# Generated at 2022-06-13 02:42:03.419202
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    result = fact_collector.collect()
    assert result['date_time']
    assert result['date_time']['year']
    assert result['date_time']['month']
    assert result['date_time']['weekday']
    assert result['date_time']['weekday_number']
    assert result['date_time']['weeknumber']
    assert result['date_time']['day']
    assert result['date_time']['hour']
    assert result['date_time']['minute']
    assert result['date_time']['second']
    assert result['date_time']['epoch']
    assert result['date_time']['epoch_int']
    assert result['date_time']['date']
   

# Generated at 2022-06-13 02:42:03.867231
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    pass

# Generated at 2022-06-13 02:42:14.792753
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import time
    import datetime
    # Since we can't mock time using this class, we need to test essentially a
    # single item
    dtf = DateTimeFactCollector()
    epoch_ts = time.time()

    facts_dict = dtf.collect()

    now = datetime.datetime.fromtimestamp(epoch_ts)

    assert(facts_dict['date_time']['year'] == now.strftime('%Y'))
    assert(facts_dict['date_time']['month'] == now.strftime('%m'))
    assert(facts_dict['date_time']['weekday'] == now.strftime('%A'))
    assert(facts_dict['date_time']['weekday_number'] == now.strftime('%w'))

# Generated at 2022-06-13 02:42:27.612819
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Test DateTimeFactCollector.collect"""
    fact_collector = DateTimeFactCollector()
    expected_facts_dict = {}

# Generated at 2022-06-13 02:42:29.967727
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    result = dtf.collect()
    assert type(result) is dict

# Generated at 2022-06-13 02:42:33.030197
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """ Unit test for method collect of class DateTimeFactCollector """

    def DateTimeFactCollector_collect():
        """ Unit Test function """
        dtObject = DateTimeFactCollector()
        dtObject.collect()
        return None

    # Call the DateTimeFactCollector.collect() method method
    DateTimeFactCollector_collect()
    return None

# Generated at 2022-06-13 02:42:41.924450
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    def test_data(target_obj, test_data):
        facts_dict = target_obj.collect()

        for key in test_data:
            assert key in facts_dict
            assert facts_dict[key] == test_data[key]

    # testing datetime values

# Generated at 2022-06-13 02:42:48.302685
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test data
    now = datetime.datetime.now()
    utcnow = datetime.datetime.utcnow()
    epoch_ts = time.time()

    # Create an object of DateTimeFactCollector
    fact_collector = DateTimeFactCollector()
    collected_facts = fact_collector.collect()

    # Check collected facts
    assert collected_facts['date_time']['year'] == now.strftime('%Y')
    assert collected_facts['date_time']['month'] == now.strftime('%m')
    assert collected_facts['date_time']['weekday'] == now.strftime('%A')
    assert collected_facts['date_time']['weekday_number'] == now.strftime('%w')

# Generated at 2022-06-13 02:43:00.318502
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Test that selecting from the date_time collector returns expected facts.
    date_time only contains a single fact, "date_time", that contains all of
    the date and time related facts.

    The date_time fact returns all facts in a dictionary, so we should be able
    to check the value in each key for testability.
    '''
    class FakeModule:
        def __init__(self):
            self.params = {}
    fake_module = FakeModule()
    fake_module.params = {}
    dtf = DateTimeFactCollector(fake_module)
    dtf.collect()
    collected_facts = dtf.get_facts()
    assert collected_facts == {}
    collected_facts = dtf.get_facts(['date_time'])
    # We should get back the expected number of facts
   

# Generated at 2022-06-13 02:43:01.260157
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_object = DateTimeFactCollector()
    assert test_object

# Generated at 2022-06-13 02:43:04.224282
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    datetime_facts_dict = collector.collect()
    assert 'date_time' in datetime_facts_dict
    assert 'day' in datetime_facts_dict['date_time']

# Generated at 2022-06-13 02:43:05.835504
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_instance = DateTimeFactCollector()
    date_time_instance.collect()


# Generated at 2022-06-13 02:43:12.807314
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    This method tests the method collect of DateTimeFactCollector
    DateTimeFactCollector calls strftime on the result of datetime.datetime.fromtimestamp(), which itself
    calls gmtime(3) or localtime(3). It then relies on those functions to format the date correctly.
    Because of this, the test does not check the validity of the date, but rather the fact that the
    values are non empty.
    """
    dt = DateTimeFactCollector()
    collected_facts = {}

# Generated at 2022-06-13 02:43:15.708797
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
  d = DateTimeFactCollector()
  assert d.collect()['date_time']['hour'] == time.strftime('%H')


# Generated at 2022-06-13 02:43:25.875874
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    collected = date_time_fact_collector.collect()

    assert 'date_time' in collected
    assert isinstance(collected['date_time'], dict)
    assert len(collected['date_time']) > 0

    for key, value in collected['date_time'].items():
        assert isinstance(value, str)

        if key in ['year', 'month', 'weekday', 'weekday_number', 'weeknumber',
                    'day', 'hour', 'minute', 'second', 'epoch']:
            assert len(value) >= 2
        elif key in ['iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short']:
            assert len(value) > 2

# Generated at 2022-06-13 02:43:28.614751
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    datetime_obj = DateTimeFactCollector()
    obj = datetime_obj.collect()
    return obj

# Generated at 2022-06-13 02:43:30.782616
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_factCollector = DateTimeFactCollector()
    date_time_factCollector.collect()


# Generated at 2022-06-13 02:43:40.831017
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Test for DateTimeFactCollector.
    """
    result_dict = DateTimeFactCollector().collect()
    assert 'date_time' in result_dict
    assert result_dict['date_time']['year'] != ''
    assert result_dict['date_time']['month'] != ''
    assert result_dict['date_time']['weekday'] != ''
    assert result_dict['date_time']['weekday_number'] != ''
    assert result_dict['date_time']['weeknumber'] != ''
    assert result_dict['date_time']['day'] != ''
    assert result_dict['date_time']['hour'] != ''
    assert result_dict['date_time']['minute'] != ''
    assert result_dict['date_time']['second'] != ''

# Generated at 2022-06-13 02:43:57.503051
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
    from ansible.module_utils.facts.collectors.base import BaseFactCollector

    # Create instance of DateTimeFactCollector
    dt_object = DateTimeFactCollector()

    # Assert instance of BaseFactCollector
    assert isinstance(dt_object, BaseFactCollector)

    # Assert value of instance attribute name
    assert dt_object.name == 'date_time'

    # Assert type of instance attribute name
    assert isinstance(dt_object.name, str)

    # Assert type of instance attribute _fact_ids
    assert isinstance(dt_object._fact_ids, set)

    # Assert not equal to empty set
   

# Generated at 2022-06-13 02:44:05.390884
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:44:06.960515
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    assert date_time_fact_collector.collect()

# Generated at 2022-06-13 02:44:08.380991
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc.collect()


# Generated at 2022-06-13 02:44:14.275106
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # on windows it is possible for the epoch to be tracked to less
    # precision than on other platforms, allow for the possiblity of the
    # microsecond portion of the time to be zero.
    # note: no unit tests available on windows, use a different OS to test
    #       this functionality
    epoch_ts = time.time()
    if (int(epoch_ts) - epoch_ts) == 0.0:
        epoch_ts = int(epoch_ts)
    dtfc = DateTimeFactCollector()
    ret = dtfc.collect()
    assert ret['date_time']['epoch'] == str(int(epoch_ts))
    assert ret['date_time']['epoch_int'] == str(int(epoch_ts))

# Generated at 2022-06-13 02:44:19.337524
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    dt_facts = dtf.collect()
    assert (isinstance(dt_facts['date_time']['epoch_int'], str))
    assert (int(dt_facts['date_time']['epoch_int']) > 1490000000)


# Generated at 2022-06-13 02:44:22.074116
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_collector.collect()
    assert 'date_time' in date_time_collector.collect()

# Generated at 2022-06-13 02:44:31.360526
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    result = date_time_fact_collector.collect()

# Generated at 2022-06-13 02:44:33.100154
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    datetimefc = DateTimeFactCollector({}, None)
    facts_dict = datetimefc.collect()
    assert 'date_time' in facts_dict
    assert 'year' in facts_dict['date_time']

# Generated at 2022-06-13 02:44:33.989162
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector.collect()

# Generated at 2022-06-13 02:45:00.017766
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    ansible_facts = fact_collector.collect()
    assert type(ansible_facts) == dict
    assert type(ansible_facts['date_time']) == dict
    assert type(ansible_facts['date_time']['year']) == str
    assert type(ansible_facts['date_time']['month']) == str
    assert type(ansible_facts['date_time']['weekday']) == str
    assert type(ansible_facts['date_time']['weekday_number']) == str
    assert type(ansible_facts['date_time']['weeknumber']) == str
    assert type(ansible_facts['date_time']['day']) == str

# Generated at 2022-06-13 02:45:10.584318
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # GIVEN: A DateTimeFactCollector instance
    date_fact_collector = DateTimeFactCollector()
    expected_datetime = datetime.datetime.utcfromtimestamp(time.time())

    # WHEN: We execute the collect method
    result = date_fact_collector.collect()

    # THEN: We should get a dictionary with the expected data
    assert 'date_time' in result
    result_date_time = result['date_time']
    assert 'month' in result_date_time
    assert 'day' in result_date_time
    assert 'year' in result_date_time
    assert 'hour' in result_date_time
    assert 'minute' in result_date_time
    assert 'second' in result_date_time
    assert 'epoch' in result_date_time
   

# Generated at 2022-06-13 02:45:13.761810
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    collected_facts = collector.collect()
    assert type(collected_facts['date_time']) is dict
    for key in collected_facts['date_time'].keys():
        assert type(collected_facts['date_time'][key]) is str

# Generated at 2022-06-13 02:45:18.090266
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    date_time_facts = dtfc.collect()
    assert date_time_facts is not None
    assert date_time_facts.get('date_time') is not None
    assert date_time_facts['date_time'].get('hour') is not None

# Generated at 2022-06-13 02:45:26.761138
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Unit test for method collect of class DateTimeFactCollector"""
    # Should build the expected result

# Generated at 2022-06-13 02:45:28.777109
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Return the current date and time facts.
    """
    dtfc = DateTimeFactCollector()
    dtfc.collect()

# Generated at 2022-06-13 02:45:30.917738
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()
    assert date_time_facts is not None
    assert date_time_facts['date_time'] is not None

# Generated at 2022-06-13 02:45:38.493185
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    dt.collect()
    assert dt.name == "date_time"
    assert dt._fact_ids == set()
    assert dt.collect()['date_time']['weekday'] == time.strftime("%A")
    assert dt.collect()['date_time']['tz_dst'] == time.tzname[1]


# Generated at 2022-06-13 02:45:46.949614
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    module = None
    collected_facts = None

    dtf = DateTimeFactCollector()
    facts_dict = dtf.collect(module, collected_facts)

    assert 'epoch' in facts_dict['date_time']
    assert 'epoch_int' in facts_dict['date_time']
    assert 'iso8601' in facts_dict['date_time']
    assert 'iso8601_basic' in facts_dict['date_time']
    assert 'iso8601_basic_short' in facts_dict['date_time']
    assert 'iso8601_micro' in facts_dict['date_time']
    assert 'tz' in facts_dict['date_time']
    assert 'tz_dst' in facts_dict['date_time']
    assert 'tz_offset' in facts_dict['date_time']

# Generated at 2022-06-13 02:45:58.266633
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dateTimeModule = DateTimeFactCollector()
    dateTimeDict = dateTimeModule.collect()
    dateTimeFacts = dateTimeDict['date_time']
    assert 'weeknumber' in dateTimeFacts
    assert 'day' in dateTimeFacts
    assert 'epoch' in dateTimeFacts
    assert 'iso8601' in dateTimeFacts
    assert 'weekday_number' in dateTimeFacts
    assert 'month' in dateTimeFacts
    assert 'iso8601_basic_short' in dateTimeFacts
    assert 'year' in dateTimeFacts
    assert 'tz_offset' in dateTimeFacts
    assert 'weekday' in dateTimeFacts
    assert 'date' in dateTimeFacts
    assert 'iso8601_micro' in dateTimeFacts

# Generated at 2022-06-13 02:46:36.597168
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # We import the module directly to test its public method collect
    from ansible.module_utils.facts import datetime_facts
    fact_collector = datetime_facts.DateTimeFactCollector()
    facts_dict = fact_collector.collect()
    assert type(facts_dict) is dict
    assert 'date_time' in facts_dict
    assert type(facts_dict['date_time']) is dict
    assert 'year' in facts_dict['date_time']
    assert type(facts_dict['date_time']['year']) is str
    assert 'month' in facts_dict['date_time']
    assert type(facts_dict['date_time']['month']) is str
    assert 'weekday' in facts_dict['date_time']

# Generated at 2022-06-13 02:46:47.065406
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    This is deliberately a standalone function so that it can be used
    by the python 2 to python 3 fact testing framework.
    '''
    date_obj = datetime.date(2016, 8, 31)
    time_obj = datetime.time(17, 0, 36)
    dt_obj = datetime.datetime.combine(date_obj, time_obj)
    epoch_ts = dt_obj.timestamp()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)
    utc_tz = datetime.timezone.utc
    dt_obj_utc = dt_obj.replace(tzinfo=utc_tz)
    date_time_facts = {}
   

# Generated at 2022-06-13 02:46:54.092499
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Use the 'fixtures/date_time_facts.txt' file to answer any query that the
    # AnsibleModule might have, instead of actually querying the system.
    # The file is in the format of '{{ "foo": "bar" }}'.
    DateTimeFactCollector.FACT_CACHE_FILENAME = 'fixtures/date_time_facts.txt'

    # Create the collector object.
    date_time_collector = DateTimeFactCollector()

    # Create the module object.
    module_obj = []

    # Collect facts.
    collected_facts = date_time_collector.collect(module_obj)
    collected_facts_dict = collected_facts['date_time']

    # Assert that the collected facts are what we expect.
    assert type(collected_facts) == dict

# Generated at 2022-06-13 02:47:03.941180
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts = DateTimeFactCollector().collect()
    assert 'date_time' in facts
    assert 'year' in facts['date_time']
    assert 'month' in facts['date_time']
    assert 'weekday' in facts['date_time']
    assert 'weekday_number' in facts['date_time']
    assert 'weeknumber' in facts['date_time']
    assert 'day' in facts['date_time']
    assert 'hour' in facts['date_time']
    assert 'minute' in facts['date_time']
    assert 'second' in facts['date_time']
    assert 'epoch' in facts['date_time']
    assert 'epoch_int' in facts['date_time']
    assert 'date' in facts['date_time']
    assert 'time' in facts['date_time']

# Generated at 2022-06-13 02:47:04.859127
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:47:13.687845
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_fact_collect_inst = DateTimeFactCollector()
    result = dt_fact_collect_inst.collect()
    assert result
    assert 'date_time' in result
    assert result['date_time']['year']
    assert result['date_time']['month']
    assert result['date_time']['weekday']
    assert result['date_time']['weekday_number']
    assert result['date_time']['weeknumber']
    assert result['date_time']['day']
    assert result['date_time']['hour']
    assert result['date_time']['minute']
    assert result['date_time']['second']
    assert result['date_time']['epoch']
    assert result['date_time']['epoch_int']
   

# Generated at 2022-06-13 02:47:22.919480
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    # print("date_time_fact_collector.collect() = ", date_time_fact_collector.collect())
    # print("type(date_time_fact_collector.collect()) = ", type(date_time_fact_collector.collect()))
    # print("date_time_fact_collector.collect().keys() = ", date_time_fact_collector.collect().keys())
    # print("type(date_time_fact_collector.collect().keys() = ", type(date_time_fact_collector.collect().keys()))
    # print("date_time_fact_collector.collect().values() = ", date_time_fact_collector.collect().values())
    # print("type(date_time_fact_collector.

# Generated at 2022-06-13 02:47:26.082457
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts_dict = {}
    result = collector.collect(collected_facts=facts_dict)
    print(result)

if __name__ == '__main__':
    test_DateTimeFactCollector_collect()

# Generated at 2022-06-13 02:47:37.713784
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts = collector.collect(None, None)
    assert facts['date_time']['year'] is not None
    assert facts['date_time']['month'] is not None
    assert facts['date_time']['weekday'] is not None
    assert facts['date_time']['weekday_number'] is not None
    assert facts['date_time']['weeknumber'] is not None
    assert facts['date_time']['day'] is not None
    assert facts['date_time']['hour'] is not None
    assert facts['date_time']['minute'] is not None
    assert facts['date_time']['second'] is not None
    assert facts['date_time']['epoch'] is not None

# Generated at 2022-06-13 02:47:47.605268
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts = DateTimeFactCollector().collect()

    assert facts['date_time']['date']
    assert facts['date_time']['day']
    assert facts['date_time']['epoch']
    assert facts['date_time']['epoch_int']
    assert facts['date_time']['hour']
    assert facts['date_time']['iso8601']
    assert facts['date_time']['iso8601_basic']
    assert facts['date_time']['iso8601_basic_short']
    assert facts['date_time']['iso8601_micro']
    assert facts['date_time']['minute']
    assert facts['date_time']['month']
    assert facts['date_time']['second']

# Generated at 2022-06-13 02:48:48.548604
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_obj = DateTimeFactCollector()
    result = dt_obj.collect()
    assert isinstance(result, dict) and result['date_time']['epoch'].isdigit()

# Generated at 2022-06-13 02:48:57.393172
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # unit test for method collect of class DateTimeFactCollector
    dtf = DateTimeFactCollector()
    collected_facts = {}
    collected_facts = dtf.collect(collected_facts)
    assert isinstance(collected_facts['date_time'], (dict))
    assert isinstance(collected_facts['date_time']['year'], (str))
    assert isinstance(collected_facts['date_time']['month'], (str))
    assert isinstance(collected_facts['date_time']['weekday'], (str))
    assert isinstance(collected_facts['date_time']['weekday_number'], (str))
    assert isinstance(collected_facts['date_time']['weeknumber'], (str))

# Generated at 2022-06-13 02:49:08.924404
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect()['date_time']
    assert type(date_time_facts['epoch']) is str
    assert type(date_time_facts['epoch_int']) is str
    assert type(date_time_facts['date']) is str
    assert type(date_time_facts['time']) is str
    assert type(date_time_facts['tz']) is str
    assert type(date_time_facts['tz_dst']) is str
    assert type(date_time_facts['tz_offset']) is str
    assert type(date_time_facts['year']) is str
    assert type(date_time_facts['month']) is str

# Generated at 2022-06-13 02:49:18.632058
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    d = dt.collect()
    assert isinstance(d, dict)
    assert d['date_time']['year'] == time.strftime('%Y')
    assert d['date_time']['month'] == time.strftime('%m')
    assert d['date_time']['weekday'] == time.strftime('%A')
    assert d['date_time']['weekday_number'] == time.strftime('%w')
    assert d['date_time']['weeknumber'] == time.strftime('%W')
    assert d['date_time']['day'] == time.strftime('%d')
    assert d['date_time']['hour'] == time.strftime('%H')

# Generated at 2022-06-13 02:49:27.820158
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Mock module_utils/facts/collector.py module
    import sys
    import ansible.module_utils.facts.collector

    collected_facts = ansible.module_utils.facts.collector.CollectedFacts()

    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect(collected_facts)

    # Validate date_time facts
    assert date_time_facts['date_time']['day'] == time.strftime("%d")
    assert date_time_facts['date_time']['date'] == time.strftime("%Y-%m-%d")
    assert date_time_facts['date_time']['time'] == time.strftime("%H:%M:%S")
    assert date_time_facts

# Generated at 2022-06-13 02:49:38.763729
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Test the collect method of DateTimeFactCollector.
    """
    # Mock dependencies
    import ansible.module_utils.facts.collector
    DateTimeFactCollector.get_module_utils_facts_collector = lambda self: ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.BaseFactCollector.get_file_content = lambda self, filename: 'mock_content'
    ansible.module_utils.facts.collector.BaseFactCollector.get_file_lines = lambda self, filename: ['mock_line1', 'mock_line2']

    date_time_fact_collector = DateTimeFactCollector()


# Generated at 2022-06-13 02:49:50.684499
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    ##############
    # Setup
    ##############
    # Initialize DateTimeFactCollector class object
    DateTimeFactCollector_obj = DateTimeFactCollector()
    # Initialize time.time() before calling DateTimeFactCollector.collect()
    time_time_obj = time.time()
    # Initialize datetime.datetime.fromtimestamp() before calling DateTimeFactCollector.collect()
    datetime_datetime_fromtimestamp_obj = datetime.datetime.fromtimestamp(time_time_obj)
    # Store the expected fact dictionary in a variable

# Generated at 2022-06-13 02:50:01.063260
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import sys
    import platform
    import ansible.utils.pycompat as pycompat
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import CollectorExecutionError
    from ansible.module_utils._text import to_native

    # initialization
    p = platform.system()
    if p == 'Windows':
        import ntpath
        sys.modules['ntpath'] = ntpath
    else:
        import posixpath
        sys.modules['posixpath'] = posixpath
    dtfc = DateTimeFactCollector()
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')

# Generated at 2022-06-13 02:50:12.386531
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test for error message if module is not passed
    dsc = DateTimeFactCollector()
    result = dsc.collect()

# Generated at 2022-06-13 02:50:20.654740
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    ans = dtfc.collect()

    keys = ['date_time']
    assert set(ans.keys()) == set(keys), 'ans should have only these keys: %r but it had: %r' % (keys, ans.keys())
