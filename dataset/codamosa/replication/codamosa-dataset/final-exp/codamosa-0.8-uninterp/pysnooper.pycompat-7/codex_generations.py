

# Generated at 2022-06-12 19:46:18.741855
# Unit test for function timedelta_format
def test_timedelta_format():
    one_hour_delta = datetime_module.timedelta(hours=1)
    one_minute_delta = datetime_module.timedelta(minutes=1)
    one_second_delta = datetime_module.timedelta(seconds=1)
    one_millisecond_delta = datetime_module.timedelta(milliseconds=1)
    one_microsecond_delta = datetime_module.timedelta(microseconds=1)

    assert '00:00:00.000000' == timedelta_format(datetime_module.timedelta(0))
    assert '01:00:00.000000' == timedelta_format(one_hour_delta)
    assert '00:01:00.000000' == timedelta_format(one_minute_delta)

# Generated at 2022-06-12 19:46:25.653954
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(
        microseconds=100)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(
        microseconds=10000)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1)
    assert timedelta_parse('00:02:00.000000') == datetime_module.timedelta(
        minutes=2)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        hours=1)

# Generated at 2022-06-12 19:46:34.050893
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=3,
                                                                      minutes=10,
                                                                      seconds=5,
                                                                      microseconds=0))) == \
                                                                      datetime_module.timedelta(hours=3,
                                                                      minutes=10,
                                                                      seconds=5,
                                                                      microseconds=0)


# Generated at 2022-06-12 19:46:43.366551
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1, 100)) == '00:00:01.000100'
    assert timedelta_format(datetime_module.timedelta(12, 5100)) == '00:00:12.005100'
    assert timedelta_format(datetime_module.timedelta(123, 100500)) == '00:02:03.100500'
    assert timedelta_format(datetime_module.timedelta(1234, 100500)) == '00:20:34.100500'
    assert timedelta_format(datetime_module.timedelta(12345, 100500)) == '03:25:45.100500'


# Unit test

# Generated at 2022-06-12 19:46:55.403500
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('01:00:01.000000') == datetime_module.timedelta(hours=1, seconds=1)
    assert timedelta_parse('00:00:01.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:01.100000')

# Generated at 2022-06-12 19:47:08.154252
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        0, 0, 1
    )
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(
        0, 0, 10
    )
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(
        0, 0, 100
    )
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(
        0, 0, 1000
    )
    assert timedelta_parse('00:00:00.100000') == datetime_module.tim

# Generated at 2022-06-12 19:47:11.685118
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:05:10.987654') == datetime_module.timedelta(
        hours=1, minutes=5, seconds=10, microseconds=987654
    )

# Generated at 2022-06-12 19:47:22.517602
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
                           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                           '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1,
                                                      seconds=1,
                                                      microseconds=1)) == \
                           '01:01:01.000001'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=100, seconds=100, microseconds=100))

# Generated at 2022-06-12 19:47:27.116682
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:10.123456') == datetime_module.timedelta(
        seconds=10, microseconds=123456
    )
    assert timedelta_parse('01:02:30.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=30, microseconds=123456
    )
    assert timedelta_parse('00:05:00') == datetime_module.timedelta(
        minutes=5
    )

# Generated at 2022-06-12 19:47:33.897659
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03:04:05') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=40005)
    assert timedelta_parse('01:02:03:4:5') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=40005)
    assert timedelta_parse('01:02:03.4:5') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=40005)

# Generated at 2022-06-12 19:47:50.632070
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == \
           datetime_module.timedelta()
    assert timedelta_parse('1:00:00.000000') == \
           datetime_module.timedelta(hours=1)
    assert timedelta_parse('1:2:3.000004') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=4)
    assert timedelta_parse('0:0:0.123456') == \
           datetime_module.timedelta(microseconds=123456)

# Generated at 2022-06-12 19:47:53.029879
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:36:04.584128') == \
           datetime_module.timedelta(hours=0, minutes=36,
                                     seconds=4, microseconds=584128)

