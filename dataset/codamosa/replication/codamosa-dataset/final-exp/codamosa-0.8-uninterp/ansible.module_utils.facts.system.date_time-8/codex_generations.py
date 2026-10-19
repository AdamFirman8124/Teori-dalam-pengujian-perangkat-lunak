

# Generated at 2022-06-13 02:40:46.522005
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Test the collect method of DateTimeFactCollector."""
    c = DateTimeFactCollector()
    x = c.collect()

    # Note: at this point there is no way to test the actual
    # value of x; this test is here to assure that collect do
    # not raise exceptions

    assert isinstance(x, dict)

# Generated at 2022-06-13 02:40:51.341503
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_collector = DateTimeFactCollector()
    collected_facts = dt_collector.collect()
    assert collected_facts['date_time']['epoch'] == collected_facts['date_time']['epoch_int']
    assert len(collected_facts['date_time']['epoch_int']) == 10

# Generated at 2022-06-13 02:40:59.899249
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """date_time.collect() Test"""

    def mock_platform_system(**kwargs):
        return 'Linux'

    def mock_time_time(**kwargs):
        return 1498273804.113567

    import ansible.module_utils.facts.system.date_time
    from ansible.module_utils.facts import collector

    module = ansible.module_utils.facts.system.date_time
    collector.platform.system = mock_platform_system
    time.time = mock_time_time

    date_time_collector = module.DateTimeFactCollector()

    ret = date_time_collector.collect()

    print(ret)

    assert ret['ansible_date_time']['iso8601'] == '2017-06-24T01:23:24Z'
    assert ret

# Generated at 2022-06-13 02:41:07.143693
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collect_instance = DateTimeFactCollector()
    collected_facts = collect_instance.collect()
    assert collected_facts['date_time']['epoch']
    assert collected_facts['date_time']['epoch_int']
    assert collected_facts['date_time']['date']
    assert collected_facts['date_time']['time']
    assert collected_facts['date_time']['iso8601_micro']
    assert collected_facts['date_time']['iso8601']
    assert collected_facts['date_time']['tz']

# Generated at 2022-06-13 02:41:10.107814
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector_obj = DateTimeFactCollector()
    res = DateTimeFactCollector_obj.collect()
    print(res)

# Generated at 2022-06-13 02:41:14.486766
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    result = date_time_fact_collector.collect()
    assert 'date_time' in result
    assert len(result['date_time']) == 18

# Generated at 2022-06-13 02:41:19.457902
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    datetime_facts = dtf.collect()
    assert len(datetime_facts) > 0
    assert 'date_time' in datetime_facts
    assert len(datetime_facts['date_time']) > 0
    assert 'date' in datetime_facts['date_time']
    year = datetime_facts['date_time']['year']
    assert len(year) == 4

# Generated at 2022-06-13 02:41:27.764107
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_obj = DateTimeFactCollector()
    date_time_facts = date_time_obj.collect()
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)
    epoch = now.strftime('%s')
    if not epoch:
        epoch = str(int(epoch_ts))
    assert date_time_facts['date_time']['year'] == now.strftime('%Y')
    assert date_time_facts['date_time']['month'] == now.strftime('%m')
    assert date_time_facts['date_time']['weekday'] == now.strftime('%A')
    assert date_time_facts

# Generated at 2022-06-13 02:41:32.001175
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['date_time']['epoch'] == '1509469391'
    assert collected_facts['date_time']['epoch_int'] == '1509469391'

# Generated at 2022-06-13 02:41:38.942494
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """ Define a test method for the collect method of the DateTimeFactCollector
    """
    fact_collector = DateTimeFactCollector()
    facts = fact_collector.collect()
    assert 'date_time' in facts
    assert 'date' in facts['date_time']
    assert 'epoch' in facts['date_time']
    assert 'epoch_int' in facts['date_time']
    assert 'hour' in facts['date_time']
    assert 'iso8601' in facts['date_time']
    assert 'iso8601_basic' in facts['date_time']
    assert 'iso8601_basic_short' in facts['date_time']
    assert 'iso8601_micro' in facts['date_time']
    assert 'minute' in facts['date_time']

# Generated at 2022-06-13 02:41:53.204065
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_args = {}
    facts_dict = DateTimeFactCollector().collect(test_args, {})
    assert type(facts_dict) == dict
    assert 'date_time' in facts_dict
    assert type(facts_dict['date_time']) == dict
    assert len(facts_dict['date_time']) == 19
    assert 'year' in facts_dict['date_time']
    assert 'month' in facts_dict['date_time']
    assert 'weekday' in facts_dict['date_time']
    assert 'weekday_number' in facts_dict['date_time']
    assert 'weeknumber' in facts_dict['date_time']
    assert 'day' in facts_dict['date_time']
    assert 'hour' in facts_dict['date_time']
    assert 'minute' in facts

# Generated at 2022-06-13 02:42:02.008328
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from tests.unit import AnsibleModuleMock
    from ansible.module_utils.facts import timeout

    module = AnsibleModuleMock()
    
    # Test for timeout parameter in function collect
    # timeout disabled
    def test_timeout_disabled():
        delattr(module, 'params')
        collector = DateTimeFactCollector()
        result = collector.collect(module = module)
        assert(result['date_time']['time'] == datetime.datetime.now().strftime('%H:%M:%S'))
     
    test_timeout_disabled()
    
    # timeout enabled
    def test_timeout_enabled():
        module.params = {'timeout': timeout}
        collector = DateTimeFactCollector()
        result = collector.collect(module = module)

# Generated at 2022-06-13 02:42:04.331427
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    datetime_facts = fact_collector.collect()
    for fact in datetime_facts['date_time']:
        assert datetime_facts['date_time'][fact] != ''

# Generated at 2022-06-13 02:42:15.041611
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Generate ansible fact module
    dt_fc = DateTimeFactCollector()
    module = AnsibleModuleStub()
    # Declare collected facts to be empty
    collected_facts = {}
    # Run collect() method to populate collected_facts
    dt_fc.collect(module=module, collected_facts=collected_facts)
    # Declare the expected output: facts_dict
    facts_dict = {}
    date_time_facts = {}
    # Store the timestamp once, then get local and UTC versions from that
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)
    # Declare the facts and their respective values
    date_time_facts['year']

# Generated at 2022-06-13 02:42:27.998449
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Create an instance of the class DateTimeFactCollector
    # A new list of fact_ids is initialized
    fact_collector = DateTimeFactCollector()
    # No module is provided
    module = None
    # collected_facts is set to an empty dictionary
    collected_facts = {}

    # Call the collect method of the DateTimeFactCollector instance
    date_time_facts = fact_collector.collect(module, collected_facts)

    # Test if type of date_time_facts is a dictionary
    assert type(date_time_facts) is dict

    # Test if type of date_time_facts['date_time'] is a dictionary
    assert type(date_time_facts['date_time']) is dict

    # Update collected_facts with the current date_time fact
    collected_facts.update(date_time_facts)

# Generated at 2022-06-13 02:42:38.832740
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Create a `DateTimeFactCollector` instance
    dtf = DateTimeFactCollector()

    # Create a fake local time
    t = datetime.datetime(2016, 9, 1, 21, 45, 9, 123456)

    # Set fake local time to mock `time.time()` and `time.strftime('%z')`
    def mock_time():
        return time.mktime(t.timetuple())
    time.time = mock_time
    time.strftime = lambda fmt: t.strftime(fmt)
    time.tzname = ('CLT', 'CLT')

    # Collect fact
    facts = dtf.collect()

    # Check if collected fact is correct
    assert facts['date_time']['year'] == '2016'

# Generated at 2022-06-13 02:42:44.102995
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import Collectors
    c = Collectors(None, None)
    c.collector['platform'] = {}
    c.collector['platform']['is_linux'] = True
    dt = DateTimeFactCollector()
    dt.collect(c)
    print('module_utils.facts.datetime.py: collect() test successful!')

# Generated at 2022-06-13 02:42:46.822187
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    # TODO: test:
    #    collect() - implemented.
    #    fact_ids() - not implemented.
    #    fact_names() - not implemented.

# Generated at 2022-06-13 02:42:57.242588
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    assert date_time_facts is not None

    # Check top-level structure
    assert 'date_time' in date_time_facts

    # Check epoch is not empty
    assert len(date_time_facts['date_time']['epoch']) > 0

    # Check epoch_int is not empty
    assert len(date_time_facts['date_time']['epoch_int']) > 0

    # Check iso8601 is not empty
    assert len(date_time_facts['date_time']['iso8601']) > 0

    # Check iso8601_basic is not empty

# Generated at 2022-06-13 02:43:05.226332
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Get the expected values
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

# Generated at 2022-06-13 02:43:11.260338
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:43:23.507519
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector.system import (
        DateTimeFactCollector
    )
    from ansible.module_utils.facts.utils import get_file_content
    ansible_collector._initialize_collectors(['system'])
    date_time_fact_collector = ansible_collector.get_collector(DateTimeFactCollector.name)

    date_time_facts = date_time_fact_collector.collect()
    assert date_time_facts

    date_time_facts_json = get_file_content(
        '__ansible_facts_cache/date_time.fact', 'tests/unit/module_utils/facts/files'
    )
    assert date_time_facts_json == date

# Generated at 2022-06-13 02:43:29.761652
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Test for DateTimeFactCollector.collect
    '''
    class TestDateTimeFactCollector(DateTimeFactCollector):
        name = 'TestDateTimeFactCollector'
        _fact_ids = set()

    dtfc = TestDateTimeFactCollector()
    res = dtfc.collect()
    assert 'date_time' in res
    assert isinstance(res['date_time'], dict)
    assert len(res['date_time']) == 19

# Generated at 2022-06-13 02:43:32.342873
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Unit test for method collect of class DateTimeFactCollector"""
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:43:35.050825
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    collected_facts = date_time_fact_collector.collect()
    assert collected_facts['date_time'] != None

