

# Generated at 2022-06-12 19:46:10.860736
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        hours=1
    )
    assert timedelta_parse(' 00:00:00.000000 ') == datetime_module.timedelta(0)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        hours=1
    )
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(
        hours=1
    )

# Generated at 2022-06-12 19:46:14.631423
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:02:03.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )



# Generated at 2022-06-12 19:46:20.943964
# Unit test for function timedelta_parse
def test_timedelta_parse():
    seconds = timedelta_parse('0:00:00.000000')
    assert seconds == datetime_module.timedelta(seconds=0)
    seconds = timedelta_parse('0:00:01.000000')
    assert seconds == datetime_module.timedelta(seconds=1)
    seconds = timedelta_parse('0:00:59.000000')
    assert seconds == datetime_module.timedelta(seconds=59)
    seconds = timedelta_parse('0:01:00.000000')
    assert seconds == datetime_module.timedelta(seconds=60)
    seconds = timedelta_parse('0:59:00.000000')
    assert seconds == datetime_module.timedelta(seconds=60*59)
    seconds = timedelta_parse('1:00:00.000000')
    assert seconds == dat

# Generated at 2022-06-12 19:46:29.305575
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('68:40:40.123456') == datetime_module.timedelta(
        hours=68, minutes=40, seconds=40, microseconds=123456)
    assert timedelta_parse('3:40:40.123456') == datetime_module.timedelta(
        hours=3, minutes=40, seconds=40, microseconds=123456)
    assert timedelta_parse('00:40:40.123456') == datetime_module.timedelta(
        minutes=40, seconds=40, microseconds=123456)
    assert timedelta_parse('00:00:40.123456') == datetime_module.timedelta(
        seconds=40, microseconds=123456)
    assert timedelta_parse('00:00:00.123456') == datetime_module.tim

# Generated at 2022-06-12 19:46:32.930512
# Unit test for function timedelta_format
def test_timedelta_format():
    td = datetime_module.timedelta(hours=1, minutes=20, seconds=20, microseconds=500)
    assert timedelta_format(td) == '01:20:20.000500'

# Generated at 2022-06-12 19:46:42.440848
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00') == datetime_module.timedelta(0)
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
        milliseconds=1
    )

# Generated at 2022-06-12 19:46:48.129694
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from .test_utils import assert_equal
    dt1 = timedelta_parse('10:00:00.123456')
    dt2 = timedelta_parse('10:00:00.123456')
    assert_equal(dt1, dt2)
    assert dt1 == dt2
    assert dt1 == 10*60*60 + 0.123456



# Generated at 2022-06-12 19:46:54.617188
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:10:20.123000') == \
           datetime_module.timedelta(minutes=10, seconds=20,
                                     microseconds=123000)
    assert timedelta_parse('1:00:10:20.123000') == \
           datetime_module.timedelta(hours=1, minutes=10, seconds=20,
                                     microseconds=123000)

test_timedelta_parse()

# Generated at 2022-06-12 19:47:03.023986
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest
    for s in ('01:02:03.123456',
              '01:02:03:123456',
              '01:02:03.1234567'):
        assert timedelta_parse(s) == datetime_module.timedelta(hours=1,
                                                                minutes=2,
                                                                seconds=3,
                                                                microseconds=123456)



# Generated at 2022-06-12 19:47:13.332760
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.999000') == datetime_module.timedelta(
        microseconds=999000
    )
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(1)
    assert timedelta_parse('00:00:59.999999') == datetime_module.timedelta(
        seconds=59, microseconds=999999
    )

# Generated at 2022-06-12 19:47:28.811059
# Unit test for function timedelta_parse
def test_timedelta_parse():
    def assert_parses(timedelta_string, expected_timedelta):
        assert timedelta_parse(timedelta_string) == expected_timedelta

    assert_parses('00:01:00.000000', datetime_module.timedelta(0, 60))
    assert_parses('00:01:00.100000', datetime_module.timedelta(0, 60, 100000))
    assert_parses('00:01:00.010000', datetime_module.timedelta(0, 60, 10000))
    assert_parses('00:01:00.001000', datetime_module.timedelta(0, 60, 1000))
    assert_parses('00:01:00.000100', datetime_module.timedelta(0, 60, 100))


# Generated at 2022-06-12 19:47:38.119724
# Unit test for function timedelta_format
def test_timedelta_format():

    inputs_and_correct_outputs = (
        (datetime_module.timedelta(minutes=5), '00:05:00.000000'),
        (datetime_module.timedelta(seconds=5), '00:00:05.000000'),
        (datetime_module.timedelta(seconds=4, microseconds=5),
         '00:00:04.000005'),
        (datetime_module.timedelta(days=5, seconds=4, microseconds=5),
         '120:00:04.000005'),
    )

    for timedelta, correct_output in inputs_and_correct_outputs:
        assert timedelta_format(timedelta) == correct_output



