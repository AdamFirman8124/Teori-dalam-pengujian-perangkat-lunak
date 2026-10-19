

# Generated at 2022-06-14 14:23:31.342552
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime(year=2020, month=2, day=3, hour=22, minute=10, second=0)
    obj1 = datetime.datetime(year=2020, month=2, day=3, hour=10, minute=0, second=0)
    test = DateTimeFormat()
    assert test.serialize(obj) == "2020-02-03T22:10:00"
    obj1.replace(tzinfo=datetime.timezone.utc)
    assert test.serialize(obj1) == "2020-02-03T10:00:00Z"



# Generated at 2022-06-14 14:23:33.659563
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    try:
        DATETIME_REGEX.match("2020-4-26T13:59:00.000003-00:00")
    except ValueError:
        return "Error"

# Generated at 2022-06-14 14:23:36.026671
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    df = DateTimeFormat()
    value = '2002-10-02T15:00:00Z'
    datetime_obj = df.validate(value)
    assert datetime_obj.isoformat() == value

# Generated at 2022-06-14 14:23:48.344764
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    validate = DateTimeFormat().validate

    assert validate("2019-11-03T16:56:10") == datetime.datetime(2019, 11, 3, 16, 56, 10)
    assert validate("2019-11-03T16:56:10+00:00") == datetime.datetime(2019, 11, 3, 16, 56, 10)
    assert validate("2019-11-03T16:56:10+02:00") == datetime.datetime(2019, 11, 3, 16, 56, 10, tzinfo=datetime.timezone(datetime.timedelta(hours=+2)))

# Generated at 2022-06-14 14:23:53.913550
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    date_time_obj = datetime.datetime(2020, 1, 8, 6, 59, 59, 0)
    date_time_str = date_time_format.serialize(date_time_obj)
    assert date_time_str == "2020-01-08T06:59:59"

# Generated at 2022-06-14 14:24:00.389169
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():

    time_format = TimeFormat()

    # test case 1: validate a invalid time
    expect_time = "18:36:00"
    result = time_format.validate(expect_time)
    assert result == datetime.time(18, 36, 0)

    # test case 2: validate a valid time
    expect_time = "18:37:00"
    result = time_format.validate(expect_time)
    assert result == datetime.time(18, 37, 0)

    assert len(time_format.errors) == 2

# Generated at 2022-06-14 14:24:06.318799
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    dateformat = DateFormat()
    # Test the serialize method with the real type of the parameter
    assert dateformat.serialize(datetime.date(2020,6,11)) == "2020-06-11"
    # Test the serialize method with a wrong type of the parameter
    with pytest.raises(AssertionError):
        dateformat.serialize(6)
    # Test the serialize method with a null value
    assert dateformat.serialize(None) == None


# Generated at 2022-06-14 14:24:16.106334
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    the_UUIDFormat = UUIDFormat()

# Generated at 2022-06-14 14:24:23.726979
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    value1 = "2019-11-14"
    value2 = "2009-12-31"
    value3 = "2009-13-31"

    assert date_format.validate(value1) == datetime.date(2019, 11, 14)
    assert date_format.validate(value2) == datetime.date(2009, 12, 31)
    # test for validation error
    try:
        date_format.validate(value3)
    except ValidationError:
        pass


# Generated at 2022-06-14 14:24:27.616423
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2019-10-01") == datetime.date(2019, 10, 1)
    assert DateFormat().validate("2019-10-31") == datetime.date(2019, 10, 31)


# Generated at 2022-06-14 14:24:35.544366
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert TimeFormat().serialize(datetime.time.min) == "00:00:00"


# Generated at 2022-06-14 14:24:39.583409
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtf = DateTimeFormat()
    assert dtf.validate('2019-09-24T04:18:48+00:00') == datetime.datetime(2019, 9, 24, 4, 18, 48)
    assert dtf.validate('2019-09-24T04:18:48.000Z') == datetime.datetime(2019, 9, 24, 4, 18, 48)

# Generated at 2022-06-14 14:24:43.557708
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    """Test method validate of class UUIDFormat."""

    fmt = UUIDFormat()
    assert fmt.validate("b7e06b0f-f9f9-11e8-b602-186590de3900")