# Generated at 2022-06-13 02:43:38.467007
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
	dtfc = DateTimeFactCollector()
	assert type(dtfc).__name__ == 'DateTimeFactCollector'
	dtfc_collect = dtfc.collect()
	assert type(dtfc_collect).__name__ == 'dict'


# Generated at 2022-06-13 02:43:50.444463
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
  collector_object = DateTimeFactCollector()
  test_dict = collector_object.collect()['date_time']
  assert test_dict['year']
  assert test_dict['month']
  assert test_dict['weekday']
  assert test_dict['weekday_number']
  assert test_dict['weeknumber']
  assert test_dict['day']
  assert test_dict['hour']
  assert test_dict['minute']
  assert test_dict['second']
  assert float(test_dict['epoch'])
  assert int(test_dict['epoch_int'])
  assert test_dict['date']
  assert test_dict['time']
  assert test_dict['iso8601_micro']
  assert test_dict['iso8601']
  assert test_dict['iso8601_basic']
 

# Generated at 2022-06-13 02:43:56.814598
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import ansible_collections
    from ansible.module_utils.facts.collector.date_time import DateTimeFactCollector
    DateTimeFactCollector_obj = DateTimeFactCollector()
    out = DateTimeFactCollector_obj.collect()
    assert('date_time' in out)
    assert('year' in out['date_time'])
    assert('month' in out['date_time'])
    assert('weekday' in out['date_time'])
    assert('weekday_number' in out['date_time'])
    assert('weeknumber' in out['date_time'])
    assert('day' in out['date_time'])
    assert('hour' in out['date_time'])
    assert('minute' in out['date_time'])


