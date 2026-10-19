

# Generated at 2022-06-13 02:40:53.239363
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    class TestDateTimeFactCollector(DateTimeFactCollector):
        def __init__(self):
            super(DateTimeFactCollector, self).__init__()
            self.test_set_date_time_facts()

        def test_set_date_time_facts(self):
            now = datetime.datetime.fromtimestamp(1543509360.0)
            self._set_date_time_facts(now)

    date_time_fact_collector = TestDateTimeFactCollector()

    # Standard
    date_time_facts = date_time_fact_collector.collect()['date_time']
    assert date_time_facts['year'] == '2018'
    assert date_time_facts['month'] == '12'
    assert date_time_facts['weekday'] == 'Wednesday'
   

# Generated at 2022-06-13 02:40:56.413750
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    c = DateTimeFactCollector()
    facts_dict = c.collect()
    assert 'date_time' in facts_dict
    assert facts_dict['date_time']['weekday'] in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Generated at 2022-06-13 02:41:06.496260
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Arrange
    date_time_fact_collector = DateTimeFactCollector()

    # Act
    result = date_time_fact_collector.collect()

    # Assert
    assert result is not None
    assert result['date_time'] is not None
    assert result['date_time']['year'] is not None
    assert result['date_time']['month'] is not None
    assert result['date_time']['weekday'] is not None
    assert result['date_time']['weekday_number'] is not None
    assert result['date_time']['day'] is not None
    assert result['date_time']['weeknumber'] is not None
    assert result['date_time']['hour'] is not None
    assert result['date_time']['minute'] is not None
   

# Generated at 2022-06-13 02:41:09.407030
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_collector = DateTimeFactCollector()
    date_time = dt_collector.collect()
    print(date_time)

# Generated at 2022-06-13 02:41:10.244898
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DateTimeFactCollector()

# Generated at 2022-06-13 02:41:15.190427
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Arrange
    DateTimeFactCollector.name = 'date_time'
    DateTimeFactCollector._fact_ids = set()
    module = ''
    collected_facts = ''
    # Act
    result = DateTimeFactCollector.collect(module, collected_facts)
    # Assert
    assert result != ''

# Generated at 2022-06-13 02:41:23.869399
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    epoch_ts = 1500000000
    facts_dict = {}
    date_time_facts = {}

    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    date_time_facts['year'] = now.strftime('%Y')
    date_time_facts['month'] = now.strftime('%m')
    date_time_facts['weekday'] = now.strftime('%A')
    date_time_facts['weekday_number'] = now.strftime('%w')
    date_time_facts['weeknumber'] = now.strftime('%W')
    date_time_facts['day'] = now.strftime('%d')
    date_time_facts['hour'] = now.strftime

# Generated at 2022-06-13 02:41:30.065867
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt_fact = DateTimeFactCollector(None)
    gathered_dict = dt_fact.collect()

    fields_required = ['date_time']
    for field in fields_required:
        assert field in gathered_dict

    fields_required = ['year', 'month', 'weekday', 'weekday_number',
                       'weeknumber', 'day', 'hour', 'minute', 'second',
                       'epoch', 'epoch_int', 'date', 'time', 'iso8601_micro',
                       'iso8601_basic', 'iso8601_basic_short', 'tz', 'tz_dst',
                       'tz_offset', 'iso8601']
    for field in fields_required:
        assert field in gathered_dict['date_time']

# Generated at 2022-06-13 02:41:33.792087
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    collected_facts = {}
    collected_facts['date_time'] = dt.collect()
    facts_dict = {}
    facts_dict['date_time'] = {}
    expected_facts = dt.collect()
    assert expected_facts['date_time'] == collected_facts['date_time']

# Generated at 2022-06-13 02:41:39.919985
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible_collections.community.general.tests.unit.compat import unittest


# Generated at 2022-06-13 02:41:49.353638
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_facts = date_time_fact_collector.collect()
    assert date_time_facts is not None
    for fact in ['year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day', 'hour', 'minute', 'second',
            'epoch', 'epoch_int', 'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
            'tz', 'tz_dst', 'tz_offset']:
        assert fact in date_time_facts['date_time']
        assert len(date_time_facts['date_time'][fact].strip()) > 0

