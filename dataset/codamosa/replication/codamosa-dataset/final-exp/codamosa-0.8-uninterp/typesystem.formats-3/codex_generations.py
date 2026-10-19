

# Generated at 2022-06-14 14:23:36.335823
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate("01:10:01") == datetime.time(1, 10, 1)
    assert time.validate("15:01") == datetime.time(15, 1)
    assert time.validate("01:10:01.17") == datetime.time(1, 10, 1, 170000)
    assert time.validate("01:10:01.17") == datetime.time(1, 10, 1, 170000)
    assert time.validate("01:10:01.123456") == datetime.time(1, 10, 1, 123456)


# Generated at 2022-06-14 14:23:41.889517
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate("2019-12-10") == datetime.date(year=2019, month=12, day=10)
    assert df.validate("2019-12-99") == datetime.date(year=2019, month=12, day=99)


# Generated at 2022-06-14 14:23:53.708151
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # case 1: valid time
    assert str(TimeFormat().validate("10:15:30")) == "10:15:30"
    # case 2: invalid time
    try:
        TimeFormat().validate("13:65")
        raise Exception("Test failed")
    except ValidationError as ve:
        assert ve.code == "invalid"
    # case 3: invalid format
    try:
        TimeFormat().validate("7:8:9:10")
        raise Exception("Test failed")
    except ValidationError as ve:
        assert ve.code == "format"
    # case 4: invalid format
    try:
        TimeFormat().validate("-7:8")
        raise Exception("Test failed")
    except ValidationError as ve:
        assert ve.code == "format"

# Generated at 2022-06-14 14:24:02.598698
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test the case without exception
    value = DateFormat().validate("2019-10-11")
    assert isinstance(value, datetime.date)
    assert value.year == 2019
    assert value.month == 10
    assert value.day == 11

    # Test the case with format exception
    with pytest.raises(ValidationError) as e:
        value = DateFormat().validate("a2019-10-11")
    assert str(e.value) == "Must be a valid date format."

    # Test the case with value exception
    with pytest.raises(ValidationError) as e:
        value = DateFormat().validate("2019-13-11")
    assert str(e.value) == "Must be a real date."



# Generated at 2022-06-14 14:24:08.574200
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuidFormat = UUIDFormat()
    assert uuidFormat.validate('a5c38a1a-f8c5-4f5a-95e9-9ce902f12a63') == uuid.UUID('a5c38a1a-f8c5-4f5a-95e9-9ce902f12a63')
    assert uuidFormat.validate('3A3063A4-D22B-4AAE-83E7-E87DC660A7A8') == uuid.UUID('3A3063A4-D22B-4AAE-83E7-E87DC660A7A8')

# Generated at 2022-06-14 14:24:09.967828
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
        data = datetime.date.today()
        assert data is not None


