

# Generated at 2022-06-12 19:46:14.219421
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(
            hours=1,
            minutes=2,
            seconds=3,
            microseconds=123456
        )
    ) == '01:02:03.123456'



# Generated at 2022-06-12 19:46:17.475757
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('01:23:45.678901') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=45, microseconds=678901
    )

# Generated at 2022-06-12 19:46:21.677082
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:02:03.123123') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=123123)



# Generated at 2022-06-12 19:46:27.723678
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    ))) == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=123456)

if sys.version_info[:2] >= (3, 5):
    def has_origin(timedelta):
        return timedelta.origin is not None
else:
    def has_origin(timedelta):
        return False

# Generated at 2022-06-12 19:46:30.158836
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('14:45:23:456789') == datetime_module.timedelta(
        hours=14, minutes=45, seconds=23, microseconds=456789
    )


# Generated at 2022-06-12 19:46:36.934600
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(days=100, hours=12, minutes=34,
                                  seconds=56, microseconds=789)
    )) == datetime_module.timedelta(days=100, hours=12, minutes=34,
                                    seconds=56, microseconds=789)
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(minutes=34, seconds=56, microseconds=789)
    )) == datetime_module.timedelta(minutes=34, seconds=56,
                                    microseconds=789)
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(seconds=56, microseconds=789)
    )) == datetime

# Generated at 2022-06-12 19:46:45.338827
# Unit test for function timedelta_parse
def test_timedelta_parse():
    def run(s):
        return (timedelta_parse(s), timedelta_format(timedelta_parse(s)))
    assert run('1:2:3.4') == (datetime_module.timedelta(hours=1, minutes=2,
                                                        seconds=3,
                                                        microseconds=400000),
                              '01:02:03.004000')
    assert run('2:7:38.0') == (datetime_module.timedelta(hours=2, minutes=7,
                                                        seconds=38),
                               '02:07:38.000000')

# Generated at 2022-06-12 19:46:57.180159
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.123000') == \
           datetime_module.timedelta(seconds=0, microseconds=123000)
    assert timedelta_parse('0:0:1.123000') == \
           datetime_module.timedelta(seconds=1, microseconds=123000)
    assert timedelta_parse('0:1:1.123000') == \
           datetime_module.timedelta(seconds=61, microseconds=123000)
    assert timedelta_parse('1:1:1.123000') == \
           datetime_module.timedelta(hours=1, seconds=61, microseconds=123000)

# Generated at 2022-06-12 19:47:08.466761
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(0, 0, 10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(0, 0, 100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(0, 0, 1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(0, 0, 10000)
    assert timedelta_parse

# Generated at 2022-06-12 19:47:15.493342
# Unit test for function timedelta_format
def test_timedelta_format():
    td = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                   microseconds=456789)
    formatted = timedelta_format(td)
    parsed = timedelta_parse(formatted)
    assert parsed == td


if PY3:
    from functools import singledispatch
else:
    class singledispatch(object):
        """
        This is an implementation of a single-dispatch generic function decorator,
        as described in PEP 443.
        """
        # TODO: Implement this on Py2 as well.



# Generated at 2022-06-12 19:47:26.773644
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:00:00.002000') == datetime_module.timedelta(hours=1, seconds=2)



# Generated at 2022-06-12 19:47:32.877141
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:23:45.678901') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=45, microseconds=678901,
    )
    assert timedelta_parse('01:23:45.678901') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=45, milliseconds=678,
    )
    assert timedelta_parse('01:23:45.678901') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=45, microseconds=678901,
    )

    with pytest.raises(ValueError):
        timedelta_parse('')
    with pytest.raises(ValueError):
        timedelta_parse('01:23:45')


# Generated at 2022-06-12 19:47:35.793177
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('12:34:56.7890') == \
           datetime_module.timedelta(hours=12, minutes=34, seconds=56,
                                     microseconds=789000)

