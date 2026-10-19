

# Generated at 2022-06-14 14:23:36.028326
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = DateFormat()
    assert d.validate('2001-01-01') == datetime.date(2001, 1, 1)


# Generated at 2022-06-14 14:23:41.030118
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
	expected = '2011-09-03T12:59:33.123456Z'
	dt = datetime.datetime(2011, 9, 3, 12, 59, 33,123456)
	obj = DateTimeFormat()
	assert obj.serialize(dt) == expected


# Generated at 2022-06-14 14:23:43.972521
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    UUIDFormat().validate('5a0d5b6c-e6dd-4a9f-a1e2-f22fcb6f5c6a')

# Generated at 2022-06-14 14:23:55.724527
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    '''
    Test validate method of class DateTimeFormat
    This method checks if the given string is a valid datetime format
    '''
    # test case 1: check if a valid datetime string is accepted
    assert(DateTimeFormat().validate("2019-03-03T14:16:08") == datetime.datetime(2019, 3, 3, 14, 16, 8))
    # test case 2: check if a string without hour is not accepted
    try:
        DateTimeFormat().validate("2019-03-03")
        assert(False)
    except ValidationError:
        assert(True)
    # test case 3: check if a string without year is not accepted

# Generated at 2022-06-14 14:24:04.716888
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2019, 10, 4, 20, 10, 0)) == "2019-10-04T20:10:00"
    assert DateTimeFormat().serialize(datetime.datetime(2019, 10, 4, 20, 10, 0, 0)) == "2019-10-04T20:10:00"
    assert DateTimeFormat().serialize(datetime.datetime(2019, 10, 4, 20, 10, 0, 0, tzinfo=datetime.timezone.utc)) == "2019-10-04T20:10:00Z"

# Generated at 2022-06-14 14:24:08.944046
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate(value="2018-06-13") == datetime.date(2018, 6, 13)
    with pytest.raises(ValidationError):
        df.validate(value="wrong format")


# Generated at 2022-06-14 14:24:14.281363
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dataTimeFormat = DateTimeFormat()
    today = datetime.datetime.now()
    assert dataTimeFormat.serialize(today) == today.isoformat()
    assert dataTimeFormat.serialize(today) == '2020-02-19T23:39:31.590155'
    assert dataTimeFormat.serialize(datetime.datetime.utcnow()) == \
           datetime.datetime.utcnow().isoformat()

# Generated at 2022-06-14 14:24:25.073417
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
     assert datetime.time(12,45,78,123456,None) == TimeFormat().validate("12:45:78.123456")
     assert datetime.time(12,45,78,None,None) == TimeFormat().validate("12:45:78")
     assert datetime.time(12,45,None,None,None) == TimeFormat().validate("12:45")
     assert datetime.time(12,45,78,123456,None) == TimeFormat().validate("12:45:78.123456-05:00")
     assert datetime.time(12,45,78,123456,None) == TimeFormat().validate("12:45:78.123456+05:00")

# Generated at 2022-06-14 14:24:27.964027
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    try:
        date_format.validate("2018-01-01")
    except Exception:
        raise AssertionError()


# Generated at 2022-06-14 14:24:29.773332
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    x = DateFormat()
    assert "2019-12-12" == x.serialize(datetime.date(2019, 12, 12))


# Generated at 2022-06-14 14:24:41.017690
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
   obj = datetime.datetime(year=2019, month=4, day=3, hour=8, minute=31, second=1, microsecond=100)
   date_format = DateTimeFormat()
   result = date_format.serialize(obj)
   assert result == "2019-04-03T08:31:01.000100"

# Generated at 2022-06-14 14:24:49.103212
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    res = DateTimeFormat().validate("1994-11-05T13:15:30Z")
    assert res == datetime.datetime(1994, 11, 5, 13, 15, 30, tzinfo=datetime.timezone.utc)
    res = DateTimeFormat().validate("1994-11-05T08:15:30-05:00")
    assert res == datetime.datetime(1994, 11, 5, 13, 15, 30, tzinfo=datetime.timezone(datetime.timedelta(hours=-5)))
    print("test_DateTimeFormat_validate OK")



# Generated at 2022-06-14 14:24:51.051096
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    test_baseFormat = BaseFormat()
    test_baseFormat.validate('12:23')
    test_baseFormat.serialize('12:23')


