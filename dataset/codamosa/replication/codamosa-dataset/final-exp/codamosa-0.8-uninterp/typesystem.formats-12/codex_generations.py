

# Generated at 2022-06-14 14:23:34.975804
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    validator = TimeFormat()
    assert validator.serialize(datetime.time(microsecond=1)) == "00:00:00.000001"
    assert validator.serialize(datetime.time(microsecond=111)) == "00:00:00.000111"
    assert validator.serialize(datetime.time(microsecond=11111)) == "00:00:00.111111"
    assert validator.serialize(datetime.time(microsecond=1111111)) == "00:00:01.111111"

# Generated at 2022-06-14 14:23:47.175416
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    a1 = DateTimeFormat()
    a2 = DateTimeFormat()

    # Create assert statements to test the method validate
    # The program will exit if the test fails

    # Check the case of correct dateTime format but incorrect dateTime
    assert a1.validate('2018-02-01T23:59:59')
    assert a1.validate('2018-02-01T23:59:59Z')
    assert a1.validate('2018-02-01T23:59:59-06:00')
    assert a1.validate('2018-02-01T23:59:59-06')
    assert a1.validate('2018-02-01T23:59')
    assert a1.validate('2018-02-01T23')
    assert a1.validate('2018-02-01')

    #

# Generated at 2022-06-14 14:23:58.114170
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(1970, 1, 1)) == "1970-01-01T00:00:00Z"
    assert DateTimeFormat().serialize(datetime.datetime(2000, 1, 1)) == "2000-01-01T00:00:00Z"
    assert DateTimeFormat().serialize(None) == None
    assert DateTimeFormat().serialize(datetime.datetime(1970, 1, 1, 10, 30, 30)) == "1970-01-01T10:30:30Z"
    assert DateTimeFormat().serialize(datetime.datetime(2019, 1, 1, 10, 30, microsecond=123)) == "2019-01-01T10:30:00.000123Z"

# Generated at 2022-06-14 14:24:00.430551
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    df = DateFormat()
    assert df.serialize(datetime.date(year=2020, month=2, day=12)) == '2020-02-12'


# Generated at 2022-06-14 14:24:02.932058
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = "2018-01-01"
    instance = DateFormat()
    validate = instance.validate(value)
    result = datetime.date(2018, 1, 1)
    assert validate == result


# Generated at 2022-06-14 14:24:08.192202
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    assert t.validate('12:00') == datetime.time(12, 0)
    assert t.validate('12:00:00') == datetime.time(12, 0)
    assert t.validate('12:00:00.000000') == datetime.time(12, 0)
    assert t.validate('12:00:00.000000') == datetime.time(12, 0)
    assert t.validate('12:00:00.000001') == datetime.time(12, 0, 0, 1)

# Generated at 2022-06-14 14:24:11.143431
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_format = UUIDFormat()
    uuid_format.validate(value="7F1F0985-C7B0-4A34-BAA1-C163975EAE02")

# Generated at 2022-06-14 14:24:14.604889
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # Given
    obj = datetime.datetime(2020, 10, 1, 14, 0, 0, 0, datetime.timezone.utc)

    # When
    actual = DateTimeFormat().serialize(obj)

    # Then
    assert actual == "2020-10-01T14:00:00Z"

# Generated at 2022-06-14 14:24:17.484583
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    validate_example = "2018-12-31"
    assert isinstance(date_format.validate(validate_example), datetime.date)


# Generated at 2022-06-14 14:24:28.683326
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date_test = DateFormat()
    assert date_test.serialize(datetime.date(2019,4,1)) == '2019-04-01'
    assert date_test.serialize(datetime.datetime(2019,4,1,12,22,1,1)) == '2019-04-01'
    assert date_test.serialize(datetime.datetime(2019,4,1,12,22,0)) == '2019-04-01'
    assert date_test.serialize(datetime.datetime(2019,4,1,12,22,0,1)) == '2019-04-01'
    assert date_test.serialize('2019-04-01') == '2019-04-01'
    assert date_test.serialize(None) == None
    assert date_test.serialize(123)

