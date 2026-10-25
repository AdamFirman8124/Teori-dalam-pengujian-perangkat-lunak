

# Generated at 2026-10-24 03:50:48.623508
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

# Generated at 2026-10-24 03:50:51.385661
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 03:50:53.892109
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 03:50:56.499109
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 03:50:59.002313
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:01.423839
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:03.841015
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:06.259063
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:08.673894
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:11.091986
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:13.778264
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:15.090638
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():collector = DateTimeFactCollector()

# Generated at 2026-10-24 03:51:16.406084
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

# Generated at 2026-10-24 03:51:17.712721
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

# Generated at 2026-10-24 03:51:19.025972
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

# Generated at 2026-10-24 03:51:20.338918
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

# Generated at 2026-10-24 03:51:21.653447
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

# Generated at 2026-10-24 03:51:22.996419
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

# Generated at 2026-10-24 03:51:24.334670
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

# Generated at 2026-10-24 03:51:25.701383
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

# Generated at 2026-10-24 03:51:27.019125
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

# Generated at 2026-10-24 03:51:28.336725
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

# Generated at 2026-10-24 03:51:29.688507
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

# Generated at 2026-10-24 03:51:30.996922
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

# Generated at 2026-10-24 03:51:32.300064
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

# Generated at 2026-10-24 03:51:33.607870
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

# Generated at 2026-10-24 03:51:34.916121
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

# Generated at 2026-10-24 03:51:36.251241
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

# Generated at 2026-10-24 03:51:37.575675
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

# Generated at 2026-10-24 03:51:40.091908
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:42.602097
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:45.040926
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:47.552231
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:49.970714
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:52.386852
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:54.802677
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:57.218669
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:51:59.636436
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:52:02.053367
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:52:04.469049
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:52:06.884094
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:52:09.312835
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:52:11.726679
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:52:14.143077
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:52:16.559548
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:52:37.016646
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import Mock, patch

# Generated at 2026-10-24 03:52:38.600063
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

# Generated at 2026-10-24 03:52:39.931132
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

# Generated at 2026-10-24 03:52:41.238317
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

# Generated at 2026-10-24 03:52:42.571731
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

# Generated at 2026-10-24 03:52:43.879670
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

# Generated at 2026-10-24 03:52:45.204248
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

# Generated at 2026-10-24 03:52:46.523923
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

# Generated at 2026-10-24 03:52:47.919512
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

# Generated at 2026-10-24 03:52:49.230244
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

# Generated at 2026-10-24 03:52:50.684143
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

# Generated at 2026-10-24 03:52:51.991290
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

# Generated at 2026-10-24 03:52:53.316128
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

# Generated at 2026-10-24 03:52:54.631599
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

# Generated at 2026-10-24 03:52:55.947268
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

# Generated at 2026-10-24 03:52:57.257447
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

# Generated at 2026-10-24 03:52:59.760344
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:02.178272
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:04.589168
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:07.005451
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:09.420540
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:11.837257
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:14.484228
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:16.900707
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:19.318447
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:21.736787
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:24.151815
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:26.569353
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:28.982070
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:31.398092
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:33.812825
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:36.228212
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:38.643461
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:41.058737
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:43.471860
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:53:45.886996
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:54:02.160379
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from types import SimpleNamespace

# Generated at 2026-10-24 03:54:03.468433
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

# Generated at 2026-10-24 03:54:04.786330
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

# Generated at 2026-10-24 03:54:06.105209
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

# Generated at 2026-10-24 03:54:07.404183
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

# Generated at 2026-10-24 03:54:08.708558
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

# Generated at 2026-10-24 03:54:11.527668
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

# Generated at 2026-10-24 03:54:12.827951
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

# Generated at 2026-10-24 03:54:14.135870
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

# Generated at 2026-10-24 03:54:15.437060
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

# Generated at 2026-10-24 03:54:16.745633
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

# Generated at 2026-10-24 03:54:18.055417
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

# Generated at 2026-10-24 03:54:19.360232
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

# Generated at 2026-10-24 03:54:20.707345
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

# Generated at 2026-10-24 03:54:22.013828
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

# Generated at 2026-10-24 03:54:23.321344
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

# Generated at 2026-10-24 03:54:28.835115
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

# Generated at 2026-10-24 03:54:30.198341
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

# Generated at 2026-10-24 03:54:31.515525
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

# Generated at 2026-10-24 03:54:32.829206
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

# Generated at 2026-10-24 03:54:34.147780
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

# Generated at 2026-10-24 03:54:35.469951
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

# Generated at 2026-10-24 03:54:36.783883
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

# Generated at 2026-10-24 03:54:38.110410
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

# Generated at 2026-10-24 03:54:39.412174
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

# Generated at 2026-10-24 03:54:40.741997
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

# Generated at 2026-10-24 03:54:51.688993
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

# Generated at 2026-10-24 03:54:52.993832
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

# Generated at 2026-10-24 03:54:54.309736
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

# Generated at 2026-10-24 03:54:55.649434
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

# Generated at 2026-10-24 03:54:56.992386
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

# Generated at 2026-10-24 03:54:58.372134
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

# Generated at 2026-10-24 03:54:59.703198
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

# Generated at 2026-10-24 03:55:01.028018
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

# Generated at 2026-10-24 03:55:02.472152
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

# Generated at 2026-10-24 03:55:03.800708
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

# Generated at 2026-10-24 03:55:28.449836
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

# Generated at 2026-10-24 03:55:29.778964
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

# Generated at 2026-10-24 03:55:31.089738
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

# Generated at 2026-10-24 03:55:32.407981
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

# Generated at 2026-10-24 03:55:33.714410
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

# Generated at 2026-10-24 03:55:35.038792
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

# Generated at 2026-10-24 03:55:36.351995
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

# Generated at 2026-10-24 03:55:37.674458
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

# Generated at 2026-10-24 03:55:38.982272
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

# Generated at 2026-10-24 03:55:40.305162
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

# Generated at 2026-10-24 03:56:23.680407
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

# Generated at 2026-10-24 03:56:24.995210
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

# Generated at 2026-10-24 03:56:26.323082
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

# Generated at 2026-10-24 03:56:28.740802
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 03:56:48.865193
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():import sys

# Generated at 2026-10-24 03:56:50.167098
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

# Generated at 2026-10-24 03:56:51.467008
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

# Generated at 2026-10-24 03:56:52.769631
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

# Generated at 2026-10-24 03:56:54.117737
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

# Generated at 2026-10-24 03:56:55.450680
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

# Generated at 2026-10-24 03:56:56.781002
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

# Generated at 2026-10-24 03:58:28.415543
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

# Generated at 2026-10-24 03:58:29.786549
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

# Generated at 2026-10-24 03:58:31.104941
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

# Generated at 2026-10-24 03:58:32.434215
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

# Generated at 2026-10-24 03:58:33.726952
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

# Generated at 2026-10-24 03:58:35.028316
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

# Generated at 2026-10-24 03:58:36.334890
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

# Generated at 2026-10-24 03:58:37.654936
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

# Generated at 2026-10-24 03:58:38.960261
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

# Generated at 2026-10-24 03:58:40.337944
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