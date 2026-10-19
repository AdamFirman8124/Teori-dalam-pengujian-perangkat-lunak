

# Generated at 2022-06-12 19:46:09.151010
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:1:1.1') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=100000
    )

test_timedelta_parse()

# Generated at 2022-06-12 19:46:14.055830
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=456)) \
           == '01:02:03.000456'


# Generated at 2022-06-12 19:46:17.043065
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=10, minutes=20, seconds=30,
                                          microseconds=405060)
    assert timedelta_format(timedelta) == '10:20:30.405060'



# Generated at 2022-06-12 19:46:22.231989
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=4, minutes=20,
                                                      seconds=36,
                                                      microseconds=123456)) == \
                                                      '04:20:36.123456'

timedelta_format.test = test_timedelta_format



# Generated at 2022-06-12 19:46:32.413398
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(microseconds=-1)) == \
           '23:59:59.999999'
    assert timedelta_format(datetime_module.timedelta(microseconds=0)) == \
           '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(microseconds=100)) == \
           '00:00:00.000100'
    assert timedelta_format(datetime_module.timedelta(microseconds=10000)) == \
           '00:00:00.010000'

# Generated at 2022-06-12 19:46:41.994914
# Unit test for function timedelta_parse
def test_timedelta_parse():
    times = [
        '00:00:00.000000',
        '01:02:03.123456',
        '45:45:45.454545',
        '99:99:99.999999',
    ]
    for time in times:
        assert timedelta_parse(time) == datetime_module.timedelta(
            hours=int(time[:2]),
            minutes=int(time[3:5]),
            seconds=int(time[6:8]),
            microseconds=int(time[9:])
        )
    for time in times + ['50:50:50.555555']:
        assert timedelta_format(timedelta_parse(time)) == time


if hasattr(datetime_module, 'timezone'):
    timezone = datetime_module.timezone
   

# Generated at 2022-06-12 19:46:53.298629
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('2:24:46.000000') == datetime_module.timedelta(
        hours=2, minutes=24, seconds=46
    )
    assert timedelta_parse('2:24:46.000001') == datetime_module.timedelta(
        hours=2, minutes=24, seconds=46, microseconds=1
    )
    assert timedelta_parse('2:24:46.999999') == datetime_module.timedelta(
        hours=2, minutes=24, seconds=46, microseconds=999999
    )
    assert timedelta_parse('2:24:46.0000004') \
        == timedelta_parse('2:24:46.000000')

# Generated at 2022-06-12 19:47:02.063939
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = datetime_module.timedelta(days=7, hours=4, seconds=3,
                                          microseconds=2)
    assert timedelta_format(timedelta) == '165:00:03.000002'
    assert timedelta_parse(timedelta_format(timedelta)) == timedelta


if PY3:

    def iterkeys(d):
        return iter(d.keys())

    def itervalues(d):
        return iter(d.values())

    def iteritems(d):
        return iter(d.items())

    viewkeys = lambda d: d.keys()
    viewvalues = lambda d: d.values()
    viewitems = lambda d: d.items()

else:

    def iterkeys(d):
        return d.iterkeys()


# Generated at 2022-06-12 19:47:06.227676
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=12, minutes=22, seconds=33, microseconds=444444))) \
           == datetime_module.timedelta(hours=12, minutes=22, seconds=33, microseconds=444444)

# Generated at 2022-06-12 19:47:17.192614
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=2)) == \
           '02:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=3,
                                                      microseconds=235)) == \
           '01:00:03.000235'
    assert timedelta_format(datetime_module.timedelta(seconds=3,
                                                      microseconds=235)) == \
           '00:00:03.000235'
    assert timedelta_format(datetime_module.timedelta(hours=1, seconds=6,
                                                      microseconds=9)) == \
           '01:00:06.000009'

# Generated at 2022-06-12 19:47:28.499177
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:08:07.123456') == datetime_module.timedelta(
        minutes=8,
        seconds=7,
        microseconds=123456,
    )

# Generated at 2022-06-12 19:47:36.456414
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4
    )) == '01:02:03.000004'

    assert timedelta_format(datetime_module.timedelta(
        hours=10, minutes=11, seconds=12, microseconds=13
    )) == '10:11:12.000013'

    assert timedelta_format(datetime_module.timedelta(
        hours=100, minutes=110, seconds=120, microseconds=130
    )) == '100:110:120.000130'



