

# Generated at 2022-06-14 14:23:42.165086
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():

    # year,month,day,hour,minute,second,microsecond,tzinfo
    # 2020-08-18T10:34:56.123456Z
    value = "2020-08-18T10:34:56.123456Z"
    res = DateTimeFormat().validate(value)
    print(res)
    assert res

# Generated at 2022-06-14 14:23:45.630088
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    tester = DateFormat()
    value = tester.validate("2020-01-04")
    expected = datetime.date(2020, 1, 4)
    assert expected == value



# Generated at 2022-06-14 14:23:49.680361
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    class TimeFormatTest(TimeFormat):
        pass

    test_class = TimeFormatTest()
    assert(test_class.serialize(datetime.datetime.now().time()) == '00:00:00')

    assert(test_class.serialize(None) == None)

# Generated at 2022-06-14 14:24:00.308604
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timefmt = TimeFormat()
    ## valid:
    assert timefmt.validate("09:15:57") == datetime.time(9, 15, 57)
    assert timefmt.validate("09:15") == datetime.time(9, 15)
    assert timefmt.validate("09:15:57.123456") == datetime.time(9, 15, 57, 123456)
    assert timefmt.validate("09:15:57.1234") == datetime.time(9, 15, 57, 123400)
    assert timefmt.validate("09:15:57.12345") == datetime.time(9, 15, 57, 123450)

# Generated at 2022-06-14 14:24:02.251209
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert df.validate("2020-01-07") == datetime.date(2020, 1, 7)


# Generated at 2022-06-14 14:24:05.699251
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
    test_time = datetime.datetime.strptime("07:21", '%H:%M').time()
    test_time_format = TimeFormat()
    print('TimeFormat.serialize: ' + test_time_format.serialize(test_time))


# Generated at 2022-06-14 14:24:13.631157
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    valid_uuid = UUIDFormat()
    uuid_obj1 = valid_uuid.validate("b5ea5b53-e0e6-4b3a-b3f2-5cf5f0f0d736")
    assert isinstance(uuid_obj1, uuid.UUID)
    try:
        valid_uuid.validate("b5ea5b53-e0e6-4b3a-b3f2s-5cf5f0f0d736")
    except ValidationError as error:
        assert error.code == "format"
    

# Generated at 2022-06-14 14:24:17.914811
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    d = DateTimeFormat()
    result = d.validate("2019-12-17T14:12:31Z")
    output_result = datetime.datetime(2019, 12, 17, 14, 12, 31, tzinfo=datetime.timezone.utc)
    assert result == output_result


# Generated at 2022-06-14 14:24:29.115171
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Check case: value is valid
    assert DateTimeFormat().validate("2009-01-12T01:30:00Z") == datetime.datetime(2009, 1, 12, 1, 30, 0, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate("2009-01-12T01:30:00+01:00") == datetime.datetime(2009, 1, 12, 1, 30, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=1)))
    assert DateTimeFormat().validate("2009-01-12T01:30:00-01:00") == datetime.datetime(2009, 1, 12, 1, 30, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-1)))
    assert Date

# Generated at 2022-06-14 14:24:39.393187
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()

# Generated at 2022-06-14 14:24:50.321539
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    _ = tf.validate("00:00:00.000000")
    _ = tf.validate("00:00:00.000000")
    _ = tf.validate("00:00:00")
    _ = tf.validate("00:00")

# Generated at 2022-06-14 14:25:02.235680
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    local_time = TimeFormat()

    assert local_time.validate('02:27:00') == datetime.time(2, 27)
    assert local_time.validate('23:59:00') == datetime.time(23, 59)
    
    with pytest.raises(ValidationError):
        local_time.validate('24:00:00')

    utc_time = TimeFormat()

    assert utc_time.validate('02:27:00Z') == datetime.time(2, 27, tzinfo=datetime.timezone(datetime.timedelta(0)))
    assert utc_time.validate('23:59:00Z') == datetime.time(23, 59, tzinfo=datetime.timezone(datetime.timedelta(0)))
    

