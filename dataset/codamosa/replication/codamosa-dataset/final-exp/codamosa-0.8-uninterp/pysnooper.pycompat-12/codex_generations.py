

# Generated at 2022-06-12 19:46:18.196493
# Unit test for function timedelta_parse
def test_timedelta_parse():
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
    assert timedelta_parse('0:01:00.000001') == datetime_module.timedelta(
        minutes=1, microseconds=1
    )

# Generated at 2022-06-12 19:46:25.631137
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(days=2, hours=3,
                                                      minutes=4,
                                                      seconds=5,
                                                      microseconds=45)) == \
        '03:04:05.000045'

    assert timedelta_parse('03:04:05.000045') == \
        datetime_module.timedelta(days=2, hours=3, minutes=4, seconds=5,
                                  microseconds=45)
    
    assert timedelta_parse('03:04:05.45') == \
        datetime_module.timedelta(days=2, hours=3, minutes=4, seconds=5,
                                  microseconds=450000)

    assert timedelta_parse('03:04:05.045') == \
        datetime_module.tim

# Generated at 2022-06-12 19:46:32.261979
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=4)
    assert timedelta == timedelta_parse(timedelta_format(timedelta))

    timedelta = datetime_module.timedelta(hours=3, minutes=2, seconds=1)
    assert timedelta == timedelta_parse(timedelta_format(timedelta))

    timedelta = datetime_module.timedelta(hours=3, minutes=2, seconds=1,
                                          microseconds=51)
    assert timedelta == timedelta_parse(timedelta_format(timedelta))

# Generated at 2022-06-12 19:46:35.321641
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(1, 0, 0)) == \
           '24:00:00.000000'



# Generated at 2022-06-12 19:46:43.998499
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000') == datetime_module.timedelta(0)
    assert timedelta_parse('0:00:00.123') == datetime_module.timedelta(0, 0, 123)
    assert timedelta_parse('0:01:00.000') == datetime_module.timedelta(0, 60)
    assert timedelta_parse('0:01:00.123') == datetime_module.timedelta(0, 60, 123)
    assert timedelta_parse('0:01:01.000') == datetime_module.timedelta(0, 61)
    assert timedelta_parse('0:01:01.123') == datetime_module.timedelta(0, 61, 123)
    assert timedelta_parse('1:00:00.000')

# Generated at 2022-06-12 19:46:56.112729
# Unit test for function timedelta_format
def test_timedelta_format():
    from garlicsim.general_misc.nifty_collections.ordered_dict \
        import OrderedDict
    from .assertions import assert_equal
    test_pairs = OrderedDict((
        (datetime_module.timedelta(0),
         '00:00:00.000000'),
        (datetime_module.timedelta(seconds=1),
         '00:00:01.000000'),
        (datetime_module.timedelta(microseconds=1),
         '00:00:00.000001'),
        (datetime_module.timedelta(days=1, hours=1, minutes=1, seconds=1,
                                   microseconds=1),
         '25:01:01.000001'),
    ))
    for timedelta, reference in test_pairs.items():
        assert_

# Generated at 2022-06-12 19:47:01.133085
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import nose
    nose.tools.assert_equal(timedelta_parse('13:37:01.123456'),
                            datetime_module.timedelta(hours=13, minutes=37,
                                                      seconds=1,
                                                      microseconds=123456))

# Generated at 2022-06-12 19:47:04.762310
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('10:59:45.736000') == (datetime_module.timedelta(
        hours=10, minutes=59, seconds=45, microseconds=736000
    ))



# Generated at 2022-06-12 19:47:16.023314
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3,
        microseconds=123456
    )) == '01:02:03.123456'
    assert timedelta_format(datetime_module.timedelta(
        hours=10, minutes=20, seconds=3,
        microseconds=123456
    )) == '10:20:03.123456'
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3,
        microseconds=123
    )) == '01:02:03.000123'

# Generated at 2022-06-12 19:47:23.783557
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=4,
                                          microseconds=56789)
    assert timedelta_format(timedelta) == '01:02:04.56789'
    timedelta = datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                                          microseconds=999999)
    assert timedelta_format(timedelta) == '23:59:59.999999'
    timedelta = datetime_module.timedelta(microseconds=1)
    assert timedelta_format(timedelta) == '00:00:00.000001'


