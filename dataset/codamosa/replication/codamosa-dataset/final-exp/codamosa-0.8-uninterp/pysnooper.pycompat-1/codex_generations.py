

# Generated at 2022-06-12 19:46:10.603791
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(seconds=123.45678)
    assert timedelta_format(timedelta) == '00:02:03.456780'



# Generated at 2022-06-12 19:46:15.885440
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('10:20:30.400000') == (
        datetime_module.timedelta(hours=10, minutes=20, seconds=30,
                                  microseconds=400000)
    )
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta()



# Generated at 2022-06-12 19:46:23.422280
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1.000001)) == \
                                                                '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=60.000001)) == \
                                                                '00:01:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=60*60*24+1)) == \
                                                                '24:00:01.000000'



# Generated at 2022-06-12 19:46:28.649596
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        '1:02:03.000000'
    ) == datetime_module.timedelta(hours=1, minutes=2, seconds=3)

    assert timedelta_parse(
        '1:02:03.123456'
    ) == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                   microseconds=123456)

# Generated at 2022-06-12 19:46:36.915231
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=123400)) == '01:02:03.123400'
    assert timedelta_format(datetime_module.timedelta(hours=10,
                                                      minutes=20,
                                                      seconds=30,
                                                      microseconds=12300)) == '10:20:30.012300'
    assert timedelta_format(datetime_module.timedelta(hours=100,
                                                      minutes=200,
                                                      seconds=300,
                                                      microseconds=12300)) == '100:200:300.012300'

# Generated at 2022-06-12 19:46:45.305083
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                              '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == \
                                                              '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=7)) == \
                                                              '00:00:07.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=13)) == \
                                                              '00:00:13.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=120)) == \
                                                              '00:02:00.000000'

# Generated at 2022-06-12 19:46:57.138680
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:0:1.001000') == datetime_module.timedelta(microseconds=1000)
    assert timedelta_parse('0:0:1.010000') == datetime_module.timedelta(microseconds=10000)
    assert timedelta_parse('0:0:1.100000') == datetime_module.timedelta(microseconds=100000)
    assert timedelta_parse('0:0:1.000001') == datetime_module.timedelta(microseconds=1)

# Generated at 2022-06-12 19:47:00.915219
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=4, minutes=2,
                                                      seconds=37,
                                                      microseconds=222)) \
           == '04:02:37.000222'



# Generated at 2022-06-12 19:47:11.680083
# Unit test for function timedelta_format
def test_timedelta_format():
    '''Test `timedelta_format` for correct output and correct
       input for timedelta_parse'''

# Generated at 2022-06-12 19:47:19.949430
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        0, 0, 1)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        0, 1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(
        0, 60)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        60 * 60)

# Generated at 2022-06-12 19:47:31.087262
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(0, 0, 123456)
    assert timedelta_format(timedelta) == '00:00:00.123456'

    timedelta = timedelta_parse('00:00:00.123456')
    assert timedelta_format(timedelta) == '00:00:00.123456'

# Generated at 2022-06-12 19:47:34.217915
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        '1:23:45.678901'
    ) == datetime_module.timedelta(hours=1, minutes=23, seconds=45,
                                   microseconds=678901)

# Generated at 2022-06-12 19:47:44.875111
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=4000)) \
                                                      == '01:02:03.004000'

    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3)) \
                                                      == '01:02:03.000000'

    assert timedelta_format(datetime_module.timedelta(seconds=1)) \
                                                      == '00:00:01.000000'

    assert timedelta_format(datetime_module.timedelta(microseconds=1)) \
                                                      == '00:00:00.000001'


# Generated at 2022-06-12 19:47:53.615611
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:48:03.491071
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert (timedelta_parse('00:00:00.000000') ==
            datetime_module.timedelta())
    assert (timedelta_parse('00:00:00.123456') ==
            datetime_module.timedelta(microseconds=123456))
    assert (timedelta_parse('00:00:01.123456') ==
            datetime_module.timedelta(seconds=1, microseconds=123456))
    assert (timedelta_parse('00:01:01.123456') ==
            datetime_module.timedelta(minutes=1, seconds=1, microseconds=123456))

