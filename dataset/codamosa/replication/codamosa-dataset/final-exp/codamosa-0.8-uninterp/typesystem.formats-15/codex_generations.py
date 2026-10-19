

# Generated at 2022-06-14 14:23:33.078745
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert TimeFormat().serialize(datetime.time(12, 34, 56, 7890)) == "12:34:56.007890"
    assert TimeFormat().serialize(None) == None

# Generated at 2022-06-14 14:23:35.544101
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(11, 1, 9)
    test_time = TimeFormat()
    assert test_time.serialize(time) == '11:01:09'


# Generated at 2022-06-14 14:23:47.023879
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("10:00") == datetime.time(10, 0)
    assert TimeFormat().validate("10:01") == datetime.time(10, 1)
    assert TimeFormat().validate("10:10") == datetime.time(10, 10)

    assert TimeFormat().validate("10:00:01") == datetime.time(10, 0, 1)
    assert TimeFormat().validate("10:00:01.123") == datetime.time(10, 0, 1, 123000)
    with pytest.raises(ValidationError):
        TimeFormat().validate("10:00:01.")

    with pytest.raises(ValidationError):
        TimeFormat().validate("10:00:01.")

# Generated at 2022-06-14 14:23:51.559942
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Create instance of class
    myInstance = DateFormat()

    # Variables for assert
    assertValue_validate = datetime.date(2019, 7, 1)

    # Execute method
    myValue = myInstance.validate("2019-07-01")

    # Assert results
    assert  myValue == assertValue_validate


# Generated at 2022-06-14 14:23:57.422479
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # given
    value = "2020-11-19T15:34:05+00:00"
    # execute
    result = DateTimeFormat().validate(value)
    # assert
    datetime_obj = datetime.datetime(2020, 11, 19, 15, 34, 5, tzinfo=datetime.timezone.utc)
    assert result == datetime_obj

# Generated at 2022-06-14 14:24:06.444519
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    def check_TimeFormat_validate(time_string, expected_output):
        tf = TimeFormat()
        time = tf.validate(time_string)
        assert time == expected_output, "TimeFormat doesn't work for string %s" % time_string
    check_TimeFormat_validate("18:02:45.123123", datetime.time(hour=18, minute=2, second=45, microsecond=123123))
    check_TimeFormat_validate("18:02:45.12312", datetime.time(hour=18, minute=2, second=45, microsecond=123120))
    check_TimeFormat_validate("18:02:45.1231", datetime.time(hour=18, minute=2, second=45, microsecond=123100))

# Generated at 2022-06-14 14:24:12.459684
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_format = DateTimeFormat()
    assert date_format.validate('2020-03-26T11:41:00Z') == datetime.datetime(2020, 3, 26, 11, 41, 00, tzinfo=datetime.timezone.utc)
    assert date_format.validate('2020-03-26T11:41:00') == datetime.datetime(2020, 3, 26, 11, 41, 00)


# Generated at 2022-06-14 14:24:14.432578
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    df = DateFormat()
    assert df.serialize(datetime.date.today()) == datetime.date.today().isoformat()


# Generated at 2022-06-14 14:24:19.343583
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    test_value = "2019-03-20T09:20:03+03:00"
    test = DateTimeFormat()
    print(test.validate(test_value))
    print(type(test.validate(test_value)))
    assert test.validate(test_value) == datetime.datetime(2019, 3, 20, 6, 20, 3)


# Generated at 2022-06-14 14:24:22.272528
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    time = DateTimeFormat()
    print(time.validate('2020-09-20T12:00:30Z'))


# Generated at 2022-06-14 14:24:31.162335
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    """
    Test if serialize method of class TimeFormat works properly

    """
    obj = TimeFormat()
    a = datetime.time(hour = 2, minute = 45)
    b = datetime.time(hour = 17, minute = 15)
    assert obj.serialize(a) == "02:45"
    assert obj.serialize(b) == "17:15"


