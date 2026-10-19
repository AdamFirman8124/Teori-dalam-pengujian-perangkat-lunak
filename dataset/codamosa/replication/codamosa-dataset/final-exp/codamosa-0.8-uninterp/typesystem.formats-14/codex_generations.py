

# Generated at 2022-06-14 14:23:36.755073
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = TimeFormat

    assert time.serialize(datetime.time(0,0,0)) == "00:00:00"
    assert time.serialize(datetime.time(12,0,0)) == "12:00:00"
    assert time.serialize(datetime.time(12,0,0,0)) == "12:00:00"
    assert time.serialize(datetime.time(12,0,0,99)) == "12:00:00.000099"

    assert time.serialize(datetime.time(0,1,0)) == "00:01:00"
    assert time.serialize(datetime.time(0,1,0,0)) == "00:01:00"

# Generated at 2022-06-14 14:23:40.713698
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-02-31T13:00:00Z") == datetime.datetime(2019, 2, 28, 13, 0, 0, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:23:43.678271
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    result = date_format.validate('2020-09-01')
    assert result.isoformat() == '2020-09-01'



# Generated at 2022-06-14 14:23:48.511961
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    fmt = DateTimeFormat()
    datetime = "2019-10-20T09:20:00Z"
    assert fmt.validate(datetime) == datetime.datetime(2019, 10, 20, 9, 20, 0, tzinfo = datetime.timezone.utc)


# Generated at 2022-06-14 14:23:59.351857
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from uuid import UUID
    from datetime import date
    from datetime import datetime
    from datetime import time

    p = UUIDFormat()
    print(p.validate("d3e6b582-6e47-4c9e-870d-a0e4a06ef1c4"))

    p = UUIDFormat()
    try:
        p.validate("d3e6b582-6e47-4c9e-870d-a0e4a06ef1")
    except Exception as err:
        print(err)

    #DateFormat test
    p = DateFormat()
    print(p.validate("2020-01-01"))

    try:
        p.validate("2020-02-31")
    except Exception as err:
        print(err)

    p = Date

# Generated at 2022-06-14 14:24:07.122767
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    def test_serialize(obj, expected):
        assert DateTimeFormat().serialize(obj) == expected

    test_serialize(None, None)
    test_serialize(datetime.datetime(2010, 3, 27, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=0))), "2010-03-27T00:00:00")
    test_serialize(datetime.datetime(2010, 3, 27, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=1))), "2010-03-27T00:00:00+01:00")

# Generated at 2022-06-14 14:24:11.143428
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    datetimeAfterSerialization = date_time_format.serialize(datetime.datetime(2020, 5, 1, 17, 58))
    assert datetimeAfterSerialization == "2020-05-01T17:58:00"

# Generated at 2022-06-14 14:24:14.792154
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_format = UUIDFormat()
    value = "550e8400-e29b-41d4-a716-446655440000"
    result = uuid_format.validate(value)
    assert isinstance(result, uuid.UUID)
    assert str(result) == value

# Generated at 2022-06-14 14:24:21.247381
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj1 = datetime.datetime(2020, 1, 1, tzinfo = datetime.timezone.utc)
    obj2 = datetime.datetime(2020, 1, 1, tzinfo = datetime.timezone(datetime.timedelta(hours = 5)))
    obj3 = datetime.datetime(2020, 1, 1, tzinfo = datetime.timezone(datetime.timedelta(hours = -5)))
    
    assert DateTimeFormat().serialize(obj1) == '2020-01-01T00:00:00+00:00'
    assert DateTimeFormat().serialize(obj2) == '2020-01-01T00:00:00+05:00'

# Generated at 2022-06-14 14:24:25.928430
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    test_time_format = TimeFormat()
    time_string = "12:34:23"
    expected_result = datetime.time(12, 34, 23, 0)
    actual_result = test_time_format.validate(time_string)
    assert actual_result == expected_result
    

# Generated at 2022-06-14 14:24:43.814419
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    assert date.validate("2000-01-01") == datetime.date(2000,1,1)