# Generated at 2022-06-14 14:24:17.838252
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtf = DateTimeFormat()
    # common case
    value = "2020-05-12T15:32:38+08:00"
    res = dtf.validate(value)
    assert res == datetime.datetime(2020, 5, 12, 15, 32, 38, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
    # case 1: datetime with no timezone
    value = "2020-05-12T15:32:38"
    res = dtf.validate(value)
    assert res == datetime.datetime(2020, 5, 12, 15, 32, 38)
    # case 2: datetime with no timezone and no microseconds
    value = "2020-05-12T15:32:38"
    res = dtf.validate(value)

# Generated at 2022-06-14 14:24:29.079428
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_format = DateTimeFormat()
    # Testing with valid date-time
    assert date_format.validate("2019-10-03T09:15:00Z") == datetime.datetime(2019,10,3,9,15,0,tzinfo=datetime.timezone.utc)
    assert date_format.validate("2019-10-03T09:15:00+02:00") == datetime.datetime(2019,10,3,9,15,0,tzinfo=datetime.timezone(datetime.timedelta(0,7200)))
    # Testing with invalid date-time format
    try:
        date_format.validate("2019-10-03T09:15:00")
    except ValidationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 14:24:36.152841
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_string = UUIDFormat().validate("e081afbb-e804-4f7d-8d88-577a3efbb27b")
    assert isinstance(uuid_string, uuid.UUID)

    with pytest.raises(ValidationError) as excinfo:
        UUIDFormat().validate("this is not a UUID")
    assert excinfo.value.code == "format"



# Generated at 2022-06-14 14:24:38.725895
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime.now()
    assert DateTimeFormat().serialize(dt) == dt.isoformat()


# Generated at 2022-06-14 14:24:45.166141
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    assert DateFormat().serialize('2019-05-01') == '2019-05-01'


# Generated at 2022-06-14 14:24:52.436755
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    with pytest.raises(NotImplementedError):
        date_format.is_native_type("")
    with pytest.raises(NotImplementedError):
        date_format.validate("")
    with pytest.raises(NotImplementedError):
        date_format.serialize("")

    assert(date_format.validation_error("invalid") == ValidationError(text="Must be a real date.", code="invalid"))
    assert(date_format.validation_error("format") == ValidationError(text="Must be a valid date format.", code="format"))
    assert(date_format.validate("1001-12-01") == datetime.date(1001, 12, 1))


# Generated at 2022-06-14 14:24:56.569040
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(3,27,50,20)
    time_format = TimeFormat()
    assert time_format.serialize(time) == '03:27:50.000020'

# Generated at 2022-06-14 14:25:06.119975
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DATE_REGEX.match("2019-01-01") is not None, "2019-01-01"
    assert DATE_REGEX.match("19-01-01") is None, "19-01-01"
    assert DATE_REGEX.match("2019-1-01") is None, "2019-1-1"
    assert DATE_REGEX.match("2019-01-1") is None, "2019-01-1"
    assert DATE_REGEX.match("2019-01-01a") is None, "2019-01-01a"
    assert DATE_REGEX.match("2019-01-01_") is None, "2019-01-01_"


# Generated at 2022-06-14 14:25:09.760017
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    tf = TimeFormat()
    t = datetime.time(12, 30, 30, 30)
    result = tf.serialize(t)
    assert result == "12:30:30.000030"

# Generated at 2022-06-14 14:25:11.915209
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    assert DateFormat().serialize(datetime.date(2020, 7, 27)) == '2020-07-27'



# Generated at 2022-06-14 14:25:20.312289
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert TimeFormat().serialize(datetime.time(5,5)) == '05:05:00'
    assert TimeFormat().serialize(datetime.time(5,5,5)) == '05:05:05'
    assert TimeFormat().serialize(datetime.time(5,5,5,5)) == '05:05:05.000005'
    assert TimeFormat().serialize(datetime.time(5,5,5,5,datetime.timezone(datetime.timedelta(hours=5)))) == '05:05:05.000005+05:00'

# Generated at 2022-06-14 14:25:22.932208
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    formatter = DateFormat()
    formatter.serialize('2014-09-04') == '2014-09-04'


test_DateFormat_serialize()



# Generated at 2022-06-14 14:25:31.238905
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(hour=8, minute=0)
    assert TimeFormat().serialize(time) == "08:00"
    time = datetime.time(hour=8, minute=0, second=5)
    assert TimeFormat().serialize(time) == "08:00:05"
    time = datetime.time(hour=8, minute=0, second=5, microsecond=123456)
    assert TimeFormat().serialize(time) == "08:00:05.123456"
    time = datetime.time(hour=8, minute=0, second=5, microsecond=123)
    assert TimeFormat().serialize(time) == "08:00:05.000123"

# Generated at 2022-06-14 14:25:33.316588
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert TimeFormat().serialize(datetime.time(12,34)) == '12:34:00'

# Generated at 2022-06-14 14:25:42.642902
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    """
    This function tests the serialize method of the class TimeFormat
    Parameter :
        None => None
     Return :
        None
    """
    time = datetime.time(5, 8, 15)
    f = TimeFormat()
    assert f.serialize(time) == "05:08:15"


# Generated at 2022-06-14 14:25:46.599158
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date = datetime.date.today()

    date_obj = DateFormat()
    date_str = date_obj.serialize(date)

    assert date_str is not None
    assert isinstance(date_str, str)

# Generated at 2022-06-14 14:25:51.743269
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date = "2020-02-29T02:02:02Z"
    dateformat = DateTimeFormat()
    assert dateformat.validate(date) == datetime.datetime(2020, 2, 29, 2, 2, 2, tzinfo=datetime.timezone.utc)
    assert dateformat.validate("2020-02-29T02:02:02+02:00") == datetime.datetime(2020, 2, 29, 2, 2, 2, tzinfo=datetime.timezone(datetime.timedelta(0, 7200)))

# Generated at 2022-06-14 14:26:01.632724
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 2, 3, 4, 5, 0, datetime.timezone(datetime.timedelta(hours=-8, minutes=0)))) == "2020-01-02T03:04:05-08:00"
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 2, 3, 4, 5, 0, datetime.timezone(datetime.timedelta(hours=0, minutes=0)))) == "2020-01-02T03:04:05Z"

