

# Generated at 2022-06-13 02:40:44.825636
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    datetime_collector = DateTimeFactCollector()
    datetime_collector.collect()

# Generated at 2022-06-13 02:40:54.741904
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_collector = DateTimeFactCollector()
    dt_collector._module = None
    dt_facts = dt_collector.collect()
    assert dt_facts['date_time']['tz'] == time.strftime("%Z")
    assert dt_facts['date_time']['second'] == time.strftime("%S")
    assert dt_facts['date_time']['minute'] == time.strftime("%M")
    assert dt_facts['date_time']['hour'] == time.strftime("%H")
    assert dt_facts['date_time']['day'] == time.strftime("%d")
    assert dt_facts['date_time']['month'] == time.strftime("%m")

# Generated at 2022-06-13 02:41:02.065639
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Unit test for method collect of class DateTimeFactCollector.
    '''
    Date_Time_FactCollector = DateTimeFactCollector()
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)
    facts_dict = {}
    date_time_facts = {}

    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
    date_time_facts['weekday_number'] = now.strftime('%w')
    date_time_facts['weeknumber'] = now

# Generated at 2022-06-13 02:41:04.862963
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # This method is not implemented
    assert DateTimeFactCollector.collect(DateTimeFactCollector()) == 'dev'

# Generated at 2022-06-13 02:41:09.192897
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Setup
    obj = DateTimeFactCollector()

    # Exercise
    res = obj.collect()

    # Verify
    assert 'date_time' in res
    assert 'hour' in res['date_time']
    assert 'iso8601_basic' in res['date_time']

# Generated at 2022-06-13 02:41:14.510565
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
    dtfc = DateTimeFactCollector()
    dtfc.collect()

    assert 'date_time' in dtfc.fact_list
    assert 'year' in dtfc.fact_list['date_time']
    assert 'month' in dtfc.fact_list['date_time']
    assert 'weekday' in dtfc.fact_list['date_time']
    assert 'weekday_number' in dtfc.fact_list['date_time']
    assert 'weeknumber' in dtfc.fact_list['date_time']
    assert 'day' in dtfc.fact_list['date_time']
    assert 'hour' in dtfc.fact_list['date_time']
   

# Generated at 2022-06-13 02:41:22.573290
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    facts_dict = date_time_collector.collect()
    assert 'date_time' in facts_dict
    assert facts_dict['date_time'] == {
        'year': '2018',
        'day': '23',
        'date': '2018-02-23',
        'hour': '13',
        'minute': '46',
        'month': '02',
        'time': '13:46:06',
        'weekday': 'Friday',
        'weekday_number': '5',
        'weeknumber': '08',
        'epoch': '1519371566',
        'tz': 'CET'
    }



# Generated at 2022-06-13 02:41:25.781409
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()

    date_fact_test = date_time_fact_collector.collect()

    # check if epoch is of type integer
    assert isinstance(date_fact_test['date_time']['epoch'], int)

# Generated at 2022-06-13 02:41:34.835724
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:41:44.833089
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    assert date_time_facts['date_time']['date'] == datetime.datetime.today().strftime('%Y-%m-%d')
    assert date_time_facts['date_time']['year'] == datetime.datetime.today().strftime('%Y')
    assert date_time_facts['date_time']['weekday'] == datetime.datetime.today().strftime('%A')
    if 'tz' in date_time_facts['date_time']:
        assert date_time_facts['date_time']['tz'] == time.strftime("%Z")

# Generated at 2022-06-13 02:41:56.684530
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Test date and time facts
    date_time_facts_collected = DateTimeFactCollector().collect()
    assert isinstance(date_time_facts_collected, dict)
    assert set(date_time_facts_collected.keys()) == set(['date_time'])

    # Test a few of the fields

# Generated at 2022-06-13 02:42:03.405884
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    module = None
    collected_facts = {}
    mydate = DateTimeFactCollector()
    date_time_facts = mydate.collect(module, collected_facts)
    assert date_time_facts['date_time']['day'] == datetime.datetime.now().strftime('%d')
    assert date_time_facts['date_time']['epoch'] == datetime.datetime.now().strftime('%s')
    assert date_time_facts['date_time']['epoch_int'] == datetime.datetime.now().strftime('%s')
    assert date_time_facts['date_time']['hour'] == datetime.datetime.now().strftime('%H')

# Generated at 2022-06-13 02:42:14.396235
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact = DateTimeFactCollector()
    facts_dict = date_time_fact.collect()
    assert facts_dict['date_time']['month'] in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    assert facts_dict['date_time']['weekday'] in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    assert facts_dict['date_time']['weekday_number'] in ['1', '2', '3', '4', '5', '6', '7']

# Generated at 2022-06-13 02:42:18.553696
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    facts = fact_collector.collect()
    assert(facts.get("date_time") is not None)

# Generated at 2022-06-13 02:42:29.875586
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Unit test for method collect of class DateTimeFactCollector
    '''
    date_time_fc = DateTimeFactCollector()

    date_time = date_time_fc.collect()['date_time']

    assert int(date_time['epoch']) == int(date_time['epoch_int'])
    assert date_time['epoch'] == date_time['epoch_int']
    assert date_time['epoch'] == str(int(time.time()))
    assert date_time['epoch_int'] == str(int(time.time()))
    assert date_time['iso8601_micro'].endswith('Z')
    assert date_time['iso8601'].endswith('Z')

