

# Generated at 2022-06-13 02:40:46.941454
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import datetime
    from ansible.module_utils.facts.collectors import date_time

    time_delta = 4
    time_format = '%Y%m%d %H%M%S'
    time_stamp = datetime.datetime.now()
    now = time_stamp.strftime(time_format)
    year = time_stamp.strftime('%Y')
    month = time_stamp.strftime('%m')
    weekday = time_stamp.strftime('%A')
    weekday_number = time_stamp.strftime('%w')
    weeknumber = time_stamp.strftime('%W')
    day = time_stamp.strftime('%d')
    hour = time_stamp.strftime('%H')
    minute = time_stamp.str

# Generated at 2022-06-13 02:40:48.745596
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Does the DateTimeFactCollector return a dictionary?
    assert isinstance(DateTimeFactCollector().collect(), dict)

# Generated at 2022-06-13 02:40:51.289212
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    collected_facts = fact_collector.collect()
    assert collected_facts['date_time']

# Generated at 2022-06-13 02:40:56.335307
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Tests the values returned by method collect of class DateTimeFactCollector
    for given sys properties
    
    Returns:
        None

    """
    dtfc = DateTimeFactCollector()
    date_time_facts = dtfc.collect()
    assert date_time_facts['date_time']['year'] == str(datetime.datetime.now().year)

# Generated at 2022-06-13 02:40:58.107393
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()

# Generated at 2022-06-13 02:41:00.215047
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    collected_facts = date_time_fact_collector.collect()
    'date_time' in collected_facts


# Generated at 2022-06-13 02:41:05.374371
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    years = list(range(1970, 2100))
    months = list(range(1, 12 + 1))
    days = list(range(1, 31 + 1))
    hours = list(range(0, 23 + 1))
    minutes = list(range(0, 60))
    seconds = list(range(0, 60))
    timezones = ['AST', 'BST', 'CST', 'EST', 'HST', 'MST', 'PST']

    for year in years:
        for month in months:
            for day in days:
                for hour in hours:
                    for minute in minutes:
                        for second in seconds:
                            for timezone in timezones:
                                date_time = datetime.datetime(year, month, day, hour, minute, second)
                                collection = DateTimeFactCollector.collect

# Generated at 2022-06-13 02:41:13.159118
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    import collections

    def to_dict(d):
        return dict(list(d.items()))

    # get the list of fact ids
    DateTimeFactCollector._fact_ids = set()
    DateTimeFactCollector.collect(collected_facts=None)
    fact_ids = DateTimeFactCollector._fact_ids

    # initialize the collector
    DateTimeFactCollector._fact_ids = set()
    datetime_fact_collector = DateTimeFactCollector()

    # get the facts
    facts = datetime_fact_collector.collect(None)

    # make sure all expected ids are present
    for key in fact_ids:
        assert key in facts['date_time']

    # make sure we have a dictionary with the right number of entries

# Generated at 2022-06-13 02:41:19.215685
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # GIVEN a DateTimeFactCollector instance
    dtfc = DateTimeFactCollector()

    # WHEN the collect method is called
    result = dtfc.collect()

    # THEN the result should be a dict
    assert isinstance(result, dict)
    # and the result should contain a key 'date_time'
    assert 'date_time' in result
    # and the key 'date_time' should be a dict
    assert isinstance(result['date_time'], dict)

# Generated at 2022-06-13 02:41:21.042135
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    dtf.populate()
    assert 'date_time' in dtf.collect()

# Generated at 2022-06-13 02:41:34.188946
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:41:43.973343
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create the DateTimeFactCollector object
    date_time_facts_obj = DateTimeFactCollector()
    # Test the method collect
    facts_dict = date_time_facts_obj.collect()

# Generated at 2022-06-13 02:41:53.393807
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    input_collect = DateTimeFactCollector()
    output = input_collect.collect()
    assert 'date_time' in output
    assert 'year' in output['date_time']
    assert 'month' in output['date_time']
    assert 'weekday' in output['date_time']
    assert 'weekday_number' in output['date_time']
    assert 'weeknumber' in output['date_time']
    assert 'day' in output['date_time']
    assert 'hour' in output['date_time']
    assert 'minute' in output['date_time']
    assert 'second' in output['date_time']
    assert 'epoch' in output['date_time']
    assert 'epoch_int' in output['date_time']
    assert 'date' in output['date_time']

# Generated at 2022-06-13 02:41:57.417293
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc_facts = dtfc.collect()
    assert dtfc_facts['date_time']['second'] == datetime.datetime.fromtimestamp(time.time()).strftime('%S')

# Generated at 2022-06-13 02:42:04.006014
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    datetime_fact_collector = DateTimeFactCollector()
    # Get the current time
    now = datetime.datetime.utcnow()
    # Run the method collect
    collect_dict = datetime_fact_collector.collect()
    # Assert that the all of the expected facts have been successfully collected
    assert 'date_time' in collect_dict
    assert 'year' in collect_dict['date_time']
    assert 'month' in collect_dict['date_time']
    assert 'weekday' in collect_dict['date_time']
    assert 'weekday_number' in collect_dict['date_time']
    assert 'weeknumber' in collect_dict['date_time']
    assert 'day' in collect_dict['date_time']
    assert 'hour' in collect_dict['date_time']
   

# Generated at 2022-06-13 02:42:07.487444
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    b = DateTimeFactCollector()
    result = b.collect()
    assert result['date_time']['weekday_number'] != ''

# Generated at 2022-06-13 02:42:16.034542
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    tz_dst = time.strftime("%Z", time.localtime(time.time()))
    tz_offset = time.strftime("%z", time.localtime(time.time()))

    facts_dict = DateTimeFactCollector().collect()

    assert facts_dict['date_time']['year'] == time.strftime("%Y", time.localtime(time.time()))
    assert facts_dict['date_time']['month'] == time.strftime("%m", time.localtime(time.time()))
    assert facts_dict['date_time']['weekday'] == time.strftime("%A", time.localtime(time.time()))

# Generated at 2022-06-13 02:42:26.559164
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    dtfc = DateTimeFactCollector()
    facts_dict = dtfc.collect()
    assert isinstance(dtfc, DateTimeFactCollector)
    assert isinstance(dtfc, BaseFactCollector)
    assert isinstance(facts_dict, dict)
    assert 'date_time' in facts_dict
    assert 'date' in facts_dict['date_time']
    assert 'time' in facts_dict['date_time']


# Generated at 2022-06-13 02:42:33.695222
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf_collector = DateTimeFactCollector()
    date_time_facts = dtf_collector.collect()['date_time']
    assert date_time_facts['year'] == time.strftime("%Y")
    assert date_time_facts['month'] == time.strftime("%m")
    assert date_time_facts['weekday'] == time.strftime("%A")
    assert date_time_facts['weekday_number'] == time.strftime("%w")
    assert date_time_facts['weeknumber'] == time.strftime("%W")
    assert date_time_facts['day'] == time.strftime("%d")
    assert date_time_facts['hour'] == time.strftime("%H")
    assert date_time_facts['minute'] == time.strftime("%M")

# Generated at 2022-06-13 02:42:42.330793
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Arrange
    #
    # Define test variables
    test_module = {}
    test_collected_facts = {}
    #
    # Act
    #
    # Call the collect method
    result = DateTimeFactCollector().collect(test_module, test_collected_facts)
    #
    # Assert
    #
    # Check that fact 'date_time' is present
    assert result['date_time'] is not None
    # Check that fact 'date_time' is a dictionary
    assert isinstance(result['date_time'], dict)
    # Check that a top-level key is present
    assert result['date_time']['epoch'] is not None
    # Check that a top-level key is present
    assert result['date_time']['epoch_int'] is not None
    #

# Generated at 2022-06-13 02:42:59.432864
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    test_data = fact_collector.collect()

# Generated at 2022-06-13 02:43:05.684074
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    collected_facts = collector.collect()
    assert 'date_time' in collected_facts
    assert isinstance(collected_facts['date_time'], dict)
    assert 'year' in collected_facts['date_time']
    assert 'epoch_int' in collected_facts['date_time']
    assert 'epoch' in collected_facts['date_time']
    assert 'time' in collected_facts['date_time']
    assert 'iso8601_basic_short' in collected_facts['date_time']
    assert 'iso8601_micro' in collected_facts['date_time']

# Generated at 2022-06-13 02:43:07.232671
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector.collect()

# Generated at 2022-06-13 02:43:08.301946
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc.collect()

# Generated at 2022-06-13 02:43:12.968905
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    ansible_facts = {}
    facts = fact_collector.collect(collected_facts=ansible_facts)
    assert type(facts['date_time']['epoch']) == str or type(facts['date_time']['epoch']) == unicode
    assert type(facts['date_time']['epoch_int']) == str
    assert facts['date_time']['epoch'].isdigit()
    assert facts['date_time']['epoch_int'].isdigit()

# Generated at 2022-06-13 02:43:24.005528
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
   c = DateTimeFactCollector()
   z = c.collect()

# Generated at 2022-06-13 02:43:35.498645
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import ansible_collections

# Generated at 2022-06-13 02:43:43.143546
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    facts = dt.collect()

# Generated at 2022-06-13 02:43:53.623011
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import collector_module

    # Init DateTimeFactCollector
    DateTimeFactCollector.init_module(collector_module)

    # call method collect of DateTimeFactCollector
    result = DateTimeFactCollector.collect()

    # Assert
    assert result.keys() == set(['date_time'])

# Generated at 2022-06-13 02:44:00.976923
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """ Test case for DateTimeFactCollector.collect """
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert 'date_time' in result
    assert result['date_time']['month'] == datetime.date.today().strftime('%m')
    assert result['date_time']['year'] == datetime.date.today().strftime('%Y')
    assert result['date_time']['tz_dst'] == time.tzname[1]
    assert result['date_time']['tz_offset'] == time.strftime("%z")
    assert result['date_time']['tz'] == time.strftime("%Z")
    assert result['date_time']['epoch'].isdigit()

# Generated at 2022-06-13 02:44:10.844169
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    t = DateTimeFactCollector()
    assert(isinstance(t.collect(), dict))

# Generated at 2022-06-13 02:44:22.655926
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    tz_dst = time.tzname[1]
    tz_offset = time.strftime("%z")
    now = datetime.datetime.now()
    utcnow = datetime.datetime.utcnow()
    epoch_ts = time.time()


# Generated at 2022-06-13 02:44:31.468560
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    timestamp = 1480690751
    epoch_stamp = datetime.datetime.fromtimestamp(timestamp)
    utc_now = datetime.datetime.utcfromtimestamp(timestamp)


# Generated at 2022-06-13 02:44:41.576846
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_collector = DateTimeFactCollector()
    facts_dict = test_collector.collect()
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
    assert 'epoch' in facts_dict['date_time']

# Generated at 2022-06-13 02:44:52.128472
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts_dict = collector.collect()
    assert isinstance(facts_dict, dict)
    assert 'date_time' in facts_dict
    assert isinstance(facts_dict['date_time'], dict)
    assert len(facts_dict['date_time']) == 17
    assert int(facts_dict['date_time']['epoch']) > 0
    assert int(facts_dict['date_time']['epoch_int']) > 0
    assert facts_dict['date_time']['epoch'] == facts_dict['date_time']['epoch_int']
    assert facts_dict['date_time']['year']
    assert int(facts_dict['date_time']['year']) > 2000

# Generated at 2022-06-13 02:45:01.873914
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    result = fact_collector.collect()
    assert 'date_time' in result
    assert 'year' in result['date_time']
    assert 'month' in result['date_time']
    assert 'weekday' in result['date_time']
    assert 'weekday_number' in result['date_time']
    assert 'day' in result['date_time']
    assert 'hour' in result['date_time']
    assert 'minute' in result['date_time']
    assert 'second' in result['date_time']
    assert 'epoch' in result['date_time']
    assert 'date' in result['date_time']
    assert 'time' in result['date_time']
    assert 'iso8601_micro' in result['date_time']


# Generated at 2022-06-13 02:45:07.378504
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    result = fact_collector.collect()
    # Just verify that there is content returned
    if not(result['date_time']):
        raise Exception("DateTimeFactCollector.collect() failed to return valid content")

if __name__ == '__main__':
    test_DateTimeFactCollector_collect()

# Generated at 2022-06-13 02:45:15.153153
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_collector = DateTimeFactCollector()
    test_facts_dict = test_collector.collect()

# Generated at 2022-06-13 02:45:20.336033
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    fact_collector = DateTimeFactCollector()
    result = fact_collector.collect()

    assert isinstance(result, dict)
    assert 'date_time' in result
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

# Generated at 2022-06-13 02:45:23.947818
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Create an instance of DateTimeFactCollector.
    date_time_fact_collector = DateTimeFactCollector()

    # Invoke date_time_fact_collector.collect()
    date_time_fact_collector.collect()

    # Test date_time_fact_collector.collect()

# Generated at 2022-06-13 02:45:47.484453
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    result = date_time_fact_collector.collect()
    assert result['date_time']['date'] == (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
    assert result['date_time']['day'] == (datetime.datetime.fromtimestamp(time.time()).strftime('%d'))
    assert result['date_time']['epoch'] == (datetime.datetime.fromtimestamp(time.time()).strftime('%s'))
    assert result['date_time']['epoch_int'] == str(int(datetime.datetime.fromtimestamp(time.time()).strftime('%s')))

# Generated at 2022-06-13 02:45:59.652325
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Test if DateTimeFactCollector.collect() returns expected results.
    '''
    # pylint: disable=import-error
    from ansible.module_utils.facts import ansible_collector

    collector = DateTimeFactCollector(
        ansible_collector,
        'ansible_date_time',
        {},
        {},
    )

    # This is horrible. Don't do this.
    # We just didn't want to test the entire date_time fact,
    # just that it has a value.
    # So we just test that some keys exist
    collected_facts = collector.collect()
    assert 'date_time' in collected_facts
    assert 'year' in collected_facts['date_time']
    assert 'iso8601' in collected_facts['date_time']


################################################################

# Generated at 2022-06-13 02:46:04.593554
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    val = dtfc.collect()
    assert 'date_time' in val
    assert 'hour' in val['date_time']
    assert val['date_time']['hour'].isdigit()
    assert len(val['date_time']) == 18

# Generated at 2022-06-13 02:46:05.786068
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:46:13.866857
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    facts_dict = dtf.collect()
    exp = ['date_time']
    assert sorted(facts_dict.keys()) == exp, \
        "Facts dict keys should contain 'date_time' but contains " + str(facts_dict.keys())
    dtf_facts = facts_dict['date_time']
    assert dtf_facts.has_key('year'), "date_time facts should contain 'year'"
    assert dtf_facts.has_key('month'), "date_time facts should contain 'month'"
    assert dtf_facts.has_key('weekday'), "date_time facts should contain 'weekday'"
    assert dtf_facts.has_key('weekday_number'), "date_time facts should contain 'weekday_number'"
    assert dtf_facts.has

# Generated at 2022-06-13 02:46:21.001814
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create an instance of the class DateTimeFactCollector, then call its
    #  method collect
    date_time_ins = DateTimeFactCollector()
    result = date_time_ins.collect()

    # Validate the result
    assert isinstance(result, dict)
    assert 'date_time' in result
    assert isinstance(result['date_time'], dict)
    for item in result['date_time']:
        assert isinstance(item, str)
        assert result['date_time'][item] != ''


# Generated at 2022-06-13 02:46:31.945408
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Instantiate DateTimeFactCollector object and call collect
    date_time_facts = DateTimeFactCollector()
    date_time_facts_dict = date_time_facts.collect()

    # Assert that epoch is an integer
    assert date_time_facts_dict['date_time']['epoch'].isdigit()

    # Assert that epoch_int is an integer
    assert date_time_facts_dict['date_time']['epoch_int'].isdigit()

    # Assert year is in format YYYY
    assert date_time_facts_dict['date_time']['year'].isdigit() and len(date_time_facts_dict['date_time']['year']) == 4

    # Assert month is in format MM

# Generated at 2022-06-13 02:46:40.559165
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts_dict = {}
    date_time_collector = DateTimeFactCollector()
    date_time_collector.collect()
    date_time_facts = date_time_collector.collect()
    assert 'date_time' in date_time_facts
    assert type(date_time_facts['date_time']) is dict
    assert 'date' in date_time_facts['date_time']
    assert 'day' in date_time_facts['date_time']
    assert 'epoch' in date_time_facts['date_time']
    assert 'epoch_int' in date_time_facts['date_time']
    assert 'time' in date_time_facts['date_time']
    assert 'tz' in date_time_facts['date_time']
    assert 'tz_dst' in date_

# Generated at 2022-06-13 02:46:50.477126
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()


# Generated at 2022-06-13 02:47:00.696441
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_dict = {}

# Generated at 2022-06-13 02:47:38.132260
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    assert (dtf.collect()['date_time']['weekday'] == datetime.datetime.now().strftime('%A'))
    dtf.name = ''
    assert (dtf.collect() == {})

# Generated at 2022-06-13 02:47:43.092827
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    result = date_time_fact_collector.collect()
    assert result.get('date_time')
    assert result['date_time'].get('year')


if __name__ == '__main__':
    test_DateTimeFactCollector_collect()

# Generated at 2022-06-13 02:47:51.244900
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    class TestModule(object):
        def __init__(self):
            self.params = {'gather_subset':['all'], 'gather_timeout':10}

    # Call DateTimeFactCollector.collect()
    test_collector = DateTimeFactCollector(TestModule())
    facts = test_collector.collect()

    # Check the facts to ensure it matches the current time on the host
    # we assume that time.time() is the same as datetime.datetime.now()
    # if not, then this unit test will fail.
    dt = datetime.datetime.now()

# Generated at 2022-06-13 02:47:53.353046
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create the test object
    date_fact_collector = DateTimeFactCollector()

    # Call the method
    date_fact_collector.collect()

# Generated at 2022-06-13 02:48:00.744885
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Execute collect method of DateTimeFactCollector object
    '''
    datetime_fact_collector = DateTimeFactCollector()
    date_time_facts = datetime_fact_collector.collect()
    # Assert that we have year, month and day in the date_time facts
    assert ('year' in date_time_facts['date_time'])
    assert ('month' in date_time_facts['date_time'])
    assert ('day' in date_time_facts['date_time'])

# Generated at 2022-06-13 02:48:02.058699
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    assert(DateTimeFactCollector().collect().keys() == {'date_time', 'ansible_localtime'})

# Generated at 2022-06-13 02:48:10.568445
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Test the method collect of class DateTimeFactCollector
    '''
    fact_collector = DateTimeFactCollector()
    ansible_facts = fact_collector.collect()
    # make sure the timestamp was captured
    assert ansible_facts['date_time']['epoch']
    # make sure the timestamp was captured
    assert ansible_facts['date_time']['epoch_int']
    # make sure the datetime was captured
    assert ansible_facts['date_time']['date']

test__all__ = [test_DateTimeFactCollector_collect]

# Generated at 2022-06-13 02:48:22.154782
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Fact: date_time
    """
    dtf = DateTimeFactCollector(None, None, None)

    # Test the method with a valid current time
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)
    facts = dtf.collect()
    assert facts is not None
    assert 'date_time' in facts.keys()
    dateTime = facts['date_time']
    assert dateTime is not None
    assert 'iso8601_micro' in dateTime
    assert dateTime['iso8601_micro'] == utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# Generated at 2022-06-13 02:48:34.125786
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Verify only one year is present
    dt = DateTimeFactCollector()
    dt_info = dt.collect()
    assert all(word in dt_info['date_time']['iso8601'] for word in ('-', 'T', ':', 'Z'))
    assert dt_info['date_time']['iso8601_micro'].count('.') == 1
    assert all(word in dt_info['date_time']['iso8601_basic'] for word in ('-', ':', '.'))
    assert all(word in dt_info['date_time']['iso8601_basic_short'] for word in ('-', ':'))
    assert len(dt_info['date_time']['iso8601_micro'].split('.')[1] ) == 6


