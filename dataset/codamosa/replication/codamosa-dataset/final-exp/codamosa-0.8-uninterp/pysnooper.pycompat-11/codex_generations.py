

# Generated at 2022-06-12 19:46:12.850890
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=12,
                                                      minutes=34,
                                                      seconds=56,
                                                      microseconds=789012)) == \
           '12:34:56.789012'

    assert timedelta_format(datetime_module.timedelta(hours=12,
                                                      minutes=34,
                                                      seconds=56,
                                                      microseconds=789000)) == \
           '12:34:56.789000'

    assert timedelta_format(datetime_module.timedelta(hours=12,
                                                      minutes=34,
                                                      seconds=56,
                                                      microseconds=789100)) == \
           '12:34:56.7891'


# Generated at 2022-06-12 19:46:20.001401
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:46:25.449411
# Unit test for function timedelta_parse
def test_timedelta_parse():
    '''
    Unit test for timedelta_parse, written in `assert`-style.
    '''
    assert timedelta_parse('1:23:45.678987') == \
           datetime_module.timedelta(seconds=1, minutes=23,
                                     microseconds=678987)
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(
                                                    microseconds=1)



# Generated at 2022-06-12 19:46:33.933581
# Unit test for function timedelta_parse
def test_timedelta_parse():
    r'''Unit test for function timedelta_parse.'''
    m1 = '0:00:00.000000'
    m2 = '0:00:00.000001'
    m3 = '0:00:00.999999'
    m4 = '0:01:00.000000'
    m5 = '0:01:00.000001'
    m6 = '0:01:00.999999'
    m7 = '0:01:01.000000'
    m8 = '0:01:01.000001'
    m9 = '0:01:01.999999'
    m10 = '1:01:01.999999'
    m11 = '23:59:59.999999'
    assert timedelta_parse(m1) == datetime_module.timedelta(0)

# Generated at 2022-06-12 19:46:43.367951
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      seconds=2)) == '00:01:02.000000'
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=2, hours=3)) == '51:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=0,
                                                      hours=0,
                                                      seconds=0,
                                                      microseconds=1)) == '00:00:00.000001'



# Generated at 2022-06-12 19:46:48.746901
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=1, hours=4,
                                          minutes=5, seconds=6,
                                          microseconds=123_456_789)
    assert timedelta_format(timedelta) == '04:05:06.123456789'


# Generated at 2022-06-12 19:46:59.857503
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=3, minutes=5, seconds=7, microseconds=9
    ))) == datetime_module.timedelta(hours=3, minutes=5, seconds=7,
                                     microseconds=9)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    ))) == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=4)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    ))) == datetime_module.timed

# Generated at 2022-06-12 19:47:10.947622
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
           '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'

    # Checking for possible rounding errors
    assert timedelta_format(datetime_module.timedelta(microseconds=0.5)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=0.5) * 2) == \
           '00:00:00.000002'



# Generated at 2022-06-12 19:47:19.430357
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta_data = [
        (0, '00:00:00.000000'),
        (1, '00:00:00.000001'),
        (99, '00:00:00.000099'),
        (100, '00:00:00.000100'),
        (1000, '00:00:00.001000'),
        (10000, '00:00:00.010000'),
        (100000, '00:00:00.100000'),
        (1000000, '00:00:01.000000'),
    ]

    for microseconds, formatted_string in timedelta_data:
        timedelta = datetime_module.timedelta(microseconds=microseconds)
        formatted = timedelta_format(timedelta)
        assert formatted == formatted_string



# Generated at 2022-06-12 19:47:25.008357
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == \
           datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        days=18, hours=12, minutes=3, seconds=18, microseconds=7345862
    ))) == datetime_module.timedelta(
        days=18, hours=12, minutes=3, seconds=18, microseconds=7345862
    )