# Generated at 2022-06-14 14:25:10.664019
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    fmt = TimeFormat()
    fmt.validate("12:30")
    fmt.validate("12:30:25")
    fmt.validate("12:30:25.432100")
    fmt.validate("12:30:25.000004")
    fmt.validate("12:30:25.000004")
    with pytest.raises(ValidationError):
        fmt.validate("123")
    with pytest.raises(ValidationError):
        fmt.validate("12:30:")
    with pytest.raises(ValidationError):
        fmt.validate("24:00:00")
    with pytest.raises(ValidationError):
        fmt.validate("12:60:00")

# Generated at 2022-06-14 14:25:18.265482
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime_format = DateTimeFormat()
    datetime_format.validate('2017-03-30T12:24:35Z')
    datetime_format.validate('2017-03-30T12:24:35.123456Z')
    datetime_format.validate('2017-03-30T12:24:35.123456+05:30')
    datetime_format.validate('2017-03-30T12:24:35.123456-05:30')


# Generated at 2022-06-14 14:25:26.330260
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Test data
    bad_data = "2017-21-12", "01:1:01"
    good_data = "2017-12-12", "01:01:01"

    # Allocation
    tfmt = TimeFormat()

    def func(value: str) -> datetime.time:
        return tfmt.validate(value)

    # Check good condition
    for data in good_data:
        func(data)

    # Check bad condition
    for data in bad_data:
        with pytest.raises(ValidationError):
            func(data)



# Generated at 2022-06-14 14:25:28.595805
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    expected = 'Must be a valid time format.'
    observed = TimeFormat().validate('23')
    assert(str(observed) == expected)


# Generated at 2022-06-14 14:25:35.713227
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date1 = "2020-01-20"
    date2 = "2020-01-001"
    date1_is_valid = True
    date2_is_valid = True

    dformat = DateFormat()
    try:
        dformat.validate(date1)
    except ValidationError:
        date1_is_valid = False

    try:
        dformat.validate(date2)
    except ValidationError:
        date2_is_valid = False

    assert date1_is_valid
    assert not date2_is_valid


# Generated at 2022-06-14 14:25:47.914584
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    data = DateFormat()
    assert data.validate("2000-01-01") == datetime.date(2000, 1, 1)
    assert data.validate("2000-12-31") == datetime.date(2000, 12, 31)
    assert data.validate("2000-02-29") == datetime.date(2000, 2, 29)
    try:
        data.validate("2000-02-30")
    except ValidationError:
        pass
    else:
        assert False, "should not reach"
    try:
        data.validate("2000-02-31")
    except ValidationError:
        pass
    else:
        assert False, "should not reach"
    try:
        data.validate("2000-02-29")
    except ValidationError:
        pass

# Generated at 2022-06-14 14:25:59.256240
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # test for normal input
    df = DateFormat()
    assert df.validate("2020-01-01") == datetime.date(2020, 1, 1)
    assert df.validate("2020-12-31") == datetime.date(2020, 12, 31)
    # test for wrong date
    with pytest.raises(ValidationError) as excinfo:
        df.validate("2020-13-31")
    assert excinfo.value.text == "Must be a real date."
    assert excinfo.value.code == "invalid"
    # test for wrong format
    with pytest.raises(ValidationError) as excinfo:
        df.validate("2020-13-1")
    assert excinfo.value.text == "Must be a valid date format."

# Generated at 2022-06-14 14:26:06.646038
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date_valid_1 = date_format.validate("1855-12-01")
    date_valid_2 = date_format.validate("2001-10-01")
    date_valid_3 = date_format.validate("2055-12-01")
    date_invalid_1 = date_format.validate("1855-12-02")
    date_invalid_2 = date_format.validate("2001-10-03")

    assert date_valid_3.month == 12

