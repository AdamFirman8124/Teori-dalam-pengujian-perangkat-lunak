

# Generated at 2022-06-12 19:46:19.884348
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(0, 1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(0, 60)
    assert timedelta_parse('00:01:01.000000') == datetime_module.timedelta(0, 60 + 1)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('01:01:00.000000') == \
                           datetime_module.timedelta(hours=1, minutes=1)

# Generated at 2022-06-12 19:46:25.612872
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:01:20.500050') \
           == datetime_module.timedelta(minutes=1, seconds=20,
                                        microseconds=500050)
    assert timedelta_parse('0:1:5.5') \
           == datetime_module.timedelta(minutes=1, seconds=5,
                                        microseconds=500000)
    assert timedelta_parse('1:2:3.4') \
           == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                        microseconds=400000)


# Generated at 2022-06-12 19:46:34.011170
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=1, minutes=1)) == '01:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=1, minutes=1, seconds=1)) == '01:01:01.000000'

# Generated at 2022-06-12 19:46:43.368126
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=-8)) == '-200:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=-8, hours=2)) == '-198:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=0, hours=2)) == '02:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=2)) == '02:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=2, minutes=-12)) == '01:48:00.000000'

# Generated at 2022-06-12 19:46:55.405331
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=6)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=6, hours=12)) == '12:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=6, hours=12,
                                                      minutes=15)) == '12:15:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=6, hours=12,
                                                      minutes=15, seconds=34)) == '12:15:34.000000'

# Generated at 2022-06-12 19:47:08.155965
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from garlicsim.general_misc import misc_tools

    nines_string_1 = '00:00:00.999999'
    nines_timedelta_1 = timedelta_parse(nines_string_1)
    nines_string_2 = timedelta_format(nines_timedelta_1)
    assert nines_string_1 == nines_string_2

    microsecond_only_string_1 = '00:00:00.000001'
    microsecond_only_timedelta_1 = timedelta_parse(microsecond_only_string_1)
    microsecond_only_string_2 = timedelta_format(microsecond_only_timedelta_1)
    assert microsecond_only_string_1 == microsecond_only_string_2

    assert not microsecond_only_timed

# Generated at 2022-06-12 19:47:17.812727
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=0
    )) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=0, seconds=0, microseconds=0
    )) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=1, seconds=0, microseconds=0
    )) == '01:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=0
    )) == '01:01:01.000000'

# Generated at 2022-06-12 19:47:22.259497
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('12:34:56.123456')
    assert timedelta.microseconds == 123456
    assert timedelta.seconds == (60 * 60 * 12) + (60 * 34) + 56
    timedelta = timedelta_parse('00:00:00.000')
    assert timedelta.microseconds == 0
    assert timedelta.seconds == 0



# Generated at 2022-06-12 19:47:28.925725
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('1:02:03.000001') == datetime_module.timedelta(
        hours=1,
        minutes=2,
        seconds=3,
        microseconds=1,
    )
    assert timedelta_parse('1:02:03.99999') == datetime_module.timedelta(
        hours=1,
        minutes=2,
        seconds=3,
        microseconds=99999
    )



# Generated at 2022-06-12 19:47:37.596772
# Unit test for function timedelta_format
def test_timedelta_format():
    assert '00:00:00.040000' == timedelta_format(datetime_module.timedelta(
                                                                seconds=4e-5))
    assert '00:00:00.000001' == timedelta_format(datetime_module.timedelta(
                                                                 microseconds=1))
    assert '00:00:00.000000' == timedelta_format(datetime_module.timedelta(
                                                                 microseconds=0))
    assert '23:59:59.999999' == timedelta_format(datetime_module.timedelta(
                                                             days=1, microseconds=-1))



# Generated at 2022-06-12 19:47:55.507676
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:00.123456') == datetime_module.timedelta(0, 0, 123456)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(0, 1)
    assert timedelta_parse('00:00:01.000001') == datetime_module.timedelta(0, 1, 1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(0, 60)

# Generated at 2022-06-12 19:48:04.894233
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=-1,
                                                      microseconds=-999999)) \
        == '-00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=999999)) \
        == '00:00:01.999999'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=1)) \
        == '01:01:01.000001'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=999999)) \
        == '01:01:01.999999'



