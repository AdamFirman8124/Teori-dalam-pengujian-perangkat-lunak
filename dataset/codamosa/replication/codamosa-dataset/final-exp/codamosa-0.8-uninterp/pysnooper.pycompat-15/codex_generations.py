

# Generated at 2022-06-12 19:46:14.950116
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=3, minutes=4, seconds=5,
                                          microseconds=123456)
    assert timedelta_format(timedelta) == '03:04:05.123456'


# Generated at 2022-06-12 19:46:16.990076
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )) == '01:02:03.000004'



# Generated at 2022-06-12 19:46:25.241961
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=2)) == '02:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=23)) == '23:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=24)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=48)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=2, minutes=15)) == \
                            '02:15:00.000000'
    assert timedelta_

# Generated at 2022-06-12 19:46:29.384741
# Unit test for function timedelta_format
def test_timedelta_format():
    for input in range(-20, 20):
        input = float(input)
        timedelta = datetime_module.timedelta(seconds=input)
        round_trip = timedelta_parse(timedelta_format(timedelta))
        assert round_trip == timedelta, (input, timedelta, round_trip)



# Generated at 2022-06-12 19:46:32.931111
# Unit test for function timedelta_parse
def test_timedelta_parse():
    s = '00:00:35.009528'
    assert timedelta_parse(s) == datetime_module.timedelta(seconds=35,
                                           microseconds=9528)

# Generated at 2022-06-12 19:46:41.119382
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=4, minutes=3,
                                                      seconds=2,
                                                      microseconds=5)) == '04:03:02.000005'
    assert timedelta_format(datetime_module.timedelta(hours=4, minutes=3,
                                                      seconds=2,
                                                      microseconds=999999)) == '04:03:02.999999'
    assert timedelta_format(datetime_module.timedelta(hours=0, minutes=0,
                                                      seconds=0,
                                                      microseconds=123456)) == '00:00:00.123456'



# Generated at 2022-06-12 19:46:45.841716
# Unit test for function timedelta_format
def test_timedelta_format():
    for delta in range(0, 24*60*60*1000000, 5000):
        assert timedelta_format(datetime_module.timedelta(microseconds=delta)) == \
               time_isoformat(datetime_module.time(hour=0, minute=0, second=0,
                                                   microsecond=delta),
                              timespec='microseconds')


# Generated at 2022-06-12 19:46:57.675759
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=1))) == datetime_module.timedelta(seconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=1, seconds=1))) == datetime_module.timedelta(days=1, seconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=2020, seconds=1))) == datetime_module.timedelta(days=2020, seconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=2020, seconds=1, microseconds=1))) == datetime_module.timedelta(days=2020, seconds=1, microseconds=1)




# Generated at 2022-06-12 19:47:08.683682
# Unit test for function timedelta_parse
def test_timedelta_parse():

    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()

    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        hours=1
    )

    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(
        minutes=1
    )

    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1
    )

    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )

    assert timedelta_parse('00:00:00.111111') == datetime_module.timedelta(
        microseconds=11
    )

# Generated at 2022-06-12 19:47:12.280444
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=12, minutes=24, seconds=13,
                                          microseconds=14)
    assert timedelta_format(timedelta) == '12:24:13.000014'



# Generated at 2022-06-12 19:47:28.095549
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta in (
        datetime_module.timedelta(hours=1),
        datetime_module.timedelta(hours=3, minutes=5),
        datetime_module.timedelta(hours=7, minutes=12, seconds=56,
                                  microseconds=340000),
        datetime_module.timedelta(hours=0)
    ):
        formatted = timedelta_format(timedelta)
        assert isinstance(formatted, str)
        parsed = timedelta_parse(formatted)
        assert parsed == timedelta


# Code stolen from six to get `zip_longest`, which is now `zip` in Python 3
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

# Generated at 2022-06-12 19:47:37.597246
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(microseconds=10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(microseconds=100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(microseconds=1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(microseconds=10000)

# Generated at 2022-06-12 19:47:41.897103
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=23,
                                                      minutes=59,
                                                      seconds=59,
                                                      microseconds=999999)) == '23:59:59.999999'


# Generated at 2022-06-12 19:47:50.797530
# Unit test for function timedelta_format
def test_timedelta_format():
    def time_roundtrip(x):
        assert x == timedelta_parse(timedelta_format(x))

    import pytest
    time_roundtrip(datetime_module.timedelta(hours=1))
    time_roundtrip(datetime_module.timedelta(minutes=1))
    time_roundtrip(datetime_module.timedelta(seconds=1))
    time_roundtrip(datetime_module.timedelta(milliseconds=1))
    time_roundtrip(datetime_module.timedelta(microseconds=1))
    with pytest.raises(NotImplementedError):
        time_isoformat(datetime_module.time(0, 0, 0), timespec='autodetect')



# Generated at 2022-06-12 19:48:01.696363
# Unit test for function timedelta_format
def test_timedelta_format():
    def test(s, timedelta):
        assert timedelta_format(timedelta) == s
        assert timedelta_parse(s) == timedelta
    test(
        '1:02:03.004456',
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=456)
    )
    test(
        '23:59:59.999456',
        datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                                  microseconds=999456)
    )
    test(
        '00:00:00.000000',
        datetime_module.timedelta(hours=0, minutes=0, seconds=0,
                                  microseconds=0)
    )

