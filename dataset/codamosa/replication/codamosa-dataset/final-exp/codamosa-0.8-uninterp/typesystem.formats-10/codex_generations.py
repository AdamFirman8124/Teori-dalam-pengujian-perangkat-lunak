

# Generated at 2022-06-14 14:23:38.052646
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    t1 = tf.validate("15:58")
    assert t1.hour == 15
    assert t1.minute == 58
    assert t1.tzinfo == None
    t2 = tf.validate("15:58:59.123")
    assert t2.hour == 15
    assert t2.minute == 58
    assert t2.second == 59
    assert t2.microsecond == 123000
    assert t2.tzinfo == None
    t3 = tf.validate("15:58:59.123567")
    assert t3.hour == 15
    assert t3.minute == 58
    assert t3.second == 59
    assert t3.microsecond == 123567
    assert t3.tzinfo == None

# Generated at 2022-06-14 14:23:49.948971
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # test case 1
    value = '2004-02-23T13:13:13'
    dt = DateTimeFormat().validate(value)
    assert dt.year == 2004
    assert dt.month == 2
    assert dt.day == 23
    assert dt.hour == 13
    assert dt.minute == 13
    assert dt.second == 13

    # test case 2
    value = '2004-02-23T13:13:13.000000'
    dt = DateTimeFormat().validate(value)
    assert dt.year == 2004
    assert dt.month == 2
    assert dt.day == 23
    assert dt.hour == 13
    assert dt.minute == 13
    assert dt.second == 13

    # test case 3

# Generated at 2022-06-14 14:24:00.590879
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime_format = DateTimeFormat()

    obj0 = datetime_format.validate("2010-12-26T12:30:06")
    assert obj0.__class__ is datetime.datetime
    assert obj0.year == 2010
    assert obj0.month == 12
    assert obj0.day == 26
    assert obj0.hour == 12
    assert obj0.minute == 30
    assert obj0.second == 6

    obj1 = datetime_format.validate("2010-12-26T12:30:06.123456")
    assert obj1.__class__ is datetime.datetime
    assert obj1.year == 2010
    assert obj1.month == 12
    assert obj1.day == 26
    assert obj1.hour == 12
    assert obj1.minute == 30
    assert obj1.second

# Generated at 2022-06-14 14:24:01.761884
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert  DateTimeFormat().validate(None)==None


# Generated at 2022-06-14 14:24:04.606867
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    obj = TimeFormat()
    value = '10:30:23'
    assert (obj.validate(value) == datetime.time(10, 30, 23)), "Failed to validate time value"



# Generated at 2022-06-14 14:24:08.855812
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate('12:33:6') == datetime.time(12,33,6)
    assert time.validate('12:33:6.012345') == datetime.time(12,33,6,12345)


# Generated at 2022-06-14 14:24:11.356730
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert str(TimeFormat().serialize(datetime.time.fromisoformat('15:45:10'))) == '15:45:10'


# Generated at 2022-06-14 14:24:19.077277
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dt = datetime.datetime(2020, 4, 1)
    dateTime =DateTimeFormat()
    dateTime.validate(dt.isoformat())
    with pytest.raises(NotImplementedError):
        dateTime.validate(dt.isoformat())
    match = DATETIME_REGEX.match('2020-04-01T20:12:23.000000Z')
    
    # case 1: timezone is 'Z'
    assert dateTime.validate(dt.isoformat(timespec='microseconds')) == '2020-04-01T20:12:23.000000Z'
    # case 2: timezone is '+-##'

# Generated at 2022-06-14 14:24:25.573947
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_format = UUIDFormat()
    assert uuid_format.validate("c38286b1-d8ce-4c87-b11d-f0dde84314a6") == uuid.UUID('c38286b1-d8ce-4c87-b11d-f0dde84314a6')


# Generated at 2022-06-14 14:24:30.393683
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # arrange
    input_obj = datetime.datetime(2019, 12, 3, 11, 5)
    expected_output = "2019-12-03T11:05:00"
    date_time_format = DateTimeFormat()
    # act
    actual_output = date_time_format.serialize(input_obj)
    # assert
    assert expected_output == actual_output



