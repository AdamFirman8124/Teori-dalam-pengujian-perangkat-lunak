

# Generated at 2022-06-12 19:46:18.766216
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse(':')) == '00:00:00.000000'
    assert timedelta_format(timedelta_parse('2.1:')) == '02:01:00.000000'
    assert timedelta_format(timedelta_parse(':2.1')) == '00:00:02.100000'
    assert timedelta_format(timedelta_parse('2.1:3.4')) == '02:01:03.400000'
    assert timedelta_format(timedelta_parse('2.1:3.4:5.6')) == '02:01:03.400000'

# Generated at 2022-06-12 19:46:22.039553
# Unit test for function timedelta_format
def test_timedelta_format():
    timedelta = datetime_module.timedelta(days=12, seconds=30, microseconds=123456)
    assert timedelta_format(timedelta) == '12:00:00.123456'



# Generated at 2022-06-12 19:46:30.791913
# Unit test for function timedelta_format
def test_timedelta_format():
    import pickle

# Generated at 2022-06-12 19:46:40.279583
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta(0, 0)
    assert timedelta_parse('0:0:0.1') == datetime_module.timedelta(0, 0, 1)
    assert timedelta_parse('0:0:1.1') == datetime_module.timedelta(0, 1, 1)
    assert timedelta_parse('0:1:1.1') == datetime_module.timedelta(0, 61, 1)
    assert timedelta_parse('1:1:1.1') == datetime_module.timedelta(1, 3661, 1)


if PY3:
    import io
else:
    import StringIO as io


if PY3:
    import collections
    collections.Mapping._abc_

# Generated at 2022-06-12 19:46:45.201073
# Unit test for function timedelta_format
def test_timedelta_format():
    cases = [(1, '00:00:00.000001'),
             (-1, '-00:00:00.000001')]
    for delta_seconds, expected_timedelta_str in cases:
        delta = datetime_module.timedelta(seconds=delta_seconds)
        actual_timedelta_str = timedelta_format(delta)
        assert actual_timedelta_str == expected_timedelta_str



# Generated at 2022-06-12 19:46:57.055412
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=1,
                                                             minutes=5))) ==\
                                                             datetime_module.timedelta(days=1, minutes=5)

    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=1,
                                                             microseconds=1))) ==\
                                                             datetime_module.timedelta(days=1,
                                                             microseconds=1)

    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=1,
                                                             microseconds=123))) ==\
                                                             datetime_module.timedelta(days=1,
                                                             microseconds=123)

    assert timedelta_

# Generated at 2022-06-12 19:47:00.874291
# Unit test for function timedelta_parse
def test_timedelta_parse():
    check = datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                      microseconds=400000)
    assert timedelta_parse(timedelta_format(check)) == check


# Generated at 2022-06-12 19:47:04.545547
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.456000') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=456
    )

# Generated at 2022-06-12 19:47:15.899270
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(
        hours=14, minutes=57, seconds=23, microseconds=998182,
    )) == '14:57:23.998182'
    assert timedelta_format(datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=0,
    )) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=0, minutes=57, seconds=23, microseconds=0,
    )) == '00:57:23.000000'
    assert timedelta_format(datetime_module.timedelta(
        hours=0, minutes=57, seconds=23, microseconds=9,
    )) == '00:57:23.000009'



# Generated at 2022-06-12 19:47:18.989675
# Unit test for function timedelta_parse
def test_timedelta_parse():
    timestamp = '00:44:57.848335'
    delta = timedelta_parse(timestamp)
    new_timestamp = timedelta_format(delta)
    assert timestamp == new_timestamp

# Generated at 2022-06-12 19:47:39.022488
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('4:00:00.000000') == datetime_module.timedelta(hours=4)
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(hours=0)
    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(seconds=1e-6)
    assert timedelta_parse('0:00:00.000010') == datetime_module.timedelta(seconds=1e-6 * 10)
    assert timedelta_parse('0:00:00.000100') == datetime_module.timedelta(seconds=1e-6 * 100)

# Generated at 2022-06-12 19:47:49.572480
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=2)) == \
           '00:00:02.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=61)) == \
           '00:01:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=3661)) == \
           '01:01:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == \
           '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=12)) == \
           '00:00:01.000012'