# Generated at 2022-06-13 02:44:07.312224
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

# Generated at 2022-06-13 02:44:08.418437
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time = DateTimeFactCollector()
    date_time.collect()

# Generated at 2022-06-13 02:44:25.981538
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    result = fact_collector.collect()
    assert 'date_time' in result, "date_time key missing in %s" % result
    datetime = result['date_time']
    assert 'year' in datetime, "year key missing in %s" % datetime
    assert 'month' in datetime, "month key missing in %s" % datetime
    assert 'weekday' in datetime, "weekday key missing in %s" % datetime
    assert 'weekday_number' in datetime, "weekday_number key missing in %s" % datetime
    assert 'weeknumber' in datetime, "weeknumber key missing in %s" % datetime
    assert 'day' in datetime, "day key missing in %s" % datetime
    assert 'hour'

# Generated at 2022-06-13 02:44:37.380458
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    result = dt.collect()
    assert result is not None
    assert result['date_time'] is not None
    assert result['date_time']['date'] is not None
    assert result['date_time']['time'] is not None
    assert result['date_time']['tz'] is not None
    assert result['date_time']['weekday'] is not None
    assert result['date_time']['day'] is not None
    assert result['date_time']['month'] is not None
    assert result['date_time']['year'] is not None
    assert result['date_time']['iso8601'] is not None
    assert result['date_time']['epoch'] is not None