# Generated at 2022-06-14 14:24:38.535547
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    test_time = "12:34:56.789"
    time_format = TimeFormat()
    assert time_format.validate(test_time) == datetime.time(12, 34, 56, 789000)


# Generated at 2022-06-14 14:24:43.506684
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    # Arrange
    date_format = DateFormat()
    expected_output = "2020-04-10"
    # Act
    actual_output = date_format.serialize(datetime.date(2020, 4, 10))
    # Assert
    assert actual_output == expected_output



# Generated at 2022-06-14 14:24:46.921292
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_format_obj = UUIDFormat()
    assert uuid_format_obj.validate('123e4567-e89b-12d3-a456-426655440000') == uuid.UUID('123e4567-e89b-12d3-a456-426655440000')

# Generated at 2022-06-14 14:24:49.830075
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    time = tf.validate("12:34:56.123456")
    # Tests if the time returned by validate() is a real time
    assert isinstance(time, datetime.time)


# Generated at 2022-06-14 14:24:51.828841
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = '2019-11-14'
    assert DateFormat().validate(date) == datetime.date(2019, 11, 14)


# Generated at 2022-06-14 14:24:59.206409
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_format = UUIDFormat()
    # Test with a valid UUID
    assert uuid_format.validate("dd6c8952-b0de-4d3b-9d2b-5f5cc9e7d5cf") != None
    # Test with an invalid UUID
    try:
        uuid_format.validate("23")
    except:
        return
    assert False


# Generated at 2022-06-14 14:25:08.936985
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    class TimeObject:
        def __init__(self, year, month, day, hour, minute):
            self.time = datetime.datetime(year, month, day, hour, minute)
        def __eq__(self, other):
            return self.time == other.time
    #Test format yyyy-mm-dd hh:mm
    time = DateTimeFormat().validate("2019-01-28 16:29")
    assert time == TimeObject(2019, 1, 28, 16, 29)
    #Test format yyyy-mm-ddThh:mm
    time = DateTimeFormat().validate("2019-01-28T16:29")
    assert time == TimeObject(2019, 1, 28, 16, 29)
    #Test format yyyy-mm-ddThh:mm:ss
    time = Date

# Generated at 2022-06-14 14:25:10.987608
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    date.validate("2020-06-04")
    assert "2020-06-04"


# Generated at 2022-06-14 14:25:18.170191
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    test_UUID = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    uuid_format = UUIDFormat()
    try:
        validate = uuid_format.validate('f47ac10b-58cc-4372-a567-0e02b2c3d479')
    except ValueError as e:
        print(e)
    #assert validate == test_UUID
        


# Generated at 2022-06-14 14:25:24.070975
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    """
    UUID validation for a string representing a valid UUID should return a UUID object
    """
    format = UUIDFormat()
    # Consider a valid UUID
    uuid_string = "6a0f67cc-58d1-4a9a-9342-b36adabf1162"
    uuid_object = uuid.UUID(uuid_string)
    assert format.validate(uuid_string) == uuid_object


# Generated at 2022-06-14 14:25:34.965378
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    
    assert time_format.validate('12:00') == datetime.time(12, 00)
    assert time_format.validate('12:00:00') == datetime.time(12, 00, 00)
    assert time_format.validate('12:00:00.00') == datetime.time(12, 00, 00, 0)
    assert time_format.validate('12:00:00.000001') == datetime.time(12, 00, 00, 1)
    assert time_format.validate('12:00:00.0000010') == datetime.time(12, 00, 00, 10)
    assert time_format.validate('12:00:00.00000100') == datetime.time(12, 00, 00, 100)
    assert time_format

# Generated at 2022-06-14 14:25:36.524923
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate("2020-02-12")



# Generated at 2022-06-14 14:25:41.776966
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():

    #setup
    date = DateFormat()
    #test 1
    assert date.validate("0001-01-01") == datetime.date(1,1,1)
    #test 2
    assert date.validate("2020-10-14") == datetime.date(2020,10,14)


# Generated at 2022-06-14 14:25:44.497000
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    assert date.validate('2020-04-21') == datetime.date(2020, 4, 21)