# Generated at 2022-06-14 14:24:52.101995
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Create a DateTimeFormat instance
    date_format = DateFormat()
    # Test dates that should pass
    assert date_format.validate('2020-10-10')==datetime.date(2020,10,10)
    assert date_format.validate('2011-11-11')==datetime.date(2011,11,11)
    # Test the format validation errors
    try:
        date_format.validate('10-10-2010')
        assert False
    except ValidationError as e:
        assert e.code =='format'
    try:
        date_format.validate('2010-101-10')
        assert False
    except ValidationError as e:
        assert e.code =='format'

# Generated at 2022-06-14 14:25:04.219516
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_format = DateTimeFormat()
    t1 = date_format.validate("2020-05-26T15:22:30Z")
    t2 = date_format.validate("2020-05-26T15:22:30")
    t3 = date_format.validate("2020-05-26T15:22:30+05:00")
    t4 = date_format.validate("2020-05-26T15:22:30+05")
    t5 = date_format.validate("2020-05-26T15:22:30.999999+05:00")
    t6 = date_format.validate("2020-05-26T15:22:30.999999")

    assert t1.isoformat() == "2020-05-26T15:22:30+00:00"
   

# Generated at 2022-06-14 14:25:15.620623
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    t = tf.validate("01:02:03.004000")
    assert t is not None
    assert t.hour == 1
    assert t.minute == 2
    assert t.second == 3
    assert t.microsecond == 4000
    t = tf.validate("14:15:16")
    assert t is not None
    assert t.hour == 14
    assert t.minute == 15
    assert t.second == 16
    t = tf.validate("2:3")
    assert t is not None
    assert t.hour == 2
    assert t.minute == 3
    assert t.second == 0
    t = tf.validate("2:3:")
    assert t is not None
    assert t.hour == 2
    assert t.minute == 3
    assert t.second == 0

# Generated at 2022-06-14 14:25:23.320535
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    formats = (
        ("10:02:32.123450", "10:02:32.123"),
        ("10:02:32.10", "10:02:32.1"),
        ("10:02:32", "10:02:32"),
        ("10:02", "10:02"),
    )
    for value, expected in formats:
        assert TimeFormat().validate(value) == datetime.time(
            hour=10, minute=2, second=32, microsecond=123000
        )



# Generated at 2022-06-14 14:25:27.056065
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format = DateTimeFormat()
    date_time = date_time_format.validate("2019-10-31T00:59:59.123Z")
    assert isinstance(date_time, datetime.datetime)

# Generated at 2022-06-14 14:25:34.932376
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    from typesystem.base import ValidationError
    from typesystem.formats import DateTimeFormat

    date_time_format = DateTimeFormat()

    date_time_str = "2019-01-01T00:00:00.000000Z"

    assert date_time_format.validate(date_time_str) == datetime.datetime(2019, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)

    with pytest.raises(ValidationError):
        date_time_str = "2019-01-0A"
        date_time_format.validate(date_time_str)



# Generated at 2022-06-14 14:25:46.654939
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetimeformat = DateTimeFormat()
    value = '2017-12-20 15:02:23'
    # test for valid value
    assert (datetimeformat.validate(value).date()) == datetime.date(2017, 12, 20)
    assert (datetimeformat.validate(value).time()) == datetime.time(15, 2, 23)

    # test for invalid value
    # test for invalid date format
    value = '2017-12-32 15:02:23'
    with pytest.raises(ValidationError):
        assert (datetimeformat.validate(value).date()) == datetime.date(2017, 12, 17)
    # test for invalid time format
    value = '2017-12-20 155:02:23'

# Generated at 2022-06-14 14:25:58.301267
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate('2020-03-09T13:42:31-04:00').isoformat(sep=' ') == '2020-03-09 13:42:31-04:00'
    assert DateTimeFormat().validate('2020-03-09T17:42:31Z').isoformat(sep=' ') == '2020-03-09 17:42:31+00:00'
    assert DateTimeFormat().validate('2020-03-09T13:42:31').isoformat(sep=' ') == '2020-03-09 13:42:31+00:00'
    assert DateTimeFormat().validate('2020-03-09T13:42:31.999898').isoformat(sep=' ') == '2020-03-09 13:42:31.999898'