# Generated at 2022-06-12 19:48:09.117140
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=2)) == '01:00:02.000000'



# Generated at 2022-06-12 19:48:17.173009
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta, string in ((datetime_module.timedelta(days=0,
                                                         hours=2,
                                                         minutes=3,
                                                         seconds=4,
                                                         microseconds=5),
                               '02:03:04.000005'),
                              (datetime_module.timedelta(days=1,
                                                         hours=2,
                                                         minutes=3,
                                                         seconds=4,
                                                         microseconds=5),
                               '26:03:04.000005')):
        assert timedelta_format(timedelta) == string
        assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:48:26.471909
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=5)) == '00:00:05.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1.5)) == '00:00:01.500000'
    assert timedelta_format(datetime_module.timedelta(seconds=1.005)) == '00:00:01.005000'
    assert timedelta_format(datetime_module.timedelta(milliseconds=25)) == '00:00:00.025000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'

# Generated at 2022-06-12 19:48:37.445481
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=3)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=2)) == '02:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=9)) == '00:09:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=2)) == '00:00:02.000000'
    assert timedelta_format(datetime_module.timedelta(milliseconds=9)) == '00:00:00.009000'


# Generated at 2022-06-12 19:48:40.595187
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1, seconds=1,
                                                      microseconds=1)) == \
                            '00:00:01.000001'


# Generated at 2022-06-12 19:49:06.257634
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:49:14.177656
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(
        hours=1)
    assert timedelta_parse('1:00:00.000001') == datetime_module.timedelta(
        hours=1, microseconds=1)
    assert timedelta_parse('1:00:00.123456') == datetime_module.timedelta(
        hours=1, microseconds=123456)
    assert timedelta_parse('1:01:02.345678') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=2, microseconds=345678)

# Generated at 2022-06-12 19:49:26.248228
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        microseconds=1
    )) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(
        seconds=1
    )) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(
        minutes=1
    )) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=1
    )) == '01:00:00.000000'



# Generated at 2022-06-12 19:49:29.911819
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(seconds=1)
    )) == datetime_module.timedelta(seconds=1)

# Generated at 2022-06-12 19:49:41.058391
# Unit test for function timedelta_parse
def test_timedelta_parse():
    if sys.version_info[:2] >= (3, 6):
        assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
        assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(seconds=1)
        assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(minutes=1)
        assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(hours=1)
        assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)

# Generated at 2022-06-12 19:49:49.914656
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:1:0.000000') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('1:0:0.000000') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('1:2:3.456000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456000
    )



# Generated at 2022-06-12 19:49:57.986062
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('1:02:03.004000')) == \
           '01:02:03.004000'
    assert timedelta_format(timedelta_parse('1:2:3.4')) == \
           '01:02:03.004000'
    assert timedelta_format(timedelta_parse('1:2:3.400')) == \
           '01:02:03.004000'
    assert timedelta_format(timedelta_parse('1:2:3.040')) == \
           '01:02:03.004000'
    assert timedelta_format(timedelta_parse('1:2:03.04')) == \
           '01:02:03.004000'

# Generated at 2022-06-12 19:50:07.668455
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta()
    assert timedelta_parse('1:0:0.0') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('1:1:0.0') == datetime_module.timedelta(hours=1,
                                                                   minutes=1)
    assert timedelta_parse('1:1:1.0') == datetime_module.timedelta(hours=1,
                                                                   minutes=1,
                                                                   seconds=1)

# Generated at 2022-06-12 19:50:11.350788
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0)
    assert timedelta_parse('1:2:3.4') == datetime_module.timedelta(hours=1,
                                                                    minutes=2,
                                                                    seconds=3,
                          microseconds=40000)