# Generated at 2022-06-13 02:41:57.417297
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    facts = dt.collect()
    assert isinstance(facts.get('date_time'), dict)
    assert facts['date_time']['year'] == strftime('%Y')
    assert facts['date_time']['month'] == strftime('%m')
    assert facts['date_time']['weekday'] == strftime('%A')
    assert facts['date_time']['weekday_number'] == strftime('%w')
    assert facts['date_time']['weeknumber'] == strftime('%W')
    assert facts['date_time']['day'] == strftime('%d')
    assert facts['date_time']['hour'] == strftime('%H')

# Generated at 2022-06-13 02:42:04.006572
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_collected_facts = {}

    # test before collect
    test_dtfc = DateTimeFactCollector()
    assert 'date_time' not in test_collected_facts
    assert 'date_time' not in test_dtfc._fact_ids

    # test collect
    test_dtfc.collect(collected_facts=test_collected_facts)
    assert 'date_time' in test_collected_facts
    assert test_dtfc.name in test_collected_facts
    assert test_dtfc.name in test_dtfc._fact_ids

    # test results
    year = datetime.datetime.now().strftime('%Y')
    month = datetime.datetime.now().strftime('%m')
    weekday = datetime.datetime.now().strftime('%A')
    weekday

# Generated at 2022-06-13 02:42:14.877347
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Some locals to simulate module args and module global facts
    module = None
    new_module_args = {}
    collected_facts = {}
    facts_dict = {}
    # Some needed datetime facts
    epoch = time.time()
    now = datetime.datetime.fromtimestamp(epoch)
    utcnow = datetime.datetime.utcfromtimestamp(epoch)

    # Call the collect method
    date_time_facts = DateTimeFactCollector.collect(module, collected_facts)

    # Assert method returned expected date_time facts
    date_time_facts_expected = {}
    date_time_facts_expected['year'] = now.strftime('%Y')
    date_time_facts_expected['month'] = now.strftime('%m')

# Generated at 2022-06-13 02:42:17.554408
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc.collect()

# Generated at 2022-06-13 02:42:29.154283
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    DTFactCollector = DateTimeFactCollector()
    DTFactCollector._module = MagicMock()
    DTFactCollector._module.exit_json = MagicMock()
    DTFactCollector._module.params = {}
    DTFactCollector.collect()

# Generated at 2022-06-13 02:42:33.190041
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfact = DateTimeFactCollector()
    res = dtfact.collect()
    # simple test
    assert res['date_time']['day'] == datetime.datetime.now().strftime('%d')

# Generated at 2022-06-13 02:42:39.424103
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """Unit test for method collect.
    This method will return datetime facts collected from system.
    """
    fc = DateTimeFactCollector()
    fc.set_module_name("test_module_name")
    fc.set_fact_name("test_fact_name")
    fc.set_config_key("test_config_key")
    fact_gather_list = fc.collect()
    assert fact_gather_list.get("date_time") is not None

# Generated at 2022-06-13 02:42:42.806433
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    facts = fact_collector.collect()
    assert isinstance(facts['date_time'], dict)
    assert facts['date_time']['year']


# Generated at 2022-06-13 02:42:53.979589
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector({}, None)
    fact_collector._collect()
    res = fact_collector._read_facts()

# Generated at 2022-06-13 02:43:05.873166
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase
    from ansible_collections.ansible.community.plugins.module_utils import basic
    from ansible_collections.ansible.community.plugins.module_utils.facts import ansible_collector

    assert hasattr(ansible_collector, 'DateTimeFactCollector')

    # Create a test object
    dtfc = ansible_collector.DateTimeFactCollector()
    assert dtfc.name == 'date_time'

    # Create a test ansible module
    test_ansible_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False)

    # Set collected_facts to an empty dict
    collected_facts = dict

# Generated at 2022-06-13 02:43:09.490317
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collections import date_time

    with pytest.raises(TypeError) as excinfo:
        date_time.DateTimeFactCollector().collect()
    assert 'date_time.DateTimeFactCollector.collect() takes exactly 2 arguments' in str(excinfo.value)


# Generated at 2022-06-13 02:43:14.756848
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    ansible_module_instance = DateTimeFactCollector()
    result = ansible_module_instance.collect()

# Generated at 2022-06-13 02:43:20.242672
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    # Initialize a DateTimeFactCollector object
    date_time_collector = DateTimeFactCollector()

    # Retrieve date time information
    date_time_facts = date_time_collector.collect()

    # Sanity check, verify we retrieved the date time facts
    assert date_time_facts['date_time'] != {}