# Generated at 2022-06-14 14:24:34.387484
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    UUIDFormat().validate("1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed")

# Generated at 2022-06-14 14:24:36.923122
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = "2018-08-02"
    valid = DateFormat().validate(value)
    assert valid == datetime.datetime(2018, 8, 2, 0, 0)


# Generated at 2022-06-14 14:24:42.129039
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_format = UUIDFormat()
    #generate some valid UUIDs
    uuid_list = ["1b4e28ba-2fa1-11d2-883f-0016d3cca427"] 
    for uuid in uuid_list:
        obj = uuid_format.validate(uuid)
        assert isinstance(obj, uuid.UUID)

# Generated at 2022-06-14 14:24:51.576031
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    inputTime = "16:11:04.596039+02:00"
    tf = TimeFormat()
    assert type(tf.validate(inputTime)) == datetime.datetime
    assert type(tf.validate(inputTime).time()) == datetime.time
    assert tf.validate(inputTime).time() == datetime.time(16,11,4,596039, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)))
    assert tf.validate(inputTime).isoformat() == "16:11:04.059604+02:00"
    assert tf.validate(inputTime).hour == 16
    assert tf.validate(inputTime).minute == 11
    assert tf.validate(inputTime).second == 4
    assert tf.validate(inputTime).micro

# Generated at 2022-06-14 14:25:03.750774
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert isinstance(tf.validate("12:59:30.500500"), datetime.time)
    assert isinstance(tf.validate("12:59:30.5"), datetime.time)
    assert isinstance(tf.validate("12:59:30"), datetime.time)
    assert isinstance(tf.validate("12:59"), datetime.time)
    assert isinstance(tf.validate("12"), datetime.time)
    assert isinstance(tf.validate("12:59:30.5+00:00"), datetime.time)
    assert isinstance(tf.validate("12:59:30+00:00"), datetime.time)
    assert isinstance(tf.validate("12:59+00:00"), datetime.time)

# Generated at 2022-06-14 14:25:07.067086
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    format = UUIDFormat()
    uuid_str = '232f5b38-61c7-4e51-b7a1-cf9886b7c0b8'
    uuid_object = format.validate(uuid_str)
    print(uuid_object)

# Generated at 2022-06-14 14:25:10.122322
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = "2019-01-01"
    dt = DateFormat()
    res = dt.validate(date)
    assert type(res) == datetime.date


# Generated at 2022-06-14 14:25:16.704579
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    a = DateTimeFormat()

# Generated at 2022-06-14 14:25:21.848695
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    # test success
    dateFormat.validate("2012-11-12")
    # test failed
    with pytest.raises(ValidationError) as execinfo:
        dateFormat.validate("2012-11-12x")
    assert execinfo.value.message == "Must be a valid date format."


# Generated at 2022-06-14 14:25:31.439117
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Case where the value entered is a valid date in the format "yyyy-mm-dd"
    # Expected result: the string converted to the format datetime.date
    format = DateFormat()
    format.errors = {
        "format": "Must be a valid date format.",
        "invalid": "Must be a real date.",
    }
    try:
        date_test = format.validate("2020-12-31")
        assert isinstance(date_test, datetime.date)
    except:
        print("Error: expected format is 'yyyy-mm-dd'")


# Generated at 2022-06-14 14:25:34.519149
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime(2019,12,6,15,30,56)
    ser = DateTimeFormat().serialize(obj)
    assert ser == "2019-12-06T15:30:56"


# Generated at 2022-06-14 14:25:36.696515
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()

    assert date_format.validate("1988-03-03") == datetime.date(1988, 3, 3)


# Generated at 2022-06-14 14:25:41.931054
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Negative test for DateFormat.validate(self, value)
    with pytest.raises(AssertionError):
        DateFormat().validate("2020-09-10")
    with pytest.raises(AssertionError):
        DateFormat().validate("10112000-09-10")