# Generated at 2022-06-14 14:26:06.780734
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate('2017-01-1') == datetime.datetime(2017, 1, 1)
    assert DateTimeFormat().validate('2017-01-11T05:34:12.123') == datetime.datetime(2017, 1, 11, 5, 34, 12, 123000)
    assert DateTimeFormat().validate('2017-01-11T05:34:12.123Z') == datetime.datetime(2017, 1, 11, 5, 34, 12, 123000, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:26:18.245971
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    s = DateTimeFormat()
    input = datetime.datetime(year=2020, month=11, day=21, hour=3, minute=45, second=6, microsecond=8, tzinfo=datetime.timezone.utc)
    output = '2020-11-21T03:45:06.000008Z'
    result = s.serialize(input)
    assert result == output

    input = datetime.datetime(year=2020, month=11, day=21, hour=3, minute=45, second=6, microsecond=8)
    output = '2020-11-21T03:45:06.000008'
    result = s.serialize(input)
    assert result == output


# Generated at 2022-06-14 14:26:27.766076
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    """
    Given:
    The value to test is a datetime object.
    When:
    The method serialize is called.
    Then:
    Ensure that the serialized value is equal to the value of obj.isoformat().
    """
    value_datetime = datetime.datetime(2018, 1, 1, 10, 15, 0, 0)
    assert value_datetime.isoformat() == '2018-01-01T10:15:00'
    datetime_format = DateTimeFormat()
    value = datetime_format.serialize(value_datetime)
    assert value == '2018-01-01T10:15:00'



# Generated at 2022-06-14 14:26:38.582547
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    mf = TimeFormat()
    assert mf.validate("12:00:00.000000") == datetime.time(12, 0, 0)
    assert mf.validate("12:00:00") == datetime.time(12, 0, 0)
    assert mf.validate("12:00") == datetime.time(12, 0, 0)
    assert mf.validate("12") == datetime.time(12, 0, 0)
    assert mf.validate("12:00:00.000001") == datetime.time(12, 0, 0, 1)
    assert mf.validate("12:00:00.0001") == datetime.time(12, 0, 0, 10)



# Generated at 2022-06-14 14:26:48.706332
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate("10:10:10") == datetime.time(10, 10, 10)
    assert time_format.validate("10:10:10.01") == datetime.time(10, 10, 10, 10)
    # assert time_format.validate("10:10:10,42") == datetime.time(10, 10, 10, 42)
    # assert time_format.validate("10:10:10,999999") == datetime.time(10, 10, 10, 999999)
    assert time_format.validate("10:10:10.999999") == datetime.time(10, 10, 10, 999999)
    # assert time_format.validate("10:10:10,999999999") == datetime.time(10,

# Generated at 2022-06-14 14:27:00.548056
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    def test_serialize_1():
        dtf = DateTimeFormat()
        dt = datetime.datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1)
        assert dtf.serialize(dt) == "2020-01-01T01:01:01"
    
    def test_serialize_2():
        dtf = DateTimeFormat()
        dt = datetime.datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1)
        dt = dt.replace(microsecond=1000)
        assert dtf.serialize(dt) == "2020-01-01T01:01:01.001"

    test_serialize_1()
    test_serialize_2()

# Generated at 2022-06-14 14:27:01.691743
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    TimeFormat = TimeFormat()

# Generated at 2022-06-14 14:27:10.138853
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Creating TimeFormat instance
    time_format = TimeFormat()
    # Test true case
    time = time_format.validate("05:17:12")
    assert time.hour == 5
    assert time.minute == 17
    assert time.second == 12
    assert time.microsecond == 0
    # Test false case
    try:
        time_format.validate("24:00:00")
    except ValidationError as e:
        assert e.code == "invalid"
    else:
        assert False

# Generated at 2022-06-14 14:27:16.696709
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    # test input invalid
    assert isinstance(df.validate("01-01-01"), datetime.date) == True
    # test input valid
    assert isinstance(df.validate("2000-01-01"), datetime.date) == True
    # test input valid
    assert isinstance(df.validate("2000-01"), ValidationError) == True
    # test input valid
    assert isinstance(df.validate("20-01-01"), ValidationError) == True