# Generated at 2022-06-12 19:47:57.732861
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.000004') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )
    assert timedelta_parse('01:02:03') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3
    )
    assert timedelta_parse('01:02') == datetime_module.timedelta(
        hours=1, minutes=2
    )
    assert timedelta_parse('01') == datetime_module.timedelta(
        hours=1
    )

# Generated at 2022-06-12 19:48:06.253244
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    ))) == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )


if PY3:

    def iteritems(d):
        return iter(d.items())

    def itervalues(d):
        return iter(d.values())

    def iterkeys(d):
        return iter(d.keys())

else:

    def iteritems(d):
        return d.iteritems()

    def itervalues(d):
        return d.itervalues()

    def iterkeys(d):
        return d.iterkeys()



# Generated at 2022-06-12 19:48:11.818012
# Unit test for function timedelta_parse
def test_timedelta_parse():
    def assert_is_timedelta(timedelta, string):
        assert timedelta == timedelta_parse(string), (
            'Error parsing timedelta: {!r} != {!r}'
            .format(timedelta, timedelta_parse(string))
        )

    assert_is_timedelta(datetime_module.timedelta(1),
                        timedelta_format(datetime_module.timedelta(1)))
    assert_is_timedelta(datetime_module.timedelta(0, 2),
                        timedelta_format(datetime_module.timedelta(0, 2)))
    assert_is_timedelta(datetime_module.timedelta(0, 0, 3),
                        timedelta_format(datetime_module.timedelta(0, 0, 3)))

# Generated at 2022-06-12 19:48:18.965369
# Unit test for function timedelta_parse
def test_timedelta_parse():

    assert timedelta_parse('00:00:00') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:01.000001') == datetime_module.timedelta(0, 1, 1)
    assert timedelta_parse('00:01:01.000001') == datetime_module.timedelta(0, 61, 1)
    assert timedelta_parse('01:01:01.000001') == datetime_module.timedelta(1, 3661, 1)

# Generated at 2022-06-12 19:48:24.954381
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=0, minutes=0,
                                                      seconds=0,
                                                      microseconds=-500)) == \
           '-00:00:00.000500'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=405060)) == \
           '01:02:03.405060'


# Generated at 2022-06-12 19:48:29.978257
# Unit test for function timedelta_format
def test_timedelta_format():
    '''
    Test that roundtripping a timedelta via `timedelta_format` results in the
    same `timedelta` object.
    '''
    for timedelta in (
        datetime_module.timedelta(0),
        datetime_module.timedelta(days=10),
        datetime_module.timedelta(hours=10, seconds=30, microseconds=400000),
        datetime_module.timedelta(minutes=1001),
        datetime_module.timedelta(days=1, minutes=1001, seconds=30,
                                  microseconds=400000),
    ):
        roundtripped_timedelta = timedelta_parse(timedelta_format(timedelta))

# Generated at 2022-06-12 19:48:34.330012
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('06:05:04.003000') == datetime_module.timedelta(
        hours=6, minutes=5, seconds=4, microseconds=3
    )



# Generated at 2022-06-12 19:48:41.443527
# Unit test for function timedelta_parse
def test_timedelta_parse():
    tests = [
        ('00:00:10.000000', datetime_module.timedelta(seconds=10)),
        ('00:01:10.000000', datetime_module.timedelta(minutes=1,
                                                      seconds=10)),
        ('01:01:10.000000', datetime_module.timedelta(hours=1,
                                                      minutes=1,
                                                      seconds=10)),
    ]
    for (input, expected) in tests:
        assert timedelta_parse(input) == expected



# Generated at 2022-06-12 19:48:56.542701
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:1:1.1') == datetime_module.timedelta(
        seconds=3661, microseconds=100000
    )
    assert timedelta_parse('1:1:1.123456') == datetime_module.timedelta(
        seconds=3661, microseconds=123456
    )

# Generated at 2022-06-12 19:49:00.145472
# Unit test for function timedelta_format
def test_timedelta_format():

    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'

    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                           '00:00:01.000000'



# Generated at 2022-06-12 19:49:09.745700
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
                       '00:00:00.000001'

    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                        microseconds=1)) == \
                       '00:00:01.000001'

    assert timedelta_format(datetime_module.timedelta(minutes=1,
                                                        seconds=1,
                                                        microseconds=1)) == \
                       '00:01:01.000001'


