

# Generated at 2022-06-12 19:46:14.631298
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(
        timedelta_parse('01:02:03.123456')
    ) == '01:02:03.123456'
    assert timedelta_format(
        timedelta_parse('10:20:30.123456')
    ) == '10:20:30.123456'

# Generated at 2022-06-12 19:46:20.969581
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('0') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('0.0') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('0.00') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('0.000') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('0.0000') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('0.00000') == datetime_module.timedelta(seconds=0)

# Generated at 2022-06-12 19:46:28.367810
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(
        hours=1)
    assert timedelta_parse('0:59:59.999999') == datetime_module.timedelta(
        minutes=59, seconds=59, microseconds=999999)
    assert timedelta_parse('0:00:01.000000') == datetime_module.timedelta(
        seconds=1)
    assert timedelta_parse('0:00:00.100000') == datetime_module.timedelta(
        microseconds=100000)



# Generated at 2022-06-12 19:46:37.554615
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:2.000000') == datetime_module.timedelta(seconds=2)
    assert timedelta_parse('0:0:2.123456') == datetime_module.timedelta(seconds=2, microseconds=123456)
    assert timedelta_parse('0:3:2.000000') == datetime_module.timedelta(minutes=3, seconds=2)
    assert timedelta_parse('0:3:2.123456') == datetime_module.timedelta(minutes=3, seconds=2, microseconds=123456)

# Generated at 2022-06-12 19:46:45.782021
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=12345
    ))) == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=12345
    )
    with pytest.raises(ValueError):
        timedelta_parse('1:1:10:10')
    with pytest.raises(ValueError):
        timedelta_parse('1:1:10.10')
    with pytest.raises(ValueError):
        timedelta_parse('1:1:10.10-')
    with pytest.raises(ValueError):
        timedelta_parse('1:1:10.10+')

# Generated at 2022-06-12 19:46:57.637645
# Unit test for function timedelta_parse
def test_timedelta_parse():
    def assert_timedelta_parse(timedelta, string):
        assert timedelta_parse(string) == timedelta
    assert_timedelta_parse(datetime_module.timedelta(seconds=1), '00:00:01')
    assert_timedelta_parse(datetime_module.timedelta(seconds=1), '0:0:1')
    assert_timedelta_parse(datetime_module.timedelta(minutes=1), '00:01:00')
    assert_timedelta_parse(datetime_module.timedelta(hours=1), '1:00:00')
    assert_timedelta_parse(datetime_module.timedelta(microseconds=1), '00:00:00.000001')

# Generated at 2022-06-12 19:47:08.644030
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        seconds=0.1, microseconds=100
    ))) == datetime_module.timedelta(seconds=0.1, microseconds=100)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        seconds=1, microseconds=100
    ))) == datetime_module.timedelta(seconds=1, microseconds=100)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        seconds=10, microseconds=100
    ))) == datetime_module.timedelta(seconds=10, microseconds=100)

# Generated at 2022-06-12 19:47:17.691149
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('8:47:15.000000') == \
                                 datetime_module.timedelta(hours=8, minutes=47,
                                                           seconds=15)
    assert timedelta_parse('8:47:15.000001') == \
                                 datetime_module.timedelta(hours=8, minutes=47,
                                                           seconds=15,
                                                           microseconds=1)
    assert timedelta_parse('8:47:15.123456') == \
                                 datetime_module.timedelta(hours=8, minutes=47,
                                                           seconds=15,
                                                           microseconds=123456)


try:
    from collections import UserList
except ImportError:
    from UserList import UserList

# Generated at 2022-06-12 19:47:20.917417
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('03:59:12.346766') == datetime_module.timedelta(
        hours=3, minutes=59, seconds=12, microseconds=346766
    )



# Generated at 2022-06-12 19:47:28.123733
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('00:01:02.123456')) == \
                                                        '00:01:02.123456'
    assert timedelta_format(timedelta_parse('1:02:03.123456')) == \
                                                        '01:02:03.123456'
    assert timedelta_format(timedelta_parse('12:3:2.123456')) == \
                                                        '12:03:02.123456'
    assert timedelta_format(timedelta_parse('12:03:2.123456')) == \
                                                        '12:03:02.123456'
    assert timedelta_format(timedelta_parse('12:03:02.123456')) == \
                                                        '12:03:02.123456'