# Generated at 2022-06-12 19:50:16.099282
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta_format(datetime_module.timedelta(hours=1))
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=1)
    )) == datetime_module.timedelta(hours=1)



# Generated at 2022-06-12 19:50:56.153301
# Unit test for function timedelta_format
def test_timedelta_format():
    _ = timedelta_format
    assert _(datetime_module.timedelta(days=1, hours=1, minutes=1, seconds=2,
                                       microseconds=3)) == '25:01:02.000003'
    assert _(datetime_module.timedelta(days=1, hours=2, minutes=3, seconds=4,
                                       microseconds=5)) == '26:03:04.000005'
    assert _(datetime_module.timedelta(days=0, hours=0, minutes=0, seconds=0,
                                       microseconds=0)) == '00:00:00.000000'

# Generated at 2022-06-12 19:50:58.246105
# Unit test for function timedelta_format
def test_timedelta_format():
    td = datetime_module.timedelta(hours=7, minutes=25, seconds=36,
                                   microseconds=123456)
    assert timedelta_format(td) == '07:25:36.123456'



# Generated at 2022-06-12 19:51:01.157403
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                         '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1.0000005)) \
                                                          == '00:00:01.000000'


# Generated at 2022-06-12 19:51:06.548541
# Unit test for function timedelta_parse
def test_timedelta_parse():
    td = datetime_module.timedelta(hours=1, minutes=23, seconds=45,
                                   microseconds=67890)
    s = timedelta_format(td)
    parsed_td = timedelta_parse(s)
    assert td == parsed_td

# Generated at 2022-06-12 19:51:14.997754
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(milliseconds=1)) == '00:00:00.001000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'

# Generated at 2022-06-12 19:51:18.088004
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(
        hours=2, minutes=3, seconds=4, microseconds=5
    )
    assert timedelta_format(timedelta) == '02:03:04.000005'



# Generated at 2022-06-12 19:51:25.389250
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta, string in [
        (datetime_module.timedelta(0), '00:00:00.000000'),
        (datetime_module.timedelta(hours=1), '01:00:00.000000'),
        (datetime_module.timedelta(minutes=25), '00:25:00.000000'),
        (datetime_module.timedelta(hours=3, minutes=25, seconds=2,
                                   microseconds=421234),
         '03:25:02.421234'),
    ]:
        assert timedelta_format(timedelta) == string


# Generated at 2022-06-12 19:51:27.899927
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:23:45.678901') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=45, microseconds=678901
    )

# Generated at 2022-06-12 19:51:34.330367
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert datetime_module.timedelta(hours=2, minutes=15, seconds=12,
                                     microseconds=989898) == timedelta_parse(
        '02:15:12.989898'
    )

try:
    import importlib.resources as resources
except ImportError:
    import importlib_resources as resources

try:
    from contextlib import asynccontextmanager
except ImportError:
    from async_generator import asynccontextmanager

# Generated at 2022-06-12 19:51:41.138170
# Unit test for function timedelta_format
def test_timedelta_format():
    from datetime import timedelta
    assert timedelta_format(timedelta(hours=1, minutes=2, seconds=3,
                                      microseconds=123456)) == \
                     '01:02:03.123456'
    assert timedelta_format(timedelta(hours=1, minutes=2, seconds=3,
                                      microseconds=999999)) == \
                     '01:02:03.999999'
    assert timedelta_format(timedelta(hours=1, minutes=2, seconds=3,
                                      microseconds=0)) == \
                       '01:02:03.000000'


# Generated at 2022-06-12 19:52:55.248327
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=2)) == \
           '00:00:02.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=2)) == \
           '00:00:00.000002'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=1
    )) == '01:01:01.000001'



