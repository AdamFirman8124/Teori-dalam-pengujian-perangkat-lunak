

# Generated at 2022-06-14 14:23:32.105248
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    utc = datetime.timezone.utc
    date = datetime.datetime(year = 2020, month = 4, day = 22, tzinfo = utc)
    a = DateTimeFormat()
    assert a.serialize(date) == "2020-04-22T00:00:00+00:00"

# Generated at 2022-06-14 14:23:38.238127
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date1 = '2117-12-31'
    date = DateFormat()
    date1 = date.validate(date1)
    assert isinstance(date1,datetime.date)
    assert date1.isoformat() == '2117-12-31'

    date2 = '2117-12-32'
    try:
        date.validate(date2)
    except ValidationError:
        pass
    else:
        assert False

    date3 = '2s17-12-31'
    try:
        date.validate(date3)
    except ValidationError:
        pass
    else:
        assert False


# Generated at 2022-06-14 14:23:50.078401
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    a = TimeFormat()
    now = datetime.datetime.now()
    time1 = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    time2 = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, 0)
    time3 = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, 6)
    assert a.serialize(time1) == time1.isoformat()
    assert a.serialize(time2) == time2.isoformat()
    assert a.serialize(time3) == time3.isoformat()

# Generated at 2022-06-14 14:23:53.139732
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    assert DateFormat().serialize(datetime.date(2020, 3, 7)) == "2020-03-07"


# Generated at 2022-06-14 14:23:56.644921
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_format = UUIDFormat()
    value = "25bfe1e3-c410-4638-aa43-f128840aad99"
    assert str(uuid_format.validate(value)) == value
    

# Generated at 2022-06-14 14:23:58.666049
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2020-01-01') == datetime.date(2020, 1, 1)


# Generated at 2022-06-14 14:24:01.239737
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuidFormat = UUIDFormat()
    assert type(uuidFormat.validate("6ba7b810-9dad-11d1-80b4-00c04fd430c8")) is uuid.UUID

# Generated at 2022-06-14 14:24:09.001759
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format = DateTimeFormat()
    assert date_time_format.validate('2019-12-04T11:36:26') == datetime(2019, 12, 4, 11, 36, 26)
    assert date_time_format.validate('2019-09-05T12:37:27-07:00') == datetime(2019, 9, 5, 12, 37, 27, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000)))
    assert date_time_format.validate('2019-09-05T12:37:27.567+05:30') == datetime(2019, 9, 5, 12, 37, 27, 567000, tzinfo=datetime.timezone(datetime.timedelta(days=0, seconds=19800)))


# Generated at 2022-06-14 14:24:13.005198
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
	assert DateFormat().serialize(obj=datetime.date(year=2020,month=10,day=23)) == '2020-10-23'
	assert DateFormat().serialize(obj=datetime.date(year=1999,month=12,day=31)) == '1999-12-31'


# Generated at 2022-06-14 14:24:14.502621
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    d = DateTimeFormat()
    d.validate("2019-05-30T12:34:56+00:00")

# Generated at 2022-06-14 14:24:21.949696
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2006-07-14") == datetime.date(2006, 7, 14)


# Generated at 2022-06-14 14:24:26.322744
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    tfmt = TimeFormat()
    dt = datetime.time(15,45,59)
    assert tfmt.serialize(dt) == "15:45:59"
    # assert tfmt.serialize(dt.isoformat()) == "15:45:59"

# Generated at 2022-06-14 14:24:28.683274
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    formats=TimeFormat()
    time=datetime.time(1,2)
    assert time.isoformat()==formats.serialize(time)

# Generated at 2022-06-14 14:24:34.034268
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    dformat = DateFormat()
    date = datetime.date(2020, 5, 11)
    print(dformat.serialize(date))
    assert dformat.serialize(date) == '2020-05-11'


# Generated at 2022-06-14 14:24:41.505591
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    form = TimeFormat()
    # test default
    assert str(form.validate("00:00:00")) == "00:00:00"
    assert str(form.validate("23:59:59")) == "23:59:59"
    # test with microseconds
    assert str(form.validate("00:00:00.123456")) == "00:00:00.123456"
    assert str(form.validate("23:59:59.123456")) == "23:59:59.123456"
    # test with microseconds and missing seconds
    assert str(form.validate("00:00:00.123456")) == "00:00:00.123456"
    assert str(form.validate("23:59:59.123456")) == "23:59:59.123456"

