

# Generated at 2022-06-13 02:40:55.418427
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    result = collector.collect()
    require(result.get('date_time').get('year'))
    require(result.get('date_time').get('month'))
    require(result.get('date_time').get('weekday'))
    require(result.get('date_time').get('weekday_number'))
    require(result.get('date_time').get('weeknumber'))
    require(result.get('date_time').get('day'))
    require(result.get('date_time').get('hour'))
    require(result.get('date_time').get('minute'))
    require(result.get('date_time').get('second'))
    require(result.get('date_time').get('epoch'))

# Generated at 2022-06-13 02:40:57.600198
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    collected_facts = {}
    collected_facts = dtf.collect(None, collected_facts)
    return collected_facts


# Generated at 2022-06-13 02:40:59.485129
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Initialize
    dtfc = DateTimeFactCollector()
    # Call the collect method
    dtfc.collect()

# Generated at 2022-06-13 02:41:10.072097
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Initialize the collector and get initial facts
    dtf = DateTimeFactCollector()
    dtf.collect()
    # Initialize a dictionary to compare with the collect method
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)
    date_time_facts = {}
    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
    date_time_facts['weekday_number'] = now.strftime('%w')

# Generated at 2022-06-13 02:41:11.248042
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector().collect()

# Generated at 2022-06-13 02:41:12.366435
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    d = DateTimeFactCollector()
    d.collect()

# Generated at 2022-06-13 02:41:22.454016
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_obj = DateTimeFactCollector(None, None)

    # Test with no error
    result = test_obj.collect()

# Generated at 2022-06-13 02:41:27.086478
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Test function for DateTimeFactCollector.collect()
    This function is a unit test for collecting facts from DateTimeFactCollector
    """

    date_time_facts_collector_obj = DateTimeFactCollector()
    date_time_facts = date_time_facts_collector_obj.collect()
    assert 'date_time' in date_time_facts
    assert 'year' in date_time_facts['date_time']

# Generated at 2022-06-13 02:41:36.098473
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import ansible.module_utils.facts.facts
    from ansible.module_utils.facts import default_collectors

    default_collectors['date_time'] = DateTimeFactCollector

    results = ansible.module_utils.facts.facts.get_facts(module_args=dict(filter='*'))

# Generated at 2022-06-13 02:41:46.032304
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Test that DateTimeFactCollector.collect returns a dictionary with the
    correct keys
    '''
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.date_time import DateTimeFactCollector
    DUT = DateTimeFactCollector(BaseFactCollector, '', {})
    dt_dict = DUT.collect()
    assert isinstance(dt_dict, dict)
    assert 'date_time' in dt_dict
    assert 'epoch_int' in dt_dict['date_time']
    assert 'weekday_number' in dt_dict['date_time']
    assert 'iso8601_basic_short' in dt_dict['date_time']
    assert 'tz_offset' in dt_

# Generated at 2022-06-13 02:41:56.493433
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:42:03.192188
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    dt_result = dt.collect()
    assert type(dt_result) is dict
    assert 'date_time' in dt_result
    assert 'epoch' in dt_result['date_time']
    assert 'epoch_int' in dt_result['date_time']
    assert 'month' in dt_result['date_time']
    assert 'tz_dst' in dt_result['date_time']
    assert 'tz_offset' in dt_result['date_time']
    assert 'weekday' in dt_result['date_time']
    assert dt_result['date_time']['epoch'].isdigit()
    assert dt_result['date_time']['epoch_int'].isdigit()


# Generated at 2022-06-13 02:42:09.108105
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts_dict = date_time_fact_collector.collect()
    assert ('date_time' in date_time_facts_dict)
    assert ('epoch' in date_time_facts_dict['date_time'])


# Generated at 2022-06-13 02:42:13.525725
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Test method collect of class DateTimeFactCollector
    """
    collector = DateTimeFactCollector('ansible.module_utils.facts.collector', '', ',')
    result = collector.collect()
    assert type(result.get('date_time')) is dict
    assert result.get('date_time').get('year')

# Generated at 2022-06-13 02:42:27.208384
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_collector = DateTimeFactCollector()
    assert dt_collector.collect()['date_time']['year'] == str(datetime.datetime.now().year)
    assert dt_collector.collect()['date_time']['month'] == str(datetime.datetime.now().strftime("%m"))
    assert dt_collector.collect()['date_time']['weekday'] == datetime.datetime.now().strftime("%A")
    assert dt_collector.collect()['date_time']['weekday_number'] == str(datetime.datetime.now().strftime("%w"))
    assert dt_collector.collect()['date_time']['weeknumber'] == str(datetime.datetime.now().strftime("%W"))
   