# Generated at 2022-06-12 19:48:15.713615
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('00:00:00.000000')) == \
                                                    '00:00:00.000000'
    assert timedelta_format(timedelta_parse('00:00:00.000001')) == \
                                                    '00:00:00.000001'
    assert timedelta_format(timedelta_parse('00:00:00.123456')) == \
                                                    '00:00:00.123456'
    assert timedelta_format(timedelta_parse('00:01:00.123456')) == \
                                                    '00:01:00.123456'
    assert timedelta_format(timedelta_parse('01:00:00.123456')) == \
                                                    '01:00:00.123456'
   

# Generated at 2022-06-12 19:48:20.506742
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=12, hours=15, minutes=6,
                                          seconds=90, microseconds=123000)
    assert timedelta_format(timedelta) == '15:06:30.123000'



# Generated at 2022-06-12 19:48:22.901305
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(1, 1, 1)) == '00:00:01.000001'



# Generated at 2022-06-12 19:48:26.743319
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from .python_toolbox.math_tools import is_close
    for i in range(1000):
        x = timedelta_parse(timedelta_format(datetime_module.timedelta(
            days=i, seconds=i, microseconds=i)))
        assert is_close(timedelta_format(x), timedelta_format(datetime_module.timedelta(
            days=i, seconds=i, microseconds=i)))

# Generated at 2022-06-12 19:48:30.775148
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=2, microseconds=123456)) == \
           '00:00:02.123456'
    assert timedelta_format(datetime_module.timedelta(minutes=3, seconds=4, microseconds=163456)) == \
           '00:03:04.163456'
    assert timedelta_format(datetime_module.timedelta(hours=5, minutes=6, seconds=7, microseconds=1)) == \
           '05:06:07.000001'



# Generated at 2022-06-12 19:48:42.138073
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta()
    assert timedelta_parse('0:0:0.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('0:0:0.000010') == datetime_module.timedelta(microseconds=10)
    assert timedelta_parse('0:0:0.000100') == datetime_module.timedelta(microseconds=100)
    assert timedelta_parse('0:0:0.001000') == datetime_module.timedelta(microseconds=1000)
    assert timedelta_parse('0:0:0.010000') == datetime_module.timedelta(microseconds=10000)

# Generated at 2022-06-12 19:48:49.316109
# Unit test for function timedelta_parse
def test_timedelta_parse():
    times = [
        '00:00:00.000001',
        '00:10:00.000000',
        '01:00:00.000001',
        '23:59:59.999999',
        '-00:00:00.000001',
        '-00:10:00.000000',
        '-01:00:00.000001',
        '-23:59:59.999999',
        ]
    for time in times:
        assert timedelta_parse(time) == timedelta_format(timedelta_parse(time))

# Generated at 2022-06-12 19:48:57.416860
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )
    assert timedelta_parse('0:0:0.123456') == datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=123456
    )
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=0
    )
    assert timedelta_parse('0:0:0') == datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=0
    )

# Generated at 2022-06-12 19:49:22.402067
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(0, 0, 10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(0, 0, 100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(0, 0, 1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(0, 0, 10000)
    assert timedelta_parse

# Generated at 2022-06-12 19:49:31.625792
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=6)) == (
        '00:00:06.000000'
    )
    assert timedelta_format(datetime_module.timedelta(minutes=6)) == (
        '00:06:00.000000'
    )
    assert timedelta_format(datetime_module.timedelta(hours=6)) == (
        '06:00:00.000000'
    )
    assert timedelta_format(datetime_module.timedelta(hours=6, minutes=7,
                                                      seconds=8,
                                                      microseconds=9)) == (
        '06:07:08.000009'
    )

# Generated at 2022-06-12 19:49:41.948567
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=0, seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=0, seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=0, seconds=0.1)) == '00:00:00.100000'
    assert timedelta_format(datetime_module.timedelta(hours=0, seconds=1, microseconds=2)) == '00:00:01.000002'
    assert timedelta_format(datetime_module.timedelta(hours=0, seconds=1, microseconds=200)) == '00:00:01.000200'

# Generated at 2022-06-12 19:49:53.206637
# Unit test for function timedelta_parse
def test_timedelta_parse():
    def assert_equal(s1, s2):
        t1 = timedelta_parse(s1)
        t2 = timedelta_parse(s2)
        assert t1 == t2

    assert_equal('00:00:00.000000', '00:00:00.000000')
    assert_equal('01:00:00.000000', '1:0:0.000000')
    assert_equal('01:00:00.000000', '01:0:0.000000')
    assert_equal('01:00:00.000000', '01:00:0.000000')
    assert_equal('01:00:00.000000', '01:00:00.000000')
    assert_equal('01:00:00.000000', '01:00:00.000')


