

# Generated at 2026-11-02 18:36:27.434283
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-11-02 18:40:37.185454
# Unit test for method collect of class DateTimeFactCollector
def test_DateTimeFactCollector_collect():
    import datetime
    import time
    from unittest.mock import patch

    fixed_epoch = 1234567890.123456

    with patch('time.time', return_value=fixed_epoch):
        collector = DateTimeFactCollector()
        facts = collector.collect()

    assert 'date_time' in facts
    dt = facts['date_time']

    now = datetime.datetime.fromtimestamp(fixed_epoch)
    utcnow = datetime.datetime.utcfromtimestamp(fixed_epoch)

    assert dt['year'] == now.strftime('%Y')
    assert dt['month'] == now.strftime('%m')
    assert dt['weekday'] == now.strftime('%A')
    assert dt['weekday_number'] == now.strftime('%w')
    assert dt['weeknumber'] == now.strftime('%W')
    assert dt['day'] == now.strftime('%d')
    assert dt['hour'] == now.strftime('%H')
    assert dt['minute'] == now.strftime('%M')
    assert dt['second'] == now.strftime('%S')

    # epoch either comes from strftime('%s') or falls back to int(epoch_ts)
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