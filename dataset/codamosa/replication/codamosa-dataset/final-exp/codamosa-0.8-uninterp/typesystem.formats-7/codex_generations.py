

# Generated at 2022-06-14 14:23:39.599972
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Arrange
    datetime_format = DateTimeFormat()
    date_str = "2020-12-31T23:59:59+00:00"
    date_str_1 = "2020-12-31T23:59:59"

    # Act
    result = datetime_format.validate(date_str)

    # Assert
    assert result == datetime.datetime(2020, 12, 31, 23, 59, 59, 0, tzinfo=datetime.timezone.utc)
    assert isinstance(result, datetime.datetime)

    # Act
    result = datetime_format.validate(date_str_1)

    # Assert

# Generated at 2022-06-14 14:23:42.413464
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = DateFormat().validate(value = '2018-07-22')
    assert isinstance(value, datetime.date)

# Generated at 2022-06-14 14:23:44.849789
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2018-10-21') == datetime.date(2018, 10, 21)



# Generated at 2022-06-14 14:23:47.883272
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert (
        DateTimeFormat().validate("2020-01-01T00:00:00") == datetime.datetime(2020, 1, 1)
    )


# Generated at 2022-06-14 14:23:50.921836
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    val = '09:00:00'
    tf = TimeFormat()
    ans = tf.validate(val)
    assert ans == datetime.time(9, 0, 0)


# Generated at 2022-06-14 14:24:01.321951
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Arrange
    # Act
    f = TimeFormat()
    # Assert
    assert f.validate("10:00") == datetime.time(hour = 10, minute = 0)
    assert f.validate("10:00:00") == datetime.time(hour = 10, minute = 0, second = 0)
    assert f.validate("10:00:00.000000") == datetime.time(hour = 10, minute = 0, second = 0)
    assert f.validate("10:00:00.000000") == datetime.time(hour = 10, minute = 0, second = 0, microsecond = 0)
    assert f.validate("10:00:00.100000") == datetime.time(hour = 10, minute = 0, second = 0, microsecond = 100000)


# Generated at 2022-06-14 14:24:05.214641
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2019-03-14') == datetime.date(2019, 3, 14)
    try:
        DateFormat().validate('2019-13-14')
        raise RuntimeError('There should be an error')
    except ValidationError:
        pass


# Generated at 2022-06-14 14:24:15.223261
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    d1 = datetime.datetime(2020, 7, 20, 0, 0, 0, 0)
    d2 = datetime.datetime(2020, 7, 20, 0, 0, 0, 0, datetime.timezone.utc)
    d3 = datetime.datetime(2020, 7, 20, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=2)))
    d4 = datetime.datetime(2020, 7, 20, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=2, minutes=30)))
    d5 = datetime.datetime(2020, 7, 20, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(hours=-2)))

# Generated at 2022-06-14 14:24:19.107113
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dt = "1990-2-2T13:13"
    format = DateTimeFormat()
    validate_dt = format.validate(dt)

    assert isinstance(validate_dt, datetime.datetime)
    assert validate_dt.date() == datetime.date(year=1990, month=2, day=2)
    assert validate_dt.time() == datetime.time(hour=13, minute=13)



# Generated at 2022-06-14 14:24:30.278308
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    tf.validate('12:31')
    tf.validate('12:31:11')
    tf.validate('12:31:11.456')
    tf.validate('12:31:11.456789')
    with pytest.raises(ValidationError):
        tf.validate('12:31:')
    with pytest.raises(ValidationError):
        tf.validate('12:31:11.')
    with pytest.raises(ValidationError):
        tf.validate('12:31:11.4567891')
    with pytest.raises(ValidationError):
        tf.validate('12:31:11.45678912')

# Generated at 2022-06-14 14:24:37.344859
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    assert UUIDFormat().validate("aaa") is None
    assert not 5 in UUIDFormat().validate("30458df6-2e44-4d8e-8b4a-3a3fa86edd32")

# Generated at 2022-06-14 14:24:41.453289
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dateTimeFormat = DateTimeFormat()
    dt = datetime.datetime(2020,1,1,20,30,40)
    error = dateTimeFormat.validate("2020-01-01T20:30:40Z")
    assert error == dt