if PY3:
    import urllib.parse
    urlencode = urllib.parse.urlencode
    quote = urllib.parse.quote
    unquote = urllib.parse.unquote
    unquote_plus = urllib.parse.unquote_plus

# Generated at 2022-06-12 19:47:45.991596
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:01:02.123456') == \
           datetime_module.timedelta(minutes=1, seconds=2, microseconds=123456)
    assert timedelta_parse('01:02:03.123456') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=123456)
    assert timedelta_parse('10:20:30.123456') == \
           datetime_module.timedelta(hours=10, minutes=20, seconds=30,
                                     microseconds=123456)

# Generated at 2022-06-12 19:47:54.424190
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.123456') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=123456)
    assert timedelta_parse('01:02:03.010203') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=10203)
    assert timedelta_parse('01:02:03.123') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=123000)

# Generated at 2022-06-12 19:48:04.280882
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) \
           == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1)) \
           == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) \
           == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=60)) \
           == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) \
           == '00:01:00.000000'

# Generated at 2022-06-12 19:48:10.429717
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == \
                            datetime_module.timedelta(seconds=0)
    assert timedelta_parse('00:00:00.000000') == \
                            datetime_module.timedelta(microseconds=0)
    assert timedelta_parse('00:00:01.000000') == \
                            datetime_module.timedelta(seconds=1)
    assert timedelta_parse('00:00:01.100000') == \
                            datetime_module.timedelta(seconds=1,
                                                      microseconds=100000)
    assert timedelta_parse('00:00:01.100000') == \
                            datetime_module.timedelta(microseconds=1100000)

# Generated at 2022-06-12 19:48:18.700604
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('00:00:00.000000')) == \
           '00:00:00.000000'
    assert timedelta_format(timedelta_parse('00:00:00.000001')) == \
           '00:00:00.000001'
    assert timedelta_format(timedelta_parse('00:00:00.000010')) == \
           '00:00:00.000010'
    assert timedelta_format(timedelta_parse('00:00:00.000100')) == \
           '00:00:00.000100'
    assert timedelta_format(timedelta_parse('00:00:00.001000')) == \
           '00:00:00.001000'

# Generated at 2022-06-12 19:48:27.006184
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for timedelta in (
        datetime_module.timedelta(seconds=1),
        datetime_module.timedelta(seconds=1, microseconds=1),
        datetime_module.timedelta(seconds=1, microseconds=123456),
        datetime_module.timedelta(minutes=1, seconds=2, microseconds=123456),
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=123456),
        datetime_module.timedelta(days=1, hours=2, minutes=3, seconds=4,
                                  microseconds=123456),
    ):
        assert timedelta_format(timedelta) == timedelta_parse(
            timedelta_format(timedelta)
        )

test_timedelta_

# Generated at 2022-06-12 19:48:34.121188
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1,
                                                      seconds=1,
                                                      microseconds=1)) == \
           '01:01:01.000001'



# Generated at 2022-06-12 19:48:44.601881
# Unit test for function timedelta_format
def test_timedelta_format():
    from . import testing_tools
    # The first line is running the actual unit-test:
    assert timedelta_format(timedelta_parse('4:5:6.123456')) == '04:05:06.123456'
    delta = datetime_module.timedelta(seconds=123)
    assert timedelta_format(delta) == '00:02:03.000000'
    testing_tools.expect_exception(
        NotImplementedError,
        lambda: timedelta_format(delta, timespec='seconds')
    )
    delta = datetime_module.timedelta(seconds=0)
    assert timedelta_format(delta) == '00:00:00.000000'

# Generated at 2022-06-12 19:48:48.183218
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(
        hours=2, minutes=1, seconds=55, microseconds=123456
    )
    assert timedelta_format(timedelta) == '02:01:55.123456'



# Generated at 2022-06-12 19:48:51.869560
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=12,
                                                      minutes=34,
                                                      seconds=56,
                                                      microseconds=7890)) == \
        '12:34:56.007890'