# Generated at 2022-06-14 14:25:03.221859
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    #Empty datetime
    with pytest.raises(ValueError):
        DateTimeFormat().validate("")
    with pytest.raises(ValueError):
        DateTimeFormat().validate(" ")

    #Invalid format for datetime
    with pytest.raises(ValueError):
        DateTimeFormat().validate("2020-13-01T00:00:00Z")
    with pytest.raises(ValueError):
        DateTimeFormat().validate("2020-01-40T00:00:00Z")
    with pytest.raises(ValueError):
        DateTimeFormat().validate("2020-02-29T00:00:00Z")
    with pytest.raises(ValueError):
        DateTimeFormat().validate("2020-10-31T24:00:00Z")

# Generated at 2022-06-14 14:25:10.541965
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    valueUTC = datetime.datetime(
        2020, 10, 11, tzinfo=datetime.timezone.utc
    ).isoformat()
    value = datetime.datetime(2020, 10, 11).isoformat() + 'Z'
    assert DateTimeFormat().serialize(datetime.datetime(2020, 10, 11, tzinfo=datetime.timezone.utc)) == value
    assert DateTimeFormat().serialize(datetime.datetime(2020, 10, 11)) == value


# Generated at 2022-06-14 14:25:15.677790
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    try:
        assert DateFormat().validate("2019-04-24") == datetime.date(2019, 4, 24)
    except ValidationError:
        assert False

    try:
        assert DateFormat().validate("2019-04-31") == datetime.date(2019, 4, 31)
    except ValidationError:
        assert False


# Generated at 2022-06-14 14:25:19.452020
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    time = datetime.time(hour=10, minute=0, second=0)
    time = TimeFormat().serialize(time)
    assert time == '10:00:00'


# Generated at 2022-06-14 14:25:22.245138
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    res = date_format.validate(value="2020-01-01")
    assert isinstance(res, datetime.date)

# Generated at 2022-06-14 14:25:30.608917
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Given a DateTimeFormat object and an isoformat string for datetime
    format = DateTimeFormat()
    value = "2020-06-20T07:20:00+00:00"

    # When the validation method is called
    result = format.validate(value)

    # Then result is the corresponding datetime object
    assert isinstance(result, datetime.datetime)
    assert result.year == 2020
    assert result.month == 6
    assert result.day == 20
    assert result.hour == 7
    assert result.minute == 20
    assert result.second == 0
    assert result.microsecond == 0
    assert result.tzinfo == datetime.timezone.utc


# Generated at 2022-06-14 14:25:38.509274
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    # arrange
    expected_result1 = None
    expected_result2 = "12:00:00.00000"
    expected_result3 = "12:00:00"
    test1 = None
    test2 = datetime.time(12, 0, 0, 0)
    test3 = datetime.time(12, 0, 0)
    timeFormat = TimeFormat()

    # act
    result1 = timeFormat.serialize(test1)
    result2 = timeFormat.serialize(test2)
    result3 = timeFormat.serialize(test3)

    # assert
    assert result1 == expected_result1
    assert result2 == expected_result2
    assert result3 == expected_result3



# Generated at 2022-06-14 14:25:49.585901
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate('2019-05-10T12:30:54Z')
    assert DateTimeFormat().validate('2019-05-10T12:30:54+01:00')
    assert DateTimeFormat().validate('2019-05-10T12:30:54+0100')
    assert DateTimeFormat().validate('2019-05-10T12:30:54-01:00')
    assert DateTimeFormat().validate('2019-05-10T12:30:54-0100')

# Generated at 2022-06-14 14:25:59.894618
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()

    assert format.validate("2019-12-23T15:18:50.1234566") == datetime.datetime(2019, 12, 23, 15, 18, 50, 123456, tzinfo=None)
    assert format.validate("2019-12-23T15:18:50Z") == datetime.datetime(2019, 12, 23, 15, 18, 50, 0, tzinfo=datetime.timezone.utc)
    assert format.validate("2019-12+02:00") == datetime.datetime(2019, 12, 1, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))