test_DateFormat_validate()


# Generated at 2022-06-14 14:27:20.823944
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()

    assert time.validate("11:00:00.12345") == datetime.time(11, 0, 0, 12345)
    assert time.validate("11:00:00") == datetime.time(11, 0, 0)
    assert time.validate("11:00") == datetime.time(11, 0)


# Generated at 2022-06-14 14:27:23.412267
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    the_date = datetime.datetime.fromisoformat('2020-07-18T15:59:44.346000+03:00')
    assert DateTimeFormat().serialize(the_date) == '2020-07-18T15:59:44.346000+03:00'

# Generated at 2022-06-14 14:27:32.978205
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    date_time_format_serialize_result = date_time_format.serialize(datetime.datetime(2020, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc))
    assert date_time_format_serialize_result == '2020-01-01T00:00:00+00:00'

date = DateFormat()
time = TimeFormat()
datetime = DateTimeFormat()
uuid = UUIDFormat()

# Generated at 2022-06-14 14:27:34.934737
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.is_native_type(datetime.date(2018, 3, 4)) == True


# Generated at 2022-06-14 14:27:44.907090
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # in the following, assert isinstance is used for
    #  - value and obj are valid, dt_format should return a datetime
    dt_format = DateTimeFormat()
    value = "2015-10-25T08:40:51.620"
    obj = dt_format.validate(value)
    assert dt_format.serialize(obj) == value
    assert isinstance(dt_format.serialize(obj), str)

    value = "2015-10-25T08:40:51.620Z"
    obj = dt_format.validate(value)
    assert dt_format.serialize(obj) == value
    assert isinstance(dt_format.serialize(obj), str)

    value = "2015-10-25T08:40:51.620+00:00"
   

# Generated at 2022-06-14 14:27:57.421721
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("1234-01-01") == datetime.date(1234, 1, 1)
    assert DateFormat().validate("1234-1-1") == datetime.date(1234, 1, 1)
    assert DateFormat().validate("1234-01-1") == datetime.date(1234, 1, 1)
    assert DateFormat().validate("1234-1-01") == datetime.date(1234, 1, 1)
    assert DateFormat().validate("1234-01-01") == datetime.date(1234, 1, 1)
    try:
        DateFormat().validate("1234-13-01")
    except ValidationError:
        pass
    else:
        assert False

# Generated at 2022-06-14 14:28:00.250739
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # This test is to verify the method serialize return a non-None value
    d = datetime.datetime(year=2019,month=1,day=1,hour=12,minute=0)
    assert DateTimeFormat().serialize(d) is not None



# Generated at 2022-06-14 14:28:04.933478
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate('2020-03-01') is not None
    assert df.validate('2020-03-01') == df.validate('2020-03-01')


# Generated at 2022-06-14 14:28:08.844056
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    f = DateTimeFormat()
    assert f.serialize(datetime.datetime(2019, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)) == "2019-01-01T00:00:00+00:00"


# Generated at 2022-06-14 14:28:12.297460
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    #Testcase 1
    result = DateFormat().validate('2020-01-23')
    assert result == datetime.date(2020,1,23)

    #Testcase 2
    result = DateFormat().validate('2020-12-01')
    assert result == datetime.date(2020,12,1)

    #Testcase 3
    result = DateFormat().validate('2020-01-01')
    assert result == datetime.date(2020,1,1)



# Generated at 2022-06-14 14:28:14.266131
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("1988-28-11") == datetime.date(1988, 11, 28)


# Generated at 2022-06-14 14:28:20.286364
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    test_validate = DateTimeFormat()
    assert str(
        test_validate.validate("2019-08-19T11:09:57.124301+02:00")
    ) == "2019-08-19 11:09:57.124301+02:00"


# Generated at 2022-06-14 14:28:31.699898
# Unit test for method validate of class TimeFormat