# Generated at 2022-06-12 19:48:08.961865
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1, microseconds=2)) == '00:00:01.000002'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1, microseconds=1)) == '00:01:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'

# Generated at 2022-06-12 19:48:18.026736
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=4)
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta
    # Make sure it fails when it should:
    with pytest.raises(ValueError):
        timedelta_parse('1:2:3')


if PY3:
    exc_message = lambda exc: exc.args[0] if exc.args else ''
else:
    exc_message = lambda exc: exc.message


try:
    from contextlib import nullcontext
except ImportError:
    from contextlib import contextmanager
    @contextmanager
    def nullcontext():
        yield



# Generated at 2022-06-12 19:48:26.961998
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for timedelta in (
        datetime_module.timedelta(seconds=0.123456),
        datetime_module.timedelta(days=1, seconds=0.123456),
        datetime_module.timedelta(seconds=1000000000.123456),
        datetime_module.timedelta(seconds=1000000000.123456,
                                  microseconds=1)
    ):
        assert timedelta == timedelta_parse(timedelta_format(timedelta))


try:
    from pathlib import Path
except ImportError:
    Path = None


try:
    import pathlib
except ImportError:
    pathlib = None


try:
    import importlib.resources as resources_package
except ImportError:
    resources_package = None



# Generated at 2022-06-12 19:48:34.887018
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=23,
                                                      minutes=59,
                                                      seconds=59,
                                                      microseconds=999999)) \
                                                      == '23:59:59.999999'
    assert timedelta_format(datetime_module.timedelta(minutes=1, seconds=1)) \
                                                      == '00:01:01.000000'



# Generated at 2022-06-12 19:48:43.941563
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2)) == \
                             '01:02:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=3.3)) == \
                             '01:00:03.300000'
    assert timedelta_format(datetime_module.timedelta(minutes=1,
                             microseconds=999999.999999)) == '00:01:00.999999'
    assert timedelta_format(datetime_module.timedelta(seconds=1.5,
                             milliseconds=1)) == '00:00:01.501000'


# Generated at 2022-06-12 19:49:11.509509
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(0, 0, 1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(0, 1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(0, 0, 1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(days=1)) == \
           '24:00:00.000000'



# Generated at 2022-06-12 19:49:24.544452
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0.0000000001') == datetime_module.timedelta(0, 0.0000000001)
    assert timedelta_parse('0:0:0.1') == datetime_module.timedelta(0, 0, 100000)

# Generated at 2022-06-12 19:49:32.412249
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('1:02:03.000000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3
    )
    assert timedelta_parse('0:00:00.099') == datetime_module.timedelta(
        microseconds=99000
    )
    assert timedelta_parse('0:00:00.000099') == datetime_module.timedelta(
        microseconds=99
    )
    assert timedelta_parse('23:59:59.999999') == datetime_module.timedelta(
        days=1, microseconds=-1
    )

# Generated at 2022-06-12 19:49:42.924208
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1)) == '24:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=2)) == '48:00:00.000000'

# Generated at 2022-06-12 19:49:52.259166
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(1, 2, 3)) == \
           '00:00:01.000002'
    assert timedelta_format(datetime_module.timedelta(1, 2, 30000)) == \
           '00:00:01.030000'
    assert timedelta_format(datetime_module.timedelta(1, 2, 300000)) == \
           '00:00:01.300000'
    assert timedelta_format(datetime_module.timedelta(1, 2, 3000000)) == \
           '00:00:01.3'



# Generated at 2022-06-12 19:49:59.516679
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == \
           datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:01.000000') == \
           datetime_module.timedelta(seconds=1)
    assert timedelta_parse('00:00:01.000001') == \
           datetime_module.timedelta(seconds=1, microseconds=1)
    assert timedelta_parse('01:00:00.000000') == \
           datetime_module.timedelta(hours=1)

# Generated at 2022-06-12 19:50:06.683525
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                                 '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1.5)) == \
                                                                 '00:00:01.500000'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=-2)) == \
                                                                 '00:59:58.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=-3661)) == \
                                                                 '-01:01:01.000000'



# Generated at 2022-06-12 19:50:08.709231
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=15, minutes=14,
                                                      seconds=13,
                                                      microseconds=1234)) ==\
                             '15:14:13.001234'