# Generated at 2022-06-12 19:50:00.528230
# Unit test for function timedelta_format
def test_timedelta_format():
    time = time_isoformat(datetime_module.time(10, 30, 15, 987654))
    assert time == '10:30:15.098765'
    assert timedelta_parse(time) == datetime_module.timedelta(
        hours=10, minutes=30, seconds=15, microseconds=987654
    )

# Generated at 2022-06-12 19:50:09.259008
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from .testing_tools import assert_equal
    assert_equal(timedelta_parse('0:00:00.123456'),
                 datetime_module.timedelta(seconds=0, microseconds=123456))
    assert_equal(timedelta_parse('0:00:01.123456'),
                 datetime_module.timedelta(seconds=1, microseconds=123456))
    assert_equal(timedelta_parse('0:01:00.123456'),
                 datetime_module.timedelta(minutes=1, seconds=0,
                                           microseconds=123456))
    assert_equal(timedelta_parse('1:00:00.123456'),
                 datetime_module.timedelta(hours=1, seconds=0,
                                           microseconds=123456))
    assert_

# Generated at 2022-06-12 19:50:19.737979
# Unit test for function timedelta_format
def test_timedelta_format():
    import pytest
    from . import py2_compatibility

    for timedelta in map(datetime_module.timedelta, range(-999, 1000, 100)):
        result = py2_compatibility.timedelta_format(timedelta)
        timestamp = '{:0>15}'.format(result)
        assert len(timestamp) == 15
        assert timestamp[:2] in ('-0', '-1')
        assert timestamp[2:5] == ':00'
        assert timestamp[5:8] in ('00', '01')
        assert timestamp[8] == ':'
        assert timestamp[9:12] == '00'
        assert timestamp[12] == '.'
        assert timestamp[13:15] in ('00', '01')
        assert timedelta_parse(result) == timedelta



# Generated at 2022-06-12 19:50:22.479501
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta_format(datetime_module.timedelta(hours=3, minutes=4,
                                        seconds=5, microseconds=67890)) == \
                                                          '03:04:05.067890'



# Generated at 2022-06-12 19:50:24.291013
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=1)
    assert timedelta_format(timedelta) == '00:00:00.000000'

# Generated at 2022-06-12 19:50:34.620110
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1.5)) == '00:00:01.500000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1.5)) == '00:01:30.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format

# Generated at 2022-06-12 19:50:56.566766
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0, 0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(0, 1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(0, 60)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(0, 3601)) == '01:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(1, 0)) == '24:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1, 1)) == '24:00:01.000000'