# Generated at 2022-06-14 14:25:49.483581
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test with valid input
    assert DateFormat().validate("2019-11-20") == datetime.date(2019, 11, 20)

    # Test with invalid input
    try:
        DateFormat().validate("2019-02-40")
    except ValidationError as e:
        assert e.code == "invalid"

    try:
        DateFormat().validate("22-02-2019")
    except ValidationError as e:
        assert e.code == "format"



# Generated at 2022-06-14 14:26:00.504467
# Unit test for method validate of class TimeFormat

# Generated at 2022-06-14 14:26:02.027628
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2015, 10, 1))


# Generated at 2022-06-14 14:26:10.250868
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtf = DateTimeFormat()
    #assert dtf.validate("2019-11-09T16:48:30.000Z") == "2019-11-09T16:48:30.000Z"
    assert dtf.validate("2019-11-09T19:48:30.000+03:00") == "2019-11-09T16:48:30.000Z"
    print("test_DateTimeFormat_validate() passed!")

test_DateTimeFormat_validate()


# Generated at 2022-06-14 14:26:18.572555
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dateTime = DateTimeFormat()

    try:
        dateTime.validate("2019-02-15T16:53:54.123456+05:00")
    except ValidationError:
        assert False

    try:
        dateTime.validate("2019-02-15T16:53:54.123456")
    except ValidationError:
        assert False

    try:
        dateTime.validate("2019-02-15T16:53:54.123456789")
    except ValidationError:
        assert False

    try:
        dateTime.validate("2019-04-12T03:50Z")
    except ValidationError:
        assert False

    try:
        dateTime.validate("2019-04-12T03:50+05:00")
    except ValidationError:
        assert False

# Generated at 2022-06-14 14:26:27.692535
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test: Test if string is valid format, but not a valid date
    with pytest.raises(ValidationError):
        date_format = DateFormat()
        date_format.validate('0000-00-00')

    # Test: Test if string is valid date
    date_format = DateFormat()
    assert date_format.validate('2000-01-02') == datetime.date(2000, 1, 2)

    # Test: Test if string is not valid format
    with pytest.raises(ValidationError):
        date_format = DateFormat()
        date_format.validate('0000')



# Generated at 2022-06-14 14:26:34.096474
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dateformat_test = datetime.datetime(2019, 6, 3, 4, 5, 6, 7)
    dateformat_class = DateTimeFormat()
    assert dateformat_class.serialize(dateformat_test) == "2019-06-03T04:05:06.000007"

# Generated at 2022-06-14 14:26:43.310424
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_format = DateFormat()
    date_result = date_format.validate("2019-12-12")
    assert date_result == datetime.date(2019, 12, 12)

    time_format = TimeFormat()
    time_result = time_format.validate("12:12")
    assert time_result == datetime.time(12, 12)

    datetime_format = DateTimeFormat()
    datetime_result = datetime_format.validate("2019-12-12T12:12:12.120000")
    assert datetime_result == datetime.datetime(2019, 12, 12, 12, 12, 12, 120000)

    uuid_format = UUIDFormat()

# Generated at 2022-06-14 14:26:48.465272
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test case 1
    format_test_1 = DateFormat()
    assert format_test_1.validate('2019-04-07') == datetime.date(2019, 4, 7)
    # Test case 2
    format_test_2 = DateFormat()
    assert format_test_2.validate('2019-04-10') == datetime.date(2019, 4, 10)
    # Test case 3
    format_test_3 = DateFormat()
    assert format_test_3.validate('2019-04-12') == datetime.date(2019, 4, 12)

# Generated at 2022-06-14 14:27:00.558484
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2020-04-10T11:30:00Z") == datetime.datetime(2020, 4, 10, 11, 30, 0, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate("2020-04-10T11:30:00+02:00") == datetime.datetime(2020, 4, 10, 11, 30, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))
    assert DateTimeFormat().validate("2020-04-10T11:30:00+0200") == datetime.datetime(2020, 4, 10, 11, 30, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))