# Generated at 2022-06-12 19:47:39.239046
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('10:20:30.111111') == datetime_module.timedelta(
        hours=10, minutes=20, seconds=30, microseconds=111111
    )


if PY3:
    from builtins import int as int_type
    from builtins import float as float_type
    from builtins import complex as complex_type
    from builtins import bool as bool_type
    from builtins import str as str_type
    from builtins import unicode as unicode_type
else:
    int_type = int
    float_type = float
    complex_type = complex
    bool_type = bool
    # `str` is `bytes` in Python 2, so `str_type` means `bytes`:
    str_type = str
    # `str` is `unicode` in Python

# Generated at 2022-06-12 19:47:45.246222
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0, 0, 5)) == '00:00:00.000005'
    assert timedelta_format(datetime_module.timedelta(0, 5)) == '00:00:05.000000'
    assert timedelta_format(datetime_module.timedelta(5)) == '05:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=5)) == '05:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=5.5)) == '05:12:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=5.5, microseconds=5)) == '05:12:00.000005'

#

# Generated at 2022-06-12 19:47:53.899006
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:48:03.758810
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('00:00:00.123450')) == \
                                                          '00:00:00.123450'
    assert timedelta_format(timedelta_parse(':00.123450')) == '00:00:00.123450'
    assert timedelta_format(timedelta_parse('0.123450')) == '00:00:00.123450'
    assert timedelta_format(timedelta_parse('.123450')) == '00:00:00.123450'
    assert timedelta_format(timedelta_parse('123450')) == '00:00:00.123450'

# Generated at 2022-06-12 19:48:10.117404
# Unit test for function timedelta_format
def test_timedelta_format():
    import datetime
    assert timedelta_format(datetime.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime.timedelta(seconds=11)) == '00:00:11.000000'
    assert timedelta_format(datetime.timedelta(seconds=111)) == '00:01:51.000000'
    assert timedelta_format(datetime.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime.timedelta(microseconds=11)) == '00:00:00.000011'
    assert timedelta_format(datetime.timedelta(microseconds=111)) == '00:00:00.000111'

# Generated at 2022-06-12 19:48:14.323554
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=23,
                                                      minutes=59,
                                                      seconds=59,
                                                      microseconds=999999)) == \
                                                      '23:59:59.999999'



# Generated at 2022-06-12 19:48:20.792714
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                                  microseconds=999999)
    ) == '23:59:59.999999'
    assert timedelta_format(
        datetime_module.timedelta(hours=23, minutes=59, seconds=59,
                                  microseconds=999)
    ) == '23:59:59.000999'



# Generated at 2022-06-12 19:48:27.917255
# Unit test for function timedelta_format
def test_timedelta_format():
    import pytest

# Generated at 2022-06-12 19:48:32.171466
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456
    )



# Generated at 2022-06-12 19:48:36.363310
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        seconds=188, microseconds=123456
    ))) == datetime_module.timedelta(seconds=188, microseconds=123456)

# Generated at 2022-06-12 19:48:51.902664
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=2, minutes=1, seconds=30,
                                   microseconds=5)
    assert timedelta_format(timedelta) == '02:01:30.000005'
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:48:59.003951
# Unit test for function timedelta_parse
def test_timedelta_parse():

    # Test parsing a duration with microseconds.
    assert timedelta_parse('1:23:45.123456') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=45, microseconds=123456
    )

    # Test parsing a duration without microseconds.
    assert timedelta_parse('1:23:45') == datetime_module.timedelta(
        hours=1, minutes=23, seconds=45
    )

    # Test that it doesn't work for a duration that has lower time units.
    with pytest.raises(ValueError):
         timedelta_parse('3600')



# Generated at 2022-06-12 19:49:04.366497
# Unit test for function timedelta_format
def test_timedelta_format():
    '''
    Test our implementation of `timedelta_format` by comparing against the
    standard `strftime "%H:%M:%S.%f"`, which is broken in Python 2.
    '''
    timedelta = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=123456)
    assert timedelta_format(timedelta) == '01:02:03.123456'



# Generated at 2022-06-12 19:49:07.534099
# Unit test for function timedelta_format
def test_timedelta_format():
    import pytest
    timedelta = datetime_module.timedelta(hours=5, minutes=6, seconds=7,
                                          microseconds=123456)
    assert timedelta_format(timedelta) == '05:06:07.123456'