# Generated at 2022-06-14 14:24:47.561973
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    df = DateTimeFormat()
    dt = datetime.datetime(2018,1,1,1,1,1)
    assert df.validate("2018-01-01T01:01:01") == dt
    assert df.validate("2018-01-01 01:01:01") == dt
    assert df.validate("2018-01-01T01:01:01+00:00") == dt
    assert df.validate("2018-01-01T01:01:01Z") == dt

    assert df.validate("2018-01-01T01:01:01.123456") == datetime.datetime(2018,1,1,1,1,1,123456)
    assert df.validate("2018-01-01T01:01:01.12") == datetime.datetime

# Generated at 2022-06-14 14:24:49.169692
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate("2020-04-14") == datetime.date(2020, 4, 14)



# Generated at 2022-06-14 14:24:58.424984
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    d = DateTimeFormat()
    assert d.serialize(datetime.datetime(2000,1,1)) == "2000-01-01T00:00:00"
    assert d.serialize(datetime.datetime(2000,1,1, tzinfo=datetime.timezone.utc)) == "2000-01-01T00:00:00Z"
    assert d.serialize(datetime.datetime(2000,1,1, tzinfo=datetime.timezone(datetime.timedelta(hours=1)))) == "2000-01-01T00:00:00+01:00"


# Generated at 2022-06-14 14:25:05.372019
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    # test case 1: value is not a valid date
    # test for error 'invalid'
    value = "2019"
    try:
        date.validate(value)
    except ValidationError as error:
        assert error.code == "invalid"

    # test case 2: value is a valid date
    value = "2019-01-01"
    res = date.validate(value)
    assert isinstance(res, datetime.date)


# Generated at 2022-06-14 14:25:16.148246
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    _time = tf.validate('13:13')
    assert(isinstance(_time, datetime.time))
    assert(_time.hour == 13)
    assert(_time.minute == 13)
    _time = tf.validate('13:13:13')
    assert(isinstance(_time, datetime.time))
    assert(_time.hour == 13)
    assert(_time.minute == 13)
    assert(_time.second == 13)
    _time = tf.validate('13:13:13.613')
    assert(isinstance(_time, datetime.time))
    assert(_time.hour == 13)
    assert(_time.minute == 13)
    assert(_time.second == 13)
    assert(_time.microsecond == 613000)


# Generated at 2022-06-14 14:25:27.392502
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timefmt = TimeFormat()
    test_values = {
        "00:00:00":datetime.datetime(1900, 1, 1, 0, 0),
        "00:00:01":datetime.datetime(1900, 1, 1, 0, 0, 1),
        "00:00:01.12":datetime.datetime(1900, 1, 1, 0, 0, 1, 120000),
        "01:02:03.1234":datetime.datetime(1900, 1, 1, 1, 2, 3, 123400),
        "01:02:03.123456":datetime.datetime(1900, 1, 1, 1, 2, 3, 123456)
    }
    for test_str in test_values:
        time = timefmt.validate(test_str)

# Generated at 2022-06-14 14:25:30.971210
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = DateFormat()
    d.validate("1990-10-11")
    d.validate("1800-03-20")
    d.validate("0-3-20")
    d.validate("0-03-20")


# Generated at 2022-06-14 14:25:39.630446
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate(
        "2020-07-10T00:00:00+0100"
    ) == datetime.datetime(
        2020, 7, 10, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=1))
    )
    assert DateTimeFormat().validate(
        "2020-07-10T00:00:00+01:00"
    ) == datetime.datetime(
        2020, 7, 10, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=1))
    )

# Generated at 2022-06-14 14:25:47.018534
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    # key = input, value = output
    inputs_outputs = {
        None: None,
        datetime.time(0, 0, 1): "00:00:01",
        datetime.time(0, 0, 1, 100000): "00:00:01.100000",
    }
    time_formatter = TimeFormat()
    for obj, serialized in inputs_outputs.items():
        assert time_formatter.serialize(obj) == serialized