# Generated at 2022-06-14 14:27:03.905444
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    time=datetime.datetime.now()
    t=time.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    str=DateTimeFormat().validate(t).strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    assert t==str


# Generated at 2022-06-14 14:27:08.951511
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    test_data = "16:07"
    actual = time_format.validate(test_data)
    expected = datetime.time(16, 7, 0, 0)
    assert actual == expected

# Unit tests for method is_native_type of class TimeFormat

# Generated at 2022-06-14 14:27:18.044693
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    #Initialize necessary objects for test
    time_format = TimeFormat()
    #Test case 1: input value is a valid time format
    input_value = "10:30:05"
    actual = time_format.validate(input_value)
    assert actual == datetime.time(hour=10, minute=30, second=5)

    #Test case 2: input value is not a valid time format
    input_value = "10:30:30.05"
    actual = time_format.validate(input_value)
    assert actual == datetime.time(hour=10, minute=30, second=30, microsecond=50000)

    #Test case 3: input value is not a valid time format
    input_value = "10:30:30.051111"

# Generated at 2022-06-14 14:27:20.017363
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate(value='2020-01-01') == datetime.date(2020, 1, 1)
    assert DateTimeFormat().validate(value='2020-11-01T15:23:30') == datetime.datetime(2020, 11, 1, 15, 23, 30)

# Generated at 2022-06-14 14:27:22.537361
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format = TimeFormat()
    assert format.validate("12:1") == datetime.time(12, 1)
    assert format.validate("00:1:5") == datetime.time(0, 1, 5)


# Generated at 2022-06-14 14:27:24.328471
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtf = DateTimeFormat()
    assert dtf.validate("1998-01-01T12:00:00") == datetime.datetime(1998, 1, 1, 12, 0, 0)

# Generated at 2022-06-14 14:27:34.822031
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    df.validate("2020-02-12")
    df.validate("2020-02-12")


# Generated at 2022-06-14 14:27:44.907466
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-09-11T12:00:00.000000") == datetime.datetime(2019, 9, 11, 12)
    assert DateTimeFormat().validate("2019-09-11T12:00:00.000001") == datetime.datetime(2019, 9, 11, 12, 0, 0, 1)
    assert DateTimeFormat().validate("2019-09-11T12:00:00.1234") == datetime.datetime(2019, 9, 11, 12, 0, 0, 123400)
    assert DateTimeFormat().validate("2019-09-11T12:00:00.1234Z") == datetime.datetime(2019, 9, 11, 12, 0, 0, 123400, tzinfo=datetime.timezone.utc)
    assert DateTime

# Generated at 2022-06-14 14:27:48.152462
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    expected_output = datetime.datetime(2019, 6, 27, tzinfo=datetime.timezone.utc)
    input_value = "2019-06-27T00:00:00Z"
    actual_output = DateTimeFormat().validate(input_value)
    assert expected_output == actual_output

# Generated at 2022-06-14 14:28:00.235133
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
	print('\n------------------- UNIT TEST DateTimeFormat_validate: -------------------\n')
	obj = DateTimeFormat()
	print('Test cases')
	# Case1
	value = '2018-08-20T16:32:18.829861+00:00'
	print('value = %s' % value)
	result = obj.validate(value)
	print('result = %s' % result)
	print('expected result = 2018-08-20 16:32:18.829861+00:00')
	if result == datetime.datetime(2018, 8, 20, 16, 32, 18, 829861, tzinfo=datetime.timezone.utc):
		print('PASSED')
	else:
		print('FAILED')
	# Case2
	

# Generated at 2022-06-14 14:28:07.842781
# Unit test for method validate of class DateTimeFormat

