

# Generated at 2022-06-12 19:46:19.096710
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:46:23.211214
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:21:34.567891') == datetime_module.timedelta(
        minutes=21, seconds=34, microseconds=567891
    )

    assert timedelta_parse('2:03:58.207778') == datetime_module.timedelta(
        hours=2, minutes=3, seconds=58, microseconds=207778
    )



# Generated at 2022-06-12 19:46:27.683662
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1,
                                                      hours=2,
                                                      minutes=3,
                                                      seconds=4,
                                                      microseconds=5)) == (
        '02:03:04.000005')



# Generated at 2022-06-12 19:46:28.974797
# Unit test for function timedelta_parse
def test_timedelta_parse():
    datetime_delta = datetime_module.datetime.now() - datetime_module.datetime.now()
    assert timedelta_format(datetime_delta) == timedelta_format(timedelta_parse(timedelta_format(datetime_delta)))



# Generated at 2022-06-12 19:46:33.678882
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:01:01.010101') == \
                                 datetime_module.timedelta(hours=1,
                                                           minutes=1,
                                                           seconds=1,
                                                           microseconds=10)

# Generated at 2022-06-12 19:46:39.470746
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(
        seconds=0
    )
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1
    )
    assert timedelta_parse('23:59:59.999999') == datetime_module.timedelta(
        days=1, seconds=-1
    )

# Generated at 2022-06-12 19:46:42.359321
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for timedelta in (datetime_module.timedelta(seconds=i)
                      for i in range(1000)):
        s = timedelta_format(timedelta)
        assert timedelta == timedelta_parse(s)

# Generated at 2022-06-12 19:46:46.277787
# Unit test for function timedelta_format
def test_timedelta_format():
    '''Unit test for `timedelta_format`.'''
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        days=1, hours=2, minutes=3, seconds=4, microseconds=5
    )) == '26:03:04.000005'

# Generated at 2022-06-12 19:46:51.260139
# Unit test for function timedelta_parse
def test_timedelta_parse():
    s = '00:00:00.000000'
    assert timedelta_format(timedelta_parse(s)) == s

    s = '01:02:03.004000'
    assert timedelta_format(timedelta_parse(s)) == s

    s = '04:05:06.007000'
    assert timedelta_format(timedelta_parse(s)) == s

    s = '07:08:09.010000'
    assert timedelta_format(timedelta_parse(s)) == s

    s = '10:11:12.013000'
    assert timedelta_format(timedelta_parse(s)) == s

    s = '13:14:15.016000'
    assert timedelta_format(timedelta_parse(s)) == s


# Generated at 2022-06-12 19:47:01.008214
# Unit test for function timedelta_format
def test_timedelta_format():
    assert '00:00:00.000000' == timedelta_format(datetime_module.timedelta())
    assert '01:02:03.000000' == timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3)
    )
    assert '01:02:03.000000' == timedelta_format(
        datetime_module.timedelta(days=1, hours=1, minutes=2, seconds=3)
    )
    assert '01:02:03.004000' == timedelta_format(
        datetime_module.timedelta(days=1, hours=1, minutes=2, seconds=3,
                                  microseconds=4000)
    )

# Generated at 2022-06-12 19:47:18.478295
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=12)) == '12:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=10.5)) == '00:00:10.500000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=10)) == '00:00:00.000010'
    assert timedelta_format(datetime_module.timedelta(microseconds=100)) == '00:00:00.000100'
    assert timedelta

# Generated at 2022-06-12 19:47:26.432731
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(microseconds=10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(microseconds=100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(microseconds=1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(microseconds=10000)

# Generated at 2022-06-12 19:47:32.455582
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1,
    )
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(
        minutes=1,
    )
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(
        hours=1,
    )
    assert timedelta_parse('01:15:01.100000') == datetime_module.timedelta(
        hours=1, minutes=15, seconds=1,
        microseconds=100000,
    )



# Generated at 2022-06-12 19:47:35.693625
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.123456') == (
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=123456)
    )