# Generated at 2022-06-14 14:24:51.118069
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    import typesystem

    class TestSchema(typesystem.Schema):
        format = typesystem.String(format=typesystem.formats.TimeFormat())

    schema = TestSchema()

    value = "13:45:20"
    assert schema.get_validator()(value) == datetime.time(13, 45, 20)

    value = "13:45:20.1"
    assert schema.get_validator()(value) == datetime.time(13, 45, 20, 100000)

    value = "13:45:20.12"
    assert schema.get_validator()(value) == datetime.time(13, 45, 20, 120000)

    value = "13:45:20.123"

# Generated at 2022-06-14 14:24:55.844452
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    df = DateTimeFormat()
    assert df.validate("2020-04-22T19:23:03.686980-05:00").isoformat() == "2020-04-22T19:23:03.686980-05:00"


# Generated at 2022-06-14 14:25:06.763149
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    assert "1:2" == TimeFormat().serialize(datetime.time(1,2))
    assert "1:2:3" == TimeFormat().serialize(datetime.time(1,2,3))
    assert "1:2:3.0001" == TimeFormat().serialize(datetime.time(1,2,3,1))
    assert "1:2:3.000100" == TimeFormat().serialize(datetime.time(1,2,3,1,1))
    assert "1:2:3.000100" == TimeFormat().serialize(datetime.time(1,2,3,1000000))
    assert "23:59:59.999999" == TimeFormat().serialize(datetime.time(23,59,59,999999))



# Generated at 2022-06-14 14:25:10.039887
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    today = datetime.datetime.today()
    assert today.isoformat() == DateFormat().serialize(today)
    assert 'None' == DateFormat().serialize(None)



# Generated at 2022-06-14 14:25:12.191626
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    UUIDFormat().validate("fa96f707-0206-48f5-a715-c14b3e61ad39")


# Generated at 2022-06-14 14:25:15.819244
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date_format = DateFormat()
    assert date_format.serialize(datetime.date.today()) == datetime.date.today().isoformat()
    assert date_format.serialize(None) == None


# Generated at 2022-06-14 14:25:23.866282
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    # Test case 1:
    # Input: obj = None
    # Expected output: None
    obj = None
    date_format = DateFormat()
    assert date_format.serialize(obj) == None

    # Test case 2:
    # Input: obj = datetime.date(2019, 7, 2)
    # Expected output: "2019-07-02"
    obj = datetime.date(2019, 7, 2)
    date_format = DateFormat()
    assert date_format.serialize(obj) == "2019-07-02"


# Generated at 2022-06-14 14:25:33.209439
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    iso_time = "12:34:56.123456"
    timeFormat = TimeFormat()
    timeValue = timeFormat.validate(iso_time)
    assert timeValue.isoformat() == iso_time

    iso_time = "12:34:56.12"
    timeFormat = TimeFormat()
    timeValue = timeFormat.validate(iso_time)
    assert timeValue.isoformat() == iso_time + '00'

    iso_time = "12:34:56"
    timeFormat = TimeFormat()
    timeValue = timeFormat.validate(iso_time)
    assert timeValue.isoformat() == iso_time + '.000000'

    iso_time = "12:34"
    timeFormat = TimeFormat()
    timeValue = timeFormat.validate(iso_time)

# Generated at 2022-06-14 14:25:48.146457
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date1 = DateTimeFormat()
    date2 = DateTimeFormat()
    date3 = DateTimeFormat()
    date4 = DateTimeFormat()
    date5 = DateTimeFormat()
    date6 = DateTimeFormat()
    date7 = DateTimeFormat()
    date8 = DateTimeFormat()
    date9 = DateTimeFormat()
    date10 = DateTimeFormat()
    date11 = DateTimeFormat()
    date12 = DateTimeFormat()

    assert str(date1.validate("2020")) == "2020-01-01 00:00:00"
    assert str(date2.validate("2020-04")) == "2020-04-01 00:00:00"
    assert str(date3.validate("2020-04-05")) == "2020-04-05 00:00:00"