# Generated at 2022-06-12 19:51:06.591605
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(0, 1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(0, 60)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(1)
    assert timedelta_parse('01:00:01.000000') == datetime_module.timedelta(1, 1)
    assert timedelta_parse('01:01:00.000000') == datetime_module.timedelta(1, 60)
    assert timedelta_parse('01:01:01.000000') == datetime_module.timed

# Generated at 2022-06-12 19:51:15.032265
# Unit test for function timedelta_parse

# Generated at 2022-06-12 19:51:20.393794
# Unit test for function timedelta_format
def test_timedelta_format():
    for i in range(1, 100):
        for j in range(1, 60):
            for k in range(1, 60):
                for l in range(1, 1000000):
                    assert (timedelta_parse(timedelta_format(
                        datetime_module.timedelta(hours=i, minutes=j, seconds=k,
                                                  microseconds=l)))
                            == datetime_module.timedelta(hours=i, minutes=j,
                                                         seconds=k,
                                                         microseconds=l))

# Generated at 2022-06-12 19:51:28.608526
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('10:02:03.123000') == datetime_module.timedelta(
        hours=10, minutes=2, seconds=3, microseconds=123000)
    assert timedelta_parse('10:02:03.002000') == datetime_module.timedelta(
        hours=10, minutes=2, seconds=3, microseconds=2000)
    assert timedelta_parse('10:02:03.000000') == datetime_module.timedelta(
        hours=10, minutes=2, seconds=3, microseconds=0)



# Generated at 2022-06-12 19:51:32.298609
# Unit test for function timedelta_format
def test_timedelta_format():
    delta = datetime_module.timedelta(days=4, hours=5, minutes=6,
                                      seconds=7.123456789)
    assert timedelta_format(delta) == '05:06:07.123457'



# Generated at 2022-06-12 19:51:40.945765
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000001') == \
           datetime_module.timedelta(microseconds=1)

    assert timedelta_parse('00:01:00.000001') == \
           datetime_module.timedelta(seconds=60, microseconds=1)

    assert timedelta_parse('00:00:01.000001') == \
           datetime_module.timedelta(seconds=1, microseconds=1)

    assert timedelta_parse('01:00:00.000001') == \
           datetime_module.timedelta(hours=1, microseconds=1)

    assert timedelta_parse('00:00:00.000000') == \
           datetime_module.timedelta()



# Generated at 2022-06-12 19:51:51.416873
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('10:20:30.123456') == datetime_module.timedelta(
        hours=10, minutes=20, seconds=30, microseconds=123456
    )
    assert timedelta_parse('10:20:30.1234') == datetime_module.timedelta(
        hours=10, minutes=20, seconds=30, microseconds=123400
    )
    assert timedelta_parse('10:20:30.12') == datetime_module.timedelta(
        hours=10, minutes=20, seconds=30, microseconds=120000
    )
    assert timedelta_parse('10:20:30') == datetime_module.timedelta(
        hours=10, minutes=20, seconds=30
    )

# Generated at 2022-06-12 19:52:01.808396
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(0, 0, 10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(0, 0, 100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(0, 0, 1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(0, 0, 10000)
    assert timedelta_parse

# Generated at 2022-06-12 19:52:05.065915
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                              seconds=3, microseconds=4)) == \
           '01:02:03.000004'



# Generated at 2022-06-12 19:52:40.556202
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('3:39:42.064717') == datetime_module.timedelta(
        hours=3, minutes=39, seconds=42, microseconds=64717
    )

test_timedelta_parse()
del test_timedelta_parse

# Generated at 2022-06-12 19:52:48.761569
# Unit test for function timedelta_format
def test_timedelta_format():
    td = datetime_module.timedelta(hours=3, minutes=14, seconds=15, microseconds=6)
    assert timedelta_format(td) == '03:14:15.000006'
    td = datetime_module.timedelta(hours=3, minutes=14, seconds=15, microseconds=60000)
    assert timedelta_format(td) == '03:14:15.006000'
    td = datetime_module.timedelta(hours=3, minutes=14, seconds=15, microseconds=600000)
    assert timedelta_format(td) == '03:14:15.060000'
    td = datetime_module.timedelta(hours=3, minutes=14, seconds=15, microseconds=6000000)

# Generated at 2022-06-12 19:52:57.939233
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1)))==datetime_module.timedelta(hours=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=-1)))==datetime_module.timedelta(hours=-1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=1)))==datetime_module.timedelta(seconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=-1)))==datetime_module.timedelta(seconds=-1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(microseconds=1)))==datetime_module.timed

# Generated at 2022-06-12 19:53:01.889930
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:23:45.678901') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=45, microseconds=678901
    )

# Generated at 2022-06-12 19:53:11.214848
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
    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=1, seconds=1,
                                  microseconds=1)
    ) == '01:01:01.000001'

# Generated at 2022-06-12 19:53:18.252337
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                                                                '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
                                                microseconds=123456)) == \
                                                            '00:00:00.123456'
    assert timedelta_format(datetime_module.timedelta(
                                                microseconds=123456789)) == \
                                                            '00:02:03.456789'
    assert timedelta_format(datetime_module.timedelta(
                                                    seconds=123456789)) == \
                                                           '34:17:36.456789'

# Generated at 2022-06-12 19:53:29.614612
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=9)) == '00:00:00.000009'
    assert timedelta_format(datetime_module.timedelta(microseconds=99)) == '00:00:00.000099'
    assert timedelta_format(datetime_module.timedelta(microseconds=999)) == '00:00:00.000999'
    assert timedelta_

# Generated at 2022-06-12 19:53:33.789361
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('2:04:02.234567') == datetime_module.timedelta(
        hours=2, minutes=4, seconds=2, microseconds=234567
    )

# Generated at 2022-06-12 19:53:41.121442
# Unit test for function timedelta_format
def test_timedelta_format(): # todo: test on different timezones
    assert timedelta_format(datetime_module.timedelta(hours=9,
                                                      minutes=42,
                                                      seconds=8,
                                                      microseconds=123456)) == \
                                                          '09:42:08.123456'