# Generated at 2022-06-14 14:24:45.961083
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    f = DateFormat()
    assert f.validate("2019-01-01") == datetime.date(2019, 1, 1)
    assert f.validate("1990-12-31") == datetime.date(1990, 12, 31)


# Generated at 2022-06-14 14:24:49.983323
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate('23:55:55') == datetime.time(hour=23, minute=55, second=55, tzinfo=None)
    with pytest.raises(ValidationError):
        TimeFormat().validate('23:55:55a')
        TimeFormat().validate('')



# Generated at 2022-06-14 14:25:01.673117
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # 1.  The 'time' must be a string
    # 2.  The 'time' must be a valid time format
    # 3.  The 'time' must be a real time
    format = TimeFormat()
    case1 = {
        1: (1, ValueError),
        "1": (1, ValueError),
        "10:10:10": (1, ValueError),
        "10:10:10.10": (1, ValueError),
        "10:10:10.10.10": (1, ValueError)}
    for case, expect in case1.items():
        try:
            format.validate(case)
            flag = 0
        except Exception as e:
            flag = 1
        assert flag == expect[0]
        if expect[0] == 1:
            assert type(e) == expect

# Generated at 2022-06-14 14:25:04.729614
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date1 = DateFormat()
    assert date1.serialize(datetime.date.today()) == datetime.date.today().isoformat()
    assert date1.serialize(None) == None


# Generated at 2022-06-14 14:25:08.650520
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time_format = TimeFormat()
    assert time_format.serialize(datetime.time(10, 15, 5)) == '10:15:05'
    assert time_format.serialize(datetime.time(10, 15, 5, 300000)) == '10:15:05.300000'
    assert time_format.serialize(None) == None

# Generated at 2022-06-14 14:25:13.975206
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    _instance_DateFormat = DateFormat()
    assert _instance_DateFormat.validate("2018-11-23")


# Generated at 2022-06-14 14:25:18.452925
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    timeformat_obj = TimeFormat()
    time_obj = datetime.time(5, 2, 40, 123456)
    assert timeformat_obj.serialize(time_obj) == "05:02:40.123456"

# Generated at 2022-06-14 14:25:22.672702
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2020-01-01T00:00:00+00:00") == datetime.datetime(2020, 1, 1, tzinfo=datetime.timezone.utc)
'''
Unit tests for method serialize of class DateTimeFormat
'''

# Generated at 2022-06-14 14:25:26.375835
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    obj = datetime.time(12, 12, 12, 1234)
    result = TimeFormat().serialize(obj)
    expectedResult = '12:12:12.012340'

    assert(result == expectedResult)



# Generated at 2022-06-14 14:25:29.037640
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = datetime.date(2020,10,2)
    df = DateFormat()
    assert df.validate("2020-10-02") == d


# Generated at 2022-06-14 14:25:34.767378
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    # Test 1: value is datetime
    value = datetime.datetime.today()
    with pytest.raises(NotImplementedError):
        date_format.validate(value)
    # Test 2: value is not datetime
    value = "2020-01-01"
    assert date_format.validate(value) == datetime.date(2020, 1, 1)


# Generated at 2022-06-14 14:25:40.005680
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time_format = TimeFormat()
    assert time_format.serialize(datetime.time(10)) == '10:00:00'
    assert time_format.serialize(datetime.time(10,10)) == '10:10:00'
    assert time_format.serialize(datetime.time(10,10,10)) == '10:10:10'
    assert time_format.serialize(datetime.time(10,10,10,10)) == '10:10:10.000010'


# Generated at 2022-06-14 14:25:44.200473
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    tf = TimeFormat()
    time = datetime.time(hour=12, minute=30, second=23, microsecond=555)
    assert tf.serialize(time) == "12:30:23.000555"



# Generated at 2022-06-14 14:25:51.519201
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat().validate("00:00:10.123456")
    assert time.hour == 0
    assert time.minute == 0
    assert time.second == 10
    assert time.microsecond == 123456

    time = TimeFormat().validate("12:01:00")
    assert time.hour == 12
    assert time.minute == 1
    assert time.second == 0
    assert time.microsecond == 0


