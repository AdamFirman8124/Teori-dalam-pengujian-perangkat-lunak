

# Generated at 2022-06-12 19:46:12.808785
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == \
           datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:01.000000') == \
           datetime_module.timedelta(0, 1)
    assert timedelta_parse('00:00:01.000001') == \
           datetime_module.timedelta(0, 1, 1)
    assert timedelta_parse('00:01:00.000000') == \
           datetime_module.timedelta(0, 60)
    assert timedelta_parse('01:00:00.000000') == \
           datetime_module.timedelta(1)

# Generated at 2022-06-12 19:46:19.978322
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(milliseconds=1)) == \
           '00:00:00.001000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
           '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
           '01:00:00.000000'

# Generated at 2022-06-12 19:46:21.923824
# Unit test for function timedelta_format
def test_timedelta_format():
    assert (timedelta_format(datetime_module.timedelta(hours=3,
                                                       minutes=2,
                                                       seconds=1,
                                                       microseconds=5123))
            == '03:02:01.005123')

# Generated at 2022-06-12 19:46:27.067498
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('1:2:3.000001')) == '01:02:03.000001'
    assert timedelta_format(timedelta_parse('01:02:03.000001')) == '01:02:03.000001'
    assert timedelta_format(timedelta_parse('0001:0002:0003.000001')) == '01:02:03.000001'

# Generated at 2022-06-12 19:46:30.413064
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=4)
    ) == '01:02:03.000004'



# Generated at 2022-06-12 19:46:39.850504
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('03:04:05.123456') == (
        datetime_module.timedelta(hours=3, minutes=4, seconds=5,
                                  microseconds=123456))
    assert timedelta_parse('03:04:05.123000') == (
        datetime_module.timedelta(hours=3, minutes=4, seconds=5,
                                  microseconds=123000))
    assert timedelta_parse('3:04:05.123000') == (
        datetime_module.timedelta(hours=3, minutes=4, seconds=5,
                                  microseconds=123000))

# Generated at 2022-06-12 19:46:41.744085
# Unit test for function timedelta_format
def test_timedelta_format():
    result = timedelta_format(datetime_module.timedelta(seconds=1))
    assert result == '00:00:01.000000'

# Generated at 2022-06-12 19:46:48.570141
# Unit test for function timedelta_format
def test_timedelta_format():
    import datetime
    timedelta = datetime.timedelta(hours=1, minutes=2, seconds=3,
                                   microseconds=4)
    assert timedelta_format(timedelta) == '01:02:03.000004'
    timedelta = datetime.timedelta(hours=1, minutes=2, seconds=3)
    assert timedelta_format(timedelta) == '01:02:03.000000'
    timedelta = datetime.timedelta(hours=1, minutes=2)
    assert timedelta_format(timedelta) == '01:02:00.000000'
    timedelta = datetime.timedelta(hours=1)
    assert timedelta_format(timedelta) == '01:00:00.000000'

# Generated at 2022-06-12 19:46:59.758509
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )
    assert timedelta_parse('1:2:3.012345') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=12345
    )
    assert timedelta_parse('1:2:3.001234') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=1234
    )
    assert timedelta_parse('1:2:3.000123') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123
    )

# Generated at 2022-06-12 19:47:09.181731
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('0:0:12.345678')) == \
                                                     '00:00:12.345678'
    assert timedelta_format(timedelta_parse('0:12.345678')) == '00:00:12.345678'
    assert timedelta_format(timedelta_parse('12.345678')) == '00:00:12.345678'
    assert timedelta_format(timedelta_parse('12.0')) == '00:00:12.000000'
    assert timedelta_format(timedelta_parse('12')) == '00:00:12.000000'

# Generated at 2022-06-12 19:47:23.598102
# Unit test for function timedelta_format
def test_timedelta_format():
    time = time_isoformat(datetime_module.time(), timespec='microseconds')
    time = time.split('.')[0]
    delta = timedelta_parse(time)
    assert timedelta_format(delta) == time

if __name__ == '__main__':
    test_timedelta_format()

