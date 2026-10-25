

# Generated at 2026-10-24 06:44:46.828623
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:44:49.251741
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:44:51.663319
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:44:54.078004
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 06:44:56.503001
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 06:44:58.907538
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:01.446038
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:02.796131
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():collector = DateTimeFactCollector()

# Generated at 2026-10-24 06:45:05.439410
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:06.742268
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():collector = DateTimeFactCollector()

# Generated at 2026-10-24 06:45:08.069482
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

# Generated at 2026-10-24 06:45:09.388768
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

# Generated at 2026-10-24 06:45:10.719355
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

# Generated at 2026-10-24 06:45:12.147289
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

# Generated at 2026-10-24 06:45:13.463130
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

# Generated at 2026-10-24 06:45:14.777297
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

# Generated at 2026-10-24 06:45:16.108158
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

# Generated at 2026-10-24 06:45:17.420079
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

# Generated at 2026-10-24 06:45:18.744363
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

# Generated at 2026-10-24 06:45:20.059941
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

# Generated at 2026-10-24 06:45:21.387240
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

# Generated at 2026-10-24 06:45:22.757428
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

# Generated at 2026-10-24 06:45:24.109049
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

# Generated at 2026-10-24 06:45:25.645275
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

# Generated at 2026-10-24 06:45:26.965959
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

# Generated at 2026-10-24 06:45:28.288523
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

# Generated at 2026-10-24 06:45:30.708206
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:33.127139
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:35.542591
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:37.957012
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:40.373251
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:42.788999
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:45.297759
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:47.713046
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:50.126587
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:52.541884
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:54.957905
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:57.372976
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:45:59.785636
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:02.213578
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:04.622171
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:07.036135
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:09.449878
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:11.861810
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:14.279035
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:16.692865
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:19.108242
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:21.519632
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:23.940783
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:26.346019
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:28.757768
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:31.173269
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:33.586479
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:35.997727
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:38.411837
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:40.836939
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:43.249440
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:45.663111
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:48.077347
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:50.493201
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:52.908890
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:55.321718
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:46:57.736545
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:00.566892
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 06:47:01.871668
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

# Generated at 2026-10-24 06:47:03.187346
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

# Generated at 2026-10-24 06:47:04.522166
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

# Generated at 2026-10-24 06:47:05.843229
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

# Generated at 2026-10-24 06:47:07.145275
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

# Generated at 2026-10-24 06:47:08.461878
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

# Generated at 2026-10-24 06:47:09.793591
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

# Generated at 2026-10-24 06:47:11.094511
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

# Generated at 2026-10-24 06:47:12.413818
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

# Generated at 2026-10-24 06:47:13.716821
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

# Generated at 2026-10-24 06:47:15.045219
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

# Generated at 2026-10-24 06:47:16.370310
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

# Generated at 2026-10-24 06:47:18.606646
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

# Generated at 2026-10-24 06:47:19.921673
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

# Generated at 2026-10-24 06:47:21.402528
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

# Generated at 2026-10-24 06:47:22.706680
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

# Generated at 2026-10-24 06:47:24.019749
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

# Generated at 2026-10-24 06:47:25.342344
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

# Generated at 2026-10-24 06:47:27.761186
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:30.258785
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:32.675453
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:35.091088
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:37.515379
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:39.928459
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:42.347664
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:44.766884
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:47.182088
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:49.804645
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:52.217887
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:54.637982
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:47:59.456584
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:48:01.872523
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:48:04.288765
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:48:05.616044
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

# Generated at 2026-10-24 06:48:07.332602
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

# Generated at 2026-10-24 06:48:08.659788
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

# Generated at 2026-10-24 06:48:09.979726
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

# Generated at 2026-10-24 06:48:11.307917
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

# Generated at 2026-10-24 06:48:12.632646
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

# Generated at 2026-10-24 06:48:13.950162
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

# Generated at 2026-10-24 06:48:15.273616
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

# Generated at 2026-10-24 06:48:16.606775
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

# Generated at 2026-10-24 06:48:22.858161
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

# Generated at 2026-10-24 06:48:24.188442
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

# Generated at 2026-10-24 06:48:25.537693
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

# Generated at 2026-10-24 06:48:26.842148
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

# Generated at 2026-10-24 06:48:28.155265
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

# Generated at 2026-10-24 06:48:29.505944
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

# Generated at 2026-10-24 06:48:30.831584
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

# Generated at 2026-10-24 06:48:32.155493
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

# Generated at 2026-10-24 06:48:33.459702
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

# Generated at 2026-10-24 06:48:34.766543
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

# Generated at 2026-10-24 06:48:52.123206
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:48:54.631040
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:48:57.047206
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:48:59.462638
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:01.879933
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:04.295965
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:06.712041
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:09.131137
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:11.553022
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:13.966125
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:16.385426
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:18.799507
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:21.220515
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:23.623890
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:26.039331
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:28.453920
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:30.868888
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:33.282418
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:49:34.699293
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

# Generated at 2026-10-24 06:49:36.016641
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

# Generated at 2026-10-24 06:49:37.382694
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

# Generated at 2026-10-24 06:49:38.688790
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

# Generated at 2026-10-24 06:50:06.094974
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

# Generated at 2026-10-24 06:50:07.549217
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

# Generated at 2026-10-24 06:50:08.882959
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

# Generated at 2026-10-24 06:50:10.198227
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

# Generated at 2026-10-24 06:50:11.533168
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

# Generated at 2026-10-24 06:50:12.986773
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

# Generated at 2026-10-24 06:50:14.324398
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

# Generated at 2026-10-24 06:50:15.680597
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

# Generated at 2026-10-24 06:50:17.026378
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

# Generated at 2026-10-24 06:50:19.580214
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:50:22.173283
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:50:24.590375
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:51:25.072419
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

# Generated at 2026-10-24 06:51:26.498107
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

# Generated at 2026-10-24 06:51:28.033686
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

# Generated at 2026-10-24 06:51:29.468278
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

# Generated at 2026-10-24 06:51:30.829614
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

# Generated at 2026-10-24 06:51:32.166261
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

# Generated at 2026-10-24 06:51:33.495049
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

# Generated at 2026-10-24 06:51:34.859671
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

# Generated at 2026-10-24 06:51:37.453436
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:51:40.164403
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 06:51:41.467373
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

# Generated at 2026-10-24 06:53:40.466464
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:53:42.879868
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:53:45.295521
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:53:48.073430
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-24 06:53:50.821047
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():from unittest.mock import patch

# Generated at 2026-10-24 06:53:52.124360
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

# Generated at 2026-10-24 06:53:53.430764
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

# Generated at 2026-10-24 06:53:54.743812
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

# Generated at 2026-10-24 06:53:56.058542
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

# Generated at 2026-10-24 06:53:57.369752
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

# Generated at 2026-10-24 06:53:58.746622
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

# Generated at 2026-10-24 06:54:00.072171
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

# Generated at 2026-10-24 06:54:01.404660
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