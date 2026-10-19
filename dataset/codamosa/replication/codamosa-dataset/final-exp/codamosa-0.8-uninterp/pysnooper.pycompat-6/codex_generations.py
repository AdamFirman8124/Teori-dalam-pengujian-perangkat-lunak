

# Generated at 2022-06-12 19:46:14.630522
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('2:01:02.012345') \
           == datetime_module.timedelta(hours=2, minutes=1, seconds=2,
                                        microseconds=12345)


# Generated at 2022-06-12 19:46:17.545861
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=1, hours=2, minutes=3,
                                          seconds=4, microseconds=5)
    assert timedelta_format(timedelta) == '51:03:04.000005'


# Generated at 2022-06-12 19:46:21.463967
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        timedelta_format(timedelta_parse('12:34:56.7890'))
    ) == timedelta_parse('12:34:56.7890')

# Generated at 2022-06-12 19:46:30.004886
# Unit test for function timedelta_format
def test_timedelta_format():
    from .test_timing import timedelta_timing

    assert timedelta_format(
        timedelta_timing(  # `timedelta_timing` is the duration of a year
            datetime_module.date(1970, 1, 1),
            datetime_module.date(1971, 1, 1)
        )
    ) == '23:59:59.999999'

    assert timedelta_format(
        timedelta_timing(  # `timedelta_timing` is just above a year
            datetime_module.date(1970, 1, 1),
            datetime_module.date(1971, 6, 1)
        )
    ) == '24:00:00.000000'


# Generated at 2022-06-12 19:46:36.916329
# Unit test for function timedelta_format
def test_timedelta_format():
    '''Test that `timedelta_format` is doing what we expect it to do.'''
    import nose
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2)) \
           == '01:02:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) \
           == '01:02:03.000004'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3, milliseconds=3,
                                                      microseconds=4)) \
           == '01:02:03.003000'

# Generated at 2022-06-12 19:46:45.305047
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('1:1:1.1')) == '01:01:01.001000'
    assert timedelta_format(timedelta_parse('1:1:1.1000001')) == '01:01:01.1000001'
    assert timedelta_format(timedelta_parse('1:1:1')) == '01:01:01'
    assert timedelta_format(timedelta_parse('1:1.1')) == '00:01:01.001000'
    assert timedelta_format(timedelta_parse('1:1.1000001')) == '00:01:01.1000001'
    assert timedelta_format(timedelta_parse('1')) == '00:00:01'

# Generated at 2022-06-12 19:46:57.138750
# Unit test for function timedelta_parse
def test_timedelta_parse():
    t1 = timedelta_parse('1:2:3')
    t2 = datetime_module.timedelta(hours=1, minutes=2, seconds=3)
    assert t1 == t2
    
    t1 = timedelta_parse('1:2:3.123456')
    t2 = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                   microseconds=123456)
    assert t1 == t2
    
    t1 = timedelta_parse('1:2:3.1234')
    t2 = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                   microseconds=123400)
    assert t1 == t2
    
    t1 = timedelta_parse('1:2:3.123')


# Generated at 2022-06-12 19:47:07.372069
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456)
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(
        minutes=62, seconds=3, microseconds=123456)
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(
        seconds=3723, microseconds=123456)
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(
        microseconds=3723123456)



# Generated at 2022-06-12 19:47:16.364327
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:30:00') == \
           datetime_module.timedelta(hours=1, minutes=30)
    assert timedelta_parse('1:30:30') == \
           datetime_module.timedelta(hours=1, minutes=30, seconds=30)
    assert timedelta_parse('1:30:30.040') == \
           datetime_module.timedelta(hours=1, minutes=30, seconds=30,
                                     microseconds=40)
    assert timedelta_parse('1:30:30.040440') == \
           datetime_module.timedelta(hours=1, minutes=30, seconds=30,
                                     microseconds=440)

# Generated at 2022-06-12 19:47:22.933509
# Unit test for function timedelta_parse