# Generated at 2022-06-13 02:44:41.173713
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    c = DateTimeFactCollector()
    dt = c.collect()
    # test that datetime values are set and not empty
    for _, v in dt['date_time'].items():
        assert v is not None and v != ""

# Generated at 2022-06-13 02:44:44.016391
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    x = DateTimeFactCollector()
    d = x.collect()
    assert d['date_time']['day'] == time.strftime("%d")

# Generated at 2022-06-13 02:44:45.710936
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    collected_facts = {}
    fact_collector.collect(None, collected_facts)

    assert collected_facts['date_time']

# Generated at 2022-06-13 02:44:51.902549
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import time
    import datetime

    # testing time
    now_time_tuple = time.localtime(time.time())
    now_tuple = datetime.datetime.fromtimestamp(time.time())

    # colledted facts

# Generated at 2022-06-13 02:45:01.714489
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    current_year = datetime.datetime.now().strftime('%Y')
    current_month = datetime.datetime.now().strftime('%m')
    current_weekday = datetime.datetime.now().strftime('%A')
    current_weekday_number = datetime.datetime.now().strftime('%w')
    current_weeknumber = datetime.datetime.now().strftime('%W')
    current_day = datetime.datetime.now().strftime('%d')
    current_hour = datetime.datetime.now().strftime('%H')
    current_minute = datetime.datetime.now().strftime('%M')
    current_second = datetime.datetime.now().strftime('%S')
    current_date = datetime.datetime.now().str

# Generated at 2022-06-13 02:45:04.744858
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    assert collector.collect()['date_time']['weekday_number'] == time.strftime("%w")

# Generated at 2022-06-13 02:45:13.118003
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    before_time = datetime.datetime.now()
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()['date_time']

    assert date_time_facts['year'] == str(before_time.year)
    assert date_time_facts['month'] == before_time.strftime('%m')
    assert date_time_facts['weekday'] == before_time.strftime('%A')
    assert date_time_facts['weekday_number'] == before_time.strftime('%w')
    assert date_time_facts['weeknumber'] == before_time.strftime('%W')
    assert date_time_facts['day'] == before_time.strftime('%d')

# Generated at 2022-06-13 02:45:14.702561
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    assert fact_collector is not None
    assert fact_collector.collect() is not None