# Generated at 2022-06-12 19:49:11.976494
# Unit test for function timedelta_parse
def test_timedelta_parse():
    for string in ('01:02:03.123456', '01:02:03:123456'):
        td = timedelta_parse(string)
        assert td.days == 0
        assert td.seconds == 1 * 60 * 60 + 2 * 60 + 3
        assert td.microseconds == 123456
        assert timedelta_format(td) == string.replace(':', '.')

# Generated at 2022-06-12 19:49:14.778284
# Unit test for function timedelta_format
def test_timedelta_format():
    time = time_isoformat(datetime_module.time(0, 0, 0, 0))
    assert time == '00:00:00.000000'
    time = time_isoformat(datetime_module.time(12, 45, 59, 987654))
    assert time == '12:45:59.987654'


# Generated at 2022-06-12 19:49:27.583901
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(0, 1)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(0, 60)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(0, 3600)
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(microseconds=10)
    assert timedelta_parse('00:00:00.000100')

# Generated at 2022-06-12 19:49:38.701950
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0') == timedelta_parse('00:00:00')
    assert timedelta_parse('0') == timedelta_parse('00:00:00.000000')
    assert timedelta_parse('6') == timedelta_parse('00:00:06')
    assert timedelta_parse('6') == timedelta_parse('00:00:06.000000')
    assert timedelta_parse('20300000') == timedelta_parse('00:00:20.300000')
    assert timedelta_parse('20300000') == timedelta_parse('00:00:20.300000')
    assert timedelta_parse('20:30:00.000000') == timedelta_parse(
        '20:30:00'
    )

# Generated at 2022-06-12 19:49:41.374004
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(
        hours=1, minutes=2, seconds=3,
        microseconds=123456
    )

    assert timedelta_format(timedelta) == '01:02:03.123456'

# Generated at 2022-06-12 19:49:46.109964
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=2, hours=4,
                                                      minutes=6,
                                                      seconds=8,
                                                      microseconds=15)) == \
           '04:06:08.000015'



# Generated at 2022-06-12 19:50:14.469371
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1, microseconds=1)) == '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(days=1, hours=2,
                                                      minutes=3, seconds=4,
                                                      microseconds=5)) == \
                                                      '02:03:04.000005'
    assert timedelta_

# Generated at 2022-06-12 19:50:17.698192
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    ))) == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )


# Generated at 2022-06-12 19:50:25.435639
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == \
                                                            datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=7))) == \
                                                            datetime_module.timedelta(days=7)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=7, hours=23))) == \
                                                        datetime_module.timedelta(days=7, hours=23)

# Generated at 2022-06-12 19:50:29.412820
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.412000') == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=412000)

# Generated at 2022-06-12 19:50:38.384071
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=1))) == datetime_module.timedelta(seconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=2))) == datetime_module.timedelta(seconds=2)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(microseconds=1))) == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=1))) == datetime_module.timedelta(days=1)

# Generated at 2022-06-12 19:50:45.619102
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import random
    for _ in range(100):
        hours = random.randrange(0, 100)
        minutes = random.randrange(0, 60)
        seconds = random.randrange(0, 60)
        microseconds = random.randrange(0, 1000000)
        td_original = datetime_module.timedelta(
            hours=hours, minutes=minutes, seconds=seconds,
            microseconds=microseconds
        )
        td_roundtripped = timedelta_parse(timedelta_format(td_original))
        assert td_roundtripped == td_original, (td_original, td_roundtripped)



# Generated at 2022-06-12 19:50:49.818844
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=1, minutes=1, seconds=1,
                                  microseconds=1)
    ) == '01:01:01.000001'



# Generated at 2022-06-12 19:50:55.489208
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('01:00:01.000001') == datetime_module.timedelta(
        hours=1, seconds=1, microseconds=1
    )
    assert timedelta_parse('01:02:03.000004') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )

# Generated at 2022-06-12 19:50:58.627848
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('0:00:00.123456')) == \
        '00:00:00.123456'
    assert timedelta_format(timedelta_parse('0:00:00.123456')) == \
        '00:00:00.123456'