# Generated at 2022-06-12 19:47:46.521196
# Unit test for function timedelta_parse
def test_timedelta_parse():
    # print(timedelta_parse('0:0:0.0'))
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0, 0)
    assert timedelta_parse('1:2:3.4') == datetime_module.timedelta(
        1, 2 * 3600 + 3 * 60 + 4 / 1e6)
    assert timedelta_parse('1:2:3.456789') == datetime_module.timedelta(
        1, 2 * 3600 + 3 * 60 + 4 / 1e6 + 56789 / 1e9)

    assert timedelta_parse('0:0:0') == datetime_module.timedelta(0, 0)
    assert timedelta_parse('1:2:3') == datetime_module.timed

# Generated at 2022-06-12 19:47:54.818641
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=23, minutes=59, seconds=59, microseconds=999999
    )) == '23:59:59.999999'
    if sys.version_info[:2] >= (3, 6):
        assert timedelta_format(datetime_module.timedelta(
            hours=23, minutes=59, seconds=59, microseconds=999990
        )) == '23:59:59.999990'

# Generated at 2022-06-12 19:47:57.633173
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('5:5:5.000000')) == '05:05:05.000000'

# Generated at 2022-06-12 19:48:06.153606
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0.000001') == datetime_module.timedelta(0, 0,
                                                                        1)
    assert timedelta_parse('0:0:0.000010') == datetime_module.timedelta(0, 0,
                                                                        10)
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(0, 1)
    assert timedelta_parse('0:1:0.000000') == datetime_module.timedelta(0, 60)
    assert timedelta_parse('1:0:0.000000') == datetime_module.timedelta(1)

# Generated at 2022-06-12 19:48:11.366252
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(weeks=0, days=0,
               hours=1, minutes=2, seconds=3, microseconds=123456)) == \
               '01:02:03.123456'
    assert timedelta_format(datetime_module.timedelta(weeks=0, days=0,
               hours=1, minutes=2, seconds=3, microseconds=0)) == \
               '01:02:03.000000'
    assert timedelta_format(datetime_module.timedelta(weeks=0, days=0,
               hours=1, minutes=2, seconds=3, microseconds=123)) == \
               '01:02:03.000123'


# Generated at 2022-06-12 19:48:15.211012
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(seconds=1,
                                                   milliseconds=1,
                                                   microseconds=1))
    ) == datetime_module.timedelta(seconds=1, milliseconds=1,
                                   microseconds=1)



# Generated at 2022-06-12 19:48:25.377770
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == \
                                             datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:00.000010') == \
                                             datetime_module.timedelta(0, 0, 10)
    assert timedelta_parse('00:00:00.000099') == \
                                             datetime_module.timedelta(0, 0, 99)
    assert timedelta_parse('00:00:00.000100') == \
                                            datetime_module.timedelta(0, 0, 100)

# Generated at 2022-06-12 19:48:49.794375
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=1, minutes=1, seconds=1,
                                          microseconds=1)
    s = timedelta_format(timedelta)
    assert s == '01:01:01.000001'
    assert timedelta_parse(s) == timedelta
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta


if 'buffer' in dir(__builtins__):
    buffer_type = buffer
else:
    buffer_type = memoryview

# Generated at 2022-06-12 19:48:52.919999
# Unit test for function timedelta_parse
def test_timedelta_parse():
    s = '3:02:01.123098'
    d = timedelta_parse(s)
    assert d == datetime_module.timedelta(hours=3, minutes=2, seconds=1,
                                          microseconds=123098)

# Generated at 2022-06-12 19:48:54.866751
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=42, hours=1,
                                                      minutes=42, seconds=42,
                                                      microseconds=123456)) == \
           '1:42:42.123456'


# Generated at 2022-06-12 19:48:57.118078
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=450
    )) == '1:02:03.000450'


# Generated at 2022-06-12 19:49:06.841603
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                                                                 '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
                                                                   '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                                   '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
                                                                        '00:00:00.000001'