# Generated at 2022-06-14 14:28:40.736366
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    import typesystem.formats
    t = typesystem.formats.TimeFormat()
    assert t.validate('12:34:56.789')==datetime.time(12, 34, 56,789000)
    assert t.validate('23:59:59')==datetime.time(23, 59, 59)
    assert t.validate('00:00:00')==datetime.time(0, 0, 0)
    # Invalid formats
    try:
        t.validate('00:00')
        assert False
    except Exception as e:
        assert type(e)==ValidationError
        assert e.code=='format'
    try:
        t.validate('25:00:00')
        assert False
    except Exception as e:
        assert type(e)==ValidationError

# Generated at 2022-06-14 14:28:52.750593
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    from typesystem.format import DateFormat

    df = DateFormat()

    with pytest.raises(ValidationError):
        df.validate("")

    with pytest.raises(ValidationError):
        df.validate("2020-02-")

    with pytest.raises(ValidationError):
        df.validate("2020-02-40")

    with pytest.raises(ValidationError):
        df.validate("2020-00-31")

    with pytest.raises(ValidationError):
        df.validate("2020-13-31")

    with pytest.raises(ValidationError):
        df.validate("2020")

    assert df.validate("2020-02-31") == datetime.date(2020, 2, 31)


# Generated at 2022-06-14 14:28:55.522335
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    ob = df.validate("2018-6-1")
    ob.year
    ob.month
    ob.day


# Generated at 2022-06-14 14:28:58.733330
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeFormat = TimeFormat()
    time = timeFormat.validate("10:30:00")
    assert isinstance(time, datetime.time)

# Generated at 2022-06-14 14:29:03.228269
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert type(TimeFormat().validate("19:03")) == datetime.time
    assert type(TimeFormat().validate("19:03:25")) == datetime.time
    assert type(TimeFormat().validate("19:03:25.123456")) == datetime.time


# Generated at 2022-06-14 14:29:06.620230
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert tf.validate("13:45") == datetime.time(13, 45)

    with pytest.raises(ValidationError):
        tf.validate("foo")



# Generated at 2022-06-14 14:29:12.343071
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeformat = TimeFormat()
    assert timeformat.validate("16:19:40.012345") == datetime.time(16, 19, 40, 12345)
    assert timeformat.validate("16:19:40") == datetime.time(16, 19, 40)
    assert timeformat.validate("16:19") == datetime.time(16, 19)
    assert timeformat.validate("16") == datetime.time(16)

# Generated at 2022-06-14 14:29:16.537298
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("23:12:45.123456") == datetime.time(23, 12, 45, 123456)
    assert TimeFormat().validate("23:12:45") == datetime.time(23, 12, 45)
    assert TimeFormat().validate("23:12") == datetime.time(23, 12)


# Generated at 2022-06-14 14:29:26.086049
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    print("\n### UNIT TEST 1 ###")
    print("DateFormat object's is_native_type() method is called, given argument: 2019-12-31")
    print("Expected: True, Actual:", df.is_native_type(datetime.date(2019,12,31)))

    print("\n### UNIT TEST 2 ###")
    print("DateFormat object's validate() method is called, given argument: 2019-12-31")
    print("Expected: 2019-12-31, Actual:", df.validate("2019-12-31"))
    # print("DateFormat object's validate() method is called, given argument: 2019-13-32")
    # print("Value Error: ", df.validate("2019-13-32"))

    print("\n### UNIT TEST 3 ###")
   

# Generated at 2022-06-14 14:29:37.152998
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test regex method
    regex = re.compile(r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})$")
    
    # Test case 1
    value = '1998-02-27'
    match = regex.match(value)
    print('1.match:',match)
    assert match != None
    kwargs = {k: int(v) for k, v in match.groupdict().items()}
    print('1.kwargs:',kwargs)
    assert kwargs == {'year': 1998, 'month': 2 , 'day': 27}
    
    # Test case 2
    value = "1998-2-2"
    match = regex.match(value)

# Generated at 2022-06-14 14:29:39.040589
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    test_time = TimeFormat()
    assert test_time.validate('00:00:00') == datetime.time(0, 0)

