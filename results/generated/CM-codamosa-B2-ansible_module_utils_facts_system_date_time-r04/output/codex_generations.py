

# Generated at 2026-11-03 02:07:35.853044
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    epoch_ts = 1483228800.0  # 2017-01-01 00:00:00 UTC

    with patch.object(time, 'time', return_value=epoch_ts):
        facts_dict = DateTimeFactCollector().collect()

    assert 'date_time' in facts_dict
    date_time_facts = facts_dict['date_time']

    expected_keys = set([
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset',
    ])
    assert set(date_time_facts.keys()) == expected_keys

    now = datetime.datetime.fromtimestamp(epoch_ts)
    utcnow = datetime.datetime.utcfromtimestamp(epoch_ts)

    assert date_time_facts['year'] == now.strftime('%Y')
    assert date_time_facts['month'] == now.strftime('%m')
    assert date_time_facts['weekday'] == now.strftime('%A')
    assert date_time_facts['weekday_number'] == now.strftime('%w')
    assert date_time_facts['weeknumber'] == now.strftime('%W')
    assert date_time_facts['day'] == now.strftime('%d')
    assert date_time_facts['hour'] == now.strftime('%H')
    assert date_time_facts['minute'] == now.strftime('%M')
    assert date_time_facts['second'] == now.strftime('%S')
    assert date_time_facts['date'] == now.strftime('%Y-%m-%d')
    assert date_time_facts['time'] == now.strftime('%H:%M:%S')

    assert date_time_facts['iso8601_micro'] == utcnow.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    assert date_time_facts['iso8601'] == utcnow.strftime('%Y-%m-%dT%H:%M:%SZ')
    assert date_time_facts['iso8601_basic'] == now.strftime('%Y%m%dT%H%M%S%f')
    assert date_time_facts['iso8601_basic_short'] == now.strftime('%Y%m%dT%H%M%S')

    # epoch may fall back to int(epoch_ts) on platforms without %s support
    epoch_str = now.strftime('%s')
    if epoch_str == '' or epoch_str[0] == '%':
        epoch_str = str(int(epoch_ts))
    assert date_time_facts['epoch'] == epoch_str

    try:
        epoch_int_str = str(int(now.strftime('%s')))
    except ValueError:
        epoch_int_str = str(int(epoch_ts))
    assert date_time_facts['epoch_int'] == epoch_int_str

    assert date_time_facts['tz'] == time.strftime('%Z')
    assert date_time_facts['tz_dst'] == time.tzname[1]
    assert date_time_facts['tz_offset'] == time.strftime('%z')

    # all values should be strings
    for value in date_time_facts.values():
        assert isinstance(value, str)

# Generated at 2026-11-03 02:08:13.087649
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()

    # Verify the instance is created and is of correct type
    assert collector is not None
    assert isinstance(collector, DateTimeFactCollector)
    assert isinstance(collector, BaseFactCollector)

    # Verify class attributes
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()

    # Verify collect() returns a dict containing 'date_time' key
    facts = collector.collect()
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    date_time_facts = facts['date_time']
    expected_keys = [
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    ]
    for key in expected_keys:
        assert key in date_time_facts

# Generated at 2026-11-03 02:09:11.663736
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()
    assert isinstance(collector, DateTimeFactCollector)
    assert isinstance(collector, BaseFactCollector)
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()

# Generated at 2026-11-03 02:09:50.470691
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()
    facts = collector.collect()
    assert 'date_time' in facts
    date_time_facts = facts['date_time']
    for key in ('year', 'month', 'weekday', 'weekday_number', 'weeknumber',
                'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
                'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
                'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'):
        assert key in date_time_facts

# Generated at 2026-11-03 02:13:13.444017
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from unittest import mock

    fixed_epoch = 1552031825.718699  # 2019-03-08 07:57:05.718699 UTC

    with mock.patch('time.time', return_value=fixed_epoch):
        collector = DateTimeFactCollector()
        facts = collector.collect()

    assert 'date_time' in facts
    date_time_facts = facts['date_time']

    # Recompute expected values from the same fixed timestamp
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

    # epoch must be the integer-second timestamp as a string, regardless of
    # whether strftime('%s') is supported on this platform
    assert date_time_facts['epoch'] == str(int(fixed_epoch))
    assert date_time_facts['epoch_int'] == str(int(fixed_epoch))

    assert date_time_facts['date'] == now.strftime('%Y-%m-%d')
    assert date_time_facts['time'] == now.strftime('%H:%M:%S')
    assert date_time_facts['iso8601_micro'] == utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert date_time_facts['iso8601'] == utcnow.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert date_time_facts['iso8601_basic'] == now.strftime("%Y%m%dT%H%M%S%f")
    assert date_time_facts['iso8601_basic_short'] == now.strftime("%Y%m%dT%H%M%S")

    assert date_time_facts['tz'] == time.strftime("%Z")
    assert date_time_facts['tz_dst'] == time.tzname[1]
    assert date_time_facts['tz_offset'] == time.strftime("%z")

    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset',
    }
    assert set(date_time_facts.keys()) == expected_keys

# Generated at 2026-11-03 02:14:39.455680
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts = collector.collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    assert set(dt.keys()) == expected_keys

    # Numeric date/time components
    assert re.match(r'^\d{4}$', dt['year'])
    assert re.match(r'^\d{2}$', dt['month'])
    assert re.match(r'^\d{2}$', dt['day'])
    assert re.match(r'^\d{2}$', dt['hour'])
    assert re.match(r'^\d{2}$', dt['minute'])
    assert re.match(r'^\d{2}$', dt['second'])
    assert re.match(r'^\d{2}$', dt['weeknumber'])

    # weekday is a full day name, weekday_number is 0-6
    assert dt['weekday'] in ['Monday', 'Tuesday', 'Wednesday',
                             'Thursday', 'Friday', 'Saturday', 'Sunday']
    assert dt['weekday_number'] in [str(i) for i in range(7)]

    # epoch values are integer strings
    assert re.match(r'^\d+$', dt['epoch'])
    assert re.match(r'^\d+$', dt['epoch_int'])

    # date/time strings
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', dt['date'])
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', dt['time'])

    # iso8601 variants
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$', dt['iso8601_micro'])
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', dt['iso8601'])
    assert re.match(r'^\d{8}T\d{12}$', dt['iso8601_basic'])
    assert re.match(r'^\d{8}T\d{6}$', dt['iso8601_basic_short'])

    # timezone offset like +0000 or -0500
    assert re.match(r'^[+-]\d{4}$', dt['tz_offset'])

    # consistency between date components
    assert dt['date'] == '%s-%s-%s' % (dt['year'], dt['month'], dt['day'])
    assert dt['time'] == '%s:%s:%s' % (dt['hour'], dt['minute'], dt['second'])

    # iso8601 date part should match 'date'
    assert dt['iso8601'].startswith(dt['date'])
    assert dt['iso8601_micro'].startswith(dt['date'])

    # module_0.collect() should tolerate module and collected_facts arguments
    facts2 = DateTimeFactCollector().collect(module=None, collected_facts={})
    assert 'date_time' in facts2