# Generated at 2022-06-13 02:43:24.338100
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector

    collector = DateTimeFactCollector()
    collected_facts = Collector().collect(collector)
    date_time_facts = collected_facts['date_time']

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

# Generated at 2022-06-13 02:43:30.053620
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    obj = DateTimeFactCollector()
    col_set = {"date_time"}
    mod_set = {"date_time"}
    result = obj.collect(collected_facts=col_set, module=mod_set)
    assert ("date_time" in result)
    assert ("year" in result['date_time'])
    assert ("month" in result['date_time'])
    assert ("weekday" in result['date_time'])
    assert ("day" in result['date_time'])
    assert ("hour" in result['date_time'])
    assert ("minute" in result['date_time'])
    assert ("second" in result['date_time'])
    assert ("epoch" in result['date_time'])
    assert ("epoch_int" in result['date_time'])

# Generated at 2022-06-13 02:43:33.046408
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts_collector = DateTimeFactCollector()
    assert isinstance(date_time_facts_collector.collect(), dict)

# Generated at 2022-06-13 02:43:41.742734
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    datetime_fact_collector = DateTimeFactCollector()

    ansible_facts = {}

# Generated at 2022-06-13 02:43:53.128932
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import datetime
    import time

    # Store the timestamp once, then get local and UTC versions from that
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)


    # Test for epoch fact
    epoch_fact = str(int(now.strftime('%s')))
    if epoch_fact == '' or epoch_fact[0] == '%':
        epoch_fact = str(int(epoch_ts))

    # Test for epoch_int fact
    epoch_int = str(int(now.strftime('%s')))
    if epoch_int == '' or epoch_int[0] == '%':
        epoch_int = str(int(epoch_ts))

# Generated at 2022-06-13 02:43:54.764283
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # create instance
    m = DateTimeFactCollector()
    # execute method collect
    m.collect()

# Generated at 2022-06-13 02:44:07.952251
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    dt_facts = dt.collect()

# Generated at 2022-06-13 02:44:20.348584
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Instantiate DateTimeFactCollector
    dtfc = DateTimeFactCollector()

    # Call collect fact method
    fact = dtfc.collect()

    assert fact['date_time']['epoch'].isdigit() == True
    assert fact['date_time']['epoch_int'].isdigit() == True
    assert fact['date_time']['iso8601_micro'] == datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert fact['date_time']['iso8601'] == datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

# Generated at 2022-06-13 02:44:30.517303
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # test for method collect of class DateTimeFactCollector
    # create an object of DateTimeFactCollector
    c = DateTimeFactCollector()

    # call collect
    date_time = c.collect()
    # test if date_time is not empty
    assert date_time
    # check if the keys are present
    assert 'date_time' in date_time
    # check if the keys in date_time are present
    assert 'year' in date_time['date_time']
    assert 'month' in date_time['date_time']
    assert 'weekday' in date_time['date_time']
    assert 'weekday_number' in date_time['date_time']
    assert 'weeknumber' in date_time['date_time']
    assert 'day' in date_time['date_time']

# Generated at 2022-06-13 02:44:31.690906
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    dtfc.collect()

# Generated at 2022-06-13 02:44:41.676126
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils._text import to_text

    dtf = DateTimeFactCollector(None)
    result = dtf.collect()

    assert result.get('date_time') is not None

    date_time = result.get('date_time')

    assert to_text(date_time['year']).isdigit()
    assert len(to_text(date_time['year'])) == 4

    assert to_text(date_time['month']).isdigit()
    assert len(to_text(date_time['month'])) == 2

    assert to_text(date_time['weekday_number']).isdigit()
    assert len(to_text(date_time['weekday_number'])) == 1

    assert to_text(date_time['weeknumber']).isdigit()
   

# Generated at 2022-06-13 02:44:45.856437
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    collected_facts = {}
    fact_list = dtf.collect(collected_facts)
    assert 'date_time' in fact_list
    return fact_list

if __name__ == '__main__':
    print(test_DateTimeFactCollector_collect())

# Generated at 2022-06-13 02:44:49.614506
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    """ Unit test for method collect of class DateTimeFactCollector
    """
    dtfc = DateTimeFactCollector()
    dtfc.collect()
    # the following assert can cause the test to fail in epoch rollover seconds.
    #assert dtfc.get_facts()['date_time']['epoch_int'] == \
    #    dtfc.get_facts()['date_time']['epoch']