# Generated at 2022-06-14 14:29:43.626248
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    # Test with invalid date format
    try:
        date.validate('2018-02-31')
    except ValidationError as e:
        assert e.message == 'Must be a real date.'
    # Test with valid date format
    try:
        date.validate('2018-02-28')
    except ValidationError as e:
        assert False


# Generated at 2022-06-14 14:29:55.907878
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Zulu TZ
    assert DateTimeFormat().validate("1984-01-31T14:00:00Z") == datetime.datetime(1984, 1, 31, 14, 0, 0, tzinfo=datetime.timezone.utc)
    # TZ of - 2:00
    assert DateTimeFormat().validate("1984-01-31T14:00:00-02:00") == datetime.datetime(1984, 1, 31, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-2)))
    # TZ of + 2:00

# Generated at 2022-06-14 14:29:58.496874
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate("2020-05-20") == datetime.date(2020, 5, 20)


# Generated at 2022-06-14 14:30:04.662803
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2020-01-01") == datetime.date(2020, 1, 1)
    assert DateFormat().validate("2020-4-4") == datetime.date(2020, 4, 4)
    assert DateFormat().validate("2020-09-01") == datetime.date(2020, 9, 1)


# Generated at 2022-06-14 14:30:13.409449
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date1 = DateFormat()
    assert isinstance(date1.validate('2019-11-09'), datetime.date)
    assert isinstance(date1.validate('2019-12-09'), datetime.date)
    try:
        date1.validate('2019-15-30')
    except ValidationError as e:
        assert e.code == 'invalid'
    try:
        date1.validate('2019')
    except ValidationError as e:
        assert e.code == 'format'


# Generated at 2022-06-14 14:30:20.882991
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    DateTimeFormat().validate("2020-01-02T00:00:01Z")
    DateTimeFormat().validate("2020-01-02T00:00:01+03:00")
    DateTimeFormat().validate("2020-01-02T00:00:01+03:00:01")
    DateTimeFormat().validate("2020-01-02T00:00:01+03")
    DateTimeFormat().validate("2020-01-02T00:00:01+0300")
    DateTimeFormat().validate("2020-01-02T00:00:01+03:01")

# Generated at 2022-06-14 14:30:23.570950
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    result = format.validate("2019-01-20")
    assert result == datetime.date(2019, 1, 20)

# Generated at 2022-06-14 14:30:28.008497
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    tf.validate('12:34:56')
    tf.validate('12:34')
    tf.validate('12:34:56.789')
    tf.validate('12:34:56.789012')

# Generated at 2022-06-14 14:30:37.063008
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtformat = DateTimeFormat()
    dt = dtformat.validate("2020-01-01T01:01:01.123456+10:00")
    assert dt.strftime('%Y%m%d%H%M%S%f%z') == '20200101010101123456+1000'