# Generated at 2022-06-14 14:26:03.755262
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    a = datetime.datetime(2019, 8, 22, 11, 1, 3, 15)
    b = (DateTimeFormat()).serialize(a)
    assert b == "2019-08-22T11:01:03.000015"

# Generated at 2022-06-14 14:26:13.578008
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    time = timezone.now().isoformat()
    time_timezone = time[:-6] + "+00:00"
    time_format = "2019-10-18T13:18:49+00:00"
    assert DateTimeFormat().validate(value=time) == DateTimeFormat().validate(value=time_timezone)
    assert DateTimeFormat().validate(value=time_timezone) == DateTimeFormat().validate(value=time_format)
    with pytest.raises(ValidationError):
        DateTimeFormat().validate(value="10:10")

# Generated at 2022-06-14 14:26:21.874085
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    df = DateFormat()
    
    # Test null case
    assert df.serialize(None) is None
    
    # Test case with normal datetime.date
    assert df.serialize(datetime.date(year = 2020, month = 2, day = 2)) == "2020-02-02"
    
    # Test case with datetime.date with 0 values
    assert df.serialize(datetime.date(year = 2000, month = 0, day = 0)) == "2000-00-00"
    
    
    


# Generated at 2022-06-14 14:26:23.859709
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time = datetime.datetime(2020,7,20,12,20,30,4000)
    assert DateTimeFormat().serialize(date_time) == '2020-07-20T12:20:30.004000'

# Generated at 2022-06-14 14:26:27.469956
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate('2016-12-20T15:20:36Z') == datetime.datetime(2016, 12, 20, 15, 20, 36, tzinfo=datetime.timezone(datetime.timedelta(0))), 'test for validate failed'


# Generated at 2022-06-14 14:26:33.356716
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    # Test case 1: test obj is None
    assert DateFormat().serialize(None) == None

    # Test case 2: Check if obj is not None
    obj = datetime.date.today()
    assert isinstance(DateFormat().serialize(obj), str) == True


# Generated at 2022-06-14 14:26:39.986078
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    print('\n\n\n')
    print('Test for function serialize of class TimeFormat')
    time_format = TimeFormat()
    time = datetime.time(17, 25, 30, 0)
    result = time_format.serialize(time)
    print('result = ' + str(result))

if __name__ == "__main__":
    test_TimeFormat_serialize()

# Generated at 2022-06-14 14:26:46.065668
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime_format = DateTimeFormat()
    # test assertion case
    assert datetime_format.validate("2020-01-23T01:45:01+00:00") == datetime.datetime(2020, 1, 23, 1, 45, 1, 0, tzinfo=datetime.timezone.utc)
    # test assertion case with invalid datetime 
    with pytest.raises(ValidationError):
        datetime_format.validate("2020-01-23T01:45:01")


# Generated at 2022-06-14 14:26:57.228650
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj1 = datetime.datetime.now()
    obj2 = datetime.datetime(1970,1,1, tzinfo=datetime.timezone.utc)
    obj3 = datetime.datetime(1970,1,1, tzinfo=datetime.timezone(datetime.timedelta(hours=-8)))
    obj4 = datetime.datetime(1970,1,1)
    assert DateTimeFormat().serialize(obj1)==obj1.isoformat()
    assert DateTimeFormat().serialize(obj2)==obj2.isoformat()[:-6]+"Z"
    assert DateTimeFormat().serialize(obj3)==obj3.isoformat()
    assert DateTimeFormat().serialize(obj4)==obj4.isoformat()

# Generated at 2022-06-14 14:27:04.133337
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    # Check if serialize function return string when obj is not None
    time = datetime.datetime(2018, 10, 20, 1, 1, 1)
    time = time.time()
    assert TimeFormat().serialize(time) == "01:01:01"

    # Check if serialize function return None when obj is None
    assert TimeFormat().serialize(None) == None


# Generated at 2022-06-14 14:27:14.990989
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    d = DateTimeFormat()
    #Test that serialize returns a valid ISO 8601 formatted string with timezone
    assert d.serialize(datetime.datetime(2020,8,7,14,15,16,719427,datetime.timezone.utc)) == "2020-08-07T14:15:16.719427Z"
    #Test that serialize returns a valid ISO 8601 formatted string with UTC timezone
    assert d.serialize(datetime.datetime(2020,8,7,14,15,16,719427)) == "2020-08-07T14:15:16.719427Z"
    #Test that serialize returns a valid ISO 8601 formatted string with non-UTC timezone