# Generated at 2022-06-14 14:25:58.526867
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    assert t.validate("12:30") == datetime.time(12, 30)
    assert t.validate("12:30:30") == datetime.time(12, 30, 30)
    assert t.validate("12:30:30.99") == datetime.time(12, 30, 30, 990000)
    assert t.validate("12:30:30.999999") == datetime.time(12, 30, 30, 999999)

    with pytest.raises(ValidationError):
        t.validate("00:60")
    with pytest.raises(ValidationError):
        t.validate("24:00")
    with pytest.raises(ValidationError):
        t.validate("00:00:60")

# Generated at 2022-06-14 14:26:03.656402
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    d1 = datetime.date(2020, 1, 1)
    date_format = DateFormat()
    assert date_format.serialize(d1) == "2020-01-01"


# Generated at 2022-06-14 14:26:09.390194
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    item = DateTimeFormat()
    obj = datetime.datetime(2019, 1, 1, 0, 0, 0)

    ret = item.serialize(obj)

    assert ret == "2019-01-01T00:00:00Z"

# Generated at 2022-06-14 14:26:11.882601
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    obj = datetime.date(2018, 11, 6)
    my_format = DateFormat()
    assert '2018-11-06' == my_format.serialize(obj)


# Generated at 2022-06-14 14:26:14.629186
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time_format = TimeFormat()
    assert time_format.serialize(datetime.time(3, 4, 5, 60000)) == "03:04:05.060000"



# Generated at 2022-06-14 14:26:22.725015
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test case 1
    obj = DateFormat()
    value = "1998-12-31"
    x = obj.validate(value)
    assert x == datetime.date(1998,12,31)
    # Test case 2
    obj = DateFormat()
    value = "2222-21-32"
    x = obj.validate(value)
    try:
        assert x == datetime.date(2222,21,32) 
    except ValueError:
        assert True 


# Generated at 2022-06-14 14:26:25.286127
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
	date = datetime.date(1234,5,6)
	assert DateFormat().serialize(date) == '1234-05-06'


# Generated at 2022-06-14 14:26:32.130275
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
	from typesystem.base import Schema

	data = datetime.datetime.now().time()
	class SmallTimeSchema(Schema):
		time = fields.Time()

	smallTimeSchema = SmallTimeSchema()
	assert smallTimeSchema.serialize({"time": data}) == {"time": data.isoformat(sep='T', timespec='milliseconds')}

# Generated at 2022-06-14 14:26:41.253438
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Tests that the validation passes with an input of a valid datetime.
    assert DateTimeFormat().validate("2020-04-06T09:07:17+00:00") == \
        datetime.datetime(2020, 4, 6, 9, 7, 17, 0, datetime.timezone.utc)

    # Tests that the validation fails with an input of an invalid datetime.
    # The method should raise a ValidationError with code "invalid".
    with pytest.raises(ValidationError) as excinfo:
        DateTimeFormat().validate("2020-04-06T09:07:17+00:00-52:00")
    assert excinfo.value.args[0] == "Must be a real datetime."
    assert excinfo.value.code == "invalid"

    # Tests that the validation fails with

# Generated at 2022-06-14 14:26:48.970855
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    x = DateTimeFormat()
    print(x.validate('2019-12-02T00:00:00.000Z').isoformat())
    print(x.validate('2019-12-02T00:00:00.000+00:00').isoformat())
    print(x.validate('2019-12-02T00:00:00.000+01:00').isoformat())
    print(x.validate('2019-12-02T00:00:00.000+01:00').isoformat())
    print(x.validate('2019-12-02T00:00:00.000-01:00').isoformat())
    print(x.validate('2019-12-02T00:00:00.000-01').isoformat())

# Generated at 2022-06-14 14:26:53.341434
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    import datetime

    # function serialize will return str type data
    date = datetime.date(2020, 7, 21)
    df = DateFormat()

    assert type(df.serialize(date)) == str

# Generated at 2022-06-14 14:27:01.112826
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    tf = TimeFormat()
    time = datetime.time(second=32, minute=12, hour=23, microsecond=123456)
    assert tf.serialize(time) == tf.serialize(time)
    assert tf.serialize(time) == "23:12:32.123456"