# Generated at 2022-06-12 19:50:14.375738
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == \
           datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.123456') == \
           datetime_module.timedelta(microseconds=123456)
    assert timedelta_parse('00:00:00.999999') == \
           datetime_module.timedelta(microseconds=999999)
    assert timedelta_parse('00:00:01.000000') == \
           datetime_module.timedelta(seconds=1)

# Generated at 2022-06-12 19:50:18.080432
# Unit test for function timedelta_parse
def test_timedelta_parse():
    time_delta = timedelta_parse('14:32:27.074212')
    assert time_delta.total_seconds() == (
        (14 * 60 + 32) * 60 + 27 + 0.074212
    )



if PY2:
    from cPickle import Pickler, Unpickler
else:
    from pickle import Pickler, Unpickler



# Generated at 2022-06-12 19:50:46.202757
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=-1)) == \
           '-01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1)) == \
           '+01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=5, minutes=6, seconds=7, microseconds=8
    )) == '05:06:07.000008'



# Generated at 2022-06-12 19:50:51.013840
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('1:1:1.001000') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=1000
    )

# Generated at 2022-06-12 19:50:59.060844
# Unit test for function timedelta_parse
def test_timedelta_parse():
    # Test for valid timedeltas
    assert timedelta_format(timedelta_parse('0:00:00.000001')) == '00:00:00.000001'
    assert timedelta_format(timedelta_parse('0:01:00.000001')) == '00:01:00.000001'
    assert timedelta_format(timedelta_parse('1:18:00.000001')) == '01:18:00.000001'
    assert timedelta_format(timedelta_parse('12:34:56.000001')) == '12:34:56.000001'
    assert timedelta_format(timedelta_parse('1:2:3.4')) == '01:02:03.004000'

    # Test for zeros

# Generated at 2022-06-12 19:51:09.895061
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=0,
                                                      minutes=0,
                                                      seconds=0,
                                                      microseconds=0)) == \
                                                      '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=0,
                                                      minutes=0,
                                                      seconds=0,
                                                      microseconds=1)) == \
                                                      '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=0,
                                                      minutes=0,
                                                      seconds=1,
                                                      microseconds=0)) == \
                                                      '00:00:01.000000'

# Generated at 2022-06-12 19:51:15.137669
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.datetime(2019, 1, 1) - \
                datetime_module.datetime(0, 0, 0)
    assert timedelta_format(timedelta) == '072:00:00.000000'
    delta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                      microseconds=4)
    assert timedelta_format(delta) == '01:02:03.000004'



# Generated at 2022-06-12 19:51:17.629975
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timestamp = '15:20:58.663011'
    assert timedelta_parse(timestamp) == (
        datetime_module.timedelta(hours=15, minutes=20, seconds=58,
                                  microseconds=663011)
    )



# Generated at 2022-06-12 19:51:26.459168
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == \
                                                      '01:02:03.000004'
    assert timedelta_format(datetime_module.timedelta(hours=3, minutes=25,
                                                      seconds=159,
                                                      microseconds=853)) == \
                                                      '03:25:159.000853'
    assert timedelta_format(datetime_module.timedelta(hours=23, minutes=59,
                                                      seconds=59,
                                                      microseconds=999999)) == \
                                                      '23:59:59.999999'

    # Regression test for #56

# Generated at 2022-06-12 19:51:29.161297
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('22:33:44.123123') == datetime_module.timedelta(
        hours=22, minutes=33, seconds=44, milliseconds=123, microseconds=123
    )

# Generated at 2022-06-12 19:51:38.879626
# Unit test for function timedelta_format
def test_timedelta_format():
    assert (
        timedelta_format(
            datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                         microseconds=123456)
        ) ==
        '23:59:59.123456'
    )
    assert (
        timedelta_format(
            datetime_module.timedelta(hours= 5, minutes= 4, seconds= 3,
                         microseconds=   2)
        ) ==
        '05:04:03.000002'
    )
    assert (
        timedelta_format(
            datetime_module.timedelta(hours= 0, minutes= 0, seconds= 0,
                         microseconds=   0)
        ) ==
        '00:00:00.000000'
    )

# Generated at 2022-06-12 19:51:44.933447
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
        '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=700000)) == \
        '00:00:01.700000'
    assert timedelta_format(datetime_module.timedelta(minutes=1,
                                                      microseconds=60000)) == \
        '00:01:00.060000'
    assert timedelta_format(datetime_module.timedelta(minutes=1,
                                                      microseconds=700000)) == \
        '00:01:00.700000'

# Generated at 2022-06-12 19:52:43.524386
# Unit test for function timedelta_format
def test_timedelta_format():
    from . import assert_equal
    td = datetime_module.timedelta(hours=3, minutes=15, seconds=30,
                                   microseconds=500500)
    assert_equal(timedelta_format(td), '03:15:30.500500')