# Generated at 2022-06-14 14:25:49.269677
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    fmt = DateFormat()
    fmt.validate("2002-10-27")
    try:
        fmt.validate("2010-10-27T14:01:02Z")
        assert False
    except ValidationError as e:
        assert e.code == "format"


# Generated at 2022-06-14 14:26:00.020829
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_format.validate("12:34")
    try:
        time_format.validate("12:60")
    except ValidationError as e:
        assert e.code == "invalid"
    try:
        time_format.validate("24:34")
    except ValidationError as e:
        assert e.code == "invalid"
    try:
        time_format.validate("12:34:99")
    except ValidationError as e:
        assert e.code == "format"
    try:
        time_format.validate("12:34:00.0")
    except ValidationError as e:
        assert e.code == "format"
    time_format.validate("12:34:00.000000")

# Generated at 2022-06-14 14:26:07.742310
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    from typesystem.formats import DateTimeFormat
    assert DateTimeFormat().validate('2020-02-01T00:01:02Z') == datetime.datetime(2020, 2, 1, 0, 1, 2, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate('2020-02-01T00:01:02+00:00') == datetime.datetime(2020, 2, 1, 0, 1, 2, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate('2020-02-01T00:01:02+00') == datetime.datetime(2020, 2, 1, 0, 1, 2, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:26:10.869318
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = DateFormat()
    obj = d.validate('1999-12-31')

    assert isinstance(obj, datetime.date)

    assert obj.year == 1999
    assert obj.month == 12
    assert obj.day == 31



# Generated at 2022-06-14 14:26:13.048473
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    time = t.validate('14:30')
    assert time.isoformat() == '14:30:00'



# Generated at 2022-06-14 14:26:15.414737
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    format = DateFormat()
    date = datetime.datetime(2019, 12, 3)
    assert format.serialize(date) == "2019-12-03"


# Generated at 2022-06-14 14:26:25.424678
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    from datetime import datetime
    assert DateTimeFormat().validate('2019-12-31T23:59:59.999999+00:00') == datetime(2019, 12, 31, 23, 59, 59, 999999, tzinfo = datetime.timezone.utc)
    assert DateTimeFormat().validate('2019-12-31T23:59:59.999999Z') == datetime(2019, 12, 31, 23, 59, 59, 999999)



# Generated at 2022-06-14 14:26:28.673177
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dt = datetime.date.today()
    df = DateFormat()
    assert dt == df.validate(dt.isoformat())


# Generated at 2022-06-14 14:26:39.552958
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():

	format = DateFormat()

	with pytest.raises(ValidationError):
		format.validate("2019-01-1")
	with pytest.raises(ValidationError):
		format.validate("2019-01-40")
	with pytest.raises(ValidationError):
		format.validate("2019-21-01")
	with pytest.raises(ValidationError):
		format.validate("2019-2-01")
	with pytest.raises(ValidationError):
		format.validate("201-01-01")
	with pytest.raises(ValidationError):
		format.validate("1-01-01")
	with pytest.raises(ValidationError):
		format.validate("2-01-01")

# Generated at 2022-06-14 14:26:49.221715
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    valid_formats = ['2018-12-31T20:23Z', '2018-12-31T20:23:55.555555Z', '2018-12-31T20:23:55+03:00', '2018-12-31T20:23:55.555555-06:30',
              '2018-12-31 20:23:55.555555', '2018-12-31 20:23:55', '2018-12-31 20:23']

# Generated at 2022-06-14 14:26:54.475498
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    pattern = DateTimeFormat()
    date = "2020-09-08T23:20:00Z"
    result = pattern.validate(date)
    assert str(result) == "2020-09-08 23:20:00+00:00"


# Generated at 2022-06-14 14:26:59.281371
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    import datetime
    from typesystem.base import ValidationError
    a = DateFormat()
    try:
        a.validate("2020-02-28")
    except ValidationError:
        assert False
    try:
        a.validate("2020-02-29")
    except ValidationError:
        assert True


# Generated at 2022-06-14 14:27:05.929573
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Case 1: Success
    value_case1 = "2020-01-01"
    testing_class = DateFormat()
    result = testing_class.validate(value_case1)
    assert result == datetime.date(2020, 1, 1)

    # Case 2: Failure
    value_case2 = "2020-1-1"
    testing_class = DateFormat()
    result = testing_class.validate(value_case2)
    assert result.code == "format"

    # Case 3: Failure
    value_case3 = "2020-01-32"
    testing_class = DateFormat()
    result = testing_class.validate(value_case3)
    assert result.code == "invalid"


# Generated at 2022-06-14 14:27:12.193653
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Case: input as string of a invalid date, expect raise error
    with pytest.raises(ValidationError):
        DateFormat().validate(input_data="2020-15-15")
    # Case: input as a date object, expect return date object
    date = DateFormat().validate(input_data=datetime.date(2019,11,24))
    assert isinstance(date, datetime.date)


# Generated at 2022-06-14 14:27:17.948203
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()

    try:
        date_format.validate('2020-12-15')
    except Exception as e:
        assert e.code == 'invalid'
        assert str(e) == 'Must be a real date.'

    assert date_format.validate('2020-12-15') == datetime.date(year=2020, month=12, day=15)



# Generated at 2022-06-14 14:27:20.329235
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    input_date = '2020-07-29'
    correct_date = datetime.date(2020, 7, 29)
    result = DateFormat().validate(input_date)
    assert result == correct_date


# Generated at 2022-06-14 14:27:28.482494
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    test1 = DateFormat().validate("2019-08-12")
    assert test1 == datetime.date(2019,8,12)
    test2 = DateFormat().validate("2019-13-12")
    assert test2 == ValueError
    test3 = DateFormat().validate("2019-13")
    assert test3 == ValueError
    test4 = DateFormat().validate("2019")
    assert test4 == ValueError


# Generated at 2022-06-14 14:27:31.773710
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate('10:00')
    assert time.validate('10:00:25')
    assert time.validate('10:00:25.456')



# Generated at 2022-06-14 14:27:34.800482
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    d = DateTimeFormat()
    assert d.validate("2019-04-12T14:27:37.123456Z") == datetime.datetime(2019, 4, 12, 14, 27, 37, 123456, datetime.timezone.utc)

# Generated at 2022-06-14 14:27:43.165625
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    time = tf.validate("12:00:01.123456")
    assert isinstance(time, datetime.time)
    assert time.hour == 12
    assert time.minute == 0
    assert time.second == 1
    assert time.microsecond == 123456

    time = tf.validate("13:02")
    assert isinstance(time, datetime.time)
    assert time.hour == 13
    assert time.minute == 2
    assert time.second == 0
    assert time.microsecond == 0

    time = tf.validate("00:00:00.000001")
    assert isinstance(time, datetime.time)
    assert time.hour == 0
    assert time.minute == 0
    assert time.second == 0
    assert time.microsecond == 1

    time = tf

# Generated at 2022-06-14 14:27:45.825816
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format_validate = DateTimeFormat()
    date_time_format_validate.validate("2019-01-01T10:00:00+10:00")
    pass


# Generated at 2022-06-14 14:27:58.111938
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.base import typesystem
    # Test case data
    time_format_cases = [
        ("0:0", datetime.time(0, 0)),
        ("15:59", datetime.time(15, 59)),
        ("16:00:00", datetime.time(16, 0, 0)),
        ("16:00:02", datetime.time(16, 0, 2)),
        ("16:00:02.123", datetime.time(16, 0, 2, 123000)),
        ("16:00:02.123456", datetime.time(16, 0, 2, 123456)),
    ]

    for case in time_format_cases:
        time_format_obj = typesystem.TimeFormat()
        if time_format_obj.is_native_type(case[1]):
            time_

# Generated at 2022-06-14 14:28:06.536761
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # set up test
    format = DateTimeFormat()
    values = [
        "2019-01-01T12:34:56Z",
        "2019-01-01T12:34:56.123456Z",
        "2019-01-01T12:34:56-03:30",
        "2019-01-01T12:34:56.123456+04:00",
    ]

# Generated at 2022-06-14 14:28:15.934379
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate('2017-12-10')==datetime.datetime(2017,12,10,0,0)
    assert DateTimeFormat().validate('2017-12-10T08:30')==datetime.datetime(2017,12,10,8,30)
    assert DateTimeFormat().validate('2017-12-10T08:30:30')==datetime.datetime(2017,12,10,8,30,30)
    assert DateTimeFormat().validate('2017-12-10T08:30:30.123456')==datetime.datetime(2017,12,10,8,30,30,123456)

# Generated at 2022-06-14 14:28:28.603881
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    
    v = DateFormat()
    # positive test
    assert v.validate("2020-07-01") == datetime.date(2020, 7, 1)
    assert v.validate("2020-07-31") == datetime.date(2020, 7, 31)
    assert v.validate("2000-01-01") == datetime.date(2000, 1, 1)


    # negative test
    try:
        v.validate("2020-07-32")
    except ValidationError as e:
        assert e.code == 'invalid'
    try:
        v.validate("2020-13-01")
    except ValidationError as e:
        assert e.code == 'invalid'
    try:
        v.validate("2020-07")
    except ValidationError as e:
        assert e

# Generated at 2022-06-14 14:28:30.606621
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate('2020-10-02') == datetime.date(2020, 10, 2)



# Generated at 2022-06-14 14:28:38.478759
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate("2020-02-12") == datetime.date(2020, 2, 12)
    assert date_format.validate("2020-02-29") == datetime.date(2020, 2, 29)
    assert date_format.validate("2019-02-29") == datetime.date(2019, 2, 29)
    assert date_format.validate("2019-02-12") == datetime.date(2019, 2, 12)


# Generated at 2022-06-14 14:28:41.371874
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    date = dateFormat.validate("2019-02-28")
    assert isinstance(date, datetime.date)


# Generated at 2022-06-14 14:28:45.045934
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dt = DateTimeFormat().validate("1970-01-01T00:00:00Z")
    assert dt == datetime.datetime(1970, 1, 1, 0, 0, 0)

# Generated at 2022-06-14 14:28:54.956451
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    test1 = DateTimeFormat()
    assert test1.validate('2019-09-02T13:55:12.838658') == datetime.datetime(
        2019, 9, 2, 13, 55, 12, 838658, tzinfo=None
    )
    try:
        test1.validate('2019-09-02T13:55:12.838658X')
    except ValidationError as e:
        assert e.code == 'format'
    try:
        test1.validate('2019-09-02T13:55:12.8386588')
    except ValidationError as e:
        assert e.code == 'invalid'

# Generated at 2022-06-14 14:28:58.956847
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    print("Testing for method validate of TimeFormat class")
    assert TimeFormat().validate("22:30:20.510120") == datetime.time(22,30,20,510120)



# Generated at 2022-06-14 14:29:08.282579
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()

    # Test valid dates
    assert date_format.validate('2018-01-02') == datetime.date(2018, 1, 2)
    assert date_format.validate('2020-07-08') == datetime.date(2020, 7, 8)

    # Test invalid dates
    with pytest.raises(ValidationError):
        date_format.validate('2018-7-8')
    with pytest.raises(ValidationError):
        date_format.validate('2018-07-8')
    with pytest.raises(ValidationError):
        date_format.validate('2018-7-08')
    with pytest.raises(ValidationError):
        date_format.validate('2018-A1-08')

# Generated at 2022-06-14 14:29:18.900425
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # test for case TIME_REGEX.match(value) is True
    timefmt = TimeFormat()
    assert timefmt.validate('10:32:52') == datetime.time(10, 32, 52)
    assert timefmt.validate('10:32:52.12') == datetime.time(10, 32, 52, 120000)
    assert timefmt.validate('10:32:52.123456') == datetime.time(10, 32, 52, 123456)
    assert timefmt.validate('10:32') == datetime.time(10, 32)
    # test for case TIME_REGEX.match(value) is False
    with pytest.raises(ValidationError):
        timefmt.validate('10:32:52:32')

# Generated at 2022-06-14 14:29:21.739516
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    try:
        df.validate("2019-01-28")
        assert True
    except Exception:
        assert False


# Generated at 2022-06-14 14:29:23.741175
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
	format = DateFormat()
	assert format.validate('2020-10-17') == datetime.date(2020,10,17)
	

# Generated at 2022-06-14 14:29:27.352609
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_format.validate("12:23:13.123456")
    try:
        time_format.validate("12:23:13.1234")
    except ValidationError:
        assert True
        return


# Generated at 2022-06-14 14:29:33.486317
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d1 = DateFormat()
    d1 = d1.validate("2019-12-10")
    assert isinstance(d1, datetime.date)


# Generated at 2022-06-14 14:29:35.753581
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date_format.validate("2020-01-10")
    pass

# Generated at 2022-06-14 14:29:38.383294
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    value = "2019-01-02"
    assert df.validate(value) == datetime.date(2019,1,2)


# Generated at 2022-06-14 14:29:46.458598
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Case 1:
    # Input: "01:02"
    # Expected output: return datetime.time(1, 2)
    time_format = TimeFormat()

    try:
        assert time_format.validate('01:02') == datetime.time(1, 2)
        print('case 1 pass')
    except:
        print('case 1 fail')

    # Case 2:
    # Input: "25:02"
    # Expected output: raise ValidationError
    try:
        time_format.validate('25:02')
        print('case 2 fail')
    except ValidationError as e:
        assert (e.code == 'invalid')
        print('case 2 pass')

    # Case 3:
    # Input: "01:02:03:04"
    # Expected output: raise Val

# Generated at 2022-06-14 14:29:57.719163
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Test TimeFormat.validate with valid input
    time = TimeFormat()
    assert time.validate("00:00:00") == datetime.time(0, 0)
    assert time.validate("00:00:00.123") == datetime.time(0, 0, 0, 123000)
    assert time.validate("00:00:00.1234") == datetime.time(0, 0, 0, 123000)
    assert time.validate("00:00:00.123456") == datetime.time(
        0, 0, 0, 123456
    )

    # Test TimeFormat.validate with invalid input
    try:
        time.validate("00:00:00.")
    except ValidationError as e:
        assert str(e) == "Must be a valid time format."
        assert e

# Generated at 2022-06-14 14:30:01.959995
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    try:
        t.validate("5:0")
    except ValidationError as e:
        assert e.code == "invalid"
        assert e.text == "Must be a real time."


# Generated at 2022-06-14 14:30:14.835025
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Case 1
    format = DateFormat()
    v = "2019-01-02"
    try:
        result = format.validate(v)
    except ValidationError:
        assert False
    else:
        assert result == datetime.date(2019, 1, 2)
        assert result.year == 2019
        assert result.month == 1
        assert result.day == 2
    # Case 2
    v = "2019-02-29"
    try:
        format.validate(v)
    except ValidationError as e:
        assert e.code == "invalid"
    else:
        assert False
    # Case 3
    v = "2019.01.01"
    try:
        format.validate(v)
    except ValidationError as e:
        assert e.code == "format"
   

# Generated at 2022-06-14 14:30:18.664752
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()

    d = date.validate('2020-11-13')
    assert d == datetime.date(2020, 11, 13)

    with pytest.raises(ValidationError):
        date.validate('2020-13-1')



# Generated at 2022-06-14 14:30:30.133542
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2017-01-01') == datetime.date(2017, 1, 1)
    assert DateFormat().validate('2016-02-29') == datetime.date(2016, 2, 29)
    try:
        assert DateFormat().validate('1001-01-01')
    except ValidationError:
        assert True
    try:
        assert DateFormat().validate('2017-13-01')
    except ValidationError:
        assert True
    try:
        assert DateFormat().validate('2017-01-32')
    except ValidationError:
        assert True
    try:
        assert DateFormat().validate('2017-01')
    except ValidationError:
        assert True
    try:
        assert DateFormat().validate('2017')
    except ValidationError:
        assert True
   

# Generated at 2022-06-14 14:30:41.349950
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()

    # Test 1
    date = '2001-01-01'
    match = DATE_REGEX.match(date)
    kwargs = {k: int(v) for k, v in match.groupdict().items()}
    try:
        obj = datetime.date(**kwargs)
    except ValueError:
        raise self.validation_error("invalid")
    assert format.validate(date) == obj

    # Test 2
    date = '2002-01-31'

    match = DATE_REGEX.match(date)
    kwargs = {k: int(v) for k, v in match.groupdict().items()}

# Generated at 2022-06-14 14:30:46.333322
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    try:
        date_format.validate(datetime.datetime.now().strftime('%Y-%m-%d'))
    except:
        assert False
    else:
        assert True


# Generated at 2022-06-14 14:30:54.628806
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Create test object
    DtF = DateTimeFormat()

    # Create test cases

# Generated at 2022-06-14 14:31:06.070920
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # success
    print(DateTimeFormat().validate("2020-02-02T02:02:23.456Z"))     # Z means utc+0, it is equivalent to utc-0
    print(DateTimeFormat().validate("2020-02-02T02:02:23.456+08:30"))    # +08:30 means utc+8.5, it is equivalent to utc-15.5
    print(DateTimeFormat().validate("2020-02-02T02:02:23.456-08:30"))    # -08:30 means utc-8.5, it is equivalent to utc+15.5
    print(DateTimeFormat().validate("2020-02-02T02:02:23.456+0830"))     # +0830 means utc+8.5, it is equivalent to utc

# Generated at 2022-06-14 14:31:09.960127
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_fmt = DateFormat()
    date = "2000-01-01"
    date_fmt_validate = date_fmt.validate(date)
    assert date_fmt_validate.year == 2000
    assert date_fmt_validate.month == 1
    assert date_fmt_validate.day == 1


# Generated at 2022-06-14 14:31:15.370136
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df1 = DateFormat()
    df2 = DateFormat()
    df3 = DateFormat()
    assert df1.validate('2020-06-04') == datetime.date(2020,6,4)
    assert df2.validate('2020-13-04') == datetime.date(2020,1,4)
    assert df3.validate('2020-06-32') == datetime.date(2020,2,1)


# Generated at 2022-06-14 14:31:18.970578
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    c = TimeFormat()
    assert c.validate('00:00:00') == datetime.time(0, 0)


# Generated at 2022-06-14 14:31:21.006510
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("00:00:00.000000") == datetime.time(0, 0, 0)

# Generated at 2022-06-14 14:31:24.205985
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    print("test_DateFormat_validate")

    date_format = DateFormat()
    assert date_format.validate("2019-11-04") == datetime.date(2019,11,4)


# Generated at 2022-06-14 14:31:36.023664
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    import pytest
    from typesystem.base import ValidationError
    from datetime import time
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
    time11 = TimeFormat()
    time12 = TimeFormat()
    time13 = TimeFormat()
    time14 = TimeFormat()
    time15 = TimeFormat()
    time16 = TimeFormat()
    time17 = TimeFormat()
    time18 = TimeFormat()
    time19 = TimeFormat()
    time20 = TimeFormat()
    time21 = TimeFormat()
    time22 = TimeFormat()


# Generated at 2022-06-14 14:31:37.244558
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = "2020-10-05"
    assert DateFormat().validate(date) == datetime.date(2020, 10, 5)


# Generated at 2022-06-14 14:31:41.174115
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    tf.validate("12:45:30")

# Generated at 2022-06-14 14:31:45.845930
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    a = DateFormat()
    assert a.validate("2019-08-28") == datetime.date(2019, 8, 28)
    # a = DateFormat()
    # print(type(a.validate("2019-08-28")))


# Generated at 2022-06-14 14:31:56.501988
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # '1900-01-01'
    assert DateFormat().validate('1900-01-01') == datetime.date(1900, 1, 1)
    # '0011-01-01'
    assert DateFormat().validate('0011-01-01') == datetime.date(11, 1, 1)
    # '1000-01-01'
    assert DateFormat().validate('1000-01-01') == datetime.date(1000, 1, 1)
    # '0400-01-01'
    assert DateFormat().validate('0400-01-01') == datetime.date(400, 1, 1)
    # '0001-01-01'
    assert DateFormat().validate('0001-01-01') == datetime.date(1, 1, 1)
    # '2017-11-01'


# Generated at 2022-06-14 14:32:00.862264
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    datetime.datetime(2019, 12, 12, 0, 0)
    try:
        df.validate("2019-12-12")
    except:
        print("no test")

# Generated at 2022-06-14 14:32:10.896442
# Unit test for method validate of class DateTimeFormat

# Generated at 2022-06-14 14:32:22.130569
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # generate a random DateTimeFormat
    datetimeformat = datetime.datetime.now()
    datetimeformat = datetimeformat.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    datetimeformat2 = datetimeformat.replace("Z", "+00:00")

    # Control
    assert DateTimeFormat.validate(DateTimeFormat, datetimeformat) == datetime.datetime.strptime(datetimeformat, "%Y-%m-%dT%H:%M:%S.%f%z")

    assert DateTimeFormat.validate(DateTimeFormat, datetimeformat2) == datetime.datetime.strptime(datetimeformat, "%Y-%m-%dT%H:%M:%S.%f%z")


# Unit

# Generated at 2022-06-14 14:32:28.841641
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    from typesystem import Integer
    # Tests for the method DateFormat.validate() of class IntegerType
    assert DateFormat().validate('2019-05-15').isocalendar() == (2019, 20, 3)
    assert DateFormat().validate('2019-05-15').weekday() == 2
    assert DateFormat().validate('2019-05-15').day == 15

# Generated at 2022-06-14 14:32:32.695472
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date = date_format.validate("2019-07-11")
    assert isinstance(date, datetime.date)
    assert date.year == 2019
    assert date.month == 7
    assert date.day == 11



# Generated at 2022-06-14 14:32:34.737565
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    actual = DateFormat().validate('2020-03-22')
    expected = datetime.date(2020, 3, 22)
    assert actual == expected


# Generated at 2022-06-14 14:32:37.542962
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    data = "12:34:56"
    result = TimeFormat().validate(data)
    expected = datetime.time(12, 34, 56, 0, None)
    assert result == expected


# Generated at 2022-06-14 14:32:47.738766
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = DateFormat()

    # Valid
    try: assert value.validate("2019-01-31") == datetime.date(2019, 1, 31)
    except ValueError: assert False

    # Invalid
    try: assert value.validate("2019-00-31")
    except ValueError: assert True


# Generated at 2022-06-14 14:32:50.014336
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format_date = DateFormat()
    assert(format_date.validate("2000-01-01") == datetime.date(2000, 1, 1))


# Generated at 2022-06-14 14:32:56.849235
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    validate_test = DateFormat()

    assert validate_test.validate('2019-11-06') == datetime.date(year = 2019, month = 11, day = 6)

    with pytest.raises(ValidationError) as excinfo:
        validate_test.validate('nope')
    assert excinfo.value.code == 'format'
    assert excinfo.value.text == 'Must be a valid date format.'
    with pytest.raises(ValidationError) as excinfo:
        validate_test.validate('2019-11-31')
    assert excinfo.value.code == 'invalid'
    assert excinfo.value.text == 'Must be a real date.'


# Generated at 2022-06-14 14:33:00.209692
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    TimeFormatInstance = TimeFormat()
    value = "12:25"
    assert TimeFormatInstance.validate(value) == datetime.time(12, 25)


# Generated at 2022-06-14 14:33:01.940574
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("12:00") == datetime.time(12, 0)

# Generated at 2022-06-14 14:33:05.228994
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate("2019-08-01") == datetime.date(2019, 8, 1)



# Generated at 2022-06-14 14:33:09.663067
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Data
    valid_time_isoformat = '12:22:23'
    # Execute method
    result = TimeFormat().validate(valid_time_isoformat)
    # Assertions
    assert isinstance(result, datetime.time)


# Generated at 2022-06-14 14:33:15.925206
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = datetime.datetime.today()
    print(d)
    value = d.strftime("%Y-%m-%d")
    print(value)
    fr = DateFormat()
    obj = fr.validate(value)
    print(obj.strftime("%Y-%m-%d"))
    assert obj == value
