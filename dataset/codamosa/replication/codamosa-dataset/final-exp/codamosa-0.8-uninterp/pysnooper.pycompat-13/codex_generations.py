

# Generated at 2022-06-12 19:46:19.318723
# Unit test for function timedelta_parse

# Generated at 2022-06-12 19:46:25.693437
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for time_string, time_tuple in (
        ('00:00:00.000000', (0, 0, 0, 0)),
        ('01:00:00.000000', (1, 0, 0, 0)),
        ('00:01:00.000000', (0, 1, 0, 0)),
        ('00:00:01.000000', (0, 0, 1, 0)),
        ('00:00:00.000001', (0, 0, 0, 1)),
        ('01:01:01.000001', (1, 1, 1, 1)),
        ('12:03:44.678901', (12, 3, 44, 678901)),
    ):
        assert timedelta_parse(time_string) == \
               datetime_module.timedelta(*time_tuple)

# Generated at 2022-06-12 19:46:33.065336
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=5)) == '00:00:00.000005'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=1)) == '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'



# Generated at 2022-06-12 19:46:39.083052
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(microseconds=10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(microseconds=100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(microseconds=1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(microseconds=10000)

# Generated at 2022-06-12 19:46:41.703258
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('03:04:05.999999') == \
           datetime_module.timedelta(hours=3, minutes=4, seconds=5,
                                     microseconds=999999)

# Generated at 2022-06-12 19:46:44.413127
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert str(timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    ))).total_seconds()) == '3723.000004'

# Generated at 2022-06-12 19:46:49.001220
# Unit test for function timedelta_format
def test_timedelta_format():
    delta = datetime_module.timedelta(days=0, hours=3, minutes=4,
                                      seconds=5, microseconds=6)
    assert timedelta_format(delta) == '03:04:05.000006'



# Generated at 2022-06-12 19:47:00.016468
# Unit test for function timedelta_parse
def test_timedelta_parse():
    """Unit test for function `timedelta_parse`."""
    assert timedelta_format(timedelta_parse('01:23:45.678901')) == \
                                                '01:23:45.678901'
    assert timedelta_format(timedelta_parse('00:00:00.000001')) == \
                                                '00:00:00.000001'
    assert timedelta_format(timedelta_parse('00:00:00.000000')) == \
                                                '00:00:00.000000'
    assert timedelta_format(timedelta_parse('23:59:59.999999')) == \
                                                '23:59:59.999999'


# Generated at 2022-06-12 19:47:11.073095
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(
        microseconds=10 ** 4
    )
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1,
    )
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(
        minutes=1,
    )

# Generated at 2022-06-12 19:47:19.527264
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                             '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == \
                                                             '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=-1)) == \
                                                             '-00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                                                             '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=-1)) == \
                                                             '-01:00:00.000000'

# Generated at 2022-06-12 19:47:33.733770
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
    assert timedelta_format(datetime_module.timedelta(minutes=1,
                                                      microseconds=2)) == \
           '00:01:00.000002'



# Generated at 2022-06-12 19:47:37.183667
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=2, minutes=2, seconds=2,
                                          microseconds=500500)
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:47:42.579583
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'

    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=4)
    ) == '01:02:03.000004'



# Generated at 2022-06-12 19:47:45.415364
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('11:31:54.152443')
    assert repr(timedelta) == 'datetime.timedelta(0, 42114, 152443)'


# Generated at 2022-06-12 19:47:50.291528
# Unit test for function timedelta_parse
def test_timedelta_parse():
    t = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=456)
    u = datetime_module.timedelta(hours=12, minutes=34, seconds=56,
                                  microseconds=7890)
    assert timedelta_parse(timedelta_format(t)) == t
    assert timedelta_parse(timedelta_format(u)) == u

# Generated at 2022-06-12 19:48:00.992304
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.400000') == datetime_module.timedelta(
        hours=1,
        minutes=2,
        seconds=3,
        microseconds=400000
    )
    assert timedelta_parse('1:2:3') == datetime_module.timedelta(
        hours=1,
        minutes=2,
        seconds=3,
    )
    assert timedelta_parse('1:2:3.0') == datetime_module.timedelta(
        hours=1,
        minutes=2,
        seconds=3,
    )