# Generated at 2022-06-14 14:28:13.026383
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate("23:59:45") == datetime.time(hour=23, minute=59, second=45)

    with pytest.raises(ValidationError) as err:
        time_format.validate("02:60:45")
 
    assert "Must be a real time" in str(err)


# Generated at 2022-06-14 14:28:19.544820
# Unit test for method serialize of class DateTimeFormat

# Generated at 2022-06-14 14:28:30.323535
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    h = 1
    m = 2
    s = 3
    ms = 4
    t = datetime.time(h, m, s, ms)
    s = "T{:02d}:{:02d}:{:02d}.{:06d}".format(h, m, s, ms)
    assert time_format.validate(s) == t
    s = "T{:02d}:{:02d}:{:02d}".format(h, m, s)
    assert time_format.validate(s) == t
    s = "T{:02d}:{:02d}".format(h, m)
    assert time_format.validate(s) == t
    s = "T{:02d}".format(h)
    assert time_format

# Generated at 2022-06-14 14:28:35.040281
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Error case: Raise ValidationError
    with pytest.raises(ValidationError):
        DateFormat().validate('test')

    # Success case: Return datetime.date format
    assert DateFormat().validate('2018-10-10') == datetime.date(2018, 10, 10)

# Generated at 2022-06-14 14:28:39.711413
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    
    # test case 1
    test_DateFormat = DateFormat()
    try:
        test_DateFormat.validate('2019-06-06')
        assert False
    except ValueError:
        assert True

    # test case 2
    test_DateFormat = DateFormat()
    try:
        test_DateFormat.validate(' ')
        assert False
    except ValueError:
        assert True


# Generated at 2022-06-14 14:28:56.225285
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Bug: arround lines 1036 and 1037, in function validate of class DateTimeFormat.
    #     the method utcfromtimestamp(...) throw an exception, because the argument that
    #     is passed is not valid. This argument is generated by the method get_tzinfo_offset.
    #     This method is in class BaseFormat from typesystem package
    # Fix: do a correction in the regex. Add a POSITIVE symbol '+' at the beginning of the regex
    #     In this way, the regex is more strict. Concretely, the regex will not capture strings
    #     with negative sign in the UTC offset field.
    # Testing
    dtf = DateTimeFormat()
    str_datetime_neg = "2020-02-13T23:40:10-04:00"

# Generated at 2022-06-14 14:29:06.883780
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    test_validate = DateTimeFormat().validate
    assert isinstance(test_validate("2009-01-01T00:00"), datetime.datetime)
    # datetime.datetime(2009, 1, 1, 0, 0)
    assert isinstance(test_validate("2009-01-01T00:00:00"), datetime.datetime)
    # datetime.datetime(2009, 1, 1, 0, 0)
    assert isinstance(test_validate("2009-01-01T00:00:00.000"), datetime.datetime)
    # datetime.datetime(2009, 1, 1, 0, 0)
    assert isinstance(test_validate("2009-01-01T00:00:00.000000"), datetime.datetime)
    # datetime.datetime(2009, 1

# Generated at 2022-06-14 14:29:07.433268
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert 1 == 1

# Generated at 2022-06-14 14:29:12.295029
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # Arrange
    obj = datetime.datetime(2020, 6, 22, 16, 36, tzinfo=datetime.timezone.utc)
    sut = DateTimeFormat()

    # Act
    result = sut.serialize(obj)

    # Assert
    assert result == "2020-06-22T16:36:00Z"



# Generated at 2022-06-14 14:29:15.250650
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    fmt = DateTimeFormat()

    serialized_datetime = fmt.serialize(datetime.datetime.now())
    # print(serialized_datetime)
    assert serialized_datetime is not None

# Generated at 2022-06-14 14:29:25.525458
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    tz_utc = datetime.timezone.utc
    rfc3339 = "%Y-%m-%dT%H:%M:%S+00:00"