# Generated at 2022-06-13 02:45:42.667490
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_collector = DateTimeFactCollector()
    test_collector_result = test_collector.collect()
    assert isinstance(test_collector_result, dict)
    assert isinstance(test_collector_result['date_time'], dict)
    assert isinstance(test_collector_result['date_time']['epoch'], str)
    assert isinstance(test_collector_result['date_time']['epoch_int'], str)
    assert isinstance(test_collector_result['date_time']['day'], str)
    assert isinstance(test_collector_result['date_time']['hour'], str)
    assert isinstance(test_collector_result['date_time']['minute'], str)

# Generated at 2022-06-13 02:45:44.608520
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    # No assert, the method returns a dict.
    date_time_fact_collector.collect()

# Generated at 2022-06-13 02:45:50.703720
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    # initialize collector instance
    facts_collector = FactsCollector(None)
    # initialize DateTimeFactCollector
    datetime_collector = DateTimeFactCollector()
    # add DateTimeFactCollector to collector
    facts_collector._fact_collectors.append(datetime_collector)

    # collect all facts
    collected_facts = facts_collector.collect()

    # assert collected facts
    assert ('date_time' in collected_facts)
    assert ('date' in collected_facts['date_time'])
    assert ('time' in collected_facts['date_time'])
    assert ('iso8601_micro' in collected_facts['date_time'])
    assert ('iso8601' in collected_facts['date_time'])


# Generated at 2022-06-13 02:45:53.587834
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_collector.collect()
    assert date_time_collector.name == 'date_time'

# Generated at 2022-06-13 02:46:03.285734
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    my_date_time_fact_collector = DateTimeFactCollector()
    my_date_time_facts = my_date_time_fact_collector.collect()

    assert isinstance(my_date_time_facts, dict), \
        "date_time_facts should be dictionary"

    assert 'date_time' in my_date_time_facts, \
        "The key 'date_time' should exist in the date_time_facts"

    assert isinstance(my_date_time_facts['date_time'], dict), \
        "date_time_facts['date_time'] should be dictionary"



# Generated at 2022-06-13 02:46:12.452088
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # prepare the test environment
    dtfc = DateTimeFactCollector()
    dtfc.collect()
    datetime_facts = dtfc.collect()
    date_time_facts = datetime_facts['date_time']

    assert(date_time_facts['day'])
    assert(date_time_facts['epoch'])
    assert(date_time_facts['hour'])
    assert(date_time_facts['iso8601'])
    assert(date_time_facts['iso8601_basic'])
    assert(date_time_facts['iso8601_basic_short'])
    assert(date_time_facts['iso8601_micro'])
    assert(date_time_facts['time'])
    assert(date_time_facts['date'])

# Generated at 2022-06-13 02:46:22.695663
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    collected_facts = fact_collector.collect()

    keys = ["date_time"]
    for key in keys:
        assert collected_facts.get(key) is not None

    # Check if the timestamp is an integer
    # There are some platforms like Windows that don't support Epoch
    # timestamp but return string instead. For those platforms
    # we skip the integer checks.
    if type(collected_facts['date_time']['epoch']) is int:
        assert collected_facts['date_time']['epoch'] > 0
        assert collected_facts['date_time']['epoch'] <= int(time.time())
        assert collected_facts['date_time']['epoch_int'] > 0

# Generated at 2022-06-13 02:46:33.848398
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    non_default_fact_ids = ['epoch_int']

    # Test without any non-default fact_ids configured
    fact_collector = DateTimeFactCollector()
    assert fact_collector.fact_ids == set()

    # Test with one non-default fact_id configured
    fact_collector = DateTimeFactCollector(fact_ids=non_default_fact_ids)
    assert fact_collector.fact_ids == set(non_default_fact_ids)

    # Test with multiple non-default fact_ids configured
    fact_collector = DateTimeFactCollector(fact_ids=non_default_fact_ids * 3)
    assert fact_collector.fact_ids == set(non_default_fact_ids)

    # Test handling of unknown fact_ids
    fact_collector = DateTimeFactCollector

# Generated at 2022-06-13 02:46:34.757625
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector.collect()

