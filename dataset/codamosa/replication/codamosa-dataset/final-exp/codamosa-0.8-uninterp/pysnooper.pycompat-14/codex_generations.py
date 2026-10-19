

# Generated at 2022-06-12 19:46:16.114902
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(timedelta_parse('0:00:00.000000')) == '00:00:00.000000'
    assert timedelta_format(timedelta_parse('1:02:03.045678')) == '01:02:03.045678'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'


# Generated at 2022-06-12 19:46:21.571474
# Unit test for function timedelta_format
def test_timedelta_format():
    for i in range(10 ** 6):
        delta = datetime_module.timedelta(seconds=i)
        s = timedelta_format(delta)
        delta2 = timedelta_parse(s)
        assert delta == delta2



# Generated at 2022-06-12 19:46:30.118475
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta()
    assert timedelta_parse('1:0:0.000000') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('0:1:0.000000') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:0:0.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('0:0:00.100000') == datetime_module.timedelta(microseconds=100)
    assert timedelta_parse('0:0:12.345678') == dat

# Generated at 2022-06-12 19:46:39.557339
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(0))) == \
           datetime_module.timedelta(0)

    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1))) == \
           datetime_module.timedelta(hours=1)

    assert timedelta_parse(timedelta_format(datetime_module.timedelta(minutes=1))) == \
           datetime_module.timedelta(minutes=1)

    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=1))) == \
           datetime_module.timedelta(seconds=1)


# Generated at 2022-06-12 19:46:47.171910
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for timedelta in [
        datetime_module.timedelta(days=1),
        datetime_module.timedelta(seconds=1),
    ]:
        assert timedelta == timedelta_parse(timedelta_format(timedelta))


if PY3:
    def range_next(range_iterator):
        return next(range_iterator)
else:
    def range_next(range_iterator):
        return range_iterator.next()


if PY3:
    class FileNotFoundError(OSError):
        pass
else:
    FileNotFoundError = OSError


if PY3:
    bytes_ = bytes
else:
    bytes_ = str


if PY3:
    from collections import UserList
else:
    from UserList import UserList



# Generated at 2022-06-12 19:46:58.664237
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.456789') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456789
    )


if sys.version_info[:2] >= (3, 6):
    datetime_isoformat = datetime_module.datetime.isoformat
else:
    def datetime_isoformat(datetime, timespec='microseconds'):
        assert isinstance(datetime, datetime_module.datetime)
        if timespec != 'microseconds':
            raise NotImplementedError
        time = time_isoformat(
            datetime.time(),
            timespec='microseconds'
        )
        return datetime.isoformat(timespec='seconds')[:10] + 'T' + time


# Generated at 2022-06-12 19:47:09.698583
# Unit test for function timedelta_format
def test_timedelta_format():
    time = datetime_module.time(1, 2, 3, 4 * 1000 * 1000)
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == (
        '00:00:01.000000')
    assert timedelta_format(datetime_module.timedelta(seconds=10)) == (
        '00:00:10.000000')
    assert timedelta_format(datetime_module.timedelta(seconds=60)) == (
        '00:01:00.000000')
    assert timedelta_format(datetime_module.timedelta(seconds=3660)) == (
        '01:01:00.000000')
    assert timedelta_format(datetime_module.timedelta(seconds=24 * 3600)) == (
        '24:00:00.000000')

# Generated at 2022-06-12 19:47:18.371344
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('0:00:01.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:01:00.000000') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('1:01:00.000000') == datetime_module.timedelta(
        minutes=61,
        hours=1
    )

    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(microseconds=1)

# Generated at 2022-06-12 19:47:26.307941
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1
    )
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(
        minutes=1
    )
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        hours=1
    )
    assert timedelta_parse('23:59:59.999999') == datetime_module.timedelta(
        hours=24 - 1,
        seconds=60 - 1,
        microseconds=1000000 - 1
    )
    assert timedelta_parse('01:23:45.678987')

# Generated at 2022-06-12 19:47:28.337540
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=10, minutes=17, seconds=38, microseconds=123456
    )) == '10:17:38.123456'