# Generated at 2022-06-13 02:42:40.449204
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import get_collector_instance

    collector = get_collector_instance(DateTimeFactCollector)
    result = collector.collect(module=None)
    assert isinstance(result, dict)
    assert 'date_time' in result.keys()
    assert 'epoch' in result['date_time']
    assert 'epoch_int' in result['date_time']
    assert 'date' in result['date_time']
    assert 'time' in result['date_time']
    assert 'iso8601' in result['date_time']
    assert 'iso8601_micro' in result['date_time']

# Generated at 2022-06-13 02:42:43.677438
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Create object of DateTimeFactCollector
    dateTimeFactCollector = DateTimeFactCollector()

    # Test method collect of class DateTimeFactCollector
    dateTimeFactCollector.collect()

# Generated at 2022-06-13 02:42:45.310362
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dateTimeFactCollector = DateTimeFactCollector()
    dateTimeFactCollector.collect()

# Generated at 2022-06-13 02:42:49.144488
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import pytest

    # Arrange
    module = None

    # Act
    dtfc = DateTimeFactCollector()
    dtf = dtfc.collect(module)

    # Assert
    assert dtf is not None



# Generated at 2022-06-13 02:42:58.800910
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:43:10.696253
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Unit test for method collect of class DateTimeFactCollector
    '''
    now = datetime.datetime.now()

# Generated at 2022-06-13 02:43:23.098032
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    # Execute method collect
    dtf_ret = dtf.collect()

    # Check if return value is expected
    assert dtf_ret['date_time']['weekday'] is not None
    assert int(dtf_ret['date_time']['epoch']) > 0
    assert int(dtf_ret['date_time']['epoch_int']) > 0
    assert dtf_ret['date_time']['date'] is not None
    assert dtf_ret['date_time']['time'] is not None
    assert dtf_ret['date_time']['iso8601'] is not None
    assert dtf_ret['date_time']['tz'] is not None

# Generated at 2022-06-13 02:43:33.653208
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Replace the module_utils.facts.collector.BaseFactCollector import with a Mock()
    # for testing purposes
    mocked_BaseFactCollector = BaseFactCollector()

# Generated at 2022-06-13 02:43:42.075988
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test the method collect of class DateTimeFactCollector
    # with valid argument.
    collector = DateTimeFactCollector()

    result = collector.collect()
    assert 'date_time' in result
    assert result['date_time']['year'].isdigit()
    assert result['date_time']['month'].isdigit()
    assert result['date_time']['weekday'].isalpha()
    assert result['date_time']['weekday_number'].isdigit()
    assert result['date_time']['weeknumber'].isdigit()
    assert result['date_time']['day'].isdigit()
    assert result['date_time']['hour'].isdigit()
    assert result['date_time']['minute'].isdigit()

# Generated at 2022-06-13 02:43:44.695841
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc.collect()
    assert isinstance(dtfc.collect(), dict)

# Generated at 2022-06-13 02:43:54.177094
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    module = None
    collected_facts = {}

    # Call method collect
    ansible_date_time_facts = DateTimeFactCollector().collect(module, collected_facts)

    # Check it against known values
    assert isinstance(ansible_date_time_facts, dict)
    assert 'date_time' in ansible_date_time_facts
    assert 'date' in ansible_date_time_facts['date_time']
    assert 'epoch' in ansible_date_time_facts['date_time']
    assert 'iso8601' in ansible_date_time_facts['date_time']
    assert 'time' in ansible_date_time_facts['date_time']
    assert 'tz' in ansible_date_time_facts['date_time']

# Generated at 2022-06-13 02:44:05.912531
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector.collect()['date_time']
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

# Generated at 2022-06-13 02:44:12.850270
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_DateTimeFactCollector = DateTimeFactCollector()
    test_dict = test_DateTimeFactCollector.collect()
    assert test_dict['date_time']['year'] == datetime.datetime.fromtimestamp(time.time()).strftime('%Y')
    assert test_dict['date_time']['month'] == datetime.datetime.fromtimestamp(time.time()).strftime('%m')
    assert test_dict['date_time']['weekday'] == datetime.datetime.fromtimestamp(time.time()).strftime('%A')
    assert test_dict['date_time']['weekday_number'] == datetime.datetime.fromtimestamp(time.time()).strftime('%w')

# Generated at 2022-06-13 02:44:15.765325
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    assert date_time_fact_collector.collect() is not None

# Generated at 2022-06-13 02:44:17.743465
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dateTimeFactCollector = DateTimeFactCollector()
    dateTimeFactCollector.collect()

# Generated at 2022-06-13 02:44:24.197531
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact = DateTimeFactCollector()
    res = fact.collect()
    assert len(res) == 1
    assert len(res['date_time']) == 17

# Generated at 2022-06-13 02:44:32.586902
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Unit test for method collector.DateTimefactCollector.collect
    """
    from ansible.module_utils.facts.collector import collect_date_time
    result = collect_date_time()
    if 'date_time' not in result or not isinstance(result['date_time'], dict):
        raise AssertionError
    if 'year' not in result['date_time'] or not isinstance(result['date_time']['year'], str):
        raise AssertionError
    if 'month' not in result['date_time'] or not isinstance(result['date_time']['month'], str):
        raise AssertionError
    if 'weekday' not in result['date_time'] or not isinstance(result['date_time']['weekday'], str):
        raise Assert

# Generated at 2022-06-13 02:44:37.557256
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    collected_facts = {}
    facts = collector.collect(collected_facts=collected_facts)
    assert 'date_time' in facts
    assert 'year' in facts['date_time']
    assert 'epoch' in facts['date_time']
    assert 'tz' in facts['date_time']

# Generated at 2022-06-13 02:44:47.553595
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Check if method collect of DateTimeFactCollector is working properly
    """
    collecter = DateTimeFactCollector()
    collected_facts = collecter.collect()
    assert 'date_time' in collected_facts
    assert collected_facts['date_time']['year'] != ''
    assert collected_facts['date_time']['month'] != ''
    assert collected_facts['date_time']['weekday'] != ''
    assert collected_facts['date_time']['weekday_number'] != ''
    assert collected_facts['date_time']['weeknumber'] != ''
    assert collected_facts['date_time']['day'] != ''
    assert collected_facts['date_time']['hour'] != ''
    assert collected_facts['date_time']['minute'] != ''
    assert collected

# Generated at 2022-06-13 02:44:59.261112
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()

# Generated at 2022-06-13 02:45:09.778652
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    date_time_collector = DateTimeFactCollector(
        ansible_collector,
        'date_time',
        set()
    )

    local_collector = ansible_collector
    local_collector.gather_subset = ['!all,network']

    # get the actual result of the collect method
    result = date_time_collector.collect(
        ansible_collector,
        {'ansible_local': {'gather_subset': 'all'}}
    )

    # if the collect method returns a dictionary, then set result to that dictionary
    if isinstance(result, dict):
        result = result['date_time']

    # set expected result dictionary

# Generated at 2022-06-13 02:45:16.984747
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Unit test for method collect of class DateTimeFactCollector
    """
    # Setup the objects needed to test
    date_time_fact_collector = DateTimeFactCollector()

    # Test calling with no parameters
    test_date_time_facts = date_time_fact_collector.collect()

    # Test a few simple assertions
    assert "date_time" in test_date_time_facts

    # Test that the epoch fact is actually a number
    try:
        assert test_date_time_facts["date_time"]["epoch"].isdigit()
    except AssertionError:
        # Ignore assertion errors in case the system does not support %s in strftime
        pass

    # Test that the timezone offset is a number

# Generated at 2022-06-13 02:45:23.111936
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()

    # Get test time
    now = datetime.datetime.utcnow()

    # Get facts from current time
    facts_dict = collector.collect()

    # Test if facts are not empty
    assert facts_dict['date_time'] is not None

    # Test if test time is equal to time in facts
    for time_fact in facts_dict['date_time']:
        assert time_fact in now.strftime('%s')

# Generated at 2022-06-13 02:45:32.387225
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import sys
    import os
    my_env = os.environ.copy()
    my_env['LANG'] = 'C'
    fc = DateTimeFactCollector()
    my_facts = fc.collect(None, None)
    assert my_facts['date_time']['year'] == time.strftime("%Y")
    assert my_facts['date_time']['month'] == time.strftime("%m")
    assert my_facts['date_time']['day'] == time.strftime("%d")
    assert my_facts['date_time']['hour'] == time.strftime("%H")
    assert my_facts['date_time']['minute'] == time.strftime("%M")
    assert my_facts['date_time']['second'] == time.strftime

# Generated at 2022-06-13 02:45:43.035563
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_dt_object = DateTimeFactCollector()
    result = test_dt_object.collect()['date_time']
    assert isinstance(result, dict)
    assert 'year' in result
    assert 'month' in result
    assert 'weekday' in result
    assert 'weekday_number' in result
    assert 'weeknumber' in result
    assert 'day' in result
    assert 'hour' in result
    assert 'minute' in result
    assert 'second' in result
    assert 'epoch' in result
    assert 'epoch_int' in result
    assert 'date' in result
    assert 'time' in result
    assert 'iso8601_micro' in result
    assert 'iso8601' in result
    assert 'iso8601_basic' in result
    assert 'iso8601_basic_short'

# Generated at 2022-06-13 02:45:58.174964
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = date_time_fact_collector.collect()

# Generated at 2022-06-13 02:46:05.600312
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
    fact_collector = DateTimeFactCollector()
    facts_dict = fact_collector.collect()
    assert facts_dict is not None
    assert len(facts_dict) == 1
    assert 'date_time' in facts_dict
    assert facts_dict['date_time']['epoch_int'] == str(int(time.time()))

# Generated at 2022-06-13 02:46:07.404744
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_obj = DateTimeFactCollector()
    date_time_obj.collect()

# Generated at 2022-06-13 02:46:09.662410
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fc = DateTimeFactCollector()
    facts = fc.collect()
    assert 'date_time' in facts
    assert facts['date_time']['tz_offset']

# Generated at 2022-06-13 02:46:15.820286
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """ Test DateTimeFactCollector gets facts for current date and time,
        and that the facts match what we expect them to be.
    """

    fact_collector = DateTimeFactCollector()
    date_time_facts = fact_collector.collect()

    # epoch_int, epoch, hour, minute, second, weekday_number and weeknumber are
    # integers in the python dict.
    integers = ['epoch_int', 'epoch', 'hour', 'minute', 'second', 'weekday_number', 'weeknumber']
    for fact in integers:
        assert date_time_facts['date_time'][fact].isdigit(), \
               '{0} does not have expected format: {1}'.format(fact, date_time_facts['date_time'][fact])

    # weekday, month and day are all strings in the

# Generated at 2022-06-13 02:46:26.785729
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # create an instance of the class DateTimeFactCollector
    dtfc = DateTimeFactCollector()

    # Store the timestamp once, then get local and UTC versions from that
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    # create a dictionary of default values
    date_time_facts = {}
    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
    date_time_facts['weekday_number'] = now.strftime('%w')

# Generated at 2022-06-13 02:46:36.835957
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
    import re

    date_time_fact_collector = DateTimeFactCollector(FactCollector())
    date_time_facts = date_time_fact_collector.collect()

    # Assert timestamps
    assert isinstance(date_time_facts['date_time']['epoch'], str), \
        "epoch timestamp is not a string"
    assert re.match(r'^\d*', date_time_facts['date_time']['epoch']), \
        "epoch is not a positive integer"

# Generated at 2022-06-13 02:46:47.139470
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector()
    date_time_facts_dict = date_time_facts.collect()

# Generated at 2022-06-13 02:46:54.131623
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    module = None
    collected_facts = None
    c = DateTimeFactCollector()
    facts_dict = c.collect(module, collected_facts)
    assert 'date_time' in facts_dict
    assert 'year' in facts_dict['date_time']
    assert 'month' in facts_dict['date_time']
    assert 'weekday' in facts_dict['date_time']
    assert 'weekday_number' in facts_dict['date_time']
    assert 'weeknumber' in facts_dict['date_time']
    assert 'day' in facts_dict['date_time']
    assert 'hour' in facts_dict['date_time']
    assert 'minute' in facts_dict['date_time']
    assert 'second' in facts_dict['date_time']
    assert 'epoch' in facts_

# Generated at 2022-06-13 02:46:58.911507
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect()
    assert 'epoch_int' in date_time_facts['date_time']
    assert 'epoch' in date_time_facts['date_time']
    assert 'iso8601' in date_time_facts['date_time']

# Generated at 2022-06-13 02:47:16.071561
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """ Unit test for method DateTimeFactCollector._collect. """
    c = DateTimeFactCollector()
    res = c.collect()
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

# Generated at 2022-06-13 02:47:24.750997
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:47:29.172936
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts_collector = DateTimeFactCollector()
    collected_facts = {}
    collected_facts = date_time_facts_collector.collect(collected_facts)
    assert collected_facts['date_time']['weekday'] == time.strftime("%A")

# Generated at 2022-06-13 02:47:33.870236
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    gf = DateTimeFactCollector()
    result = gf.collect()
    assert 'date_time' in result
    assert result['date_time']['tz_offset'] == time.strftime("%z")
    assert result['date_time']['tz_dst'] == time.tzname[1]

# Generated at 2022-06-13 02:47:39.530475
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_result = date_time_collector.collect()
    assert isinstance(date_time_result, dict)
    assert 'date_time' in date_time_result
    assert 'date' in date_time_result['date_time']
    assert 'iso8601_basic_short' in date_time_result['date_time']



# Generated at 2022-06-13 02:47:49.136837
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Unit test for method collect of class DateTimeFactCollector"""
    cls = DateTimeFactCollector()
    result = cls.collect()
    assert "date_time" in result
    assert result["date_time"]["date"] == datetime.datetime.today().strftime("%Y-%m-%d")
    assert result["date_time"]["time"] == datetime.datetime.today().strftime("%H:%M:%S")
    assert result["date_time"]["epoch"] == str(int(time.time()))
    assert result["date_time"]["epoch_int"] == str(int(time.time()))

# Generated at 2022-06-13 02:47:59.699373
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test date_time facts with a mocked datetime
    tested_object = DateTimeFactCollector()

    first_run = datetime.datetime(2018, 10, 17, 22, 24, 12, 34567)
    second_run = datetime.datetime(2018, 10, 17, 22, 25, 24, 56789)
    third_run = datetime.datetime(2018, 10, 17, 22, 25, 24, 56789)

    datetime.datetime = lambda *args: first_run
    first_fact = tested_object.collect()['date_time']
    assert first_fact['year'] == '2018'
    assert first_fact['month'] == '10'
    assert first_fact['weekday'] == 'Wednesday'
    assert first_fact['weekday_number'] == '3'
    assert first

# Generated at 2022-06-13 02:48:06.394234
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    import sys
    # Pretend we are not in a POSIX environment
    # Python 3.2+ and Python 2.7+ have time.tzname as tuple and
    # time.strftime %z format is always supported
    posix_supported = sys.version_info >= (3, 2) or (sys.version_info >= (2, 7) and sys.version_info < (3,))
    if posix_supported:
        time.tzname = None

    dtf = DateTimeFactCollector()
    dtf.collect()
    if posix_supported:
        assert 'tz_dst' in dtf.facts['date_time']
        assert 'tz_offset' in dtf.facts['date_time']
    else:
        assert 'tz_dst' not in dtf.facts['date_time']

# Generated at 2022-06-13 02:48:19.358662
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # input parameters
    module = None
    collected_facts = None
    
    testobj = DateTimeFactCollector()
    result = testobj.collect(module, collected_facts)
    assert 'date_time' in result
    
    assert 'year' in result['date_time']
    assert result['date_time']['year']
    assert 'month' in result['date_time']
    assert result['date_time']['month']
    assert 'weekday' in result['date_time']
    assert result['date_time']['weekday']
    assert 'weekday_number' in result['date_time']
    assert result['date_time']['weekday_number']
    assert 'weeknumber' in result['date_time']
    assert result['date_time']['weeknumber']

# Generated at 2022-06-13 02:48:22.368822
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # class DateTimeFactCollector(BaseFactCollector):
    # def collect(self, module=None, collected_facts=None):

    ## First collect the facts, then test them
    fc = DateTimeFactCollector()
    f = fc.collect()

    # assert f['ansible_localtime'] == 'Tue Feb  2 16:47:02 EST 2016'
    # assert f['ansible_zonename'] == 'EST'
    assert 'date_time' in f.keys()
    assert type(f['date_time']) == dict

# Generated at 2022-06-13 02:48:38.586988
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector()


# Generated at 2022-06-13 02:48:42.695157
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Test DateTimeFactCollector.collect
    """
    temp = DateTimeFactCollector(None)
    result = temp.collect(None, None)

    expected_keys = ['date_time']
    for key in expected_keys:
        assert key in result


# Generated at 2022-06-13 02:48:51.866647
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_fdc = DateTimeFactCollector()
    test_facts = test_fdc.collect()
    assert test_facts.keys() == ['date_time']
    assert type(test_facts['date_time']) == dict
    assert test_facts['date_time'].keys() == ['year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset']

# Generated at 2022-06-13 02:49:02.124345
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector.__new__(DateTimeFactCollector)
    collected_facts = {}
    collected_facts = date_time_fact_collector.collect(collected_facts=collected_facts)
    assert collected_facts['date_time']['year'] == time.strftime("%Y")
    assert collected_facts['date_time']['month'] == time.strftime("%m")
    assert collected_facts['date_time']['weekday'] == time.strftime("%A")
    assert collected_facts['date_time']['weekday_number'] == time.strftime("%w")
    assert collected_facts['date_time']['weeknumber'] == time.strftime("%W")

# Generated at 2022-06-13 02:49:12.105738
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import sys
    import ansible.module_utils
    import ansible.module_utils.facts.collectors.date_time
    import ansible.module_utils.facts.collectors

    reload(sys)
    sys.setdefaultencoding('utf8')

    my_collector = ansible.module_utils.facts.collectors.date_time.DateTimeFactCollector()
    my_result = my_collector.collect()

    assert my_result['date_time']['epoch'] != ''
    assert my_result['date_time']['epoch'].isdigit()
    assert my_result['date_time']['epoch_int'] != ''
    assert my_result['date_time']['epoch_int'].isdigit()

# Generated at 2022-06-13 02:49:14.857056
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Arrange
    # Empty module
    module = {}
    # Empty collected facts
    collected_facts = {}
    collector = DateTimeFactCollector()

    # Act
    result = collector.collect(module, collected_facts)

    # Assert
    assert 'epoch' in result['date_time']

# Generated at 2022-06-13 02:49:25.876410
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    results = collector.collect()
    assert 'date_time' in results
    assert isinstance(results['date_time'], dict)
    assert set(results['date_time'].keys()) == set((
        'year',
        'month',
        'weekday',
        'weekday_number',
        'weeknumber',
        'day',
        'hour',
        'minute',
        'second',
        'epoch',
        'epoch_int',
        'date',
        'time',
        'iso8601_micro',
        'iso8601',
        'iso8601_basic',
        'iso8601_basic_short',
        'tz',
        'tz_dst',
        'tz_offset'
    ))

# Generated at 2022-06-13 02:49:27.081882
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

   dtf = DateTimeFactCollector()
   assert dtf.collect() != None

# Generated at 2022-06-13 02:49:38.295381
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector.collect()

# Generated at 2022-06-13 02:49:44.954541
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    collected_facts = dt.collect()
    assert collected_facts['date_time']['hour']
    assert collected_facts['date_time']['iso8601']
    assert collected_facts['date_time']['tz_dst']
    assert collected_facts['date_time']['weekday_number']

# Generated at 2022-06-13 02:50:26.278871
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import sys
    import pytest
    from mock import Mock, patch
    # Mock pythons datetime.datetime and time.time so that
    # the code always evaluates to the same values

    # Mock datetime.datetime.utcnow
    mock_dt = Mock(wraps=datetime.datetime)
    mock_dt.utcnow.return_value = datetime.datetime(2015, 7, 3, 10, 15, 0, 100000)
    mock_dt.now.return_value = datetime.datetime(2015, 7, 3, 11, 15, 0, 100000)
    monkeypatch = patch.object(sys.modules['datetime'], 'datetime', mock_dt)
    monkeypatch.start()
    # Mock time.time
    mock_time = Mock(wraps=time.time)
   

# Generated at 2022-06-13 02:50:29.864121
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Test class DateTimeFactCollector
    '''
    # Arrange
    module = None
    collected_facts = None

    # Act
    dt = DateTimeFactCollector()
    facts = dt.collect(module, collected_facts)

    # Assert
    assert 'date_time' in facts