# Generated at 2022-06-12 19:47:26.989166
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=3, minutes=12, seconds=47, microseconds=345230,
    ))) == datetime_module.timedelta(
        hours=3, minutes=12, seconds=47, microseconds=345230,
    )

# Generated at 2022-06-12 19:47:33.787137
# Unit test for function timedelta_parse
def test_timedelta_parse():

    assert timedelta_parse('0:01:02.012345') == datetime_module.timedelta(
        minutes=1, seconds=2, microseconds=12345
    )
    assert timedelta_parse('01:02:03.012345') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=12345
    )
    assert timedelta_parse('1:2:3.012345') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=12345
    )
    assert timedelta_parse('1:02:03.012345') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=12345
    )
    assert timed

# Generated at 2022-06-12 19:47:39.172235
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta()
    assert timedelta_parse('0:0:0.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('0:0:0.100000') == datetime_module.timedelta(
        microseconds=100000
    )
    assert timedelta_parse('0:0:0.123456') == datetime_module.timedelta(
        microseconds=123456
    )
    assert timedelta_parse('0:0:10.01') == datetime_module.timedelta(
        seconds=10, microseconds=10000
    )
    assert timedelta_parse('0:0:10.9999') == datetime_module.timedelta

# Generated at 2022-06-12 19:47:45.179787
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=1,
        microseconds=1,
    )) == '01:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(
        hours=1,
        seconds=1,
    )) == '01:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(
        minutes=1,
        seconds=1,
    )) == '00:01:01.000000'

# Generated at 2022-06-12 19:47:51.720736
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta in (datetime_module.timedelta(microseconds=1),
                      datetime_module.timedelta(seconds=1),
                      datetime_module.timedelta(hours=1),
                      datetime_module.timedelta(days=1),
                      datetime_module.timedelta(days=12345),
                      datetime_module.timedelta(days=-12345),
                      datetime_module.timedelta(days=-1)):
        assert timedelta_parse(timedelta_format(timedelta)) == timedelta



# Generated at 2022-06-12 19:48:02.084375
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=3,
                                                      minutes=42,
                                                      seconds=11,
                                                      microseconds=231)) == '03:42:11.000231'
    assert timedelta_format(datetime_module.timedelta(hours=3,
                                                      minutes=42,
                                                      seconds=11,
                                                      microseconds=231,
                                                      days=-4)) == '-4 day, 03:42:11.000231'
    assert timedelta_format(datetime_module.timedelta(hours=3,
                                                      minutes=42,
                                                      seconds=11,
                                                      microseconds=231,
                                                      days=-8)) == '-8 day, 03:42:11.000231'

# Unit test

# Generated at 2022-06-12 19:48:06.903068
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(0))) == \
                                            datetime_module.timedelta(0)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(0, 0,
                                                                      1))) == \
                                          datetime_module.timedelta(0, 0, 1)

# Generated at 2022-06-12 19:48:11.957869
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=0.1)) == '00:00:00.100000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      seconds=0.1)) == '01:00:00.100000'
    assert timedelta_format(datetime_module.timedelta(hours=13)) == '13:00:00.000000'

# Generated at 2022-06-12 19:48:14.774714
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )) == '01:02:03.000004'



# Generated at 2022-06-12 19:48:30.356549
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=3, minutes=10,
                                                      seconds=20,
                                                      microseconds=3))\
                           == '03:10:20.000003'



# Generated at 2022-06-12 19:48:41.773833
# Unit test for function timedelta_parse

# Generated at 2022-06-12 19:48:51.128807
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('23:59:59.999999') == datetime_module.timedelta(1)
    assert timedelta_parse('23:59:59.000000') == datetime_module.timedelta(
        seconds=86399
    )
    assert timedelta_parse('23:59:59.001') == datetime_module.timedelta(
        seconds=86399, milliseconds=1
    )
    assert timedelta_parse('23:59:59.0001') == datetime_module.timedelta(
        seconds=86399, microseconds=10
    )