# Generated at 2022-06-12 19:49:14.579595
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_format(datetime_module.timedelta(seconds=30)) == '00:00:30.000000'
    assert timedelta_parse('00:00:30.000000') == datetime_module.timedelta(seconds=30)
    assert timedelta_format(datetime_module.timedelta(seconds=0,
                                                      microseconds=12345)) == '00:00:00.012345'

# Generated at 2022-06-12 19:49:27.580266
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta()
    assert timedelta_parse('0:0:0.5') == datetime_module.timedelta(microseconds=500000)
    assert timedelta_parse('0:0:1') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:1:1') == datetime_module.timedelta(minutes=1, seconds=1)
    assert timedelta_parse('1:1:1') == datetime_module.timedelta(hours=1, minutes=1, seconds=1)
    assert timedelta_parse('0:0:0.000') == datetime_module.timedelta()
    assert timedelta_parse('0:0:0.000000') == datetime

# Generated at 2022-06-12 19:49:34.898334
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('1:2:3.456')) == '01:02:03.456000'
    assert timedelta_format(timedelta_parse('100:10:20.34')) == '100:10:20.340000'
    assert timedelta_format(timedelta_parse('0:0:0.000000')) == '00:00:00.000000'
    assert timedelta_format(timedelta_parse('0:0:0.012345')) == '00:00:00.012345'
    assert timedelta_format(timedelta_parse('1:2:3.123456')) == '01:02:03.123456'



# Generated at 2022-06-12 19:49:44.795942
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=2)) == \
                                                      '00:00:01.000002'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1)) == '24:00:00.000000'



# Generated at 2022-06-12 19:49:54.878868
# Unit test for function timedelta_format
def test_timedelta_format():
    def assert_timedelta_format(timedelta, expected):
        assert timedelta_format(timedelta) == expected
    
    assert_timedelta_format(datetime_module.timedelta(), '00:00:00.000000')
    assert_timedelta_format(datetime_module.timedelta(seconds=5), '00:00:05.000000')
    assert_timedelta_format(datetime_module.timedelta(microseconds=5), '00:00:00.000005')
    assert_timedelta_format(datetime_module.timedelta(microseconds=5000), '00:00:00.005000')
    assert_timedelta_format(datetime_module.timedelta(seconds=65, microseconds=5000), '00:01:05.005000')


# Generated at 2022-06-12 19:50:45.266058
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('10:20:30.123456') == datetime_module.timedelta(
        hours=10, minutes=20, seconds=30, microseconds=123456
    )
    assert timedelta_parse('10:20:30') == datetime_module.timedelta(
        hours=10, minutes=20, seconds=30
    )
    assert timedelta_parse('10:20:30.001') == datetime_module.timedelta(
        hours=10, minutes=20, seconds=30, microseconds=1000
    )



# Generated at 2022-06-12 19:50:47.366999
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=1, minutes=2,
                                          seconds=3, microseconds=4)
    assert timedelta_format(timedelta) == '01:02:03.000004'



# Generated at 2022-06-12 19:50:51.466720
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=13,
                                          minutes=12,
                                          seconds=34,
                                          microseconds=456000)
    assert timedelta == timedelta_parse(timedelta_format(timedelta))

# Generated at 2022-06-12 19:50:57.214045
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(milliseconds=1)) == '00:00:00.001000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'


# Generated at 2022-06-12 19:51:02.268665
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for timedelta in (
        datetime_module.timedelta(hours=5, minutes=4, seconds=3, microseconds=2),
        datetime_module.timedelta(days=5, minutes=4, seconds=3,
                                  microseconds=2),
        datetime_module.timedelta(days=55, minutes=4, seconds=3,
                                  microseconds=2),
        datetime_module.timedelta(days=555, minutes=4, seconds=3,
                                  microseconds=2),
    ):
        assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:51:12.577376
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1)
    assert timedelta_parse('00:00:01.000002') == datetime_module.timedelta(
        seconds=1, microseconds=2)
    assert timedelta_parse('01:02:03.000004') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4)
    assert timedelta_parse('01:02:03.000004') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4)