# Generated at 2022-06-12 19:47:39.332177
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(
        hours=5, minutes=6, seconds=7, microseconds=8
    )
    assert timedelta_format(timedelta) == '05:06:07.000008'

    timedelta = datetime_module.timedelta(
        hours=5, minutes=6, seconds=7, microseconds=890
    )
    assert timedelta_format(timedelta) == '05:06:07.000890'


# Generated at 2022-06-12 19:47:49.904453
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        days=25, hours=3, minutes=14, seconds=55, microseconds=99999
    ))) == datetime_module.timedelta(
        days=25, hours=3, minutes=14, seconds=55, microseconds=99999
    )
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        days=25, hours=30, minutes=14, seconds=55, microseconds=99999
    ))) == datetime_module.timedelta(
        days=25, hours=30, minutes=14, seconds=55, microseconds=99999
    )

# Generated at 2022-06-12 19:47:52.686886
# Unit test for function timedelta_format
def test_timedelta_format():

    timedelta = datetime_module.timedelta(hours=8, minutes=24, seconds=3,
                                          microseconds=500)
    assert timedelta_format(timedelta) == '08:24:03.000500'



# Generated at 2022-06-12 19:48:02.778451
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(0,0,1)
    assert timedelta_parse('0:00:00.100000') == datetime_module.timedelta(0,0,100000)
    assert timedelta_parse('0:00:00.1') == datetime_module.timedelta(0,0,1)
    assert timedelta_parse('0:00:01.000000') == datetime_module.timedelta(0,1)
    assert timedelta_parse('0:01:00.000000') == datetime_module.timedelta(0,60)

# Generated at 2022-06-12 19:48:07.720477
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=444444)) == \
                                                      '01:02:03.444444'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=2,
                                                      minutes=3,
                                                      seconds=4,
                                                      milliseconds=5)) == \
                                                      '26:03:04.005000'


# Generated at 2022-06-12 19:48:11.908788
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('09:08:07:123456')
    assert timedelta == datetime_module.timedelta(
        hours=9, minutes=8, seconds=7, microseconds=123456
    )



# Generated at 2022-06-12 19:48:15.055427
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=5, minutes=7, seconds=23, microseconds=1333333
    )) == '05:07:23.133333'


# Generated at 2022-06-12 19:48:25.183918
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1)) == \
           '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1,
                                                      microseconds=1)) \
           == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'


# Generated at 2022-06-12 19:48:28.894729
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=23, minutes=32, seconds=43,
                                  microseconds=123456)) == \
           '23:32:43.123456'


# Generated at 2022-06-12 19:48:34.533919
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:23:45.678901') == \
           datetime_module.timedelta(hours=1, minutes=23, seconds=45,
                                     microseconds=678901)

# Generated at 2022-06-12 19:49:07.249425
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=4567)) == \
           '01:02:03.004567'
    assert timedelta_format(datetime_module.timedelta(hours=-1, minutes=-2,
                                                      seconds=-3,
                                                      microseconds=-4567)) == \
           '-01:-02:-03.004567'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=0)) == \
           '01:02:03'

# Generated at 2022-06-12 19:49:14.851991
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == (
        '00:00:00.000000'
    )
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == (
        '00:00:01.000000'
    )
    assert timedelta_format(datetime_module.timedelta(milliseconds=1)) == (
        '00:00:00.001000'
    )
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == (
        '00:00:00.000001'
    )

# Generated at 2022-06-12 19:49:27.580949
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(
        hours=1
    )
    assert timedelta_parse('1:01:00.000000') == datetime_module.timedelta(
        minutes=61
    )
    assert timedelta_parse('0:59:59.999999') == datetime_module.timedelta(
        minutes=59,
        seconds=59,
        microseconds=999999,
    )
    assert timedelta_parse('0:09:59.999999') == datetime_module.timedelta(
        seconds=599,
        microseconds=999999,
    )

# Generated at 2022-06-12 19:49:31.709797
# Unit test for function timedelta_format
def test_timedelta_format():
    a_timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                            microseconds=123456)
    assert timedelta_format(a_timedelta) == '01:02:03.123456'