# Generated at 2022-06-14 14:25:58.750116
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert "00:00:00" == tf.validate("00:00")
    assert "13:00:00" == tf.validate("13:00")
    assert "10:12:00" == tf.validate("10:12")
    assert "10:12:30" == tf.validate("10:12:30")
    assert "10:12:30" == tf.validate("10:12:30.00")
    assert "10:12:30.123456" == tf.validate("10:12:30.123456")
    assert "10:12:30.123456" == tf.validate("10:12:30.123456123456")


# Generated at 2022-06-14 14:26:02.379789
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()
    value = "2020-06-10T13:45:28.674600+02:00"
    print(format.validate(value))

if __name__ == "__main__":
    test_DateTimeFormat_validate()

# Generated at 2022-06-14 14:26:12.178475
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    #time_list = ["12:05:34.123456", "12:05:34.123456Z", "05", "12:05", "12:05:34", "12:05:34.123456+05:00"]
    time_list = ["12:05:34.123456", "12:05:34.123456+05:00"]
    for t in time_list:
        time = TimeFormat().validate(t)
        print(time)
        print(type(time))


if __name__ == "__main__":
    test_TimeFormat_validate()

# Generated at 2022-06-14 14:26:14.428090
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    format_time = TimeFormat()

    time = datetime.time(14, 15, 2)

    assert format_time.serialize(time) == '14:15:02'

# Generated at 2022-06-14 14:26:21.874924
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    df = DateFormat()
    dt = datetime.date.today()
    # Check if the response is a string
    assert isinstance(df.serialize(dt),str), "Result of serialize is not a string"
    # Check if the response is a valid string
    assert re.match("\d\d\d\d-\d\d-\d\d",df.serialize(dt)) != None, "Result of serialize is not a valid string"



# Generated at 2022-06-14 14:26:22.985999
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()

# Generated at 2022-06-14 14:26:26.029660
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    validate('20:18', t)
    validate('10:30:00', t)
    # validate('20:18:12:00:00:00:00', t)


# Generated at 2022-06-14 14:26:32.756618
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    result = DateTimeFormat().validate("2020-01-02T05:06:07")
    assert result.year == 2020
    assert result.month == 1
    assert result.day == 2
    assert result.hour == 5
    assert result.minute == 6
    assert result.second == 7
    assert result.microsecond == 0
    


# Generated at 2022-06-14 14:26:35.758284
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date = datetime.date.today()
    serialize = DateFormat().serialize(date)
    assert str(date) == serialize
    assert type(serialize) == str


# Generated at 2022-06-14 14:26:48.529715
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dt_format = DateTimeFormat()
    # time zone
    time_zone = '2020-01-23'
    dt = dt_format.validate(time_zone)
    assert(dt.isoformat() == time_zone)
    time_zone = '2020-01-23T11:44:00+01:00'
    dt = dt_format.validate(time_zone)
    assert(dt.isoformat() == time_zone)
    time_zone = '2020-01-23T11:44:00Z'
    dt = dt_format.validate(time_zone)
    assert(dt.isoformat() == time_zone)
    time_zone = '2020-01-23T11:44:00+03:00'
    dt = dt_format.validate

# Generated at 2022-06-14 14:26:53.650358
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(11, 11, 11, 111111)
    time_format = TimeFormat()
    result = time_format.serialize(time)
    assert result == '11:11:11.111111'


# Generated at 2022-06-14 14:26:58.254423
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    value = "2017-05-31T03:33:00+09:00"
    format = DateTimeFormat()
    result = format.validate(value)
    assert str(result) == "2017-05-31 03:33:00+09:00"
    assert str(result.tzinfo) == "UTC+09:00"

# Generated at 2022-06-14 14:27:07.429372
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.types import String
    from typesystem.formats import TimeFormat

    class TimeSchema(String):
        format = TimeFormat()

    assert TimeSchema().validate("12:00:00") == datetime.time(12, 0)
    assert TimeSchema().validate("12:00:00.0") == datetime.time(12, 0)
    assert TimeSchema().validate("12:00:00.123456") == datetime.time(12, 0, 0, 123456)


# Generated at 2022-06-14 14:27:10.492760
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    t = TimeFormat()
    assert t.serialize(datetime.time(23, 34, 56, 789)) == '23:34:56.000789'