# Generated at 2022-06-12 19:47:46.389042
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from python_toolbox import cute_testing
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('00:00:00.999999') == datetime_module.timedelta(microseconds=999999)
    assert timedelta_parse

# Generated at 2022-06-12 19:47:54.726761
# Unit test for function timedelta_format
def test_timedelta_format():
    '''
    Verify that timedelta_format() works as we expect.
    '''
    from .python_toolbox.cute_testing import assert_equal

    assert_equal(timedelta_format(datetime_module.timedelta()),
                 '00:00:00.000000')

    assert_equal(timedelta_format(datetime_module.timedelta(seconds=1)),
                 '00:00:01.000000')

    assert_equal(timedelta_format(
                 datetime_module.timedelta(microseconds=1)),
                 '00:00:00.000001')


# Generated at 2022-06-12 19:48:04.529833
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(1000)) == '00:16:40.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(milliseconds=1)) == '00:00:00.001000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'

# Generated at 2022-06-12 19:48:06.969158
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=3, minutes=4,
                                                      seconds=5,
                                                      microseconds=678)) == \
                                                      '03:04:05.000678'

# Generated at 2022-06-12 19:48:17.142352
# Unit test for function timedelta_parse
def test_timedelta_parse():

    for timedelta in [
            datetime_module.timedelta(days=1),
            datetime_module.timedelta(seconds=0),
            datetime_module.timedelta(microseconds=1),
            datetime_module.timedelta(days=1, seconds=2, microseconds=3),
    ]:
        assert timedelta_parse(timedelta_format(timedelta)) == timedelta

    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0)
    assert timedelta_parse('0.0') == datetime_module.timedelta(0)

    assert timedelta_parse('1:0:0.000001') == datetime_module.timedelta(
        hours=1, microseconds=1
    )

    assert timedelta_

# Generated at 2022-06-12 19:48:20.315075
# Unit test for function timedelta_format
def test_timedelta_format():
    # type: () -> None
    import doctest
    doctest.testmod(verbose=False)



# Generated at 2022-06-12 19:48:41.622820
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
        '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=1)) == \
        '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=10)) == \
        '00:00:01.000010'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=100)) == \
        '00:00:01.000100'

# Generated at 2022-06-12 19:48:45.218142
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=12, minutes=34,
                                                      seconds=56,
                                                      microseconds=789)) == \
                                                      '12:34:56.000789'



# Generated at 2022-06-12 19:48:53.994023
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0') == timedelta_parse('00') == timedelta_parse(
        '00:00'
    ) == timedelta_parse('00:00:00') == timedelta_parse('00:00:00.000000') == \
                                        timedelta_parse('00:00:00.000123')
    assert timedelta_parse('1') == timedelta_parse('01') == timedelta_parse(
        '01:00'
    ) == timedelta_parse('01:00:00') == timedelta_parse('01:00:00.000000') == \
                                        timedelta_parse('01:00:00.000123')
    assert timedelta_parse('12') == timedelta_parse('12:00') == timedelta_parse(
        '12:00:00'
    ) == timedelta_

# Generated at 2022-06-12 19:48:59.426715
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        years=1, days=1, minutes=2, seconds=3, microseconds=4
    )) == '26:02:03.000004'
    assert timedelta_format(datetime_module.timedelta(days=2)) == '48:00:00.000000'



# Generated at 2022-06-12 19:49:05.641275
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
           '00:00:01.000000'

    assert timedelta_format(datetime_module.timedelta(seconds=60)) == \
           '00:01:00.000000'

    assert timedelta_format(datetime_module.timedelta(minutes=1,
                                                      microseconds=1)) == \
           '00:01:00.000001'




# Generated at 2022-06-12 19:49:13.264161
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from . import testing_tools
    assert timedelta_parse('19:22:47') == \
           datetime_module.timedelta(hours=19, minutes=22, seconds=47)
    assert timedelta_parse('19:22:47.123456') == \
           datetime_module.timedelta(hours=19, minutes=22, seconds=47,
                                     microseconds=123456)
    testing_tools.assert_raises(ValueError, timedelta_parse, '19:22')
    testing_tools.assert_raises(ValueError, timedelta_parse, '19:22:47.1234567')
    testing_tools.assert_raises(ValueError, timedelta_parse, '19:22:47.1234')