# Generated at 2022-06-14 14:26:04.542196
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format = DateTimeFormat()
    assert date_time_format.errors == {'format': 'Must be a valid datetime format.', 'invalid': 'Must be a real datetime.'}
    assert date_time_format.validate("2020-01-30T12:04:24Z") == datetime.datetime(2020, 1, 30, 12, 4, 24, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:26:11.062930
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
        dt_custom_format = DateTimeFormat()
        assert dt_custom_format.serialize(datetime.datetime(2020, 1, 2, 15, 30, 20, 854545)) == "2020-01-02T15:30:20.854545"

# Generated at 2022-06-14 14:26:21.401020
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime.fromisoformat('2020-11-27T22:00:00')
    assert(DateTimeFormat().serialize(dt) == '2020-11-27T22:00:00')

    dt = datetime.datetime.fromisoformat('2020-11-27T22:00:00.123456')
    assert(DateTimeFormat().serialize(dt) == '2020-11-27T22:00:00.123456')

    dt = datetime.datetime.fromisoformat('2020-11-27T22:00:00.123456+01:00')
    assert(DateTimeFormat().serialize(dt) == '2020-11-27T22:00:00.123456+01:00')


# Generated at 2022-06-14 14:26:30.906000
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(1, 1, 1, tzinfo=None)) == '0001-01-01T00:00:00'
    assert DateTimeFormat().serialize(datetime.datetime(2, 2, 2, tzinfo=None)) == '0002-02-02T00:00:00'
    assert DateTimeFormat().serialize(datetime.datetime(3, 3, 3, tzinfo=None)) == '0003-03-03T00:00:00'
    assert DateTimeFormat().serialize(datetime.datetime(4, 4, 4, tzinfo=None)) == '0004-04-04T00:00:00'

# Generated at 2022-06-14 14:26:33.592681
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate("00:00:00") == datetime.time(0, 0)
    assert time.validate("00:00:00.123456") == datetime.time(0, 0, 0, 123456)
    assert time.validate("23:59:59.999999") == datetime.time(23, 59, 59, 999999)

# Generated at 2022-06-14 14:26:37.240135
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate("2020-11-01") == datetime.date(2020, 11, 1)
    assert df.validate("2020-11-01") == datetime.date(2020, 11, 1)


# Generated at 2022-06-14 14:26:39.798802
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    try:
        dateFormat.validate("2020-10-13")
    except ValidationError:
        assert 0



# Generated at 2022-06-14 14:26:44.036531
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    input_time = "13:15:00"
    tf = TimeFormat()
    assert repr(tf.validate(input_time)) == repr(datetime.time(13, 15))

# Generated at 2022-06-14 14:26:51.081106
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    input_object = datetime.datetime(1969, 7, 20, 20, 17, 40, tzinfo=datetime.timezone.utc)
    expected_output = "1969-07-20T20:17:40Z"
    actual_output = DateTimeFormat.serialize(input_object)
    assert expected_output == actual_output

# Generated at 2022-06-14 14:26:56.843394
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    a = DateTimeFormat()
    date1 = datetime.datetime(2020, 9, 13, 10, 5)
    result = a.serialize(date1)
    #print(result)
    assert result == "2020-09-13T10:05:00", "Result must be '2020-09-13T10:05:00'"


# Generated at 2022-06-14 14:27:01.204251
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dt = DateTimeFormat()
    assert dt.validate('2016-11-05T11:45:16.601928+00:00') == datetime.datetime(2016, 11, 5, 11, 45, 16, 601928, tzinfo=datetime.timezone(datetime.timedelta(0)))

# Generated at 2022-06-14 14:27:13.177216
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    DateTimeFormat_serialize = DateTimeFormat()
    time1 = datetime.datetime.strptime("2020-02-17T10:15:25.540828-05:00", "%Y-%m-%dT%H:%M:%S.%f%z")
    time2 = datetime.datetime.strptime("2020-02-17T10:15:25.540828", "%Y-%m-%dT%H:%M:%S.%f")
    time3 = datetime.datetime.strptime("2020-02-17T10:15:25-05:00", "%Y-%m-%dT%H:%M:%S%z")

# Generated at 2022-06-14 14:27:20.780440
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from typesystem.fields import DateTime

    dt = DateTime(format="iso")

    assert dt.serialize(None) == None

    assert dt.serialize(datetime.datetime(2018, 7, 11, 11, 4, 4, tzinfo=datetime.timezone.utc)) == "2018-07-11T11:04:04Z"
    assert dt.serialize(datetime.datetime(2018, 7, 11, 11, 4, 4, tzinfo=datetime.timezone(datetime.timedelta(hours=-3, minutes=30)))) == "2018-07-11T11:04:04-03:30"