# Generated at 2022-06-12 19:49:22.491051
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1, microseconds=1)) == '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(minutes=1, seconds=1, microseconds=1)) == '00:01:01.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1, seconds=1, microseconds=1)) == '01:01:01.000001'




# Generated at 2022-06-12 19:49:27.907950
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0,
                                                               microseconds=1)
    assert timedelta_parse(
        '23:59:59.999999'
    ) == datetime_module.timedelta(days=1) - datetime_module.timedelta(
        microseconds=1)
    assert timedelta_parse('23:59:59.999999') == datetime_module.timedelta(
        days=1) - datetime_module.timedelta(microseconds=1)

# Generated at 2022-06-12 19:49:35.088380
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.000004') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=4)
    assert timedelta_parse('1:02:03.000004') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=4)
    assert timedelta_parse('01:2:03.000004') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=4)
    assert timedelta_parse('1:2:3.4') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=400000)

# Generated at 2022-06-12 19:49:46.059626
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('1:23:45.012345')
    _timedelta = datetime_module.timedelta(
        hours=1,
        minutes=23,
        seconds=45,
        microseconds=12345
    )
    if timedelta != _timedelta:
        raise AssertionError(timedelta)

    timedelta = timedelta_parse(
        timedelta.total_seconds().isoformat(timespec='microseconds')
    )
    if timedelta != _timedelta:
        raise AssertionError(timedelta)

    timedelta = timedelta_parse(b'1:23:45.012345')
    if timedelta != _timedelta:
        raise AssertionError(timedelta)



# Generated at 2022-06-12 19:49:48.591780
# Unit test for function timedelta_format
def test_timedelta_format(): assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000' # noqa

# Generated at 2022-06-12 19:49:57.276828
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=24)) == \
                                                '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=23)) == \
                                                '23:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1)) == \
                                                '01:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=1,
        seconds=1, microseconds=1
    )) == '01:01:01.000001'

# Generated at 2022-06-12 19:50:01.202360
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('12:34:56.000001') == \
                                 datetime_module.timedelta(hours=12,
                                                           minutes=34,
                                                           seconds=56,
                                                           microseconds=1)

# Generated at 2022-06-12 19:50:05.189701
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=4567)) == \
        '01:02:03.004567'


# Generated at 2022-06-12 19:50:07.907327
# Unit test for function timedelta_parse
def test_timedelta_parse():
    delta = timedelta_parse('3:14:15.926535')
    assert delta.total_seconds() == 3 * 60**2 + 14 * 60 + 15 + .926535
    assert timedelta_format(delta) == '03:14:15.926535'



# Generated at 2022-06-12 19:50:13.831924
# Unit test for function timedelta_format
def test_timedelta_format():
    from . import test_utils
    test_utils.assert_exception(ValueError, timedelta_format,
                                datetime_module.time.fromisoformat('23:59:59'),
                                'bla')
    for i in range(24):
        for j in range(60):
            for k in range(60):
                for l in range(1000000):
                    timedelta = datetime_module.timedelta(hours=i, minutes=j,
                                                          seconds=k,
                                                          microseconds=l)
                    time = (datetime_module.datetime.min + timedelta).time()
                    s = time_isoformat(time, 'microseconds')
                    assert timedelta_format(timedelta) == s

# Generated at 2022-06-12 19:50:39.410732
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('03:04:05.600000')
    assert timedelta == datetime_module.timedelta(seconds=11_145)
    assert timedelta.microseconds == 600000

    timedelta = timedelta_parse('3:4:5.600000')
    assert timedelta == datetime_module.timedelta(seconds=11_145)
    assert timedelta.microseconds == 600000

# Generated at 2022-06-12 19:50:46.924550
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1, microseconds=1)) == '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(days=1, seconds=1, microseconds=1)) == '24:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(days=1, minutes=1, seconds=1, microseconds=1)) == '24:01:01.000001'