# Generated at 2022-06-12 19:49:26.597046
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=1)
    )) == datetime_module.timedelta(hours=1)
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(days=2, hours=1, minutes=3, seconds=4)
    )) == datetime_module.timedelta(days=2, hours=1, minutes=3, seconds=4)
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(minutes=2, seconds=1, microseconds=123456)
    )) == datetime_module.timedelta(minutes=2, seconds=1, microseconds=123456)



# Generated at 2022-06-12 19:49:34.334359
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=1)) == '01:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=1, microseconds=1)) == '01:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1, microseconds=1)) == '01:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1, seconds=1, microseconds=1)) == '01:01:01.000001'


# Generated at 2022-06-12 19:49:39.345029
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(microseconds=1)
    )) == datetime_module.timedelta(microseconds=1)

    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(days=1)
    )) == datetime_module.timedelta(days=1)

# Generated at 2022-06-12 19:49:44.151007
# Unit test for function timedelta_format
def test_timedelta_format():
    def test(timedelta, expected_result):
        result = timedelta_format(timedelta)
        assert result == expected_result


# Generated at 2022-06-12 19:50:05.224413
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
                      '00:00:00.000001'

    assert timedelta_format(datetime_module.timedelta(microseconds=12)) == \
                      '00:00:00.000012'

    assert timedelta_format(datetime_module.timedelta(microseconds=123)) == \
                      '00:00:00.000123'

    assert timedelta_format(datetime_module.timedelta(microseconds=1234)) == \
                      '00:00:00.001234'

    assert timedelta_format(datetime_module.timedelta(microseconds=12345)) == \
                      '00:00:00.012345'


# Generated at 2022-06-12 19:50:13.862633
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == \
                                            datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == \
                                            datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:01.000000') == \
                                            datetime_module.timedelta(0, 1)
    assert timedelta_parse('00:01:00.000000') == \
                                            datetime_module.timedelta(0, 60)
    assert timedelta_parse('01:00:00.000000') == \
                                            datetime_module.timedelta(1)
    assert timedelta_parse('01:01:01.000001') == \
                                            datetime_

# Generated at 2022-06-12 19:50:17.522155
# Unit test for function timedelta_format
def test_timedelta_format():
    assert (
        timedelta_format(
            datetime_module.timedelta(days=1, seconds=1, microseconds=1)
        ) ==
        '{}T00:00:01.000001'.format(datetime_module.datetime.min.date())
    )

# Generated at 2022-06-12 19:50:23.227377
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'



# Generated at 2022-06-12 19:50:29.848034
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=5, minutes=3, seconds=45,
                                          microseconds=123456)
    assert timedelta == timedelta_parse(timedelta_format(timedelta))
    # Test the sign:
    assert timedelta == timedelta_parse(timedelta_format(-timedelta))

# Generated at 2022-06-12 19:50:38.121937
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(milliseconds=1)) == '00:00:00.001000'
    assert timedelta_format(datetime_module.timedelta(seconds=1, milliseconds=1)) == '00:00:01.001000'
    assert timedelta_format(datetime_module.timedelta(minutes=1, milliseconds=1)) == '00:01:00.001000'
    assert timedelta_format(datetime_module.timedelta(days=1, milliseconds=1)) == '24:00:00.001000'


# Generated at 2022-06-12 19:50:42.287063
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=42, minutes=16, seconds=42,
                                          microseconds=16)
    assert timedelta_format(timedelta) == '42:16:42.000016'


# Generated at 2022-06-12 19:50:45.593638
# Unit test for function timedelta_format
def test_timedelta_format():
    for input_timedelta in (
        datetime_module.timedelta(hours=1),
        datetime_module.timedelta(minutes=2),
        datetime_module.timedelta(seconds=3),
        datetime_module.timedelta(microseconds=4),
        datetime_module.timedelta(hours=10, minutes=20, seconds=30,
                                  microseconds=405060),
    ):
        assert timedelta_parse(timedelta_format(input_timedelta)) == \
               input_timedelta