# Generated at 2022-06-13 02:44:54.493041
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    date_time_dict = date_time_fact_collector.collect()
    assert date_time_dict['date_time']['hour'] == datetime.datetime.now().strftime('%H')

# Generated at 2022-06-13 02:45:00.517047
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Test data collector
    DateTimeFactCollector = DateTimeFactCollector()
    # collect method
    DateTimeFactCollector._get_mount_size_list = mock_get_mount_size_list
    DateTimeFactCollector._get_partition_size_list = mock_get_partition_size_list
    result = DateTimeFactCollector.collect()
    # Test result, currently we will only test if date_time fact exist
    assert 'date_time' in result

# Unit test mock data

# Generated at 2022-06-13 02:45:10.698413
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # for more information about the following import, have a look at:
    # http://www.voidspace.org.uk/python/mock/examples.html#working-with-magic-methods
    from ansible.module_utils.facts import collector

    # Mock "ansible.module_utils.facts.collector.BaseFactCollector.get_file_content"
    # to return a dictionary
    real_get_file_content = collector.BaseFactCollector.get_file_content

    def mocked_get_file_content(self, file):
        if file == '':
            return '{"key": "value"}'
        else:
            return real_get_file_content(self, file)

    collector.BaseFactCollector.get_file_content = mocked_get_file_content

    # Mock "ansible.

# Generated at 2022-06-13 02:45:30.573230
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Make an instance of class DateTimeFactCollector
    f = DateTimeFactCollector()

    # Collect the data
    collected_facts = f.collect()

    # Check the keys
    assert 'date_time' in collected_facts
    assert collected_facts['date_time']['year'].isdigit()
    assert collected_facts['date_time']['month'].isdigit()
    assert collected_facts['date_time']['weekday'].isalpha()
    assert collected_facts['date_time']['weekday_number'].isdigit()
    assert collected_facts['date_time']['weeknumber'].isdigit()
    assert collected_facts['date_time']['day'].isdigit()
    assert collected_facts['date_time']['hour'].isdigit

# Generated at 2022-06-13 02:45:34.872419
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_dt = DateTimeFactCollector()
    result = test_dt.collect()
    assert result.get('date_time', {}).get('year') != ''

# Generated at 2022-06-13 02:45:44.768179
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    result = dt.collect()
    assert type(result['date_time']) is dict
    assert 'month' in result['date_time']
    assert type(result['date_time']['month']) is str
    assert result['date_time']['month'] != ''
    assert 'year' in result['date_time']
    assert type(result['date_time']['year']) is str
    assert result['date_time']['year'] != ''
    assert 'weekday' in result['date_time']
    assert type(result['date_time']['weekday']) is str
    assert result['date_time']['weekday'] != ''
    assert 'weekday_number' in result['date_time']

# Generated at 2022-06-13 02:45:47.019830
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    try:
        dt = DateTimeFactCollector()
        dt.collect()
    except Exception:
        assert False, 'failed to collect date/time facts'
    assert True

# Generated at 2022-06-13 02:45:58.429845
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import sys
    import os.path
    import re
    import platform
    import subprocess

    # Mock the module object for this test
    import ansible.module_utils.facts.collector
    class fake_module:
        def __init__(self):
            self.params = {'gather_subset': 'all'}
            self.config = {'gather_timeout': 10}
        def fail_json(self, msg):
            self.fail_json_msg = msg
    module = fake_module()

    # Mock the AnsibleModule object for this test
    import ansible.module_utils.facts
    ansible.module_utils.facts.AnsibleModule = lambda *args, **kwargs: module
    ansible.module_utils.facts.collector = sys.modules[__name__]

    # Test

# Generated at 2022-06-13 02:46:05.458753
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts = collector.collect()
    assert isinstance(facts, dict)
    assert 'date_time' in facts
    assert 'epoch_int' in facts['date_time']
    assert 'epoch' in facts['date_time']
    assert 'iso8601' in facts['date_time']
    assert 'tz' in facts['date_time']

# Generated at 2022-06-13 02:46:13.690503
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    time.strftime = lambda x: "example"
    epoch_ts = time.time()
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)


# Generated at 2022-06-13 02:46:16.372116
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fc = DateTimeFactCollector()
    ans = fc.collect()
    assert 'date_time' in ans
    assert isinstance(ans['date_time'], dict)