# Generated at 2022-06-12 19:51:17.584703
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.000000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=0,
    )
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(
        hours=0, minutes=0, seconds=1, microseconds=0,
    )
    assert timedelta_parse('0:1:0.000000') == datetime_module.timedelta(
        hours=0, minutes=1, seconds=0, microseconds=0,
    )
    assert timedelta_parse('1:0:0.000000') == datetime_module.timedelta(
        hours=1, minutes=0, seconds=0, microseconds=0,
    )

# Generated at 2022-06-12 19:51:22.181453
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(milliseconds=1)) == '00:00:00.001000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1)) == '24:00:00.000000'

# Generated at 2022-06-12 19:51:31.675249
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta()
    assert timedelta_parse('0:0:0.123456') == datetime_module.timedelta(
        microseconds=123456
    )
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(
        seconds=1
    )
    assert timedelta_parse('0:1:1.000000') == datetime_module.timedelta(
        minutes=1, seconds=1
    )
    assert timedelta_parse('1:1:1.000000') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1
    )

# Generated at 2022-06-12 19:51:37.401918
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == \
           '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=40)) == \
           '00:40:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'



# Generated at 2022-06-12 19:53:23.535979
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=4)
    s = timedelta_format(timedelta)
    assert timedelta == timedelta_parse(s)



# Generated at 2022-06-12 19:53:32.780532
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=-1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=-1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'

# Generated at 2022-06-12 19:53:38.963099
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=0,
                                                      microseconds=42)) == \
           '00:00:00.000042'
    assert timedelta_format(datetime_module.timedelta(days=3, seconds=42,
                                                      microseconds=4)) == \
           '72:00:00.000004'



# Generated at 2022-06-12 19:53:41.391848
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('0:00:00.235600')
    assert timedelta.seconds == 0
    assert timedelta.microseconds == 235600



# Generated at 2022-06-12 19:53:52.950209
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=0, minutes=0, seconds=0,
                                  microseconds=0)
    ) == '00:00:00.000000'
    assert timedelta_format(
        datetime_module.timedelta(hours=0, minutes=0, seconds=1,
                                  microseconds=0)
    ) == '00:00:01.000000'
    assert timedelta_format(
        datetime_module.timedelta(hours=0, minutes=1, seconds=0,
                                  microseconds=0)
    ) == '00:01:00.000000'

# Generated at 2022-06-12 19:53:59.316260
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta()
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(
        seconds=1,
    )
    assert timedelta_parse('0:1:1.000000') == datetime_module.timedelta(
        minutes=1, seconds=1,
    )
    assert timedelta_parse('1:1:1.000000') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1,
    )
    assert timedelta_parse('1:1:1.000001') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=1,
    )

# Generated at 2022-06-12 19:54:04.512830
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('0:0:0.1') == datetime_module.timedelta(microseconds=100000)
    assert timedelta_parse('00:00:00.999999') == datetime_module.timedelta(microseconds=999999)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('00:00:01.000001') == datetime_

# Generated at 2022-06-12 19:54:14.419741
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('03:04:05.000001')) == \
            '03:04:05.000001'
    assert timedelta_format(timedelta_parse('-1:04:05.000001')) == \
            '22:55:55.999999'
    assert timedelta_format(timedelta_parse('1:04:05.000001')) == \
            '01:04:05.000001'
    assert timedelta_format(timedelta_parse('-0:04:05.000001')) == \
            '23:55:55.999999'
    assert timedelta_format(timedelta_parse('0:04:05.000001')) == \
            '00:04:05.000001'

# Generated at 2022-06-12 19:54:21.559739
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                             '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      milliseconds=345)) == \
                             '01:00:00.000345'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      microseconds=345)) == \
                             '01:00:00.000345'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
                             '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                             '00:00:01.000000'
    assert timedelta

# Generated at 2022-06-12 19:54:31.759200
# Unit test for function timedelta_format