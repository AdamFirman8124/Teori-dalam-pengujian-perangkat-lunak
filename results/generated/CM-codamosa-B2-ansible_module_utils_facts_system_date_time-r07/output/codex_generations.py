

# Generated at 2026-11-02 09:16:08.987681
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()
    assert hasattr(collector, 'collect')

# Generated at 2026-11-02 09:17:35.518925
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()

    fake_epoch = 1500000000.5
    fake_now = datetime.datetime(2017, 7, 14, 2, 40, 0, 500000)
    fake_utcnow = datetime.datetime(2017, 7, 14, 2, 40, 0, 500000)


# Generated at 2026-11-02 09:18:01.934843
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()

    # Constructor should create an instance without arguments
    assert collector is not None
    assert isinstance(collector, DateTimeFactCollector)

    # Class attributes should be set correctly
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()

    # Should have a callable collect method
    assert callable(collector.collect)

# Generated at 2026-11-02 09:18:30.403173
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from unittest.mock import patch

    collector = DateTimeFactCollector()
    epoch_ts = 1521542000.3566489

    with patch.object(time, 'time', return_value=epoch_ts):
        facts_dict = collector.collect(module=None, collected_facts=None)

    assert 'date_time' in facts_dict
    dt = facts_dict['date_time']

    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset'
    }
    assert set(dt.keys()) == expected_keys

    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    assert dt['year'] == now.strftime('%Y')
    assert dt['month'] == now.strftime('%m')
    assert dt['weekday'] == now.strftime('%A')
    assert dt['weekday_number'] == now.strftime('%w')
    assert dt['weeknumber'] == now.strftime('%W')
    assert dt['day'] == now.strftime('%d')
    assert dt['hour'] == now.strftime('%H')
    assert dt['minute'] == now.strftime('%M')
    assert dt['second'] == now.strftime('%S')
    assert dt['date'] == now.strftime('%Y-%m-%d')
    assert dt['time'] == now.strftime('%H:%M:%S')
    assert dt['iso8601_micro'] == utcnow.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    assert dt['iso8601'] == utcnow.strftime('%Y-%m-%dT%H:%M:%SZ')
    assert dt['iso8601_basic'] == now.strftime('%Y%m%dT%H%M%S%f')
    assert dt['iso8601_basic_short'] == now.strftime('%Y%m%dT%H%M%S')
    assert dt['tz'] == time.strftime('%Z')
    assert dt['tz_dst'] == time.tzname[1]
    assert dt['tz_offset'] == time.strftime('%z')

    # epoch falls back to the int of time.time() when %s is unsupported/empty
    assert dt['epoch'] == str(int(epoch_ts))
    assert dt['epoch_int'] == str(int(epoch_ts))

# Generated at 2026-11-02 09:18:52.216537
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()

    assert isinstance(collector, DateTimeFactCollector)
    assert isinstance(collector, BaseFactCollector)
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()

# Generated at 2026-11-02 09:19:36.562865
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts = collector.collect()

    assert 'date_time' in facts
    date_time_facts = facts['date_time']

    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset'
    }
    assert expected_keys.issubset(set(date_time_facts.keys()))

    # Verify format of each fact
    assert re.match(r'^\d{4}$', date_time_facts['year'])
    assert re.match(r'^\d{2}$', date_time_facts['month'])
    assert date_time_facts['weekday'] in ('Monday', 'Tuesday', 'Wednesday',
                                          'Thursday', 'Friday', 'Saturday', 'Sunday')
    assert date_time_facts['weekday_number'] in ('0', '1', '2', '3', '4', '5', '6')
    assert re.match(r'^\d{2}$', date_time_facts['weeknumber'])
    assert re.match(r'^\d{2}$', date_time_facts['day'])
    assert re.match(r'^\d{2}$', date_time_facts['hour'])
    assert re.match(r'^\d{2}$', date_time_facts['minute'])
    assert re.match(r'^\d{2}$', date_time_facts['second'])

    # epoch facts must be integer strings, never empty or an unresolved format
    assert re.match(r'^\d+$', date_time_facts['epoch'])
    assert re.match(r'^\d+$', date_time_facts['epoch_int'])
    assert date_time_facts['epoch'] != ''
    assert not date_time_facts['epoch'].startswith('%')
    assert not date_time_facts['epoch_int'].startswith('%')

    assert re.match(r'^\d{4}-\d{2}-\d{2}$', date_time_facts['date'])
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', date_time_facts['time'])
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$', date_time_facts['iso8601_micro'])
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', date_time_facts['iso8601'])
    assert re.match(r'^\d{8}T\d{6}\d{6}$', date_time_facts['iso8601_basic'])
    assert re.match(r'^\d{8}T\d{6}$', date_time_facts['iso8601_basic_short'])

    # tz facts should reflect the current local time module values
    assert date_time_facts['tz'] == time.strftime("%Z")
    assert date_time_facts['tz_dst'] == time.tzname[1]
    assert date_time_facts['tz_offset'] == time.strftime("%z")


