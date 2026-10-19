

# Generated at 2022-06-13 02:40:54.994843
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:41:02.231514
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector import MockFile

    mocked_module = MockModule()
    mocked_module.params = dict()
    mocked_module.params['gather_subset'] = ['all']
    mocked_module.params['gather_timeout'] = 1
    mocked_module.facts = ModuleFacts(mocked_module)

    datetime_facts_collector = DateTimeFactCollector(mocked_module)
    datetime_facts = datetime_facts_collector.collect()
    return_code = datetime_facts.get('returncode', None)

    assert return_code == 0, 'date_time facts could not be collected'

    # Unit test assertion


# Generated at 2022-06-13 02:41:12.029875
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    from ansible.module_utils.facts.collector.date_time import DateTimeFactCollector

    date_time_fact_collector = DateTimeFactCollector()

    result_dtc_collect = date_time_fact_collector.collect()


# Generated at 2022-06-13 02:41:15.574224
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    # Just test we get some data.
    response = dtfc.collect()
    assert(response['date_time'])

# Generated at 2022-06-13 02:41:24.281430
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    result = dtfc.collect()
    assert 'date_time' in result
    assert result['date_time']['year'] == datetime.datetime.now().strftime('%Y')
    assert result['date_time']['month'] == datetime.datetime.now().strftime('%m')
    assert result['date_time']['weekday'] == datetime.datetime.now().strftime('%A')
    assert result['date_time']['weekday_number'] == datetime.datetime.now().strftime('%w')
    assert result['date_time']['weeknumber'] == datetime.datetime.now().strftime('%W')
    assert result['date_time']['day'] == datetime.datetime.now().str

# Generated at 2022-06-13 02:41:30.655014
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Set up arguments
    module = ""
    # set up Test object
    test_obj = DateTimeFactCollector(module=module)
    # Run test
    test = test_obj.collect()
    # Check result
    assert test['date_time']
    assert test['date_time']['epoch']
    assert test['date_time']['epoch_int']
    assert test['date_time']['iso8601']
    assert test['date_time']['iso8601_basic']
    assert test['date_time']['iso8601_basic_short']
    assert test['date_time']['iso8601_micro']
    assert test['date_time']['date']
    assert test['date_time']['hour']
    assert test['date_time']['minute']

# Generated at 2022-06-13 02:41:38.082502
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    a = DateTimeFactCollector()
    res = a.collect()
    assert len(res['date_time']) > 0
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
    assert 'date' in res['date_time']
    assert 'time' in res['date_time']

# Generated at 2022-06-13 02:41:45.694838
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    collected_facts = fact_collector.collect()
    assert "date_time" in collected_facts
    collected_date_time_info = collected_facts["date_time"]
    assert "date" in collected_date_time_info
    assert "time" in collected_date_time_info
    assert "hour" in collected_date_time_info
    assert "minute" in collected_date_time_info
    assert "epoch" in collected_date_time_info
    assert "epoch_int" in collected_date_time_info

# Generated at 2022-06-13 02:41:47.996362
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    collected_facts = fact_collector.collect()

    assert isinstance(collected_facts['date_time'], dict)

# Generated at 2022-06-13 02:41:56.460731
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # FactCollector class method collect should always return a dictionary.
    # It collects facts by calling platform specific code.  For this test,
    # we will use mock data.
    dtfc = DateTimeFactCollector()
    dtfc._get_time_parameters = lambda : {'epoch_ts': 1428229010.0,
                                          'now' : datetime.datetime(2015,4,10,6,23,30),
                                          'utcnow' : datetime.datetime(2015,4,10,13,23,30)}
    dtfc._get_timestamp_from_epoch = lambda epoch_ts: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch_ts))
    dtfc._interpret_tim