# Generated at 2022-06-14 14:27:23.168927
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 2, 3, 4, 5, 612345, tzinfo=datetime.timezone.utc)) == "2020-01-02T03:04:05.612345Z"
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 2, 3, 4, 5, 612345, tzinfo=datetime.timezone(datetime.timedelta(hours=1, minutes=2)))) == "2020-01-02T03:04:05.612345+01:02"
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 2, 3, 4, 5, 612000, tzinfo=datetime.timezone(datetime.timedelta(hours=1, minutes=2))))

# Generated at 2022-06-14 14:27:25.682286
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    tf = TimeFormat()

    assert tf.serialize(datetime.time(13,30))=="13:30:00"
    assert tf.serialize(datetime.time(13,30,10))=="13:30:10"
    assert tf.serialize(datetime.time(13,30,10,123456))=="13:30:10.123456"


# Generated at 2022-06-14 14:27:32.059167
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    obj = DateFormat()
    value = "2020-05-19"
    try:
        result = obj.validate(value)
        assert datetime.date == type(result)
    except ValidationError as err:
        assert False
    
    value = "2020-15-19"
    try:
        result = obj.validate(value)
        assert True == False
    except ValidationError:
        assert True


# Generated at 2022-06-14 14:27:34.395344
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time_format = TimeFormat()
    assert time_format.serialize(datetime.time(11, 24, 59, 2)) == "11:24:59.000002"

# Generated at 2022-06-14 14:27:38.752633
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj1 = datetime.datetime(2020,4,10,12,30,00)
    dtf = DateTimeFormat()
    assert dtf.serialize(obj1) == "2020-04-10T12:30:00"
    assert dtf.serialize(None) is None
# End of unit test for method serialize of class DateTimeFormat


# Generated at 2022-06-14 14:27:49.189437
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    fmt = DateTimeFormat()

    dt = datetime.datetime(2020, 3, 11, 11, 39, 49, 648056)
    assert fmt.serialize(dt) == "2020-03-11T11:39:49.648056"

    dt1 = datetime.datetime(2020, 3, 11, 11, 39, 49, 648056, datetime.timezone.utc)
    assert fmt.serialize(dt1) == "2020-03-11T11:39:49.648056Z"

    dt2 = (
        datetime.datetime(2020, 3, 11, 11, 39, 49, 648056) - datetime.timedelta(hours=3)
    )

# Generated at 2022-06-14 14:27:54.762633
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time = datetime.datetime(year=2020, month=9, day=12, hour=10, minute=50, second=30)
    date_time_format = DateTimeFormat()
    assert date_time_format.serialize(date_time) == "2020-09-12T10:50:30"


# Generated at 2022-06-14 14:27:59.783886
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Arrange
    valid_format = "2019-11-03T11:00:00Z"

    # Act
    result = DateTimeFormat().validate(valid_format)

    # Assert
    assert isinstance(result, datetime.datetime)
    assert result.isoformat() == valid_format



# Generated at 2022-06-14 14:28:01.851270
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_test = DateTimeFormat()
    date_time_test.validate("2019-10-08T11:00:00Z")

# Generated at 2022-06-14 14:28:07.938803
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date = datetime.datetime(year=2020, month=1, day=1, tzinfo=datetime.timezone.utc)
    date_format = DateTimeFormat()
    serialized_date = date_format.serialize(obj = date)
    assert serialized_date == "2020-01-01T00:00:00Z"

# Generated at 2022-06-14 14:28:14.140334
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Instantiate DateTimeFormat
    value = '2019-11-21T10:50:00+03:00'
    expected_output = datetime.datetime(2019, 11, 21, 10, 50, tzinfo=datetime.timezone(datetime.timedelta(0, 10800)))
    format = DateTimeFormat()
    # Call method validate
    actual_output = format.validate(value)
    # Compare expected output and actual output
    assert actual_output == expected_output


# Generated at 2022-06-14 14:28:19.149288
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtf = DateTimeFormat()
    result = dtf.validate("2018-12-13T18:31:07.971151")
    assert result == datetime.datetime(2018, 12, 13, 18, 31, 7, 971151)