# Generated at 2022-06-14 14:25:54.256110
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    tf = TimeFormat()
    obj = datetime.time(17, 15, 52, 457000)
    assert tf.serialize(obj) == '17:15:52.457000'

# Generated at 2022-06-14 14:26:03.180804
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
	obj = datetime.datetime(year=2015, month=12, day=15, hour=4, minute=30, second=10, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
	test_obj = DateTimeFormat()
	assert test_obj.serialize(obj) == '2015-12-15T04:30:10+02:00'


# Generated at 2022-06-14 14:26:10.836583
# Unit test for method validate of class DateTimeFormat

# Generated at 2022-06-14 14:26:13.012495
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime(2020, 5, 20, 21, 11)
    assert DateTimeFormat().serialize(obj) == "2020-05-20T21:11:00Z"

# Generated at 2022-06-14 14:26:17.866859
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from datetime import datetime

    # Given
    dtf = DateTimeFormat()
    obj = dtf.validate('2019-01-01T10:00:00+00:00')
    assert type(obj) is datetime

    # When
    str_val = dtf.serialize(obj)

    # Then
    assert type(str_val) is str
    assert str_val == '2019-01-01T10:00:00Z'



# Generated at 2022-06-14 14:26:28.676572
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Create a timeformat object
    a = TimeFormat()
    # Test wrong input data
    # Input data: '12-13'
    # Expected output: ValidationError
    try:
        b = a.validate('12-13')
        assert False, "Expected ValidationError, got {} instead".format(type(b))
    except ValidationError as e:
        assert True
    # Input data: '12:13:41'
    # Expected output: datetime.time(12, 13, 41)
    b = a.validate('12:13:41')
    assert b == datetime.time(12, 13, 41)
    # Input data: '12:13:41.123456'
    # Expected output: datetime.time(12, 13, 41, 123456)

# Generated at 2022-06-14 14:26:32.182007
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    assert format.validate('2006-03-03') == datetime.date(2006, 3, 3)


# Generated at 2022-06-14 14:26:38.038531
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dateTimeFormat = DateTimeFormat()
    dateTimeFormat.validate("2019-10-23T12:13:14.123456+01:00")
    dateTimeFormat.validate("2019-10-23T12:13:14.123456Z")
    with pytest.raises(ValidationError):
        dateTimeFormat.validate("2019-10-23")
    with pytest.raises(ValidationError):
        dateTimeFormat.validate("2019-10-23T12:13:14.123456")
    with pytest.raises(ValidationError):
        dateTimeFormat.validate("2019-10-23T12:13:14.123456R")

# Generated at 2022-06-14 14:26:41.737347
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert(DateFormat().validate("2017-12-15") == datetime.date(2017,12,15))


# Generated at 2022-06-14 14:26:45.842900
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date = date_format.validate("2017-02-08")
    assert isinstance(date, datetime.date)
    assert date.day == 8
    assert date.month == 2
    assert date.year == 2017
    assert str(date) == "2017-02-08"



# Generated at 2022-06-14 14:26:52.046963
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()
    _format = datetime.datetime
    #
    assert format.validate("2018-12-31T10:00:12.900000Z") == _format(2018, 12, 31, 10, 0, 12, 900000, datetime.timezone.utc)
    assert format.validate("2018-12-31T10:00:12.900000+02:00") == _format(2018, 12, 31, 10, 0, 12, 900000, datetime.timezone(datetime.timedelta(0, 7200)))
    assert format.validate("2018-12-31T10:00:12.900000+0200") == _format(2018, 12, 31, 10, 0, 12, 900000, datetime.timezone(datetime.timedelta(0, 7200)))


# Generated at 2022-06-14 14:26:57.608811
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format = DateTimeFormat()
    date_time_format.validate("1999-12-31T23:59:59.999999-00:00")


# Generated at 2022-06-14 14:27:06.696464
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    value = '2019-02-01T15:30:00Z'
    # test if value match the regex
    assert DATETIME_REGEX.match(value)

    # test if value is native type
    fmt = DateTimeFormat()
    assert fmt.is_native_type(datetime.datetime(2019,2,1,15,30,0,0,datetime.timezone.utc))

    #test if validate method return is a datetime type
    datetime = fmt.validate(value)
    assert datetime



# Generated at 2022-06-14 14:27:15.629450
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    valid_value = "2020-11-07T15:26:49.485735+00:00"
    date_time_format = DateTimeFormat()
    date_time = date_time_format.validate(valid_value)
    assert isinstance(date_time, datetime.datetime)
    assert date_time.year == 2020
    assert date_time.month == 11
    assert date_time.day == 7
    assert date_time.hour == 15
    assert date_time.minute == 26
    assert date_time.second == 49
    assert date_time.microsecond == 485735
    assert date_time.tzinfo == datetime.timezone.utc


# Generated at 2022-06-14 14:27:23.608826
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()
    
    assert format.validate("2020-01-02T03:04:05") == datetime.datetime(2020,1,2,3,4,5)
    assert format.validate("2020-01-02T03:04:05Z") == datetime.datetime(2020,1,2,3,4,5,tzinfo=datetime.timezone.utc)
    assert format.validate("2020-01-02T03:04:05+07:00") == datetime.datetime(2020,1,2,3,4,5,tzinfo=datetime.timezone(datetime.timedelta(hours=7)))

# Generated at 2022-06-14 14:27:32.282845
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()


    for valid_time in [
        "23:59:59.999999",
        "23:59:59",
        "23:59",
        "23:59:59.999999999",
        "23:59:59:",
        "23:59:",
        "23:59:59.",
        "23:59:59.999999Z",
        "12:00:00.1",
    ]:
        assert time_format.validate(valid_time).isoformat() == valid_time



# Generated at 2022-06-14 14:27:42.240728
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
        x = DateTimeFormat()
        assert x.validate('2020-01-18T15:21:28Z') == datetime.datetime(2020, 1, 18, 15, 21, 28, tzinfo=datetime.timezone.utc)
        assert x.validate('2020-01-18T15:21:28.123456Z') == datetime.datetime(2020, 1, 18, 15, 21, 28, 123456, tzinfo=datetime.timezone.utc)
        assert x.validate('2020-01-18T15:21:28+03:30') == datetime.datetime(2020, 1, 18, 15, 21, 28, tzinfo=datetime.timezone(datetime.timedelta(0, 12600)))

# Generated at 2022-06-14 14:27:45.028843
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    value = "10:30:15.003"
    format = TimeFormat()
    format.validate(value) == datetime.time(10, 30, 15, 30000)


# Generated at 2022-06-14 14:27:57.417555
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    date.validate('2019-01-01')
    date.validate('2019-06-01')
    date.validate('2019-12-01')
    date.validate('2019-01-09')
    date.validate('2019-01-31')
    date.validate('2019-12-31')
    date.validate('2019-02-28')
    date.validate('2000-02-29')
    date.validate('2100-02-28')
    with pytest.raises(ValidationError):
        date.validate('199-01-01')
    with pytest.raises(ValidationError):
        date.validate('192-06-01')

# Generated at 2022-06-14 14:28:05.849736
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("1:12") == datetime.time(hour=1, minute=12)
    assert TimeFormat().validate("1:12:12") == datetime.time(hour=1, minute=12, second=12)
    assert TimeFormat().validate("1:12:12.123") == datetime.time(hour=1, minute=12, second=12, microsecond=123000)
    assert TimeFormat().validate("1:12:12.123456") == datetime.time(hour=1, minute=12, second=12, microsecond=123456)


# Generated at 2022-06-14 14:28:14.842657
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()

    # Validate formats with positive timezone offset
    value = "2020-07-22T15:15:30.33+04:00"
    expected_result = datetime.datetime(2020, 7, 22, 15, 15, 30, 330000, tzinfo=datetime.timezone(datetime.timedelta(hours=4)))
    assert expected_result == format.validate(value)

    # Validate formats without timezone offset
    value = "2020-07-22T15:15:30.33"
    expected_result = datetime.datetime(2020, 7, 22, 15, 15, 30, 330000)
    assert expected_result == format.validate(value)



# Generated at 2022-06-14 14:28:20.483285
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate('10:00') == datetime.time(10)


# Generated at 2022-06-14 14:28:30.840404
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    fmt = DateTimeFormat()
    with pytest.raises(ValidationError):
        fmt.validate('xyz')
    with pytest.raises(ValidationError):
        fmt.validate('2020-10-01T10:10:10')
    with pytest.raises(ValidationError):
        fmt.validate('2020-10-01T10:10:10Z')
    with pytest.raises(ValidationError):
        fmt.validate('01-01-01T10:10:10Z')
    with pytest.raises(ValidationError):
        fmt.validate('2020-10-01T10:10:10Z00')

# Generated at 2022-06-14 14:28:39.215913
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format = DateTimeFormat()
    assert date_time_format.validate("2020-01-01 00:00:00") == datetime.datetime(2020, 1, 1, 0, 0)
    assert date_time_format.validate("2020-01-01T00:00:00Z") == datetime.datetime(2020, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)
    assert date_time_format.validate("2020-01-01 00:00:00Z") == datetime.datetime(2020, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)


# Generated at 2022-06-14 14:28:41.702719
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    with pytest.raises(NotImplementedError):
        DateFormat().validate("2017-06-23")


# Generated at 2022-06-14 14:28:44.930202
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate(value="22:30:59.123456") == datetime.time(hour=22, minute=30, second=59, microsecond=123456)

# Generated at 2022-06-14 14:28:51.323801
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime_format = DateTimeFormat()
    value = '2018-07-10T15:00:00.123456-03:00'
    expected = datetime.datetime(2018, 7, 10, 15, 0, 0, 123456, tzinfo=datetime.timezone(datetime.timedelta(hours=-3)))
    assert datetime_format.validate(value) == expected

# Generated at 2022-06-14 14:29:03.092157
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("00:00:00") == datetime.time(0, 0)
    assert TimeFormat().validate("00:00:00.000000") == datetime.time(0, 0)
    assert TimeFormat().validate("00:00:00.123456") == datetime.time(0, 0, 0, 123456)
    assert TimeFormat().validate("01:02:03") == datetime.time(1, 2, 3)
    assert TimeFormat().validate("12:34:56.654321") == datetime.time(12, 34, 56, 654321)
    assert TimeFormat().validate("23:59:59") == datetime.time(23, 59, 59)

# Generated at 2022-06-14 14:29:07.254282
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()

    try:
        time.validate("01:59")
    except ValidationError:
        pass
    else:
        assert False

    assert datetime.time(1,59) == time.validate("01:59")


# Generated at 2022-06-14 14:29:18.026428
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert tf.validate("10:30:45+01:00") == datetime.time(
        hour=10, minute=30, second=45, tzinfo=datetime.timezone(datetime.timedelta(hours=1)))
    assert tf.validate("10:30:45Z") == datetime.time(
        hour=10, minute=30, second=45, tzinfo=datetime.timezone.utc)
    assert tf.validate("10:30:45.236541+01:00") == datetime.time(
        hour=10,
        minute=30,
        second=45,
        microsecond=236541,
        tzinfo=datetime.timezone(datetime.timedelta(hours=1)),
    )

# Generated at 2022-06-14 14:29:20.761488
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    testTime = datetime.time(12, 30)
    testStr = testTime.isoformat()
    timeFormat = TimeFormat()
    assert timeFormat.validate(testStr) == testTime


# Generated at 2022-06-14 14:29:33.065387
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # test_DateTimeFormat_validate_Z_even_hours
    test_obj = DateTimeFormat()
    check = test_obj.validate("2020-02-14T12:00:11Z")
    assert check == datetime.datetime(2020,2,14,12,0,11,tzinfo=datetime.timezone.utc)
    # test_DateTimeFormat_validate_Z_odd_hours
    test_obj = DateTimeFormat()
    check = test_obj.validate("2020-02-14T13:00:11Z")
    assert check == datetime.datetime(2020,2,14,13,0,11,tzinfo=datetime.timezone.utc)
    # test_DateTimeFormat_validate_Z_even_hours_and_minutes

# Generated at 2022-06-14 14:29:43.443785
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    check_DateFormat_validate = DateFormat().validate('2019-01-01')
    assert isinstance(check_DateFormat_validate, datetime.date)

    check_DateFormat_validate = DateFormat().validate('2019-13-01')
    assert isinstance(check_DateFormat_validate, ValidationError)

    check_DateFormat_validate = DateFormat().validate('2019-03-40')
    assert isinstance(check_DateFormat_validate, ValidationError)

    check_DateFormat_validate = DateFormat().validate('2019-01')
    assert isinstance(check_DateFormat_validate, ValidationError)

    check_DateFormat_validate = DateFormat().validate('2019')
    assert isinstance(check_DateFormat_validate, ValidationError)

    check_Date

# Generated at 2022-06-14 14:29:55.744977
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    match1 = DATETIME_REGEX.match('2017-10-14T10:05:54Z')
    match1_groups = match1.groupdict()
    tzinfo_str1 = match1_groups.pop('tzinfo')
    if tzinfo_str1 == 'Z':
        tzinfo1 = datetime.timezone.utc
    elif tzinfo_str1 is not None:
        offset_mins = int(tzinfo_str1[-2:]) if len(tzinfo_str1) > 3 else 0
        offset_hours = int(tzinfo_str1[1:3])
        delta = datetime.timedelta(hours=offset_hours,minutes=offset_mins)
        if tzinfo_str1[0] == '-':
            delta = -delta
       

# Generated at 2022-06-14 14:29:59.827229
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_format = DateFormat()
    date_value = '2018-11-01'
    date_result = date_format.validate(date_value) # get result of method validate
    assert isinstance(date_result, datetime.date) # check right type of result


# Generated at 2022-06-14 14:30:04.449914
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    validate=DateTimeFormat()
    result=validate.validate("2020-01-21 13:06:28")
    assert result == datetime.datetime(2020, 1, 21, 13, 6, 28)

# Generated at 2022-06-14 14:30:16.007254
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()
    assert format.validate("2018-01-01T01:23:45Z").isoformat() == "2018-01-01T01:23:45+00:00"
    assert format.validate("2018-01-01T01:23:45+01:00").isoformat() == "2018-01-01T01:23:45+01:00"
    assert format.validate("2018-01-01T01:23:45-01:00").isoformat() == "2018-01-01T01:23:45-01:00"
    assert format.validate("2018-01-01T01:23:45.6-01:00").isoformat() == "2018-01-01T01:23:45.600000-01:00"

# Generated at 2022-06-14 14:30:23.308017
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tz = TimeFormat()
    assert tz.validate("03:15:45") == datetime.time(3, 15, 45)
    assert tz.validate("03:15") == datetime.time(3, 15)
    assert tz.validate("03") == datetime.time(3)
    assert tz.validate("03:15:45.123") == datetime.time(3, 15, 45, 123000)



# Generated at 2022-06-14 14:30:27.221297
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeFormat = TimeFormat()
    time = timeFormat.validate("09:00:30")

    assert time.hour == 9
    assert time.minute == 0
    assert time.second == 30
    assert time.microsecond == 0


# Generated at 2022-06-14 14:30:28.605250
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate('00:00:00') == datetime.time(0, 0)


# Generated at 2022-06-14 14:30:32.050815
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    input = datetime.datetime(2019, 10, 23, 14, 34, 42, 42)
    datetime_format = DateTimeFormat()
    result = datetime_format.validate(input)
    assert(result == input)



# Generated at 2022-06-14 14:30:39.430271
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate("23:59:59.999999") == datetime.time(23, 59, 59, 999999)


# Generated at 2022-06-14 14:30:44.074789
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format = TimeFormat()
    value = format.validate('12:00:00')
    assert value.hour == 12
    value = format.validate('12:00')
    assert value.hour == 12
    value = format.validate('12:00:00.123')
    assert value.hour == 12
    assert value.microsecond == 123000


# Generated at 2022-06-14 14:30:46.204950
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    X = TimeFormat()
    assert isinstance(X.validate('15:23:49.999999'), datetime.time)

# Generated at 2022-06-14 14:30:54.298438
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert(DateTimeFormat().validate("2019-07-08T20:52:07.079768Z")) == datetime.datetime(2019, 7, 8, 20, 52, 7, 79768, tzinfo=datetime.timezone.utc)
    assert(DateTimeFormat().validate("2019-07-08T20:52:07.079768+00:00")) == datetime.datetime(2019, 7, 8, 20, 52, 7, 79768, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:30:59.191264
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("09:00:12") == datetime.time(9, 0, 12)
    assert TimeFormat().validate("09:00:12.23") == datetime.time(9, 0, 12, 230000)



# Generated at 2022-06-14 14:31:06.955169
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t1 = TimeFormat()
    print(t1.validate('12:34:56.123456'))
    print(t1.validate('12:34:56.12345'))
    print(t1.validate('12:34:56.1234'))
    print(t1.validate('12:34:56.'))
    print(t1.validate('12:34:56'))
    print(t1.validate('12:34:'))
    print(t1.validate('12:34'))
    print(t1.validate('12:'))


# Generated at 2022-06-14 14:31:16.503710
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("00:00:00") == datetime.time(0, 0, 0)
    assert TimeFormat().validate("00:00:00.000001") == datetime.time(0, 0, 0, 1)
    assert TimeFormat().validate("00:00:00.000001") == datetime.time(0, 0, 0, 1)
    assert TimeFormat().validate("00:00:00.000010") == datetime.time(0, 0, 0, 10)
    assert TimeFormat().validate("00:00:00.000100") == datetime.time(0, 0, 0, 100)
    assert TimeFormat().validate("00:00:00.001000") == datetime.time(0, 0, 0, 1000)

# Generated at 2022-06-14 14:31:24.309779
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # If a format is invalid, then it should raise "invalid" error
    datetimeFormat = DateTimeFormat()
    value = "2018-12-31T23:59:59+0000"
    # 0 is not a valid hour
    try:
        datetimeFormat.validate(value)
    except ValidationError as e:
        assert(e.code == "invalid")
    assert(e.text == "Must be a real datetime.")
    # DateTimeFormat raise "invalid" error if a datetime is invalid.


# Generated at 2022-06-14 14:31:26.428536
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate('2019-08-27') == datetime.date(2019,8,27)


# Generated at 2022-06-14 14:31:37.748766
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    time_str = "2006-10-25T08:15:30-06:00"
    time_str_test = "2006-10-25T08:15:30-05:00"
    time_str_test_1 = "2006-10-25T08:15:30-07:00"
    time_str_test_2 = "2006-10-25T22:15:30+01:00"
    time_str_test_3 = "2006-10-25T08:15:30Z"
    time_str_test_4 = "2006-10-25T08:15:30"
    time_str_test_5 = "2006/10/25T08:15:30"
    time_str_test_6 = "2006-10-25T08:15"
    time_str_test

# Generated at 2022-06-14 14:31:45.792861
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timefmt = TimeFormat()
    test_time = '10:10:10.1'
    time = timefmt.validate(test_time)
    assert time, datetime.time(10, 10, 10, 100000)

# Generated at 2022-06-14 14:31:50.414914
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.is_native_type(datetime.time.now()) == True
    assert time.validate("12:30:59.999999") == datetime.time(12, 30, 59, 999999)


# Generated at 2022-06-14 14:31:51.639412
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf=TimeFormat()
    time=tf.validate("00:00:00")
    assert time.isoformat()=="00:00:00"

# Generated at 2022-06-14 14:31:57.191049
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from datetime import datetime, time
    from typesystem.base import Format
    from typesystem.formats import TimeFormat

    assert TimeFormat(required=True).validate('13:37:00') == time(13, 37, 0)
    assert TimeFormat(required=True).validate('13:37:00.123000') == time(13, 37, 0, 123000)
    assert TimeFormat(required=True).validate('13:37:00.12300') == time(13, 37, 0, 123000)
    assert TimeFormat(required=True).validate('13:37:00.1230') == time(13, 37, 0, 123000)
    assert TimeFormat(required=True).validate('13:37:00.123') == time(13, 37, 0, 123000)

# Generated at 2022-06-14 14:32:03.121536
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()

    try:
        time_format.validate(None)
    except ValueError:
        pass

    try:
        time_format.validate(12)
    except ValueError:
        pass

    try:
        time_format.validate("123")
    except ValueError:
        pass

    try:
        time_format.validate("25:14")
    except ValueError:
        pass

    try:
        time_format.validate("12:61")
    except ValueError:
        pass

    try:
        time_format.validate("12:60:10")
    except ValueError:
        pass

    try:
        time_format.validate("12:00:61")
    except ValueError:
        pass


# Generated at 2022-06-14 14:32:12.238729
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Test case 1
    time = TimeFormat()
    value = "11:59"
    serial = time.validate(value)
    assert serial == datetime.time(11,59)

    # Test case 2
    time = TimeFormat()
    value = "20:34:22"
    serial = time.validate(value)
    assert serial == datetime.time(20,34,22)
    
    # Test case 3
    time = TimeFormat()
    value = "10:59:55.12"
    serial = time.validate(value)
    assert serial == datetime.time(10,59,55,120000)

    # Test case 4
    time = TimeFormat()
    value = "11:30:00.000"
    serial = time.validate(value)
    assert serial == datetime

# Generated at 2022-06-14 14:32:18.510260
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    assert t.validate("12:30:00.000000")==datetime.time(12, 30)
    assert t.validate("12:30:00.2523")==datetime.time(12, 30, 0, 252300)
    import pytest
    with pytest.raises(ValidationError):
        t.validate("12:60:00.2523")

# Generated at 2022-06-14 14:32:20.053852
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeStr = '17:36:30.000001'
    timeFormat = TimeFormat()
    timeFormat.validate(timeStr)
    assert True


# Generated at 2022-06-14 14:32:31.399965
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    with pytest.raises(ValidationError):
        tf.validate('12:00')
    with pytest.raises(ValidationError):
        tf.validate('12:00:00')
    with pytest.raises(ValidationError):
        tf.validate('12:00:00.123456')
    with pytest.raises(ValidationError):
        tf.validate('12:00:00.1234567')
    with pytest.raises(ValidationError):
        tf.validate('12:00:00.12345678')
    with pytest.raises(ValidationError):
        tf.validate('12:00:00.123456789')

# Generated at 2022-06-14 14:32:34.375401
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    my_format = TimeFormat()
    assert my_format.validate('20:57:41') == datetime.time(20,57,41)
    assert my_format.validate('20:57') == datetime.time(20,57)


# Generated at 2022-06-14 14:32:40.230026
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format_object = TimeFormat()
    assert format_object.validate("12:30:59") == datetime.time(12,30,59)

# Generated at 2022-06-14 14:32:46.898092
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value1 = "2012-12-12"
    value2 = "2012-12-13"
    result1 = DateFormat()
    result1.validate(value1)
    result2 = DateFormat()
    result2.validate(value2)
    assert str(result1.validate(value1)) == "2012-12-12"
    assert str(result2.validate(value2)) == "2012-12-13"


# Generated at 2022-06-14 14:32:50.588636
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate('2020-02-24') == datetime.date(2020, 2, 24)
    try:
        df.validate('2020-02-30')
    except ValidationError:
        return 1
    return 0


# Generated at 2022-06-14 14:32:53.163276
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    expected = '1900-01-01'
    actual = dateFormat.validate('1900-01-01')
    assert expected == actual.isoformat()

# Generated at 2022-06-14 14:32:54.889834
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2019-12-12") == datetime.date(2019, 12, 12)


# Generated at 2022-06-14 14:33:01.998942
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    cota = DateFormat()
    data = "2019-04-07"
    assert cota.validate(data) == datetime.date(2019, 4, 7)
    data = "2019-14-07"
    try:
        assert cota.validate(data)
    except Exception as e:
        assert e.args[0] == "Must be a real date."


# Generated at 2022-06-14 14:33:05.291222
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = '0001-01-02'
    test_value = DateFormat().validate(value)
    assert isinstance(test_value,datetime.date)


# Generated at 2022-06-14 14:33:12.432052
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("00:00:00") == datetime.time(0, 0, 0)
    assert TimeFormat().validate("01:30:00") == datetime.time(1, 30)
    assert TimeFormat().validate("01:30:59") == datetime.time(1, 30, 59)
    assert TimeFormat().validate("01:30:59.123000") == datetime.time(1, 30, 59, 123000)



# Generated at 2022-06-14 14:33:17.195444
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    tf.validate("00:00:00")
    tf.validate("23:59:59")
    tf.validate("12:12:12.123456")
    tf.validate("12:12:12.999999")