# Generated at 2022-06-12 19:50:55.916159
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=1)
    ))) == timedelta_format(datetime_module.timedelta(hours=1))

    assert timedelta_format(timedelta_parse(timedelta_format(
        datetime_module.timedelta(minutes=1)
    ))) == timedelta_format(datetime_module.timedelta(minutes=1))

    assert timedelta_format(timedelta_parse(timedelta_format(
        datetime_module.timedelta(seconds=1)
    ))) == timedelta_format(datetime_module.timedelta(seconds=1))


# Generated at 2022-06-12 19:51:01.290115
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0.111111') == datetime_module.timedelta(
        microseconds=111111
    )
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(
        seconds=1
    )
    assert timedelta_parse('1:0:0.000000') == datetime_module.timedelta(
        hours=1
    )



# Generated at 2022-06-12 19:51:25.297711
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.004123') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4123
    )



# Generated at 2022-06-12 19:51:28.876287
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=5, minutes=5, seconds=5,
                                          microseconds=5)
    assert timedelta_format(timedelta) == '05:05:05.000005'
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:51:38.607037
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=15,
                                                      minutes=11,
                                                      seconds=36,
                                                      microseconds=543123)) == \
                                                      '15:11:36.543123'
    assert timedelta_format(datetime_module.timedelta(hours=15,
                                                      minutes=11,
                                                      seconds=36,
                                                      microseconds=1)) == \
                                                      '15:11:36.000001'
    assert timedelta_format(datetime_module.timedelta(hours=15,
                                                      minutes=11,
                                                      seconds=36,
                                                      microseconds=0)) == \
                                                      '15:11:36.000000'


# Generated at 2022-06-12 19:51:49.900865
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=4)) == '04:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=4, minutes=5)) == '04:05:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=4, minutes=5, seconds=6)) == '04:05:06.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=4, minutes=5, seconds=6, microseconds=7)) == '04:05:06.000007'

#

# Generated at 2022-06-12 19:51:59.454010
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta in map(datetime_module.timedelta,
                         range(-1000000, 1000000, 111)):
        assert timedelta == timedelta_parse(timedelta_format(timedelta))

if not PY2:
    from contextlib import suppress
else:
    from contextlib import contextmanager
    @contextmanager
    def suppress(*exceptions):
        """Context manager to suppress specified exceptions
        After the exception is suppressed, execution proceeds with the next
        statement following the with statement.
        
        Usage:
        
        with suppress(FileNotFoundError):
            os.remove(somefile)
        """
        try:
            yield
        except exceptions:
            pass

# Generated at 2022-06-12 19:52:10.024931
# Unit test for function timedelta_parse
def test_timedelta_parse():
    s = '00:00:00.000000'
    assert timedelta_parse(s) == datetime_module.timedelta()
    s = '00:00:00.000001'
    assert timedelta_parse(s) == datetime_module.timedelta(microseconds=1)
    s = '00:00:00.000010'
    assert timedelta_parse(s) == datetime_module.timedelta(microseconds=10)
    s = '00:00:00.000100'
    assert timedelta_parse(s) == datetime_module.timedelta(microseconds=100)
    s = '00:00:00.001000'
    assert timedelta_parse(s) == datetime_module.timedelta(microseconds=1000)