# Generated at 2022-06-14 14:26:19.046801
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    obj1 = TimeFormat()
    # time with seconds and microseconds
    time_str = '12:34:56.123456'
    time = obj1.validate(time_str)
    assert type(time) == datetime.time
    # time without seconds and microseconds
    time_str = '12:34'
    time = obj1.validate(time_str)
    assert time.strftime("%H:%M:%S.%f") == '12:34:00.000000'
    # time with seconds but without microseconds
    time_str = '12:34:56'
    time = obj1.validate(time_str)
    assert time.strftime("%H:%M:%S.%f") == '12:34:56.000000'
    # time with microseconds but without seconds

# Generated at 2022-06-14 14:26:21.453744
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    test = DateFormat()
    test.validate("2019-12-17")

# Generated at 2022-06-14 14:26:30.299721
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():

    dateTimeFormat = DateTimeFormat()
    # 'format'
    try:
        dateTimeFormat.validate('2018-05-0')
    except ValidationError as error:
        assert error.code == 'format'

    # 'invalid'
    try:
        dateTimeFormat.validate('2018-05-32')
    except ValidationError as error:
        assert error.code == 'invalid'

    # 'invalid'
    try:
        dateTimeFormat.validate('2018-02-30')
    except ValidationError as error:
        assert error.code == 'invalid'

    # 'invalid'
    try:
        dateTimeFormat.validate('2018-04-31')
    except ValidationError as error:
        assert error.code == 'invalid'

    # 'invalid'