# Generated at 2022-06-14 14:27:24.211441
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate('20:00:00') == datetime.time(20, 0, 0)

# Generated at 2022-06-14 14:27:35.515341
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    test_instance = DateTimeFormat()

# Generated at 2022-06-14 14:27:43.703625
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value1 = "2020-11-01"
    assert value1 == DateFormat().validate(value1).isoformat()

    value2 = "2020-01-1"
    assert value2 == DateFormat().validate(value2).isoformat()

    value3 = "2020-1-01"
    assert value3 == DateFormat().validate(value3).isoformat()

    value4 = "20-11-01"
    assert value4 == DateFormat().validate(value4).isoformat()

    value5 = "2000-1-1"
    assert value5 == DateFormat().validate(value5).isoformat()

    value6 = "1999-11-1"
    assert value6 == DateFormat().validate(value6).isoformat()

    value7 = "19-11-01"
    assert value7 == DateFormat

# Generated at 2022-06-14 14:27:46.582384
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    obj = TimeFormat()
    assert obj.validate("00:00:00") == datetime.time(0, 0)



# Generated at 2022-06-14 14:27:58.851900
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    print('Testing method serialize of class DateTimeFormat...')
    # From wikipedia https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations
    print('{0:>10}|{1:>10}|{2:>10}'.format('ISO 8601', 'Expected', 'Result'))
    expected = '20060705T190000Z'
    result = DateTimeFormat().serialize(datetime.datetime(2006, 7, 5, 19, 0, tzinfo=datetime.timezone.utc))
    print('{0:>10}|{1:>10}|{2:>10}'.format(expected, expected, result))
    expected = '1996-12-19T16:39:57-08:00'
    result = DateTimeFormat

# Generated at 2022-06-14 14:28:10.652457
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime_format = DateTimeFormat()

    # валидная строка даты и времени
    value = "2015-01-30T15:09:22+03:00"
    datetime_format.validate(value)

    # невалидная строка даты и времени
    value = "2015-01-30T15:09:22"
    with pytest.raises(ValidationError):
        datetime_format.validate(value)

# Generated at 2022-06-14 14:28:18.344571
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # Test case 1
    # Input parameter: "datetime"
    obj = datetime.datetime(2020, 7, 21, 11, 45, 35)
    assert DateTimeFormat().serialize(obj) == "2020-07-21T11:45:35"

    # Test case 2
    # Input parameter: "datetime"
    obj = datetime.datetime(2020, 7, 21, 11, 45, 35, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().serialize(obj) == "2020-07-21T11:45:35Z"

    # Test case 3
    # Input parameter: "datetime"
    obj = datetime.datetime(2020, 7, 21, 11, 45, 35, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:28:29.416619
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    a = DateTimeFormat()
    assert a.serialize(datetime.datetime(2019, 9, 8, 23, 0, 0)) == '2019-09-08T23:00:00'
    assert a.serialize(datetime.datetime(2019, 9, 8, 23, 0, 0, tzinfo=datetime.timezone.utc)) == '2019-09-08T23:00:00Z'
    assert a.serialize(datetime.datetime(2019, 9, 8, 23, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=4)))) == '2019-09-08T23:00:00+04:00'

# Generated at 2022-06-14 14:28:31.205712
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    actual = DateTimeFormat().serialize(datetime.datetime.now())
    assert actual

# Generated at 2022-06-14 14:28:35.658669
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    date_time = datetime.datetime(2020,3,3,3,3,3,3)
    assert(date_time_format.serialize(date_time) == "2020-03-03T03:03:03.000003Z")


# Generated at 2022-06-14 14:28:42.920738
# Unit test for method serialize of class DateTimeFormat

# Generated at 2022-06-14 14:28:47.097283
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    valid_date = '2019-04-30'
    date_fmt = dateFormat.validate(valid_date)
    assert date_fmt == datetime.date(2019,4,30)

# Generated at 2022-06-14 14:28:49.349236
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time = DateTimeFormat()
    date_time.validate("2019-01-25 13:32:52")

# Generated at 2022-06-14 14:29:01.448705
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # 1. Test case: no timezone
    time = "2019-12-24"
    pattern_expected = r"(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})"
    match = DATE_REGEX.match(time)
    assert match
    kwargs = {k: int(v) for k, v in match.groupdict().items()}
    result = datetime.date(**kwargs)

    assert type(result) == datetime.date

    # 2. Test case: with timezone
    time = "2019-12-24T10:45:00.100-07:00"