# Generated at 2022-06-12 19:49:11.548921
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=65)) == \
                  '00:01:05.000000'


# Generated at 2022-06-12 19:49:23.218580
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('4:12:32.5681368')) == \
        '04:12:32.568136'

try:
    from types import coroutine as coroutine_type
except ImportError:
    class coroutine_type(object): pass # Python 2.7

if PY3:
    from functools import reduce
    from collections.abc import MutableMapping as MutableMappingABC
else:
    from functools32 import reduce
    from collections import MutableMapping as MutableMappingABC

try:
    from importlib import reload as reload_module
except ImportError: # Python 2.7
    from imp import reload as reload_module

# Generated at 2022-06-12 19:49:32.130925
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(microseconds=10)

# Generated at 2022-06-12 19:49:35.540007
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456
    )) == '01:02:03.456000'



# Generated at 2022-06-12 19:49:39.138077
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:02:03.123456') == \
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=123456)


# Generated at 2022-06-12 19:49:41.172891
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(
        timedelta_parse('01:23:45.678901')
    ) == '01:23:45.678901'

# Generated at 2022-06-12 19:49:46.357484
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=2, hours=3, minutes=4,
                                          seconds=5, milliseconds=6,
                                          microseconds=7)
    assert timedelta_format(timedelta) == '50:04:05.006007'



# Generated at 2022-06-12 19:50:05.908363
# Unit test for function timedelta_parse
def test_timedelta_parse():
    td = timedelta_parse('1:23:45.678901')
    assert td.total_seconds() == 12345.678901
    assert timedelta_parse(timedelta_format(td)) == td


if hasattr(datetime_module.timedelta, 'total_seconds'):
    timedelta_total_seconds = datetime_module.timedelta.total_seconds
else:
    def timedelta_total_seconds(td):
        return (td.microseconds + 0.0 +
                (td.seconds + td.days * 24 * 3600) * 10 ** 6) / 10 ** 6

if PY3:
    from imp import reload
else:
    reload = reload # Python 2


# Generated at 2022-06-12 19:50:09.235613
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1, microseconds=2)) == '00:00:01.000002'


# Generated at 2022-06-12 19:50:12.889032
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('-1:02:03.123456') == datetime_module.timedelta(
        days=-1, hours=-2, minutes=-3, microseconds=-123456
    )

# Generated at 2022-06-12 19:50:22.129371
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.100000') == datetime_module.timedelta(microseconds=100000)
    assert timedelta_parse('00:00:00.100100') == datetime_module.timedelta(microseconds=100100)
    assert timedelta_parse('01:00:01.000000') == datetime_module.timedelta(seconds=3601)
    assert timedelta_parse('01:00:01.123456') == datetime_module.timedelta(seconds=3601, microseconds=123456)
    assert timedelta_parse('3600:01:01.000000') == datetime_module.timedelta(days=1, seconds=1)
   

# Generated at 2022-06-12 19:50:28.169776
# Unit test for function timedelta_parse
def test_timedelta_parse():
    test_cases = (
        ('1:02:03.123456', datetime_module.timedelta(hours=1, minutes=2,
                                                     seconds=3,
                                                     microseconds=123456)),
        ('0:00:03.123456', datetime_module.timedelta(seconds=3,
                                                     microseconds=123456)),
        ('1:02:03.000000', datetime_module.timedelta(hours=1, minutes=2,
                                                     seconds=3)),
        ('1:02:03', datetime_module.timedelta(hours=1, minutes=2, seconds=3)),
    )
    for s, result in test_cases:
        assert timedelta_parse(s) == result
        assert timedelta_format(result) == s
    assert timedelta_format

# Generated at 2022-06-12 19:50:37.335192
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=123)) == '00:00:00.000123'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=123)) == '00:00:01.000123'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'