# Generated at 2022-06-12 19:49:42.033696
# Unit test for function timedelta_format
def test_timedelta_format():
    for i in range(1, 1000):
        delta = datetime_module.timedelta(microseconds=i)
        assert timedelta_parse(timedelta_format(delta)) == delta

    delta = datetime_module.timedelta(hours=10, minutes=9, seconds=8,
                                      microseconds=7)
    assert timedelta_parse(timedelta_format(delta)) == delta


if sys.version_info[0] == 2:
    import itertools
    import functools

    class _Empty(object):
        """
        A helper class to make default arguments of iterators immutable.
        """
        def __init__(self, value):
            self.value = value

        def __iter__(self):
            return self

        def __next__(self):
            raise StopIteration

# Generated at 2022-06-12 19:49:49.277756
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.060000') == \
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=60000)
    assert timedelta_parse('2:04:06.080000') == \
        datetime_module.timedelta(hours=2, minutes=4, seconds=6,
                                  microseconds=80000)



# Generated at 2022-06-12 19:49:57.592653
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:50:07.353702
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:01:00.000001') == datetime_module.timedelta(
        minutes=1, seconds=1, microseconds=1
    )
    assert timedelta_parse('00:01:00.123456') == datetime_module.timedelta(
        minutes=1, seconds=0, microseconds=123456
    )
    assert timedelta_parse('01:10:30.123456') == datetime_module.timedelta(
        hours=1, minutes=10, seconds=30, microseconds=123456
    )

# Generated at 2022-06-12 19:50:14.709660
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == \
        '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
        '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=1)) == \
        '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(minutes=1,
                                                      microseconds=1)) == \
        '00:01:00.000001'

# Generated at 2022-06-12 19:50:19.080606
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=10, minutes=2,
                                                     seconds=3)) == \
           '10:02:03.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1000)) == \
           '00:00:00.001000'
    assert timedelta_format(datetime_module.timedelta(microseconds=10)) == \
           '00:00:00.000010'



# Generated at 2022-06-12 19:51:10.179157
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(1, 1.2)) == \
           '0000-00-00 00:00:01.001200'
    assert timedelta_format(datetime_module.timedelta(1, 2.4)) == \
           '0000-00-00 00:00:02.002400'

# Generated at 2022-06-12 19:51:17.660444
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1))) == datetime_module.timedelta(hours=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(minutes=1))) == datetime_module.timedelta(minutes=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=1))) == datetime_module.timedelta(seconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(microseconds=1))) == datetime_module.timedelta(microseconds=1)


try:
    from contextlib import nullcontext
except ImportError: # Python 3.6
    from contextlib import ExitStack as null

# Generated at 2022-06-12 19:51:23.389825
# Unit test for function timedelta_format
def test_timedelta_format():
    from .test_turtle_simulate import test_turtle_simulate
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=234,
    )) == '01:02:03.000234'
    assert timedelta_parse(timedelta_format(
        test_turtle_simulate.simulation_duration
    )) == test_turtle_simulate.simulation_duration



# Generated at 2022-06-12 19:51:33.317537
# Unit test for function timedelta_format
def test_timedelta_format():
    from .cache_key import cache_key

# Generated at 2022-06-12 19:51:36.568672
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:02:03.123456') == datetime_module.timedelta(
        hours=1,
        minutes=2,
        seconds=3,
        microseconds=123456
    )

# Generated at 2022-06-12 19:51:47.095544
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, microseconds=1)) == '00:00:00.000001'

# Generated at 2022-06-12 19:51:50.418714
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=23, minutes=58, seconds=40,
                                  microseconds=123456)
    ) == '23:58:40.123456'


# Generated at 2022-06-12 19:51:59.992117
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=10)) == '00:00:10.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=12, microseconds=123456)) == '00:00:12.123456'
    assert timedelta_format(datetime_module.timedelta(minutes=5, seconds=12, microseconds=123456)) == '00:05:12.123456'
    assert timedelta_format(datetime_module.timedelta(hours=4, minutes=5, seconds=12, microseconds=123456)) == '04:05:12.123456'