# Generated at 2022-06-14 14:26:35.074714
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    f = DateTimeFormat()

    # test for string
    res = f.validate("2019-11-22T10:14:37Z")
    exp = datetime.datetime(2019, 11, 22, 10, 14, 37, tzinfo=datetime.timezone.utc)
    assert res == exp

    res = f.validate("2019-11-22T10:14:37+07")
    exp = datetime.datetime(2019, 11, 22, 3, 14, 37, tzinfo=datetime.timezone.utc)
    assert res == exp

    res = f.validate("2019-11-22T10:14:37")
    exp = datetime.datetime(2019, 11, 22, 10, 14, 37, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:26:43.566710
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # Case 1: Check value is None
    value = None
    assert DateTimeFormat().validate(value) == value

    # Case 2: Check value is datetime
    value = datetime.datetime.now()
    assert DateTimeFormat().validate(value) == value

    # Case 3: Check value is not datetime
    value = "12:24:01.000213Z"
    assert DateTimeFormat().validate(value) == datetime.datetime(
        12, 24, 1, 0, 0, 2, 13000, datetime.timezone.utc
    )


# Generated at 2022-06-14 14:26:45.140121
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    test = DateTimeFormat()
    test.validate('2018-01-01T12:30:59Z')

# Generated at 2022-06-14 14:26:47.270207
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    obj = DateTimeFormat()
    assert isinstance(obj.validate("2012-12-21T15:29:43+02:00"), datetime.datetime)

# Generated at 2022-06-14 14:26:59.508032
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    df = DateTimeFormat()
    assert df.validate("2019-06-18T07:55") == datetime.datetime(2019, 6, 18, 7, 55)
    assert df.validate("2019-06-18T07:55:10") == datetime.datetime(2019, 6, 18, 7, 55, 10)
    assert df.validate("2019-06-18T07:55:10.5") == datetime.datetime(2019, 6, 18, 7, 55, 10, 500000)
    assert df.validate("2019-06-18T07:55:10.5Z") == datetime.datetime(2019, 6, 18, 7, 55, 10, 500000, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:27:05.415770
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    print('test_DateTimeFormat_validate started')
    dtFormat = DateTimeFormat()
    print(dtFormat.validate('2019-08-21T12:07:07Z'))
    # raise Exception('test_DateTimeFormat_validate failed with exception')


# Generated at 2022-06-14 14:27:15.710304
# Unit test for method validate of class DateTimeFormat

# Generated at 2022-06-14 14:27:24.921052
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    validator = DateFormat()
    assert validator.validate('2020-09-08') == datetime.date(2020, 9, 8)
    assert validator.validate('2020-10-11') == datetime.date(2020, 10, 11)
    assert validator.validate('2019-11-12') == datetime.date(2019, 11, 12)
    assert validator.validate('2018-12-13') == datetime.date(2018, 12, 13)

    with pytest.raises(ValidationError) as error:
        # value = '2020-09-08a'
        validator.validate('2020-09-08a')
    assert 'format' in str(error.value)


# Generated at 2022-06-14 14:27:36.038096
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time_format = DateTimeFormat()
    try:
        date_time_format.validate("2019-01-01T12:30:45Z")
    except ValidationError:
        print("DateTimeFormat.validate has error")
    try:
        date_time_format.validate("2019-01-01T12:30:45+0245")
    except ValidationError:
        print("DateTimeFormat.validate has error")
    try:
        date_time_format.validate("2019-01-01T12:30:45-0245")
    except ValidationError:
        print("DateTimeFormat.validate has error")

# Generated at 2022-06-14 14:27:39.137025
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    m = re.search(DATE_REGEX, "2019-05-23")
    assert m.group(0) is not None

if __name__ == "__main__":
    test_DateTimeFormat_validate()

# Generated at 2022-06-14 14:27:42.495567
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert isinstance(TimeFormat().validate("16:20:30.123456"), datetime.time)
    assert isinstance(TimeFormat().validate("16:20:30"), datetime.time)
    assert isinstance(TimeFormat().validate("16:20"), datetime.time)



# Generated at 2022-06-14 14:27:54.568612
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    print(DateTimeFormat().validate("2018-09-23T15:04:06.123456+01:00"))
    print(DateTimeFormat().validate("2018-09-23T15:04:06.1234560"))
    print(DateTimeFormat().validate("2018-09-23T15:04:06.123456Z"))
    print(DateTimeFormat().validate("2018-09-23T15:04:06+02:00"))
    print(DateTimeFormat().validate("2018-09-23T15:04:06"))
    print(DateTimeFormat().validate("2018-09-23T15:04:06.123456-03:00"))
    print(DateTimeFormat().validate("2018-09-23T15:04:06.123456-03"))

    # datetime.datetime

# Generated at 2022-06-14 14:28:01.183660
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format = TimeFormat()
    assert format.validate('23:59:59.999999') == datetime.time(23, 59, 59, 999999)
    assert format.validate('23:59:59') == datetime.time(23, 59, 59)
    assert format.validate('23:59') == datetime.time(23, 59)
    assert format.validate('23') == datetime.time(23)

test_TimeFormat_validate()

# Generated at 2022-06-14 14:28:07.183476
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    formatter = DateTimeFormat()
    val = "1517-04-18T22:59:42.841Z"
    new_val = formatter.validate(val)
    assert isinstance(new_val, datetime.datetime)
    assert new_val.isoformat() == val


# Generated at 2022-06-14 14:28:09.865907
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = '2019-11-21'
    f = DateFormat()
    assert f.validate(value) == datetime.date(2019, 11, 21)


# Generated at 2022-06-14 14:28:13.466956
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    value = "1:00:30"
    time = TimeFormat()
    expected = datetime.time(1, 0, 30)
    actual = time.validate(value)
    assert actual == expected
    assert isinstance(actual, datetime.time)


# Generated at 2022-06-14 14:28:16.348057
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2019-01-06 14:19:41.111111+00:00") == "2019-01-06 14:19:41.111111+00:00"


# Generated at 2022-06-14 14:28:26.750460
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    assert(df.validate('2020-01-01') == datetime.datetime(2020, 1, 1).date())
    with pytest.raises(ValidationError):
        df.validate('2020-01-01aa')
    with pytest.raises(ValidationError):
        df.validate('2020-00-01')


# Generated at 2022-06-14 14:28:32.911281
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    try:
        result = format.validate("2018-01-02")
        assert result.day == 2
        assert result.month == 1
        assert result.year == 2018
    except ValidationError:
        raise AssertionError("Must be a valid date format.")

# Generated at 2022-06-14 14:28:41.910698
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # DateTimeFormat validator test with valid input
    dt = DateTimeFormat()
    assert datetime.timezone(datetime.timedelta(seconds=-28800)) == \
        dt.validate('2017-06-28T15:08:00-08:00').tzinfo

    # DateTimeFormat validator test with invalid input
    # dt = DateTimeFormat()
    # try:
    #   dt.validate('2017-06-28T15:08:00-8:00')
    # except ValidationError as e:
    #   assert 'format' == e.code

# Generated at 2022-06-14 14:28:53.991331
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()
    datetime_obj = format.validate('2019-01-01T10:10:10')
    assert(str(datetime_obj) == '2019-01-01 10:10:10')
    datetime_obj = format.validate('2019-01-01T10:10:10Z')
    assert(str(datetime_obj) == '2019-01-01 10:10:10+00:00')
    datetime_obj = format.validate('2019-01-01T10:10:10+08:00')
    assert(str(datetime_obj) == '2019-01-01 10:10:10+08:00')
    datetime_obj = format.validate('2019-01-01T10:10:10+08')

# Generated at 2022-06-14 14:29:01.596201
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    try:
        date1 = DateFormat().validate('2021-12-31')
        assert date1.year == 2021
        assert date1.month == 12
        assert date1.day == 31
    except ValueError:
        pass
    try:
        date1 = DateFormat().validate('2021-02-31')
        print(date1.year)
        assert date1.year == 2021
        assert date1.month == 2
        assert date1.day == 31
    except ValueError:
        pass
    try:
        date1 = DateFormat().validate('2021-02-31')
        print(date1.year)
        assert date1.year == 2021
        assert date1.month == 2
        assert date1.day == 31
    except ValueError:
        pass

# Generated at 2022-06-14 14:29:04.948468
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t=TimeFormat()
    time=t.validate("15:00")
    assert time == datetime.time(hour=15,minute=0)
    assert isinstance(time, datetime.time)


# Generated at 2022-06-14 14:29:10.556054
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():

    # Fixture.
    value = "2020-05-09T19:37:16Z"
    format_ = DateTimeFormat()

    # Action
    value_parsed = format_.validate(value)

    # Test
    assert datetime.datetime(2020, 5, 9, 19, 37, 16, tzinfo=datetime.timezone.utc) == value_parsed


# Generated at 2022-06-14 14:29:20.297423
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate('2018-04-22T00:00:00Z') == datetime.datetime(2018, 4, 22, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)
    #assert DateTimeFormat().validate('2018-04-22T00:00:00+0000') == datetime.datetime(2018, 4, 22, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)
    #assert DateTimeFormat().validate('2018-04-22T00:00:00+00:00') == datetime.datetime(2018, 4, 22, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)

# Generated at 2022-06-14 14:29:30.079682
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():

    f = TimeFormat()

    # Test time with seconds only
    cases = [
        ("01:02", datetime.time(hour=1, minute=2, second=0, microsecond=0)),
        ("12:34", datetime.time(hour=12, minute=34, second=0, microsecond=0)),
    ]
    for value, result in cases:
        assert f.validate(value) == result

    # Test time with seconds and microseconds

# Generated at 2022-06-14 14:29:36.400527
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # arrange
    fmt = DateFormat()
    test_data = "2020-02-01"

    # act
    result = fmt.validate(test_data)

    # assert
    assert type(result) is datetime.date
    assert result == datetime.date(2020, 2, 1)


# Generated at 2022-06-14 14:29:57.718740
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_val = time_format.validate('23:12:02')
    time_val_min = time_format.validate('12:2')
    time_val_min_sec = time_format.validate('12:2:23')
    time_val_min_sec_micro = time_format.validate('23:12:02.123456')
    time_val_min_sec_micro1 = time_format.validate('23:12:02.123400000')
    time_val_min_sec_micro2 = time_format.validate('23:12:02.123')
    assert isinstance(time_val, datetime.time)
    assert isinstance(time_val_min, datetime.time)

# Generated at 2022-06-14 14:30:02.379748
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    try:
        df.validate('2020-04-31')
    except Exception as e:
        assert(e.code == 'invalid')
        assert(e.args == ('Must be a real date.',))


# Generated at 2022-06-14 14:30:12.212061
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    """
    Teste case TimeFormat validate method.
    """
    # Arrange
    expected = [
        ("12:34", datetime.time(12, 34)),
        ("12:34:56", datetime.time(12, 34, 56)),
        ("12:34:56.123456", datetime.time(12, 34, 56, 123456)),
    ]

    # Act
    actual = [
        TimeFormat().validate(d) for d, result in expected
    ]

    # Assert
    assert actual == [obj for _, obj in expected]

# Generated at 2022-06-14 14:30:15.728421
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    obj = TimeFormat()
    assert obj.validate("00:00:00") == datetime.time(0, 0)
    assert obj.validate("01:01:01.000001") == datetime.time(1, 1, 1, 1)

# Generated at 2022-06-14 14:30:24.117167
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Matching value
    assert TimeFormat().validate('00:00:00.000000') == datetime.time(0, 0, 0, 0)
    assert TimeFormat().validate('23:59:59.999999') == datetime.time(23, 59, 59, 999999)
    assert TimeFormat().validate('00:00:00') == datetime.time(0, 0, 0)
    assert TimeFormat().validate('23:59:59') == datetime.time(23, 59, 59)
    assert TimeFormat().validate('00:00') == datetime.time(0, 0)
    assert TimeFormat().validate('23:59') == datetime.time(23, 59)

    # Non matching value

# Generated at 2022-06-14 14:30:26.770859
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateformat = DateFormat()
    date = dateformat.validate("2020-12-31")
    print(date)


# Generated at 2022-06-14 14:30:31.324618
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    '''
    Method tests validate method of TimeFormat class (it is valid case)
    '''
    # Create TimeFormat instance
    time = TimeFormat()
    
    # Assert method validate returns value equals to value of method validate
    assert time.validate("01:02:03.123456") == time.validate("01:02:03.123456")


# Generated at 2022-06-14 14:30:34.400865
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format = TimeFormat()
    test = "12:34"
    expected = datetime.time(12, 34, 0)
    assert format.validate(test) == expected

# Generated at 2022-06-14 14:30:38.752011
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    time_str = "2020-06-03T19:48:40.958390Z"

    assert DateTimeFormat().validate(time_str) == datetime.datetime(2020, 6, 3, 19, 48, 40, 958390, datetime.timezone.utc)

# Generated at 2022-06-14 14:30:47.845498
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    # Value is not string
    with pytest.raises(TypeError, match="Value must be a string."):
        date_format.validate(2)
    # Value is string of date with wrong format
    with pytest.raises(ValidationError, match="Must be a valid date format."):
        date_format.validate("year-month-day")
    # Value is string of date with wrong value
    with pytest.raises(ValidationError, match="Must be a real date."):
        date_format.validate("2020-13-02")
    # Value is string of date with correct value
    assert date_format.validate("2020-12-02") == datetime.date(2020, 12, 2)


# Generated at 2022-06-14 14:31:05.577780
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # test 'HH:MM:SS.ffffff'
    tf = TimeFormat()
    assert tf.validate("00:00:00.000000") == datetime.time(0,0,0)

    # test 'HH:MM:SS'
    assert tf.validate("12:00:00") == datetime.time(12,0,0)

    # test 'HH:MM'
    assert tf.validate("14:00") == datetime.time(14, 0, 0)

    # test 'HH'
    assert tf.validate("02") == datetime.time(2, 0, 0)

    # test microsecond is None
    assert tf.validate("01:01:01") == datetime.time(1, 1, 1)

# Generated at 2022-06-14 14:31:08.892179
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    value = "2020-01-01"
    assert df.validate(value).strftime("%Y-%m-%d") == value
    
    

# Generated at 2022-06-14 14:31:12.724585
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    """
    Method Name: validate
    Purpose: Modify validate method of class DateFormat
    Parameters: self, value
    Returns: datetime.date or ValidationError
    """
    try:
        validate = DateFormat.validate
        validate(DateFormat(), "2020-06-11")
        assert True
    except Exception as e:
        assert False, e
 

# Generated at 2022-06-14 14:31:17.483765
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():

    obj = DateTimeFormat()
    try:
        obj.validate("2020-03-27T21:00:00.000Z")
        print("SUCCESS")
    except ValidationError:
        print("FAIL")

    try:
        obj.validate("2020-03-27T22:00:00.000Z")
        print("FAIL")
    except ValidationError:
        print("SUCCESS")

if __name__ == "__main__":
    test_DateTimeFormat_validate()

# Generated at 2022-06-14 14:31:27.349261
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    testobj = TimeFormat()
    testdata = [
        ('08:12:01.345', datetime.time(8, 12, 1, 345000)),
        ('08:12:01.3', datetime.time(8, 12, 1, 300000)),
        ('08:12:01', datetime.time(8, 12, 1, 0)),
        ('08:12', datetime.time(8, 12, 0, 0)),
        ('08:12:01.345678', datetime.time(8, 12, 1, 345678)),
    ]
    for input_value, expected_result in testdata:
        actual_result = testobj.validate(input_value)
        assert actual_result == expected_result


# Generated at 2022-06-14 14:31:31.560692
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d1 = DateFormat()
    assert d1.validate('2019-01-31') == datetime.date(2019, 1, 31)
    assert d1.validate('2018-03-28') == datetime.date(2018, 3, 28)



# Generated at 2022-06-14 14:31:38.535429
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Verify that the DateFormat class can validate a value string according to the YYYY-MM-DD format.
    # Given a value string according to the YYYY-MM-DD format
    value = "2019-08-11"
    dateFormat = DateFormat()

    # When I validate the given value string
    actual = dateFormat.validate(value)

    # Then the datetime.date object is returned.
    expected = datetime.date(2019, 8, 11)
    assert actual == expected



# Generated at 2022-06-14 14:31:45.271921
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    f = DateFormat()
    with pytest.raises(ValidationError) as e:
        f.validate('2019-50-0')
    assert 'Must be a real date' in str(e.value)
    assert 'invalid' in str(e.value)

    with pytest.raises(ValidationError) as e:
        f.validate('2019-03-01:')
    assert 'Must be a valid date format' in str(e.value)
    assert 'format' in str(e.value)

    with pytest.raises(ValidationError) as e:
        f.validate('2019')
    assert 'Must be a valid date format' in str(e.value)
    assert 'format' in str(e.value)


# Generated at 2022-06-14 14:31:56.077454
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    def assert_valid(value):
        time_format = TimeFormat()
        timestamp = time_format.validate(value)
        assert isinstance(timestamp, datetime.time)

    def assert_invalid(value):
        time_format = TimeFormat()
        with pytest.raises(ValidationError):
            time_format.validate(value)

    assert_valid('05:00')
    assert_valid('05:00:00')
    assert_valid('05:00:00.1')
    assert_valid('05:00:00.123456')
    assert_valid('05:00:00.999999')

    assert_invalid('5:00')
    assert_invalid('05:0')
    assert_invalid('5:0')
    assert_invalid('5:00:00')

# Generated at 2022-06-14 14:32:00.306251
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    assert date_format.validate("2019-04-03") == datetime.date(2019, 4, 3)
    assert date_format.validate("2019-04-03") == datetime.date(2019, 4, 3)



# Generated at 2022-06-14 14:32:24.108390
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    date_time = datetime.datetime(year=2019, month=1, day=1, hour=0, minute=0, second=0)
    date_time_offset = datetime.datetime(year=2019, month=1, day=1, hour=0, minute=0, second=0, tzinfo=datetime.timezone(datetime.timedelta(hours=2, minutes=0)))

    # the utc and offset date_time instances must match
    date_time_to_match = date_time.replace(tzinfo=datetime.timezone.utc)
    date_time_offset_to_match = date_time_offset.replace(tzinfo=datetime.timezone.utc)  # type: ignore
    assert date_time_to_match == date_time_offset_to_match
    

# Generated at 2022-06-14 14:32:36.009837
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    import datetime
    f = DateFormat()

    assert f.validate("2019-01-01") == datetime.date(2019, 1, 1)
    assert f.validate("2019-1-01") == datetime.date(2019, 1, 1)
    assert f.validate("2019-01-1") == datetime.date(2019, 1, 1)
    assert f.validate("2019-1-1") == datetime.date(2019, 1, 1)

    # Error messages
    try:
        f.validate("2019-01-01T00:00:00Z")
    except ValidationError as e:
        assert e.text == "Must be a valid date format."
        assert e.code == "format"


# Generated at 2022-06-14 14:32:38.670732
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    date.validate('2020-05-11')
    try:
        date.validate('2020-05-32')
    except ValidationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:32:41.211817
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert(DateFormat().validate('2020-01-06') == datetime.date(2020, 1, 6))


# Generated at 2022-06-14 14:32:44.400411
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    datetime = DateTimeFormat().validate("2020-01-01T01:01:01.012345Z")
    print(datetime)


# Generated at 2022-06-14 14:32:54.060350
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    """
    # test case 1
    check function returns right value with right input
    """
    time = TimeFormat()
    result = time.validate("12:00:00")
    assert isinstance(result, datetime.time)
    assert result.minute == 0
    """
    # test case 2
    check function returns right value with right input
    """
    result = time.validate("00:00:00.000000")
    assert isinstance(result, datetime.time)
    assert result.minute == 0
    """
    # test case 3
    check function returns exception with wrong input
    """
    time.validate("12:00")
    """
    # test case 4
    check function returns exception with wrong input
    """
    time.validate("13:00:00")


# Generated at 2022-06-14 14:32:58.255662
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateformat = DateFormat()
    date_text = dateformat.validate("2019-05-12")
    assert str(date_text) == "2019-05-12"
    assert isinstance(date_text, datetime.date)



# Generated at 2022-06-14 14:33:01.240163
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = TimeFormat()
    assert time.validate('10:00') == datetime.time(10, 0)


# Generated at 2022-06-14 14:33:13.922339
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateFormat = DateFormat()
    
    # Validate a valid date format
    try:
        assert dateFormat.validate("1999-01-01") == datetime.date(1999,1,1)
    except ValidationError:
        assert False

    # Invalid date format
    try:
        dateFormat.validate("1999-01-01T01:01:01")
        assert False
    except ValidationError as e:
        assert str(e) == "Must be a valid date format."
        assert str(e.code) == "format"

    # Invalid date
    try:
        dateFormat.validate("2019-02-29")
        assert False
    except ValidationError as e:
        assert str(e) == "Must be a real date."
        assert str(e.code) == "invalid"




# Generated at 2022-06-14 14:33:18.216022
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    obj = TimeFormat()
    data = obj.validate("10:20:30.010")
    assert data == datetime.time(10, 20, 30, 10000)
    assert data.microsecond == 10000
    assert data.tzname() is None
    assert not data.fold