# Generated at 2022-06-14 14:24:50.209290
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    testFormat = DateTimeFormat()
    assert str(testFormat.validate('2019-06-19T08:51:33+11:00')) == '2019-06-19 08:51:33+11:00'
    assert str(testFormat.validate('2019-06-19T08:51:33-11:00')) == '2019-06-19 08:51:33-11:00'
    assert str(testFormat.validate('2019-06-19T08:51:33')) == '2019-06-19 08:51:33+00:00'

# Generated at 2022-06-14 14:24:54.441318
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    test_validate_string = "062d8b61-50c7-49b1-9ad7-915819f0065a"
    uuidFormat = UUIDFormat()
    print(uuidFormat.validate(test_validate_string))


# Generated at 2022-06-14 14:24:57.908839
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert TimeFormat().serialize(None) == None
    assert TimeFormat().serialize(datetime.time(10, 10, 10, 100000)) == "10:10:10.100000"

# Generated at 2022-06-14 14:25:06.242176
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    print("\n === Unit test for method validate of class DateTimeFormat === \n")
    dtf = DateTimeFormat()
    cur_datetime = datetime.datetime.now()
    print("Current date time: ", cur_datetime)
    str_datetime = cur_datetime.strftime(r"%Y-%m-%dT%H:%M:%S%z")
    print("Current date time convert to string: ", str_datetime)
    dtf_validate = dtf.validate(str_datetime)
    print("Validate current date time string: ", dtf_validate)



# Generated at 2022-06-14 14:25:11.813772
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    input_data = "2019-08-01T16:47:58.548034Z"
    actual_output = DateTimeFormat().validate(input_data)
    actual_output = actual_output.isoformat()
    expected_output = "2019-08-01T16:47:58.548034+00:00"
    assert actual_output == expected_output

# Generated at 2022-06-14 14:25:22.974318
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():

    # Test with invalid values
    assert(DateTimeFormat().validate("hello") == ValidationError(text="Must be a valid datetime format.", code="format"))

    # Test with value with string tzinfo
    assert(DateTimeFormat().validate("2020-06-22T16:00:11.123456Z") == datetime.datetime(2020, 6, 22, 16, 0, 11, microsecond=123456, tzinfo=datetime.timezone.utc))

    # Test with value with tzinfo

# Generated at 2022-06-14 14:25:24.966064
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    timeformat = TimeFormat()
    timeformat.validate("11:45")
    timeformat.serialize("11:45")



# Generated at 2022-06-14 14:25:35.950213
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    def t(value, expected):
        actual = DateTimeFormat().serialize(datetime.datetime.fromisoformat(value))
        assert actual == expected

    t("2020-05-18T10:45:39", "2020-05-18T10:45:39Z")
    t("2020-05-18T10:45:39+00:00", "2020-05-18T10:45:39Z")
    t("2020-05-18T10:45:39-07:00", "2020-05-18T10:45:39-07:00")
    t("2020-05-18T10:45:39+12:00", "2020-05-18T10:45:39+12:00")

# Generated at 2022-06-14 14:25:39.671050
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    with pytest.raises(Exception):
        tf.validate("02:12:43.999999")
    assert tf.validate("02:12:43.999999") is None

# Generated at 2022-06-14 14:25:46.600036
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    obj = datetime.time(20, 12, 14)
    t = TimeFormat()
    assert t.serialize(obj) == '20:12:14'

    obj = datetime.time(20, 12, 14, 1000)
    t = TimeFormat()
    assert t.serialize(obj) == '20:12:14.001000'

    obj = None
    t = TimeFormat()
    assert t.serialize(obj) == None

# Generated at 2022-06-14 14:25:53.290806
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert tf.validate("15:31:00") == datetime.time(15, 31)
    assert tf.validate("15:31:00.123") == datetime.time(15, 31, 0, 123000)
    assert tf.validate("15:31:00.123456") == datetime.time(15, 31, 0, 123456)


# Generated at 2022-06-14 14:25:59.548718
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # test1
    time_format = TimeFormat()
    assert time_format.validate('14:30') == datetime.time(14, 30)

    # test2
    assert time_format.validate('14:30:59') == datetime.time(14, 30, 59)

    # test3
    assert time_format.validate('14:30:59.123456') == datetime.time(14, 30, 59, 123456)