# Generated at 2022-06-12 19:52:10.106623
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                  '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1.123)) == \
                                  '00:00:01.123000'
    assert timedelta_format(datetime_module.timedelta(seconds=60)) == \
                                  '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=3660)) == \
                                  '01:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=3660.123)) == \
                                  '01:01:00.123000'



# Generated at 2022-06-12 19:52:17.304983
# Unit test for function timedelta_parse
def test_timedelta_parse():
    td = timedelta_parse('00:30:05.123456')
    assert td.seconds == 1805 and td.microseconds == 123456
    assert td == datetime_module.timedelta(hours=0, minutes=30,
                                           seconds=5, microseconds=123456)

    td = timedelta_parse('1:1:1.1')
    assert td.seconds == 3661 and td.microseconds == 100000
    assert td == datetime_module.timedelta(hours=1, minutes=1,
                                           seconds=1, microseconds=100000)

# Generated at 2022-06-12 19:53:14.279315
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import nose.tools as tools
    from collections import namedtuple
    Sample = namedtuple('Sample', ['s', 'timedelta'])
    samples = [
        Sample('1:01:01:01.001000', datetime_module.timedelta(
            hours=1, minutes=1, seconds=1, microseconds=1000)),
        Sample('02:02:02.000100', datetime_module.timedelta(
            hours=2, minutes=2, seconds=2, microseconds=100)),
        Sample('00:00:01.000001', datetime_module.timedelta(
            seconds=1, microseconds=1)),
    ]

    for sample in samples:
        tools.eq_(timedelta_parse(sample.s), sample.timedelta)



# Generated at 2022-06-12 19:53:23.954969
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert (
        timedelta_format(datetime_module.timedelta(microseconds=1)) ==
        '00:00:00.000001'
    )
    assert (
        timedelta_format(datetime_module.timedelta(milliseconds=1)) ==
        '00:00:00.001000'
    )



# Generated at 2022-06-12 19:53:33.020941
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(milliseconds=1)) == '00:00:00.001000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'

# Generated at 2022-06-12 19:53:40.812236
# Unit test for function timedelta_parse
def test_timedelta_parse():

    # The `timedelta_parse` function with these arguments should return the
    # corresponding `datetime.timedelta`:
    test_cases = [
        ('00:00:00.000000', datetime_module.timedelta(seconds=0)),
        ('12:00:00.000000', datetime_module.timedelta(hours=12)),
        ('00:34:56.123456', datetime_module.timedelta(minutes=34, seconds=56,
                                                      microseconds=123456))
    ]

    for i, (time_string, timedelta_) in enumerate(test_cases):
        assert timedelta_ == timedelta_parse(time_string)
        assert time_string == timedelta_format(timedelta_)

    print('timedelta_parse passed unit test.')

# Generated at 2022-06-12 19:53:44.249954
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )) == '01:02:03.000004'



# Generated at 2022-06-12 19:53:51.670067
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(
        hours=23, minutes=59, seconds=59, microseconds=999999
    )
    assert timedelta_format(timedelta) == '23:59:59.999999'


if PY3:
    def get_timezone(dt):
        return dt.tzinfo
else:
    def get_timezone(dt):
        return (dt.tzinfo and dt.tzinfo.tzname(dt)) or None

# Generated at 2022-06-12 19:53:58.740939
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(
        microseconds=0
    )
    assert timedelta_parse('00:00:00.999999') == datetime_module.timedelta(
        microseconds=999999
    )
    assert timedelta_parse('00:00:00.999999') == datetime_module.timedelta(
        microseconds=999999
    )
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.000000') == datetime

# Generated at 2022-06-12 19:54:07.168881
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == \
         '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
         '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
         '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
         '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
         '00:00:00.000001'


# Generated at 2022-06-12 19:54:12.811815
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta_string = '1:2:3.456000'
    assert timedelta_format(timedelta_parse(timedelta_string)) == \
                                                             timedelta_string
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=5))) == datetime_module.timedelta(hours=5)

# Generated at 2022-06-12 19:54:13.966951
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'