# Generated at 2022-06-12 19:52:14.867929
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(0, 0, 10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(0, 0, 100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(0, 0, 1000)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(0, 1, 0)

# Generated at 2022-06-12 19:52:23.389827
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == (
        '00:00:00.000000'
    )
    assert timedelta_format(datetime_module.timedelta()) == (
        '00:00:00.000000'
    )
    assert timedelta_format(datetime_module.timedelta(hours=1)) == (
        '01:00:00.000000'
    )
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == (
        '00:01:00.000000'
    )
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == (
        '00:00:01.000000'
    )

# Generated at 2022-06-12 19:52:30.292680
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=1)
    assert timedelta_format(timedelta) == time_isoformat(timedelta, timespec='microseconds')
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta
    timedelta = datetime_module.timedelta(hours=7, minutes=6, seconds=5,
                                          microseconds=4)
    assert timedelta_format(timedelta) == time_isoformat(timedelta, timespec='microseconds')
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:52:34.767596
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == \
                            "00:00:00.000000"

    assert timedelta_format(datetime_module.timedelta(days=1,
                                                      seconds=3)) == \
                            "00:00:03.000000"

    assert timedelta_format(datetime_module.timedelta(days=1,
                                                      microseconds=3)) == \
                            "00:00:00.000003"

    assert timedelta_format(datetime_module.timedelta(days=1, hours=4,
                                                      minutes=5, seconds=6,
                                                      microseconds=7)) == \
                            "04:05:06.000007"



# Generated at 2022-06-12 19:53:23.619457
# Unit test for function timedelta_format
def test_timedelta_format():
    time = time_isoformat(
        datetime_module.time(hour=3, minute=4, second=5, microsecond=6)
    )
    assert time == '03:04:05.000006'
    time = time_isoformat(
        datetime_module.time(hour=0, minute=0, second=0, microsecond=0)
    )
    assert time == '00:00:00.000000'
    time = time_isoformat(
        datetime_module.time(hour=23, minute=59, second=58, microsecond=999999)
    )
    assert time == '23:59:58.999999'



# Generated at 2022-06-12 19:53:32.829250
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('0:0:0.1') == datetime_module.timedelta(
        microseconds=100000
    )
    assert timedelta_parse('0:0:1.1') == datetime_module.timedelta(
        seconds=1,
        microseconds=100000
    )
    assert timedelta_parse('0:1:1.1') == datetime_module.timedelta(
        minutes=1,
        seconds=1,
        microseconds=100000
    )

# Generated at 2022-06-12 19:53:35.880172
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=13, minutes=23, seconds=14, microseconds=123456
    )) == '13:23:14.123456'


# Generated at 2022-06-12 19:53:42.074180
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('0:00:01.000000') == datetime_module.timedelta(
        seconds=1
    )
    assert timedelta_parse('0:01:00.000000') == datetime_module.timedelta(
        minutes=1
    )
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(
        hours=1
    )

# Generated at 2022-06-12 19:53:53.283047
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert isinstance(timedelta_parse('1:2:3.4'), datetime_module.timedelta)
    assert timedelta_parse('1:2:3.4') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )
    assert timedelta_parse('1:2:3') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=0
    )
    assert timedelta_parse('1:2:3.40000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=40000
    )

# Generated at 2022-06-12 19:54:00.325621
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4567
    ))) == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=4567)


try:
    import configparser as _configparser
except ImportError:
    import ConfigParser as _configparser


# Generated at 2022-06-12 19:54:08.047939
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(weeks=1)) == '00:00:00.000000'



# Generated at 2022-06-12 19:54:17.454197
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('1:1:1.1')) == '01:01:01.001000'
    assert timedelta_format(timedelta_parse('1:1:1.111111')) == '01:01:01.111111'
    assert timedelta_format(timedelta_parse('1:1:1.1111')) == '01:01:01.001111'
    assert timedelta_format(timedelta_parse('1:1:1')) == '01:01:01.000000'
    assert timedelta_format(timedelta_parse('1:1:1.999999')) == '01:01:01.999999'

# Generated at 2022-06-12 19:54:21.129878
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=40005)) \
                                                      == '01:02:03.40005'



# Generated at 2022-06-12 19:54:24.873470
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == '01:02:03.000004'



# Generated at 2022-06-12 19:56:01.701680
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_parse('1:2:3.000000')
    assert timedelta == datetime_module.timedelta(hours=1, minutes=2, seconds=3)
    timedelta = timedelta_parse('-1:2:3.000000')
    assert timedelta == datetime_module.timedelta(hours=-1, minutes=2, seconds=3)
    timedelta = timedelta_parse('-1:02:3.000000')
    assert timedelta == datetime_module.timedelta(hours=-1, minutes=2, seconds=3)