# Generated at 2022-06-12 19:47:41.214220
# Unit test for function timedelta_format
def test_timedelta_format():
    test_cases = [
        datetime_module.timedelta(0),
        datetime_module.timedelta(1),
        datetime_module.timedelta(days=1),
        datetime_module.timedelta(days=1, microseconds=1),
        datetime_module.timedelta(microseconds=1),
    ]
    for test_case in test_cases:
        assert timedelta_parse(timedelta_format(test_case)) == test_case

test_timedelta_format()



# Generated at 2022-06-12 19:47:43.682088
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=2.5)) == \
                                                              '00:00:02.500000'



# Generated at 2022-06-12 19:47:46.565962
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(minutes=1,
                                                      seconds=1,
                                                      microseconds=1))=='00:01:01.000001'



# Generated at 2022-06-12 19:47:50.673177
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=3,
                                          minutes=21,
                                          seconds=53,
                                          microseconds=340000)
    assert timedelta_format(timedelta) == '03:21:53.340000'

test_timedelta_format()



# Generated at 2022-06-12 19:48:01.282253
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456
    )

    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0)

    assert timedelta_parse('1:3:0.0') == datetime_module.timedelta(
        hours=1, minutes=3
    )

    assert timedelta_parse('1:45:0.0') == datetime_module.timedelta(
        hours=1, minutes=45
    )

    assert timedelta_parse('2:0:0.0') == datetime_module.timedelta(
        hours=2
    )


# Generated at 2022-06-12 19:48:05.740924
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=1, minutes=18,
                                          seconds=45, microseconds=123456)
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta
    timedelta = datetime_module.timedelta(seconds=70)
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta



# Generated at 2022-06-12 19:48:11.316863
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from .testing import assert_equal
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(0, 1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(0, 60)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(1)
    assert timedelta_parse('01:00:00.000001') == datetime_module.timedelta(1, 0, 1)

# Generated at 2022-06-12 19:48:13.848564
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('01:02:03.456789')) == \
                           '01:02:03.456789'

# Generated at 2022-06-12 19:48:17.233457
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=10, minutes=11,
                                          seconds=12, microseconds=13)
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:48:26.526863
# Unit test for function timedelta_format
def test_timedelta_format():
    def test_case(td, s):
        assert timedelta_format(td) == s

    test_case(datetime_module.timedelta(hours=3, minutes=5, seconds=7,
                                        microseconds=123456),
              '03:05:07.123456')
    test_case(datetime_module.timedelta(hours=23, minutes=10, seconds=12,
                                        microseconds=678),
              '23:10:12.000678')
    test_case(datetime_module.timedelta(days=3, seconds=3, microseconds=456789),
              '72:00:03.456789')
    test_case(datetime_module.timedelta(days=3, seconds=3),
              '72:00:03.000000')
    test_case

# Generated at 2022-06-12 19:48:49.607579
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert (
        timedelta_format(timedelta_parse('01:02:03.004000')) ==
        '01:02:03.004000'
    )
    assert (
        timedelta_format(timedelta_parse('01:02:03.004000')) ==
        '01:02:03.004000'
    )

# Generated at 2022-06-12 19:48:57.619910
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('0:00:00:00')) == '00:00:00.000000'
    assert timedelta_format(timedelta_parse('0:00:00:01')) == '00:00:00.000001'
    assert timedelta_format(timedelta_parse('0:00:00:12')) == '00:00:00.000012'
    assert timedelta_format(timedelta_parse('0:00:00:123')) == '00:00:00.000123'
    assert timedelta_format(timedelta_parse('0:00:00:1234')) == '00:00:00.001234'

# Generated at 2022-06-12 19:49:04.309682
# Unit test for function timedelta_format
def test_timedelta_format():
    my_timedelta = datetime_module.timedelta(
        hours=4, minutes=0, seconds=45, microseconds=600000,
    )
    formatted_my_timedelta = timedelta_format(my_timedelta)
    assert formatted_my_timedelta == '04:00:45.600000'
    assert timedelta_parse(formatted_my_timedelta) == my_timedelta

# Generated at 2022-06-12 19:49:06.258319
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.320000') == datetime_module.timedelta(
        microseconds=320000)

# Generated at 2022-06-12 19:49:12.746132
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:01:02.003004') == \
                          datetime_module.timedelta(seconds=62,
                                                    microseconds=3004)

    assert timedelta_parse('01:02:03.004005') == \
                          datetime_module.timedelta(hours=1, minutes=2,
                                                    seconds=3, microseconds=4005)

    assert timedelta_parse('01:02:03') == \
                          datetime_module.timedelta(hours=1, minutes=2,
                                                    seconds=3)