# Generated at 2022-06-13 02:48:39.059156
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Create a new instance of DateTimeFactCollector
    instance_of_DateTimeFactCollector = DateTimeFactCollector()

    # Call method collect of class DateTimeFactCollector
    # Test version - return empty dictionary
    # Test id: 1
    result = instance_of_DateTimeFactCollector.collect()
    assert result == {"ansible_date_time": {}}


# Generated at 2022-06-13 02:49:52.278786
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Mock datetime
    from datetime import datetime
    epoch = datetime.utcfromtimestamp(0)
    def mock_utcnow():
        return epoch
    datetime.utcnow = mock_utcnow

    # Mock time
    import time
    def mock_strftime(format_str):
        if format_str == '%Y':
            return '1970'
        elif format_str == '%m':
            return '01'
        elif format_str == '%w':
            return '4'
        elif format_str == '%W':
            return '01'
        elif format_str == '%d':
            return '01'
        elif format_str == '%H':
            return '00'

# Generated at 2022-06-13 02:50:02.064742
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # create singleton of DateTimeFactCollector
    date_time_fact_collector = DateTimeFactCollector()

    # "collect" method always return the same results
    # so we can test it with a snapshot

# Generated at 2022-06-13 02:50:07.617384
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector('date_time')
    facts = dtfc.collect()
    assert facts['date_time']['year'] == time.strftime('%Y')
    assert facts['date_time']['month'] == time.strftime('%m')
    assert facts['date_time']['weekday'] == time.strftime('%A')
    assert facts['date_time']['weekday_number'] == time.strftime('%w')
    assert facts['date_time']['weeknumber'] == time.strftime('%W')
    assert facts['date_time']['day'] == time.strftime('%d')
    assert facts['date_time']['hour'] == time.strftime('%H')
    assert facts['date_time']['minute'] == time

