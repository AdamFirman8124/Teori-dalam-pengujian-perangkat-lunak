

# Generated at 2026-11-01 22:55:02.406071
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()

    # Works with no args and with explicit args
    facts = collector.collect()
    facts_with_args = collector.collect(module=None, collected_facts={})

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    assert facts['date_time'] == facts_with_args['date_time']

    dt = facts['date_time']

    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset',
    }
    assert set(dt.keys()) == expected_keys

    # Numeric field formats
    assert re.match(r'^\d{4}$', dt['year'])
    assert re.match(r'^\d{2}$', dt['month'])
    assert re.match(r'^\d{2}$', dt['day'])
    assert re.match(r'^\d{2}$', dt['hour'])
    assert re.match(r'^\d{2}$', dt['minute'])
    assert re.match(r'^\d{2}$', dt['second'])
    assert re.match(r'^\d$', dt['weekday_number'])
    assert re.match(r'^\d{2}$', dt['weeknumber'])

    # Weekday name and its number are consistent
    assert dt['weekday'] in ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                             'Friday', 'Saturday', 'Sunday')
    weekday_numbers = {'Sunday': '0', 'Monday': '1', 'Tuesday': '2',
                       'Wednesday': '3', 'Thursday': '4', 'Friday': '5',
                       'Saturday': '6'}
    assert dt['weekday_number'] == weekday_numbers[dt['weekday']]

    # date and time composed from individual components
    assert dt['date'] == '%s-%s-%s' % (dt['year'], dt['month'], dt['day'])
    assert dt['time'] == '%s:%s:%s' % (dt['hour'], dt['minute'], dt['second'])

    # ISO 8601 variants
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$',
                    dt['iso8601_micro'])
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', dt['iso8601'])
    assert re.match(r'^\d{8}T\d{12}$', dt['iso8601_basic'])
    assert re.match(r'^\d{8}T\d{6}$', dt['iso8601_basic_short'])
    assert dt['iso8601'] == dt['iso8601_micro'][:20]

    # Epoch values parse as ints and are close to "now" (within 10s slack)
    now_epoch = int(time.time())
    assert abs(now_epoch - int(float(dt['epoch']))) <= 10
    assert abs(now_epoch - int(dt['epoch_int'])) <= 10

    # Timezone facts are non-empty strings matching system values
    assert isinstance(dt['tz'], str) and len(dt['tz']) > 0
    assert isinstance(dt['tz_dst'], str) and len(dt['tz_dst']) > 0
    assert dt['tz'] == time.strftime('%Z')
    assert dt['tz_dst'] == time.tzname[1]
    assert re.match(r'^[+-]\d{4}$', dt['tz_offset'])