# Generated at 2022-06-14 14:29:33.715017
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    print("test_DateTimeFormat_validate()")
    assert DATETIME_REGEX.match(DateTimeFormat().validate("2019-01-01T01:01:01Z").isoformat())
    assert DATETIME_REGEX.match(DateTimeFormat().validate("2019-01-01T01:01:01+00:00").isoformat())
    assert DATETIME_REGEX.match(DateTimeFormat().validate("2019-01-01T01:01:01+09:00").isoformat())
    assert DATETIME_REGEX.match(DateTimeFormat().validate("2019-01-01T01:01:01-09:00").isoformat())

# Generated at 2022-06-14 14:29:43.877827
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-01-01T12:00Z") == datetime.datetime(2019, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate("2019-01-01T12:00+00:00") == datetime.datetime(2019, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate("2019-01-01T12:00") == datetime.datetime(2019, 1, 1, 12, 0)
    assert DateTimeFormat().validate("2019-01-01") == datetime.datetime(2019, 1, 1)

# Generated at 2022-06-14 14:29:56.187882
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format_ = DateTimeFormat()
    date = format_.validate("2018-12-1T08:14:12.123456Z")
    assert date == datetime.datetime(2018, 12, 1, 8, 14, 12, 123456, datetime.timezone.utc)
    date = format_.validate("2018-12-1T8:14:12.123456")
    assert date == datetime.datetime(2018, 12, 1, 8, 14, 12, 123456)
    date = format_.validate("2018-12-1T8:14:12.123456-01:30")
    assert date == datetime.datetime(2018, 12, 1, 8, 14, 12, 123456, datetime.timezone(datetime.timedelta(hours=-1, minutes=-30)))

# Generated at 2022-06-14 14:29:57.944811
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime.now()) is not None


# Generated at 2022-06-14 14:30:06.552543
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    datetimeFormat = DateTimeFormat()
    now = datetime.datetime.now()
    assert(datetimeFormat.serialize(now) == now.isoformat())

# Generated at 2022-06-14 14:30:15.080440
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date_string = '2020-05-08'
    assert date_format.validate(date_string) == datetime.date(2020, 5, 8)
    # the string does not match the defined regex
    assert str(date_format.validate('2020-5-8')) == 'Must be a valid date format.'
    # the year is invalid
    assert str(date_format.validate('3000-05-08')) == 'Must be a real date.'
# This is a unit test for the method is_native_type of class DateFormat

# Generated at 2022-06-14 14:30:26.667625
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format = DateTimeFormat()
    assert date_time_format.validate("2020-06-06T12:00:00.000000Z") == datetime.datetime(year = 2020, month = 6, day = 6, hour = 12, minute = 0, second = 0, microsecond = 0, tzinfo = datetime.timezone.utc)
    assert date_time_format.validate("2020-06-06T12:00:00.000000+02:00") == datetime.datetime(year = 2020, month = 6, day = 6, hour = 12, minute = 0, second = 0, microsecond = 0, tzinfo = datetime.timezone(datetime.timedelta(hours=2)))
    assert date_time_format.validate("2020-06-06T12:00:00Z")

# Generated at 2022-06-14 14:30:37.382135
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t1='05:00'
    t2='5:00'
    t3='05:00:00.000000'
    t4='05:00:00.000001'
    t5='05:00:00.123456'
    t6='05:00:00.1234'
    t7='05:00:00.1234567'
    t8='05:00:00.12345678'
    t9='05:00:00.123456789'
    t10='05:00:00.1234567890'
    t11='05:00:00.12345678912345'
    t12='05:00:00.123456789123456'
    t13='05:00:00.1234567891234567'

# Generated at 2022-06-14 14:30:45.217869
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = "2020-01-31"
    # is_native_type use to check whether the data type is a valid data type which has been defined
    assert isinstance(date, datetime.date) == False
    # convert the string to a datetime.date type
    match = DATE_REGEX.match(date)
    kwargs = {k: int(v) for k, v in match.groupdict().items()}
    try:
        assert type(datetime.date(**kwargs)) == type(datetime.date(2020, 2, 29))
    except ValueError:
        print("The date is not valid")