def test_DateTimeFactCollector_collect_fixed_epoch():
    fixed_epoch = 1234567890.123456

    with patch.object(time, 'time', return_value=fixed_epoch):
        collector = DateTimeFactCollector()
        facts = collector.collect()

    date_time_facts = facts['date_time']

    now = datetime.datetime.fromtimestamp(fixed_epoch)
    utcnow = datetime.datetime.utcfromtimestamp(fixed_epoch)

    assert date_time_facts['year'] == now.strftime('%Y')
    assert date_time_facts['month'] == now.strftime('%m')
    assert date_time_facts['weekday'] == now.strftime('%A')
    assert date_time_facts['weekday_number'] == now.strftime('%w')
    assert date_time_facts['weeknumber'] == now.strftime('%W')
    assert date_time_facts['day'] == now.strftime('%d')
    assert date_time_facts['hour'] == now.strftime('%H')
    assert date_time_facts['minute'] == now.strftime('%M')
    assert date_time_facts['second'] == now.strftime('%S')

    # epoch should be the integer portion of the fixed timestamp
    assert date_time_facts['epoch'] == str(int(fixed_epoch))
    assert date_time_facts['epoch_int'] == str(int(fixed_epoch))

    assert date_time_facts['date'] == now.strftime('%Y-%m-%d')
    assert date_time_facts['time'] == now.strftime('%H:%M:%S')
    assert date_time_facts['iso8601_micro'] == utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert date_time_facts['iso8601'] == utcnow.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert date_time_facts['iso8601_basic'] == now.strftime("%Y%m%dT%H%M%S%f")
    assert date_time_facts['iso8601_basic_short'] == now.strftime("%Y%m%dT%H%M%S")


def test_DateTimeFactCollector_collect_ignores_collected_facts():
    collector = DateTimeFactCollector()
    facts = collector.collect(module=None, collected_facts={'date_time': {'stale': 'value'}})

    date_time_facts = facts['date_time']
    assert 'stale' not in date_time_facts
    assert 'year' in date_time_facts
    assert 'epoch' in date_time_facts


def test_DateTimeFactCollector_collect_module_none():
    collector = DateTimeFactCollector()
    facts = collector.collect(module=None)

    assert isinstance(facts, dict)
    assert list(facts.keys()) == ['date_time']

# Generated at 2026-11-02 09:21:56.430226
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()

    # Fixed timestamp for deterministic results
    # 1500000000.123456 == 2017-07-14 02:40:00.123456 UTC
    epoch_ts = 1500000000.123456
    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    with mock.patch('time.time', return_value=epoch_ts):
        facts_dict = collector.collect(module=None, collected_facts=None)

    # The collector returns facts wrapped under its 'date_time' namespace
    assert list(facts_dict.keys()) == ['date_time']
    date_time_facts = facts_dict['date_time']

    # All expected fact keys are present

# Generated at 2026-11-02 09:24:21.872242
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Fix the timestamp so UTC-derived values are deterministic:
    # 1557350605 == 2019-05-08 21:23:25 UTC
    fixed_epoch = 1557350605.0

    with mock.patch('time.time', return_value=fixed_epoch):
        collector = DateTimeFactCollector()
        facts_dict = collector.collect()

    assert isinstance(facts_dict, dict)
    assert 'date_time' in facts_dict

    date_time_facts = facts_dict['date_time']

    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset',
    }
    assert set(date_time_facts.keys()) == expected_keys

    # Deterministic, UTC-based values for the fixed timestamp
    assert date_time_facts['iso8601'] == '2019-05-08T21:23:25Z'
    assert date_time_facts['iso8601_micro'] == '2019-05-08T21:23:25.000000Z'

    # epoch must be the integer timestamp whether or not strftime('%s') is supported