# Generated at 2022-06-14 14:28:30.063150
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    assert t.validate("12:01:02.345678") == datetime.time(12, 1, 2, 345678)
    assert t.validate("12:01:02") == datetime.time(12, 1, 2)
    assert t.validate("12:01") == datetime.time(12, 1)
    assert t.validate("12") == datetime.time(12)
    assert t.validate("12:01:02.3456789") == datetime.time(12, 1, 2, 345678)
    assert t.validate("12:01:02.34567") == datetime.time(12, 1, 2, 345000)

# Generated at 2022-06-14 14:28:34.045319
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    format = DateTimeFormat()
    value = format.validate('2019-06-06T11:00:00Z')
    serialized = format.serialize(value)
    assert serialized == '2019-06-06T11:00:00Z'

# Generated at 2022-06-14 14:28:37.124288
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 23, 59, 59)) == "2020-01-01T23:59:59"

# Generated at 2022-06-14 14:28:50.861950
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeFormat = TimeFormat()
    value = "00:00:00.000000"
    assert timeFormat.validate(value) == datetime.time(hour=0, minute=0, second=0, microsecond=0)
    value = "00:00:00.000001"
    assert timeFormat.validate(value) == datetime.time(hour=0, minute=0, second=0, microsecond=100)
    value = "00:00:00.012345"
    assert timeFormat.validate(value) == datetime.time(hour=0, minute=0, second=0, microsecond=12345)
    value = "00:00:00.123456"

# Generated at 2022-06-14 14:29:02.669815
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()

    # Case 1: input format is not in 'HH:mm:ss'
    assert tf.validate("ab:cd:ef") == ValidationError(text="Must be a valid time format.", code="format")

    # Case 2: input format is 'HH:mm:ss', but no leading 0
    assert tf.validate("1:1:1") == ValidationError(text="Must be a real time.", code="invalid")

    # Case 3: input format is 'HH:mm:ss', but with microsecond
    assert tf.validate("01:01:01.1") == ValidationError(text="Must be a valid time format.", code="format")

    # Case 4: input format is 'HH:mm:ss'
    assert tf.validate("01:01:01")


# Generated at 2022-06-14 14:29:13.110000
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format_ = DateFormat()
    d1 = format_.validate('2017-10-14')
    assert d1.year == 2017
    assert d1.month == 10
    assert d1.day == 14
    d2 = format_.validate('1900-01-31')
    assert d2.year == 1900
    assert d2.month == 1
    assert d2.day == 31
    d3 = format_.validate('1003-09-24')
    assert d3.year == 1003
    assert d3.month == 9
    assert d3.day == 24
    d4 = format_.validate('3-9-24')
    assert d4.year == 3
    assert d4.month == 9
    assert d4.day == 24
    d5 = format_.validate('023-09-24')
   

# Generated at 2022-06-14 14:29:23.234037
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # happy path test
    t = TimeFormat()
    assert t.validate("12:00:00.abcdef") == datetime.time(
        12, 0, 0, microsecond=0, tzinfo=None
    )
    assert t.validate("12:00:00.abcdef") == datetime.time(
        12, 0, 0, microsecond=0, tzinfo=None
    )
    # happy path test with tzinfo
    t = TimeFormat()
    assert t.validate("12:00:00.abcdef+00:00") == datetime.time(
        12, 0, 0, microsecond=0, tzinfo=datetime.timezone.utc
    )

# Generated at 2022-06-14 14:29:26.303611
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-11-28T22:38:16+00:00") == datetime.datetime(2019, 11, 28, 22, 38, 16)



# Generated at 2022-06-14 14:29:34.428383
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    f = DateFormat()
    assert f.validate('1999-01-01') == datetime.date(1999, 1, 1)
    assert f.validate('2099-01-01') == datetime.date(2099, 1, 1)
    assert f.validate('1999-12-01') == datetime.date(1999, 12, 1)
    assert f.validate('1999-01-31') == datetime.date(1999, 1, 31)
    assert f.validate('1999-12-31') == datetime.date(1999, 12, 31)
    assert f.validate('1999-02-28') == datetime.date(1999, 2, 28)
    assert f.validate('1999-02-29') == datetime.date(1999, 2, 29)

# Generated at 2022-06-14 14:29:39.350161
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test valid input
    test = "2020-01-20"
    assert DateFormat().validate(test) == datetime.date(2020, 1, 20)
    # Test invalid input (not a date)
    test = "test"
    with pytest.raises(ValidationError):
        DateFormat().validate(test)



