

# Generated at 2022-06-14 14:23:35.168905
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    dt = datetime.time(12, 30)
    tf1 = TimeFormat()
    assert tf1.validate('12:30') == dt


# Generated at 2022-06-14 14:23:43.159682
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    # Testing null input
    res = UUIDFormat().validate(None)
    assert res == None
    # Testing invalid input
    with pytest.raises(ValidationError):
        UUIDFormat().validate("InvalidInput")
    # Testing correct input
    res = UUIDFormat().validate("8b6664a7-5c5e-4d2b-8d5f-53c8977c9a7a")
    assert isinstance(res, uuid.UUID)


# Generated at 2022-06-14 14:23:47.214974
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    format_object = DateTimeFormat()
    assert format_object.serialize(datetime.datetime(2012, 12, 12, 12, 12, 12, 12)) == "2012-12-12T12:12:12.000012"


# Generated at 2022-06-14 14:23:50.710035
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    mock_data = {}
    mock_data['second']='5'
    mock_data['microsecond']='5'
    mock_data['minute']='5'
    mock_data['hour']='5'

    def mock_groupdict():
        return mock_data

    def mock_match():
        return mock_groupdict

    def mock_TIME_REGEX_match():
        return mock_match

    TIME_REGEX_match = TimeFormat.TIME_REGEX.match
    TimeFormat.TIME_REGEX.match = mock_TIME_REGEX_match

    time = TimeFormat()
    time.validate('5:5:5.5')
    TimeFormat.TIME_REGEX.match = TIME_REGEX_match

# Generated at 2022-06-14 14:23:53.808944
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    instance = DateFormat()
    value = '20190307'
    result = instance.validate(value)
    assert result


# Generated at 2022-06-14 14:24:02.931560
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # datetime.datetime(2000, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().serialize(datetime.datetime(2000, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)) == "2000-01-01T00:00:00+00:00"
    assert DateTimeFormat().serialize(datetime.datetime(2000, 1, 1, 0, 0, 0)) == "2000-01-01T00:00:00+00:00"
    # datetime.datetime(2000, 1, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:24:04.716602
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2020-03-14') == datetime.date(2020, 3, 14)


# Generated at 2022-06-14 14:24:08.081941
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date = datetime.date(year=2019, month=3, day=12)
    format = DateFormat()
    assert format.serialize(date) == "2019-03-12"


# Generated at 2022-06-14 14:24:14.281926
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate('12:00') == datetime.time(12, 0, 0)
    assert time.validate('12:00:00') == datetime.time(12, 0, 0)
    assert time.validate('12:00:00.000000') == datetime.time(12, 0, 0)
    assert time.validate('12:00:00.42') == datetime.time(12, 0, 0, 420000)


# Generated at 2022-06-14 14:24:25.076757
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    test_case_1_input = '2020-07-01T20:00:00Z'
    test_case_1_result = {
        'day': 1,
        'hour': 20,
        'microsecond': 0,
        'minute': 0,
        'month': 7,
        'second': 0,
        'tzinfo': 'Z',
        'year': 2020
    }
    test_case_2_input = '2020-07-01T20:00:00-07:00'
    test_case_2_result = {
        'day': 1,
        'hour': 20,
        'microsecond': 0,
        'minute': 0,
        'month': 7,
        'second': 0,
        'tzinfo': '-07:00',
        'year': 2020
    }
   

# Generated at 2022-06-14 14:24:32.265285
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_obj = datetime.datetime(2019, 11, 12, 12, 0, 0)
    date_obj = date_obj.astimezone(datetime.timezone.utc)
    date_format = DateTimeFormat()
    serialized_date = date_format.serialize(date_obj)
    assert serialized_date == "2019-11-12T12:00:00+00:00"
    assert type(serialized_date) == str