# Generated at 2026-11-01 22:55:53.601871
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    fixed_epoch = 1609459200.123456

    with mock.patch('time.time', return_value=fixed_epoch):
        facts = collector.collect(module=None, collected_facts=None)

    assert 'date_time' in facts
    dt = facts['date_time']

    now = datetime.datetime.fromtimestamp(fixed_epoch)
    utcnow = datetime.datetime.utcfromtimestamp(fixed_epoch)

    expected_keys = set([
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset'])
    assert set(dt.keys()) == expected_keys

    assert dt['year'] == now.strftime('%Y')
    assert dt['month'] == now.strftime('%m')
    assert dt['weekday'] == now.strftime('%A')
    assert dt['weekday_number'] == now.strftime('%w')
    assert dt['weeknumber'] == now.strftime('%W')
    assert dt['day'] == now.strftime('%d')
    assert dt['hour'] == now.strftime('%H')
    assert dt['minute'] == now.strftime('%M')
    assert dt['second'] == now.strftime('%S')
    # epoch falls back to str(int(epoch_ts)) when %s is unsupported
    assert dt['epoch'] == str(int(fixed_epoch))
    assert dt['epoch_int'] == str(int(fixed_epoch))
    assert dt['date'] == now.strftime('%Y-%m-%d')
    assert dt['time'] == now.strftime('%H:%M:%S')
    assert dt['iso8601_micro'] == utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert dt['iso8601'] == utcnow.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert dt['iso8601_basic'] == now.strftime("%Y%m%dT%H%M%S%f")
    assert dt['iso8601_basic_short'] == now.strftime("%Y%m%dT%H%M%S")
    assert dt['tz'] == time.strftime("%Z")
    assert dt['tz_dst'] == time.tzname[1]
    assert dt['tz_offset'] == time.strftime("%z")


def test_DateTimeFactCollector_collect_mocked_datetime():
    collector = DateTimeFactCollector()

    fake_now = datetime.datetime(2021, 1, 1, 12, 34, 56, 789012)
    fake_utcnow = datetime.datetime(2021, 1, 1, 10, 34, 56, 789012)

    with mock.patch('time.time', return_value=1609500000.0), \
            mock.patch('ansible.module_utils.facts.system.date_time.datetime') as mock_dt:
        mock_dt.datetime.fromtimestamp.return_value = fake_now
        mock_dt.datetime.utcfromtimestamp.return_value = fake_utcnow

        facts = collector.collect()

    dt = facts['date_time']
    assert dt['year'] == '2021'
    assert dt['month'] == '01'
    assert dt['day'] == '01'
    assert dt['weekday'] == 'Friday'
    assert dt['weekday_number'] == '5'
    assert dt['hour'] == '12'
    assert dt['minute'] == '34'
    assert dt['second'] == '56'
    assert dt['date'] == '2021-01-01'
    assert dt['time'] == '12:34:56'
    assert dt['iso8601_micro'] == '2021-01-01T10:34:56.789012Z'
    assert dt['iso8601'] == '2021-01-01T10:34:56Z'
    assert dt['iso8601_basic'] == '20210101T123456789012'
    assert dt['iso8601_basic_short'] == '20210101T123456'
    # epoch values are numeric strings regardless of %s platform support
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()

# Generated at 2026-11-01 22:56:28.519630
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()

    result = collector.collect()

    # Result should be a dict containing a 'date_time' key
    assert isinstance(result, dict)
    assert 'date_time' in result

    facts = result['date_time']
    assert isinstance(facts, dict)

    # All expected keys must be present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    assert set(facts.keys()) == expected_keys

    # All values must be strings
    for key, value in facts.items():
        assert isinstance(value, str), "fact %r is not a string: %r" % (key, value)

    # Verify format of individual facts against the current time (with tolerance)
    now = datetime.datetime.now()

    assert facts['year'] == now.strftime('%Y')
    assert len(facts['year']) == 4

    assert facts['month'] == now.strftime('%m')
    assert len(facts['month']) == 2

    assert facts['day'] == now.strftime('%d')
    assert len(facts['day']) == 2

    assert facts['hour'] == now.strftime('%H')
    assert len(facts['hour']) == 2

    assert facts['minute'] == now.strftime('%M')
    assert len(facts['minute']) == 2

    assert facts['second'] == now.strftime('%S')
    assert len(facts['second']) == 2

    # weekday_number must be a single digit 0-6
    assert re.match(r'^[0-6]$', facts['weekday_number'])

    # weeknumber must be two digits
    assert re.match(r'^\d{2}$', facts['weeknumber'])

    # weekday must be a full day name
    assert facts['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # date must be YYYY-MM-DD
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', facts['date'])

    # time must be HH:MM:SS
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', facts['time'])

    # epoch must be numeric (int as string)
    assert re.match(r'^\d+$', facts['epoch'])

    # epoch_int must be numeric (int as string)
    assert re.match(r'^\d+$', facts['epoch_int'])

    # epoch should be close to current time (within a small tolerance)
    epoch_val = int(facts['epoch'])
    assert abs(epoch_val - time.time()) < 5

    # epoch_int should be close to current time (within a small tolerance)
    epoch_int_val = int(facts['epoch_int'])
    assert abs(epoch_int_val - time.time()) < 5

    # iso8601 must match ISO 8601 format with Z suffix (UTC)
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', facts['iso8601'])

    # iso8601_micro must match ISO 8601 format with microseconds and Z suffix
    assert re.match(
        r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$',
        facts['iso8601_micro']
    )

    # iso8601_basic must match basic format without separators
    assert re.match(r'^\d{8}T\d{6}\d*$', facts['iso8601_basic'])

    # iso8601_basic_short must match basic format without microseconds
    assert re.match(r'^\d{8}T\d{6}$', facts['iso8601_basic_short'])

    # tz facts must be non-empty strings
    assert len(facts['tz']) > 0
    assert len(facts['tz_dst']) > 0
    assert len(facts['tz_offset']) > 0

    # tz_offset should look like +HHMM or -HHMM
    assert re.match(r'^[+-]\d{4}$', facts['tz_offset'])


def test_DateTimeFactCollector_collect_with_args():
    # module_0.collect() should accept optional module and collected_facts args and ignore them
    collector = DateTimeFactCollector()

    result = collector.collect(module=None, collected_facts={})

    assert isinstance(result, dict)
    assert 'date_time' in result
    facts = result['date_time']
    assert 'year' in facts
    assert 'epoch' in facts
    assert 'iso8601' in facts


def test_DateTimeFactCollector_collect_epoch_not_placeholder():
    # Regression test: epoch must never contain the unformatted '%' placeholder
    collector = DateTimeFactCollector()
    result = collector.collect()
    facts = result['date_time']

    assert '%' not in facts['epoch']
    assert '%' not in facts['epoch_int']
    assert facts['epoch'] != ''
    assert facts['epoch_int'] != ''

# Generated at 2026-11-01 22:56:51.760651
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector_obj = DateTimeFactCollector()

    assert isinstance(collector_obj, DateTimeFactCollector)
    assert collector_obj.name == 'date_time'
    assert isinstance(collector_obj._fact_ids, set)
    assert callable(collector_obj.collect)

# Generated at 2026-11-01 22:57:35.899364
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()

# Generated at 2026-11-01 22:57:56.074701
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import re

    collector = DateTimeFactCollector()
    facts_dict = collector.collect()

    assert isinstance(facts_dict, dict)
    assert 'date_time' in facts_dict

    date_time_facts = facts_dict['date_time']
    assert isinstance(date_time_facts, dict)

    expected_keys = set([
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    ])
    assert set(date_time_facts.keys()) == expected_keys

    # Verify string formats
    assert re.match(r'^\d{4}$', date_time_facts['year'])
    assert re.match(r'^\d{2}$', date_time_facts['month'])
    assert re.match(r'^\d{2}$', date_time_facts['day'])
    assert re.match(r'^\d{2}$', date_time_facts['hour'])
    assert re.match(r'^\d{2}$', date_time_facts['minute'])
    assert re.match(r'^\d{2}$', date_time_facts['second'])
    assert re.match(r'^\d+$', date_time_facts['epoch'])
    assert re.match(r'^\d+$', date_time_facts['epoch_int'])
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', date_time_facts['date'])
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', date_time_facts['time'])
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$',
                    date_time_facts['iso8601_micro'])
    assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$',
                    date_time_facts['iso8601'])
    assert re.match(r'^\d{8}T\d{12}$', date_time_facts['iso8601_basic'])
    assert re.match(r'^\d{8}T\d{6}$', date_time_facts['iso8601_basic_short'])
    assert re.match(r'^[+-]\d{4}$', date_time_facts['tz_offset'])

    # Verify value ranges
    assert 1 <= int(date_time_facts['month']) <= 12
    assert 1 <= int(date_time_facts['day']) <= 31
    assert 0 <= int(date_time_facts['hour']) <= 23
    assert 0 <= int(date_time_facts['minute']) <= 59
    assert 0 <= int(date_time_facts['second']) <= 59
    assert date_time_facts['weekday_number'] in [str(i) for i in range(7)]

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']
    assert date_time_facts['weekday'] in weekdays

    # epoch and epoch_int should be consistent integers of time.time()
    epoch_ts = int(time.time())
    assert abs(int(date_time_facts['epoch']) - epoch_ts) <= 2
    assert abs(int(date_time_facts['epoch_int']) - epoch_ts) <= 2

    # date/time should be internally consistent
    assert date_time_facts['date'] == '%s-%s-%s' % (
        date_time_facts['year'], date_time_facts['month'], date_time_facts['day'])
    assert date_time_facts['time'] == '%s:%s:%s' % (
        date_time_facts['hour'], date_time_facts['minute'], date_time_facts['second'])

    # iso8601 should be derived from the date and time (UTC)
    assert date_time_facts['iso8601'].startswith(date_time_facts['iso8601_micro'][:19])

    # tz facts should be non-empty strings
    assert isinstance(date_time_facts['tz'], str)
    assert isinstance(date_time_facts['tz_dst'], str)
    assert isinstance(date_time_facts['tz_offset'], str)

# Generated at 2026-11-01 22:58:34.475566
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH) as mock_time:
        collector = DateTimeFactCollector()
        facts_dict = collector.collect()

        mock_time.assert_called_once_with()

        assert isinstance(facts_dict, dict)
        assert 'date_time' in facts_dict
        date_time_facts = facts_dict['date_time']

        # Recompute expected values from the mocked epoch
        now = datetime.datetime.fromtimestamp(FIXED_EPOCH)
        utcnow = datetime.datetime.utcfromtimestamp(FIXED_EPOCH)

        expected_keys = [
            'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
            'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
            'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
            'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset',
        ]
        for key in expected_keys:
            assert key in date_time_facts

        # All fact values must be strings
        for value in date_time_facts.values():
            assert isinstance(value, str)

        # Verify each field is formatted from the mocked timestamp
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

        # ISO8601 values are based on UTC
        assert date_time_facts['iso8601_micro'] == utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        assert date_time_facts['iso8601'] == utcnow.strftime("%Y-%m-%dT%H:%M:%SZ")
        assert date_time_facts['iso8601_basic'] == now.strftime("%Y%m%dT%H%M%S%f")
        assert date_time_facts['iso8601_basic_short'] == now.strftime("%Y%m%dT%H%M%S")

        assert date_time_facts['iso8601'] == '2018-03-16T19:05:48Z'
        assert date_time_facts['iso8601_micro'] == '2018-03-16T19:05:48.033332Z'

        # Timezone facts come straight from the time module
        assert date_time_facts['tz'] == time.strftime("%Z")
        assert date_time_facts['tz_dst'] == time.tzname[1]
        assert date_time_facts['tz_offset'] == time.strftime("%z")

        # Epoch handling: strftime('%s') result, falling back to int(epoch) on
        # platforms where '%s' is unsupported
        expected_epoch = now.strftime('%s')
        if expected_epoch == '' or expected_epoch[0] == '%':
            expected_epoch = str(int(FIXED_EPOCH))
        assert date_time_facts['epoch'] == expected_epoch

        expected_epoch_int = str(int(now.strftime('%s')))
        if expected_epoch_int == '' or expected_epoch_int[0] == '%':
            expected_epoch_int = str(int(FIXED_EPOCH))
        assert date_time_facts['epoch_int'] == expected_epoch_int

        # Deterministic with a fixed clock
        assert collector.collect() == {'date_time': date_time_facts}