# Generated at 2022-06-14 14:26:05.723008
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()

    for time_str in [
        "00:00:00.000000",
        "23:59:59.123456",
        "12:34:56.456789",
        "12:34",
        "03:43:49",
    ]:
        assert time_format.validate(time_str) == datetime.time.fromisoformat(time_str)

    try:
        time_format.validate("24:00:00.000000")
    except ValidationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:26:16.783117
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from datetime import datetime, timezone
    def func_test_0():
        assert DateTimeFormat().serialize(None) is None
    def func_test_1():
        assert DateTimeFormat().serialize(datetime(2020,1,1,1,1,1,1,timezone.utc)) == "2020-01-01T01:01:01.00000" + "1Z"
    def func_test_2():
        assert DateTimeFormat().serialize(datetime(2020,1,1,1,1,1,1,timezone(datetime.timedelta(hours=-1)))) == "2020-01-01T01:01:01.00000" + "1-01:00"

# Generated at 2022-06-14 14:26:20.843907
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(13, 24, 58, 566193)
    tf = TimeFormat()
    assert tf.serialize(time) == "13:24:58.566193"


# Generated at 2022-06-14 14:26:26.920720
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(11, 59, 59)
    fmt = TimeFormat()
    assert fmt.serialize(time) == '11:59:59'
    time = datetime.time(11, 59)
    assert fmt.serialize(time) == '11:59:00'
    time = datetime.time(11)
    assert fmt.serialize(time) == '11:00:00'


# Generated at 2022-06-14 14:26:33.901129
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("17:00") == datetime.time(17)
    assert TimeFormat().validate("17:00:30") == datetime.time(17, 0, 30)
    assert TimeFormat().validate("17:00:30.500") == datetime.time(17, 0, 30, 500000)

# Generated at 2022-06-14 14:26:46.857175
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
	time1 = TimeFormat()
	time2 = TimeFormat()
	time3 = TimeFormat()
	time4 = TimeFormat()
	time5 = TimeFormat()
	time6 = TimeFormat()
	time7 = TimeFormat()
	time8 = TimeFormat()
	time9 = TimeFormat()
	time10 = TimeFormat()

	try:
		time1.validate("2020-04-30T17:24:00Z")
		assert False
	except:
		assert True
	try:
		time2.validate("04:30:00.1248")
		assert False
	except:
		assert True
	try:
		time3.validate("12:02:55.10")
		assert True
	except:
		assert False

# Generated at 2022-06-14 14:26:50.414223
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = DateTimeFormat()
    assert dt.serialize(datetime.datetime(2019, 8, 31, 15, 0)) == "2019-08-31T15:00:00"

# Generated at 2022-06-14 14:26:52.652156
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-12-26T22:34:05.015+02:00") == datetime.datetime(2019, 12, 26, 22, 34, 5, 150000, 
                                                                                              tzinfo=datetime.timezone(datetime.timedelta(hours=2)))

# Generated at 2022-06-14 14:26:54.745930
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(11, 59, 33, 20)
    result = TimeFormat().serialize(time)
    assert result == '11:59:33.000020'


# Generated at 2022-06-14 14:27:03.435673
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    obj = datetime.datetime(2020, 2, 22, 2, 20, 2, 2000)
    timeformat = TimeFormat()
    result = timeformat.serialize(obj)
    assert result == '02:20:02.002000'
    obj = datetime.datetime(2020, 2, 22, 2, 20, 2, 20000)
    timeformat = TimeFormat()
    result = timeformat.serialize(obj)
    assert result == '02:20:02.020000'
    obj = datetime.datetime(2020, 2, 22, 2, 20, 2, 200000)
    timeformat = TimeFormat()
    result = timeformat.serialize(obj)
    assert result == '02:20:02.200000'

# Generated at 2022-06-14 14:27:11.504321
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    test_obj = datetime.datetime(2021, 4, 16, 4, 9, 23, tzinfo=datetime.timezone(datetime.timedelta(hours=-4)))
    assert DateTimeFormat().serialize(test_obj) == '2021-04-16T04:09:23-04:00'
    test_obj = datetime.datetime(2021, 4, 16, 4, 9, 23)
    assert DateTimeFormat().serialize(test_obj) == '2021-04-16T04:09:23'