# Generated at 2022-06-13 02:42:28.662696
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # test with empty parameters
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert result

# Generated at 2022-06-13 02:42:32.499431
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts import facts

    c = DateTimeFactCollector()

    # set some data in the cache
    c.collect()
    facts.FACTS_CACHE['ansible_date_time'] = c.get_facts()

    # get data from cache
    data = c.collect()
    # data should have some values
    assert len(data['date_time']) > 0

# Generated at 2022-06-13 02:42:36.983457
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    def collect(Module):
        c = DateTimeFactCollector(Module)
        c.collect()
        return c.data

    class DummyModule(object):
        def __init__(self, params):
            self.params = params

        def fail_json(self, msg):
            raise Exception(msg)

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return executable

    # Test that all the fields are set
    dm = DummyModule({})
    dt = collect(dm)
    dt_fields = dt['date_time']
    assert dt_fields['year']
    assert dt_fields['month']
    assert dt_fields['weekday']
    assert dt_fields['weekday_number']

# Generated at 2022-06-13 02:42:46.545576
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test the method DateTimeFactCollector.collect with valid input
    df = DateTimeFactCollector()
    result = df.collect()
    # Check if result is a dict
    assert isinstance(result, dict)
    # Check if keys in dict are as expected
    assert set(result.keys()) == set(['date_time'])
    assert isinstance(result['date_time'], dict)

# Generated at 2022-06-13 02:42:51.659220
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Setup the test object
    a = DateTimeFactCollector()

    # Create dictionary of facts to return
    facts = {}

    # Call the collect method
    a.collect(collected_facts=facts)

    # Assert that the method returned a dictionary
    assert isinstance(facts, dict)

# Generated at 2022-06-13 02:43:03.037328
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts = DateTimeFactCollector().collect()
    assert isinstance(facts['date_time']['epoch'], str)
    assert isinstance(facts['date_time']['epoch_int'], str)
    assert isinstance(facts['date_time']['tz_offset'], str)
    assert isinstance(facts['date_time']['weekday_number'], str)
    assert isinstance(facts['date_time']['year'], str)
    assert isinstance(facts['date_time']['month'], str)
    assert isinstance(facts['date_time']['weekday'], str)
    assert isinstance(facts['date_time']['weeknumber'], str)
    assert isinstance(facts['date_time']['day'], str)

# Generated at 2022-06-13 02:43:11.176317
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert result['date_time']['weekday'] == time.strftime("%A")
    assert result['date_time']['epoch'] == time.strftime("%s")
    assert result['date_time']['epoch_int'] == str(int(time.time()))
    assert result['date_time']['iso8601_micro'] == time.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert result['date_time']['iso8601_basic'] == time.strftime("%Y%m%dT%H%M%S%f")
    assert result['date_time']['tz_dst'] == time.strftime("%Z")
    assert result

# Generated at 2022-06-13 02:43:23.447055
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_module = DateTimeFactCollector()
    result = fact_module.collect()
    assert result is not None
    assert result['date_time'] is not None
    assert result['date_time']['year'] is not None
    assert result['date_time']['month'] is not None
    assert result['date_time']['weekday'] is not None
    assert result['date_time']['weekday_number'] is not None
    assert result['date_time']['weeknumber'] is not None
    assert result['date_time']['day'] is not None
    assert result['date_time']['hour'] is not None
    assert result['date_time']['minute'] is not None
    assert result['date_time']['second'] is not None