# Generated at 2022-06-13 02:46:42.146945
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fc = DateTimeFactCollector()
    date_time_facts = date_time_fc.collect()

    assert 'date_time' in date_time_facts
    assert 'year' in date_time_facts['date_time']
    assert 'month' in date_time_facts['date_time']
    assert 'weekday' in date_time_facts['date_time']
    assert 'weekday_number' in date_time_facts['date_time']
    assert 'weeknumber' in date_time_facts['date_time']
    assert 'day' in date_time_facts['date_time']
    assert 'hour' in date_time_facts['date_time']
    assert 'minute' in date_time_facts['date_time']

# Generated at 2022-06-13 02:47:25.202075
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Return facts from DateTimeFactCollector
    :return: Dictionary of facts
    """
    facts_dict = {}
    datetime_facts = {}

# Generated at 2022-06-13 02:47:29.939759
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    date_time_fact = DateTimeFactCollector()
    date_time = date_time_fact.collect()

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

# Generated at 2022-06-13 02:47:40.472020
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    tzname = time.tzname[0]
    tzoffset = time.strftime("%z")
    epoch = str(int(time.time()))
    epoch_int = int(time.time())
    assert(time.strftime("%s") == epoch)
    dt = datetime.datetime.fromtimestamp(time.time())
    dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    dt_arr = dt_str.split(' ')

    collector = DateTimeFactCollector({}, {})
    result = collector.collect()

# Generated at 2022-06-13 02:47:43.225543
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fixture_class = DateTimeFactCollector
    fixture_obj = DateTimeFactCollector()
    result = fixture_obj.collect()
    assert result is not None

# Generated at 2022-06-13 02:47:51.334530
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:48:01.544499
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create a test DateTimeFactCollector object
    dtf = DateTimeFactCollector()

    # Get the time now
    time_now = time.time()

    # Collect the facts
    facts = dtf.collect()

    # Make sure the key 'date_time' exists
    assert 'date_time' in facts

    # Make sure the key 'date_time' is a dict
    assert isinstance(facts['date_time'], dict)

    # Get the date_time facts
    date_time_facts = facts['date_time']

    # Make sure the key 'epoch' exists
    assert 'epoch' in date_time_facts

    # Make sure it's a float
    assert isinstance(float(date_time_facts['epoch']), float)

    # Make sure the key 'epoch' is a string


# Generated at 2022-06-13 02:48:07.408765
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts_dict = DateTimeFactCollector().collect()
    assert 'date_time' in facts_dict
    assert len(facts_dict['date_time']) == 19
    assert isinstance(facts_dict['date_time']['year'], str)
    assert isinstance(facts_dict['date_time']['month'], str)
    assert isinstance(facts_dict['date_time']['weekday'], str)
    assert isinstance(facts_dict['date_time']['weekday_number'], str)
    assert isinstance(facts_dict['date_time']['weeknumber'], str)
    assert isinstance(facts_dict['date_time']['day'], str)
    assert isinstance(facts_dict['date_time']['hour'], str)

# Generated at 2022-06-13 02:48:16.843761
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.date_time import DateTimeFactCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector

    # Arrange
    test_object = DateTimeFactCollector()
    test_object._fact_ids = set()

    # Act
    result = test_object.collect()

    # Assert
    assert isinstance(result, dict)
    assert 'date_time' in result
    assert len(result['date_time']) == 22

# Generated at 2022-06-13 02:48:28.021170
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector(None, None)
    result = dtfc.collect()

    if not isinstance(result, dict):
        raise AssertionError("Facts returned are not of type dict: %s" % type(result))

    dt_fact_ids = result['date_time'].keys()
    for fid in dt_fact_ids:
        if fid not in ('epoch', 'epoch_int', 'year', 'month', 'day', 'weekday', 'weekday_number', 'weeknumber',
                        'hour', 'minute', 'second', 'time', 'tz', 'tz_offset', 'date', 'tz_dst', 'iso8601',
                        'iso8601_micro', 'iso8601_basic', 'iso8601_basic_short'):
            raise AssertionError

# Generated at 2022-06-13 02:48:38.902225
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()

    # mock datetime.datetime to return fixed datetime object
    a = datetime.datetime(2016,9,23,17,36,1)
    b = datetime.datetime(2016,9,23,17,36,1)
    dtf.datetime = mock.Mock(side_effect=[a,b])

    # mock time.time to return fixed timestamp
    time.time = mock.Mock(return_value=1474600766.27)

    # mock time.strftime('%Z') to return fixed timezone
    time.strftime = mock.Mock(return_value='GMT')

    # mock time.tzname to return fixed tzname list
    time.tzname = mock.Mock(return_value=['',''])

    # Call collect;

# Generated at 2022-06-13 02:49:55.782399
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Expected results
    epoch_ts = time.time()

# Generated at 2022-06-13 02:49:58.204944
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    df = DateTimeFactCollector()
    d = df.collect()
    assert 'date_time' in d

# Generated at 2022-06-13 02:50:05.551730
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    my_collector = DateTimeFactCollector()
    my_facts = my_collector.collect()
    assert my_facts['date_time']['year'] == time.strftime('%Y')
    assert my_facts['date_time']['month'] == time.strftime('%m')
    assert my_facts['date_time']['weekday'] == time.strftime('%A')
    assert my_facts['date_time']['weekday_number'] == time.strftime('%w')
    assert my_facts['date_time']['weeknumber'] == time.strftime('%W')
    assert my_facts['date_time']['day'] == time.strftime('%d')
    assert my_facts['date_time']['hour'] == time.strftime('%H')


# Generated at 2022-06-13 02:50:16.038214
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_fact = DateTimeFactCollector()

    # Test: if type of the response is 'dict'
    # Expected: FactCollectorResult.success == True
    #           type of the response == dict
    #           response has Key 'date_time'
    #           type(response['date_time']) == dict
    #           response['date_time'] contains 'year'
    #           response['date_time'] contains 'month'
    #           response['date_time'] contains 'weekday'
    #           response['date_time'] contains 'weekday_number'
    #           response['date_time'] contains 'weeknumber'
    #           response['date_time'] contains 'day'
    #           response['date_time'] contains 'hour'
    #           response['date_time'] contains 'minute'
    #           response

# Generated at 2022-06-13 02:50:22.867123
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFacts = DateTimeFactCollector.collect()
    assert DateTimeFacts['date_time']['year'] == time.strftime('%Y')
    assert DateTimeFacts['date_time']['month'] == time.strftime('%m')
    assert DateTimeFacts['date_time']['weekday'] == time.strftime('%A')
    assert DateTimeFacts['date_time']['weekday_number'] == time.strftime('%w')
    assert DateTimeFacts['date_time']['weeknumber'] == time.strftime('%W')
    assert DateTimeFacts['date_time']['day'] == time.strftime('%d')
    assert DateTimeFacts['date_time']['hour'] == time.strftime('%H')
    assert DateTime

# Generated at 2022-06-13 02:50:32.581551
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()['date_time']
    assert date_time_facts['year'] != ''
    assert date_time_facts['month'] != ''
    assert date_time_facts['weekday'] != ''
    assert date_time_facts['weekday_number'] != ''
    assert date_time_facts['weeknumber'] != ''
    assert date_time_facts['day'] != ''
    assert date_time_facts['hour'] != ''
    assert date_time_facts['minute'] != ''
    assert date_time_facts['second'] != ''
    assert date_time_facts['epoch'] != ''
    assert date_time_facts['epoch_int'] != ''
    assert date_time_facts['iso8601_micro'].endswith('Z')
    assert date_

# Generated at 2022-06-13 02:50:43.682724
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Unit test for method collect of class DateTimeFactCollector"""
    # Fixture data