# Generated at 2022-06-14 14:27:15.419455
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    my_time1 = datetime.time(12, 20, 00, 234567)
    my_time2 = datetime.time(12, 20, 00)
    assert TimeFormat().serialize(obj = my_time1) == "12:20:00.234567"
    assert TimeFormat().serialize(obj = my_time2) == "12:20:00"


# Generated at 2022-06-14 14:27:17.907422
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time_format = TimeFormat()
    time = datetime.time()
    result = time_format.serialize(time)
    assert result == time.isoformat()


# Generated at 2022-06-14 14:27:27.172870
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-12-18T13:53:44.577953Z") == datetime.datetime(2019, 12, 18, 13, 53, 44, 577953, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate("2019-12-18T13:53:44.577953+08:00") == datetime.datetime(2019, 12, 18, 13, 53, 44, 577953, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

# Generated at 2022-06-14 14:27:30.788780
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.datetime.now().time()
    time_serialize = TimeFormat.serialize(TimeFormat(), time)
    assert time_serialize == '{:%H:%M:%S}'.format(time)

# Generated at 2022-06-14 14:27:34.538488
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    #Test string
    value1 = '2019-06-11'
    value2 = '2019/06/11'
    value3 = '2019-06/11'
    value4 = '2019/06-11'
    #Test int
    value5 = 20190611
    #Test float
    value6 = 2019.0611
    #Test empty string
    value7 = ''
    #Test boolean
    value8 = True
    #Test null
    value9 = None
    #Test dict
    value10 = {'2019-06-11':12}
    #Test list
    value11 = [12, 2019, '2019-06-11']
    #Test tuple
    value12 = (12, 2019, '2019-06-11')
    #Test set
    value13 = {1,2019}
    #Test date
   

# Generated at 2022-06-14 14:27:44.734863
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    error = TimeFormat().validate('12:00:00')
    assert isinstance(error, datetime.time)
    error = TimeFormat().validate('12:00')
    assert isinstance(error, datetime.time)
    error = TimeFormat().validate('00:00')
    assert isinstance(error, datetime.time)
    error = TimeFormat().validate('00')
    assert isinstance(error, ValidationError)
# End of unit test


# Generated at 2022-06-14 14:27:47.423809
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2020-12-18') == datetime.date(year=2020, month=12, day=18)
    assert DateFormat().validate('2020-12-18') is not None