# Generated at 2022-06-12 19:47:41.426355
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:47:44.631424
# Unit test for function timedelta_format
def test_timedelta_format():
    dt = datetime_module.timedelta(days=1, hours=2, minutes=3, seconds=4,
                                   microseconds=5)
    assert timedelta_format(dt) == '26:03:04:000005'

# Generated at 2022-06-12 19:47:52.192669
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                 minutes=2,
                                                 seconds=3,
                                                 microseconds=456789)) == \
                                                 '01:02:03.456789'
    assert timedelta_format(datetime_module.timedelta(0, 60 * 60 * 1000,
                                                 123456)) == \
                                                 '1000:00:00.123456'
    assert timedelta_format(datetime_module.timedelta(0, 1,
                                                 123456789)) == \
                                                 '00:00:00.123456789'



# Generated at 2022-06-12 19:48:02.237310
# Unit test for function timedelta_parse

# Generated at 2022-06-12 19:48:05.709313
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        minutes=1, seconds=2, microseconds=3
    ))) == datetime_module.timedelta(
        minutes=1, seconds=2, microseconds=3
    )

# Generated at 2022-06-12 19:48:08.147397
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=400000)) == \
           '01:02:03.400000'
    
    

# Generated at 2022-06-12 19:48:12.773985
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(hours=23, minutes=59,
                                                   seconds=59,
                                                   microseconds=875555))
    ) == datetime_module.timedelta(hours=23, minutes=59,
                                   seconds=59,
                                   microseconds=875555)


if sys.version_info[0] >= 3:
    def force_unicode(s): return s
else:
    import types
    def force_unicode(s):
        if isinstance(s, unicode):
            return s
        try:
            return unicode(s)
        except UnicodeDecodeError:
            if isinstance(s, Exception):
                return ' '.join([force_unicode(arg) for arg in s])

# Generated at 2022-06-12 19:48:14.733908
# Unit test for function timedelta_format
def test_timedelta_format():
    from . import test_my_timer
    assert test_my_timer.test_timedelta_format(timedelta_format)



# Generated at 2022-06-12 19:48:20.651297
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=10)) == '00:00:10'
    assert timedelta_format(datetime_module.timedelta(seconds=11.75)) == '00:00:11.750000'
    assert timedelta_parse('00:00:11.750000') == datetime_module.timedelta(seconds=11.75)

# Generated at 2022-06-12 19:48:24.153274
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=456789)
    assert timedelta_format(timedelta) == '01:02:03.456789'



# Generated at 2022-06-12 19:48:46.008159
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('01:02:03.000000') == datetime_module.timedelta(
        seconds=1*60*60 + 2*60 + 3,
    )
    assert timedelta_parse('00:02:03.000000') == datetime_module.timedelta(
        seconds=2*60 + 3,
    )
    assert timedelta_parse('00:00:03.000000') == datetime_module.timedelta(
        seconds=3,
    )
    assert timedelta_parse('00:00:03.040000') == datetime_module.timedelta(
        seconds=3,
        microseconds=40000,
    )

# Generated at 2022-06-12 19:48:55.584631
# Unit test for function timedelta_parse
def test_timedelta_parse():
    td = timedelta_parse('12:34:56.123456')
    assert td.total_seconds() == 45296.123456
    td = timedelta_parse('12:34:56.654321')
    assert td.total_seconds() == 45296.654321


_windows_requires_backslash = (
    sys.version_info[0] == 2 and
    sys.version_info[1] < 4
)

if PY2:

    def make_path_backslash_escaped(path):
        '''
        Convert a path from forward slashes to backslashes, with escaping.

        Under Python 2, some versions of `os.path.normpath` would parse mixed
        slashes, which we want to avoid.
        '''