# Generated at 2022-06-14 14:27:15.917970
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    timeformat = TimeFormat()
    assert timeformat.serialize(datetime.time(hour=1, minute=2, second=3, microsecond=444444)) == '01:02:03.444444'


# Generated at 2022-06-14 14:27:18.753004
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
	result = TimeFormat().serialize(datetime.time(hour=19, minute=35, second=10))
	assert result == '19:35:10', "Wrong result for TimeFormat().serialize"


# Generated at 2022-06-14 14:27:24.330654
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time_format = TimeFormat()
    result = time_format.serialize("12:30:30")
    assert result == "12:30:30", "Testing if the serialize function of TimeFormat returns the time with seconds."
    result = time_format.serialize("12:30:30.123546")
    assert result == "12:30:30.123546", "Testing if the serialize function of TimeFormat returns the time with microseconds."
    result = time_format.serialize("12:30")
    assert result == "12:30:00", "Testing if the serialize function of TimeFormat returns the time with seconds."


# Generated at 2022-06-14 14:27:31.315798
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    from test_data.datetime_test_data import datetime_test_data_list
    dtf = DateTimeFormat()
    for test_data in datetime_test_data_list:
        assert dtf.validate(test_data["str"]) == datetime.datetime.strptime(test_data["str"], "%Y-%m-%dT%H:%M:%S.%f%z")


# Generated at 2022-06-14 14:27:35.898114
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2019, 1, 1)) == '2019-01-01T00:00:00'


# Generated at 2022-06-14 14:27:39.963738
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert str(df.validate("2020-09-01")) == "2020-09-01"
    with pytest.raises(ValidationError):
        df.validate("202009-01")
    with pytest.raises(ValidationError):
        df.validate("2020-09-32")


# Generated at 2022-06-14 14:27:48.881994
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():

    valid_values = [
        "2020-01-01",
        "2020-01-01T00:00:00",
        "2020-01-01T00:00:00+01:00",
        "2019-12-31T23:00:00Z",
        "2019-12-31T23:00:00-01:00",
    ]
    invalid_values = [
        "2019-12-0",
        "2020-01-01T00:00:00Zr",
        "2019-12-31T23:00:00+01",
        "2019-12-31T23:00:00+01:0",
        "2019-12-31T23:00:00-01x00",
        "2019-12-31T23:00:00-01:00:00",
    ]

# Generated at 2022-06-14 14:28:00.419993
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Check validation of date
    date = "2011-12-18"
    date_format = DateFormat()
    assert date_format.validate(date) == datetime.date(2011, 12, 18)

    # Check validation of time
    time = "12:18:00"
    time_format = TimeFormat()
    assert time_format.validate(time) == datetime.time(12, 18, 0)

    # Check validation of datetime
    dt = "2011-12-18 10:18:00"
    datetime_format = DateTimeFormat()
    assert datetime_format.validate(dt) == datetime.datetime(2011, 12, 18, 10, 18, 0)

    # Check validation of UUID

# Generated at 2022-06-14 14:28:08.844264
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    assert date.validate('2018-01-01') == datetime.date(2018,1,1)
    assert date.validate('2019-12-25') == datetime.date(2019,12,25)
    with pytest.raises(AssertionError):
        assert date.validate('2019-13-25')
    with pytest.raises(AssertionError):
        assert date.validate('2019-12-32')


# Generated at 2022-06-14 14:28:11.557370
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2018-10-01') == datetime.date(2018, 10, 1)
    assert DateFormat().validate('2018-10-12') != datetime.date(2018, 10, 23)


# Generated at 2022-06-14 14:28:18.813389
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time = datetime.datetime(2020, 4, 22, 17, 18, 19)
    date_time_format = DateTimeFormat()
    assert date_time_format.serialize(date_time) == '2020-04-22T17:18:19'

    date_time = datetime.datetime(2020, 4, 22, 17, 18, 19, tzinfo=datetime.timezone.utc)
    date_time_format = DateTimeFormat()
    assert date_time_format.serialize(date_time) == '2020-04-22T17:18:19Z'

    date_time = datetime.datetime(2020, 4, 22, 17, 18, 19, tzinfo=datetime.timezone(datetime.timedelta(hours=-8)))
    date_time_format = Date