# Generated at 2022-06-12 19:53:05.570448
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('72:10:23:100400')) == \
           '72:10:23.100400'
    assert timedelta_format(timedelta_parse('5:27:1')) == '05:27:01.000000'
    assert timedelta_format(timedelta_parse('0:27.2')) == '00:27:12.000000'
    assert timedelta_format(timedelta_parse('0:27')) == '00:27:00.000000'
    assert timedelta_format(timedelta_parse('0:27.1')) == '00:27:01.000000'
    assert timedelta_format(timedelta_parse('0:0.1')) == '00:00:01.000000'

# Generated at 2022-06-12 19:53:09.263789
# Unit test for function timedelta_format
def test_timedelta_format():
    time = datetime_module.datetime.strptime(
        '14:19:54.437661',
        '%H:%M:%S.%f'
    ).time()
    assert timedelta_format(time - datetime_module.time()) == '14:19:54.437661'

# Generated at 2022-06-12 19:53:17.390293
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=3)) == '03:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=66,
                                                      microseconds=100)) == \
           '01:06:00.000100'
    assert timedelta_format(datetime_module.timedelta(minutes=66,
                                                      microseconds=100)) == \
           '01:06:00.000100'
    assert timedelta_format(datetime_module.timedelta(minutes=-7, seconds=-2)) == \
           '-00:07:02.000000'
    assert timedelta_format(datetime_module.timedelta(hours=24)) == '24:00:00.000000'


# Generated at 2022-06-12 19:53:29.042252
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.456789') == timedelta_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456789
    )


if PY3:
    def iter_zip(*iterables):
        return zip(*iterables)
    def iter_zip_longest(*iterables, fillvalue = None):
        return zip_longest(*iterables, fillvalue = fillvalue)
else:
    from future_builtins import zip, zip_longest
    def iter_zip(*iterables):
        return list(zip(*iterables))
    def iter_zip_longest(*iterables, fillvalue = None):
        return list(zip_longest(*iterables, fillvalue = fillvalue))

# Generated at 2022-06-12 19:53:39.521506
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:44:44.444444') == datetime_module.timedelta(1, 16284, 444444)
    assert timedelta_parse('1:44:44.444444').total_seconds() == 325484.444444
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(0, 0, 0)
    assert timedelta_parse('0:00:00.000000').total_seconds() == 0
    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('0:00:00.000001').total_seconds() == 0.000001

# Generated at 2022-06-12 19:53:51.240740
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(days=3)) == '00:00:43:2000000'
    assert timedelta_parse('00:00:43:2000000') == datetime_module.timedelta(days=3)


if PY3:
    class DateOnlyMeta(type):
        def __getnewargs_ex__(self):
            return (self.year, self.month, self.day)

    class DateOnly(datetime_module.date, metaclass=DateOnlyMeta):
        """A datetime.date with no time."""
        def __new__(cls, year, month, day):
            return super().__new__(cls, year, month, day)


# Generated at 2022-06-12 19:53:58.533212
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00:000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00:000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01:000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00:000001'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1)) == '01:01:00:000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=1)) == '01:00:01:000000'

# Generated at 2022-06-12 19:54:03.841126
# Unit test for function timedelta_format
def test_timedelta_format():
    timestring = timedelta_format(datetime_module.timedelta(days=2,
                                                            hours=4,
                                                            minutes=12,
                                                            seconds=33,
                                                            microseconds=123456))
    assert timestring == '04:12:33.123456'


# Generated at 2022-06-12 19:54:14.170921
# Unit test for function timedelta_parse
def test_timedelta_parse():
    def assert_timedelta(s, expected_timedelta):
        assert timedelta_parse(s) == expected_timedelta
    
    assert_timedelta('0:0:0.000000', datetime_module.timedelta(0))
    assert_timedelta('0:0:0.000001', datetime_module.timedelta(0, 0, 1))
    assert_timedelta('0:0:1.000000', datetime_module.timedelta(0, 1))
    assert_timedelta('0:1:0.000000', datetime_module.timedelta(0, 60))
    assert_timedelta('1:0:0.000000', datetime_module.timedelta(0, 3600))