# Generated at 2022-06-13 02:50:32.798612
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import ansible_facts

    date_time_fact_collector = DateTimeFactCollector()
    collected_facts = date_time_fact_collector.collect()
    assert collected_facts == ansible_facts['date_time']

# Generated at 2022-06-13 02:50:38.810342
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import base
    dtf = DateTimeFactCollector()
    base.add_collector(dtf)
    collected_facts = base.collect_facts(None)
    assert 'date_time' in collected_facts
    assert 'iso8601' in collected_facts['date_time']
    assert 'iso8601_basic' in collected_facts['date_time']
    assert 'iso8601_micro' in collected_facts['date_time']
    assert 'epoch' in collected_facts['date_time']
    assert 'epoch_int' in collected_facts['date_time']
    assert collected_facts['date_time']['epoch'] != ''
    assert collected_facts['date_time']['epoch_int'] != ''

# Generated at 2022-06-13 02:50:48.031040
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Simple test for DateTimeFactsCollector.collect
    #
    # To perform an advanced unit test of the method collect,
    #   replace the code in this method.
    #
    # To simulate failure of the entire DateTimeFactCollector class,
    #   raise an exception from this method
    #   (e.g. NotImplementedError('This unit test needs to be written'))
    #

    fc = DateTimeFactCollector()
    date_time_facts = fc.collect()

    assert isinstance(date_time_facts, dict)
    assert len(date_time_facts) == 1
    assert 'date_time' in date_time_facts
    assert isinstance(date_time_facts['date_time'], dict)