# Generated at 2022-06-12 19:47:48.697015
# Unit test for function timedelta_parse
def test_timedelta_parse():
    # The issue with using `__name__ == '__main__'` here is that we want to
    # test `__main__` when it's imported *for* the testing of `compatibility`,
    # but it still shouldn't run if `compatibility` is just imported.
    if not getattr(sys.modules['__main__'], '_tried_running_test_timedelta_parse', False):
        sys.modules['__main__']._tried_running_test_timedelta_parse = True
        delta = timedelta_parse('1:2:3.123456')
        assert (datetime_module.datetime.min + delta).strftime('%H:%M:%S.%f') == '01:02:03.123456'

# Generated at 2022-06-12 19:47:56.249138
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(weeks=0, days=0, hours=0, minutes=0,
                                  seconds=0, microseconds=1)
    ) == '00:00:00.000001'

    assert timedelta_format(
        datetime_module.timedelta(weeks=0, days=0, hours=3, minutes=0,
                                  seconds=0, microseconds=1)
    ) == '03:00:00.000001'

    assert timedelta_format(
        datetime_module.timedelta(weeks=0, days=0, hours=0, minutes=4,
                                  seconds=0, microseconds=1)
    ) == '00:04:00.000001'


# Generated at 2022-06-12 19:48:05.455298
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                                                  '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2)) == \
                                                  '01:02:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3)) == \
                                                  '01:02:03.000000'

# Generated at 2022-06-12 19:48:16.033097
# Unit test for function timedelta_parse
def test_timedelta_parse():
    td = timedelta_parse('3:07:5.567892')
    assert td == datetime_module.timedelta(hours=3, minutes=7, seconds=5,
                                           microseconds=567892)
    td = timedelta_parse('1:2:3.4')
    assert td == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                           microseconds=400000)


# Workaround for https://bugs.python.org/issue29167
try:
    from collections.abc import UserString
except ImportError:
    from UserString import UserString


# Workaround for https://bugs.python.org/issue29167
try:
    from collections.abc import UserList
except ImportError:
    from UserList import UserList

# Generated at 2022-06-12 19:48:22.425536
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('03:22:01.543000') == datetime_module.timedelta(
        hours=3, minutes=22, seconds=1, microseconds=543000)
    assert timedelta_parse('03:22:01.543000') == timedelta_format(
        datetime_module.timedelta(hours=3, minutes=22, seconds=1,
                                  microseconds=543000))

# Generated at 2022-06-12 19:48:28.610543
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(
        seconds=1, microseconds=2)) == '00:00:01.000002'
    assert timedelta_parse('01:00:00') == datetime_module.timedelta(hours=1)
    assert timedelta_

# Generated at 2022-06-12 19:48:40.992943
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=3, minutes=4, seconds=5,
                                          microseconds=6)
    assert timedelta_format(timedelta) == '03:04:05.000006'
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta

test_timedelta_format()


if not hasattr(os, 'scandir'):
    try:
        from scandir import scandir
    except ImportError:
        def scandir(directory):
            def yield_stat_object(path):
                yield os.stat(path)
            return ((filename, yield_stat_object(os.path.join(directory,
                                                              filename)))
                    for filename in os.listdir(directory))

# Generated at 2022-06-12 19:48:43.986041
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=4)
    ) == '01:02:03.000004'



# Generated at 2022-06-12 19:49:14.924052
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:02.123456') == datetime_module.timedelta(
        seconds=2, microseconds=123456)
    assert timedelta_parse('00:00:02.123456789') == datetime_module.timedelta(
        seconds=2, microseconds=123456)
    assert timedelta_parse('00:00:02.123') == datetime_module.timedelta(
        seconds=2, microseconds=123000)
    assert timedelta_parse('00:00:02.12') == datetime_module.timedelta(
        seconds=2, microseconds=120000)
    assert timedelta_parse('00:00:02.1') == datetime_module.timedelta(
        seconds=2, microseconds=100000)
    assert timedelta_

# Generated at 2022-06-12 19:49:25.053490
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                                  microseconds=999999)
    )) == datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                                    microseconds=999999)


if PY3:
    string_convertible_types = (str, bytes, bytearray, memoryview)
else:
    string_convertible_types = (str, buffer, bytearray, memoryview)