# Generated at 2022-06-12 19:48:59.896810
# Unit test for function timedelta_parse
def test_timedelta_parse():
    expected = datetime_module.timedelta(hours=5, minutes=10, seconds=7,
                                         microseconds=123456)
    got = timedelta_parse('5:10:7.123456')
    assert got == expected
    assert got != expected + datetime_module.timedelta(days=1)


# Generated at 2022-06-12 19:49:02.605476
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.560800') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=560800)



# Generated at 2022-06-12 19:49:12.042519
# Unit test for function timedelta_parse
def test_timedelta_parse():
    cases = {
        '00:00:00.000000': datetime_module.timedelta(0),
        '00:00:00.000001': datetime_module.timedelta(0, 0, 1),
        '00:00:10.000000': datetime_module.timedelta(0, 10),
        '00:00:10.000001': datetime_module.timedelta(0, 10, 1),
        '01:02:03.000000': datetime_module.timedelta(days=1, seconds=3723),
        '01:02:03.000001': datetime_module.timedelta(days=1, seconds=3723,
                                                     microseconds=1),
    }
    for s, timedelta in cases.items():
        assert timedelta_parse(s) == timed

# Generated at 2022-06-12 19:49:25.141321
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.123456') == \
           datetime_module.timedelta(hours=1, minutes=2,
                                     seconds=3, microseconds=123456)

    assert timedelta_parse('1:2:03.123456') == \
           datetime_module.timedelta(hours=1, minutes=2,
                                     seconds=3, microseconds=123456)

    assert timedelta_parse('1:2:3.123456') == \
           datetime_module.timedelta(hours=1, minutes=2,
                                     seconds=3, microseconds=123456)


# Generated at 2022-06-12 19:49:27.926675
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('12:34:56.123456') == datetime_module.timedelta(
        hours=12, minutes=34, seconds=56, microseconds=123456
    )

# Generated at 2022-06-12 19:49:35.141178
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=456789)) == \
           '01:02:03.456789'
    assert timedelta_format(datetime_module.timedelta(hours=10, minutes=20,
                                                      seconds=30,
                                                      microseconds=456789)) == \
           '10:20:30.456789'


# Generated at 2022-06-12 19:49:41.559702
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3') == datetime_module.timedelta(hours=1,
                                                                 minutes=2,
                                                                 seconds=3)
    assert timedelta_parse('1:2:3.4') == \
        datetime_module.timedelta(seconds=3, milliseconds=4)
    assert timedelta_parse('1:2:3.456789') == \
        datetime_module.timedelta(seconds=3, microseconds=456789)

# Generated at 2022-06-12 19:49:52.866494
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:50:25.043693
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('3:0:0.000000') == datetime_module.timedelta(days=1/8)
    assert timedelta_parse('0:30:0.000000') == datetime_module.timedelta(minutes=30)
    assert timedelta_parse('0:0:30.000000') == datetime_module.timedelta(seconds=30)
    assert timedelta_parse('0:0:0.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('0:0:0.1') == datetime_module.timedelta(microseconds=100000)

# Generated at 2022-06-12 19:50:35.167769
# Unit test for function timedelta_parse
def test_timedelta_parse():
    zero = timedelta_parse(timedelta_format(datetime_module.timedelta()))
    assert zero == datetime_module.timedelta()

    one_microsecond = timedelta_parse(
        timedelta_format(datetime_module.timedelta(microseconds=1))
    )
    assert one_microsecond == datetime_module.timedelta(microseconds=1)

    one_microsecond = timedelta_parse(
        timedelta_format(datetime_module.timedelta(microseconds=1))
    )
    assert one_microsecond == datetime_module.timedelta(microseconds=1)

    one_hour = timedelta_parse(
        timedelta_format(datetime_module.timedelta(hours=1))
    )
    assert one_hour == datetime_module

# Generated at 2022-06-12 19:50:43.884446
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=0, minutes=0, seconds=0,
                                  microseconds=0)
    ) == '00:00:00.000000'

    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=4)
    ) == '01:02:03.000004'

    assert timedelta_format(
        datetime_module.timedelta(hours=10, minutes=20, seconds=30,
                                  microseconds=40)
    ) == '10:20:30.000040'

    assert timedelta_format(
        datetime_module.timedelta(hours=100, minutes=200, seconds=300,
                                  microseconds=400)
    )