# Generated at 2022-06-14 14:27:12.011839
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # create an instance of class DateFormat
    dateFormat = DateFormat()

    # test for valid date format
    dateFormat.validate("2020-04-01")

    # test for invalid date format
    try:
        dateFormat.validate("20200401")
    except ValidationError as e:
        assert e.code == "format"
        assert e.text.count("Must be a valid date format.") == 1

    # test for invalid date
    try:
        dateFormat.validate("2020-13-01")
    except ValidationError as e:
        assert e.code == "invalid"
        assert e.text.count("Must be a real date.") == 1



# Generated at 2022-06-14 14:27:21.719031
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d_fmt = DateFormat()
    # 1. pass the test
    date_1 = d_fmt.validate("2018-02-02")
    date_2 = d_fmt.validate("2017-03-03")
    date_3 = datetime.date(2018, 2, 2)
    assert date_1 == date_2
    assert date_1 == date_3
    assert date_3 == date_2

    # 2. pass the test
    assert d_fmt.is_native_type(date_1)
    assert d_fmt.is_native_type(date_2)
    assert d_fmt.is_native_type(date_3)

    # 3. fail the test

# Generated at 2022-06-14 14:27:24.883949
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2000, 1, 1, 10, 15, 20)) == "2000-01-01T10:15:20"




# Generated at 2022-06-14 14:27:36.038250
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dtf = DateTimeFormat()

# Generated at 2022-06-14 14:27:39.467319
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    date_time = datetime.time(9, 22, 45, 9)
    format_instance = TimeFormat()
    actual_result = format_instance.serialize(date_time)
    expected_result = "09:22:45.000009"
    assert actual_result == expected_result