# Generated at 2022-06-12 19:47:56.789536
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:42:53.000000') == datetime_module.timedelta(
        hours=1, minutes=42, seconds=53, microseconds=0
    )
    assert timedelta_parse('1:42:53.000001') == datetime_module.timedelta(
        hours=1, minutes=42, seconds=53, microseconds=1
    )
    assert timedelta_parse('01:42:53.000001') == datetime_module.timedelta(
        hours=1, minutes=42, seconds=53, microseconds=1
    )
    assert timedelta_parse('0:0:0.000001') == datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=1
    )

# Generated at 2022-06-12 19:48:05.740973
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=10)) == \
           '00:00:10.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=5, seconds=10)) == \
           '00:05:10.000000'
    assert timedelta_format(datetime_module.timedelta(hours=2, seconds=10)) == \
           '02:00:10.000000'
    assert timedelta_format(datetime_module.timedelta(hours=2, minutes=3, seconds=10)) == \
           '02:03:10.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, seconds=10)) == \
           '24:00:10.000000'

# Generated at 2022-06-12 19:48:11.316742
# Unit test for function timedelta_format
def test_timedelta_format():
    a_timedelta = datetime_module.timedelta(days=1, hours=2, minutes=3,
                                            seconds=4, microseconds=5)
    assert timedelta_format(a_timedelta) == '02:03:04.000005'
    negative_timedelta = -a_timedelta
    assert timedelta_format(negative_timedelta) == '-02:03:04.000005'
    assert timedelta_format(datetime_module.timedelta(0)) == '00:00:00'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01'
    assert timed

# Generated at 2022-06-12 19:48:18.907511
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta()
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('00:00:00.000010') == datetime_module.timedelta(microseconds=10)
    assert timedelta_parse('00:00:00.000100') == datetime_module.timedelta(microseconds=100)
    assert timedelta_parse('00:00:00.001000') == datetime_module.timedelta(microseconds=1000)
    assert timedelta_parse('00:00:00.010000') == datetime_module.timedelta(microseconds=10000)

# Generated at 2022-06-12 19:48:24.094680
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta())) == (
        datetime_module.timedelta()
    )
    assert timedelta_parse(timedelta_format(timedelta_parse('1:20:30.456789'))) == (
        timedelta_parse('1:20:30.456789')
    )

test_timedelta_parse()

# Generated at 2022-06-12 19:48:31.391183
# Unit test for function timedelta_format
def test_timedelta_format():
    zero_delta = datetime_module.timedelta()
    assert zero_delta == timedelta_parse(timedelta_format(zero_delta))

    random_delta = datetime_module.timedelta(
        hours=14, minutes=13, seconds=23, microseconds=123456
    )
    assert random_delta == timedelta_parse(timedelta_format(random_delta))

# Generated at 2022-06-12 19:48:37.860967
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(
        microseconds=1
    )) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'


# Generated at 2022-06-12 19:48:40.640873
# Unit test for function timedelta_format
def test_timedelta_format():
    delta = datetime_module.timedelta(hours=1)
    assert timedelta_format(delta) == '01:00:00.000000'


# Generated at 2022-06-12 19:49:02.604936
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:2:3.123456') == (
        datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                  microseconds=123456)
    )



# Generated at 2022-06-12 19:49:07.187990
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('13:004:786.234567')) == \
           '13:04:07.862346'
    assert timedelta_format(timedelta_parse('13:04:07.862346')) == \
           '13:04:07.862346'

# Generated at 2022-06-12 19:49:14.802291
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(days=1))) \
           == datetime_module.timedelta(days=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(hours=1))) \
           == datetime_module.timedelta(hours=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(minutes=1))) \
           == datetime_module.timedelta(minutes=1)
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(seconds=1))) \
           == datetime_module.timedelta(seconds=1)

# Generated at 2022-06-12 19:49:24.643187
# Unit test for function timedelta_format
def test_timedelta_format():
    def try_timedelta_format(timedelta):
        time = (datetime_module.datetime.min + timedelta).time()
        assert timedelta_format(timedelta) == time_isoformat(time)

    try_timedelta_format(datetime_module.timedelta(seconds=1, microseconds=1))
    try_timedelta_format(datetime_module.timedelta(hours=12, minutes=34))
    try_timedelta_format(datetime_module.timedelta())



# Generated at 2022-06-12 19:49:28.837855
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('1:02:03.000123') == \
           datetime_module.timedelta(seconds=3723, microseconds=123)
    assert timedelta_parse('24:02:03.000123') == \
           datetime_module.timedelta(days=1, seconds=3723, microseconds=123)