# Generated at 2022-06-12 19:50:45.426859
# Unit test for function timedelta_parse
def test_timedelta_parse():

    def check_timedelta_parse(s):
        assert timedelta_parse(timedelta_format(timedelta_parse(s))) == s

    check_timedelta_parse('00:10:22.000000')
    check_timedelta_parse('00:10:22.100100')
    check_timedelta_parse('00:10:22.100100')
    check_timedelta_parse('00:10:22.100100')
    check_timedelta_parse('00:10:22.100100')
    check_timedelta_parse('00:10:22.100000')
    check_timedelta_parse('00:10:22.000001')
    check_timedelta_parse('00:10:22.000000')

# Generated at 2022-06-12 19:50:51.549374
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=1, hours=2, minutes=3,
                                          seconds=4, microseconds=567890)
    fmt = timedelta_format(timedelta)
    assert fmt == '47:03:04.056789'
    assert timedelta == timedelta_parse(fmt)


# Generated at 2022-06-12 19:50:59.479961
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:30:45.123456789') == datetime_module.timedelta(
        hours=1, minutes=30, seconds=45, microseconds=123456
    )


if hasattr(datetime_module.datetime, 'fromisoformat'):
    datetime_fromisoformat = datetime_module.datetime.fromisoformat
else:
    try:
        from dateutil.parser import parse as parse_datetime
    except ImportError:
        def parse_datetime(s):
            assert '.' in s, f'Can not parse a datetime without microseconds'
            return datetime_module.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%f')

# Generated at 2022-06-12 19:51:06.852177
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('05:03:02.007000') == datetime_module.timedelta(
        hours=5, minutes=3, seconds=2, milliseconds=7
    )


if PY3:
    from importlib import machinery
    import_module = machinery.SourceFileLoader(
        '', ''
    ).load_module
else:
    import imp
    import_module = imp.load_source if hasattr(imp, 'load_source') else imp.load_compiled

# Generated at 2022-06-12 19:51:33.316942
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('12:30:00.123456') == \
           datetime_module.timedelta(hours=12, minutes=30, seconds=0.123456)

test_timedelta_parse()

# Generated at 2022-06-12 19:51:39.489859
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=23, minutes=59,
                                          seconds=59, microseconds=999999)
    assert timedelta_format(timedelta) == '23:59:59.999999'

    timedelta = datetime_module.timedelta(days=2, hours=6, seconds=6,
                                          microseconds=6)
    assert timedelta_format(timedelta) == '54:00:06.000006'



# Generated at 2022-06-12 19:51:50.065700
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('00:00:01.000000')
    assert timedelta.total_seconds() == 1
    assert timedelta == datetime_module.timedelta(seconds=1)
    timedelta = timedelta_parse('00:00:01.000001')
    assert timedelta.total_seconds() == 1.000001
    assert timedelta == datetime_module.timedelta(seconds=1, microseconds=1)
    timedelta = timedelta_parse('00:00:01.123456')
    assert timedelta.total_seconds() == 1.123456
    assert timedelta == datetime_module.timedelta(seconds=1, microseconds=123456)
    timedelta = timedelta_parse('02:03:04.000000')

# Generated at 2022-06-12 19:51:59.956756
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for input in ('1:2:3.4', '01:02:03.4', '01:02:03.004', '1:2:3.400000'):
        assert timedelta_parse(input) == datetime_module.timedelta(
            hours=1, minutes=2, seconds=3, milliseconds=4
        )
    

if PY3:
    def zip_longest(*args, **kwargs):
        return zip(*args, **kwargs)
else:
    import itertools
    zip_longest = itertools.izip_longest


if PY3:
    import queue as queue_module
else:
    import Queue as queue_module

# Generated at 2022-06-12 19:52:10.387866
# Unit test for function timedelta_parse
def test_timedelta_parse():

    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(hours=1)

    assert timedelta_parse('1:00:00.000001') == datetime_module.timedelta(hours=1,
                                                                          microseconds=1)

    assert timedelta_parse('1:00:00.000010') == datetime_module.timedelta(hours=1,
                                                                          microseconds=10)

    assert timedelta_parse('1:00:00.000100') == datetime_module.timedelta(hours=1,
                                                                          microseconds=100)

    assert timedelta_parse('1:00:00.001000') == datetime_module.timedelta(hours=1,
                                                                          microseconds=1000)

   