# Generated at 2022-06-13 02:50:17.420582
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Unit test for method collect of class DateTimeFactCollector."""

    # Create the class under test
    test_dtfc = DateTimeFactCollector()

    # Create the expected result

# Generated at 2022-06-13 02:50:26.995575
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    date_time_collector = DateTimeFactCollector()
    ansible_facts = date_time_collector.collect()

    assert isinstance(ansible_facts, dict), "collected facts are not a dictionary"

    date_time_facts = ansible_facts.get('date_time')

    assert date_time_facts is not None, "collected facts did contain date_time facts"

    assert 'year' in date_time_facts, "collected facts did not contain year fact"
    assert 'month' in date_time_facts, "collected facts did not contain month fact"
    assert 'weekday' in date_time_facts, "collected facts did not contain weekday fact"
    assert 'weekday_number' in date_time_facts, "collected facts did not contain weekday_number fact"
    assert 'weeknumber'

# Generated at 2022-06-13 02:50:32.931283
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:50:37.479237
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Test DateTimeFactCollector class.
    """
    date_time_fact_collector = DateTimeFactCollector()
    date_time = date_time_fact_collector.collect()
    assert 'date_time' in date_time
    assert 'iso8601_micro' in date_time['date_time']

# Generated at 2022-06-13 02:50:45.300275
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector.collect()
    date_time = date_time_fact_collector.collect()['date_time']
    assert date_time['zone'] == str(time.strftime("%Z")),"zone is not %s" %(str(time.strftime("%Z")))
    assert date_time['month'] == time.strftime("%m"),"month is not %s" %(str(time.strftime("%m")))