# Generated at 2022-06-12 19:47:37.943304
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(timedelta_parse('1:02:03.000045')) == \
                                                  '01:02:03.000045'


# Generated at 2022-06-12 19:47:48.533227
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:01:00.01') == datetime_module.timedelta(
        minutes=1, seconds=0, milliseconds=10
    )
    assert timedelta_parse('00:01:00.010000') == datetime_module.timedelta(
        minutes=1, seconds=0, milliseconds=10
    )
    assert timedelta_parse('00:01:00.01000000') == datetime_module.timedelta(
        minutes=1, seconds=0, milliseconds=10
    )
    assert timedelta_parse('00:01:00.1') == datetime_module.timedelta(
        minutes=1, seconds=0, milliseconds=100
    )

# Generated at 2022-06-12 19:47:56.137522
# Unit test for function timedelta_format
def test_timedelta_format():
    timedeltas = [
        datetime_module.timedelta(),
        datetime_module.timedelta(microseconds=1),
        datetime_module.timedelta(milliseconds=1),
        datetime_module.timedelta(seconds=1),
        datetime_module.timedelta(minutes=1),
        datetime_module.timedelta(hours=1),
        datetime_module.timedelta(days=1),
        datetime_module.timedelta(weeks=1),
    ]

    assert timedelta_format(timedeltas[0]) == '00:00:00.000000'
    assert timedelta_format(timedeltas[1]) == '00:00:00.000001'

# Generated at 2022-06-12 19:48:03.603036
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=2,
                                                      hours=3,
                                                      minutes=4,
                                                      days=5,
                                                      microseconds=6)) == \
                                                      '05:04:02.000006'
    assert timedelta_format(datetime_module.timedelta(seconds=2,
                                                      hours=3,
                                                      minutes=4,
                                                      days=5,
                                                      microseconds=6)) == \
                                                      '05:04:02.000006'



# Generated at 2022-06-12 19:48:10.001485
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.123456') == \
           datetime_module.timedelta(microseconds=123456)
    assert timedelta_parse('00:00:01.012345') == \
           datetime_module.timedelta(microseconds=1012345)
    assert timedelta_parse('00:01:00.012345') == \
           datetime_module.timedelta(seconds=60, microseconds=12345)
    assert timedelta_parse('01:00:00.012345') == \
           datetime_module.timedelta(minutes=60, microseconds=12345)

# Generated at 2022-06-12 19:48:18.541538
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:01:00.00') == datetime_module.timedelta(
        minutes=1
    )
    assert timedelta_parse('00:00:01.000000') == datetime_module.timedelta(
        seconds=1
    )
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(
        microseconds=10
    )
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(
        microseconds=100
    )
    assert timedelta_parse('00:00:00.001000') == datetime_module.tim

# Generated at 2022-06-12 19:48:24.854907
# Unit test for function timedelta_parse
def test_timedelta_parse():
    duration = timedelta_parse('5:23:42.421023')
    assert duration == datetime_module.timedelta(
                                            hours=5, minutes=23, seconds=42,
                                            microseconds=421023)

    duration = timedelta_parse('00:00:42.421023')
    assert duration == datetime_module.timedelta(
                                            hours=0, minutes=0, seconds=42,
                                            microseconds=421023)

# Generated at 2022-06-12 19:48:29.919733
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(seconds=1, microseconds=2)
    )) == datetime_module.timedelta(seconds=1, microseconds=2)

    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(microseconds=1)
    )) == datetime_module.timedelta(microseconds=1)

    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(seconds=1)
    )) == datetime_module.timedelta(seconds=1)

    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(days=1)
    )) == datetime_module.timedelta(days=1)

    assert timed

# Generated at 2022-06-12 19:48:49.521506
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                   microseconds=456000)
    )) == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                     microseconds=456000)
    assert timedelta_parse(timedelta_format(
        datetime_module.timedelta(hours=3, minutes=20, seconds=59,
                                   microseconds=234100)
    )) == datetime_module.timedelta(hours=3, minutes=20, seconds=59,
                                     microseconds=234100)

# Generated at 2022-06-12 19:48:57.591383
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0, 0, 0)) == \
           '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(0, 0, 1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(0, 0, 10)) == \
           '00:00:00.000010'
    assert timedelta_format(datetime_module.timedelta(0, 0, 100)) == \
           '00:00:00.000100'
    assert timedelta_format(datetime_module.timedelta(0, 0, 1000)) == \
           '00:00:00.001000'

