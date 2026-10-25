

# Generated at 2026-10-24 06:34:28.561423
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

# Generated at 2026-10-24 06:34:29.887662
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

# Generated at 2026-10-24 06:34:31.204625
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

# Generated at 2026-10-24 06:34:33.818211
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 06:34:35.132407
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():collector = DateTimeFactCollector()

# Generated at 2026-10-24 06:34:37.770000
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 06:34:39.079101
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():collector = DateTimeFactCollector()

# Generated at 2026-10-24 06:34:40.410208
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

# Generated at 2026-10-24 06:34:41.730145
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

# Generated at 2026-10-24 06:34:43.035821
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

# Generated at 2026-10-24 06:34:44.404527
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

# Generated at 2026-10-24 06:34:45.716608
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

# Generated at 2026-10-24 06:34:47.020814
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

# Generated at 2026-10-24 06:34:48.391710
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

# Generated at 2026-10-24 06:34:49.711742
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

# Generated at 2026-10-24 06:34:51.041190
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

# Generated at 2026-10-24 06:34:52.348028
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

# Generated at 2026-10-24 06:34:53.655168
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

# Generated at 2026-10-24 06:34:54.989406
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

# Generated at 2026-10-24 06:34:56.315478
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

# Generated at 2026-10-24 06:34:57.616900
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

# Generated at 2026-10-24 06:34:58.928934
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

# Generated at 2026-10-24 06:35:00.270587
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

# Generated at 2026-10-24 06:35:01.597891
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

# Generated at 2026-10-24 06:35:02.915316
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

# Generated at 2026-10-24 06:35:04.248587
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

# Generated at 2026-10-24 06:35:05.572065
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

# Generated at 2026-10-24 06:35:06.927205
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

# Generated at 2026-10-24 06:35:09.442710
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:11.966052
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:14.382882
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:16.796113
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:19.212742
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:21.708337
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:24.124534
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:26.539119
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:28.955132
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:31.370248
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:33.784108
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:36.198509
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:38.613821
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:41.028647
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:35:59.167227
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 06:36:00.483909
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

# Generated at 2026-10-24 06:36:01.859171
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

# Generated at 2026-10-24 06:36:03.190802
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

# Generated at 2026-10-24 06:36:04.503474
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

# Generated at 2026-10-24 06:36:05.815834
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

# Generated at 2026-10-24 06:36:08.344733
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:10.760208
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:13.323286
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:15.737063
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:18.155155
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:20.567689
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:22.983842
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:25.397867
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:27.814927
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:30.227211
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:32.783223
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:35.198230
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:37.611627
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:40.038109
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:42.439411
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:44.863309
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:47.275282
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:49.688439
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:52.103957
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:54.522086
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:56.942464
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:36:59.353929
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:01.768330
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:04.184968
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:05.567150
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

# Generated at 2026-10-24 06:37:06.891088
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

# Generated at 2026-10-24 06:37:08.197747
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

# Generated at 2026-10-24 06:37:09.521357
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

# Generated at 2026-10-24 06:37:10.833414
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

# Generated at 2026-10-24 06:37:12.270855
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

# Generated at 2026-10-24 06:37:13.589027
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

# Generated at 2026-10-24 06:37:14.981596
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

# Generated at 2026-10-24 06:37:16.305323
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

# Generated at 2026-10-24 06:37:17.620296
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

# Generated at 2026-10-24 06:37:18.932682
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

# Generated at 2026-10-24 06:37:21.764027
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

# Generated at 2026-10-24 06:37:23.081515
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

# Generated at 2026-10-24 06:37:24.457703
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

# Generated at 2026-10-24 06:37:25.777099
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

# Generated at 2026-10-24 06:37:27.088445
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

# Generated at 2026-10-24 06:37:28.406310
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

# Generated at 2026-10-24 06:37:29.715820
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

# Generated at 2026-10-24 06:37:31.032734
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

# Generated at 2026-10-24 06:37:33.453639
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:35.997219
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:38.413684
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:40.834062
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:43.387501
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:45.797804
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:52.857894
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:37:55.488029
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 06:37:56.802478
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

# Generated at 2026-10-24 06:37:58.102775
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

# Generated at 2026-10-24 06:37:59.412331
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

# Generated at 2026-10-24 06:38:00.712119
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

# Generated at 2026-10-24 06:38:02.034362
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

# Generated at 2026-10-24 06:38:03.354048
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

# Generated at 2026-10-24 06:38:04.670507
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

# Generated at 2026-10-24 06:38:05.996986
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

# Generated at 2026-10-24 06:38:07.312255
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

# Generated at 2026-10-24 06:38:20.146628
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:22.565279
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:24.986607
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:27.555150
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:29.970366
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:32.389679
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:34.806924
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:37.220740
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:39.633483
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:42.048377
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:44.465065
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:46.881593
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:49.294939
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:51.712477
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:54.129438
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:56.543603
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:38:58.959584
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:01.377685
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:03.793413
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:06.207542
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:08.622816
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:11.039734
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:13.457552
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:15.870730
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:18.285826
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:20.700657
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:23.116725
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:25.529900
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:27.955778
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:30.358310
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:39:54.392672
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:12.416547
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 06:40:13.725582
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

# Generated at 2026-10-24 06:40:15.029104
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

# Generated at 2026-10-24 06:40:16.354460
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

# Generated at 2026-10-24 06:40:17.694984
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

# Generated at 2026-10-24 06:40:19.022852
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

# Generated at 2026-10-24 06:40:20.342308
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

# Generated at 2026-10-24 06:40:22.891643
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:25.305554
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:27.879580
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:30.297909
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:32.815367
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:35.230232
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:37.644960
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:40.061457
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:40:42.572938
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:38.294450
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:40.708308
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:43.125236
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:45.538411
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:47.954134
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:50.369497
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:52.787375
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:55.201901
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:41:57.615288
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:00.031758
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:02.448671
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:04.862887
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:07.277628
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:09.693027
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:12.108464
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:14.523641
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:16.941370
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:19.355571
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:21.772700
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:24.186800
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:26.606256
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:29.019998
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:31.436648
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:33.855310
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:36.275718
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:38.689566
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:42:42.306179
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 06:42:43.612432
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