# Generated at 2022-06-13 02:43:34.411462
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Unit test method to test collect method of class DateTimeFactCollector
    """
    date_time_facts = DateTimeFactCollector()

    date_time_facts_dict = date_time_facts.collect()

    assert date_time_facts_dict.has_key('date_time')

    for key in ('year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day', 'hour',
                'minute', 'second', 'epoch', 'epoch_int',
                'date', 'time', 'iso8601', 'iso8601_micro', 'iso8601_basic', 'iso8601_basic_short',
                'tz', 'tz_dst', 'tz_offset'):
        assert date_time_facts_dict['date_time'].has_key(key)

# Generated at 2022-06-13 02:43:37.245229
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    data_time_collector = DateTimeFactCollector()
    data_time_facts = data_time_collector.collect()
    assert(data_time_facts.get('date_time', None) is not None)

# Generated at 2022-06-13 02:43:47.230902
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Read in test data
    test_data = {}
    with open('/tmp/ansible_date_time_facts.json', 'r') as f:
        test_data = json.load(f)

    # Instantiate DateTimeFactCollector and call collect
    dfc = DateTimeFactCollector()
    output = dfc.collect()

    # Get expected values from test data
    expected = test_data['ansible_date_time']
    # Get actual values from collect method
    actual = output['date_time']

    # Assert that the expected dictionary is equal to the actual dictionary
    assert expected == actual


# Generated at 2022-06-13 02:43:49.777108
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    facts_dict = {}
    result = DateTimeFactCollector().collect(collected_facts=facts_dict)
    assert result.get('date_time') is not None

# Generated at 2022-06-13 02:43:57.157019
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    output = dt.collect()

    assert 'date_time' in output
    assert len(output['date_time']) > 1
    assert 'month' in output['date_time']
    assert 'time' in output['date_time']
    assert 'iso8601_micro' in output['date_time']

    assert len(output['date_time']['month']) == 2
    assert len(output['date_time']['time'].split(':')) == 3
    assert len(output['date_time']['iso8601_micro'].split(':')) == 4

# Generated at 2022-06-13 02:43:58.249372
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    col = DateTimeFactCollector()
    col.collect()


# Generated at 2022-06-13 02:44:03.820321
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Arrange
    test_subject = DateTimeFactCollector()

    # Act
    results = test_subject.collect()

    # Assert
    date_time_facts = results['date_time']
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
    assert date_time_facts['epoch_int']

# Generated at 2022-06-13 02:44:22.948922
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Arrange
    module = AnsibleModuleMock()
    facts_dict = {}
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    # Act
    date_time_fact_collector = DateTimeFactCollector()
    facts_dict = date_time_fact_collector.collect(module, facts_dict)

    # Assert
    assert facts_dict['date_time']['year'] == now.strftime('%Y')
    assert facts_dict['date_time']['month'] == now.strftime('%m')
    assert facts_dict['date_time']['weekday'] == now.strftime('%A')
    assert facts

# Generated at 2022-06-13 02:44:31.709954
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact = DateTimeFactCollector()

    date_time_facts = date_time_fact.collect()['date_time']

    assert 'year' in date_time_facts
    assert 'month' in date_time_facts
    assert 'weekday' in date_time_facts
    assert 'weekday_number' in date_time_facts
    assert 'weeknumber' in date_time_facts
    assert 'day' in date_time_facts
    assert 'hour' in date_time_facts
    assert 'minute' in date_time_facts
    assert 'second' in date_time_facts
    assert 'epoch_int' in date_time_facts
    assert 'epoch' in date_time_facts
    assert 'date' in date_time_facts
    assert 'time' in date_time_facts

# Generated at 2022-06-13 02:44:34.110093
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    ft = DateTimeFactCollector()
    assert "date_time" in ft.collect()

# Generated at 2022-06-13 02:44:38.733307
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Setup
    date_time_collector = DateTimeFactCollector()

    # Execute
    date_time_facts = date_time_collector.collect()

# Generated at 2022-06-13 02:44:48.207760
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import datetime
    import time
    DateTimeFactCollector_instance = DateTimeFactCollector()

    # We need to replace datetime.datetime.now() because we can't set the current time
    # (e.g. we can't set the timezone in the module_utils)

    class MyDateTime(datetime.datetime):
        def __new__(cls, *args, **kwargs):
            return super(MyDateTime, cls).__new__(cls, *args, **kwargs)

        @classmethod
        def now(cls, *args, **kwargs):
            return cls(2010, 1, 1, 12, 0, 0)
    old_class = datetime.datetime
    datetime.datetime = MyDateTime


# Generated at 2022-06-13 02:44:52.073678
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Test DateTimeFactCollector.collect()
    '''
    dtfc = DateTimeFactCollector()
    dtfc.collect()
    assert 'date_time' in dtfc.collect()

# Generated at 2022-06-13 02:44:57.151852
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    DateTimeFactCollector collects data and time related facts
    '''
    c = DateTimeFactCollector()
    facts = c.collect(None, None)
    assert facts['date_time']['month'] == datetime.datetime.now().strftime('%m')

# Generated at 2022-06-13 02:44:59.401895
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    result = collector.collect()

    assert result['date_time']['iso8601'][-1] == 'Z'

# Generated at 2022-06-13 02:45:06.917486
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    args = dict(
        module=dict(
            params=dict(),
            tmpdir="/path/to/directory",
            connection=dict(
                network_os="NetworkOS",
                _socket_path="/dev/null",
                stdin="",
                stdout="",
            ),
        ),
        collected_facts=dict(),
    )
    dtfc = DateTimeFactCollector(**args)

    result = dtfc.collect(**args)
    assert 'date_time' in result

# Generated at 2022-06-13 02:45:14.804807
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Create test object
    dtfc = DateTimeFactCollector()

    # We mock the datetime module to always be in a fixed date/time
    mock_datetime = datetime.datetime(2019, 2, 15, 11, 37, 21, 1234)

    # We mock the time module to always be in a fixed date/time
    mock_time = datetime.datetime(2019, 2, 15, 13, 37, 21, 1234)

    # We mock the datetime module to always be in a fixed date/time
    with mock.patch.object(datetime.datetime, 'datetime', mock_datetime):
        # We mock the time module to always be in a fixed date/time
        with mock.patch.object(datetime, 'time', mock_time):
            result = dtfc.collect()

    # We

# Generated at 2022-06-13 02:45:42.339014
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    assert 'date_time' in date_time_facts
    assert 'hour' in date_time_facts['date_time']
    assert 'minute' in date_time_facts['date_time']
    assert 'second' in date_time_facts['date_time']
    assert 'epoch' in date_time_facts['date_time']
    assert 'epoch_int' in date_time_facts['date_time']
    assert 'date' in date_time_facts['date_time']
    assert 'time' in date_time_facts['date_time']
    assert 'iso8601_micro' in date_time_facts['date_time']

# Generated at 2022-06-13 02:45:49.587066
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Test return of date_time facts"""

    # populate facts dict with date_time facts
    date_fact = DateTimeFactCollector()
    facts = date_fact.collect()

    # test return of date_time facts
    assert facts['date_time']['date'] == time.strftime("%Y-%m-%d")
    assert facts['date_time']['day'] == time.strftime("%d")
    assert facts['date_time']['epoch'] == time.strftime("%s")
    assert facts['date_time']['hour'] == time.strftime("%H")