# Generated at 2022-06-14 14:27:42.495552
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    value = "2018-12-31T00:00:00+00:00"
    format = DateTimeFormat()
    assert format.validate(value) == datetime.datetime(2018, 12, 31, 0, 0, 0, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:27:50.080069
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    tf = TimeFormat()

    assert tf.serialize(datetime.datetime(2018, 8, 15, 11, 11, 0, 0)) == '11:11:00'
    assert tf.serialize(datetime.datetime(2018, 8, 15, 11, 11, 30, 0)) == '11:11:30'
    assert tf.serialize(datetime.datetime(2018, 8, 15, 11, 11, 30, 456)) == '11:11:30.000456'
    assert tf.serialize(datetime.datetime(2018, 8, 15, 11, 11, 0, 456)) == '11:11:00.000456'
    assert tf.serialize(datetime.datetime(2018, 8, 15, 11, 11, 0)) == '11:11:00'
    assert tf.serialize

# Generated at 2022-06-14 14:27:52.264249
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert TimeFormat().serialize('07:21:43') == '07:21:43'


# Generated at 2022-06-14 14:27:54.515408
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert TimeFormat().serialize(datetime.time(hour=5, minute=1)) == "05:01:00"

# Generated at 2022-06-14 14:28:04.174869
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Test for ValueError
    try:
        datetimeformat = DateTimeFormat()
        datetimeforma.validate("00-03-18 10:00:00+00:00")
    except ValidationError as e:
        assert e.code == "invalid"
    # Test for returning correct date time format
    datetimeformat = DateTimeFormat()
    assert datetimeformat.validate("2020-03-18T10:00:00+00:00") == datetime.datetime(2020, 3, 18, 10, 0, 0, tzinfo=datetime.timezone.utc)
    
    
    

# Generated at 2022-06-14 14:28:08.798786
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    obj = datetime.datetime(2020,12,3,3,3,3,3,tzinfo=datetime.timezone.utc)
    #obj = datetime.date(2020,12,3)
    assert(DateTimeFormat().serialize(obj) == "2020-12-03T03:03:03.000003+00:00")

# Generated at 2022-06-14 14:28:13.200727
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    value = "2019-12-13T13:13:13Z"
    format = DateTimeFormat()
    result = format.serialize(value)

    if result != value:
        raise AssertionError("Результат не равен ожидаемому")

# Generated at 2022-06-14 14:28:14.977680
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2015-10-23') == datetime.date(2015, 10, 23)


# Generated at 2022-06-14 14:28:20.969668
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    obj = DateTimeFormat()
    value = '2019-04-09T19:46:23.640704'

    result = obj.validate(value)

    assert result == datetime.datetime(2019, 4, 9, 19, 46, 23, 640704)



# Generated at 2022-06-14 14:28:29.173653
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate("23:59:30") == datetime.time(0, 0, 0)
    assert time.validate("23:59:30.1") == datetime.time(0, 0, 0)
    assert time.validate("23:59:30.1") == datetime.time(0, 0, 0)
    assert time.validate("23:59:30.123") == datetime.time(0, 0, 0)
    assert time.validate("23:59:30.1123") == datetime.time(0, 0, 0)



# Generated at 2022-06-14 14:28:32.911433
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time = time_format.validate('09:12:34')
    assert time.hour == 9
    assert time.minute == 12
    assert time.second == 34

# Generated at 2022-06-14 14:28:38.103383
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Setup
    time_format = TimeFormat()

    # Exercise
    actual_time_result = time_format.validate("20:07:00")

    # Verify
    actual_time = datetime.time(20, 7, 0)
    assert actual_time_result == actual_time



# Generated at 2022-06-14 14:28:43.047287
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    if((datetime.datetime.now().isoformat())[-6:] == "+00:00"):
        assert(DateTimeFormat().serialize(datetime.datetime.now()).endswith("Z"))
    else:
        assert(not DateTimeFormat().serialize(datetime.datetime.now()).endswith("Z"))


# Generated at 2022-06-14 14:28:47.802659
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    #test = time_format.validate("18:00:00")
    #test = time_format.validate("23:00:00")
    test = time_format.validate("25:00:00")



# Generated at 2022-06-14 14:28:57.930548
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    fmt = TimeFormat()
    assert fmt.validate("00:00:00") == datetime.time(0, 0, 0)
    assert fmt.validate("00:00:00.000000") == datetime.time(0, 0, 0)
    assert fmt.validate("00:00:00.000001") == datetime.time(0, 0, 0, 1)
    assert fmt.validate("00:00:00.937309") == datetime.time(0, 0, 0, 937309)

# Generated at 2022-06-14 14:28:59.157722
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("15:00") == datetime.time(hour=15, minute=0)



# Generated at 2022-06-14 14:29:06.884269
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Simple test case
    time_format = TimeFormat()
    time_str = "19:30:59"
    time_obj = datetime.time(hour=19, minute=30, second=59)
    assert time_format.validate(time_str) == time_obj

    # Now let's try some negative cases
    # 1. invalid time
    with pytest.raises(ValidationError):
        time_format.validate("19:31:30")

    # 2. invalid format
    with pytest.raises(ValidationError):
        time_format.validate("19:30:30.12345")

# Generated at 2022-06-14 14:29:11.838041
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    #test nonetype
    s=DateTimeFormat()
    assert s.serialize(None) is None
    #test
    test_obj=datetime.datetime(2020, 2, 12, 1, 57, 52, 159499)
    assert s.serialize(test_obj)=='2020-02-12T01:57:52.159499'


# Generated at 2022-06-14 14:29:21.782205
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert tf.validate("12:30:15.123123") == datetime.time(12,30,15,123123)
    assert tf.validate("12:30:15.123") == datetime.time(12,30,15,123000)
    assert tf.validate("12:30:15") == datetime.time(12,30,15)
    assert tf.validate("12:30") == datetime.time(12,30)
    assert tf.validate("12:30:15.12") == datetime.time(12,30,15,120000)
    assert tf.validate("12:30:15.00") == datetime.time(12,30,15,000000)


# Generated at 2022-06-14 14:29:30.676091
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    f = DateTimeFormat()
    s = f.serialize(datetime.datetime(2019, 2, 16, 15, 34, 59))
    assert s == "2019-02-16T15:34:59"
    s = f.serialize(datetime.datetime(2019, 2, 16, 15, 34, 59, tzinfo=datetime.timezone.utc))
    assert s == "2019-02-16T15:34:59Z"
    s = f.serialize(datetime.datetime(2019, 2, 16, 15, 34, 59, tzinfo=datetime.timezone(datetime.timedelta(hours=3))))
    assert s == "2019-02-16T15:34:59+03:00"

# Generated at 2022-06-14 14:29:33.662997
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-05-15T14:14:10")



# Generated at 2022-06-14 14:29:37.617141
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    assert date_time_format.serialize(datetime.datetime(2018, 3, 18, 6, 16, 3)) == '2018-03-18T06:16:03'

# Generated at 2022-06-14 14:29:40.189603
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date = datetime.datetime(2015, 12, 31, 23, 59, 59, 123456)
    assert DateTimeFormat().serialize(date) == '2015-12-31T23:59:59.123456'

# Generated at 2022-06-14 14:29:46.808249
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(None) is None

    obj = datetime.datetime(2018, 5, 22, 11, 45, 55, tzinfo=datetime.timezone.utc)

    value = DateTimeFormat().serialize(obj)
    assert value == "2018-05-22T11:45:55+00:00"

    obj = datetime.datetime(2018, 5, 22, 11, 45, 55, tzinfo=datetime.timezone(datetime.timedelta(hours=5)))

    value = DateTimeFormat().serialize(obj)
    assert value == "2018-05-22T11:45:55+05:00"

# Generated at 2022-06-14 14:29:51.816356
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # Arrange
    dtformat = DateTimeFormat()
    sample = datetime.datetime.fromisoformat("2019-12-25T17:06:20")
    expected = "2019-12-25T17:06:20"

    # Act
    actual = dtformat.serialize(obj=sample)

    # Assert
    assert expected == actual

# Generated at 2022-06-14 14:29:56.811105
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # test for valid date format
    value = '2020-04-27'
    obj = DateFormat()
    assert obj.validate(value) == datetime.date(2020, 4, 27)
    # test for invalid date format
    value = '2020/04/27'
    with pytest.raises(ValidationError):
        obj = DateFormat()
        obj.validate(value)


# Generated at 2022-06-14 14:29:58.686803
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dtf = DateTimeFormat()
    return dtf.serialize(datetime.datetime.now())

# Generated at 2022-06-14 14:30:12.001455
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    d1 = datetime.datetime(2000, 1, 1, 23, 1, 34)
    d2 = datetime.datetime(2000, 1, 1, 23, 1, 34, 0, tzinfo=datetime.timezone.utc)
    d3 = datetime.datetime(2000, 1, 1, 23, 1, 34, 0, tzinfo=datetime.timezone(datetime.timedelta(0)))
    d4 = datetime.datetime(2000, 1, 1, 23, 1, 34, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-5, minutes=-30)))

    format = DateTimeFormat()
    assert format.serialize(d1) == '2000-01-01T23:01:34'