# Generated at 2022-06-12 19:51:09.433234
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(timedelta_parse('1:22:33.444444')) == \
           '01:22:33.444444'
    assert timedelta_format(timedelta_parse('4:33:22.333333')) == \
           '04:33:22.333333'
    assert timedelta_format(timedelta_parse('0:33:22.111111')) == \
           '00:33:22.111111'
    assert timedelta_format(timedelta_parse('0:33:22.666666')) == \
           '00:33:22.666666'
    assert timedelta_format(timedelta_parse('0:03:22.666666')) == \
           '00:03:22.666666'

# Generated at 2022-06-12 19:51:55.410206
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('12:34:56.000789') == datetime_module.timedelta(
        hours=12, minutes=34, seconds=56, microseconds=789
    )
    assert timedelta_parse('12:34:56') == datetime_module.timedelta(
        hours=12, minutes=34, seconds=56
    )
    assert timedelta_parse('56.123456') == datetime_module.timedelta(
        seconds=56, microseconds=123456
    )
    assert timedelta_parse('12:34:56:1200:45:1000') == datetime_module.timedelta(
        days=12, hours=34, minutes=56, seconds=1200, microseconds=451000
    )

# Generated at 2022-06-12 19:52:01.865831
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.004000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )
    assert timedelta_parse('-01:02:03.004000') == datetime_module.timedelta(
        hours=-1, minutes=-2, seconds=-3, microseconds=-4
    )

test_timedelta_parse()
del test_timedelta_parse

# Generated at 2022-06-12 19:52:08.949214
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:1.000000') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('23:59:59.999999') == datetime_module.timedelta(days=1)
    assert timedelta_parse('1:2:3.456789') == datetime_module.timedelta(hours=1,
                                                                         minutes=2,
                                                                         seconds=3,
                                                                         microseconds=456789)



# Generated at 2022-06-12 19:52:18.154305
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == \
                                               datetime_module.timedelta(0)
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(days=2)
    )) == datetime_module.timedelta(days=2)
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(microseconds=100)
    )) == datetime_module.timedelta(microseconds=100)
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(days=3650)
    )) == datetime_module.timedelta(days=3650)

# Generated at 2022-06-12 19:52:22.681195
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:10.5') == datetime_module.timedelta(0, 10,
                                                                      500000)
    assert timedelta_parse('01:02:03.456789') == datetime_module.timedelta(
        1, 7323, 456789
    )



# Generated at 2022-06-12 19:52:27.960900
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1))) == \
           datetime_module.timedelta(hours=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1,
                                                                      minutes=2))) \
                                                                      == \
           datetime_module.timedelta(hours=1, minutes=2)

    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1,
                                                                      minutes=2,
                                                                      seconds=3))) \
                                                                      == \
           datetime_module.timedelta(hours=1, minutes=2, seconds=3)


# Generated at 2022-06-12 19:52:35.827664
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=12)) == '00:00:00.000012'
    assert timedelta_format(datetime_module.timedelta(microseconds=123)) == '00:00:00.000123'
    assert timedelta_format(datetime_module.timedelta(microseconds=1234)) == '00:00:00.001234'
    assert timedelta_format(datetime_module.timedelta(microseconds=12345)) == '00:00:00.012345'
    assert timed

# Generated at 2022-06-12 19:52:40.452596
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=12, minutes=34,
                                          seconds=56, microseconds=789012)
    assert timedelta_format(timedelta) == '12:34:56.789012'



# Generated at 2022-06-12 19:52:48.696241
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.009999') == datetime_module.timedelta(
        0, 0, 9999
    )
    assert timedelta_parse('00:00:01.009999') == datetime_module.timedelta(
        0, 1, 9999
    )
    assert timedelta_parse('00:01:00.009999') == datetime_module.timedelta(
        0, 60, 9999
    )
    assert timedelta_parse('00:01:01.009999') == datetime_module.timedelta(
        0, 61, 9999
    )
    assert timedelta_parse('01:00:00.009999') == datetime_module.timedelta(
        0, 3600, 9999
    )

# Generated at 2022-06-12 19:52:54.198889
# Unit test for function timedelta_parse
def test_timedelta_parse():
    delta = datetime_module.timedelta(hours=20, seconds=20, minutes=20,
                                      microseconds=20)
    assert timedelta_parse(timedelta_format(delta)) == delta


if sys.version_info[0] == 2:
    import __builtin__
    raw_input = getattr(__builtin__, 'raw_input')