# Generated at 2022-06-13 02:46:27.222120
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtfc = DateTimeFactCollector()
    res = dtfc.collect(collected_facts={})
    assert res['date_time']['day'] == time.strftime('%d')
    assert res['date_time']['epoch'] == str(int(time.time()))
    assert res['date_time']['epoch_int'] == str(int(time.time()))
    assert res['date_time']['hour'] == time.strftime('%H')
    assert res['date_time']['iso8601'] == datetime.datetime.utcfromtimestamp(time.time()).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert res['date_time']['iso8601_basic'] == datetime.datetime

# Generated at 2022-06-13 02:46:37.228570
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector.date_time import DateTimeFactCollector as DTC
    from ansible.module_utils.facts.collector.base import BaseFactCollector as BFC

    # Create a Collector instance
    c = Collector(None)

    # Create a DateTimeFactCollector instance
    dtc_instance = DTC(c)

    # Assert that our instance is an instance of a DateTimeFactCollector
    assert isinstance(dtc_instance, DTC)

    # Assert that our instance is an instance of a BaseFactCollector
    assert isinstance(dtc_instance, BFC)

    # Create a set containing the expected

# Generated at 2022-06-13 02:47:16.595493
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_fact_collector = DateTimeFactCollector()
    # Ensure that `date_time` key in the returned dict
    assert 'datetime' in date_time_fact_collector.collect()['datetime']
    # Ensure that `date_time` key in the returned dict
    # has `epoch` and `date` keys
    assert 'epoch' in date_time_fact_collector.collect()['datetime']
    assert 'date' in date_time_fact_collector.collect()['datetime']

# Generated at 2022-06-13 02:47:21.767202
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.facts import Facts
    test_collected_facts = Facts()
    date_time_fact_collector = DateTimeFactCollector()
    collected_facts = date_time_fact_collector.collect(collected_facts=test_collected_facts)
    assert 'date_time' in collected_facts
    assert 'date' in collected_facts['date_time']

# Generated at 2022-06-13 02:47:23.177419
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    result = dt.collect()
    assert 'date_time' in result

# Generated at 2022-06-13 02:47:25.442440
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    name = 'date_time'
    d = DateTimeFactCollector()
    result = d.collect()
    assert(name in result)
    assert type(result[name]) == dict

# Generated at 2022-06-13 02:47:36.865188
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Given
    datetime_fact = DateTimeFactCollector()
    module = None

# Generated at 2022-06-13 02:47:41.947876
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():

    dt = DateTimeFactCollector()

    # Get the date_time facts
    date_time_facts = dt.collect()

    # Check that the date_time facts are not empty
    assert date_time_facts != {}

    # Check that there is a "date_time" entry
    assert 'date_time' in date_time_facts

# Generated at 2022-06-13 02:47:46.169994
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact = DateTimeFactCollector()
    facts = fact.collect()
    assert isinstance(facts, dict)
    assert 'date_time' in facts
    assert isinstance(facts['date_time'], dict)
    assert facts['date_time']['date'] == datetime.datetime.now().strftime('%Y-%m-%d')

# Generated at 2022-06-13 02:47:47.489192
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_dict = DateTimeFactCollector().collect()
    assert isinstance(test_dict, dict)

# Generated at 2022-06-13 02:47:50.948005
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector()
    facts_dict = date_time_facts.collect()
    assert 'date_time' in facts_dict
    assert isinstance(facts_dict['date_time'], dict)

# Generated at 2022-06-13 02:48:01.169851
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dt = DateTimeFactCollector()
    now = datetime.datetime.now()
    utcnow = datetime.datetime.utcfromtimestamp(time.time())

    dt_facts = dt.collect()
    assert dt_facts['date_time']['year'] == now.strftime('%Y')
    assert dt_facts['date_time']['month'] == now.strftime('%m')
    assert dt_facts['date_time']['weekday'] == now.strftime('%A')
    assert dt_facts['date_time']['weekday_number'] == now.strftime('%w')
    assert dt_facts['date_time']['weeknumber'] == now.strftime('%W')