# Generated at 2022-06-13 02:42:10.369716
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtc = DateTimeFactCollector()
    l = dtc.collect()
    assert isinstance(l["date_time"]["year"], str)
    assert isinstance(l["date_time"]["month"], str)
    assert isinstance(l["date_time"]["weekday"], str)
    assert isinstance(l["date_time"]["weekday_number"], str)
    assert isinstance(l["date_time"]["weeknumber"], str)
    assert isinstance(l["date_time"]["day"], str)
    assert isinstance(l["date_time"]["hour"], str)
    assert isinstance(l["date_time"]["minute"], str)
    assert isinstance(l["date_time"]["second"], str)

# Generated at 2022-06-13 02:42:14.115531
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # create instance of class DateTimeFactCollector
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    # test if date_time_facts is not empty
    assert date_time_facts != {}

# Generated at 2022-06-13 02:42:15.527317
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    assert DateTimeFactCollector.collect()

# Generated at 2022-06-13 02:42:18.881234
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector()
    date_time_facts.collect()

# Generated at 2022-06-13 02:42:21.605721
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()
    assert date_time_facts['date_time']['year']

# Generated at 2022-06-13 02:42:30.568036
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create instance of DateTimeFactCollector
    date_time_collector = DateTimeFactCollector()
    # Get fact dictionary
    fact = date_time_collector.collect()
    assert 'date_time' in fact
    # Get date_time fact dictionary
    date_time = fact['date_time']
    assert date_time['year']
    assert date_time['month']
    assert date_time['weekday']
    assert date_time['day']
    assert date_time['hour']
    assert date_time['minute']
    assert date_time['second']
    assert date_time['epoch']
    assert date_time['epoch_int']
    assert date_time['date']
    assert date_time['time']
    assert date_time['iso8601_micro']

# Generated at 2022-06-13 02:42:37.257907
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # We are only interested in the 'date_time' key from the returned dict
    actual = DateTimeFactCollector().collect()['date_time']

# Generated at 2022-06-13 02:42:46.855474
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Define a class for testing with mocks
    class MyDateTimeFactCollector(DateTimeFactCollector):
        def __init__(self):
            self.epoch_ts = int(time.time())
            self.utcnow = datetime.datetime.utcfromtimestamp(self.epoch_ts)

        def _get_timestamp(self):
            return self.epoch_ts

        def _get_utc_timestamp(self):
            return self.utcnow

    my_collector = MyDateTimeFactCollector()

# Generated at 2022-06-13 02:42:52.272073
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    c = DateTimeFactCollector()
    f = c.collect()
    assert 'date_time' in f
    assert type(f['date_time']) is dict
    assert 'tz_dst' in f['date_time']
    assert f['date_time']['tz_dst'] is not None

# Generated at 2022-06-13 02:42:54.361375
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert result['date_time']['iso8601_basic'] != ''

# Generated at 2022-06-13 02:43:03.241049
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    assert DateTimeFactCollector.collect

# Generated at 2022-06-13 02:43:06.716336
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Create a DateTimeFactCollector and call the collect method
    fact_collector = DateTimeFactCollector()
    result = fact_collector.collect()

    # Check that result is as expected
    assert 'date_time' in result
    assert 'year' in result['date_time']

# Generated at 2022-06-13 02:43:07.535670
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:43:10.065832
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_1 = DateTimeFactCollector()
    date_2 = date_1.collect()
    date_3 = date_1.collect()
    assert date_2['date_time'] == date_3['date_time']

# Generated at 2022-06-13 02:43:19.641086
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # testing for method collect of class DateTimeFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import date_time
    date_time_col = date_time.DateTimeFactCollector
    date_time_col.collect()
    c = Collector(module=None, facts={})
    c.add_collector(date_time_col)
    facts = c.collect()
    assert 'date_time' in facts
    assert len(date_time_col._fact_ids) == 0

# Generated at 2022-06-13 02:43:27.770926
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    assert fact_collector._collect_only_if_required is False
    assert fact_collector.name == 'date_time'
    assert fact_collector._fact_ids == set()

    result = fact_collector.collect()
    assert result is not None
    assert result['date_time'] is not None
    date_time_facts = result['date_time']
    assert date_time_facts['year'] == time.strftime("%Y")
    assert date_time_facts['month'] == time.strftime("%m")
    assert date_time_facts['weekday'] == time.strftime("%A")
    assert date_time_facts['weekday_number'] == time.strftime("%w")