# Generated at 2022-06-14 14:29:04.846129
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    value = time.validate("12:34:56.789012")
    assert value.hour == 12
    assert value.minute == 34
    assert value.second == 56
    assert value.microsecond == 789012

# Generated at 2022-06-14 14:29:11.882579
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime(2020, 1, 1, tzinfo=datetime.timezone.utc)
    dtf = DateTimeFormat()
    assert dtf.serialize(dt) == "2020-01-01T00:00:00Z"

# Generated at 2022-06-14 14:29:21.822442
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert type(tf.validate('12:10:10')) == datetime.time
    assert type(tf.validate('12:10')) == datetime.time
    assert type(tf.validate('10')) == datetime.time
    assert type(tf.validate('12:10:10.123')) == datetime.time
    assert type(tf.validate('12:10:10.123456')) == datetime.time
    assert type(tf.validate('12:10:10.1234')) == datetime.time
    assert type(tf.validate('12:10:10.12')) == datetime.time
    assert type(tf.validate('12:10:10.1')) == datetime.time

# Generated at 2022-06-14 14:29:29.128464
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    format_ = DateTimeFormat()
    assert format_.serialize(None) == None

    obj = datetime.datetime(2020, 12, 1, 12, 15, 4, tzinfo=datetime.timezone.utc)
    assert format_.serialize(obj) == "2020-12-01T12:15:04+00:00"

    obj = datetime.datetime(2020, 12, 1, 12, 15, 4, tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    assert format_.serialize(obj) == "2020-12-01T12:15:04+05:30"

# Generated at 2022-06-14 14:29:36.769700
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    match = DATE_REGEX.match("2019-10-28")
    assert match
    kwargs = {k: int(v) for k, v in match.groupdict().items()}
    try:
        return datetime.date(**kwargs)
    except ValueError:
        raise self.validation_error("invalid")

# Generated at 2022-06-14 14:29:42.334297
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    d = datetime.datetime(2017, 2, 3, 4, 5, 6)

    assert DateTimeFormat().serialize(d) == '2017-02-03T04:05:06'

    d = datetime.datetime(2017, 2, 3, 4, 5, 6, tzinfo=datetime.timezone(datetime.timedelta(hours=1)))

    assert DateTimeFormat().serialize(d) == '2017-02-03T04:05:06+01:00'

# Generated at 2022-06-14 14:29:45.548140
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    value = datetime.datetime.now().isoformat()
    test_dt_format = DateTimeFormat()
    dt = test_dt_format.validate(value)
    assert test_dt_format.serialize(dt) == value



# Generated at 2022-06-14 14:29:56.810502
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    match = TIME_REGEX.match("11:25:30.123")
    assert match
    assert match.groupdict() == {'hour': '11', 'minute': '25', 'second': '30', 'microsecond': '123'}
    assert time.validate("11:25:30.123") == datetime.time(11, 25, 30, 123000)
    assert time.validate("11:25:30") == datetime.time(11, 25, 30)
    assert time.validate("11:25") == datetime.time(11, 25)
    assert time.validate("11") == datetime.time(11)


# Generated at 2022-06-14 14:30:02.835322
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dateFormat = DateTimeFormat() # create instance of DateTimeFormat
    dateFormat.serialize('2019-01-01T14:45:29.123123+03:00')  # serialize datetime of first type
    dateFormat.serialize('2019-01-01T14:45:29.123123Z')  # serialize datetime of second type

# Generated at 2022-06-14 14:30:14.527991
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert isinstance(tf, TimeFormat) and isinstance(tf, BaseFormat)
    assert tf.validate('12:30:00') is not None and tf.validate('12:30') is not None
    #assert tf.validate('12:30:00') is datetime.time and tf.validate('12:30') is datetime.time
    assert tf.validate('12:30:00.000001') is not None
    assert tf.validate('12:30:00.0000') is not None
    #assert tf.validate('12:30:00.000001') is datetime.time and tf.validate('12:30:00.0000') is datetime.time


# Generated at 2022-06-14 14:30:23.215094
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    import datetime
    fmt = DateTimeFormat()
    assert fmt.serialize(datetime.datetime(2020, 1, 1, 7, 5)) == '2020-01-01T07:05:00'
    assert fmt.serialize(datetime.datetime(2020, 1, 1, 7, 5, 5)) == '2020-01-01T07:05:05'
    assert fmt.serialize(datetime.datetime(2020, 1, 1, 7, 5, 5, 111111)) == '2020-01-01T07:05:05.111111'
    assert fmt.serialize(datetime.datetime(2020, 1, 1, 7, 5, 5, 111111, tzinfo = datetime.timezone.utc)) == '2020-01-01T07:05:05.111111Z'


#

# Generated at 2022-06-14 14:30:32.797262
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    datetimeObject = datetime.datetime(2018, 4, 27, 12, 15, 23, 687000)
    assert DateTimeFormat().serialize(datetimeObject) == '2018-04-27T12:15:23.687000'


# Generated at 2022-06-14 14:30:43.615571
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    instance = DateTimeFormat()
    test_obj = datetime.datetime(2019, 1, 31, 0, 0, 0, tzinfo=datetime.timezone.utc)
    assert instance.serialize(test_obj) == "2019-01-31T00:00:00+00:00"
    print("test avec objet datetime ok")
    test_obj = datetime.datetime(2018, 2, 28, 2, 0, 0, tzinfo=datetime.timezone.utc)
    assert instance.serialize(test_obj) == "2018-02-28T02:00:00+00:00"
    print("test avec objet datetime ok")

# Generated at 2022-06-14 14:30:45.764888
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2019-05-09') == datetime.date(2019, 5, 9)



# Generated at 2022-06-14 14:30:53.976189
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate('2020-07-11') == datetime.date(2020, 7, 11)
    assert df.validate('2020-07-31') == datetime.date(2020, 7, 31)
    assert df.validate('2020-1-1') == datetime.date(2020, 1, 1)
    assert df.validate('2020-12-1') == datetime.date(2020, 12, 1)
    assert df.validate('2020-12-31') == datetime.date(2020, 12, 31)
    assert df.validate('2020-07-31') == datetime.date(2020, 7, 31)
    assert df.validate('2020-08-23') == datetime.date(2020, 8, 23)

# Generated at 2022-06-14 14:30:56.666083
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate('1098-03-02') == datetime.date(1098, 3, 2)


# Generated at 2022-06-14 14:31:02.031400
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date = datetime.datetime(2013, 1, 29, 20, 59, 59, tzinfo=datetime.timezone.utc)
    date_format = DateTimeFormat()
    assert date_format.serialize(date) == "2013-01-29T20:59:59Z"

# Generated at 2022-06-14 14:31:10.684565
# Unit test for method validate of class TimeFormat

# Generated at 2022-06-14 14:31:14.716644
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    time_obj = datetime.datetime(2019, 9, 3, 11, 58, 9, 583000, tzinfo=datetime.timezone.utc)
    time_str = DateTimeFormat().serialize(time_obj)
    assert time_str == "2019-09-03T11:58:09.583000Z"


# Generated at 2022-06-14 14:31:20.691713
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime(year=2016,month=4,day=1,hour=11,minute=12,second=13, microsecond=140000)
    
    df = DateTimeFormat()
    assert df.serialize(dt) == dt.isoformat()

# Generated at 2022-06-14 14:31:27.262123
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # test case 1
    obj1 = datetime.datetime(2020, 1, 1, 0, 0)
    value1 = DateTimeFormat().serialize(obj1)
    assert value1 == "2020-01-01T00:00:00"

    # test case 2
    obj2 = datetime.datetime(2019, 1, 1, 0, 0)
    value2 = DateTimeFormat().serialize(obj2)
    assert value2 == "2019-01-01T00:00:00"

# Generated at 2022-06-14 14:31:42.706142
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate("2019-11-05") == datetime.date(year=2019, month=11, day=5)



# Generated at 2022-06-14 14:31:48.057145
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime(2019, 12, 2, 11, 11, 11, tzinfo=datetime.timezone.utc)
    ret = DateTimeFormat().serialize(dt)
    assert ret == "2019-12-02T11:11:11+00:00"

# Generated at 2022-06-14 14:31:52.705179
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # arrange
    value = "2020-02-28T10:37:10Z"
    my_dt = DateTimeFormat().validate(value)
    

    # act
    returned_value = DateTimeFormat().serialize(my_dt)

    # assert
    assert returned_value == value

# Generated at 2022-06-14 14:31:57.778511
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from typesystem.base import Model, String
    from typesystem.types import DateTime

    class TestModel(Model):
        datetime = DateTime(format="date-time")

    model = TestModel()

    assert model.serialize({"datetime": "2015-07-31T12:23:34.095Z"}) == {
        "datetime": "2015-07-31T12:23:34.095000Z"
    }

# Generated at 2022-06-14 14:32:01.817516
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2018, 1, 1, 0, 0, 0, 0)) == "2018-01-01T00:00:00"