# Generated at 2022-06-14 14:30:21.681055
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    df = DateTimeFormat()
    assert df.validate("2019-01-01T00:00:00Z") == datetime.datetime(2019, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
    assert df.validate("2019-01-01T17:00:00+09:00") == datetime.datetime(2019, 1, 1, 17, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
    assert df.validate("2019-01-01T15:00:00-07:00") == datetime.datetime(2019, 1, 1, 15, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-7)))


# Generated at 2022-06-14 14:30:32.318670
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime(2017, 12, 11, 0, 0, 1, 0, datetime.timezone.utc)
    assert DateTimeFormat().serialize(obj) == "2017-12-11T00:00:01Z"

    obj = datetime.datetime(2017, 12, 11, 0, 0, 1, 0, datetime.timezone(datetime.timedelta(hours=3)))
    assert DateTimeFormat().serialize(obj) == "2017-12-11T00:00:01+03:00"

    obj = datetime.datetime(2017, 12, 11, 0, 0, 1, 0, datetime.timezone(datetime.timedelta(hours=-3)))

# Generated at 2022-06-14 14:30:36.864445
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeformat=TimeFormat()
    timeformat.validate("12:12")
    timeformat.validate("12:12:12")
    timeformat.validate("12:12:12.999999")


# Generated at 2022-06-14 14:30:41.743416
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    test_serialize = DateTimeFormat()
    date_time = datetime.datetime(year=2020, month=1, day=1, hour=12, 
                                  minute=0, second=0, microsecond=0)
    assert test_serialize.serialize(date_time) == "2020-01-01T12:00:00"