# Generated at 2022-06-14 14:28:21.953914
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    input = '2020-03-03'
    res = df.validate(input)
    assert isinstance(res, datetime.date)


# Generated at 2022-06-14 14:28:23.233789
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    DATE_FORMAT = DateFormat()  # type: ignore
    with pytest.raises(ValidationError):
        DATE_FORMAT.validate(1234)


# Generated at 2022-06-14 14:28:26.955152
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    fmt = DateTimeFormat()
    assert fmt.serialize(datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)) == "2017-04-12T17:53:53.983690Z"

# Generated at 2022-06-14 14:28:32.468583
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(22,12,2019,15,50,30)) == '2019-12-22T15:50:30'

# Generated at 2022-06-14 14:28:36.575132
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()

    assert date.is_native_type(datetime.date(2016, 3, 14))
    print("Test is_native_type of class DateFormat")
    print(date.validate('2016-03-14'))
    print("Test validate of class DateFormat")



# Generated at 2022-06-14 14:28:41.703250
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():

    dtf = DateTimeFormat()

    assert dtf.serialize(None) == None
    assert dtf.serialize(datetime.datetime.fromisoformat('2020-01-01 14:30:00+00:00')) == '2020-01-01T14:30:00+00:00'


# Unit tests for method serialize of class DateFormat

# Generated at 2022-06-14 14:28:46.748923
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    datetime_test = datetime.datetime(2020, 4, 10, 20, 16, 12, 184901)
    datetime_test_ = DateTimeFormat().serialize(datetime_test)
    assert datetime_test_ == '2020-04-10T20:16:12.184901'

# Generated at 2022-06-14 14:28:51.799182
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime(2020, 1, 1, 15, 30, 0, 0, tzinfo=datetime.timezone.utc)
    result = DateTimeFormat().serialize(obj)
    assert result == "2020-01-01T15:30:00Z", f"result={result}"

# Generated at 2022-06-14 14:28:55.923595
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dateTime = "2018-01-02T03:04:05+00:00"
    dateTime = DateTimeFormat.validate(dateTime)
    assert dateTime.year == 2018
    assert dateTime.month == 1
    assert dateTime.day == 2



# Generated at 2022-06-14 14:29:01.773906
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from typesystem.datetime import DateTimeFormat
    import datetime
    dt = datetime.datetime.now()
    dtz = dt.astimezone()
    assert DateTimeFormat().serialize(dt) == dt.isoformat()
    assert DateTimeFormat().serialize(dtz) == dtz.isoformat()

# Generated at 2022-06-14 14:29:09.988848
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dtf = DateTimeFormat()
    assert dtf.serialize(None) == None
    datetime = dtf.validate('2012-12-21T00:40:00Z')
    assert dtf.serialize(datetime) == '2012-12-21T00:40:00Z'
    datetime = dtf.validate('2012-12-21 00:40:20.123456')
    assert dtf.serialize(datetime) == '2012-12-21T00:40:20.123456'
    datetime = dtf.validate('2012-12-21 00:40:20.123456+02:00')
    assert dtf.serialize(datetime) == '2012-12-21T00:40:20.123456+02:00'

# Generated at 2022-06-14 14:29:14.385632
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate("13:01") == datetime.time(hour=13, minute=1)
    assert time.validate("13:01:01") == datetime.time(hour=13, minute=1, second=1)
    assert time.validate("13:01:01.02") == datetime.time(hour=13, minute=1, second=1, microsecond=20000)
    assert time.validate("13:01:01.123") == datetime.time(hour=13, minute=1, second=1, microsecond=123000)


# Generated at 2022-06-14 14:29:24.468022
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    assert date_time_format.serialize(datetime.datetime(2020,1,1,0,0)) == "2020-01-01T00:00:00"
    assert date_time_format.serialize(datetime.datetime(2020,1,1,0,0,30)) == "2020-01-01T00:00:30"
    assert date_time_format.serialize(datetime.datetime(2020,1,1,0,0,30,32)) == "2020-01-01T00:00:30.000032"

# Generated at 2022-06-14 14:29:34.593373
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    # test_datetime_01
    date_format = "2019-08-01"
    date_validation = date.validate(date_format)
    assert date_validation == datetime.date(2019, 8, 1)
    # test_datetime_02
    date_format = "2020-02-27"
    date_validation = date.validate(date_format)
    assert date_validation == datetime.date(2020, 2, 27)
    # test_datetime_03
    date_format = "2020-02-02"
    date_validation = date.validate(date_format)
    assert date_validation == datetime.date(2020, 2, 2)
    # test_datetime_04