# Generated at 2022-06-12 19:49:07.141104
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )
    assert timedelta_parse('1:02:03.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )
    assert timedelta_parse('1:2:3.123456') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )
    assert timedelta_parse('1:2:3.123') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123000
    )
    assert timedelta

# Generated at 2022-06-12 19:49:10.775681
# Unit test for function timedelta_parse
def test_timedelta_parse():
    # assert timedelta_parse('12:34:56.123456') == datetime.
    assert timedelta_parse('12:34:56.123456') == datetime_module.timedelta(
        hours=12, minutes=34, seconds=56, microseconds=123456
    )

# Generated at 2022-06-12 19:49:15.725986
# Unit test for function timedelta_parse
def test_timedelta_parse():
    # type: () -> None
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=1))) == datetime_module.timedelta(days=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=1))) == datetime_module.timedelta(seconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(microseconds=1))) == datetime_module.timedelta(microseconds=1)

# Generated at 2022-06-12 19:49:24.186021
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=0,
                                                      minutes=0,
                                                      seconds=0,
                                                      microseconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=17,
                                                      minutes=3,
                                                      seconds=3,
                                                      microseconds=123456)) == '17:03:03.123456'



# Generated at 2022-06-12 19:49:32.682743
# Unit test for function timedelta_format

# Generated at 2022-06-12 19:49:43.229338
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == \
                                                      '01:02:03.000004'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=40)) == \
                                                      '01:02:03.000040'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=400)) == \
                                                      '01:02:03.000400'

# Generated at 2022-06-12 19:49:54.257822
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0') == datetime_module.timedelta(seconds=0)
    assert timedelta_parse('1') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('10') == datetime_module.timedelta(seconds=10)
    assert timedelta_parse('99') == datetime_module.timedelta(seconds=99)
    assert timedelta_parse('1.2') == datetime_module.timedelta(seconds=1,
                                                               microseconds=200000)
    assert timedelta_parse('1.99') == datetime_module.timedelta(seconds=1,
                                                                microseconds=990000)

# Generated at 2022-06-12 19:50:06.090144
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=10, minutes=20, seconds=30, microseconds=40500
    )) == '10:20:30.040500'
    assert timedelta_format(datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=1000000
    )) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=0
    )) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=24, minutes=0, seconds=0, microseconds=0
    )) == '00:00:00.000000'
    assert timedelta

# Generated at 2022-06-12 19:50:35.500813
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3)) \
                                                          == '01:02:03'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=456789)) \
                                                          == '01:02:03.456789'
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00'

# Generated at 2022-06-12 19:50:38.339250
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:1:1.1') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=100000
    )

# Generated at 2022-06-12 19:50:44.603253
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:01:00.000001') == datetime_module.timedelta(
        minutes=1, microseconds=1
    )
    assert timedelta_parse('01:01:01.011111') == datetime_module.timedelta(
        hours=1, minutes=1, seconds=1, microseconds=11111
    )



# Generated at 2022-06-12 19:50:49.655174
# Unit test for function timedelta_format
def test_timedelta_format():
    delta = datetime_module.timedelta(hours=1, minutes=1, seconds=1,
                                      microseconds=1)
    assert timedelta_format(delta) == '01:01:01.000001'


# Generated at 2022-06-12 19:50:58.311892
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('03:02:01.123450') == (
        datetime_module.timedelta(hours=3, minutes=2, seconds=1,
                                  microseconds=123450)
    )
    assert timedelta_parse('03:02:01.001234') == (
        datetime_module.timedelta(hours=3, minutes=2, seconds=1,
                                  microseconds=1234)
    )
    assert timedelta_parse('03:02:01.000000') == (
        datetime_module.timedelta(hours=3, minutes=2, seconds=1)
    )
    assert timedelta_parse('03:02:01') == (
        datetime_module.timedelta(hours=3, minutes=2, seconds=1)
    )

# Generated at 2022-06-12 19:51:06.505055
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:01:02.000003') == \
                                            datetime_module.timedelta(hours=0,
                                                              minutes=1,
                                                              seconds=2,
                                                              microseconds=3)

    assert timedelta_parse('02:01:02.000003') == \
                                            datetime_module.timedelta(hours=2,
                                                              minutes=1,
                                                              seconds=2,
                                                              microseconds=3)