# Generated at 2022-06-13 02:43:38.509692
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

# Generated at 2022-06-13 02:43:50.443173
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_module = None
    test_collect_facts = None
    test_facts_dict = {}
    # Setup test variables
    test_date_time = {}
    test_epoch = datetime.datetime.now().strftime('%s')
    test_yr = datetime.datetime.now().strftime('%Y')
    test_mo = datetime.datetime.now().strftime('%m')
    test_wk = datetime.datetime.now().strftime('%W')
    test_day = datetime.datetime.now().strftime('%d')
    test_hr = datetime.datetime.now().strftime('%H')
    test_mi = datetime.datetime.now().strftime('%M')

# Generated at 2022-06-13 02:43:55.782155
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
  dt_fc = DateTimeFactCollector()
  res = dt_fc.collect()
  assert(res['date_time']['iso8601_micro'] == datetime.datetime.utcfromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
  assert(float(res['date_time']['epoch']) != 0)

# Generated at 2022-06-13 02:44:00.769407
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dc = DateTimeFactCollector()
    facts = dc.collect()
    assert(facts['date_time']['month'] == datetime.datetime.now().strftime("%m"))

# Generated at 2022-06-13 02:44:14.580863
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Example converted from: https://unix.stackexchange.com/questions/53212/what-is-the-difference-between-localtime-and-epoch
    # I ran "date -u" and got the time "Tue Oct 20 21:49:20 UTC 2015"
    # Then I ran "date -d @1445377760" and got "Tue Oct 20 22:49:20 UTC 2015"
    epoch = 1445377760.0
    expected_tz_offset = "+0000"

    # Set up the fake module object
    tmp_module = type('FakeModule', (object,), {})
    module = tmp_module()
    # Set up the fake collector object

# Generated at 2022-06-13 02:44:19.574236
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collecter = DateTimeFactCollector()
    collected_facts = collecter.collect()
    assert isinstance(collected_facts, dict)
    assert collected_facts.get('date_time') is not None
    assert isinstance(collected_facts['date_time'], dict)



# Generated at 2022-06-13 02:44:24.397309
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # date_time_facts collect test
    test_dt = DateTimeFactCollector()
    test_dict = test_dt.collect()
    assert test_dict['date_time'] is not None
    assert test_dict['date_time']['hour'] is not None
    assert test_dict['date_time']['minute'] is not None

# Generated at 2022-06-13 02:44:32.716717
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import datetime
    import time
    mock_module = None
    mock_collected_facts = None

# Generated at 2022-06-13 02:44:41.973066
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    date_time_facts = fact_collector.collect()['date_time']
    assert(date_time_facts['year'])
    assert(date_time_facts['month'])
    assert(date_time_facts['weekday'])
    assert(date_time_facts['weekday_number'])
    assert(date_time_facts['weeknumber'])
    assert(date_time_facts['day'])
    assert(date_time_facts['hour'])
    assert(date_time_facts['minute'])
    assert(date_time_facts['second'])
    assert(date_time_facts['epoch'])
    assert(date_time_facts['epoch_int'])
    assert(date_time_facts['date'])
   

# Generated at 2022-06-13 02:44:47.190769
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Unit test to verify values returned from method collect

    valid_facts = {}

    # Create instance of DateTimeFactCollector
    dtfc = DateTimeFactCollector()
    # Execute method collect
    result = dtfc.collect()

    if result['date_time']['year'] != '':
        valid_facts['date_time'] = result['date_time']

    assert valid_facts == result

# Generated at 2022-06-13 02:44:57.423444
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    from ansible.module_utils.facts import FactManager

    test_fact_collector = get_collector_instance('DateTimeFactCollector')
    assert(isinstance(test_fact_collector, DateTimeFactCollector))
    assert(len(test_fact_collector._fact_ids) == 0)

    test_fact_collector.collect()

    assert(len(test_fact_collector._fact_ids) == 18)



# Generated at 2022-06-13 02:45:00.653103
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    df = DateTimeFactCollector()
    result = df.collect()
    
    epoch = int(time.time())
    assert result['date_time']['epoch'] == str(epoch)
    assert result['date_time']['epoch_int'] == str(epoch)

# Generated at 2022-06-13 02:45:10.699939
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_fc = DateTimeFactCollector()
    result = dt_fc.collect()
    assert isinstance(result, dict)
    assert len(result) == 1
    assert isinstance(result['date_time'], dict)
    assert len(result['date_time']) > 0
    assert isinstance(result['date_time']['epoch'], str)
    assert isinstance(float(result['date_time']['epoch']), float)
    assert isinstance(result['date_time']['epoch_int'], str)
    assert isinstance(int(result['date_time']['epoch_int']), int)
    assert isinstance(result['date_time']['iso8601_micro'], str)

# Generated at 2022-06-13 02:45:17.694738
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Returns a dictionary where keys are date_time related keys and
    values are the string representation of the value.
    """
    collector = DateTimeFactCollector()
    facts = collector.collect()
    assert isinstance(facts['date_time']['year'], str)
    assert facts['date_time']['year'].isdigit()
    assert isinstance(facts['date_time']['month'], str)
    assert facts['date_time']['month'].isdigit()
    assert isinstance(facts['date_time']['weekday'], str)
    assert isinstance(facts['date_time']['weekday_number'], str)
    assert facts['date_time']['weekday_number'].isdigit()

# Generated at 2022-06-13 02:45:39.996690
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Regardless of any value of module, collected_facts, this method always returns the same result.
    module = object()
    collected_facts = {}

    dt = DateTimeFactCollector(module=module, collected_facts=collected_facts)
    result = dt.collect()

    # Check the result
    assert isinstance(result, dict)
    assert len(result) == 1
    assert isinstance(result['date_time'], dict)

# Generated at 2022-06-13 02:45:43.237747
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_test = DateTimeFactCollector()
    date_time_test_result = date_time_test.collect()
    assert date_time_test_result.has_key('date_time'), "test_DateTimeFactCollector_collect() has no key date_time"

# Generated at 2022-06-13 02:45:49.694365
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect({"_ansible_version": "2.5.5"})
    assert 'date_time' in date_time_facts
    assert 'year' in date_time_facts['date_time']
    assert 'month' in date_time_facts['date_time']
    assert 'day' in date_time_facts['date_time']
    assert 'date' in date_time_facts['date_time']
    assert 'weekday' in date_time_facts['date_time']
    assert 'weekday_number' in date_time_facts['date_time']
    assert 'weeknumber' in date_time_facts['date_time']

# Generated at 2022-06-13 02:46:01.702436
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()['date_time']
    assert isinstance(date_time_facts['year'], str)
    assert isinstance(date_time_facts['month'], str)
    assert isinstance(date_time_facts['weekday'], str)
    assert isinstance(date_time_facts['weekday_number'], str)
    assert isinstance(date_time_facts['weeknumber'], str)
    assert isinstance(date_time_facts['day'], str)
    assert isinstance(date_time_facts['hour'], str)
    assert isinstance(date_time_facts['minute'], str)
    assert isinstance(date_time_facts['second'], str)


# Generated at 2022-06-13 02:46:06.162272
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    ansible_facts = {}
    dtfc.collect(collected_facts=ansible_facts)
    # Hard to test since no comparisons to an expected value
    # Just verify we can get through the whole routine
    assert(True)

# Generated at 2022-06-13 02:46:14.097484
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # DateTimeFactCollector() method collect. It can fail if
    # datetime.datetime.fromtimestamp(time.time()) method return an invalid
    # string.
    dtfc = DateTimeFactCollector()
    date_time_facts_dict = dtfc.collect()['date_time']
    assert date_time_facts_dict['year']
    assert date_time_facts_dict['month']
    assert date_time_facts_dict['weekday']
    assert date_time_facts_dict['weekday_number']
    assert date_time_facts_dict['weeknumber']
    assert date_time_facts_dict['day']
    assert date_time_facts_dict['hour']
    assert date_time_facts_dict['minute']
    assert date_time_facts_dict['second']

# Generated at 2022-06-13 02:46:15.134512
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:46:17.068393
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_collector = DateTimeFactCollector()
    assert 'date_time' in test_collector.collect()

# Generated at 2022-06-13 02:46:21.781267
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect(None, None)

    assert date_time_facts is not None
    assert 'date_time' in date_time_facts
    assert type(date_time_facts['date_time']) is dict

# Generated at 2022-06-13 02:46:32.701124
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create a DateTimeFactCollector object and call the method collect on its instance
    result = DateTimeFactCollector().collect()
    # Check if the result is of dictionary type
    assert isinstance(result, dict)
    # Check if the result has a key named "date_time"
    assert 'date_time' in result
    # Check if the result's "date_time" value is of dictionary type
    assert isinstance(result['date_time'], dict)
    # Check if the result's "date_time" value dictionnary has keys named :
    # year, month, weekday, weekday_number, weeknumber, day, hour, minute, second, epoch, epoch_int, date, time, iso8601_micro,
    # iso8601, iso8601_basic, iso8601_basic_short, tz, tz_d

# Generated at 2022-06-13 02:47:10.675702
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts_collector = DateTimeFactCollector()
    date_time_facts = date_time_facts_collector.collect()
    assert date_time_facts.get('date_time') is not None
    assert date_time_facts.get('date_time').get('epoch') is not None
    assert date_time_facts.get('date_time').get('epoch_int') is not None

# Generated at 2022-06-13 02:47:12.527181
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    assert date_time_collector.collect()['date_time']['epoch']

# Generated at 2022-06-13 02:47:19.122958
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    base_obj = BaseFactCollector()
    obj = DateTimeFactCollector()

    # Verifying the attributes
    assert obj.name == "date_time"
    assert obj._fact_ids == set()

    obj._module = base_obj.setup_module_object()
    obj._collect_platform_facts = base_obj._collect_platform_facts
    obj._collect_subset_facts = base_obj._collect_subset_facts
    obj.get_facts = base_obj.get_facts
    ret = obj.collect()

    assert (ret.has_key('date_time'))
    assert (ret['date_time'].has_key('epoch_int'))
    assert (ret['date_time'].has_key('date'))

# Generated at 2022-06-13 02:47:24.623048
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create a DateTimeFactCollector instance for testing
    date_time_fact_collector = DateTimeFactCollector()

    # Unit test for method DateTimeFactCollector.collect()
    collected_facts = date_time_fact_collector.collect(None, None)
    date_time_facts = collected_facts['date_time']

    # Assert that year has a value
    assert date_time_facts['year'] != '', "year is not defined"

    # Assert that month has a value
    assert date_time_facts['month'] != '', "month is not defined"

    # Assert that weekday has a value
    assert date_time_facts['weekday'] != '', "weekday is not defined"

    # Assert that weekday_number has a value
    assert date_time_facts['weekday_number']

# Generated at 2022-06-13 02:47:35.646092
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    now = datetime.datetime.utcnow()
    epoch_ts = time.time()


# Generated at 2022-06-13 02:47:46.040401
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()

    # collect facts
    facts_dict = date_time_fact_collector.collect()
    date_time_dict = facts_dict['date_time']

    # verify facts from date_time
    assert date_time_dict['epoch']        # epoch returns float or string in some non-linux environments
    assert int(date_time_dict['epoch'])   # epoch should convert to int and not raise a ValueError
    assert int(date_time_dict['epoch_int']) == int(date_time_dict['epoch'])  # epoch_int always returns integer format of epoch
    assert int(date_time_dict['year'])    # year should convert to int and not raise a ValueError
    assert int(date_time_dict['month'])  

# Generated at 2022-06-13 02:47:52.211970
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Initialize object MyCollector
    DateTimeFactCollectorObj = DateTimeFactCollector()
    # Get the result of function collect
    result = DateTimeFactCollectorObj.collect()
    # Check if result is expected
    if result['date_time']['year'] == str(datetime.datetime.now().year) and result['date_time']['tz'] == time.strftime("%Z") and result['date_time']['day'] == str(datetime.datetime.now().day):
        print("DateTimeFactCollector collect test passed")
        return True
    else:
        print("DateTimeFactCollector collect test failed")
        return False


# Generated at 2022-06-13 02:47:55.462154
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dc = DateTimeFactCollector()
    dt = dc.collect()
    assert dt['date_time']['day'] == str(datetime.datetime.now().day)

# Generated at 2022-06-13 02:48:04.045550
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:48:05.776637
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """ Test method collect of class DateTimeFactCollector"""
    date_time_facts = DateTimeFactCollector()
    date_time_facts.collect()

# Generated at 2022-06-13 02:49:14.106268
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import mock
    from ansible.module_utils.facts import default_collectors

    # patch so we can test cached results
    dtfc = DateTimeFactCollector()
    dtfc.collect = mock.Mock(return_value={'date_time':{'epoch': '12345'}})
    # collect new facts
    result = dtfc.collect()
    assert result == {'date_time': {'epoch': '12345'}}
    # clear cache and collect from cache
    dtfc.get_from_cache = mock.Mock(return_value={'date_time':{'epoch': '12345'}})
    dtfc.collect.reset_mock()
    result = dtfc.collect()
    assert not dtfc.collect.called

# Generated at 2022-06-13 02:49:24.140868
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    ansible_date_time_facts = dtfc.collect()
    assert 'date_time' in ansible_date_time_facts, 'test_DateTimeFactCollector_collect has failed!'
    assert 'epoch' in ansible_date_time_facts['date_time'], 'test_DateTimeFactCollector_collect has failed!'
    assert 'date' in ansible_date_time_facts['date_time'], 'test_DateTimeFactCollector_collect has failed!'
    assert 'time' in ansible_date_time_facts['date_time'], 'test_DateTimeFactCollector_collect has failed!'


# Generated at 2022-06-13 02:49:30.863056
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:49:32.017109
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector.collect()

# Generated at 2022-06-13 02:49:34.009006
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Not implemented yet
    pass

# Generated at 2022-06-13 02:49:37.623258
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fc = DateTimeFactCollector()
    datetime_fact = date_time_fc.collect()
    assert 'date_time' in datetime_fact, "date_time fact not collected"
    assert isinstance(datetime_fact['date_time'], dict), "date_time fact is not a dict"

# Generated at 2022-06-13 02:49:49.305335
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    result = dtfc.collect()
    assert result['date_time']
    assert result['date_time']['epoch']
    assert result['date_time']['epoch_int']
    assert result['date_time']['iso8601']
    assert result['date_time']['iso8601_micro']
    assert result['date_time']['iso8601_basic']
    assert result['date_time']['iso8601_basic_short']
    assert result['date_time']['day']
    assert result['date_time']['date']
    assert result['date_time']['month']
    assert result['date_time']['time']
    assert result['date_time']['hour']

# Generated at 2022-06-13 02:49:50.957003
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    c = DateTimeFactCollector()
    facts = c.collect()
    assert 'date_time' in facts

# Generated at 2022-06-13 02:50:01.417686
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Test DateTimeFactCollector.collect()
    """

    fact_collector = DateTimeFactCollector()
    fact = fact_collector.collect()
    assert fact_collector.name in fact
    assert fact['date_time']['iso8601_micro'] is not None
    assert fact['date_time']['iso8601'] is not None
    assert fact['date_time']['iso8601_basic'] is not None
    assert fact['date_time']['iso8601_basic_short'] is not None
    assert fact['date_time']['year'] is not None
    assert fact['date_time']['month'] is not None
    assert fact['date_time']['weekday'] is not None
    assert fact['date_time']['weekday_number'] is not None
   

# Generated at 2022-06-13 02:50:12.596889
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector.collect()['date_time']
    assert date_time_facts
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
    assert date_time_facts['iso8601_micro']
    assert date