# Generated at 2022-06-14 14:30:51.132111
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Valid data
    t = datetime.time(microsecond=123456)
    str_t = t.isoformat()
    print("Valid data: " + str_t)

    # Convert to datetime.time
    tf = TimeFormat()
    dt_t = tf.validate(str_t)
    str_t = dt_t.isoformat()
    print("Converted time: " + str_t)
    assert("23:59:59.123456" == str_t)

    # Invalid data
    str_t = "ab:cd:ef"
    print("Invalid data: " + str_t)

    # Convert to datetime.time

# Generated at 2022-06-14 14:30:53.573547
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime.utcnow()
    dt_format = DateTimeFormat()
    assert dt_format.serialize(dt) == dt.isoformat() + 'Z'


# Generated at 2022-06-14 14:31:00.926203
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    obj = DateFormat()
    input = '2020-03-08'
    output = obj.validate(input)
    expected = datetime.date(2020, 3, 8)
    assert output == expected


# Generated at 2022-06-14 14:31:05.209486
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    import datetime
    my_date_time = datetime.datetime(2020, 2, 15, 13, 30, 0, 0)
    str_date_time = '2020-02-15T13:30:00'
    assert DateTimeFormat().serialize(my_date_time) == str_date_time

# Generated at 2022-06-14 14:31:13.142217
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2017, 6, 1, 11, 46, 29, 0)) == "2017-06-01T11:46:29"
    assert DateTimeFormat().serialize(datetime.datetime(2017, 6, 1, 11, 46, 29, 12)) == "2017-06-01T11:46:29.000012"
    assert DateTimeFormat().serialize(datetime.datetime(2017, 6, 1, 11, 46, 29, 123456)) == "2017-06-01T11:46:29.123456"
    assert DateTimeFormat().serialize(datetime.datetime(2017, 6, 1, 11, 46, 29, 123456, datetime.timezone.utc)) == "2017-06-01T11:46:29.123456Z"

# Generated at 2022-06-14 14:31:20.029671
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    a = datetime.datetime(2018, 1, 1, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)
    assert a.isoformat() == '2018-01-01T00:00:00+00:00'
    assert DateTimeFormat().serialize(a) == '2018-01-01T00:00:00Z'

    b = datetime.datetime(2018, 1, 1, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=1)))
    assert b.isoformat() == '2018-01-01T00:00:00+01:00'
    assert DateTimeFormat().serialize(b) == '2018-01-01T00:00:00+01:00'


# Generated at 2022-06-14 14:31:29.639977
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    a = DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 12, 0, 0, 0))
    assert str(a) == "2020-01-01T12:00:00", "Expected: '2020-01-01T12:00:00' Got: '" + str(a) + "'"
    b = DateTimeFormat().serialize(datetime.datetime(2020, 12, 31, 23, 59, 59, 999999))
    assert str(b) == "2020-12-31T23:59:59.999999", "Expected: '2020-12-31T23:59:59.999999' Got: '" + str(b) + "'"

# Generated at 2022-06-14 14:31:32.565896
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    validator = DateFormat()
    date = validator.validate("2020-11-03")
    assert date == datetime.date(2020, 11, 3)


# Generated at 2022-06-14 14:31:36.162113
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    type = DateTimeFormat()
    assert type.validate("2019-04-12T06:00:00Z"), datetime.datetime(2019, 4, 12, 6, 0, 0, 0, datetime.timezone.utc)

# Generated at 2022-06-14 14:31:42.522389
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    input_patterns = ["12:34", "12:34:56", "12:34:56.0000001", "12:34:56.9999999"]
    expected_format = ["12:34", "12:34:56", "12:34:56.000001", "12:34:56.999999"]
    for i in range(0, len(input_patterns)):
        output = time_format.validate(input_patterns[i])
        assert str(output) == expected_format[i]



# Generated at 2022-06-14 14:31:48.832518
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime(2020, 6, 18, hour=10, minute=11, second=12)
    dtf = DateTimeFormat()
    value = dtf.serialize(obj)
    assert value == "2020-06-18T10:11:12"
    print("test_DateTimeFormat_serialize")


# Generated at 2022-06-14 14:31:51.806769
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    data = datetime.datetime.now()
    obj = DateTimeFormat()
    result = obj.serialize(data)
    assert(isinstance(result, str))