# Generated at 2022-06-12 19:48:08.527023
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=5))) == \
           datetime_module.timedelta(hours=5)

    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=5,
                                                                      minutes=7))) == \
           datetime_module.timedelta(hours=5, minutes=7)

    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=5,
                                                                      minutes=7,
                                                                      seconds=61))) == \
           datetime_module.timedelta(hours=5, minutes=7, seconds=61)

if hasattr(datetime_module, 'fromisoformat'):
    datetime_fromisoformat = datetime_

# Generated at 2022-06-12 19:48:14.323161
# Unit test for function timedelta_format
def test_timedelta_format():
    time = time_isoformat(datetime_module.time(0, 0, 0),
                          timespec='microseconds')
    assert timedelta_format(datetime_module.timedelta(0)) == time
    assert timedelta_format(datetime_module.timedelta(0)) == \
        timedelta_format(datetime_module.timedelta(0, 0, 0, 0))



# Generated at 2022-06-12 19:48:23.820024
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
           '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, microseconds=6)) == \
           '01:00:00.000006'



# Generated at 2022-06-12 19:48:25.894748
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=400000
    )) == '01:02:03.400000'



# Generated at 2022-06-12 19:48:39.817827
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                 '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=-1)) == \
                                 '-1 day, 23:59:59.000000'
    assert timedelta_format(datetime_module.timedelta(days=1)) == \
                                 '24:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=23, minutes=59,
                                                      seconds=59,
                                                      microseconds=999999)) == \
                                 '23:59:59.999999'

# Generated at 2022-06-12 19:48:49.643136
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=10,
                           minutes=0, seconds=0, microseconds=0)) ==\
                           '10:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=0,
                           minutes=10, seconds=0, microseconds=0)) ==\
                           '00:10:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=0,
                           minutes=0, seconds=10, microseconds=0)) ==\
                           '00:00:10.000000'

# Generated at 2022-06-12 19:48:51.265333
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()



# Generated at 2022-06-12 19:48:54.991354
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
        '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                       microseconds=1)) == \
        '01:00:00.000001'



# Generated at 2022-06-12 19:49:04.836618
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(milliseconds=1)
    assert timedelta_parse('00:00:00.100000') == datetime_module.timedelta(milliseconds=100)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(minutes=1)

# Generated at 2022-06-12 19:49:08.927802
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=2, hours=3, minutes=4,
                                          seconds=5, microseconds=6)
    result = timedelta_format(timedelta)
    assert result == '067:04:05.000006'



# Generated at 2022-06-12 19:49:12.909365
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('12:20:54.337000') == datetime_module.timedelta(0,
                                                                           45254,
                                                                           337000)
    assert timedelta_parse('1:54:46.121000') == datetime_module.timedelta(0,
                                                                          6726,
                                                                          121000)


# Generated at 2022-06-12 19:49:17.294055
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=3)) == \
                                                          '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=45)) == \
                                                          '00:00:45.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=123456)) == \
                                                          '00:00:00.123456'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == \
                                                          '01:02:03.000004'

# Generated at 2022-06-12 19:49:29.006016
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest
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
    assert timedelta_parse('01:00:01.000000') == datetime_module.timedelta(
        hours=1, seconds=1
    )

# Generated at 2022-06-12 19:49:32.688173
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        days=3, hours=14, minutes=35, seconds=46, microseconds=9
    )) == '14:35:46.000009'



# Generated at 2022-06-12 19:50:06.234895
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest

    def assert_roundtrips(timedelta):
        assert timedelta == timedelta_parse(timedelta_format(timedelta))

    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(
        microseconds=10
    )
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(
        microseconds=100
    )

# Generated at 2022-06-12 19:50:14.587319
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert (timedelta_format(timedelta_parse('12:01:02.012345')) ==
            '12:01:02.012345')
    assert (timedelta_format(timedelta_parse('12:01:02.123456')) ==
            '12:01:02.123456')
    assert (timedelta_format(timedelta_parse('12:01:02.123456 ')) ==
            '12:01:02.123456')
    assert (timedelta_format(timedelta_parse('12:01:02:123456')) ==
            '12:01:02.123456')
    assert (timedelta_format(timedelta_parse('12:01:02:123456 ')) ==
            '12:01:02.123456')