if PY3:
    import typing as typing_module
    if sys.version_info[:2] >= (3, 7):
        typing_module_types = typing_module.types
    else:
        import types
        typing_module_types = types
    if sys.version_info[:2] >= (3, 6):
        typing_module_get_type_hints = typing_module.get_type_hints
    else:
        import typing
        typing_module_get_type_hints = typing

# Generated at 2022-06-12 19:53:52.729795
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0, microseconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=10, microseconds=0)) == '00:00:10.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=0, microseconds=10)) == '00:00:00.000010'
    assert timedelta_format(datetime_module.timedelta(seconds=0, microseconds=10000)) == '00:00:00.010000'
    assert timedelta_format(datetime_module.timedelta(seconds=0, microseconds=100000)) == '00:00:00.100000'

# Generated at 2022-06-12 19:55:02.497976
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=10, seconds=1)) ==\
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=100)) ==\
           '00:00:01.000100'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) ==\
           '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=10)) ==\
           '10:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=10,
                                                      microseconds=10)) ==\
           '10:00:00.000010'



# Generated at 2022-06-12 19:55:11.728822
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('22:47:40.0') == datetime_module.timedelta(
        hours=22, minutes=47, seconds=40, microseconds=0
    )
    assert timedelta_parse('22:47:40.1') == datetime_module.timedelta(
        hours=22, minutes=47, seconds=40, microseconds=100
    )
    assert timedelta_parse('22:47:40.12') == datetime_module.timedelta(
        hours=22, minutes=47, seconds=40, microseconds=120
    )
    assert timedelta_parse('22:47:40.123') == datetime_module.timedelta(
        hours=22, minutes=47, seconds=40, microseconds=123
    )

# Generated at 2022-06-12 19:55:20.649873
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta, result in (
        (datetime_module.timedelta(), '00:00:00.000000'),
        (datetime_module.timedelta(days=1, hours=2, minutes=3, seconds=4,
                                   microseconds=5),
         '02:03:04.000005'),
        (datetime_module.timedelta(days=-1, hours=-2, minutes=-3, seconds=-4,
                                   microseconds=-5),
         '-02:03:04.000005'),
    ):
        assert timedelta_format(timedelta) == result
        assert timedelta_parse(timedelta_format(timedelta)) == timedelta

test_timedelta_format()

# Generated at 2022-06-12 19:55:29.415182
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
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      microseconds=1)) == \
                                    '01:00:00.000001'

# Generated at 2022-06-12 19:55:35.993059
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(0))) == (
        datetime_module.timedelta(0))

    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=25, minutes=4)
    )) == datetime_module.timedelta(hours=25, minutes=4)

    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(microseconds=30000)
    )) == datetime_module.timedelta(microseconds=30000)

# Generated at 2022-06-12 19:55:46.703394
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == \
                                          datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        seconds=3600)
    )) == datetime_module.timedelta(seconds=3600)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, days=1, seconds=3600)
    )) == datetime_module.timedelta(days=2, seconds=3600)



if PY3:
    from contextlib import AbstractContextManager
else:
    class AbstractContextManager(object):
        __metaclass__ = abc.ABCMeta


# Generated at 2022-06-12 19:55:51.285334
# Unit test for function timedelta_format
def test_timedelta_format():
    format_for_testing = timedelta_format(
        datetime_module.timedelta(hours=5, minutes=8, seconds=13,
                                  microseconds=567890)
    )
    assert format_for_testing == '05:08:13.567890'



# Generated at 2022-06-12 19:55:58.020037
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(
        '00:00:04.123456'
    ) == datetime_module.timedelta(seconds=4, microseconds=123456)
    assert timedelta_parse(
        '00:04:00.123456'
    ) == datetime_module.timedelta(minutes=4, microseconds=123456)
    assert timedelta_parse(
        '04:00:00.123456'
    ) == datetime_module.timedelta(hours=4, microseconds=123456)
    assert timedelta_parse(
        '00:00:00.123456'
    ) == datetime_module.timedelta(microseconds=123456)
    assert timedelta_parse(
        '00:00:00.123456'
    ) == datetime_module.timed

# Generated at 2022-06-12 19:56:04.385059
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(timedelta_parse('01:02:03.123456')) == '01:02:03.123456'
    assert timedelta_format(timedelta_parse('123:02:03.123456')) == '123:02:03.123456'
    assert timedelta_format(timedelta_parse('03:02:03.123456')) == '03:02:03.123456'