# Generated at 2022-06-14 14:29:45.900907
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-05-02") == datetime.date(2019, 5, 2)
    assert DateTimeFormat().validate("2019-05-02T12:10Z") == datetime.datetime(
        2019, 5, 2, 12, 10, tzinfo=datetime.timezone.utc
    )
    assert DateTimeFormat().validate("2019-05-02T12:10-03:00") == datetime.datetime(
        2019, 5, 2, 12, 10, tzinfo=datetime.timezone(datetime.timedelta(hours=-3))
    )



# Generated at 2022-06-14 14:29:50.959088
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeFormat = TimeFormat()
    assert timeFormat.validate('03:33:10.01') == datetime.time(3, 33, 10, 1000, tzinfo=None)


# Generated at 2022-06-14 14:29:59.246203
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    df.validate("1989-02-05")
    df.validate("1899-12-30")
    df.validate("2999-01-31")
    assert df.validate("1999-03-04") == datetime.date(1999, 3, 4)
    assert df.validate("1999-3-04") == datetime.date(1999, 3, 4)
    assert df.validate("1999-03-4") == datetime.date(1999, 3, 4)
    assert df.validate("1999-3-4") == datetime.date(1999, 3, 4)
    assert df.validate("99-03-04") == datetime.date(1999, 3, 4)

# Generated at 2022-06-14 14:30:13.832641
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = DateFormat()
    value = datetime.date(2020, 3, 22)
    # given value is a Date type
    assert d.is_native_type(value)
    # given value is a string "2020-03-22"
    value = d.validate('2020-03-22')
    # Expected value is in datetime.date format 2020, 3, 22
    assert value.year == 2020 and value.month == 3 and value.day == 22
    # Format Error
    try:
        d.validate('2020-03')
    except ValidationError as err:
        assert err.code == 'format'
    else:
        assert False
    # Format Error

# Generated at 2022-06-14 14:30:18.838267
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_input = "2018-12-25T14:14:13+05:45"
    date_output = "2018-12-25T14:14:13+05:45"

    result = DateTimeFormat().validate(date_input)
    assert result.isoformat() == date_output, result
    print('Validate DateTimeFormat: True')


# Generated at 2022-06-14 14:30:21.311879
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_formatter = DateTimeFormat()
    date_formatter.validate("2020-01-01T20:00:00Z")

# Generated at 2022-06-14 14:30:32.083870
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # create an object DateTimeFormat
    object_ = DateTimeFormat()
    # test the method validate in the case where value is a string that has a valid format
    value = '2020-06-09T12:11:20.000Z'
    assert isinstance(object_.validate(value), datetime.datetime)
    # test the method validate in the case where value is a string that has an invalid format
    value = '2020-06-09T12:11:20'
    with pytest.raises(ValidationError):
        object_.validate(value)
    # test the method validate in the case where value is a string that has an invalid format
    value = '2020-06-09 123:11:20.000Z'
    with pytest.raises(ValidationError):
        object_.validate(value)
    #

# Generated at 2022-06-14 14:30:43.145467
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("1946-12-07T00:00:00Z") == datetime.datetime(1946, 12, 7, 0, 0, 0, 0, datetime.timezone.utc)
    assert DateTimeFormat().validate("1946-12-07T00:00:00.000000Z") == datetime.datetime(1946, 12, 7, 0, 0, 0, 0, datetime.timezone.utc)
    assert DateTimeFormat().validate("1946-12-07T00:00:00.000023Z") == datetime.datetime(1946, 12, 7, 0, 0, 0, 23, datetime.timezone.utc)
    assert DateTimeFormat().validate("1946-12-07T00:00:00.000023-03") == dat