# Unit test for the default state of DateTimeFactCollector
def test_DateTimeFactCollector_defaults():
    collector = DateTimeFactCollector()
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()


# Unit test ensuring module_0.collect() contains every documented date_time key

# Generated at 2026-11-01 22:59:27.455512
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    # Freeze time at a known instant: 2019-01-01 00:00:00 UTC
    fixed_epoch = 1546300800.0

    collector = DateTimeFactCollector()
    assert collector.name == 'date_time'

    real_time = time.time
    try:
        time.time = lambda: fixed_epoch
        facts_dict = collector.collect(module=None, collected_facts=None)
    finally:
        time.time = real_time

    assert isinstance(facts_dict, dict)
    assert set(facts_dict.keys()) == {'date_time'}

    date_time_facts = facts_dict['date_time']
    assert isinstance(date_time_facts, dict)

    expected_keys = set([
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset',
    ])
    assert set(date_time_facts.keys()) == expected_keys

    # Every fact value must be a string

# Generated at 2026-11-01 23:00:08.384561
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import time as _time
    import datetime as _datetime
    from unittest.mock import patch

    collector = DateTimeFactCollector()

    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset',
    }

    # Freeze the timestamp so results are deterministic
    with patch('time.time', return_value=1234567890.0) as mock_time:
        facts = collector.collect()

    # The timestamp must be captured exactly once
    mock_time.assert_called_once_with()

    assert isinstance(facts, dict)
    assert 'date_time' in facts