# Generated at 2022-06-12 19:50:45.078662
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=4.4)) == \
           '00:00:04.400000'



# Generated at 2022-06-12 19:50:55.837468
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.002550') == datetime_module.timedelta(0, 0, 2550)
    assert timedelta_parse('00:00:00.490000') == datetime_module.timedelta(0, 0, 49000)
    assert timedelta_parse('00:00:00.499999') == datetime_module.timedelta(0, 0, 499999)
    assert timedelta_parse('00:00:00.500000') == datetime_module.timedelta(0, 0, 500000)

# Generated at 2022-06-12 19:51:02.303216
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('.5') == datetime_module.timedelta(seconds=.5)
    assert timedelta_parse(':1.5') == datetime_module.timedelta(
        minutes=1, seconds=.5
    )
    assert timedelta_parse(':01:1.5') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=.5
    )
    assert timedelta_parse(':01:01:1.5') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1.5
    )
    assert timedelta_parse('01:00:01.000001') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=1
    )


#

# Generated at 2022-06-12 19:51:05.386357
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:05.342995') == \
           datetime_module.timedelta(seconds=5, microseconds=342995)

# Generated at 2022-06-12 19:51:11.234814
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == \
           datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(days=1)
    )) == datetime_module.timedelta(days=1)


if PY3:
    def raise_from(exception, *other_exceptions):
        if not other_exceptions:
            raise exception
        else:
            raise exception from other_exceptions[0]
else:
    def raise_from(exception, *other_exceptions):
        # Stupid Python 2.7
        if not other_exceptions:
            raise exception
        else:
            raise other_exceptions[0]



# Generated at 2022-06-12 19:51:14.728681
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import random
    for _ in range(100):
        hours = random.randrange(1000)
        minutes = random.randrange(60)
        seconds = random.randrange(60)
        microseconds = random.randrange(1000000)
        td = datetime_module.timedelta(hours=hours, minutes=minutes,
                                       seconds=seconds,
                                       microseconds=microseconds)
        assert timedelta_parse(timedelta_format(td)) == td



# Generated at 2022-06-12 19:51:18.266658
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=3,
                                                      minutes=14,
                                                      seconds=21)) == '03:14:21.000000'
    assert timedelta_format(datetime_module.timedelta(hours=13,
                                                      minutes=0,
                                                      seconds=21,
                                                      microseconds=99)) == '13:00:21.000099'

# Generated at 2022-06-12 19:52:11.972700
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(minutes=30)) == \
                                                        '00:30:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=30,
                                                      seconds=30)) == \
                                                        '00:30:30.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=30,
                                                      microseconds=30)) == \
                                                        '00:00:30.000030'
    assert timedelta_format(datetime_module.timedelta(hours=30,
                                                      seconds=30,
                                                      microseconds=30)) == \
                                                        '30:00:30.000030'



# Generated at 2022-06-12 19:52:20.884880
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('10') == datetime_module.timedelta(seconds=10)
    assert timedelta_parse('-10') == datetime_module.timedelta(seconds=-10)
    assert timedelta_parse('0:0') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('0:10') == datetime_module.timedelta(seconds=10)
    assert timedelta_parse('0:-10') == datetime_module.timedelta(seconds=-10)
    assert timedelta_parse('10:0') == datetime_module.timedelta(seconds=600)

# Generated at 2022-06-12 19:52:25.840810
# Unit test for function timedelta_parse
def test_timedelta_parse():
    hours = 1
    minutes = 1
    seconds = 1
    microseconds = 1
    s = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        hours, minutes, seconds, microseconds
    )
    parsed_timedelta = timedelta_parse(s)
    assert parsed_timedelta == datetime_module.timedelta(
        hours=hours, minutes=minutes, seconds=seconds,
        microseconds=microseconds
    )
    assert isinstance(parsed_timedelta, datetime_module.timedelta)



# Generated at 2022-06-12 19:52:32.905502
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=15)) == '00:15:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=10)) == '00:00:10.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=10,
                                                      microseconds=149000)) == '00:00:10.149000'