# Generated at 2022-06-14 14:30:51.997041
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # When value is a valid format(2020-01-28T23:58:54.934103+00:00)
    # Should return a datetime
    value = "2020-01-28T23:58:54.934103+00:00"
    dt = datetime.datetime(2020, 1, 28, 23, 58, 54, 934103, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate(value) == dt

    # When value is a valid format(2020-01-28T23:58:54.934103Z)
    # Should return a datetime
    value = "2020-01-28T23:58:54.934103Z"

# Generated at 2022-06-14 14:30:55.394339
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dt = DateTimeFormat().validate('2020-01-01T00:00:00+00:00')
    assert(dt.year == 2020 and dt.month == 1 and dt.day == 1 and dt.hour == 0 and dt.minute == 0 and dt.second == 0 and dt.tzinfo.tzname(None) == 'UTC')


# Generated at 2022-06-14 14:31:00.051903
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2018-01-01") == datetime.date(2018, 1, 1)
    with pytest.raises(ValidationError):
        DateFormat().validate("2018-1-1")



# Generated at 2022-06-14 14:31:08.766789
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    test_data = [
        ("09:20:19.000000", True),
        ("09:20", True),
        ("09:20:19", True),
        ("09:20:19.123456", True),
        ("09:20:19.", False),
        ("09:20:19.1234567", False),
        ("9:20:19.000000", False),
        ("09:20:19.000000+03", False),
    ]
    for value, isvalid in test_data:
        if not isvalid:
            assert TimeFormat().validate(value) == "Must be a valid time format."
        else:
            assert isinstance(TimeFormat().validate(value), datetime.time)


# Generated at 2022-06-14 14:31:17.841524
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    print(type(time.validate("11:12:13")))
    print(type(time.validate("11:12:13.000123")))
    print(type(time.validate("11:12:13.12")))
    print(type(time.validate("11:12")))
    print(type(time.validate("11:12:13.1234")))
    print(type(time.validate("11:12:13.123456")))
    # print(time.validate("11:12:13.1"))
    # time.validate("11:12:13.123")
    # time.validate("11:12:13.1234")
    # time.validate("11:12:13.12345")
    # time.validate("

# Generated at 2022-06-14 14:31:22.160114
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
	# creating object of class DateFormat
	obj = DateFormat()
	# calling method validate of class DateFormat
	obj.validate("2019-09-02")


# Generated at 2022-06-14 14:31:24.499300
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2020-09-13") == datetime.date(2020, 9, 13)


# Generated at 2022-06-14 14:31:32.298630
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.is_native_type(datetime.time(1, 1)) == True
    assert time.validate("12:00") == datetime.time(12)
    assert time.validate("12:00:00") == datetime.time(12)
    assert time.validate("12:00:00.000000") == datetime.time(12)
    assert time.validate("12:00:00.123456") == datetime.time(12, 0, 0,
                                                              123456)
    assert time.validate("12:00:00.12345") == datetime.time(12, 0, 0,
                                                             1234500)

# Generated at 2022-06-14 14:31:35.619731
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    t = DateFormat()
    value = '2020-04-07'
    expected = datetime.date(2020, 4, 7)
    assert t.validate(value) == expected


# Generated at 2022-06-14 14:31:41.817775
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from datetime import datetime
    test = ['12:30:31', '12:30:31.001', '12:30:31.0033', '12:30:31.003323', '12:30:31.003323123']
    expected = [datetime.strptime(t, '%H:%M:%S').time() for t in test]
    time_format = TimeFormat()
    actual = [time_format.validate(t) for t in test]
    assert actual == expected


# Generated at 2022-06-14 14:31:46.225656
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    # time_format.validate('01:02:03.123456')
    # time_format.validate('01:02')
    time_format.validate('01:02:03')



# Generated at 2022-06-14 14:31:50.411141
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format = TimeFormat()
    value = format.validate('09:12:11')
    x = value.hour
    y = value.minute
    z = value.second
    assert x == 9 and y == 12 and z == 11

# Generated at 2022-06-14 14:31:59.265136
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Not datetime format
    DATE_TEST = "2014-09-18"
    TIME_TEST = "23:05:00"
    DATETIME_TEST = "2014-09-18T23:05:00.123456Z"
    UUID_TEST = "c9bf9e57-1685-4c89-bafb-ff5af830be8a"

    date_test = DateFormat().validate(DATE_TEST)
    time_test = TimeFormat().validate(TIME_TEST)
    datetime_test = DateTimeFormat().validate(DATETIME_TEST)
    uuid_test = UUIDFormat().validate(UUID_TEST)

    # List of lists
    LENGTH = 2
    iter_validate_test = [[], []]

# Generated at 2022-06-14 14:32:03.934220
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    print('test_DateFormat_validate')
    d1 = DateFormat()
    assert d1.validate('2018-12-31') == datetime.date(2018, 12, 31)
    assert d1.validate('2018-12-32') == 'Invalid date format: 2018-12-32'



# Generated at 2022-06-14 14:32:10.401859
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    class Test_TimeFormat_validate(unittest.TestCase):
        def test_validate(self):
            T = TimeFormat()
            t = T.validate('00:00:00')
            self.assertEqual(t, datetime.time(0, 0))
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_TimeFormat_validate)
    unittest.TextTestRunner(verbosity=2).run(suite)