# Generated at 2022-06-13 02:45:54.326958
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Note: this test is a best-effort since the epoch timestamp is different for every invocation
    #       and even within the test code the epoch_ts value varies.
    # Arrange
    dtf = DateTimeFactCollector()
    dtf.collect()
    # Act
    epoch_int = int(dtf.get_fact('epoch_int'))
    epoch = int(dtf.get_fact('epoch'))
    # Assert
    assert dtf.get_fact('year') == '2018'
    assert dtf.get_fact('month') == '08'
    assert dtf.get_fact('weekday') == 'Tuesday'
    assert dtf.get_fact('weekday_number') == '2'
    assert dtf.get_fact('weeknumber') == '33'

# Generated at 2022-06-13 02:46:05.190266
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_collector = DateTimeFactCollector()
    date_time_facts = date_time_collector.collect()
    assert date_time_facts is not None
    assert 'date_time' in date_time_facts
    assert 'date' in date_time_facts['date_time']
    assert 'time' in date_time_facts['date_time']
    assert 'epoch' in date_time_facts['date_time']
    assert 'epoch_int' in date_time_facts['date_time']
    assert 'iso8601' in date_time_facts['date_time']
    assert 'iso8601_micro' in date_time_facts['date_time']

# Generated at 2022-06-13 02:46:13.536121
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import os
    import sys
    import inspect
    import time
    import pytest
    from ansible.module_utils.facts.collector import BaseFactCollector
    # Get the path to the directory containing this module
    module_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # Add that path to the system search path
    sys.path.append(module_path)
    # And import the module
    from date_time_fact_collector import DateTimeFactCollector

    # Create an instance of the class
    dtf_factor = DateTimeFactCollector()

    # Call the collect method with a module and a fact collection object
    facts_dict = dtf_factor.collect()

    # Test if the method returned a dictionary

# Generated at 2022-06-13 02:46:23.768773
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Initialize a DateTimeFactCollector object
    dt_collector = DateTimeFactCollector()

    # Call the collect function of DateTimeFactCollector object
    dt_facts = dt_collector.collect()
    assert dt_facts is not None, "DateTimeFactCollector collect method is broken."
    assert type(dt_facts) is dict, "DateTimeFactCollector collect method returns other than dict."
    assert 'date_time' in dt_facts, "DateTimeFactCollector collect method returns other than dict."
    dt_dict = dt_facts['date_time']
    assert type(dt_dict) is dict, "DateTimeFactCollector collect method returns other than dict."
    assert 'year' in dt_dict, "DateTimeFactCollector collect method returns other than dict."