# Generated at 2022-06-12 19:52:37.296182
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.4') == timedelta_parse('1:2:3.000004')
    assert timedelta_parse('1:2:3.4') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )



# Generated at 2022-06-12 19:52:47.115038
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=4,
                                                      microseconds=5)) == \
                                                      '00:00:04.000005'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=999999)) == \
                                                      '00:00:01.999999'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
                                                      '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                                                      '01:00:00.000000'

# Generated at 2022-06-12 19:52:52.089294
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=123)) == \
                                                                '00:00:00.000123'
    assert timedelta_format(datetime_module.timedelta(microseconds=1234)) == \
                                                                '00:00:00.001234'
    assert timedelta_format(datetime_module.timedelta(microseconds=12345)) == \
                                                                '00:00:00.012345'
    assert timedelta_format(datetime_module.timedelta(microseconds=123456)) == \
                                                                '00:00:00.123456'

# Generated at 2022-06-12 19:52:55.358062
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=500)
    )) == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                    microseconds=500)



# Generated at 2022-06-12 19:53:01.167704
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('3:12:56.082270') == \
        datetime_module.timedelta(hours=3, minutes=12, seconds=56,
                                  microseconds=82_270)
    assert timedelta_parse('0:00:00.000000') == \
        datetime_module.timedelta()

# Generated at 2022-06-12 19:53:10.704883
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=10)) == \
           '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=10)) == \
           '10:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=10)) == \
           '00:10:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=10)) == \
           '00:00:10.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=10)) == \
           '00:00:00.000010'

# Generated at 2022-06-12 19:55:04.014665
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1
    )
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(
        minutes=1
    )
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        hours=1
    )
    assert timedelta_parse('00:00:00.100000') == datetime_module.timedelta(
        microseconds=100
    )

# Generated at 2022-06-12 19:55:11.955693
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(
        microseconds=1000
    )
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(
        minutes=1
    )
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        hours=1
    )


# Generated at 2022-06-12 19:55:22.441879
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
           '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
           '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'

# Generated at 2022-06-12 19:55:30.500248
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('05:34:23.004508') == datetime_module.timedelta(
        hours=5, minutes=34, seconds=23, microseconds=4508
    )
    assert timedelta_parse('05:34:23.0045') == datetime_module.timedelta(
        hours=5, minutes=34, seconds=23, microseconds=4500
    )
    assert timedelta_parse('05:34:23.004') == datetime_module.timedelta(
        hours=5, minutes=34, seconds=23, microseconds=4000
    )
    assert timedelta_parse('05:34:23.00') == datetime_module.timedelta(
        hours=5, minutes=34, seconds=23, microseconds=0
    )
    assert timedelta_parse

# Generated at 2022-06-12 19:55:38.682409
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:55:44.908162
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta in [
        datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=4),
        datetime_module.timedelta(hours=0, minutes=0, seconds=0, microseconds=4),
        datetime_module.timedelta(hours=0, minutes=59, seconds=59,
                                  microseconds=999999),
        datetime_module.timedelta(hours=1, minutes=0, seconds=0, microseconds=0),
        datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                                  microseconds=999999),
    ]:
        assert timedelta_format(timedelta) == timedelta_format(timedelta)



# Generated at 2022-06-12 19:55:48.302119
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for timedelta in (datetime_module.timedelta(seconds=123456789),
                      datetime_module.timedelta(seconds=123456789,
                                                microseconds=12345)):
        assert timedelta == timedelta_parse(timedelta_format(timedelta))

# Generated at 2022-06-12 19:55:55.976871
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=1,
        minutes=2,
        seconds=3,
        microseconds=4
    )) == '01:02:03.000004'

    assert timedelta_format(datetime_module.timedelta(
        hours=10,
        minutes=20,
        seconds=30,
        microseconds=40
    )) == '10:20:30.000040'

    assert timedelta_format(datetime_module.timedelta(
        hours=100,
        minutes=200,
        seconds=300,
        microseconds=400
    )) == '100:200:300.000400'

