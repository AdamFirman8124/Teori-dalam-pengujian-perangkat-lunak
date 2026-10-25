

# Generated at 2026-10-24 10:32:48.328249
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 10:32:54.409552
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():collector = DateTimeFactCollector()

# Generated at 2026-10-24 10:33:29.843979
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:33:53.139935
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch


# Generated at 2026-10-24 10:34:27.506362
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:34:30.667904
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 10:34:31.989461
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():collector = DateTimeFactCollector()

# Generated at 2026-10-24 10:34:34.848653
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:34:37.638089
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:34:40.399971
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:34:43.149950
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:34:45.746396
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:34:48.382969
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 10:34:51.465238
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:34:54.154643
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:34:56.833446
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:34:59.591452
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:35:02.310113
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:35:05.029923
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:35:07.723540
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:35:10.294064
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:12.716088
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:15.138732
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:17.666887
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:20.087237
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:22.509962
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:25.015375
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:27.437674
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:29.946848
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:32.365630
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:34.788116
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:37.205771
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:39.627629
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:42.055063
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:44.474672
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:46.905297
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:35:49.323029
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:36:26.175797
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 10:36:28.912203
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:36:31.706937
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:36:34.554541
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:36:37.397150
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:36:40.197251
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:36:42.621661
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:36:45.041025
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:36:47.461007
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:36:49.881836
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:36:52.594864
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 10:36:55.359844
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:36:58.228254
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:00.906996
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:03.712503
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:06.420078
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:09.165312
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:11.958328
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:14.778287
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:17.457440
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:20.250612
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:23.016694
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:25.990275
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:28.741786
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:31.602262
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:34.368337
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:37:36.873301
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:37:39.292984
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:37:41.965100
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:37:44.979343
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:37:47.398850
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:37:50.028845
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:37:52.963592
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:37:55.382259
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:37:57.801280
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:38:00.478985
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:03.352534
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:06.023203
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:09.037541
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:12.160424
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:14.920330
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:17.668840
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:20.449320
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:25.621433
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:28.546122
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:31.630552
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:34.371715
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:37.130747
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:40.022041
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:42.880823
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:45.639499
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:48.406880
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:38:51.006944
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:38:53.427855
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:38:55.853752
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:39:06.128283
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:08.994278
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:12.069637
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:15.138244
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:17.885279
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:20.658324
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:23.435658
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:26.148202
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:28.963447
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:31.820950
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:39:53.198485
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:39:55.634239
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:39:58.170125
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:40:00.812981
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:40:03.235200
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:40:05.828009
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 10:40:08.622897
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:40:11.462376
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:40:14.337644
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:40:17.071400
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:40:20.080161
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:40:22.702781
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:40:25.377509
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:40:28.266474
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:01.847194
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:41:04.406651
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:41:20.884986
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch


# Generated at 2026-10-24 10:41:23.614260
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:26.326278
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:29.181366
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:31.923627
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:34.708933
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:37.770250
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:40.651375
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:43.350884
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    collector = DateTimeFactCollector()
    facts = collector.collect()

    # module_0.collect() must return a dict with a 'date_time' key
    assert isinstance(facts, dict)
    assert 'date_time' in facts

    dt = facts['date_time']

    # All expected fact keys are present
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber',
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int',
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic',
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    for key in expected_keys:
        assert key in dt, "missing fact key: %s" % key

    # All values must be strings
    for key, value in dt.items():
        assert isinstance(value, str), "fact %s is not a string: %r" % (key, value)

    # epoch / epoch_int must be integer-formatted strings and consistent
    assert dt['epoch'].isdigit()
    assert dt['epoch_int'].isdigit()
    assert dt['epoch'] == dt['epoch_int']

    # Reconstruct a timestamp from the numeric fields and compare with epoch
    reconstructed = datetime.datetime.strptime(
        dt['date'] + ' ' + dt['time'], '%Y-%m-%d %H:%M:%S'
    )
    assert int(dt['epoch']) == int(time.mktime(reconstructed.timetuple()))

    # Numeric field sanity checks
    assert len(dt['year']) == 4 and dt['year'].isdigit()
    assert 1 <= int(dt['month']) <= 12
    assert 1 <= int(dt['day']) <= 31
    assert 0 <= int(dt['hour']) <= 23
    assert 0 <= int(dt['minute']) <= 59
    assert 0 <= int(dt['second']) <= 59
    assert 0 <= int(dt['weekday_number']) <= 6
    assert 0 <= int(dt['weeknumber']) <= 53

    # Weekday is a full day name, no trailing whitespace
    assert dt['weekday'] in (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )

    # ISO 8601 formats (UTC-based, fixed suffix/format)
    assert dt['iso8601'].endswith('Z')
    assert len(dt['iso8601']) == 20  # e.g. 2023-01-05T12:34:56Z
    assert dt['iso8601_micro'].endswith('Z')
    assert len(dt['iso8601_micro']) == 27  # e.g. 2023-01-05T12:34:56.123456Z

    # iso8601 truncated to seconds matches iso8601_micro prefix
    assert dt['iso8601_micro'][:19] == dt['iso8601'][:19]

    # iso8601_basic format: YYYYmmddTHHMMSSffffff
    assert len(dt['iso8601_basic']) == 20
    assert 'T' == dt['iso8601_basic'][8]

    # iso8601_basic_short format: YYYYmmddTHHMMSS
    assert len(dt['iso8601_basic_short']) == 15

    # Cross-check iso8601 against manually derived UTC from epoch
    parsed_utc = datetime.datetime.strptime(dt['iso8601'], '%Y-%m-%dT%H:%M:%SZ')
    epoch_from_iso = int(
        (parsed_utc - datetime.datetime(1970, 1, 1)).total_seconds()
    )
    assert abs(epoch_from_iso - int(dt['epoch'])) <= 1

    # Timezone fields are non-empty strings
    assert dt['tz'] != ''
    assert dt['tz_dst'] != ''
    assert dt['tz_offset'] != ''

    # tz_offset must match +HHMM / -HHMM pattern
    assert len(dt['tz_offset']) == 5
    assert dt['tz_offset'][0] in ('+', '-')
    assert dt['tz_offset'][1:].isdigit()

    # module_0.collect() with explicit arguments behaves the same
    facts_with_args = collector.collect(module=None, collected_facts=None)
    assert facts_with_args['date_time'] == dt

# Generated at 2026-10-24 10:41:46.081811
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:41:48.592309
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 10:41:51.136601
# Unit test for method collect of class DateTimeFactCollector