# Generated at 2022-06-12 19:49:21.286859
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )) == '01:02:03.000004'
    assert timedelta_format(
        datetime_module.timedelta(hours=12345678, minutes=9, microseconds=654321)
    ) == '12345678:09:00.654321'



# Generated at 2022-06-12 19:49:25.360476
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=123456)
    assert timedelta_format(timedelta) == '01:02:03.123456'



# Generated at 2022-06-12 19:49:33.266944
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('50:10:12.123456') == datetime_module.timedelta(
        days=1, hours=50, minutes=10, seconds=12, microseconds=123456
    )
    assert timedelta_parse('-31:07:00.490000') == datetime_module.timedelta(
        days=-1, hours=-31, minutes=-7, seconds=0, microseconds=-490000
    )
    assert timedelta_parse('12:34:56.789012') == datetime_module.timedelta(
        hours=12, minutes=34, seconds=56, microseconds=789012
    )

# Generated at 2022-06-12 19:49:43.314690
# Unit test for function timedelta_format
def test_timedelta_format():
    import math
    import random
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=10)) == '00:00:00.000010'

# Generated at 2022-06-12 19:49:54.332464
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=2)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=2)) == '02:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1000)) == '1000:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=2, microseconds=999)) == '00:02:00.009999'
    assert timedelta_format(datetime_module.timedelta(seconds=2)) == '00:00:02.000000'
    assert timedelta_format(datetime_module.timedelta(milliseconds=2)) == '00:00:00.002000'
    assert timed

# Generated at 2022-06-12 19:50:45.597958
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta, string in (
        (datetime_module.timedelta(), '00:00:00.000000'),
        (datetime_module.timedelta(seconds=1), '00:00:01.000000'),
        (datetime_module.timedelta(seconds=3600+60+1, microseconds=1),
                                                     '01:01:01.000001'),
    ):
        assert timedelta_format(timedelta) == string



# Generated at 2022-06-12 19:50:52.249132
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1,
                                                                      minutes=2,
                                                                      seconds=3,
                                                                      microseconds=4))) == datetime_module.timedelta(hours=1,
                                                                                                                     minutes=2,
                                                                                                                     seconds=3,
                                                                                                                     microseconds=4)

# Generated at 2022-06-12 19:50:56.351404
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(10))) == \
           datetime_module.timedelta(10)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(0, 1))) == \
           datetime_module.timedelta(0, 1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(0, 0, 5))) == \
           datetime_module.timedelta(0, 0, 5)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(0, 0, 0, 6))) == \
           datetime_module.timedelta(0, 0, 0, 6)

# Generated at 2022-06-12 19:51:04.349976
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=0, minutes=0,
                                                      seconds=0,
                                                      microseconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=40000)) == '01:02:03.040000'
    assert timedelta_format(datetime_module.timedelta(hours=12, minutes=13,
                                                      seconds=14,
                                                      microseconds=150000)) == '12:13:14.150000'


# Generated at 2022-06-12 19:51:13.739995
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(microseconds=10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(microseconds=100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(microseconds=1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(microseconds=10000)

# Generated at 2022-06-12 19:51:18.391597
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
          '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=59)) == \
          '00:00:59.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=60)) == \
          '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=61)) == \
          '00:01:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=3599)) == \
          '00:59:59.000000'

# Generated at 2022-06-12 19:51:28.365229
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == \
           '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=60)) == \
           '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=123456)) == \
           '34:17:36.000000'



# Generated at 2022-06-12 19:51:34.645778
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:1:1.1') == datetime_module.timedelta(
        hours=1,
        minutes=1,
        seconds=1,
        microseconds=100000
    )
    assert timedelta_parse('1:1:1.000001') == datetime_module.timedelta(
        hours=1,
        minutes=1,
        seconds=1,
        microseconds=1
    )



# Generated at 2022-06-12 19:51:38.053176
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=3, minutes=7, seconds=22,
                                          microseconds=123456)
    assert timedelta_format(timedelta) == \
           '03:07:22.123456'