# Generated at 2022-06-12 19:49:28.880005
# Unit test for function timedelta_format
def test_timedelta_format():
    from itertools import permutations
    for time_args in permutations([-2, 0, 2], 3):
        time = datetime_module.time(*time_args)
        timedelta = time - datetime_module.time.min
        assert timedelta == timedelta_parse(timedelta_format(timedelta))

# Generated at 2022-06-12 19:49:32.160872
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:15:51.734412') == datetime_module.timedelta(
        hours=1, minutes=15, seconds=51, microseconds=734412
    )



# Generated at 2022-06-12 19:49:42.676960
# Unit test for function timedelta_format
def test_timedelta_format():
    if PY3:
        timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                              microseconds=456789)
        assert timedelta_format(timedelta) == '01:02:03.456789'


if sys.version_info[:2] >= (3, 5):
    from asyncio import ensure_future as ensure_future_
else:

    def ensure_future_(coro_or_future, *args, **kwargs):
        from asyncio import ensure_future
        # The following is a workaround for asyncio bug in Python 3.4.
        # See: https://bugs.python.org/issue26336
        if hasattr(coro_or_future, '_asyncio_future_blocking'):
            return coro_or_future

# Generated at 2022-06-12 19:49:53.038439
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:1:1.1') == datetime_module.timedelta(
        seconds=1 + 60 + 3600 + 0.1
    )
    assert timedelta_parse('-1:1:1.1') == datetime_module.timedelta(
        seconds=-(1 + 60 + 3600 + 0.1)
    )
    assert timedelta_parse('1:1:1.123') == datetime_module.timedelta(
        seconds=1 + 60 + 3600 + 0.123
    )
    assert timedelta_parse('-1:1:1.123') == datetime_module.timedelta(
        seconds=-(1 + 60 + 3600 + 0.123)
    )

# Generated at 2022-06-12 19:50:00.018706
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(0, 1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(0, 60)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(1)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(0, 0, 1000)

# Generated at 2022-06-12 19:50:06.207329
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:23:27.999999') == datetime_module.timedelta(
        minutes=23, seconds=27, microseconds=999999)
    assert timedelta_parse('01:23:27.999999') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=27, microseconds=999999)

# Generated at 2022-06-12 19:50:10.982167
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert (
        timedelta_parse(timedelta_format(datetime_module.timedelta(
            hours=3, minutes=13, seconds=33, microseconds=600000
        ))) ==
        datetime_module.timedelta(hours=3, minutes=13, seconds=33,
                                  microseconds=600000)
    )

# Generated at 2022-06-12 19:50:21.332460
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(-1)) == '-1:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1, 2)) == '00:00:01.000002'
    assert timedelta_format(datetime_module.timedelta(1, 2, 3)) == '00:00:01.000002'
    assert timedelta_format(datetime_module.timedelta(1, 2, 3, 4)) == '00:00:01.000002'

# Generated at 2022-06-12 19:51:16.167418
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000500') == datetime_module.timedelta(microseconds=500)
    assert timedelta_parse('00:00:00.000999') == datetime_module.timedelta(microseconds=999)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(microseconds=1000)
    assert timedelta_parse('00:00:00.001999') == datetime_module.timedelta(microseconds=1000 + 999)
    assert timedelta_parse('00:00:00.002000') == datetime_module.timedelta(microseconds=2000)

# Generated at 2022-06-12 19:51:25.658243
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=1,
                                                      seconds=1,
                                                      microseconds=1)) == \
                             '01:01:01.000001'


# Generated at 2022-06-12 19:51:35.458624
# Unit test for function timedelta_format
def test_timedelta_format():
    assert '00:00:00.000000' == timedelta_format(datetime_module.timedelta())
    assert '00:00:01.000000' == timedelta_format(
        datetime_module.timedelta(seconds=1)
    )
    assert '00:01:00.000000' == timedelta_format(
        datetime_module.timedelta(minutes=1)
    )
    assert '01:00:00.000000' == timedelta_format(
        datetime_module.timedelta(hours=1)
    )
    assert '00:00:00.100000' == timedelta_format(
        datetime_module.timedelta(microseconds=100000)
    )

# Generated at 2022-06-12 19:51:37.107666
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.000001') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=1)

# Generated at 2022-06-12 19:51:48.243386
# Unit test for function timedelta_format
def test_timedelta_format():
    from .utils import assert_equivalent

    def zzz(timedelta):
        return timedelta_format(timedelta)

    assert_equivalent(zzz(datetime_module.timedelta(hours=1)),
                      '01:00:00.000000')
    assert_equivalent(zzz(datetime_module.timedelta(minutes=1)),
                      '00:01:00.000000')
    assert_equivalent(zzz(datetime_module.timedelta(seconds=1)),
                      '00:00:01.000000')
    assert_equivalent(zzz(datetime_module.timedelta(microseconds=1)),
                      '00:00:00.000001')