# Generated at 2022-06-12 19:51:14.962512
# Unit test for function timedelta_format
def test_timedelta_format():
    time = datetime_module.time(hour=14, minute=10, second=23, microsecond=123478)
    assert timedelta_format(datetime_module.timedelta(microseconds=99999)) == \
           '{:02d}:{:02d}:{:02d}.{:06d}'.format(
               0, 0, 0, 99999
           )
    assert timedelta_format(datetime_module.timedelta(days=1, microseconds=99999)) == \
           '{:02d}:{:02d}:{:02d}.{:06d}'.format(
               0, 0, 0, 99999
           )

# Generated at 2022-06-12 19:51:20.686037
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('1.0') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('1.00') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('1.000') == datetime_module.timedelta(seconds=1)

    assert timedelta_parse('1.000001') == \
           datetime_module.timedelta(microseconds=100001)
    assert timedelta_parse('1.0000010') == \
           datetime_module.timedelta(microseconds=1000001)


# Generated at 2022-06-12 19:51:26.351541
# Unit test for function timedelta_format
def test_timedelta_format():
    from . import testing_tools
    t = testing_tools.Timer(0.123)
    assert timedelta_format(t.delta) == '00:00:00.123000'
    assert timedelta_parse(timedelta_format(t.delta)) == t.delta


# Generated at 2022-06-12 19:51:36.269698
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0.123456)) == \
                                                            '00:00:00.123456'
    assert timedelta_format(datetime_module.timedelta(seconds=1.123456)) == \
                                                            '00:00:01.123456'
    assert timedelta_format(datetime_module.timedelta(minutes=5)) == \
                                                            '00:05:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=10)) == \
                                                            '10:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=20.23456)) == \
                                                            '20:13:45.600000'




# Generated at 2022-06-12 19:52:07.680303
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.123456') == datetime_module.timedelta(
        seconds=.123456,
    )
    assert timedelta_parse('1:00:00.123456') == datetime_module.timedelta(
        hours=1,
        seconds=.123456,
    )
    assert timedelta_parse('0:01:00.123456') == datetime_module.timedelta(
        minutes=1,
        seconds=.123456,
    )
    assert timedelta_parse('0:00:01.123456') == datetime_module.timedelta(
        seconds=1.123456,
    )

# Generated at 2022-06-12 19:52:15.945323
# Unit test for function timedelta_parse
def test_timedelta_parse():
    from . import testutils
    for timedelta, strings in ((datetime_module.timedelta(seconds=2), ['2s', '02s', '02:00s']),
                               (datetime_module.timedelta(seconds=2,
                                                           microseconds=133),
                                ['2:00.000133s', '2.000133s',
                                 '2.000133000s', '2:00.000133000s'])):
        for string in strings:
            assert timedelta_parse(string) == timedelta
    with testutils.assert_raises(ValueError):
        timedelta_parse('')
    with testutils.assert_raises(ValueError):
        timedelta_parse('1')



# Generated at 2022-06-12 19:52:23.008102
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1)) == '24:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'



# Generated at 2022-06-12 19:52:31.955693
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2,
                                                      seconds=3,
                                                      microseconds=400000))\
                            == '01:02:03.400000'
    assert timedelta_format(datetime_module.timedelta(hours=23, minutes=59,
                                                      seconds=59,
                                                      microseconds=999999))\
                            == '23:59:59.999999'
    assert timedelta_format(datetime_module.timedelta(hours=0, minutes=0,
                                                      seconds=0,
                                                      microseconds=0))\
                            == '00:00:00.000000'



# Generated at 2022-06-12 19:52:34.150609
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:05:34.123456') == \
           datetime_module.timedelta(hours=1, minutes=5, seconds=34,
                                     microseconds=123456)

# Generated at 2022-06-12 19:52:44.853889
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('00:00:00.000000')) == \
                                                           '00:00:00.000000'
    assert timedelta_format(timedelta_parse('01:02:03.000000')) == \
                                                           '01:02:03.000000'
    assert timedelta_format(timedelta_parse('01:02:03.040000')) == \
                                                           '01:02:03.040000'
    assert timedelta_format(timedelta_parse('01:02:03.040000')) == \
                                                           '01:02:03.040000'

# Generated at 2022-06-12 19:52:47.560884
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timedelta = timedelta_format(datetime_module.timedelta(hours=2.1,
                                                           minutes=3.2,
                                                           seconds=4.312345))
    assert timedelta_parse(timedelta) == datetime_module.timedelta(hours=2,
                                                             minutes=3,
                                                             seconds=4,
                                                             microseconds=312346)