# Generated at 2022-06-14 14:30:49.247776
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():

    # test_DateTimeFormat_validate_simple
    def test_DateTimeFormat_validate_simple():
        value = "2014-01-01T00:00:00Z"
        expected = datetime.datetime(2014, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
        actual = DateTimeFormat().validate(value)
        assert actual == expected

    # test_DateTimeFormat_validate_milliseconds
    def test_DateTimeFormat_validate_milliseconds():
        value = "2014-01-01T00:00:00.1234Z"
        expected = datetime.datetime(2014, 1, 1, 0, 0, 0, 123400, tzinfo=datetime.timezone.utc)
        actual = DateTimeFormat().validate

# Generated at 2022-06-14 14:30:53.990101
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate('10:00') == datetime.time(hour=10,minute=0)
    assert TimeFormat().validate('10:00:10') == datetime.time(hour=10,minute=0,second=10)
    assert TimeFormat().validate('10:00:10.123456') == datetime.time(hour=10,minute=0,second=10,microsecond=123456)


# Generated at 2022-06-14 14:30:57.339814
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_format.validate('12:00')
    time_format.validate('12:00:00')
    time_format.validate('12:00:00.000000')

# Generated at 2022-06-14 14:30:59.735914
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    with pytest.raises(NotImplementedError) as info:
        date.validate("2020-05-12")
    

# Generated at 2022-06-14 14:31:02.596900
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = '2019-01-23'
    obj = DateFormat()
    assert obj.validate(date) == datetime.date(2019, 1, 23)



# Generated at 2022-06-14 14:31:05.163134
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    date = format.validate('2019-05-07')
    assert date.day == 7
    assert date.month == 5
    assert date.year == 2019

# Generated at 2022-06-14 14:31:13.108024
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Case 1: value does not match with the given pattern
    # Case 1.1: value is not a string
    value1 = 123456
    try:
        df = DateFormat()
        df.validate(value1)
    except:
        print("Test case 1.1 pass")
    # Case 1.2: value is a string but value is not a date
    value2 = "1996-00-32"
    try:
        df = DateFormat()
        df.validate(value2)
    except:
        print("Test case 1.2 pass")
    # Case 2: value matches with pattern
    value3 = "1996-11-21"
    df = DateFormat()
    date = df.validate(value3)

# Generated at 2022-06-14 14:31:20.003316
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    assert format.validate("2020-01-01") == datetime.date(2020, 1, 1)
    assert format.validate("2020-01-31") == datetime.date(2020, 1, 31)
    assert format.validate("2020-02-01") == datetime.date(2020, 2, 1)
    assert format.validate("2020-03-31") == datetime.date(2020, 3, 31)
    assert format.validate("2020-04-01") == datetime.date(2020, 4, 1)
    assert format.validate("2020-05-31") == datetime.date(2020, 5, 31)
    assert format.validate("2020-06-01") == datetime.date(2020, 6, 1)

# Generated at 2022-06-14 14:31:24.500354
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    date1 = date.validate("1997-07-16")
    date2 = date.validate("2019-10-04")
    assert date1 == datetime.date(1997, 7, 16)
    assert date2 == datetime.date(2019,10,4)


# Generated at 2022-06-14 14:31:38.787338
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    try:
        assert format.validate("2000-01-01") == datetime.date(2000, 1, 1)
        assert format.validate("2000-1-1") == datetime.date(2000, 1, 1)
        assert format.validate("2000-01-1") == datetime.date(2000, 1, 1)
        assert format.validate("2000-1-01") == datetime.date(2000, 1, 1)
    except AssertionError as e:
        raise Exception(e)


# Generated at 2022-06-14 14:31:46.821802
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    try:
        DateFormat().validate("1999-1-1")
        DateFormat().validate("1999-01-01")
    except Exception:
        raise AssertionError("method validate of class DateFormat has not been passed")
    
    try:
        DateFormat().validate("1999-1-1a")
        DateFormat().validate("1-1-1999")
        DateFormat().validate("1999-1")
        DateFormat().validate("1999")
        raise AssertionError("method validate of class DateFormat has not been passed")
    except ValueError:
        pass


# Generated at 2022-06-14 14:31:51.914921
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Case:
    #    - TimeFormat instance is created
    #    - method validate is called with a valid input
    #    - expected type: datetime.datetime
    x = TimeFormat()
    assert isinstance(x.validate("12:30"), datetime.time)


# Generated at 2022-06-14 14:31:54.066035
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    fmt = datetimeformat.DateTimeFormat()
    time = datetime.datetime.now()
    assert fmt.validate(time.isoformat()) == time

# Generated at 2022-06-14 14:32:00.920760
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    import pdb; pdb.set_trace()
    t=tf.validate("11:22:33")
    assert isinstance(t, datetime.time)
    assert t.hour==11
    assert t.minute==22
    assert t.second==33
    #assert t.microsecond==0
    t=tf.validate("11:22:33.123456")
    assert isinstance(t, datetime.time)
    assert t.hour==11
    assert t.minute==22
    assert t.second==33
    assert t.microsecond==123456

# Example of how to use the code
if __name__ == '__main__':
    test_TimeFormat_validate()

# Generated at 2022-06-14 14:32:03.749181
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    rule = TimeFormat()
    res = rule.validate("12:59:59.999999Z")
    assert isinstance(res, datetime.time)



# Generated at 2022-06-14 14:32:07.895683
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
  time_value = "12:39"
  time_result = {
    'hour': 12,
    'minute': 39
  }
  time_test = TimeFormat().validate(time_value)
  assert time_test.isoformat(' ') == time_result

# Generated at 2022-06-14 14:32:12.794217
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    from typesystem.formats import DateTimeFormat
    import datetime

    _format = DateTimeFormat()
    value = datetime.datetime(2019,11,3,0,0,0,0)
    result = value
    assert _format.validate("2019-11-03T00:00:00Z") == result, "Method validate of class DateTimeFormat failed!"


# Generated at 2022-06-14 14:32:23.257416
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    try:
        tf.validate('11:22:33')
    except ValidationError as e:
        assert False

    try:
        tf.validate('11:22')
    except ValidationError as e:
        assert False

    try:
        tf.validate('11:22:33.123')
    except ValidationError as e:
        assert False

    try:
        tf.validate('11:22:33.123456')
    except ValidationError as e:
        assert False

    try:
        tf.validate('11:22:33.1234567')
    except ValidationError as e:
        assert False

    try:
        tf.validate('11:22:33.12345678')
    except ValidationError as e:
        assert False

   

# Generated at 2022-06-14 14:32:35.507973
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()

    assert time.validate("00:00:00.0000") == datetime.time(0, 0, 0, 0)
    assert time.validate("00:00:00") == datetime.time(0, 0, 0)
    assert time.validate("00:00") == datetime.time(0, 0)
    assert time.validate("00:00:00.1") == datetime.time(0, 0, 0, 100000)
    assert time.validate("23:59:59") == datetime.time(23, 59, 59)

    with pytest.raises(ValidationError):
        time.validate("00:60:00")

    with pytest.raises(ValidationError):
        time.validate("24:00:00")


# Generated at 2022-06-14 14:32:47.693006
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    a = DateFormat()
    assert a.validate('2020-04-15') == datetime.date(2020, 4, 15)
    try:
        a.validate('2020-04-32')
    except ValidationError as e:
        print('ValidationError: ' + e.error_code + ' ' + e.error_text)


# Generated at 2022-06-14 14:32:56.150115
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    data = """
    2016-12-12
    """
    lines = data.splitlines()
    for line in lines:
        line = line.strip()
        if line:
            date = DateFormat()
            date_ = date.validate(line)
            assert date_ == datetime.date(2016, 12, 12)

    from typesystem.utils import to_camel_case
    import datetime
    from uuid import UUID
    assert to_camel_case(str(datetime.date(2016, 12, 12))) == "Date20161212"

# Generated at 2022-06-14 14:32:58.738052
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2000-04-02') == datetime.date(2000, 4, 2)


# Generated at 2022-06-14 14:33:02.753445
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    date = dateFormat.validate("2010-01-01")
    assert date.year == 2010
    assert date.month == 1
    assert date.day == 1


# Generated at 2022-06-14 14:33:07.481205
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    value = DateTimeFormat()
    assert value.validate('2020-02-19T14:45:00+00:00') == datetime.datetime(2020, 2, 19, 14, 45, tzinfo=datetime.timezone.utc)


# Generated at 2022-06-14 14:33:15.925267
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.is_native_type(datetime.date.today()) == True
    assert df.is_native_type(datetime.datetime.now()) == False
    assert df.validate("2019-01-01") == datetime.date(2019, 1, 1)
    assert df.validate("2019-01-01") == datetime.date(2019, 1, 1)
    assert df.serialize(datetime.date.today()) == datetime.date.today().isoformat()


# Generated at 2022-06-14 14:33:24.849758
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    match_value = datetime.time(hour=15, minute=30, second=45, microsecond=123456)
    non_match_value1 = "15:30:45.12345"
    non_match_value2 = "15:30:45.123456"
    input_value1 = "15:30:45.1234567"
    input_value2 = "15:30:45"

    t_format = TimeFormat()
    assert t_format.validate(input_value1) == match_value
    assert t_format.validate(input_value2) == datetime.time(15, 30, 45)
    try:
        t_format.validate(non_match_value1)
    except ValidationError as e:
        assert e.code == "format"