# Generated at 2022-06-14 14:32:22.448269
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("07:00:00") == datetime.time(7, 0, 0)
    assert TimeFormat().validate("07:00") == datetime.time(7, 0, 0)
    assert TimeFormat().validate("07:00:00.000000") == datetime.time(7, 0, 0)
    assert TimeFormat().validate("07:00:00.1") == datetime.time(7, 0, 0, 100000)
    assert TimeFormat().validate("07:00:00.12") == datetime.time(7, 0, 0, 120000)
    assert TimeFormat().validate("07:00:00.123") == datetime.time(7, 0, 0, 123000)
    assert TimeFormat().validate("07:00:00.1234") == datetime.time

# Generated at 2022-06-14 14:32:25.625936
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = "2020-05-01"
    assert DateFormat().validate(date) == datetime.date(2020, 5, 1)


# Generated at 2022-06-14 14:32:27.149297
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    fmt = TimeFormat()
    fmt.validate('13:15')

# Generated at 2022-06-14 14:32:34.878756
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date_format.validate("2020-08-01")
    date_format.validate("2018-02-28")
    #Date out of range
    try:
        date_format.validate("2020-08-40")
    except ValidationError as e:
        assert e.code == "invalid"
    #Wrong date format
    try:
        date_format.validate("2020/08/30")
    except ValidationError as e:
        assert e.code == "format"


# Generated at 2022-06-14 14:32:37.287777
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value_list = [(datetime.date(1,1,1))]
    for value in value_list:
        assert DateFormat().validate(value) == value


# Generated at 2022-06-14 14:32:45.445112
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    assert t.validate("00:00:00") == datetime.time(0,0,0)
    assert t.validate("01:00:00") == datetime.time(1,0,0)
    assert t.validate("03:00:00") == datetime.time(3,0,0)
    assert t.validate("23:59:59") == datetime.time(23,59,59)
    assert t.validate("00:00:00.000000") == datetime.time(0,0,0)


# Generated at 2022-06-14 14:32:50.722743
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate('2014-10-15') == datetime.date(2014, 10, 15)
    assert date_format.is_native_type(datetime.date(2014, 10, 15)) == True
    assert date_format.serialize(datetime.date(2014, 10, 15)) == '2014-10-15'

# Generated at 2022-06-14 14:32:55.900247
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime1 = datetime.datetime(2020,5,1,16,24,27)
    pattern1 = datetime1.isoformat()
    assert DateTimeFormat().validate(pattern1) == datetime1
    datetime2 = datetime.datetime(2020,5,1,16,24,27, tzinfo=datetime.timezone.utc)
    pattern2 = datetime2.isoformat()
    assert DateTimeFormat().validate(pattern2) == datetime2


# Generated at 2022-06-14 14:33:00.736768
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
   dateFormat = DateFormat()
   date = datetime.date(2011, 10, 11)
   assert dateFormat.validate("2011-10-11") == date
   assert dateFormat.validate("2011-10-11") != "2011-10-11"


# Generated at 2022-06-14 14:33:05.515398
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
	time_format = TimeFormat()
	result = time_format.validate(value='11:12:13.123456+00:00')
	print(result)
	assert result == datetime.time(11,12,13,123456)


# Generated at 2022-06-14 14:33:09.543618
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    # test for not match
    val = "1234567890"
    try:
        tf.validate(val)
    except:
        assert True
    
    # test for True
    val1 = "12:24:59"
    assert tf.validate(val1).isoformat() == val1
 

# Generated at 2022-06-14 14:33:12.919736
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = '2020-01-15'
    dateFormat = DateFormat()
    result = dateFormat.validate(date)
    assert result == datetime.date(2020, 1, 15)


# Generated at 2022-06-14 14:33:22.357066
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    with pytest.raises(ValidationError, match="format"):
        TimeFormat().validate("23:45:60")

    with pytest.raises(ValidationError, match="invalid"):
        TimeFormat().validate("25:45:60")

    #
    assert TimeFormat().validate("23:45:59") == datetime.time(23, 45, 59)
    assert TimeFormat().validate("23:45:59.123") == datetime.time(23, 45, 59, microsecond=123000)
    assert TimeFormat().validate("23:45:59.123001") == datetime.time(23, 45, 59, microsecond=123000)