# Generated at 2022-06-14 14:30:53.562348
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Summary: Test validation for utc datetime
    test_DateTimeFormat = DateTimeFormat()
    datetime_str = "2019-01-01T01:10:15.123456Z"
    res = test_DateTimeFormat.validate(datetime_str)
    assert res.isoformat() == "2019-01-01T01:10:15.123456+00:00"
    print("Test case 1 passed")

    # Summary: Test validation for nonutc datetime
    datetime_str = "2019-01-01T01:10:15.123456+10:00"
    res = test_DateTimeFormat.validate(datetime_str)
    assert res.isoformat() == "2019-01-01T01:10:15.123456+10:00"
    print("Test case 2 passed")

# Generated at 2022-06-14 14:30:57.201575
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2004-12-23") == datetime.date(2004, 12, 23)
    assert DateFormat().validate("2004-1-1") == datetime.date(2004, 1, 1)


# Generated at 2022-06-14 14:30:59.093388
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    value = DateTimeFormat().serialize(datetime.datetime.now())
    assert value is not None


# Generated at 2022-06-14 14:31:04.381777
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
	time = TimeFormat()
	value = "10:10:10"
	print(time.validate(value))
	# value = "10:10"
	# print(time.validate(value))
	# value = "10:10:10:10"
	# print(time.validate(value))

# test_TimeFormat_validate()


# Generated at 2022-06-14 14:31:06.754912
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    date = '2020-8-18'
    assert isinstance(df.validate(date), datetime.date) == True


# Generated at 2022-06-14 14:31:25.832364
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    date_time = datetime.datetime.now()
    str_formated = date_time_format.serialize(date_time)
    
    assert len(str_formated) == len(date_time.isoformat())

# Generated at 2022-06-14 14:31:31.470924
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtf = DateTimeFormat()
    # valid
    assert dtf.validate('2012-04-23T18:25:43.511Z')
    # invalid
    assert dtf.validate('2012-04-23T18:25:43Z')
    assert dtf.validate('xx2012-04-23T18:25:43.511Z')


# Generated at 2022-06-14 14:31:33.823602
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("14:30") == datetime.time(14, 30)



# Generated at 2022-06-14 14:31:38.361540
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date = datetime.datetime(year=2020, month=8, day=24, hour=13, minute=12, second=11, microsecond=1)
    print(date.isoformat())
    assert DateTimeFormat().serialize(date) == '2020-08-24T13:12:11.000001'


# Generated at 2022-06-14 14:31:44.569553
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2020-10-5") == datetime.date(2020, 10, 5)
    assert DateFormat().validate("2020-10-05") == datetime.date(2020, 10, 5)
    assert DateFormat().validate("2020-10-6") == datetime.date(2020, 10, 6)
    assert DateFormat().validate("2020-10-06") == datetime.date(2020, 10, 6)


# Generated at 2022-06-14 14:31:47.765946
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate("2020-06-05") == datetime.date(2020, 6, 5)


# Generated at 2022-06-14 14:31:57.705793
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    #test input value with different formats
    #HH:MM
    value_1 = "07:30"
    #HH:MM:SS
    value_2 = "07:30:30"
    #HH:MM:SS.mmmmmm
    value_3 = "07:30:30.123456"

    #test HH:MM
    time_format = TimeFormat()
    assert time_format.validate(value_1) == datetime.time(7,30)

    #test HH:MM:SS
    time_format = TimeFormat()
    assert time_format.validate(value_2) == datetime.time(7,30,30)

    #test HH:MM:SS.mmmmmm
    time_format = TimeFormat()