# Generated at 2022-06-12 19:48:59.861480
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=123)
    ) == '01:02:03.000123'

    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=123456)
    ) == '01:02:03.123456'

    assert timedelta_format(
        datetime_module.timedelta(0, 0, 123456)
    ) == '00:00:00.123456'

    assert timedelta_format(
        datetime_module.timedelta(0, 0, 123)
    ) == '00:00:00.000123'


# Generated at 2022-06-12 19:49:08.798334
# Unit test for function timedelta_parse
def test_timedelta_parse():
    # Test that the functions format and parse are inverses
    for s in (
        '1:00:00:000000000',
        '1:09:00:000000000',
        '1:09:9:000000000',
        '1:09:09:000000000',
        '1:09:09:999999999',
        '1:09:9:999999999',
        '1:09:0:999999999',
        '0:01:00.000000',
        '0:00:01.000000',
        '0:00:00.000001',
        '0:00:00.999999',
    ):
        parsed = timedelta_parse(s)
        formatted = timedelta_format(parsed)
        assert formatted == s


# Generated at 2022-06-12 19:49:15.372333
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(timedelta_parse('01:02:03.123456')) == \
                                                       '01:02:03.123456'
    assert timedelta_format(timedelta_parse('01:02:03.120000')) == \
                                                       '01:02:03.120000'
    assert timedelta_format(timedelta_parse('01:02:03.000000')) == \
                                                       '01:02:03.000000'
    assert timedelta_format(timedelta_parse('00:02:00.000000')) == \
                                                       '00:02:00.000000'
    assert timedelta_format(timedelta_parse('00:00:00.123456')) == \
                                                       '00:00:00.123456'

# Generated at 2022-06-12 19:49:27.667465
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:01.000002') == datetime_module.timedelta(
        seconds=1, microseconds=2
    )
    assert timedelta_parse('01:00:01.000002') == datetime_module.timedelta(
        hours=1, seconds=1, microseconds=2
    )


if sys.version_info[:2] >= (3, 7):
    # https://bugs.python.org/issue29200
    class_method = classmethod
    static_method = staticmethod

# Generated at 2022-06-12 19:49:34.749170
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                             '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
                             '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                             '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        microseconds=10
    )) == '00:00:00.000010'
    assert timedelta_format(datetime_module.timedelta(
        microseconds=1
    )) == '00:00:00.000001'



# Generated at 2022-06-12 19:49:43.493025
# Unit test for function timedelta_format
def test_timedelta_format():
    f = timedelta_format

    assert f(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert f(datetime_module.timedelta(hours=1, minutes=1)) == \
                                                     '01:01:00.000000'
    assert f(datetime_module.timedelta(hours=1, minutes=1, seconds=1)) == \
                                                     '01:01:01.000000'
    assert f(datetime_module.timedelta(hours=1, minutes=1,
                                       seconds=1, microseconds=1)) == \
                                                     '01:01:01.000001'



# Generated at 2022-06-12 19:49:51.790483
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=2,
                                                      minutes=45,
                                                      seconds=38,
                                                      microseconds=1000)) == \
                                                                '02:45:38.001000'
    assert timedelta_format(datetime_module.timedelta(hours=2,
                                                      minutes=45,
                                                      seconds=38,
                                                      microseconds=1001)) == \
                                                                '02:45:38.001001'



# Generated at 2022-06-12 19:50:22.324794
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
        '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == \
        '01:02:03.000004'
    assert timedelta_format(datetime_module.timedelta(
        days=1, hours=2, minutes=3, seconds=4, microseconds=5)) == \
        '50:03:04.000005'



# Generated at 2022-06-12 19:50:27.465587
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta_string = timedelta_format(datetime_module.timedelta(seconds=1))
    assert timedelta_string == '00:00:01.000000'
    timedelta_string = timedelta_format(datetime_module.timedelta(hours=2))
    assert timedelta_string == '02:00:00.000000'
    timedelta_string = timedelta_format(
        datetime_module.timedelta(seconds=1, microseconds=407677)
    )
    assert timedelta_string == '00:00:01.407677'



# Generated at 2022-06-12 19:50:33.134686
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:02:03.1234') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=1234)

    assert timedelta_parse('00:01:02.000001') == \
           datetime_module.timedelta(minutes=1, seconds=2, microseconds=1)