# Generated at 2022-06-13 02:49:14.020051
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from . import MockModule, MockCollectedFacts

    date_time_fact_collector = DateTimeFactCollector()

    module = MockModule()
    collected_facts = MockCollectedFacts({'date_time': {}})
    result = date_time_fact_collector.collect(module, collected_facts)
    assert result['date_time']['day']
    assert result['date_time']['epoch']
    assert result['date_time']['epoch_int']
    assert result['date_time']['hour']
    assert result['date_time']['iso8601_basic']
    assert result['date_time']['iso8601_basic_short']
    assert result['date_time']['iso8601']

# Generated at 2022-06-13 02:49:16.282719
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    result = collector.collect()
    assert result['date_time']['year'] > 2000


# Generated at 2022-06-13 02:49:21.784501
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fact_collector = DateTimeFactCollector()
    date_time_facts = fact_collector.collect()
    assert type(date_time_facts) == dict
    assert type(date_time_facts['date_time']) == dict
    assert date_time_facts['date_time']['hour'] == datetime.datetime.now().strftime('%H')

# Generated at 2022-06-13 02:49:25.128761
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # check if epoch is float or string
    date_time_facts = DateTimeFactCollector().collect()
    assert type(date_time_facts['date_time']['epoch']) == str

# Generated at 2022-06-13 02:49:36.467333
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_obj = DateTimeFactCollector()
    dt_facts = date_time_obj.collect()
    assert 'date_time' in dt_facts
    assert 'date' in dt_facts['date_time']
    assert 'day' in dt_facts['date_time']
    assert 'hour' in dt_facts['date_time']
    assert 'minute' in dt_facts['date_time']
    assert 'month' in dt_facts['date_time']
    assert 'second' in dt_facts['date_time']
    assert 'time' in dt_facts['date_time']
    assert 'weekday' in dt_facts['date_time']
    assert 'weekday_number' in dt_facts['date_time']
    assert 'weeknumber' in dt

# Generated at 2022-06-13 02:49:47.954701
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # check class exists
    assert 'ansible.module_utils.facts.system.date_time.DateTimeFactCollector' in globals()

    # Testing dictionary values against expected output
    fc = DateTimeFactCollector()
    facts = fc.collect()
    assert isinstance(facts, dict)
    # Testing for top level key
    assert 'date_time' in facts.keys()
    assert isinstance(facts['date_time'], dict)
    # Testing for keys in date_time_facts subdictionary
    date_time_facts = facts['date_time']
    assert 'weekday' in date_time_facts.keys()
    assert 'month' in date_time_facts.keys()
    assert 'weekday_number' in date_time_facts.keys()
    assert 'weeknumber' in date_time_

# Generated at 2022-06-13 02:49:58.038130
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    date_time_facts = DateTimeFactCollector().collect()
    assert date_time_facts['date_time']
    assert isinstance(date_time_facts['date_time'], dict)
    keys_date_time = ['year', 'month', 'weekday', 'weekday_number', 'weeknumber',
                      'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
                      'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
                      'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset']
    for key in keys_date_time:
        assert date_time_facts['date_time'][key]

# Generated at 2022-06-13 02:50:05.192683
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    test_DateTimeFactCollector = DateTimeFactCollector()
    test_DateTimeFactCollector_collect = test_DateTimeFactCollector.collect()
    assert test_DateTimeFactCollector_collect is not None
    assert isinstance(test_DateTimeFactCollector_collect, dict)
    assert 'date_time' in test_DateTimeFactCollector_collect
    assert test_DateTimeFactCollector_collect['date_time'] is not None
    assert isinstance(test_DateTimeFactCollector_collect['date_time'], dict)
    assert 'epoch_int' in test_DateTimeFactCollector_collect['date_time']
    assert isinstance(test_DateTimeFactCollector_collect['date_time']['epoch_int'], str)

# Generated at 2022-06-13 02:50:07.861923
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    dtf = DateTimeFactCollector()
    dtf.collect()
    assert 'date_time' in dtf._collected_facts

# Generated at 2022-06-13 02:50:17.641575
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    fake_datetime = datetime.datetime(2016, 1, 1, 12, 0, 0)

    dtf = DateTimeFactCollector()

    with mock.patch.object(dtf, '_get_epoch_time', return_value = 1454161600):
        with mock.patch.object(dtf, '_get_datetime', return_value = fake_datetime):
            facts_dict = dtf.collect()

    assert(facts_dict['date_time']['year'] == "2016")
    assert(facts_dict['date_time']['month'] == "01")
    assert(facts_dict['date_time']['weekday'] == "Friday")
    assert(facts_dict['date_time']['weekday_number'] == "5")