# Generated at 2022-06-14 14:24:36.194419
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()
    assert format.validate("2020-04-19T11:03:10Z") == datetime.datetime(2020, 4, 19, 11, 3, 10, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:24:41.998717
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate('2016-07-05') == datetime.date(2016, 7, 5)
    try:
        date_format.validate('2016-13-05')
    except ValidationError:
        assert True
    try:
        date_format.validate('2016-07-32')
    except ValidationError:
        assert True


# Generated at 2022-06-14 14:24:46.044377
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    DateTimeFormat().validate("2020-04-21T14:40:00Z")

    with pytest.raises(ValidationError):
        DateTimeFormat().validate("2020-04-21T14:40:00Z")

# Generated at 2022-06-14 14:24:48.392258
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    a = DateFormat()
    
    assert a.validate("2020-11-02") == datetime.date(2020,11,2)
    

# Generated at 2022-06-14 14:24:59.206563
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format = DateTimeFormat()
    result = date_time_format.validate('2019-05-30T19:20:30.456789+01:00')
    assert result.isoformat() == '2019-05-30T19:20:30.456789+01:00'
    result = date_time_format.validate('2019-05-30T19:20:30.456789-05:00')
    assert result.isoformat() == '2019-05-30T19:20:30.456789-05:00'
    result = date_time_format.validate('2019-05-30T19:20:30+05:00')
    assert result.isoformat() == '2019-05-30T19:20:30+05:00'
    result = date_time

# Generated at 2022-06-14 14:25:08.903483
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    print("\n[UNIT TESTING FOR METHOD validate of class DateTimeFormat]")
    

    # Test 1
    print("[UNIT TESTING] Testing on: 2019-07-21T17:20:00Z")
    try:
        print(DateTimeFormat().validate("2019-07-21T17:20:00Z"))
    except Exception as error:
        print(error)

    # Test 2
    print("[UNIT TESTING] Testing on: 2019-11-10T00:00+08:00")
    try:
        print(DateTimeFormat().validate("2019-11-10T00:00+08:00"))
    except Exception as error:
        print(error)

    # Test 3
    print("[UNIT TESTING] Testing on: 2019-11-10T00:00")
   

# Generated at 2022-06-14 14:25:13.069601
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("13:37") == datetime.time(hour=13, minute=37)
    assert TimeFormat().validate("12:34:55") == datetime.time(
        hour=12, minute=34, second=55
    )
    assert TimeFormat().validate("12:34:56.789000") == datetime.time(
        hour=12, minute=34, second=56, microsecond=789000
    )



# Generated at 2022-06-14 14:25:23.988531
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    instance_DateTimeFormat=DateTimeFormat()
    #test for year out of range
    validation_error=instance_DateTimeFormat.validate("9999-12-12T23:12:12")
    assert (validation_error.code=='invalid')
    #test for hour out of range
    validation_error=instance_DateTimeFormat.validate("2018-12-12T25:12:12")
    assert (validation_error.code=='invalid')
    #test for leap year
    validation_error=instance_DateTimeFormat.validate("2008-02-30T12:12:12")
    assert (validation_error.code=='invalid')
    #test for case "-" missing

# Generated at 2022-06-14 14:25:32.068756
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_value = datetime.datetime(2020, 1, 10, 7, 17, 18, 645000, datetime.timezone.utc)
    date_value_formatted = '2020-01-10T07:17:18.645000+00:00'
    assert date_value.isoformat() == date_value_formatted
    date_value_formatted = '2020-01-10T07:17:18.645000Z'
    date_value_serialized = DateTimeFormat().serialize(date_value)
    print(date_value_serialized)
    assert date_value_serialized == date_value_formatted


# Generated at 2022-06-14 14:25:39.228364
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uid = uuid.uuid4()
    string_uid = str(uid)
    print(string_uid)
    uuid_format = UUIDFormat()
    print(uuid_format.validate(string_uid))
    assert uuid_format.validate(string_uid) == uid, 'UUIDFormat validate is wrong!'

# Generated at 2022-06-14 14:25:48.409970
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_format.validate("12:34:00.000001")
    time_format.validate("12:34:00.00001")
    time_format.validate("12:34:00.0001")
    time_format.validate("12:34:00.001")
    time_format.validate("12:34:00.01")
    time_format.validate("12:34:00.1")
    time_format.validate("12:34:00")
    time_format.validate("12:34")


# Generated at 2022-06-14 14:25:59.683166
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.formats import TimeFormat
    time = TimeFormat()
    result = time.validate('05:34:00.000000')
    assert result.isoformat() == '05:34:00'
    time = TimeFormat()
    result = time.validate('12:00:00') 
    assert result.isoformat() == '12:00:00'
    time = TimeFormat()
    result = time.validate('14:05:00') 
    assert result.isoformat() == '14:05:00'
    time = TimeFormat()
    result = time.validate('23:00:00') 
    assert result.isoformat() == '23:00:00'
    time = TimeFormat()
    result = time.validate('00:00:00') 

# Generated at 2022-06-14 14:26:07.374390
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
	print(" ")
	print("Test of the method validate of class UUIDFormat")
	print(" ")

	print(" ")
	print("Test with value = '0075a6c9-98a1-4fd5-b453-4c2c92a3230b' (valid UUID)")
	formatUUID = UUIDFormat()
	try:
		print(formatUUID.validate("0075a6c9-98a1-4fd5-b453-4c2c92a3230b"))
		print("Result -> correct")
		print("Test OK")
	except:
		print("Result -> error")
		print("Test ERROR")
	print(" ")

	print(" ")

# Generated at 2022-06-14 14:26:13.034489
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uf=UUIDFormat()
    assert(uf.validate('3a3f3c18-fad8-4422-bab0-b1233b9d9d8c')==uuid.UUID('3a3f3c18-fad8-4422-bab0-b1233b9d9d8c'))

# Generated at 2022-06-14 14:26:16.902540
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    value = "12:20"
    time = TimeFormat()
    test = time.validate(value)
    assert test.hour == 12
    assert test.minute == 20
    assert test.microsecond == 0
    assert test.second == 0
    assert test.tzinfo == None


# Generated at 2022-06-14 14:26:18.653836
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    errors = {"format": "Must be valid UUID format."}

# Generated at 2022-06-14 14:26:22.095902
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    tf = TimeFormat()
    time = datetime.time()
    assert isinstance(tf.serialize(time), str) == True


# Generated at 2022-06-14 14:26:25.465073
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time_format = TimeFormat()
    result = time_format.serialize(datetime.time(12, 5, 30, tzinfo=datetime.timezone.utc))
    assert result == '12:05:30+00:00'

# Generated at 2022-06-14 14:26:30.253270
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(1,2,3)
    time_format = TimeFormat()
    assert time_format.serialize(time) == "01:02:03"

# Generated at 2022-06-14 14:26:34.133750
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    df.validate('2019-12-01')


# Generated at 2022-06-14 14:26:41.176045
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_hour = time_format.validate('13:00:00')
    assert time_hour.hour == 13
    time_hour_sec = time_format.validate('13:00:00.000000')
    assert time_hour_sec.hour == 13
    time_hour_sec_micro = time_format.validate('13:00:00.000001')
    assert time_hour_sec_micro.hour == 13
    time_hour_sec_micro = time_format.validate('13:00:00.000001')
    assert time_hour_sec_micro.hour == 13

        

# Generated at 2022-06-14 14:26:47.223752
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Test without a microsecond.
    value = "20:30:45"
    format = TimeFormat()
    assert isinstance(format.validate(value), datetime.time)
    # Test with a microsecond.
    value = "20:30:45.123456"
    format = TimeFormat()
    assert isinstance(format.validate(value), datetime.time)

    # Test with invalid value.
    value = "10:00,00"
    format = TimeFormat()
    with pytest.raises(ValidationError):
        format.validate(value)

# Generated at 2022-06-14 14:26:56.938571
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format = TimeFormat()
    assert datetime.time(12, 11, 59, 0) == format.validate('12:11:59')
    with pytest.raises(ValidationError):
        format.validate('12:11:59.12')
    with pytest.raises(ValidationError):
        format.validate('31:11:59')
    with pytest.raises(ValidationError):
        format.validate('12:21:59')
    with pytest.raises(ValidationError):
        format.validate('12:11:69')


# Generated at 2022-06-14 14:26:59.419182
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    input_value = '23:59:59'
    assert time.validate(input_value) == datetime.time(23, 59, 59)

# Generated at 2022-06-14 14:27:01.219033
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("11:15:30")

# Generated at 2022-06-14 14:27:06.484333
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    obj = TimeFormat().validate('12:32:53.345999')
    assert isinstance(obj, datetime.time)
    assert obj.hour == 12
    assert obj.minute == 32
    assert obj.second == 53
    assert obj.microsecond == 345999

# Generated at 2022-06-14 14:27:07.782279
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate('2019-09-07') == datetime.date(2019, 9, 7)

# Generated at 2022-06-14 14:27:17.005636
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    arg = "00:02:03.123450"
    assert time.validate(arg).hour == 00

# Generated at 2022-06-14 14:27:23.198012
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # type: () -> None
    obj = TimeFormat()
    assert datetime.time(17, 30) == obj.validate("17:30")
    assert datetime.time(17, 30, 30) == obj.validate("17:30:30")
    assert datetime.time(17, 30, 30, 60000) == obj.validate("17:30:30.06")
    assert datetime.time(17, 30, 30, 60100) == obj.validate("17:30:30.0601")
    assert datetime.time(17, 30, 30, 60000) == obj.validate("17:30:30.06000")

# Generated at 2022-06-14 14:27:35.335518
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_format = DateTimeFormat()
    date_format.validate("2019-04-15T12:23:39Z")
    date_format.validate("2019-04-15T04:23:39+08:00")
    date_format.validate("2019-04-15T04:23:39")
    date_format.validate("2019-04-15T04:23:39.123")
    date_format.validate("2019-04-15T04:23:39.123456")
    date_format.validate("2019-04-15T04:23:39+08")
    date_format.validate("2019-04-15T04:23:39-08:30")



# Generated at 2022-06-14 14:27:43.552356
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Test 1
    # is_native_type = False
    dateTimeFormat = DateTimeFormat()
    value = '11 aa'
    result = dateTimeFormat.validate(value)
    assert True == isinstance(result, ValidationError) # test if the value return is a ValidationError type
    assert result.code == "format" # test if the code contains the error 'format'
    assert result.text == "Must be a valid datetime format."

    # Test 2
    # is_native_type = False
    dateTimeFormat = DateTimeFormat()
    value = '2019-11-11T11:11:11.123456-11'
    result = dateTimeFormat.validate(value)
    assert True == isinstance(result, ValidationError) # test if the value return is a ValidationError type
    assert result

# Generated at 2022-06-14 14:27:50.713831
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    assert dateFormat.validate("2019-09-03") == datetime.datetime(2019, 9, 3).date()
    # assert dateFormat.validate("20190903") == ValidationError
    # assert dateFormat.validate(12345) == ValidationError
    assert dateFormat.validate("2010-13-01") == ValidationError
    assert dateFormat.validate("2010-00-01") == ValidationError
    assert dateFormat.validate("2010-01-00") == ValidationError
    assert dateFormat.validate("2010-01-32") == ValidationError
    assert dateFormat.validate("2010-02-29") == ValidationError
    assert dateFormat.validate("2010-04-31") == ValidationError


# Generated at 2022-06-14 14:28:01.941724
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # c1
    d1 = DateFormat()
    assert d1.validate("2019-05-27") == datetime.date(2019, 5, 27)
    assert d1.validate("2019-05-27") != datetime.date(2019, 2, 27)

    # c2
    d2 = DateFormat()
    assert d2.validate("2019-05-00") == datetime.date(2019, 5, 1)
    assert d2.validate("2019-05-00") != datetime.date(2019, 2, 27)

    # c3
    d3 = DateFormat()
    assert d3.validate("1111-11-11") == datetime.date(1111, 11, 11)

# Generated at 2022-06-14 14:28:13.246044
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    obj = DateTimeFormat()

    assert repr(obj.validate('2019-10-15T04:30:00Z')) == 'datetime.datetime(2019, 10, 15, 4, 30, tzinfo=datetime.timezone.utc)'
    assert repr(obj.validate('2019-10-15T04:30:00+00:00')) == 'datetime.datetime(2019, 10, 15, 4, 30, tzinfo=datetime.timezone.utc)'
    assert repr(obj.validate('2019-10-15T04:30:00-05:00')) == 'datetime.datetime(2019, 10, 15, 4, 30, tzinfo=datetime.timedelta(seconds=-18000))'

# Generated at 2022-06-14 14:28:25.682195
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Case 1
    res_1 = DateFormat().validate("2020-04-20")
    assert res_1 == "2020-04-20"
    # Case 2
    with pytest.raises(Exception) as error:
        res_2 = DateFormat().validate("2020-14-20")
    # Case 3
    with pytest.raises(Exception) as error:
        res_3 = DateFormat().validate("2020-04-40")
    # Case 4
    with pytest.raises(Exception) as error:
        res_4 = DateFormat().validate("2010-04-20")
    # Case 5
    with pytest.raises(Exception) as error:
        res_5 = DateFormat().validate("2020")
    # Case 6

# Generated at 2022-06-14 14:28:30.602989
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dt = DateFormat()
    date = datetime.date(2020, 4, 2)
    date_str = '2020-04-02'
    assert date == dt.validate(date_str)


# Generated at 2022-06-14 14:28:34.044788
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date = date_format.validate("2019-07-12")
    assert date.year == 2019
    assert date.month == 7
    assert date.day == 12



# Generated at 2022-06-14 14:28:38.604739
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time = DateTimeFormat()
    test_input = '2019-02-01T12:30:40Z'
    try:
        datetime.datetime(2019,2,1,12,30,40,0)
        assert date_time.validate(test_input)
    except ValueError:
        raise AssertionError("Date format is not valid")

# Generated at 2022-06-14 14:28:50.479139
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime_format = DateTimeFormat()
    assert datetime_format.validate("2018-11-2T14:30:05+00:00") == datetime.datetime(2018, 11, 2, 14, 30, 5, tzinfo=datetime.timezone.utc)
    assert datetime_format.validate("2018-11-2T14:30:05-01:30") == datetime.datetime(2018, 11, 2, 14, 30, 5, tzinfo=datetime.timezone(datetime.timedelta(hours=-1, minutes=-30)))
    assert datetime_format.validate("2018-11-2T14:30:05Z") == datetime.datetime(2018, 11, 2, 14, 30, 5, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:28:54.043857
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_format.validate("12:34:56.123456")

# Generated at 2022-06-14 14:28:56.207914
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateformat = DateFormat()
    date = dateformat.validate("2019-11-07")
    assert date == datetime.date(2019, 11, 7)


# Generated at 2022-06-14 14:29:04.955064
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    """
    - Create an instance of TimeFormat class
    - Check that method validate of the class returns that '00:00:00' is a valid format
    - Check that method validate of the class returns that '00:00:00.000000' is a valid format
    - Check that method validate of the class returns that '00:00' is a valid format
    """
    time_format = TimeFormat()
    time_format.validate('00:00:00')
    time_format.validate('00:00:00.000000')
    time_format.validate('00:00')


# Generated at 2022-06-14 14:29:06.939464
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    df.validate('2000-12-31')



# Generated at 2022-06-14 14:29:17.702039
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime1 = '2020-08-13T00:00:00.000000Z'
    datetime2 = '2020-08-13T00:00:00Z'
    datetime3 = '2020-08-13T00:00:00.000000+00:00'
    datetime4 = '2020-08-13T00:00:00+00:00'
    datetime5 = '2020-08-13T00:00:00.000000+0000'
    datetime6 = '2020-08-13T00:00:00+0000'
    datetime7 = '2020-08-13T00:00:00.000000-00:00'
    datetime8 = '2020-08-13T00:00:00-00:00'

# Generated at 2022-06-14 14:29:20.212688
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = DateFormat()
    assert d.validate("2000-01-01") == datetime.date(2000, 1, 1)


# Generated at 2022-06-14 14:29:28.987193
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    from typesystem.fields import Date

    date = Date()
    date_format = date._format
    
    test_cases = {
    (True, "2019-12-31", datetime.date(2019, 12, 31)),
    (False, "2019-13-01", datetime.date(2019, 12, 31)),
    (False, "2019-12-32", datetime.date(2019, 12, 31))
    }

    for case in test_cases:
        try:
            date_format.validate(case[1])
        except:
            assert not case[0]
            continue
        assert case[0] and date_format.validate(case[1]) == case[2]



# Generated at 2022-06-14 14:29:30.684021
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
  dateformat = DateFormat()
  try:
    dateformat.validate('2020-02-20')
  except Exception as e:
    assert str(e) == 'Must be a real date.'



# Generated at 2022-06-14 14:29:34.591951
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dformat = DateFormat()
    date = dformat.validate('2020-09-11')
    assert date == datetime.date(2020, 9, 11)


# Generated at 2022-06-14 14:29:43.297351
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    tstamp = t.validate("12:55:55")
    assert tstamp == datetime.time(hour=12, minute=55, second=55),\
        "Failed to parse HH:MM:SS with no microseconds"
    tstamp = t.validate("12:55")
    assert tstamp == datetime.time(hour=12, minute=55),\
        "Failed to parse HH:MM with no microseconds"
    tstamp = t.validate("12:55:55.123")
    assert tstamp == datetime.time(hour=12, minute=55, second=55, microsecond=123000),\
        "Failed to parse HH:MM:SS.microseconds"

# Generated at 2022-06-14 14:29:51.064700
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    test_date = datetime.date.today()

    test_format = DateFormat()

    assert test_format.validate(test_date.isoformat()) == test_date



# Generated at 2022-06-14 14:29:54.117149
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    a = DateFormat()
    parsed = a.validate("2019-06-02")
    print(parsed)
    print(type(parsed))


# Generated at 2022-06-14 14:29:57.332607
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    method_test_succ("DateTimeFormat validate")
    method_test_fail("DateTimeFormat validate", "Must be a valid datetime format.")
    method_test_fail("DateTimeFormat validate", "Must be a real datetime.")


# Generated at 2022-06-14 14:30:10.480679
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    #DateFormat instancie
    DateFormat_test = DateFormat()
    DateFormat_test.validate("2020-07-07")
    DateFormat_test.validate("2020-07-07")
    try:
        DateFormat_test.validate("22-07-07")
    except ValidationError as e:
        print("Yes it's there")
    try:
        DateFormat_test.validate("2020-07-44")
    except ValidationError as e:
        print("Yes it's there")
    try:
        DateFormat_test.validate("2020-07-07-07")
    except ValidationError as e:
        print("Yes it's there")

# Generated at 2022-06-14 14:30:20.803672
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format1 = DateFormat()
    value1 = '2019-11-06'
    result1 = format1.validate(value1)
    expected1 = datetime.datetime(2019, 11, 6)
    assert result1 == expected1

    format2 = DateFormat()
    value2 = '2019-11-063'
    try:
        format2.validate(value2)
    except ValidationError as e:
        result2 = e.code
        expected2 = 'format'
        assert result2 == expected2

    format3 = DateFormat()
    value3 = '0019-11-06'
    try:
        format3.validate(value3)
    except ValidationError as e:
        result3 = e.code
        expected3 = 'invalid'
        assert result3 == expected3



# Generated at 2022-06-14 14:30:31.759565
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    from datetime import datetime
    from datetime import date
    from typesystem.base import ValidationError
    from utils.date_time_formats import DateFormat

    test_cases = [
        ['2019-12-12', date(2019, 12, 12)],
        ['2019-02-31', ValidationError],
        ['2019-02-01', date(2019, 2, 1)],
        ['2019-01-01', date(2019, 1, 1)],
        ['2019-12-01', date(2019, 12, 1)],
        ['2019-01-31', date(2019, 1, 31)],
        ['2019-10-31', date(2019, 10, 31)]
    ]


# Generated at 2022-06-14 14:30:37.063491
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    time_value = "12:00:00"
    expected_time = datetime.time(hour=12, minute=0, second=0, microsecond=0, tzinfo=None)
    assert tf.validate(time_value) == expected_time



# Generated at 2022-06-14 14:30:39.233479
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    a = DateFormat()
    assert a.validate('2020-01-01') == datetime.date(2020, 1, 1)


# Generated at 2022-06-14 14:30:41.349708
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    f = DateFormat

# Generated at 2022-06-14 14:30:44.324614
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    validator = DateFormat()
    value = "2020-09-26"
    assert isinstance(validator.validate(value), datetime.date)


# Generated at 2022-06-14 14:30:53.004244
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    with pytest.raises(ValidationError, match = "Must be a valid date format."):
        df.validate("abc")
    with pytest.raises(ValidationError, match = "Must be a real date."):
        df.validate("2020-99-99")
    df.validate('2020-01-01') == '2020-01-01'

# Generated at 2022-06-14 14:30:55.646958
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date = date_format.validate('2009-8-23')
    assert date.year == 2009
    assert date.month == 8
    assert date.day == 23

# Generated at 2022-06-14 14:31:00.783518
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    print(DateTimeFormat().validate('2018-12-31T23:59:59.999999Z'))
    print(DateTimeFormat().validate('2011-12-31T23:59:59.999999'))

test_DateTimeFormat_validate()

# Generated at 2022-06-14 14:31:05.855624
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # test1: tests a valid time format
    format_date1 = DateFormat()
    format_date1.validate("2005-10-20")

    # test2: tests an invalid time format
    format_date2 = DateFormat()
    with pytest.raises(ValidationError):
        format_date2.validate("10/20/2005")


# Generated at 2022-06-14 14:31:09.775832
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    value1 = time_format.validate("23:59:59")
    assert isinstance(value1, datetime.time)  # type: ignore
    value2 = time_format.validate("23:59:59.999999")
    assert isinstance(value2, datetime.time)  # type: ignore


# Generated at 2022-06-14 14:31:11.825098
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    df.validate("1998-01-02")


# Generated at 2022-06-14 14:31:17.806682
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    m_TimeFormat = TimeFormat()
    assert m_TimeFormat.validate('10:11') == datetime.time(10, 11, 0)
    assert m_TimeFormat.validate('10:11:52') == datetime.time(10, 11, 52)
    assert m_TimeFormat.validate('10:11:52.000000') == datetime.time(10, 11, 52, 0)
    assert m_TimeFormat.validate('10:11:52.00') == datetime.time(10, 11, 52, 0)



# Generated at 2022-06-14 14:31:20.958890
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    value = dateFormat.validate('2020-03-31')
    assert value == datetime.date(2020, 3, 31)

# Generated at 2022-06-14 14:31:30.212071
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = datetime.date(2019, 1, 1)

    string = '2019-01-0'
    expected = False
    assert not DATE_REGEX.match(string)
    assert DATE_REGEX.match(string) == expected

    string = '2019-01-1'
    expected = True
    assert DATE_REGEX.match(string) == expected

    string = '2019-01-01'
    expected = True
    assert DATE_REGEX.match(string) == expected

    string = '2019-1-01'
    expected = True
    assert DATE_REGEX.match(string) == expected

    string = '2019-01-1'
    expected = True
    assert DATE_REGEX.match(string) == expected

    string = '2019-1-1'
    expected = True

# Generated at 2022-06-14 14:31:34.185233
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date_format.validate('2016-01-04')
    date_format.validate('2016-12-04')
    date_format.validate('2016-11-01')


# Generated at 2022-06-14 14:31:54.292540
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Test if format is correct
    assert TimeFormat.validate('12:12:12') == datetime.time(12, 12, 12, 0)
    assert TimeFormat.validate('12:12') == datetime.time(12, 12, 0, 0)
    assert TimeFormat.validate('12') == datetime.time(12, 0, 0, 0)
    # Test if format is incorrect
    with pytest.raises(ValidationError):
        TimeFormat.validate('12:12:12:'), 'Must be a valid time format.'
    with pytest.raises(ValidationError):
        TimeFormat.validate('12:12:12.12345678'), 'Must be a valid time format.'
    # Test if values are incorrect
    with pytest.raises(ValidationError):
        TimeFormat.validate

# Generated at 2022-06-14 14:31:56.770635
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    fmt = DateFormat()
    # Validate for valid date format
    assert fmt.validate("2019-11-02") == datetime.date(2019, 11, 2)
    # Validate for invalid date format
    with pytest.raises(ValidationError):
        fmt.validate("2019-11-32")

# Generated at 2022-06-14 14:32:08.524604
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    res = tf.validate("12:00:00.123456")
    assert (res == datetime.time(12, 0, 0, 123456))
    res = tf.validate("00:00:00.123456")
    assert (res == datetime.time(0, 0, 0, 123456))
    res = tf.validate("00:00:00.123")
    assert (res == datetime.time(0, 0, 0, 123000))
    res = tf.validate("23:59:59.999999")
    assert (res == datetime.time(23, 59, 59, 999999))
    res = tf.validate("23:59:59.999999")
    assert (res == datetime.time(23, 59, 59, 999999))

# Generated at 2022-06-14 14:32:10.032850
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    with pytest.raises(KeyError):
        DateFormat.validate("2019-03-03")


# Generated at 2022-06-14 14:32:21.439520
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
	date_format = DateFormat()
	#validate
	try:
		date_format.validate("1998-08-28")
	except ValidationError:
		assert False
	try:
		date_format.validate("1998-07-11")
	except ValidationError:
		assert False
	try:
		date_format.validate("1998-08-29")
	except ValidationError:
		assert False
	try:
		date_format.validate("2100-12-31")
	except ValidationError:
		assert False
	try:
		date_format.validate("2000-02-29")
	except ValidationError:
		assert False

# Generated at 2022-06-14 14:32:25.905078
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2018-12-31") == datetime.date(year=2018, month=12, day=31)
    import pytest
    with pytest.raises(ValidationError):
        DateFormat().validate("2018-02-31")


# Generated at 2022-06-14 14:32:36.905400
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.base import Field
    
#    class TimeField(Field):
#        def __init__(self, *args, **kwargs):
#            kwargs.setdefault('format', 'time')
#            super().__init__(*args, **kwargs)
#
#        def validate(self, value: typing.Any) -> typing.Union[datetime.time, ValidationError]:
#            if value is None:
#                if self.required:
#                    raise ValidationError(code="required", text="This field is required.")
#                return None
#            return self.format.validate(value)

    time_field = Field(format='time')

    assert time_field.format.validate('21:23:22') == datetime.time(hour=21,minute=23,second=22)
   

# Generated at 2022-06-14 14:32:40.591131
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Set up test fixture:
    df = DateFormat()
    # Invoke the SUT:
    result = df.validate('2019-12-8')
    # Verify the result:
    assert result.isoformat()=='2019-12-08'


# Generated at 2022-06-14 14:32:51.430986
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
	date1 = '2014-09-05'
	assert DateFormat().validate(date1) == datetime.date(2014, 9, 5)
	date2 = '2014-9-05'
	assert DateFormat().validate(date2) == datetime.date(2014, 9, 5)
	date3 = '14-09-05'
	assert DateFormat().validate(date3) == datetime.date(2014, 9, 5)
	date4 = '14-9-05'
	assert DateFormat().validate(date4) == datetime.date(2014, 9, 5)
	date5 = '2014-00-00'
	assert DateFormat().validate(date5) == datetime.date(2014, 1, 1)
	date6 = 'abc'
	assert DateFormat().validate(date6)

# Generated at 2022-06-14 14:33:04.518320
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # second is not an integer
    with pytest.raises(ValidationError):
        TimeFormat().validate("31:15:1.2")

    # hour is not an integer
    with pytest.raises(ValidationError):
        TimeFormat().validate("aa:15:1.2")

    # hour is less than 0
    with pytest.raises(ValidationError):
        TimeFormat().validate("-1:15:1.2")

    # hour is greater than 24
    with pytest.raises(ValidationError):
        TimeFormat().validate("99:15:1.2")

    # minute is not an integer
    with pytest.raises(ValidationError):
        TimeFormat().validate("24:0x:1.2")

    # minute is not between 0 and 60

# Generated at 2022-06-14 14:33:15.243017
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    date.validate("2019-01-02")
    date.validate("2019-01-2")


# Generated at 2022-06-14 14:33:24.394790
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from pdb import set_trace
    set_trace()
    tf = TimeFormat()
    t = '11:42'
    assert tf.validate(t).strftime('%H:%M') == t
    t = '11:42:00'
    assert tf.validate(t).strftime('%H:%M:%S') == t
    t = '11:42:00.000111'
    assert tf.validate(t).strftime('%H:%M:%S.%f') == t
    t = '11:42:00.000111111'
    assert tf.validate(t).strftime('%H:%M:%S.%f') == '11:42:00.000111'
    t = '11:42:00.000001111'
    assert tf.valid