# Generated at 2022-06-14 14:31:58.845166
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dateTimeFormat = DateTimeFormat()
    time = dateTimeFormat.validate("2019-01-12T13:49:23+00:00")
    year = time.year
    tzinfo = time.tzinfo
    assert (year == 2019)
    assert (tzinfo == datetime.timezone.utc)



# Generated at 2022-06-14 14:32:05.927027
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    datetime_obj = datetime.datetime(year  = 2018,
                              month = 12,
                              day   = 12,
                              hour  = 12,
                              minute= 12,
                              second= 12,
                              microsecond=123000,
                              tzinfo=datetime.timezone.utc)
    result = DateTimeFormat().serialize(datetime_obj)
    assert result == '2018-12-12T12:12:12.123000Z'

# Generated at 2022-06-14 14:32:13.663294
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    D = DateFormat()
    assert D.validate("2019-11-30") == datetime.date(2019, 11, 30)

# Generated at 2022-06-14 14:32:23.821947
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    obj = DateTimeFormat()
    value = obj.validate("2019-12-24T11:10:23.678Z")
    assert value.hour == 11
    assert value.minute == 10
    assert value.second == 23
    assert value.microsecond == 678000
    assert value.tzinfo == datetime.timezone.utc
    # 
    value = obj.validate("2019-12-24T11:10:23Z")
    assert value.hour == 11
    assert value.minute == 10
    assert value.second == 23
    assert value.microsecond == 0
    assert value.tzinfo == datetime.timezone.utc
    #
    value = obj.validate("2019-12-24T11:10:23+05:00")
    assert value.hour == 6
    assert value.minute

# Generated at 2022-06-14 14:32:27.750357
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2020, 4, 13, 14, 17, 12, 848597)) == '2020-04-13T14:17:12.848597'



# Generated at 2022-06-14 14:32:31.399284
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-09-06T11:43:40.098Z") == datetime.datetime(2019,9,6,11,43,40,98000)

# Generated at 2022-06-14 14:32:34.508572
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    data = datetime.datetime(2020, 10, 10, 12, 12, 12, 12)
    assert DateTimeFormat().serialize(data) == '2020-10-10T12:12:12.000012'

# Generated at 2022-06-14 14:32:37.064889
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate(datetime.datetime.now().isoformat().split('T')[0]) == datetime.datetime.now().date()


# Generated at 2022-06-14 14:32:39.848544
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime(2020, 10, 15, 13, 10)
    assert DateTimeFormat().serialize(obj) == '2020-10-15T13:10:00'


# Generated at 2022-06-14 14:32:42.946673
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date = date_format.validate("2019-11-11")
    assert date.isoformat() == "2019-11-11"


# Generated at 2022-06-14 14:32:55.900853
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat=DateFormat()
    val1=dateFormat.validate("2020-05-03")
    val2=dateFormat.validate("2000-02-01")
    val3=dateFormat.validate("2020-04-39")
    val4=dateFormat.validate("2000-02-33")
    assert val1==datetime.date(2020,5,3)
    assert val2==datetime.date(2000,2,1)
    assert val3==datetime.date(2020,4,39)
    assert val4==datetime.date(2000,2,33)


# Generated at 2022-06-14 14:33:08.634338
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2019, 8, 8, 9, 30, 30, 30)) == '2019-08-08T09:30:30.000030'
    assert DateTimeFormat().serialize(datetime.datetime(2019, 8, 8, 9, 30)) == '2019-08-08T09:30:00'
    assert DateTimeFormat().serialize(datetime.datetime(2019, 8, 8, 9)) == '2019-08-08T09:00:00'
    assert DateTimeFormat().serialize(datetime.datetime(2019, 8, 8)) == '2019-08-08T00:00:00'
    assert DateTimeFormat().serialize(None) == None

# Generated at 2022-06-14 14:33:14.029367
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    import datetime as dt
    # case when obj is datetime object
    obj = dt.datetime.utcnow()
    format1 = DateTimeFormat()
    assert isinstance(format1.serialize(obj), str)

    # case when obj is None
    assert format1.serialize(None) == None