# Generated at 2022-06-12 19:50:51.875607
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == datetime_module.timedelta()
    assert timedelta_parse('12:34:56.123456') == datetime_module.timedelta(hours=12, minutes=34, seconds=56, microseconds=123456)


# Generated at 2022-06-12 19:50:59.732340
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('01:02:03.000000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3)
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456)
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456)

# Generated at 2022-06-12 19:51:06.462600
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1,
                                   minutes=2, seconds=3,
                                   microseconds=123456))) == \
                                                datetime_module.timedelta(hours=1,
                                   minutes=2, seconds=3,
                                   microseconds=123456)



NullType = type(None)

# Generated at 2022-06-12 19:51:14.924832
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=22,
                                                      minutes=32,
                                                      seconds=57,
                                                      microseconds=123456))==\
           '22:32:57.123456'
    assert timedelta_format(datetime_module.timedelta(hours=22,
                                                      minutes=32,
                                                      seconds=0,
                                                      microseconds=0))==\
           '22:32:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=22,
                                                      minutes=0,
                                                      seconds=0,
                                                      microseconds=0))==\
           '22:00:00.000000'

# Generated at 2022-06-12 19:51:20.667265
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:01:02.014567') == datetime_module.timedelta(
        seconds=62, microseconds=1456
    )

    assert timedelta_parse('01:02:03.014567') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=1456
    )

    assert timedelta_parse('22:30:00.014567') == datetime_module.timedelta(
        hours=22, minutes=30, seconds=0, microseconds=1456
    )

    assert timedelta_parse('23:00:00.014567') == datetime_module.timedelta(
        hours=23, minutes=0, seconds=0, microseconds=1456
    )


# Generated at 2022-06-12 19:51:25.683455
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=2, minutes=1,
                                                      seconds=32,
                                                      microseconds=615000)) == \
           '02:01:32.615000'


# Generated at 2022-06-12 19:51:33.489952
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.456000') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=456000)
    assert timedelta_parse('0:0:0.000000') == \
           datetime_module.timedelta(hours=0, minutes=0, seconds=0,
                                     microseconds=0)
    assert timedelta_parse('23:59:59.999999') == \
           datetime_module.timedelta(days=1, hours=23, minutes=59, seconds=59,
                                     microseconds=999999)



# Generated at 2022-06-12 19:51:40.487958
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(
        datetime_module.timedelta(hours=23, minutes=24, seconds=25,
                                  microseconds=60000)
    ) == '23:24:25.060000'
    assert timedelta_format(
        datetime_module.timedelta(hours=10, minutes=1, seconds=2,
                                  microseconds=425000)
    ) == '10:01:02.425000'

test_timedelta_format()

# Generated at 2022-06-12 19:52:29.348437
# Unit test for function timedelta_format
def test_timedelta_format():
    td = datetime_module.timedelta(hours=100, minutes=2, seconds=30,
                                   microseconds=1232)
    assert timedelta_format(td) == '100:02:30.001232'

# Generated at 2022-06-12 19:52:34.412290
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=2)) == \
        '00:00:02.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=2.5)) == \
        '00:00:02.500000'
    assert timedelta_format(datetime_module.timedelta(seconds=2.54)) == \
        '00:00:02.540000'



# Generated at 2022-06-12 19:52:45.152686
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=14)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=14, seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(days=14, seconds=1, microseconds=1)) == '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(days=14, minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=14, minutes=1, seconds=1)) == '00:01:01.000000'

# Generated at 2022-06-12 19:52:48.054639
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == (
        '01:02:03.000004'
    )



# Generated at 2022-06-12 19:52:55.252778
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == (
                                                          '01:02:03.000004'
                                                      )
    assert timedelta_format(datetime_module.timedelta(hours=1 * 24 * 365 * 10)) == (
                                                          '8760:00:00.000000'
                                                      )