# Generated at 2022-06-13 02:46:34.801220
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)


# Generated at 2022-06-13 02:46:42.173914
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:46:51.261993
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    '''
    Unit test for method collect of class DateTimeFactCollector
    '''
    # Instantiate the DateTimeFactCollector class
    dtfc = DateTimeFactCollector()

    # Invoke the collect method
    dtfc_result = dtfc.collect()

    # Returned value should have a dictionary with a dictionary entry 'date_time'
    assert 'date_time' in dtfc_result
    # Returned value should have a dictionary with a dictionary entry 'date_time', which itself
    # is a dictionary with keys 'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
    # 'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time', 'iso8601_micro', 'iso8601',
    # 'iso8601

# Generated at 2022-06-13 02:47:00.337824
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    datetime_fact_collector = DateTimeFactCollector({}, None, None)

    facts_dict = datetime_fact_collector.collect()
    datetime_facts = facts_dict['date_time']

    assert isinstance(datetime_facts['iso8601_micro'], str)
    assert isinstance(datetime_facts['iso8601'], str)
    assert isinstance(datetime_facts['iso8601_basic'], str)
    assert isinstance(datetime_facts['iso8601_basic_short'], str)
    assert isinstance(datetime_facts['epoch'], str)
    assert isinstance(datetime_facts['epoch_int'], str)

# Generated at 2022-06-13 02:47:21.650009
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Unit test for method collect of class DateTimeFactCollector
    """

    # Build the test DateTimeFactCollector
    test_date_time_fact_collector = DateTimeFactCollector()
    test_date_time_fact_collector.collect()

    # TODO: Add assert statements to test that the resulting facts are correct

# Generated at 2022-06-13 02:47:27.824676
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector()
    date_facts = date_time_facts.collect()
    assert 'date_time' in date_facts.keys()
    assert 'month' in date_facts['date_time'].keys()
    assert 'iso8601_micro' in date_facts['date_time'].keys()
    assert 'tz_dst' in date_facts['date_time'].keys()
    assert 'tz' in date_facts['date_time'].keys()
    assert 'day' in date_facts['date_time'].keys()
    assert 'year' in date_facts['date_time'].keys()
    assert 'iso8601_basic_short' in date_facts['date_time'].keys()
    assert 'time' in date_facts['date_time'].keys()

# Generated at 2022-06-13 02:47:38.774678
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time = DateTimeFactCollector()

# Generated at 2022-06-13 02:47:48.508967
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    res = dtf.collect()
    assert res.get('date_time')
    date_time_facts = res.get('date_time')
    assert date_time_facts
    assert date_time_facts.get('year')
    assert date_time_facts.get('month')
    assert date_time_facts.get('weekday')
    assert date_time_facts.get('weekday_number')
    assert date_time_facts.get('weeknumber')
    assert date_time_facts.get('day')
    assert date_time_facts.get('hour')
    assert date_time_facts.get('minute')
    assert date_time_facts.get('second')
    assert date_time_facts.get('date')
    assert date_time_facts.get

# Generated at 2022-06-13 02:47:50.889203
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    dtf.collect()
    assert dtf._fact_ids == set(('date_time',))

# Generated at 2022-06-13 02:47:53.320563
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    d = DateTimeFactCollector()
    result = d.collect()
    assert result['date_time']
    assert len(result['date_time']) == 21

# Generated at 2022-06-13 02:48:00.061662
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts = collector.collect()
    date_time_facts = facts.get('date_time')
    assert date_time_facts['month'] == '11'
    assert date_time_facts['weekday_number'] == '6'
    assert date_time_facts['day'] == '23'
    assert date_time_facts['hour'] == '17'
    assert date_time_facts['minute'] == '41'

# Generated at 2022-06-13 02:48:06.611602
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    assert collector.collect()['date_time']['day'] == datetime.datetime.now().strftime('%d')
    assert collector.collect()['date_time']['month'] == datetime.datetime.now().strftime('%m')
    assert collector.collect()['date_time']['year'] == datetime.datetime.now().strftime('%Y')
    assert collector.collect()['date_time']['weekday'] == datetime.datetime.now().strftime('%A')
    assert collector.collect()['date_time']['weeknumber'] == datetime.datetime.now().strftime('%W')
    assert collector.collect()['date_time']['hour'] == datetime.datetime.now().strftime('%H')
   

# Generated at 2022-06-13 02:48:19.532884
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fc = DateTimeFactCollector()
    fc.collect()
    # Convert dict to list of tuples for ease of comparison
    fc_dict_list = list()
    for key, value in fc.collect().items():
        fc_dict_list.append((key, value))

# Generated at 2022-06-13 02:48:21.772570
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    result = dt.collect()
    assert result is not None
    assert type(result) == dict

# Generated at 2022-06-13 02:48:55.806810
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    col = DateTimeFactCollector()
    dt_facts = col.collect()
    date_time_facts = dt_facts['date_time']

    # test that the key-value pairs are NOT empty
    for key in date_time_facts:
        assert date_time_facts[key] != ''


# Generated at 2022-06-13 02:49:07.084703
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Test that DateTimeFactCollector.collect returns expected dict.
    """

    collected_facts = dict()

    # Patch datetime.datetime.utcfromtimestamp to return fixed datetime
    # object.
    def patched_utc_from_timestamp(ts):
        return datetime.datetime(2016, 1, 19, 23, 43, 20, 5)

    import ansible.module_utils.facts.system.date_time
    ansible.module_utils.facts.system.date_time.datetime.utcfromtimestamp = patched_utc_from_timestamp