# Generated at 2022-06-12 19:51:55.008781
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:52:03.809504
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:01:01.010001') == timedelta_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=100)
    assert timedelta_parse('1:01:01.010101') == timedelta_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=101)
    assert timedelta_parse('1:01:01.010111') == timedelta_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=111)
    assert timedelta_parse('1:01:01.011101') == timedelta_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=1101)

# Generated at 2022-06-12 19:52:07.179792
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.456000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456000
    )

# Generated at 2022-06-12 19:52:11.973049
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
           '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3)) == \
           '01:02:03.000000'



# Generated at 2022-06-12 19:52:14.772642
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for i in range(10 ** 6):
        x = datetime_module.timedelta(microseconds=i)
        s = timedelta_format(x)
        y = timedelta_parse(s)
        assert x == y

# Generated at 2022-06-12 19:53:56.089418
# Unit test for function timedelta_format
def test_timedelta_format():
    td = datetime_module.timedelta(hours=5, minutes=7, seconds=8,
                                   microseconds=9)
    assert timedelta_format(td) == '05:07:08.000009'



# Generated at 2022-06-12 19:54:06.305551
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('11:01:02.000003') == datetime_module.timedelta(
        hours=11, minutes=1, seconds=2, microseconds=3
    )
    assert timedelta_parse('11:01:02.000003') == timedelta_parse('11:01:02.3')
    assert timedelta_parse('11:01:02.000003') == timedelta_parse('11:01:02.03')
    assert timedelta_parse('11:01:02.000003') == timedelta_parse('11:01:02.003')

# Generated at 2022-06-12 19:54:14.061553
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:1.123456') == datetime_module.timedelta(
        seconds=1,
        microseconds=123456
    )
    assert timedelta_parse('0:1:1.123456') == datetime_module.timedelta(
        minutes=1,
        seconds=1,
        microseconds=123456
    )
    assert timedelta_parse('1:1:1.123456') == datetime_module.timedelta(
        hours=1,
        minutes=1,
        seconds=1,
        microseconds=123456
    )

# Generated at 2022-06-12 19:54:17.790393
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=13,
        minutes=37,
        seconds=59,
        microseconds=879786
    )) == '13:37:59.879786'


if PY3:
    import collections.abc as collections_abc
else:
    import collections as collections_abc

# Generated at 2022-06-12 19:54:23.614381
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('1:02:03.000010')) == \
                                                            '01:02:03.000010'
    assert timedelta_format(timedelta_parse('1:02:03.000010')) == \
                                                            '01:02:03.000010'
    assert timedelta_format(timedelta_parse('0:00:00.000001')) == \
                                                            '00:00:00.000001'
    assert timedelta_format(timedelta_parse('0:00:00.000000')) == \
                                                            '00:00:00.000000'


# Generated at 2022-06-12 19:54:31.925181
# Unit test for function timedelta_format
def test_timedelta_format():
    from .python_toolbox.context_management import captured_stdout
    from .testing.fake_subprocess import assert_subprocess
    assert time_isoformat(datetime_module.time(12, 11, 10, 123456)) == '12:11:10.123456'
    assert timedelta_format(datetime_module.timedelta(minutes=2)) == '00:02:00.000000'
    with captured_stdout() as stdout:
        assert_subprocess(
            '%s %s' % (sys.executable, __file__),
            include_stderr=False,
            expected_stdout='16:31:00.123456'
        )


# Generated at 2022-06-12 19:54:42.166653
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('12:34:56.789000')) == \
                                                     '12:34:56.789000'
    assert timedelta_format(timedelta_parse('12:34:56.789001')) == \
                                                     '12:34:56.789001'
    assert timedelta_format(timedelta_parse('12:34:56.789002')) == \
                                                     '12:34:56.789002'
    assert timedelta_format(timedelta_parse('12:34:56.789003')) == \
                                                     '12:34:56.789003'

# Generated at 2022-06-12 19:54:48.482073
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=999999)) == '00:00:00.999999'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=59)) == '00:00:59.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'

# Generated at 2022-06-12 19:54:59.680085
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(1, 1)) == '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(0, 0, 1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=123456.789012)) == \
                                                          '34:17:36.789012'

# Generated at 2022-06-12 19:55:04.587048
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=3, minutes=4, seconds=5,
                                  microseconds=123456)
    )) == datetime_module.timedelta(hours=3, minutes=4, seconds=5,
                                    microseconds=123456)