# Generated at 2022-06-12 19:49:31.807200
# Unit test for function timedelta_parse
def test_timedelta_parse():
    actual = timedelta_parse('00:00:30.1')
    assert isinstance(actual, datetime_module.timedelta)
    assert str(actual) == '0:00:30.001000'
    assert not actual.days



# Generated at 2022-06-12 19:49:38.919757
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours = 1)) == \
           '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours = 1,
                                                      seconds = 16)) == \
           '01:00:16.000000'
    assert timedelta_format(datetime_module.timedelta(hours = 1,
                                                      microseconds = 16)) == \
           '01:00:00.000016'


# Generated at 2022-06-12 19:49:44.138563
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1)) == '01:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1, seconds=1)) == '01:01:01.000000'


# Generated at 2022-06-12 19:49:50.194270
# Unit test for function timedelta_parse
def test_timedelta_parse():
    print(timedelta_parse('1:00:00.000000'))
    print(timedelta_parse('1:00:00.5'))
    print(timedelta_parse('1:00:00.5.0'))
    print(timedelta_parse('1:00:00.5.0'))
# test_timedelta_parse()

# Generated at 2022-06-12 19:49:58.198076
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(
        datetime_module.timedelta(hours=7, minutes=6, seconds=5)
    ) == '07:06:05.000000'
    assert timedelta_format(
        datetime_module.timedelta(hours=7, minutes=6, seconds=5,
                                  microseconds=4)
    ) == '07:06:05.000004'
    assert timedelta_format(
        datetime_module.timedelta(hours=7, minutes=6, seconds=5,
                                  microseconds=4, seconds=3)
    ) == '07:06:08.000004'
    assert timedelta_format(
        datetime_module.timedelta(days=7, hours=6, minutes=5)
    ) == '06:05:00.000000'
   

# Generated at 2022-06-12 19:50:44.319821
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(seconds=5,
                                                      microseconds=1)) == \
                                                      '00:00:05.000001'
    assert timedelta_format(datetime_module.timedelta(minutes=1,
                                                      microseconds=11)) == \
                                                      '00:01:00.000011'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      microseconds=111)) == \
                                                      '01:00:00.000111'
    assert timedelta_format(datetime_module.timedelta(days=1,
                                                      microseconds=1111)) == \
                                                      '24:00:00.001111'

# Generated at 2022-06-12 19:50:50.521954
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse(timedelta_format(
        datetime_module.timedelta(seconds=1, microseconds=123456)
    ))) == timedelta_format(
        datetime_module.timedelta(seconds=1, microseconds=123456)
    )

# Generated at 2022-06-12 19:50:58.866873
# Unit test for function timedelta_parse
def test_timedelta_parse():
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
        microseconds=1000
    )

# Generated at 2022-06-12 19:51:07.185096
# Unit test for function timedelta_format
def test_timedelta_format():
    for some_timedelta in (
        datetime_module.timedelta(0),
        datetime_module.timedelta(1),
        datetime_module.timedelta(days=1, hours=1, minutes=1, seconds=1,
                                  microseconds=1),
        datetime_module.timedelta(days=-1, hours=-1, minutes=-1, seconds=-1,
                                  microseconds=-1),
    ):
        assert timedelta_parse(timedelta_format(some_timedelta)) == \
                                   some_timedelta

# Generated at 2022-06-12 19:51:09.225001
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(timedelta_parse('1:2:3.123456')) == '01:02:03.123456'

# Generated at 2022-06-12 19:51:13.004390
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    ))) == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=123456
    )



# Generated at 2022-06-12 19:51:15.578039
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2,
                                                      seconds=3,
                                                      microseconds=4)) == '01:02:03.000004'

# Generated at 2022-06-12 19:51:20.900200
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta()) == '00:00:00.000000'
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

# Generated at 2022-06-12 19:51:30.925853
# Unit test for function timedelta_format
def test_timedelta_format():
    dt = datetime_module.datetime.now()
    dt2 = timedelta_parse(timedelta_format(dt-dt))
    assert dt2 == datetime_module.timedelta(0)


try:
    from _thread import get_ident
except ImportError:
    from thread import get_ident


if PY3:
    from collections import UserDict
else:
    import UserDict

if PY3:
    from itertools import zip_longest, filterfalse