# Generated at 2022-06-13 02:49:09.322182
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """
    Test DateTimeFactCollector.collect()
    """
    dtf = DateTimeFactCollector()
    facts = dtf.collect()

    assert 'epoch' in facts['date_time']
    assert 'date_time' in facts

# Generated at 2022-06-13 02:49:15.791389
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert "date_time" in result
    assert "epoch" in result["date_time"]
    assert "epoch_int" in result["date_time"]
    assert "date" in result["date_time"]
    assert "time" in result["date_time"]
    assert "iso8601_micro" in result["date_time"]
    assert "iso8601" in result["date_time"]
    assert "iso8601_basic" in result["date_time"]
    assert "tz" in result["date_time"]
    assert "tz_dst" in result["date_time"]
    assert "tz_offset" in result["date_time"]

# Generated at 2022-06-13 02:49:26.348156
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    result = dtfc.collect()
    assert 'date_time' in result
    assert type(result['date_time']) is dict
    assert 'weeknumber' in result['date_time']
    assert type(result['date_time']['weeknumber']) is str
    assert 'tz_dst' in result['date_time']
    assert type(result['date_time']['tz_dst']) is str
    assert 'epoch' in result['date_time']
    assert type(result['date_time']['epoch']) is str
    # We cannot accurately test if epoch is an integer as, for example, a
    # float of 2.0 is accepted as an integer and will not raise an exception
    # if we try an int(2.0)


# Generated at 2022-06-13 02:49:37.660662
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2022-06-13 02:49:40.446598
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_fc = DateTimeFactCollector()
    dt_fc.collect()

# Generated at 2022-06-13 02:49:42.343731
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_fact_collector.collect()

# Generated at 2022-06-13 02:49:52.975265
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()['date_time']
    assert date_time_facts['year'].isdigit()
    assert date_time_facts['month'].isdigit()
    assert date_time_facts['weekday'].isalpha()
    assert date_time_facts['weekday_number'].isdigit()
    assert date_time_facts['weeknumber'].isdigit()
    assert date_time_facts['day'].isdigit()
    assert date_time_facts['hour'].isdigit()
    assert date_time_facts['minute'].isdigit()
    assert date_time_facts['second'].isdigit()

# Generated at 2022-06-13 02:50:02.684899
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    f = DateTimeFactCollector()
    facts = f.collect()
    assert 'date_time' in facts
    facts = facts['date_time']
    assert 'year' in facts
    assert 'month' in facts
    assert 'weekday' in facts
    assert 'weekday_number' in facts
    assert 'weeknumber' in facts
    assert 'day' in facts
    assert 'hour' in facts
    assert 'minute' in facts
    assert 'second' in facts
    assert 'epoch' in facts
    assert 'epoch_int' in facts
    assert 'date' in facts
    assert 'time' in facts
    assert 'iso8601_micro' in facts
    assert 'iso8601' in facts
    assert 'iso8601_basic' in facts
    assert 'iso8601_basic_short' in facts