# Generated at 2022-06-12 19:50:17.081290
# Unit test for function timedelta_format
def test_timedelta_format():
    td1 = datetime_module.timedelta(hours=0, minutes=0,
                                    seconds=2, microseconds=50)
    assert timedelta_format(td1) == '00:00:02.000050'


# Generated at 2022-06-12 19:50:25.039141
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=0, minutes=0,
                                                      seconds=0,
                                                      microseconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=0, minutes=0,
                                                      seconds=0,
                                                      microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=0, minutes=0,
                                                      seconds=0,
                                                      microseconds=10)) == '00:00:00.000010'
    assert timedelta_format(datetime_module.timedelta(hours=0, minutes=0,
                                                      seconds=0,
                                                      microseconds=100))

# Generated at 2022-06-12 19:50:35.123738
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from nose.tools import assert_equal
    try:
        from .test_utils import assert_datetime_objects_equal
    except (SyntaxError, ImportError):
        # SyntaxError: not in Python 3
        # ImportError: outside of package
        assert_equal = assert_datetime_objects_equal = lambda x: x

    assert_datetime_objects_equal(
        timedelta_parse('0:00:00.00000'),
        datetime_module.timedelta(seconds=0)
    )
    assert_datetime_objects_equal(
        timedelta_parse('0:00:00.62997'),
        datetime_module.timedelta(seconds=0.62997)
    )

# Generated at 2022-06-12 19:50:40.405837
# Unit test for function timedelta_format
def test_timedelta_format():
    import pytest
    timedelta = datetime_module.timedelta(microseconds=1234)
    result = timedelta_format(timedelta)
    assert result == '00:00:00.001234'
    timedelta = datetime_module.timedelta(seconds=4, microseconds=123456)
    result = timedelta_format(timedelta)
    assert result == '00:00:04.123456'



# Generated at 2022-06-12 19:50:47.291314
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=123456)
    assert timedelta_parse('01:02:03.1234567') == datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=123456)
    assert timedelta_parse('01:02:03.12345678') == datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=123456)
    assert timedelta_parse('01:02:03.123456789') == datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=123456)

# Generated at 2022-06-12 19:50:56.715946
# Unit test for function timedelta_format
def test_timedelta_format():
    from collections import namedtuple
    TestCase = namedtuple('TestCase', 'timedelta s')
    test_cases = (
        TestCase(timedelta=datetime_module.timedelta(seconds=1),
                 s='00:00:01.000000'),
        TestCase(timedelta=datetime_module.timedelta(hours=1, minutes=1,
                                                     seconds=1),
                 s='01:01:01.000000'),
        TestCase(timedelta=datetime_module.timedelta(hours=1, minutes=1,
                                                     seconds=1,
                                                     microseconds=1),
                 s='01:01:01.000001'),
    )

# Generated at 2022-06-12 19:50:58.755862
# Unit test for function timedelta_parse
def test_timedelta_parse():
    td = datetime_module.timedelta(hours=2, minutes=3, seconds=4,
                                   microseconds=5)
    assert timedelta_parse(timedelta_format(td)) == td




# Generated at 2022-06-12 19:51:03.150282
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=4))) == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=4)



# Generated at 2022-06-12 19:52:00.381586
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:02:03.456789') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456789
    )
    assert timedelta_parse('1:02:03') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3
    )
    assert timedelta_parse('1:02') == datetime_module.timedelta(
        hours=1, minutes=2
    )
    assert timedelta_parse('1') == datetime_module.timedelta(
        hours=1
    )

# Generated at 2022-06-12 19:52:10.594284
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('12:34:56.123456') == \
           datetime_module.timedelta(hours=12, minutes=34, seconds=56,
                                     microseconds=123456)
    assert timedelta_parse('12:34:56') == \
           datetime_module.timedelta(hours=12, minutes=34, seconds=56)
    assert timedelta_parse('1:2:3.4') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=400000)
    assert timedelta_parse('1:2:3.0') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3)

# Generated at 2022-06-12 19:52:15.564729
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1.5)) == \
           '00:00:01.500000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=10,
                                                      seconds=11.2345)) == \
           '01:10:11.234500'