if sys.platform == 'win32':
    import ctypes
    _IS_TEXT_FILE_DEFAULT = ctypes.windll.kernel32.GetFileType(
        ctypes.c_long(0)
    ) == 1 # FILE_TYPE_CHAR
else:
    _IS_TEXT_FILE_DEFAULT = True


# Generated at 2022-06-12 19:50:36.515447
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for s in ['05:59:07.000001',
              '02:15:05.082702']:
        assert timedelta_parse(s) == timedelta_format(
            timedelta_parse(s)
        )

test_timedelta_parse()

# Generated at 2022-06-12 19:50:39.620213
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('01:02:03.004050')
    assert timedelta == datetime_module.timedelta(hours=1, minutes=2,
                                                  seconds=3, microseconds=4050)

# Generated at 2022-06-12 19:50:46.952234
# Unit test for function timedelta_parse

# Generated at 2022-06-12 19:50:53.331074
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1)) == '00:00:00.000001'
    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=29, seconds=33,
                                  microseconds=799999)
    ) == '01:29:33.799999'



# Generated at 2022-06-12 19:50:56.109041
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=3, minutes=50, seconds=3,
                                          microseconds=123456)
    assert timedelta_format(timedelta) == '03:50:03.123456'



# Generated at 2022-06-12 19:51:05.344437
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:00:00.000001') == datetime_module.timedelta(
        seconds=60, microseconds=1
    )
    assert timedelta_parse('1:00:00.999999') == datetime_module.timedelta(
        seconds=60, microseconds=999999
    )


if PY2:
    import jsonpickle.util
    import jsonpickle.util_py26
    jsonpickle.util.get_method_function = \
        jsonpickle.util_py26.get_method_function
    jsonpickle.util.noargs_decorator = \
        jsonpickle.util_py26.noargs_decorator
    jsonpickle.util.setdefault_decorator = \
        jsonpickle.util_py26.setdefault

# Generated at 2022-06-12 19:51:11.123750
# Unit test for function timedelta_format
def test_timedelta_format():
    dt = datetime_module.timedelta(days=2, hours=3, minutes=4,
                                   seconds=5, microseconds=6)
    assert timedelta_format(dt) == '75:04:05.000006'
    timedelta = datetime_module.timedelta(seconds=1)
    assert timedelta_format(timedelta) == '00:00:01.000001'


# Generated at 2022-06-12 19:52:10.309105
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0, 0, 1)) == \
                                                            '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(0, 1, 2)) == \
                                                            '00:00:01.000002'
    assert timedelta_format(datetime_module.timedelta(0, 3600, 37)) == \
                                                            '01:00:00.000037'
    assert timedelta_format(datetime_module.timedelta(0, 86400, 38)) == \
                                                            '24:00:00.000038'

# Generated at 2022-06-12 19:52:13.351196
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=3, minutes=4, seconds=5, microseconds=6)
    s = timedelta_format(timedelta)
    assert timedelta_parse(s) == timedelta

# Generated at 2022-06-12 19:52:22.089423
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(
        microseconds=10
    )
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(
        microseconds=100
    )
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(
        microseconds=1000
    )

# Generated at 2022-06-12 19:52:30.255758
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=3)) == \
           '03:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=3, minutes=2)) == \
           '03:02:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=3, minutes=2,
                                                      seconds=5)) == \
           '03:02:05.000000'
    assert timedelta_format(datetime_module.timedelta(hours=3, minutes=2,
                                                      seconds=5,
                                                      microseconds=400000)) == \
           '03:02:05.400000'

# Generated at 2022-06-12 19:52:36.384084
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert all((
        timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0),
        timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
            microseconds=1),
        timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
            seconds=1),
        timedelta_parse('00:01:00.000000') == datetime_module.timedelta(
            minutes=1),
        timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
            hours=1),
    ))