# Generated at 2022-06-14 14:32:09.677864
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    class TestClass(object):
        pass
    test_class = TestClass()
    test_class.errors = {
        "format": "Must be a valid date format.",
        "invalid": "Must be a real date.",
    }
    date = DateFormat()
    date.validate("2016-05-16")
    date.validate("2016-05-1")
    date.validate("2016-5-16")
    date.validate("2016-5-1")
    try:
        date.validate("2016-05")
    except Exception as ex:
        assert ex.code == "format"
        assert ex.text == "Must be a valid date format."
    try:
        date.validate("2016-5")
    except Exception as ex:
        assert ex.code == "format"
        assert ex

# Generated at 2022-06-14 14:32:18.086696
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format_test_class = DateFormat()
    assert format_test_class.is_native_type(datetime.date.today())
    try:
        format_test_class.validate('2020-03-04')
    except Exception as e:
        #print(e)
        assert False
    try:
        format_test_class.validate('2020-02-30')
    except Exception as error:
        #print(error)
        assert str(error) == 'Must be a real date.'
        assert True


# Generated at 2022-06-14 14:32:27.254221
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate('08:00') == datetime.time(8)
    assert time_format.validate('08:01') == datetime.time(8, 1)
    assert time_format.validate('08:01:00') == datetime.time(8, 1)
    assert time_format.validate('08:01:00.123123') == datetime.time(8, 1, 0, 123123)
    time_format.validate('08:01:01.12312')
    with pytest.raises(ValidationError):
        time_format.validate('12:91:01.12312')
    with pytest.raises(ValidationError):
        time_format.validate('12:91:01.12312')

# Generated at 2022-06-14 14:32:38.870240
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    date = datetime.date(2019, 2, 28)
    result = format.validate("2019-02-28")
    assert result == date


# Generated at 2022-06-14 14:32:45.843470
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    try:
        df.validate('2019-01-01')
        assert True, "Must be a real date"
    except ValidationError:
        assert False, "Must be a real date"
    try:
        df.validate('2019-01-40')
        assert False, "Must be a real date"
    except ValidationError:
        assert True, "Must be a real date"
    

# Generated at 2022-06-14 14:32:48.025092
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('1997-01-28') == datetime.date(year=1997, month=1, day=28)



# Generated at 2022-06-14 14:32:50.546350
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    inputValue = "2020-01-01"
    testDateFormat = DateFormat()
    assert isinstance(testDateFormat.validate(inputValue), datetime.date)


# Generated at 2022-06-14 14:32:54.060426
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dtf = DateTimeFormat()
    assert dtf.serialize(datetime.datetime(2018, 1, 1, 12, 00, tzinfo=datetime.timezone(datetime.timedelta(0))))=="2018-01-01T12:00:00+00:00"


# Generated at 2022-06-14 14:32:58.114513
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(None) == None
    x = datetime.datetime(2001, 2, 3, 4, 5, 6, 7)
    assert DateTimeFormat().serialize(x) == '2001-02-03T04:05:06.000007'
    assert DateTimeFormat().serialize(datetime.date(2001,2,3)) == '2001-02-03'
    assert DateTimeFormat().serialize(datetime.time(4,5,6,7)) == '04:05:06.000007'


# Generated at 2022-06-14 14:33:02.590060
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    value = "2020-04-05 20:41:42"
    assert DateTimeFormat().validate(value) == datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


# Generated at 2022-06-14 14:33:07.818979
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    obj = date_time_format.validate("2020-06-01T00:00:00.00Z")
    result = date_time_format.serialize(obj)
    assert result == "2020-06-01T00:00:00Z"

# Generated at 2022-06-14 14:33:09.375160
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    DATE_OBJ = datetime.date(year=1990, month=11, day=6)
    assert DateFormat().validate("1990-11-06") == DATE_OBJ


# Generated at 2022-06-14 14:33:11.879927
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    result = DateFormat().validate("2020-10-30")
    assert result == datetime.date(2020, 10, 30)