# Generated at 2022-06-12 19:52:23.794555
# Unit test for function timedelta_format
def test_timedelta_format():
    if sys.version_info[:2] >= (3, 6):
        assert timedelta_format(datetime_module.timedelta(seconds=14,
                                                          microseconds=5)) \
                                                          == '00:00:14.000005'
        assert timedelta_format(datetime_module.timedelta(days=14, seconds=5)) \
                                                          == '00:00:05.000000'
        assert timedelta_format(datetime_module.timedelta(days=14)) \
                                                          == '00:00:00.000000'
        assert timedelta_format(datetime_module.timedelta(days=14,
                                                          minutes=23,
                                                          seconds=5)) \
                                                          == '00:23:05.000000'


# Generated at 2022-06-12 19:52:25.102717
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.123456') == \
           datetime_module.timedelta(seconds=3723.123456)

# Generated at 2022-06-12 19:52:26.766477
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == '01:02:03.000004'



# Generated at 2022-06-12 19:52:32.504954
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(2, 3, 4)) == \
           '00:00:02.000004'
    assert timedelta_format(datetime_module.timedelta(9, 8, 7, 6)) == \
           '00:00:09.000008'


# Unit tests for function timedelta_parse

# Generated at 2022-06-12 19:52:37.918565
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
        '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
        '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=1000)) == \
        '00:00:00.001000'



# Generated at 2022-06-12 19:52:47.674622
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:52:54.538740
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:54:43.946872
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=23)) == \
                                                              '00:00:23.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=23,
                                                      microseconds=23)) == \
                                                              '00:00:23.000023'
    assert timedelta_format(datetime_module.timedelta(seconds=23,
                                                      microseconds=1)) == \
                                                              '00:00:23.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=5474)) == \
                                                              '01:31:14.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=5474,
                                                      microseconds=234))

# Generated at 2022-06-12 19:54:47.532809
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=23,
                                                      minutes=12,
                                                      seconds=54,
                                                      microseconds=123456)) == \
                                                      '23:12:54.123456'



# Generated at 2022-06-12 19:54:50.275973
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=123456)
    assert timedelta_format(timedelta) == '01:02:03.123456'



# Generated at 2022-06-12 19:55:01.198472
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=10)) == '00:00:10.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=55)) == '00:00:00.000055'
    assert timedelta_format(datetime_module.timedelta(seconds=10,
                                                      microseconds=55)) == '00:00:10.000055'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=10,
                                                      microseconds=55)) == '01:00:10.000055'



# Generated at 2022-06-12 19:55:11.294301
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.234000') == (datetime_module.
                                                  timedelta(hours=1,
                                                            minutes=2,
                                                            seconds=3,
                                                            microseconds=234))

    assert timedelta_parse('1:02:03.234000') == (datetime_module.
                                                 timedelta(hours=1,
                                                           minutes=2,
                                                           seconds=3,
                                                           microseconds=234))

    assert timedelta_parse('0:02:03.234000') == (datetime_module.
                                                 timedelta(hours=0,
                                                           minutes=2,
                                                           seconds=3,
                                                           microseconds=234))


# Generated at 2022-06-12 19:55:20.905836
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=23, minutes=59,
                                                      seconds=59,
                                                      microseconds=999999)) == \
                                                              '23:59:59.999999'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=405060)) == \
                                                              '01:02:03.405060'
    assert timedelta_format(datetime_module.timedelta(hours=-1, minutes=-2,
                                                      seconds=-3,
                                                      microseconds=-405060)) == \
                                                              '-01:02:03.405060'



# Generated at 2022-06-12 19:55:24.554907
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=8,
                                                      minutes=3,
                                                      seconds=4,
                                                      microseconds=654789)) ==\
           '08:03:04.654789'



# Generated at 2022-06-12 19:55:27.050668
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('1:2:3.123456')
    assert timedelta.days == 0
    assert timedelta.seconds == 3723
    assert timedelta.microseconds == 123456

# Generated at 2022-06-12 19:55:34.075502
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(minutes=2, seconds=3)) == '00:02:03.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=3, microseconds=5000)) == '00:00:03.005000'
    assert timedelta_format(datetime_module.timedelta(weeks=2, days=5)) == '168:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=20000)) == '00:00:00.020000'
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'


# Generated at 2022-06-12 19:55:41.505275
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      milliseconds=400,
                                                      microseconds=500)) == \
                                                      '01:02:03.400500'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3)) == \
                                                      '01:02:03.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      milliseconds=300)) == \
                                                      '01:02:00.300000'