# Generated at 2026-11-01 23:01:20.779004
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import re
    from unittest.mock import patch

    fake_epoch = 1520000000.5

    with patch('time.time', return_value=fake_epoch):
        collector = DateTimeFactCollector()
        facts = collector.collect(module=None, collected_facts=None)

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    date_time_facts = facts['date_time']

    expected_keys = [
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 'day',
        'hour', 'minute', 'second', 'epoch', 'epoch_int', 'date', 'time',
        'iso8601_micro', 'iso8601', 'iso8601_basic', 'iso8601_basic_short',
        'tz', 'tz_dst', 'tz_offset',
    ]
    for key in expected_keys:
        assert key in date_time_facts

    now = datetime.datetime.fromtimestamp(fake_epoch)
    utcnow = datetime.datetime.utcfromtimestamp(fake_epoch)

    assert date_time_facts['year'] == now.strftime('%Y')
    assert date_time_facts['month'] == now.strftime('%m')
    assert date_time_facts['weekday'] == now.strftime('%A')
    assert date_time_facts['weekday_number'] == now.strftime('%w')
    assert date_time_facts['weeknumber'] == now.strftime('%W')
    assert date_time_facts['day'] == now.strftime('%d')
    assert date_time_facts['hour'] == now.strftime('%H')
    assert date_time_facts['minute'] == now.strftime('%M')
    assert date_time_facts['second'] == now.strftime('%S')

    # epoch / epoch_int may fall back to int(epoch_ts) where %s is unsupported
    assert re.match(r'^\d+$', str(date_time_facts['epoch']))
    assert re.match(r'^\d+$', str(date_time_facts['epoch_int']))

    assert date_time_facts['date'] == now.strftime('%Y-%m-%d')
    assert date_time_facts['time'] == now.strftime('%H:%M:%S')

    assert date_time_facts['iso8601_micro'] == utcnow.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert date_time_facts['iso8601'] == utcnow.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert date_time_facts['iso8601_basic'] == now.strftime("%Y%m%dT%H%M%S%f")
    assert date_time_facts['iso8601_basic_short'] == now.strftime("%Y%m%dT%H%M%S")

    assert isinstance(date_time_facts['tz'], str)
    assert isinstance(date_time_facts['tz_dst'], str)
    assert isinstance(date_time_facts['tz_offset'], str)