else:
    def raw_input(prompt=None):
        """Builtin `input` in Python 2; `input` in Python 3."""
        if prompt:
            print(prompt, end='')
        return input()

# Generated at 2022-06-12 19:54:27.770248
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=11)) == \
                                                                 '00:00:11.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=11,
                                                      microseconds=5)) == \
                                                                 '00:00:11.000005'
    assert timedelta_format(datetime_module.timedelta(minutes=11,
                                                      microseconds=5)) == \
                                                              '00:11:00.000005'
    assert timedelta_format(datetime_module.timedelta(days=11,
                                                      microseconds=5)) == \
                                                            '264:00:00.000005'

# Generated at 2022-06-12 19:54:32.396008
# Unit test for function timedelta_format
def test_timedelta_format():
    for timedelta in (
        datetime_module.timedelta(hours=5, minutes=7, seconds=11, microseconds=13),
        datetime_module.timedelta(days=5, hours=7, minutes=11, seconds=13),
    ):
        assert timedelta_parse(timedelta_format(timedelta)) == timedelta

# Generated at 2022-06-12 19:54:42.541946
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == \
           datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('01:23:45.678901') == \
           datetime_module.timedelta(hours=1, minutes=23, seconds=45,
                                     microseconds=678901)
    assert timedelta_parse('10:11:12.131415') == \
           datetime_module.timedelta(hours=10, minutes=11, seconds=12,
                                     microseconds=131415)

# Generated at 2022-06-12 19:54:48.650510
# Unit test for function timedelta_parse

# Generated at 2022-06-12 19:54:53.706877
# Unit test for function timedelta_format
def test_timedelta_format():
    import datetime
    timedelta = datetime.timedelta(days=1, hours=3, minutes=5, seconds=7,
                                   microseconds=9)
    assert timedelta_format(timedelta) == '03:05:07.000009'
    assert timedelta_parse('03:05:07.000009') == timedelta



# Generated at 2022-06-12 19:55:03.436017
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.00') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0.1') == datetime_module.timedelta(
        microseconds=100
    )
    assert timedelta_parse('1:1:1.01') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=10000
    )
    assert timedelta_parse('356:59:59.999999') == datetime_module.timedelta(
        days=356, hours=23, minutes=59, seconds=59, microseconds=999999
    )

# Generated at 2022-06-12 19:55:12.628877
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0.1') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('0:0:0.10') == datetime_module.timedelta(0, 0, 10)
    assert timedelta_parse('1:2:3.4') == datetime_module.timedelta(1, 7260, 400000)
    assert timedelta_parse('1:2:3.400000') == datetime_module.timedelta(1, 7260, 400000)
    assert timedelta_parse('.1') == datetime_module.timedelta(0, 0, 1)

# Generated at 2022-06-12 19:55:18.667916
# Unit test for function timedelta_format
def test_timedelta_format():
    unit = datetime_module.timedelta(microseconds=1)
    assert timedelta_format(unit) == '00:00:00.000001'
    assert timedelta_format(13 * unit) == '00:00:00.000013'
    assert timedelta_format(999 * unit) == '00:00:00.000999'
    assert timedelta_format(1000 * unit) == '00:00:00.001000'
    assert timedelta_format(1999 * unit) == '00:00:00.001999'
    assert timedelta_format(100000 * unit) == '00:00:00.100000'
    assert timedelta_format(999999 * unit) == '00:00:00.999999'

# Generated at 2022-06-12 19:55:21.703007
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(minutes=5,
                                                      seconds=5,
                                                      microseconds=50)) == \
           '00:05:05.000050'
    assert timedelta_parse('00:05:05.000050') == \
           datetime_module.timedelta(minutes=5, seconds=5, microseconds=50)

# Generated at 2022-06-12 19:55:29.833003
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:0:0.0') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('1:0:0.0') != datetime_module.timedelta(hours=1.1)
    assert timedelta_parse('1:0:0.0') != datetime_module.timedelta(hours=1.01)
    assert timedelta_parse('1:0:0.0') != datetime_module.timedelta(hours=1.001)
    assert timedelta_parse('1:0:0.0') != datetime_module.timedelta(hours=1.0001)
    assert timedelta_parse('1:0:0.000009') != datetime_module.timedelta(hours=1)