# Generated at 2022-06-12 19:52:19.576306
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == \
           datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
                                            microseconds=1))) == \
           datetime_module.timedelta(microseconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
                                            microseconds=999))) == \
           datetime_module.timedelta(microseconds=999)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
                                            microseconds=1000))) == \
           datetime_module.timedelta(microseconds=1000)

# Generated at 2022-06-12 19:52:24.816108
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                          '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=9)) == \
                          '00:00:01.000009'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      seconds=1,
                                                      microseconds=9)) == \
                          '01:00:01.000009'



# Generated at 2022-06-12 19:52:32.289447
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.000000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3
    )
    assert timedelta_parse('01:02:03.000001') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=1
    )
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )



# Generated at 2022-06-12 19:52:33.953452
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                    '00:00:01.000000'

# Generated at 2022-06-12 19:52:44.629623
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(
        hours=1
    )
    assert timedelta_parse('1:02:00.000000') == datetime_module.timedelta(
        hours=1, minutes=2
    )
    assert timedelta_parse('1:02:03.000000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3
    )
    assert timedelta_parse('1:02:03.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )



# Generated at 2022-06-12 19:53:34.923843
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.04') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=4)



# Generated at 2022-06-12 19:53:39.936383
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta_format_results = {
        datetime_module.timedelta(): '00:00:00.000000',
        datetime_module.timedelta(days=1, seconds=2): '24:00:02.000000',
        datetime_module.timedelta(days=2, hours=3): '48:03:00.000000',
    }
    for timedelta, result in timedelta_format_results.items():
        assert timedelta_format(timedelta) == result


# Generated at 2022-06-12 19:53:51.749155
# Unit test for function timedelta_format
def test_timedelta_format():

    def assert_format(timedelta, string):
        assert timedelta_format(timedelta) == string
        assert timedelta_parse(string) == timedelta

    assert_format(datetime_module.timedelta(), '00:00:00.000000')
    assert_format(datetime_module.timedelta(seconds=.1), '00:00:00.100000')
    assert_format(datetime_module.timedelta(seconds=10), '00:00:10.000000')
    assert_format(datetime_module.timedelta(minutes=1), '00:01:00.000000')
    assert_format(datetime_module.timedelta(minutes=1, seconds=1),
                  '00:01:01.000000')

# Generated at 2022-06-12 19:53:58.780634
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=2, minutes=12, seconds=34, microseconds=567_890
    )) == '02:12:34.567890'
    assert timedelta_format(datetime_module.timedelta(
        minutes=12, seconds=34, microseconds=567_890
    )) == '00:12:34.567890'
    assert timedelta_format(datetime_module.timedelta(
        seconds=34, microseconds=567_890
    )) == '00:00:34.567890'

# Generated at 2022-06-12 19:54:07.658097
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == \
                                                    '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=3)) == \
                                                    '00:00:03.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=70)) == \
                                                    '00:01:10.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=4)) == \
                                                    '00:04:00.000000'
    assert timedelta_format(datetime_module.timedelta(
                                                minutes=3, seconds=50
                                            )) == '00:03:50.000000'

# Generated at 2022-06-12 19:54:10.926999
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=12345678.901234)) \
           == '03:25:45.901234'


# Generated at 2022-06-12 19:54:19.102107
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:54:23.969835
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(hours=5, seconds=15,
                                                   microseconds=123456))
    ) == datetime_module.timedelta(hours=5, seconds=15, microseconds=123456)

# Generated at 2022-06-12 19:54:29.229479
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=4)
    ) == '01:02:03.000004'
    assert timedelta_format(
        datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                                  microseconds=999999)
    ) == '23:59:59.999999'



# Generated at 2022-06-12 19:54:36.388418
# Unit test for function timedelta_parse
def test_timedelta_parse():
    cases = [
        ('00:00:00.000000', 0),
        ('00:00:00.123456', 123456),
        ('00:00:01.000000', 1000000),
        ('00:01:00.000000', 1000000 * 60),
        ('01:00:00.000000', 1000000 * 60 * 60),
    ]
    for input, desired_result in cases:
        result = timedelta_parse(input)
        assert result.total_seconds() == desired_result / 1000000.