# Generated at 2026-11-01 23:01:58.355506
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    collector = DateTimeFactCollector()
    facts = collector.collect()

    assert 'date_time' in facts
    date_time_facts = facts['date_time']


# Generated at 2026-11-01 23:02:23.441567
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from unittest.mock import patch
    import datetime

    collector = DateTimeFactCollector()

    # Fixed timestamp: 2020-01-15 10:30:45 UTC (a Wednesday)
    fixed_epoch = 1579081845.0
    fixed_utc = datetime.datetime(2020, 1, 15, 10, 30, 45)

    with patch('time.time', return_value=fixed_epoch), \
         patch('ansible.module_utils.facts collectors.date_time.datetime.datetime') as mock_dt, \
         patch('time.strftime', side_effect=lambda fmt: fixed_utc.strftime(fmt) if fmt == '%z' else 'UTC' if fmt == '%Z' else fixed_utc.strftime(fmt)), \
         patch('time.tzname', ('UTC', 'UTC')):
        mock_dt.fromtimestamp.return_value = fixed_utc
        mock_dt.utcfromtimestamp.return_value = fixed_utc
        # strftime must still work on real datetime objects
        mock_dt.datetime = datetime.datetime

        facts = collector.collect()

    assert 'date_time' in facts
    dt = facts['date_time']

    assert dt['year'] == '2020'
    assert dt['month'] == '01'
    assert dt['weekday'] == 'Wednesday'
    assert dt['weekday_number'] == '3'
    assert dt['weeknumber'] == '03'
    assert dt['day'] == '15'
    assert dt['hour'] == '10'
    assert dt['minute'] == '30'
    assert dt['second'] == '45'
    assert dt['epoch'] == '1579081845'
    assert dt['epoch_int'] == '1579081845'
    assert dt['date'] == '2020-01-15'
    assert dt['time'] == '10:30:45'
    assert dt['iso8601_micro'] == '2020-01-15T10:30:45.000000Z'
    assert dt['iso8601'] == '2020-01-15T10:30:45Z'
    assert dt['iso8601_basic'] == '20200115T103045000000'
    assert dt['iso8601_basic_short'] == '20200115T103045'
    assert dt['tz'] == 'UTC'
    assert dt['tz_dst'] == 'UTC'
    assert dt['tz_offset'] == '+0000'


# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect_handles_epoch_fallback():
    from unittest.mock import patch

    collector = DateTimeFactCollector()

    # Simulate platform where %s is unsupported (strftime returns the literal format)
    with patch('time.time', return_value=1579081845.0), \
         patch('time.strftime', return_value=''):
        facts = collector.collect()

    dt = facts['date_time']
    assert dt['epoch'] == '1579081845'
    assert dt['epoch_int'] == '1579081845'


# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect_ignores_collected_facts():
    from unittest.mock import patch

    collector = DateTimeFactCollector()

    with patch('time.time', return_value=1579081845.0), \
         patch('time.strftime', return_value=''):
        facts = collector.collect(module=None, collected_facts={'foo': 'bar'})

    assert facts == {'date_time': facts['date_time']}
    assert 'foo' not in facts

# Generated at 2026-11-01 23:03:24.988417
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-11-01 23:04:05.333615
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-11-01 23:04:33.143018
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import sys
    import datetime as datetime_module
    from unittest import mock
    from ansible.module_utils.facts.system.date_time import DateTimeFactCollector

    EPOCH_TS = 1484473845.123456

    class FixedEpochDateTime(datetime_module.datetime):
        # Make '%s' deterministic regardless of host timezone/platform
        def strftime(self, fmt):
            if fmt == '%s':
                return '1484473845'
            return super(FixedEpochDateTime, self).strftime(fmt)

    fake_local = FixedEpochDateTime(2017, 1, 15, 11, 30, 45, 123456)
    fake_utc = FixedEpochDateTime(2017, 1, 15, 10, 30, 45, 123456)

    fake_datetime_ns = mock.Mock()
    fake_datetime_ns.datetime.fromtimestamp.return_value = fake_local
    fake_datetime_ns.datetime.utcfromtimestamp.return_value = fake_utc

    def fake_time_strftime(fmt):
        return {'%Z': 'CET', '%z': '+0100'}[fmt]

    module = sys.modules[DateTimeFactCollector.__module__]

    with mock.patch.object(module, 'datetime', fake_datetime_ns), \
            mock.patch.object(module, 'time') as mock_time:
        mock_time.time.return_value = EPOCH_TS
        mock_time.strftime.side_effect = fake_time_strftime
        mock_time.tzname = ('CET', 'CEST')

        collector = DateTimeFactCollector()
        facts = collector.collect(module=None, collected_facts=None)

    expected = {
        'date_time': {
            'year': '2017',
            'month': '01',
            'weekday': 'Sunday',
            'weekday_number': '0',
            'weeknumber': '02',
            'day': '15',
            'hour': '11',
            'minute': '30',
            'second': '45',
            'epoch': '1484473845',
            'epoch_int': '1484473845',
            'date': '2017-01-15',
            'time': '11:30:45',
            'iso8601_micro': '2017-01-15T10:30:45.123456Z',
            'iso8601': '2017-01-15T10:30:45Z',
            'iso8601_basic': '20170115T113045123456',
            'iso8601_basic_short': '20170115T113045',
            'tz': 'CET',
            'tz_dst': 'CEST',
            'tz_offset': '+0100',
        }
    }

    assert facts == expected