# Generated at 2022-06-12 19:52:50.751613
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=0, seconds=0)) == \
                                                                      '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=0, seconds=1)) == \
                                                                      '00:00:01.00000'
    assert timedelta_format(datetime_module.timedelta(days=0, seconds=60)) == \
                                                                      '00:01:00.00000'
    assert timedelta_format(datetime_module.timedelta(days=0, seconds=3600)) == \
                                                                      '01:00:00.00000'

# Generated at 2022-06-12 19:52:58.183377
# Unit test for function timedelta_parse

# Generated at 2022-06-12 19:53:02.531287
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=5, minutes=3, seconds=2,
                                          microseconds=900)
    assert timedelta_format(timedelta) == '05:03:02.000900'



# Generated at 2022-06-12 19:53:05.647262
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=10, minutes=11,
                                                      seconds=12,
                                                      microseconds=123456)) == \
           '10:11:12.123456'



# Generated at 2022-06-12 19:53:10.895719
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('03:20:30.456789') == datetime_module.timedelta(
        hours=3, minutes=20, seconds=30, milliseconds=456,
        microseconds=789000
    )
    assert timedelta_parse('03:20:30.456') == datetime_module.timedelta(
        hours=3, minutes=20, seconds=30, milliseconds=456
    )
    assert timedelta_parse('03:20:30') == datetime_module.timedelta(
        hours=3, minutes=20, seconds=30
    )

# Generated at 2022-06-12 19:53:18.088632
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=-1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=-1, hours=5)) == '05:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=-1, hours=5, minutes=4)) == '05:04:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=-1, hours=5, minutes=4, seconds=3)) == '05:04:03.000000'
    assert timedelta_format(datetime_module.timedelta(days=-1, hours=5, minutes=4, seconds=3, microseconds=2)) == '05:04:03.000002'

# Generated at 2022-06-12 19:53:29.105023
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for timedelta in (
        datetime_module.timedelta(seconds=60),
        datetime_module.timedelta(seconds=60.1),
        datetime_module.timedelta(minutes=60),
        datetime_module.timedelta(minutes=60.1),
        datetime_module.timedelta(hours=60),
        datetime_module.timedelta(hours=60.1),
        datetime_module.timedelta(hours=120),
        datetime_module.timedelta(days=60),
        datetime_module.timedelta(days=60.1),
    ):
        assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:53:39.524510
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:23:45.123456') == datetime_module.timedelta(hours=1, minutes=23, seconds=45, microseconds=123456)
    assert timedelta_parse('01:23:45.012345') == datetime_module.timedelta(hours=1, minutes=23, seconds=45, microseconds=12345)
    assert timedelta_parse('01:23:45.001234') == datetime_module.timedelta(hours=1, minutes=23, seconds=45, microseconds=1234)
    assert timedelta_parse('01:23:45.000123') == datetime_module.timedelta(hours=1, minutes=23, seconds=45, microseconds=123)
    assert timedelta_parse('01:23:45.000012') == dat

# Generated at 2022-06-12 19:53:50.007756
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=4)
    assert timedelta_format(timedelta) == '01:02:03.000004'

    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3)
    assert timedelta_format(timedelta) == '01:02:03.000000'

    timedelta = datetime_module.timedelta(hours=0, minutes=0, seconds=0,
                                          microseconds=0)
    assert timedelta_format(timedelta) == '00:00:00.000000'


# Generated at 2022-06-12 19:55:45.584456
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
                                 datetime_module.timedelta(days=1))) == \
                                                                 datetime_module.timedelta(days=1)
    assert timedelta_parse(timedelta_format(
                                 datetime_module.timedelta(seconds=1))) == \
                                                                 datetime_module.timedelta(seconds=1)
    assert timedelta_parse(timedelta_format(
                                 datetime_module.timedelta(seconds=1,
                                                          microseconds=1))) == \
                                                                 datetime_module.timedelta(seconds=1,
                                                                                          microseconds=1)

# Generated at 2022-06-12 19:55:54.567842
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(days=1))
    ) == datetime_module.timedelta(days=1)
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(days=1, hours=1))
    ) == datetime_module.timedelta(days=1, hours=1)
    assert timedelta_parse(
        timedelta_format(datetime_module.timedelta(days=1, hours=1, minutes=1))
    ) == datetime_module.timedelta(days=1, hours=1, minutes=1)

# Generated at 2022-06-12 19:56:01.440534
# Unit test for function timedelta_parse
def test_timedelta_parse():
    s =  '01:09:08.128000'
    timedelta = datetime_module.timedelta(hours=1, minutes=9, seconds=8,
                                          microseconds=128000)
    assert timedelta == timedelta_parse(s)
    assert s == timedelta_format(timedelta)


datetime_format = (
    datetime_module.datetime.isoformat if PY3
    else datetime_module.datetime.strftime
)