# Generated at 2022-06-14 14:32:05.516440
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dtf = DateTimeFormat()
    value = dtf.serialize(datetime.datetime.utcfromtimestamp(0))
    assert value == "1970-01-01T00:00:00Z"


# Generated at 2022-06-14 14:32:09.385778
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime(year=2019, month=1, day=1, hour=1, minute=1, second=1)
    df = DateTimeFormat()
    assert df.serialize(dt) == "2019-01-01T01:01:01"

# Generated at 2022-06-14 14:32:20.617148
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    formatted_time = TimeFormat()
    
    assert str(formatted_time.validate('00:00:00.000000')) == '00:00:00'
    assert str(formatted_time.validate('12:34:56.123456')) == '12:34:56.123456'
    assert str(formatted_time.validate('23:59:59.999999')) == '23:59:59.999999'
    assert str(formatted_time.validate('01:01:01')) == '01:01:01'

    try:
        formatted_time.validate('24:00:00')
        assert False
    except ValidationError:
        assert True
    

# Generated at 2022-06-14 14:32:22.242101
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("2020-03-03") == datetime.date(2020, 3, 3)


# Generated at 2022-06-14 14:32:26.234794
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
	df = DateFormat()
	assert_equals(
		df.validate("2019-11-20"),
		datetime.date(2019, 11, 20)
	)