# Generated at 2022-06-12 19:52:51.319557
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('05:32:14.000000') == datetime_module.timedelta(
        hours=5, minutes=32, seconds=14
    )
    assert timedelta_parse('23:59:59.999999') == datetime_module.timedelta(
        days=1, microseconds=-1
    )
    assert timedelta_parse('23:59:59.9999999999999') == datetime_module.timedelta(
        days=1, microseconds=-1
    )

# Generated at 2022-06-12 19:52:56.060511
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == "00:00:00.000000"
    assert timedelta_format(datetime_module.timedelta(days=1,
                                                      seconds=1)) == "00:00:01.000000"
    assert timedelta_format(datetime_module.timedelta(days=1,
                                                      microseconds=1)) == "00:00:00.000001"



# Generated at 2022-06-12 19:53:05.688904
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=12)) == '12:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=12)) == '00:00:12.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=12)) == '00:00:00.000012'
    assert timedelta_format(datetime_module.timedelta(seconds=12.5)) == '00:00:12.500000'
    assert timedelta_format(datetime_module.timedelta(hours=12, seconds=12.5)) == '12:00:12.500000'

# Generated at 2022-06-12 19:54:06.589705
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1)) == \
                                                          '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, seconds=2,
                                                      microseconds=3)) == \
                                                          '24:00:02.000003'
    assert timedelta_format(datetime_module.timedelta(seconds=2,
                                                      microseconds=3)) == \
                                                          '00:00:02.000003'
    assert timedelta_format(datetime_module.timedelta(seconds=2)) == \
                                                          '00:00:02.000000'


# Generated at 2022-06-12 19:54:16.402932
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('04:05:06.123456') == datetime_module.timedelta(hours=4, minutes=5, seconds=6, microseconds=123456)
    assert timedelta_parse('04:05:06.000000000123456') == datetime_module.timedelta(hours=4, minutes=5, seconds=6, microseconds=123456)
    assert timedelta_parse('04:05:06.999999999123456') == datetime_module.timedelta(hours=4, minutes=5, seconds=6, microseconds=999999999)
    assert timedelta_parse('04:05:06.999999999999999999999999') == datetime_module.timedelta(hours=4, minutes=5, seconds=6, microseconds=999999999)

# Generated at 2022-06-12 19:54:25.998236
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(
        hours=1,
    )
    assert timedelta_parse('1:00:00.000001') == datetime_module.timedelta(
        hours=1,
    )
    assert timedelta_parse('-1:00:00.000000') == datetime_module.timedelta(
        hours=-1,
    )
    assert timedelta_parse('-1:00:00.000001') == datetime_module.timedelta(
        hours=-1,
    )
    assert timedelta_parse('1:00:00.000010') == datetime_module.timedelta(
        hours=1,
    )
    assert timedelta_parse('1:00:00.000100') == datetime

# Generated at 2022-06-12 19:54:28.914815
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        days=1, hours=2, minutes=3, seconds=4, microseconds=5
    )) == '02:03:04.000005'



# Generated at 2022-06-12 19:54:34.102208
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        days=1, hours=2, minutes=3, seconds=4, microseconds=5)
    ) == '26:03:04.000005'
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00.000000'



# Generated at 2022-06-12 19:54:42.953693
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(hours=4, minutes=5, seconds=6,
                                          microseconds=7)
    s = timedelta_format(timedelta)
    assert s == '04:05:06.000007'

    timedelta = datetime_module.timedelta(hours=-3, minutes=-2, seconds=-1,
                                          microseconds=-3)
    s = timedelta_format(timedelta)
    assert s == '-03:-02:-01.999997'

    timedelta = datetime_module.timedelta(hours=-4)
    s = timedelta_format(timedelta)
    assert s == '-04:00:00.000000'



# Generated at 2022-06-12 19:54:53.707858
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'

# Generated at 2022-06-12 19:55:03.438190
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == \
           datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=1))) == \
           datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=60))) == \
           datetime_module.timedelta()
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=1))) == \
           datetime_module.timedelta(seconds=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(milliseconds=1))) == \
           datetime_module.tim

# Generated at 2022-06-12 19:55:08.698820
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(0, 0, 1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(0, 1, 1)) == '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(1, 1, 1)) == '24:00:01.000001'


# Generated at 2022-06-12 19:55:12.517920
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=5, hours=17, minutes=22,
                                          seconds=33, microseconds=444444)
    formatted = timedelta_format(timedelta)
    parsed = timedelta_parse(formatted)
    assert timedelta == parsed