# Generated at 2022-06-12 19:52:46.305824
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == (
        datetime_module.timedelta(seconds=0)
    )
    assert timedelta_parse('00:00:00.000001') == (
        datetime_module.timedelta(microseconds=1)
    )
    assert timedelta_parse('00:00:00.1') == (
        datetime_module.timedelta(microseconds=100000)
    )
    assert timedelta_parse('00:00:00.00001') == (
        datetime_module.timedelta(microseconds=10)
    )
    assert timedelta_parse('00:00:00.1234') == (
        datetime_module.timedelta(microseconds=12340)
    )

# Generated at 2022-06-12 19:52:51.446961
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=0,
                                                      minutes=0,
                                                      seconds=0,
                                                      microseconds=0)) == \
                                                      '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == \
                                                      '01:02:03.000004'
    assert timedelta_format(datetime_module.timedelta(hours=3,
                                                      minutes=4,
                                                      seconds=5,
                                                      microseconds=1)) == \
                                                      '03:04:05.000001'

# Generated at 2022-06-12 19:52:58.635837
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=10, minutes=33,
                                                      seconds=23,
                                                      microseconds=400000)) == (
                          '10:33:23.400000')
    assert timedelta_format(datetime_module.timedelta(hours=12, minutes=0,
                                                      seconds=0,
                                                      microseconds=0)) == (
                          '12:00:00')
    assert timedelta_format(datetime_module.timedelta()) == (
                          '00:00:00')
    assert timedelta_format(datetime_module.timedelta(hours=12, minutes=0,
                                                      seconds=0,
                                                      microseconds=0)) == (
                          '12:00:00')
    assert timedelta

# Generated at 2022-06-12 19:53:07.077059
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=33,
                                                      microseconds=4321)) == \
                                                      '01:02:33.004321'
    assert timedelta_format(datetime_module.timedelta(seconds=1000)) == \
                                                      '00:16:40.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=33)) == '01:02:33'



# Generated at 2022-06-12 19:53:15.788773
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=6)) == (
        '06:00:00.000000')
    assert timedelta_format(datetime_module.timedelta(hours=6,
                                                      microseconds=1)) == (
        '06:00:00.000001')
    assert timedelta_format(datetime_module.timedelta(hours=6,
                                                      microseconds=10)) == (
        '06:00:00.000010')
    assert timedelta_format(datetime_module.timedelta(hours=6,
                                                      microseconds=100)) == (
        '06:00:00.000100')

# Generated at 2022-06-12 19:55:11.374089
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.999999') == datetime_module.timedelta(
        microseconds=999999
    )
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1
    )
    assert timedelta_parse('00:00:59.999999') == datetime_module.timedelta(
        seconds=59,
        microseconds=999999
    )
    assert timedelta_parse('00:01:00.000000') == datetime

# Generated at 2022-06-12 19:55:18.317856
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        days=4, hours=11, minutes=19, seconds=31, microseconds=456003
    ))) == datetime_module.timedelta(days=4, hours=11, minutes=19,
                                     seconds=31, microseconds=456003)

if PY2:
    from itertools import izip as zip
    zip_longest = zip
else:
    zip_longest = zip
    from itertools import zip_longest



# Generated at 2022-06-12 19:55:25.301174
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=2, hours=3, minutes=4,
                                                       seconds=5,
                                                       microseconds=6)) == \
                                                       '51:04:05.000006'
    assert timedelta_format(datetime_module.timedelta(days=2, hours=3, minutes=4,
                                                       seconds=5,
                                                       microseconds=6000)) == \
                                                       '51:04:05.006000'



# Generated at 2022-06-12 19:55:29.834279
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('23:59:59.999999') == datetime_module.timedelta(days=1) - datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)



# Generated at 2022-06-12 19:55:38.217034
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, microseconds=1)) == '01:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'

# Generated at 2022-06-12 19:55:47.822983
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(
        microseconds=10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(
        microseconds=100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(
        microseconds=1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(
        microseconds=10000)
   

# Generated at 2022-06-12 19:55:51.805238
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=4, minutes=4, seconds=4,
                                          microseconds=4)
    assert timedelta_parse('04:04:04.000004') == timedelta



# Generated at 2022-06-12 19:55:57.041918
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
           '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
           '01:00:00.000000'