# Generated at 2022-06-14 14:27:59.620485
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate('2020-10-01T00:00:00Z') == datetime.datetime(
        2020, 10, 1, 0, 0, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate('2020-10-01T00:00:00+00:00') == datetime.datetime(
        2020, 10, 1, 0, 0, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate('2020-10-01T00:00:00-00:00') == datetime.datetime(
        2020, 10, 1, 0, 0, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate('2020-10-01T00:00:00+03:00') == datetime

# Generated at 2022-06-14 14:28:02.062918
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format=TimeFormat()
    result = format.validate("10:20:30")
    assert isinstance(result, datetime.time)


# Generated at 2022-06-14 14:28:05.020226
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    s = "10:34:05.123456"
    TimeFormat().validate(s)

# Generated at 2022-06-14 14:28:14.802319
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    test_class = TimeFormat()
    # test case 1
    input_value = "12:14:08+11:00"
    result = test_class.validate(input_value)
    expected_result = datetime.time(12, 14, 8, tzinfo=datetime.timezone(datetime.timedelta(hours=11)))
    assert result == expected_result

    # test case 2
    input_value = "12:14:08-11:00"
    result = test_class.validate(input_value)
    expected_result = datetime.time(12, 14, 8, tzinfo=datetime.timezone(datetime.timedelta(hours=-11)))
    assert result == expected_result

    # test case 3
    input_value = "12:14:08.098"


# Generated at 2022-06-14 14:28:16.487462
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate("18:10") == datetime.time(hour=18, minute=10)



# Generated at 2022-06-14 14:28:21.036170
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()

# Generated at 2022-06-14 14:28:27.865148
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_str = "18:00:00"
    time_obj = TimeFormat().validate(time_str)
    assert time_obj.hour == 18

    time_str = "18:00"
    time_obj = TimeFormat().validate(time_str)
    assert time_obj.hour == 18
    assert time_obj.minute == 0
    assert time_obj.second == 0
    assert time_obj.microsecond == 0


# Generated at 2022-06-14 14:28:32.035633
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    result = t.validate('12:40:45')
    assert (result==datetime.time(12, 40, 45))


# Generated at 2022-06-14 14:28:37.888132
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat().validate('12:15')
    assert time.strftime('%H:%M') == '12:15'


# Generated at 2022-06-14 14:28:49.605833
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()
    value_1 = u"2019-10-19T06:35:05"
    ret_1 = format.validate(value_1)
    assert ret_1 == datetime.datetime(
        2019, 10, 19, 6, 35, 5, tzinfo=datetime.timezone.utc
    )
    value_2 = u"2019-10-19T06:35:05.1"
    ret_2 = format.validate(value_2)
    assert ret_2 == datetime.datetime(
        2019, 10, 19, 6, 35, 5, 100000, tzinfo=datetime.timezone.utc
    )
    value_3 = u"2019-10-19T06:35:05.123456"
    ret_3 = format.validate

# Generated at 2022-06-14 14:28:59.507210
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("09:12") == datetime.time(hour=9,minute=12,second=0,microsecond=0)
    assert TimeFormat().validate("09:12:12") == datetime.time(hour=9,minute=12,second=12,microsecond=0)
    assert TimeFormat().validate("09:12:12.123123123") == datetime.time(hour=9,minute=12,second=12,microsecond=123123)
    assert TimeFormat().validate("09:12:12.123123") == datetime.time(hour=9,minute=12,second=12,microsecond=123123)

# Generated at 2022-06-14 14:29:08.645653
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtf = DateTimeFormat()
    date_1 = dtf.validate("2018-01-02")
    date_2 = dtf.validate("2018-1-2")
    assert date_1 == date_2
    assert date_1.year == 2018
    assert date_1.day == 1
    assert date_1.month == 1

    dtf = DateTimeFormat()    
    dt_1 = dtf.validate("2018-01-02T14:00")
    dt_2 = dtf.validate("2018-1-2T14:0")
    assert dt_1 == dt_2
    assert dt_1.year == 2018
    assert dt_1.day == 2
    assert dt_1.month == 1
    assert dt_1.minute == 0
    


# Generated at 2022-06-14 14:29:09.607143
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf1 = TimeFormat()
    assert tf1.validate("12:00") == datetime.time(12,0)

# Generated at 2022-06-14 14:29:15.873276
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    str1 = "2020-10-12"
    assert isinstance(date_format.validate(str1), datetime.date)

    str2 = "2020-10-12/12/5"
    with pytest.raises(ValidationError):
        assert date_format.validate(str2)

    str3 = "2020-13-12"
    with pytest.raises(ValidationError):
        assert date_format.validate(str3)



# Generated at 2022-06-14 14:29:22.944241
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d1 = '2018-01-01'
    d2 = '2018-01-32'
    d3 = '2018-01'

    assert DateFormat().validate(d1) == datetime.date(2018,1,1)
    with pytest.raises(ValidationError) as excinfo:
        DateFormat().validate(d2)
    with pytest.raises(ValidationError) as excinfo:
        DateFormat().validate(d3)
    # print(excinfo.value)


# Generated at 2022-06-14 14:29:24.888641
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2017-08-11') == datetime.date(2017, 8, 11)

# Generated at 2022-06-14 14:29:26.625805
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
	time=TimeFormat()
	assert time.validate('14:30')==datetime.time(14,30)

# Generated at 2022-06-14 14:29:31.730270
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("00:00:00") == datetime.time(0, 0, 0)
    assert TimeFormat().validate("00:00:00.000000") == datetime.time(0, 0, 0)
    assert TimeFormat().validate("00:00:00.000123") == datetime.time(0, 0, 0, 123)
    assert TimeFormat().validate("23:59:59.999999") == datetime.time(23, 59, 59, 999999)
    assert TimeFormat().serialize(datetime.time(0, 0, 0, 123456)) == "00:00:00.123456"

# Generated at 2022-06-14 14:29:39.561524
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    f = TimeFormat()
    if f.validate("12:30:59.999999") == "12:30:59.999999":
        print("test_TimeFormat_validate() passed.")
    else:
        print("test_TimeFormat_validate() failed.")


# Generated at 2022-06-14 14:29:47.382118
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    res = TimeFormat().validate("22:12:11")
    assert res.hour == 22
    assert res.minute == 12
    assert res.second == 11
    assert res.tzinfo is None

    res = TimeFormat().validate("22:12:11.5924")
    assert res.hour == 22
    assert res.minute == 12
    assert res.second == 11
    assert res.microsecond == 592400
    assert res.tzinfo is None

    res = TimeFormat().validate("22:12:11.592400")
    assert res.hour == 22
    assert res.minute == 12
    assert res.second == 11
    assert res.microsecond == 592400
    assert res.tzinfo is None

    res = TimeFormat().validate("22:12:11+04:00")
    assert res

# Generated at 2022-06-14 14:29:51.114123
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    TimeFormat().validate('23:59:59.999999')
    TimeFormat().validate('23:59:59')
    TimeFormat().validate('23:59')
    TimeFormat().validate('23')

# Generated at 2022-06-14 14:29:57.655113
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dt = DateTimeFormat()
    res = dt.validate('2019-11-29T17:55:00Z')
    assert res == datetime.datetime(2019, 11, 29, 17, 55, 00, tzinfo=datetime.timezone.utc)
    res = dt.validate('2019-11-29T17:55:00+00:00')
    assert res == datetime.datetime(2019, 11, 29, 17, 55, 00, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:30:10.861982
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat();
    assert tf.validate("00:00") == datetime.time(0, 0)
    assert tf.validate("00:00:00") == datetime.time(0, 0, 0)
    assert tf.validate("00:00:00.0") == datetime.time(0, 0, 0)
    assert tf.validate("00:00:00.00000") == datetime.time(0, 0, 0)
    assert tf.validate("01:01:01.000001") == datetime.time(1, 1, 1, 1)
    assert tf.validate("01:01:01.000011") == datetime.time(1, 1, 1, 11)

# Generated at 2022-06-14 14:30:17.503190
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    fmt = DateTimeFormat()
    obj = '2020-03-03T20:19:58+00:00'
    obj = fmt.validate(obj)
    assert obj.year == 2020
    assert obj.month == 3
    assert obj.day == 3
    assert obj.hour == 20
    assert obj.minute == 19
    assert obj.second == 58
    assert obj.microsecond == 0
    assert obj.tzinfo == datetime.timezone.utc


# Generated at 2022-06-14 14:30:21.297735
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dt = DateTimeFormat()
    assert dt.validate('2008-09-03T20:56:35.450686Z') ==\
        datetime.datetime(2008, 9, 3, 20, 56, 35, 450686, tzinfo=datetime.timezone.utc)


# Generated at 2022-06-14 14:30:24.069433
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    assert date.validate('2020-07-30') == datetime.date(2020, 7, 30)

# Generated at 2022-06-14 14:30:26.231772
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    f = TimeFormat()
    time = f.validate("12:00:00")
    assert time.hour == 12

# Generated at 2022-06-14 14:30:28.159412
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("23:59:59") == datetime.time(23,59,59)

# Generated at 2022-06-14 14:30:36.538625
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format_test = DateFormat()
    result = date_format_test.validate("1995-12-12")
    assert result == datetime.date(1995, 12, 12)


# Generated at 2022-06-14 14:30:41.783222
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat().validate("15:31:00")
    assert time.hour == 15
    assert time.minute == 31
    assert time.second == 0
    assert time.microsecond == 0



# Generated at 2022-06-14 14:30:50.796202
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # positive case
    DATE_ODD_DAYS_IN_MONTH = ['2018-01-00', '2018-02-01', '2018-02-00',
                              '2018-03-00', '2018-04-00', '2018-05-00',
                              '2018-06-00', '2018-07-00', '2018-08-00',
                              '2018-09-00', '2018-10-00', '2018-11-00', '2018-12-00']

# Generated at 2022-06-14 14:30:52.656525
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = DateFormat()
    assert d.validate("1999-08-08") == datetime.date(1999, 8, 8)


# Generated at 2022-06-14 14:30:54.139574
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    with pytest.raises(NotImplementedError):
        TimeFormat().validate(None)


# Generated at 2022-06-14 14:31:05.530816
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    today = datetime.datetime.today()
    today_time = datetime.time(today.hour, today.minute, today.second)
    assert time.validate(today_time.isoformat()) == today_time
    assert time.validate("11:12:13") == datetime.time(11, 12, 13)
    assert time.validate("11:12:13.123456+01:00") == datetime.time(11, 12, 13, 123456)
    assert time.validate("11:12:13+01:00") == datetime.time(11, 12, 13)

# Generated at 2022-06-14 14:31:13.381484
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    data = '2016-09-05'
    #Boundary conditions (when the input string is not in ISO8601 format)
    assert df.validate(data) == datetime.date(2016,9,5)
    data = '2016-09-00'
    with pytest.raises(ValidationError):
        df.validate(data)
    data = '2016-09-32'
    with pytest.raises(ValidationError):
        df.validate(data)
    data = '2016-9-5'
    with pytest.raises(ValidationError):
        df.validate(data)
    data = '2016'
    with pytest.raises(ValidationError):
        df.validate(data)
    data = '2016-09-05X'


# Generated at 2022-06-14 14:31:25.786666
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate("13:00:10") == datetime.time(13, 00, 10, 0, None)
    assert time.validate("13:00:10.123456") == datetime.time(13, 00, 10, 123456, None)
    assert time.validate("13:00:10.123") == datetime.time(13, 00, 10, 123000, None)
    assert time.validate("13:00:10.12") == datetime.time(13, 00, 10, 120000, None)
    assert time.validate("13:00:10.1") == datetime.time(13, 00, 10, 100000, None)

# Generated at 2022-06-14 14:31:33.556982
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    value = tf.validate('14:25:20')
    assert isinstance(value, datetime.time)
    assert value.hour == 14
    assert value.minute == 25
    assert value.second == 20

    with pytest.raises(ValidationError) as excinfo:
        tf.validate('1425:20')
    assert excinfo.value.as_dict() == {'code': 'format', 'text': 'Must be a valid time format.'}

# Generated at 2022-06-14 14:31:34.966031
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2018-10-11") == datetime.date(2018, 10, 11)


# Generated at 2022-06-14 14:31:40.492583
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    expected = datetime.time(23, 33, 40)
    test = TimeFormat()
    assert expected == test.validate("23:33:40")

test_TimeFormat_validate()

# Generated at 2022-06-14 14:31:52.270526
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    fmt = TimeFormat()
    fmt.validate("00:00:00")
    fmt.validate("2:00:00")
    fmt.validate("13:00:00")
    fmt.validate("23:00:00")
    fmt.validate("23:59:00")
    fmt.validate("23:59:59")
    fmt.validate("23:59:59.123")
    fmt.validate("23:59:59.123456")
    fmt.validate("23:59:59.1234567")
    
    try:
        fmt.validate("23:59:60")
        assert False, "Should raise an error"
    except ValidationError:
        pass

# Generated at 2022-06-14 14:31:58.613764
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    print("\nTest DateFormat validate")
    # Invalid Date format
    # DateFormat().validate("2019-12")
    # DateFormat().validate("20-4-12")
    # DateFormat().validate("2019/12/2")
    # Valid Date format
    d1 = DateFormat().validate("2019-12-12")
    assert d1 == datetime.date(2019, 12, 12)
    d2 = DateFormat().validate("1970-01-01")
    assert d2 == datetime.date(1970, 1, 1)



# Generated at 2022-06-14 14:32:02.921110
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time=time_format.validate("23:59:59.999999")
    print(time)
    assert time == datetime.time(23, 59, 59, 999999)


# Generated at 2022-06-14 14:32:12.122095
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeFormat = TimeFormat()
    timeStr = '10:45:30'
    time = timeFormat.validate(timeStr)
    assert time == datetime.time(hour=10,minute=45,second=30)
    timeStr = '10:45:30.123456'
    time = timeFormat.validate(timeStr)
    assert time == datetime.time(hour=10,minute=45,second=30,microsecond=123456)
    timeStr = '10:45'
    time = timeFormat.validate(timeStr)
    assert time == datetime.time(hour=10,minute=45)
    timeStr = '10:45:00.12'
    time = timeFormat.validate(timeStr)

# Generated at 2022-06-14 14:32:16.345278
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    """
    Unit test for method validate of class DateFormat.
    """
    dateFormat = DateFormat()
    dateTime = dateFormat.validate("2020-02-11")
    assert isinstance(dateTime, datetime.date)


# Generated at 2022-06-14 14:32:25.099481
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert (date_format.validate("2012-12-12") == datetime.date(2012, 12, 12))
    assert (date_format.validate("1200-12-12") == datetime.date(1200, 12, 12))
    assert (date_format.validate("2012-1-12") == datetime.date(2012, 1, 12))
    assert (date_format.validate("2012-12-1") == datetime.date(2012, 12, 1))

    # Unit test for invalid format
    try:
        assert (date_format.validate("2012-12-1212") == datetime.date(2012, 12, 12))
    except ValidationError as e:
        assert (e.code == "format")

    # Unit test for invalid date

# Generated at 2022-06-14 14:32:30.233471
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat().validate('2022-02-02')
    assert isinstance(date, datetime.date)
    
    with pytest.raises(ValidationError):
        DateFormat().validate('2022-02-02T09:30:00Z')


# Generated at 2022-06-14 14:32:31.639394
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    TimeFormat().validate("23:24:25")



# Generated at 2022-06-14 14:32:37.059930
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert tf.validate('12:34') == datetime.time(12, 34)
    assert tf.validate('13:56:15.23') == datetime.time(13, 56, 15, 230000)
    assert tf.validate('13:56:15.2314') == datetime.time(13, 56, 15, 231000)



# Generated at 2022-06-14 14:32:44.004993
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dt = DateFormat()
    assert dt.validate('2018-11-10') == datetime.date(2018, 11, 10)


# Generated at 2022-06-14 14:32:44.860407
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    TimeFormat().validate("10:20:30.123456")
    assert 1 == 1


# Generated at 2022-06-14 14:32:48.890780
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    value = "12:34:56.012345"
    fmt = TimeFormat()
    t1 = fmt.validate(value)
    value2 = "12:34"
    t2 = fmt.validate(value2)
    assert (t1.hour == t2.hour)

# Generated at 2022-06-14 14:32:52.999404
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2019-01-01") == datetime.date(2019,1,1)
    assert DateFormat().validate("2000-12-31") == datetime.date(2000,12,31)
    assert DateFormat().validate("1999-01-01") == datetime.date(1999,1,1)


# Generated at 2022-06-14 14:32:56.656160
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    value = "2020-02-28"
    obj = dateFormat.validate(value)
    assert isinstance(obj, datetime.date)

# Generated at 2022-06-14 14:32:59.525170
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    with pytest.raises(NotImplementedError):
        time = TimeFormat()
        time.validate("test")


# Generated at 2022-06-14 14:33:08.992520
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    def test_validate(df, value, expected):
        actual = df.validate(value)
        assert actual == expected

    df = DateFormat()

    test_validate(df, "2020-01-01", datetime.date(2020, 1, 1))
    test_validate(df, "2020-12-31", datetime.date(2020, 12, 31))

    with pytest.raises(ValidationError):
        df.validate("2020-02-30")

    with pytest.raises(ValidationError):
        df.validate("2020-13-01")


# Generated at 2022-06-14 14:33:13.922382
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    f = DateFormat()
    try:
        date = f.validate("2020-08-12")
        assert date.year == 2020
        assert date.month == 8
        assert date.day == 12
    except ValidationError:
        raise AssertionError("Wrong validation error")

# Generated at 2022-06-14 14:33:16.704524
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    value = date.validate("2020-03-14")
    assert isinstance(value, datetime.date)


# Generated at 2022-06-14 14:33:20.200258
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()

    assert date.validate(datetime.date.today()) == datetime.date.today()
    assert date.validate('2020-01-01') == datetime.date(2020, 1, 1)