# Generated at 2022-06-12 19:53:05.570288
# Unit test for function timedelta_parse
def test_timedelta_parse():
    start_time = datetime_module.datetime.now()
    print(timedelta_format(datetime_module.timedelta(1, 2, 3)))
    stop_time = datetime_module.datetime.now()
    assert stop_time - start_time < datetime_module.timedelta(0.01)
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(0))
    ) == datetime_module.timedelta(0)
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(1))
    ) == datetime_module.timedelta(1)

# Generated at 2022-06-12 19:53:12.218637
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
   

# Generated at 2022-06-12 19:53:15.207703
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=14, minutes=39,
                                                      seconds=22,
                                                      microseconds=725045)) == \
           '14:39:22.725045'


# Generated at 2022-06-12 19:53:20.972973
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=4)
    assert timedelta == timedelta_parse(timedelta_format(timedelta))

test_timedelta_parse()

# Generated at 2022-06-12 19:53:30.168634
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=5))) == (datetime_module.timedelta(hours=5))
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=5, minutes=3))) == (datetime_module.timedelta(hours=5, minutes=3))
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=5, minutes=3, seconds=10))) == (datetime_module.timedelta(hours=5, minutes=3, seconds=10))

# Generated at 2022-06-12 19:55:11.492762
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(15)) == '00:00:15.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=12, minutes=34, seconds=56, microseconds=123456
    )) == '12:34:56.123456'
    assert timedelta_format(datetime_module.timedelta(
        days=999, hours=12, minutes=34, seconds=56, microseconds=123456
    )) == '12:34:56.123456'



# Generated at 2022-06-12 19:55:21.896822
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                                                          '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=78)) == \
                                                          '01:18:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=90)) == \
                                                          '00:01:30.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                          '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=123456)) == \
                                                          '00:00:00.123456'

# Generated at 2022-06-12 19:55:30.076422
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=0))) == datetime_module.timedelta(hours=0)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1))) == datetime_module.timedelta(hours=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=2))) == datetime_module.timedelta(hours=2)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=0, minutes=1))) == datetime_module.timedelta(hours=0, minutes=1)

# Generated at 2022-06-12 19:55:38.403944
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(1)) == '24:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1, microseconds=2)) == '00:00:01.000002'
    assert timedelta_format

# Generated at 2022-06-12 19:55:44.882782
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(days=100, hours=1,
                                                   minutes=2, seconds=3,
                                                   microseconds=4))
    ) == datetime_module.timedelta(days=100, hours=1,
                                   minutes=2, seconds=3,
                                   microseconds=4)


if sys.version_info[:2] >= (3, 6):
    timezone_from_offset = datetime_module.timezone.fromutc
else:
    def timezone_from_offset(offset):
        return datetime_module.timezone(offset=offset, name='cute_timezone')



# Generated at 2022-06-12 19:55:53.971236
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
        '00:00:00.000001'
    assert timedelta_format(
        datetime_module.timedelta(hours=1, seconds=1, microseconds=2)
    ) == \
        '01:00:01.000002'
    assert timedelta_format(
        datetime_module.timedelta(hours=12, minutes=24, seconds=36,
                                  microseconds=48)
    ) == \
        '12:24:36.000048'
    assert timedelta_format(
        datetime_module.timedelta(days=1, hours=1, seconds=1, microseconds=2)
    ) == \
        '25:00:01.000002'



# Unit test

# Generated at 2022-06-12 19:56:04.166326
# Unit test for function timedelta_format
def test_timedelta_format():
    try:
        from nose.tools import assert_equal
    except ImportError:
        pass
    else:
        assert_equal(timedelta_format(datetime_module.timedelta(hours=3,
                                                                minutes=2,
                                                                seconds=1,
                                                                microseconds=6)),
                     '03:02:01.000006')
        assert_equal(timedelta_format(datetime_module.timedelta(hours=3,
                                                                minutes=2,
                                                                seconds=1,
                                                                microseconds=5)),
                     '03:02:01.000005')