# Generated at 2022-06-14 14:32:43.583825
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    test_DateFormat = DateFormat()
    assert test_DateFormat.validate("2019-01-01") == datetime.date(2019, 1, 1)
    assert test_DateFormat.validate("2020-02-02") == datetime.date(2020, 2, 2)


# Generated at 2022-06-14 14:32:53.525163
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    try:
        value = datetime.datetime(2000, 1, 1, tzinfo=datetime.timezone.utc)
        assert DateFormat().validate(value) == value.astimezone().date()

        value = datetime.date(2000, 1, 1)
        assert DateFormat().validate(value) == value

        value = "2000-01-01"
        assert DateFormat().validate(value) == datetime.date(2000, 1, 1)

        value = "2000-1-1"
        assert DateFormat().validate(value) == datetime.date(2000, 1, 1)
    except ValidationError:
        assert False  # pragma: no cover


# Generated at 2022-06-14 14:33:06.296724
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t = TimeFormat()
    assert t.validate("01:02:03") == datetime.time(hour=1, minute=2, second=3)
    assert t.validate("01:02:03.123456") == datetime.time(hour=1, minute=2, second=3, microsecond=123456)
    assert t.validate("01:02:03.123") == datetime.time(hour=1, minute=2, second=3, microsecond=123000)
    assert t.validate("01:02:03.1") == datetime.time(hour=1, minute=2, second=3, microsecond=100000)
    assert t.validate("01:02:03.12") == datetime.time(hour=1, minute=2, second=3, microsecond=120000)

# Generated at 2022-06-14 14:33:18.179433
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    fmt = DateTimeFormat()
    assert fmt.validate('2012-04-23T18:25:43.511Z') == datetime.datetime(2012, 4, 23, 18, 25, 43, 511000, tzinfo=datetime.timezone.utc)
    assert fmt.validate('2012-04-23T18:25:43.511+00:00') == datetime.datetime(2012, 4, 23, 18, 25, 43, 511000, tzinfo=datetime.timezone.utc)
    assert fmt.validate('2012-04-23T18:25:43.511-07:00') == datetime.datetime(2012, 4, 23, 18, 25, 43, 511000, tzinfo=datetime.timezone(datetime.timedelta(hours=-7)))


# Generated at 2022-06-14 14:33:20.494587
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert (DateFormat().validate('2000-01-01')) == datetime.date(2000, 1, 1)