# Generated at 2022-06-12 19:51:44.494939
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:23:45.123456') == (
        datetime_module.timedelta(hours=1, minutes=23, seconds=45,
                                  microseconds=123456)
    )

    assert timedelta_parse('1:23:45.123') == (
        datetime_module.timedelta(hours=1, minutes=23, seconds=45,
                                  microseconds=123000)
    )

    assert timedelta_parse('1:23:45') == (
        datetime_module.timedelta(hours=1, minutes=23, seconds=45)
    )

    assert timedelta_parse('1:23') == (
        datetime_module.timedelta(hours=1, minutes=23)
    )


# Generated at 2022-06-12 19:53:25.454175
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(
        0
    )
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1
    )


# Generated at 2022-06-12 19:53:29.273516
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('02:00:00.002000') == datetime_module.timedelta(
        hours=2, minutes=0, seconds=0, microseconds=2000
    )
    assert timedelta_parse('02:00:00.002000') == datetime_module.timedelta(
        minutes=120, seconds=0, microseconds=2000
    )
    assert timedelta_parse('02:00:00.002000') == datetime_module.timedelta(
        seconds=7200, microseconds=2000
    )
    assert timedelta_parse('02:00:00.002000') == datetime_module.timedelta(
        microseconds=72000002000
    )


# Generated at 2022-06-12 19:53:36.622089
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from .fake_time import fake_time

    with fake_time() as time:
        s = timedelta_format(time.timezone)
        assert timedelta_parse(s) == time.timezone
        s = timedelta_format(time.timedelta)
        assert timedelta_parse(s) == time.timedelta
        s = timedelta_format(datetime_module.timedelta())
        assert timedelta_parse(s) == datetime_module.timedelta()

# Generated at 2022-06-12 19:53:46.646793
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1, microseconds=1)) == '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=60)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=60, microseconds=1)) == '00:01:00.000001'
    assert timedelta_format(datetime_module.timedelta(minutes=1, seconds=1)) == '00:01:01.000000'

# Generated at 2022-06-12 19:53:51.979855
# Unit test for function timedelta_format
def test_timedelta_format():
    import datetime
    assert timedelta_format(datetime.timedelta(days=2, hours=3, minutes=4,
                                               seconds=5, microseconds=6)) == \
                                               '51:04:05.000006'



# Generated at 2022-06-12 19:53:58.081330
# Unit test for function timedelta_format
def test_timedelta_format():
    cases = (
        datetime_module.timedelta(seconds=1),
        datetime_module.timedelta(seconds=10, microseconds=1234),
        datetime_module.timedelta(seconds=100, microseconds=123456),
        datetime_module.timedelta(seconds=1000, microseconds=1234567),
        datetime_module.timedelta(days=1),
        datetime_module.timedelta(days=2),
        datetime_module.timedelta(days=3),
    )
    for timedelta in cases:
        assert timedelta == timedelta_parse(timedelta_format(timedelta))

# Generated at 2022-06-12 19:54:05.587812
# Unit test for function timedelta_format
def test_timedelta_format():
    d = datetime_module.timedelta(days=4, hours=20, minutes=35, seconds=1)
    assert timedelta_format(d) == '20:35:01.000000'

    assert timedelta_format(datetime_module.timedelta(hours=20, seconds=1)) == \
        '20:00:01.000000'

    assert timedelta_format(datetime_module.timedelta(minutes=1, seconds=1)) == \
        '00:01:01.000000'



# Generated at 2022-06-12 19:54:13.499923
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('0:00:00.000000')) == \
                                                 '00:00:00.000000'
    assert timedelta_format(timedelta_parse('12:34:56.000000')) == \
                                                 '12:34:56.000000'
    assert timedelta_format(timedelta_parse('.123456')) == '00:00:00.123456'
    assert timedelta_format(timedelta_parse('123456')) == '00:02:03.456000'
test_timedelta_parse()

# Generated at 2022-06-12 19:54:20.874176
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=123456)) == '00:00:12.345600'
    assert timedelta_format(datetime_module.timedelta(seconds=54321)) == '00:00:54.321000'
    assert timedelta_format(datetime_module.timedelta(seconds=123456,
                                                      microseconds=532453)) ==\
                                                      '00:00:12.345653'

# Generated at 2022-06-12 19:54:30.289432
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
           '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
           '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(days=1)) == \
           '24:00:00.000000'