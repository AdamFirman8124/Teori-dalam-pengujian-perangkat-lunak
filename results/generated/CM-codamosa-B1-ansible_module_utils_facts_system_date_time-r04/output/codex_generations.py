

# Generated at 2026-10-24 04:39:12.091714
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:39:14.771164
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:17.272864
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:19.859277
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:22.271449
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:24.682041
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:27.095094
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:29.639626
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:32.049968
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:34.460173
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:36.871952
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:39.286421
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:41.699052
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 04:39:43.089569
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:39:44.453082
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:40:03.282641
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:40:24.721284
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():import datetime as real_datetime

# Generated at 2026-10-24 04:40:25.991024
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:40:28.593269
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:40:31.105931
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:40:33.518894
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:40:36.089130
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:40:38.499676
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:40:40.908897
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:40:43.318742
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:03.366308
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from types import SimpleNamespace

# Generated at 2026-10-24 04:41:04.686533
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:41:06.022357
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:41:07.332135
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:41:08.647569
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:41:09.960384
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:41:11.277837
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:41:12.591763
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:41:13.898144
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:41:16.511470
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:18.965153
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:21.375175
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:23.786342
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:26.198233
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:28.712753
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:31.127024
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:33.537578
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:35.949249
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:38.361094
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:40.771842
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:43.183549
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:45.595512
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:48.011391
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:50.424728
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:52.837701
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:55.250213
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:41:57.660816
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:00.072858
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:19.885084
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from types import SimpleNamespace

# Generated at 2026-10-24 04:42:21.187368
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:22.509799
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:23.869963
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:25.206923
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:28.987191
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:30.309183
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:31.617039
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:32.923625
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:34.236039
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:35.565248
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:36.883234
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:42:39.295393
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:42.000810
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:44.413599
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:46.899525
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:49.314617
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:51.732249
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:54.376156
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:56.790102
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:42:59.200657
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:01.612705
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:04.025458
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:06.439266
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:08.854102
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:11.267664
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:13.685025
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:16.101229
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:18.511369
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:20.923529
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:23.339745
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:25.752210
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:28.164852
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:30.575337
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:32.989229
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:35.403418
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:37.817010
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:40.231634
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:42.643877
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:45.059804
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:47.474327
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:49.888147
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:52.302296
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:54.713839
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:57.124793
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:43:59.735443
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:16.665698
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from types import SimpleNamespace

# Generated at 2026-10-24 04:44:18.028823
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:44:19.398391
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:44:20.711614
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:44:22.187119
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:44:23.485143
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:44:25.667658
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:44:26.975996
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:44:29.478532
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:31.982797
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:34.487267
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:37.009723
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:39.423107
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:41.835267
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:44.247292
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:46.660563
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:49.074805
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:51.489272
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:53.903767
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:56.319015
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:44:58.732253
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:01.150073
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:03.564699
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:05.975577
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:08.388319
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:10.802835
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:13.218433
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:15.632879
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:18.045652
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:20.461891
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:22.875781
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:25.291981
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:30.198274
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:32.609804
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:35.025612
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:37.437699
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:39.849772
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:42.268331
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:44.680053
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:47.106855
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:49.510997
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:51.934344
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:54.340358
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:56.751994
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:45:59.165271
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:01.588232
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:03.992909
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:06.409709
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:08.834922
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:11.242572
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:13.657608
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:16.071005
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:18.486286
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:20.900590
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:23.315851
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:25.729139
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:28.140953
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:30.556442
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:32.967183
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:35.392462
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:37.808553
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:40.220808
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:46:47.931393
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:46:49.377922
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:46:50.676594
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:46:52.067428
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:46:53.367403
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:46:54.704860
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:46:56.032554
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:46:57.493509
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:46:58.820134
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:47:00.373213
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:47:18.321831
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:20.735038
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:23.247004
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:25.656114
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:28.071465
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:30.623157
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:33.117580
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:35.538536
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:37.946938
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:47:40.361948
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:48:02.524881
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from types import SimpleNamespace

# Generated at 2026-10-24 04:48:03.948793
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:05.271212
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:06.597285
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:07.909808
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:09.222078
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:10.521588
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:42.898404
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:48:45.313631
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:48:47.727168
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 04:48:49.076678
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:50.383160
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:51.774007
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:53.071271
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:54.384694
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:55.694494
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:57.001938
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:58.335336
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant

# Generated at 2026-10-24 04:48:59.663986
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    with patch('time.time', return_value=FIXED_EPOCH):
        facts = DateTimeFactCollector().collect()

    assert isinstance(facts, dict)
    assert 'date_time' in facts
    dt = facts['date_time']

    # exact key set -- catches silently added/renamed facts
    assert set(dt) == EXPECTED_KEYS
    assert all(isinstance(v, str) for v in dt.values())

    # epoch is derived from the single captured timestamp
    assert dt['epoch'] == str(int(FIXED_EPOCH))
    assert dt['epoch_int'] == str(int(FIXED_EPOCH))

    # format checks (values are tz-dependent, shapes are not)
    assert re.fullmatch(r'\d{4}', dt['year'])
    assert re.fullmatch(r'\d{2}', dt['month'])
    assert re.fullmatch(r'\d{2}', dt['day'])
    assert re.fullmatch(r'\d{2}', dt['hour'])
    assert re.fullmatch(r'\d{2}', dt['minute'])
    assert re.fullmatch(r'\d{2}', dt['second'])
    assert re.fullmatch(r'[0-6]', dt['weekday_number'])
    assert re.fullmatch(r'\d{2}', dt['weeknumber'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', dt['date'])
    assert re.fullmatch(r'\d{2}:\d{2}:\d{2}', dt['time'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z', dt['iso8601_micro'])
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', dt['iso8601'])
    assert re.fullmatch(r'\d{8}T\d{6}\d{6}', dt['iso8601_basic'])
    assert re.fullmatch(r'\d{8}T\d{6}', dt['iso8601_basic_short'])
    assert re.fullmatch(r'[+-]\d{4}', dt['tz_offset'])

    # local and UTC views must agree on the same instant