# Generated at 2022-06-14 14:29:41.639112
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    fmt = DateTimeFormat()

    for value in [
        "2019-01-01T00:00:00Z",
        "2019-01-01T00:00:00+01:00",
        "2019-01-01T00:00:00-00:30",
    ]:
        result = fmt.validate(value)
        assert isinstance(result, datetime.datetime)
        assert result.tzinfo is not None  # type: ignore

    try:
        fmt.validate("2019-01-01T00:00:00+00:71")
    except ValidationError:
        pass
    else:
        assert False

# Generated at 2022-06-14 14:29:47.913770
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test error when value does not match format
    date_format = DateFormat()
    with pytest.raises(ValidationError) as e:
        date_format.validate("09-2-1999")
    assert str(e.value) == "Must be a valid date format."

    # Test invalid value raise ValueError exception
    with pytest.raises(ValidationError) as e:
        date_format.validate("1999-03-32")
    assert str(e.value) == "Must be a real date."

    # Test valid value return right type of datetime
    assert type(date_format.validate("1999-03-09")) == datetime.date


# Generated at 2022-06-14 14:29:51.804748
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.is_native_type("2019-04-11") == False
    date = df.validate("2019-04-11")
    assert date == datetime.date(2019, 4, 11)


# Generated at 2022-06-14 14:29:59.482842
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_value = DateFormat()
    test_value = date_value.validate("1585-05-21")
    assert test_value == "1585-05-21"
    test_value = date_value.validate("1585-21-05")
    assert test_value == "1585-21-05"
    test_value = date_value.validate("1585-05-05")
    assert test_value == "1585-05-05"
    test_value = date_value.validate("1585-05-05")
    assert test_value == "1585-05-05"
    test_value = date_value.validate("1585/05/05")
    assert test_value == "1585/05/05"

# Generated at 2022-06-14 14:30:11.113101
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate("02:45") == time_format.validate("02:45:00")
    assert time_format.validate("02:45:00") == time_format.validate("02:45:00.00")
    assert time_format.validate("02:45") == time_format.validate("02:45:00.00")
    assert time_format.validate("02:45:00.00") == time_format.validate("02:45:00.000000")
    try:
        time_format.validate("02:45:00.1")
    except ValidationError:
        return
    assert False

# Generated at 2022-06-14 14:30:19.811323
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Case 1
    assert DateTimeFormat().validate('2018-12-05T20:11:52.468100Z') == datetime.datetime(2018,12,5,20,11,52,468100, tzinfo=datetime.timezone.utc)

    # Case 2
    assert DateTimeFormat().validate('2018-12-05T20:11:52.468100-01:00') == datetime.datetime(2018,12,5,20,11,52,468100, tzinfo=datetime.timezone(datetime.timedelta(hours=-1)))

    # Case 3

# Generated at 2022-06-14 14:30:30.891842
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate("12:30:00") == datetime.time(12, 30)
    assert time.validate("12:30:00.00") == datetime.time(12, 30)
    assert time.validate("12:30:00.000000") == datetime.time(12, 30)
    assert time.validate("12:30:00.000099") == datetime.time(12, 30, tzinfo=None, microsecond=99)
    assert time.validate("12:30:00.999999") == datetime.time(12, 30, tzinfo=None, microsecond=999999)
    assert time.validate("23:59:00.000000") == datetime.time(23, 59)
    assert time.validate("2:00") == dat

# Generated at 2022-06-14 14:30:36.493812
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    fmt = TimeFormat()

    # Test 00:00:00
    value = "00:00:00"
    t = fmt.validate(value)
    assert isinstance(t, datetime.time)
    assert t.hour == 0
    assert t.minute == 0
    assert t.second == 0
    assert t.microsecond == 0

    # Test 12:00:00
    value = "12:00:00"
    t = fmt.validate(value)
    assert isinstance(t, datetime.time)
    assert t.hour == 12
    assert t.minute == 0
    assert t.second == 0
    assert t.microsecond == 0

    # Test 23:59
    value = "23:59"
    t = fmt.validate(value)