else:
    from itertools import izip_longest as zip_longest, ifilterfalse as filterfalse


if PY3:
    relpath = os.path.relpath

# Generated at 2022-06-12 19:51:32.724367
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('01:02:03.123456') == \
                               datetime_module.timedelta(hours=1, minutes=2,
                                                         seconds=3,
                                                         microseconds=123456)

# Generated at 2022-06-12 19:52:55.798582
# Unit test for function timedelta_parse
def test_timedelta_parse():
    datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=4) ==\
        timedelta_parse('1:02:03.000004')
    datetime_module.timedelta(microseconds=1) ==\
        timedelta_parse('00:00:00.000001')

# Generated at 2022-06-12 19:53:05.688845
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == '00:00:00.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1, seconds=1, microseconds=1)) == \
           '01:01:01.000001'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1, seconds=1, microseconds=0)) == \
           '01:01:01.000000'

# Generated at 2022-06-12 19:53:10.704395
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse(timedelta_format(datetime_module.timedelta(
        days=2, hours=3, minutes=4, seconds=5, milliseconds=6,
        microseconds=7,
    ))) == datetime_module.timedelta(
        days=2, hours=3, minutes=4, seconds=5, milliseconds=6,
        microseconds=7,
    )

# Generated at 2022-06-12 19:53:14.930715
# Unit test for function timedelta_format
def test_timedelta_format():
    assert timedelta_format(datetime_module.timedelta(days=2)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1,
                                                      minutes=2, seconds=3,
                                                      microseconds=45678)) == \
                           '01:02:03.045678'


# Generated at 2022-06-12 19:53:27.493185
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('0:00:00.000000') == \
                                 datetime_module.timedelta(seconds=0)
    assert timedelta_parse('0:00:01.000000') == \
                                 datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:01:00.000000') == \
                                 datetime_module.timedelta(minutes=1)
    assert timedelta_parse('1:00:00.000000') == \
                                 datetime_module.timedelta(hours=1)
    assert timedelta_parse('0:00:00.000001') == \
                                 datetime_module.timedelta(microseconds=1)

# Generated at 2022-06-12 19:53:36.253026
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert (timedelta_parse('1:02:03.000001') ==
            datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                      microseconds=1))


if PY3:
    def isidentifier(thing):
        return thing.isidentifier()
else:
    import re
    
    isidentifier = re.compile(r'^[a-z_][a-z0-9_]*$', re.I).match

# Generated at 2022-06-12 19:53:46.606889
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_format(datetime_module.timedelta(days=1)) == \
                                                              '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1, seconds=1)) == \
                                                              '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == \
                                                              '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=1,
                                                      microseconds=1)) == \
                                                              '00:00:01.000001'
    assert timedelta_format(datetime_module.timedelta(hour=1)) == \
                                                              '01:00:00.000000'


# Generated at 2022-06-12 19:53:56.680648
# Unit test for function timedelta_parse
def test_timedelta_parse():
    assert timedelta_parse('00:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('00:00:00.9') == datetime_module.timedelta(
        milliseconds=900
    )
    assert timedelta_parse('00:00:01.2') == datetime_module.timedelta(
        seconds=1, microseconds=200000
    )
    assert timedelta_parse('00:01:00.0') == datetime_module.timedelta(
        minutes=1
    )
    assert timedelta_parse('01:00:00.0') == datetime_module.timedelta(
        hours=1
    )
    assert timedelta_parse('09:01:23.456789') == datetime_module

# Generated at 2022-06-12 19:54:01.433361
# Unit test for function timedelta_format
def test_timedelta_format():
    dt = datetime_module.timedelta(hours=2, minutes=3, seconds=4,
                                   microseconds=567)
    assert timedelta_format(dt) == '02:03:04.00567'



# Generated at 2022-06-12 19:54:08.522820
# Unit test for function timedelta_parse
def test_timedelta_parse():
    import pytest
    assert timedelta_parse('1:00:00.000000') == datetime_module.timedelta(
        hours=1)
    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(
        microseconds=1)
    assert timedelta_parse('0:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('1:01:00.000000') == datetime_module.timedelta(
        hours=1, minutes=1)

    with pytest.raises(ValueError):
        timedelta_parse('a')
    with pytest.raises(ValueError):
        timedelta_parse('0')
    with pytest.raises(ValueError):
        timedelta_parse('0:00')