# Generated at 2022-06-14 14:30:44.358845
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    val = time_format.validate('14:25')
    assert val == datetime.time(14, 25)
    val = time_format.validate('14:25:30')
    assert val == datetime.time(14, 25, 30)
    val = time_format.validate('14:25:30.123456')
    assert val == datetime.time(14, 25, 30, 123456)
    val = time_format.validate('14:25:30.123456789')
    assert val == datetime.time(14, 25, 30, 123456)


# Generated at 2022-06-14 14:30:52.812287
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t=TimeFormat()
    value="20:30"
    result=t.validate(value)
    expected_result=datetime.time(20,30)
    assert result==expected_result
    # test for exception
    try:
        value="30:30"
        t.validate(value)
    except ValidationError:
        assert 1
    try:
        value="25:30"
        t.validate(value)
    except ValidationError:
        assert 1

# Generated at 2022-06-14 14:30:58.935043
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("15:02:00") == datetime.time(15, 2)
    assert TimeFormat().validate("15:02:00.123456") == datetime.time(15, 2, 0, 123456)
    assert TimeFormat().validate("15:02:00.1234") == datetime.time(15, 2, 0, 123400)


# Generated at 2022-06-14 14:31:08.582631
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeformat = TimeFormat()

    assert timeformat.validate("23:59:59.999999") == datetime.time(23, 59, 59, 999999)
    assert timeformat.validate("23:59:59") == datetime.time(23, 59, 59)
    assert timeformat.validate("23:59") == datetime.time(23, 59)
    assert timeformat.validate("23") == datetime.time(23)

    with pytest.raises(ValidationError):
        timeformat.validate("24:00")

    with pytest.raises(ValidationError):
        timeformat.validate("23:60")

    with pytest.raises(ValidationError):
        timeformat.validate("23:59:60")


# Generated at 2022-06-14 14:31:17.745383
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate("09:30") == datetime.time(9, 30)
    assert time.validate("09:30:30") == datetime.time(9, 30, 30)
    assert time.validate("09:30:30.000030") == datetime.time(9, 30, 30, 30)
    assert time.validate("09:30:30.000030Z") == datetime.time(9, 30, 30, 30, tzinfo=datetime.timezone.utc)
    with pytest.raises(ValidationError):
        time.validate("09:30:30.")
    with pytest.raises(ValidationError):
        time.validate("09:30:30.Z")

# Generated at 2022-06-14 14:31:19.123492
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    t = DateTimeFormat()


# Generated at 2022-06-14 14:31:21.554471
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    obj = DateFormat()
    value = datetime.date(2020, 5, 1)
    assert obj.validate(value) == value



# Generated at 2022-06-14 14:31:23.904830
# Unit test for method validate of class DateFormat

# Generated at 2022-06-14 14:31:31.958426
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date = DateTimeFormat()
    with pytest.raises(ValidationError) as ve:
        date.validate("2017-13-43")
    assert ve.value.code == "invalid"

    with pytest.raises(ValidationError) as ve:
        date.validate("2017-11-43T21:43:43.000Z")
    assert ve.value.code == "invalid"
    
    with pytest.raises(ValidationError) as ve:
        date.validate("2017-11-43T21:43:43.Z")
    assert ve.value.code == "format"

    with pytest.raises(ValidationError) as ve:
        date.validate("2017-11-43T21:43:43.1234567Z")
    assert ve.value.code

# Generated at 2022-06-14 14:31:35.759449
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_str = "23:59:59"
    time = time_format.validate(time_str)
    assert time.hour==23 and time.minute==59 and time.second==59

# Generated at 2022-06-14 14:31:40.965451
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date = date_format.validate('2019-10-01')
    assert date.year == 2019
    assert date.month == 10
    assert date.day == 1

    with pytest.raises(ValidationError):
        date_format.validate('20191010')

    with pytest.raises(ValidationError):
        date_format.validate('2019-00-01')



# Generated at 2022-06-14 14:31:54.826155
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert isinstance(df, BaseFormat)
    with pytest.raises(NotImplementedError):
        df.is_native_type(df)
    with pytest.raises(NotImplementedError):
        df.serialize(df)
    dt = datetime.date(2019, 11, 7)
    assert dt == df.validate("2019-11-07")
    assert df.validate("2019-11-07") == datetime.date(2019, 11, 7)
    assert df.validate(None) is None
    with pytest.raises(ValidationError):
        df.validate("2019-14-1")
    with pytest.raises(ValidationError):
        df.validate("2019-1-1")

# Generated at 2022-06-14 14:32:04.976433
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    # Valid format

# Generated at 2022-06-14 14:32:08.899507
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    test1 = "21:58:11"
    test2 = "21:58:11.005000"
    test3 = "21:58:11.00000"
    test4 = "21:58:11.000001"
    assert TimeFormat().validate(test1)
    assert TimeFormat().validate(test2)
    assert TimeFormat().validate(test3)
    assert TimeFormat().validate(test4)



# Generated at 2022-06-14 14:32:13.625711
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.base import TypeSystem
    from typesystem.fields import String, Time

    class MyType(TypeSystem):
        time = Time()

    typesystem = MyType()
    assert typesystem.time.validate("14:30") == datetime.time(hour=14, minute=30)

# Generated at 2022-06-14 14:32:17.457148
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    value = "2020-07-07T13:13:13.123456Z"
    dateTimeFormat_check = DateTimeFormat()
    dateTimeFormat_check.validate(value)

# Generated at 2022-06-14 14:32:25.513830
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeFormat = TimeFormat()
    time = timeFormat.validate('12:12:22')
    assert(time.hour == 12 and time.minute == 12 and time.second == 22)
    time = timeFormat.validate('12:12:22.123')
    assert(time.hour == 12 and time.minute == 12 and time.second == 22 and time.microsecond == 123000)
    time = timeFormat.validate('12:12')
    assert(time.hour == 12 and time.minute == 12 and time.second == 0)
    time = timeFormat.validate('12:12:22.123456')
    assert(time.hour == 12 and time.minute == 12 and time.second == 22 and time.microsecond == 123456)


# Generated at 2022-06-14 14:32:30.946295
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate("2020-05-15") == datetime.date(2020, 5, 15)
    try:
        date_format.validate("2020-15-15")
    except ValidationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:32:36.188831
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = "2015/7/9"
    match = DATE_REGEX.match(value)
    kwargs = {k: int(v) for k, v in match.groupdict().items()}
    try:
        return datetime.date(**kwargs)
    except ValueError:
        raise self.validation_error("invalid")


# Generated at 2022-06-14 14:32:37.596287
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2019-01-01") == datetime.date(2019, 1, 1)

# Generated at 2022-06-14 14:32:40.229975
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()

    result = format.validate("2020-02-20")
    assert isinstance(result, datetime.date)



# Generated at 2022-06-14 14:32:52.512132
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    d = DateTimeFormat()
    # test validate a valid datetime format
    assert d.validate('1985-04-12T23:20:50.52Z') == datetime.datetime(1985,4,12,23,20,50,520000)
    # test validate a invalid datetime format
    assert d.validate('1985-04-12T23:20:50.52') == datetime.datetime(1985,4,12,23,20,50,520)
    # test validate a datetime format in the future 
    assert d.validate('2054-04-12T23:20:50.52Z') == datetime.datetime(2054,4,12,23,20,50,520000)
    # test validate a datetime format in negative years

# Generated at 2022-06-14 14:33:05.812885
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate('10:10:10') == datetime.time(10, 10, 10)
    assert time_format.validate('10:10:10.1') == datetime.time(10, 10, 10, 100000)
    assert time_format.validate('10:10:10.1123123') == datetime.time(10, 10, 10, 112312)
    assert time_format.validate('10:10:10.1123123123123123') == datetime.time(10, 10, 10, 112312)
    assert time_format.validate('10:10:10.123123123123123') == datetime.time(10, 10, 10, 123123)

# Generated at 2022-06-14 14:33:08.942363
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = '2019-07-09'
    formats = DateFormat()
    assert isinstance(formats.validate(value), datetime.date)


# Generated at 2022-06-14 14:33:13.861811
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    expectedTime = datetime.time(hour=00, minute=00, second=00, microsecond=0)
    timeFormat = TimeFormat()
    actualTime = timeFormat.validate(str(expectedTime))
    assert expectedTime == actualTime
