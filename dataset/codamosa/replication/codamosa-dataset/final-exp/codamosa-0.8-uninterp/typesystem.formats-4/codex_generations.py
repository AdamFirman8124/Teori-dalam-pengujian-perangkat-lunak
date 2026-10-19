

# Generated at 2022-06-14 14:23:37.190147
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    data = {'year': 2020, 'month': 3, 'day': 12, 'tzinfo': '+10:00'}
    datetime_format = DateTimeFormat()
    assert datetime_format.validate("2020-03-12+10:00:00") == datetime.datetime(**data)

# Generated at 2022-06-14 14:23:45.387383
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
#     """
#     test for UUIDFormat validate method
#     """
    uuid_instance = UUIDFormat()
    UUID_TEST = '9c04a4e6-7c83-4f58-a2e8-cd805518fb68'
    assert uuid_instance.validate(UUID_TEST).hex == UUID_TEST
    assert str(uuid_instance.validate(UUID_TEST)) == UUID_TEST



# Generated at 2022-06-14 14:23:56.695566
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    formatter = DateTimeFormat()
    assert isinstance(formatter.validate("2018-01-31T22:30:00Z"), datetime.datetime)
    assert isinstance(formatter.validate("2018-01-31T22:30:00"), datetime.datetime)
    assert isinstance(formatter.validate("2018-01-31T22:30:00+01:00"), datetime.datetime)
    assert isinstance(formatter.validate("2018-01-31T22:30:00+01"), datetime.datetime)
    assert isinstance(formatter.validate("2018-01-31T22:30:00.123456Z"), datetime.datetime)

# Generated at 2022-06-14 14:24:05.699224
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dateTimeFormat = DateTimeFormat()
    dateTimeFormat.validate('2018-05-06T20:16:47.222000Z')
    dateTimeFormat.validate('2018-05-06T20:16:47.222000+00:00')
    dateTimeFormat.validate('2018-05-06T20:16:47.222000+08')
    dateTimeFormat.validate('2018-05-06T20:16:47.222000-08:30')
    dateTimeFormat.validate('2018-05-06T20:16:47.222000+0830')
    dateTimeFormat.validate('2018-05-06T20:16:47+08')
    dateTimeFormat.validate('2018-05-06T20:16+08')

# Generated at 2022-06-14 14:24:09.199365
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    from typesystem.datetime import DateTimeFormat

    datetime_format = DateTimeFormat()

    datetime_format.validate('2019-09-30T18:05:22.152712+00:00')

# Generated at 2022-06-14 14:24:15.851886
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # When
    time_format = TimeFormat()

    # Then
    assert isinstance(time_format.validate("00:01"), datetime.time)
    assert isinstance(time_format.validate("01:00"), datetime.time)
    assert isinstance(time_format.validate("12:00"), datetime.time)
    assert isinstance(time_format.validate("12:00:00"), datetime.time)
    assert isinstance(time_format.validate("12:00:00.123456"), datetime.time)



# Generated at 2022-06-14 14:24:21.838633
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime.strptime('2020-05-29T08:47:28+05:30','%Y-%m-%dT%H:%M:%S%z')) == '2020-05-29T08:47:28+05:30'
    assert DateTimeFormat().serialize(datetime.datetime.strptime('2020-05-29T08:47:28+05:00','%Y-%m-%dT%H:%M:%S%z')) == '2020-05-29T08:47:28+05:00'

# Generated at 2022-06-14 14:24:26.229585
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_to_validate = "2020-06-26"
    date_format = DateFormat()
    date = date_format.validate(date_to_validate)
    assert date == datetime.date(2020, 6, 26)


# Generated at 2022-06-14 14:24:33.073241
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    test_cases = [
        ('2019-01-01T01:00:00Z', datetime.datetime(2019, 1, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)),
        ('2019-01-01T01:00:00+01:30', datetime.datetime(2019, 1, 1, 1, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=1, minutes=30)))),
        ('2019-01-01T01:00:00-01:30', datetime.datetime(2019, 1, 1, 1, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-1, minutes=-30))))
    ]

    for string, target in test_cases:
        test_class = Date

# Generated at 2022-06-14 14:24:34.975723
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    date_time_value = date_time_format.validate("2019-10-01T23:59:59Z")
    assert date_time_format.serialize(date_time_value) == "2019-10-01T23:59:59Z"


# Generated at 2022-06-14 14:24:41.275025
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date = datetime.date(year=2020, month=1, day=1)
    assert DateFormat().serialize(date) == "2020-01-01"


# Generated at 2022-06-14 14:24:44.116723
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    assert DateFormat().serialize(datetime.date(2020,1,1)) == "2020-01-01"


# Generated at 2022-06-14 14:24:47.773322
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value1 = "2020-01-01"
    value2 = "2019-09-10"
    res1 = DateFormat().validate(value1)
    res2 = DateFormat().validate(value2)
    assert res1 == res2


# Generated at 2022-06-14 14:24:51.304036
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    input_value_1 = '00:00'
    input_value_2 = '00:00:00:00'
    assert time_format.validate(input_value_1) == datetime.time(0)
    assert time_format.validate(input_value_2) == datetime.time(0)

# Generated at 2022-06-14 14:24:57.507666
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    # Test if input is of type datetime.date
    assert df.is_native_type(datetime.date(2018, 11, 21)) == True
    # Test if input is not of type datetime.date
    assert df.is_native_type(datetime.date(2018, 1, 21)) == True


# Generated at 2022-06-14 14:24:59.356716
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    assert DateFormat().serialize(datetime.date(2020,11,17)) == '2020-11-17'

# Generated at 2022-06-14 14:25:02.650609
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    format = DateFormat()
    assert format.serialize(None) is None
    assert format.serialize(datetime.date(2015, 2, 3)) == "2015-02-03"


# Generated at 2022-06-14 14:25:08.903979
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    tf.validate("00:00:00.00")
    tf.validate("00:00:00.00Z")
    tf.validate("00:00:00.001Z")
    tf.validate("00:00:00.01Z")
    tf.validate("00:00:00.01")
    tf.validate("00:00:00.101")
    tf.validate("00:00:00.10")
    tf.validate("00:00:00.012345")

# Generated at 2022-06-14 14:25:19.806555
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf1 = TimeFormat()
    assert tf1.validate('23:01:11.123456') == datetime.time(23, 1, 11, 123456)
    assert tf1.validate('23:01') == datetime.time(hour=23, minute=1)
    assert tf1.validate('23') == datetime.time(hour=23)
    assert tf1.validate('23:') == datetime.time(hour=23)
    assert tf1.validate('23:01:') == datetime.time(hour=23, minute=1)
    assert tf1.validate('23:01:11') == datetime.time(hour=23, minute=1, second=11)

# Generated at 2022-06-14 14:25:23.825913
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date = date_format.validate('2019-08-28')
    assert date == datetime.date(2019, 8, 28)
    with pytest.raises(ValidationError):
        date = date_format.validate('2019-08-32')


# Generated at 2022-06-14 14:25:28.380921
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert tf.validate("23:59:59.999999") == datetime.time(23, 59, 59, 999999)


# Generated at 2022-06-14 14:25:30.476057
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date = datetime.date(2020,2,24)
    assert DateFormat().serialize(date) == "2020-02-24"


# Generated at 2022-06-14 14:25:31.986569
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
	assert serialize(obj) == None

# Generated at 2022-06-14 14:25:39.944434
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    expected = datetime.time(12, 34, 56)
    assert tf.validate("12:34:56") == expected
    assert tf.validate("12:34") == datetime.time(12, 34)
    assert tf.validate("12:34:56.789") == expected
    assert tf.validate("12:34:56.789000") == expected
    assert tf.validate("12:34:56.789000000") == expected
    assert tf.validate("12:34:56.000789") == expected
    assert tf.validate("12:34:56.78900") == expected
    assert tf.validate("12:34:56.7890000") == expected
    assert tf.validate("12:34:56.789") == expected


# Generated at 2022-06-14 14:25:52.535766
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    DateFormat().serialize(datetime.date(2019, 4, 15))
    DateFormat().serialize(datetime.date(2020, 4, 20))
    DateFormat().serialize(datetime.date(2021, 4, 20))
    DateFormat().serialize(datetime.date(2022, 4, 20))
    DateFormat().serialize(datetime.date(2023, 4, 20))
    DateFormat().serialize(datetime.date(2024, 4, 20))
    DateFormat().serialize(datetime.date(2025, 4, 20))
    DateFormat().serialize(datetime.date(2026, 4, 20))
    DateFormat().serialize(datetime.date(2027, 4, 20))
    DateFormat().serialize(datetime.date(2028, 4, 20))
   

# Generated at 2022-06-14 14:25:55.826910
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    data = DateFormat()
    assert data.serialize(datetime.date(1999, 12, 1)) == '1999-12-01'
    assert data.serialize(None) == None

# Generated at 2022-06-14 14:26:00.353261
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    result = DateFormat().validate('2019-01-01')
    assert result == datetime.date(2019, 1, 1)



# Generated at 2022-06-14 14:26:02.931244
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    df = DateFormat()
    assert df.serialize(datetime.date(2020, 2, 28)) == "2020-02-28"
    assert df.serialize(None) == None


# Generated at 2022-06-14 14:26:10.585386
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d = DateFormat()
    date1 = d.validate('2020-09-15')
    assert date1 == datetime.date(2020, 9, 15)

    # Invalid date
    try:
        d.validate('2020-13-25')
    except ValidationError:
        # assert str(err) == d.errors['invalid']
        assert d.errors['invalid'] == "Must be a real date."
    else:
        raise AssertionError('Exception not thrown')

    # Invalid format
    try:
        d.validate('abc')
    except ValidationError:
        # assert str(err) == d.errors['format']
        assert d.errors['format'] == "Must be a valid date format."
    else:
        raise AssertionError('Exception not thrown')

    

# Generated at 2022-06-14 14:26:13.700312
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2019-12-31') is not None
    assert DateFormat().validate('2019-12-31') == datetime.date(year=2019, month=12, day=31)


# Generated at 2022-06-14 14:26:23.146555
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    with pytest.raises(ValidationError):
        df.validate("not-date")

    result = df.validate("2019-09-10")
    assert isinstance(result, datetime.date)
    assert result == datetime.date(2019, 9, 10)



# Generated at 2022-06-14 14:26:31.167395
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    df = DateFormat()
    # Check valid dates
    assert df.validate("2019-01-09") == datetime.date(2019, 1, 9)
    assert df.validate("2019-12-31") == datetime.date(2019, 12, 31)

    # Check invalid dates
    with pytest.raises(ValidationError):
        df.validate("2009-99-99")
    with pytest.raises(ValidationError):
        df.validate("2009-13-32")
    with pytest.raises(ValidationError):
        df.validate("2019-12-32")
    with pytest.raises(ValidationError):
        df.validate("2019-11-31")

# Generated at 2022-06-14 14:26:34.339544
# Unit test for method validate of class DateFormat
def test_DateFormat_validate(): 
    format = DateFormat()
    valueDateDs = '2020-01-28'
    valueDateCpasDs = '2020-01-29'
    objDate = format.validate(valueDateDs)
    objDateCpas = format.validate(valueDateCpasDs)
    assert objDate == datetime.date(2020, 1, 28)
    assert objDateCpas == datetime.date(2020, 1, 29)
    assert objDate < objDateCpas


# Generated at 2022-06-14 14:26:39.435920
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    """
    Test for method validate of class TimeFormat
    """
    tf = TimeFormat()
    assert tf.validate('08:30:00.000000')
    assert tf.validate('08:30:00.101010')
    assert tf.validate('08:30:00.101')
    assert tf.validate('08:30:00')
    assert tf.validate('08:30')
    assert tf.validate('08')

# Generated at 2022-06-14 14:26:42.551357
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateformat = DateFormat()
    print(dateformat.validate('2020-01-30'))


# Generated at 2022-06-14 14:26:45.305667
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    data = datetime.date(2015,5,19)
    obj = DateFormat()
    result = obj.serialize(data)
    assert result=="2015-05-19"


# Generated at 2022-06-14 14:26:49.223563
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date_format = DateFormat()
    date_result = date_format.serialize(datetime.date(2020, 5, 6))
    # assertEqual is used to test if the two inputs are equal in value.
    # It can also test if the two inputs are the same in reference.
    assertEqual(date_result, '2020-05-06')

test_DateFormat_serialize()



# Generated at 2022-06-14 14:26:54.023429
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    obj = datetime.date(year=2020, month=11, day=20)
    assert DateFormat().serialize(obj) == '2020-11-20'
    assert DateFormat().serialize(None) == None



# Generated at 2022-06-14 14:26:56.364742
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    assert DateFormat().serialize(datetime.date(year=2020, month=5, day=15)) == "2020-05-15"

# Generated at 2022-06-14 14:26:59.191969
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    assert DateFormat().serialize(datetime.date(2019, 7, 27)) == '2019-07-27'
    assert DateFormat().serialize(None) == None



# Generated at 2022-06-14 14:27:10.191353
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    #Arrange
    #Expected result
    expectedResult: str = "2018-02-05"
    #Tested object creation
    testedObject = DateFormat()
    #Act
    testedResult = testedObject.serialize(datetime.datetime(2018, 2, 5))
    #Assert
    assert expectedResult == testedResult


# Generated at 2022-06-14 14:27:11.719608
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    value = tf.validate('11:11:11.111111')
    print(value)

if __name__ == "__main__":
    test_TimeFormat_validate()

# Generated at 2022-06-14 14:27:18.539496
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time = "10:12"
    tf = TimeFormat()
    assert tf.validate(time) == datetime.time(10, 12)

    time = "10:12:12"
    assert tf.validate(time) == datetime.time(10, 12, 12)

    time = "10:12:12.123456"
    assert tf.validate(time) == datetime.time(10, 12, 12, 123456)


# Generated at 2022-06-14 14:27:20.629197
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date = DateFormat()
    assert date.serialize(None) is None
    assert date.serialize(datetime.date.today()) == "2020-01-06"

# Generated at 2022-06-14 14:27:25.842679
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate("00:00:30") == datetime.time(0, 0, 30)
    assert TimeFormat().validate("12:10") == datetime.time(12, 10)
    assert TimeFormat().validate("01:02:03.002000") == datetime.time(1, 2, 3, 2000)


# Generated at 2022-06-14 14:27:30.489538
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date_format = DateFormat()

    real_date = datetime.date(2017,11,19)
    isoformat_date = '2017-11-19'
    
    serialize_date = date_format.serialize(real_date)

    assert isoformat_date == serialize_date



# Generated at 2022-06-14 14:27:33.804132
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date_format=DateFormat()
    date=(datetime.datetime.now()).date()
    assert date_format.serialize(date) is not None
    assert date_format.serialize(date) is not int

# Generated at 2022-06-14 14:27:40.614865
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.types.time import TimeFormat
    
    dt = TimeFormat()
    str_t = "14:36:30.123456"
    obj_t = dt.validate(str_t)
    
    #obj_t is datetime.time instance
    assert isinstance(obj_t, datetime.time)
    #hour
    assert obj_t.hour == 14
    #minute
    assert obj_t.minute == 36
    #second
    assert obj_t.second == 30
    #microsecond
    assert obj_t.microsecond == 123456
    
    

# Generated at 2022-06-14 14:27:43.017481
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    # test for obj is None
    d1 = DateFormat()
    assert d1.serialize(None) == None



# Generated at 2022-06-14 14:27:45.705841
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date_string = "2007-05-12"
    date = datetime.date(2007, 5, 12)
    assert DateFormat().serialize(date) == date_string


# Generated at 2022-06-14 14:27:56.369544
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    d = datetime.date(2020, 7, 2)
    try:
        DateFormat().serialize(d)
    except AssertionError as e:
        print(e)
        print("Test for method 'serialize' of class 'DateFormat' failed.")
        exit(1)


# Generated at 2022-06-14 14:28:04.609548
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    
    # Verify that the method DateFormat.validate raises the error "invalid"
    # when the input value is not a valid date
    assert DateFormat().validate("2000-45-45")=='Must be a real date.'
    
    # Verify that the method DateFormat.validate raises the error "format"
    # when the format of the input value is not correct
    assert DateFormat().validate("2000/45/45")=='Must be a valid date format.'
    
    # Verify that the method DateFormat.validate returns a date object if the
    # input value is a valid date and its format is correct
    assert type(DateFormat().validate("2000-03-03"))==datetime.date
    

# Generated at 2022-06-14 14:28:10.823334
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dfm = DateTimeFormat()
    dt = dfm.validate('2019-01-07T13:20:07.143028+00:00')
    assert dt.year == 2019
    assert dt.month == 1
    assert dt.day == 7
    assert dt.hour == 13
    assert dt.minute == 20
    assert dt.second == 7
    assert dt.microsecond == 143028

# Generated at 2022-06-14 14:28:15.576814
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    obj1 = '2020-01-01'
    obj2 = None
    result1 = DateFormat().serialize(obj1)
    assert isinstance(result1, str)
    assert result1 == "2020-01-01"
    result2 = DateFormat().serialize(obj2)
    assert isinstance(result2, type(obj2))
    assert result2 == obj2


# Generated at 2022-06-14 14:28:20.286351
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date = datetime.date(2020, 1, 1)
    format = DateFormat()
    assert format.serialize(date) == date.isoformat()


# Generated at 2022-06-14 14:28:23.745660
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    assert TimeFormat().validate('03:04:05') == datetime.time(3, 4, 5)
    assert TimeFormat().serialize(datetime.time(3, 4, 5)) == '03:04:05'

# Generated at 2022-06-14 14:28:26.491535
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    d1 = datetime.date(2019, 3, 4)
    D1 = DateFormat()
    assert D1.serialize(d1) == "2019-03-04"


# Generated at 2022-06-14 14:28:31.990686
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    df = DateFormat()
    assert "2020-05-01" == df.serialize(datetime.date(2020, 5, 1))

    # cannot test `None` because isinstance(None, datetime.date) => False


# Generated at 2022-06-14 14:28:37.712280
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    time_format.validate("12:59")
    time_format.validate("12:59:59")
    time_format.validate("12:59:59.123456")
    assert(str(time_format.validate("12:59:59.123456")) == "12:59:59.123456")

# Generated at 2022-06-14 14:28:40.417297
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    serialize_value=DateFormat().serialize(datetime.date(2020, 1, 2))
    assert(serialize_value=="2020-01-02")


# Generated at 2022-06-14 14:28:59.232191
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    d = DateFormat()
    d.validate("2019-8-5")
    today = datetime.date.today()
    assert(d.serialize(today) == '%d-%d-%d' % (today.year, today.month, today.day))


# Generated at 2022-06-14 14:29:08.467033
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    f = TimeFormat()
    assert f.validate("00:00:00.00000") == datetime.time(0, 0, 0)
    assert f.validate("00:00:00.001") == datetime.time(0, 0, 0, 1000)
    assert f.validate("00:00:00.111111") == datetime.time(0, 0, 0, 111111)
    assert f.validate("00:00:00") == datetime.time(0, 0, 0)
    assert f.validate("00:00") == datetime.time(0, 0)
    assert f.validate("12:34:56.654321") == datetime.time(12, 34, 56, 654321)

# Generated at 2022-06-14 14:29:12.849479
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate("12:00") == datetime.time(12,0)
    assert time_format.validate("12:00:00.000000") == datetime.time(12,0)
    assert time_format.validate("12:00:00") == datetime.time(12,0)
    assert time_format.validate("00:00:00") == datetime.time(0, 0)

# Generated at 2022-06-14 14:29:20.888050
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test case 1
    print("Test case 1")
    format = DateFormat()
    print("Result:", format.validate("2020-02-25"))
    print("Expect:", datetime.date(2020, 2, 25))
    print("--------------------------------------------------------")

    # Test case 2
    print("Test case 2")
    final_input = input("Please input a value: ")
    try:
        result = format.validate(final_input)
    except:
        print("Result:", "Invalid Input")
    else:
        print("Result:", result)
    print("--------------------------------------------------------")


# Generated at 2022-06-14 14:29:26.485561
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t1 = "00:00"
    t2 = "00:00:00"
    t3 = "00:00:00.000000"
    t3 = "00:00:00.000111"
    t3 = "00:00:00.111000"
    t1 = "24:00"
    t2 = "24:00:00"
    t3 = "24:00:00.000000"

# Generated at 2022-06-14 14:29:29.254165
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    df = DateFormat()
    assert df.serialize(None) == None
    assert df.serialize(datetime.date(2020,8,1)) == "2020-08-01"
    

# Generated at 2022-06-14 14:29:35.354175
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date_format = DateFormat()
    date = date_format.validate('2020-10-22')
    assert date_format.serialize(date) == '2020-10-22'
    assert date_format.serialize(None) is None



# Generated at 2022-06-14 14:29:38.849587
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    '''Serialize a valid datetime format'''
    date_input = datetime.date(2020, 4, 20)
    assert DateFormat().serialize(date_input) == '2020-04-20'



# Generated at 2022-06-14 14:29:41.434663
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    with pytest.raises(AssertionError):
        format = DateFormat()
        obj = datetime.time(12, 2, 3)
        format.serialize(obj)


# Generated at 2022-06-14 14:29:43.329621
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    assert DateFormat().serialize(datetime.date(2020,1,1)) == "2020-01-01"


test_DateFormat_serialize()

# Generated at 2022-06-14 14:29:59.548002
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    dateformat = DateFormat()
    date_str = dateformat.validate("2020-08-19")
    assert date_str == datetime.date(2020, 8, 19)


# Generated at 2022-06-14 14:30:08.351315
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    fmt = DateFormat()
    fmt.validate('2020-03-13')
    fmt.validate('2020-03-14')
    try:
        fmt.validate('202002-03-13')
        assert False
    except ValidationError as e:
        assert e.code == 'format'

    try:
        fmt.validate('2020-02-30')
        assert False
    except ValidationError as e:
        assert e.code == 'invalid'


# Generated at 2022-06-14 14:30:19.387260
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    # Test for invalid format
    timeFormat = TimeFormat()
    with pytest.raises(ValidationError) as ve:
        timeFormat.validate("1:2")
        assert ve.value.code == "format"
    # Test for real time
    assert timeFormat.validate("01:02") == datetime.time(1,2)
    # Test for invalid time
    with pytest.raises(ValidationError) as ve:
        timeFormat.validate("25:00")
        assert ve.value.code == "invalid"
    # Test for real time
    assert timeFormat.validate("13:02:30") == datetime.time(13,2,30)
    # Test for invalid time

# Generated at 2022-06-14 14:30:20.047983
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    pass

# Generated at 2022-06-14 14:30:25.922900
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    a = TimeFormat().validate('12:30:59.123414')
    print(a)
    assert a is not None
    a = TimeFormat().validate('12:30:59')
    print(a)
    assert a is not None
    a = TimeFormat().validate('12:30')
    print(a)
    assert a is not None

# Generated at 2022-06-14 14:30:28.700373
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    format = DateTimeFormat()
    assert format.validate("2019-01-01T00:00:00+00:00") == datetime.datetime(2019, 1, 1)

# Generated at 2022-06-14 14:30:40.012346
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    format = TimeFormat()
    assert format.validate('14:30:59') == datetime.time(14, 30, 59)
    assert format.validate('0:30:59') == datetime.time(0, 30, 59)
    assert format.validate('0:0:59') == datetime.time(0, 0, 59)
    assert format.validate('0:0:0') == datetime.time(0, 0, 0)
    assert format.validate('0:0:0.00000') == datetime.time(0, 0, 0, 0)
    assert format.validate('0:0:0.01') == datetime.time(0, 0, 0, 10000)

# Generated at 2022-06-14 14:30:46.399341
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    # Test successful case
    assert time_format.validate("11:59") == datetime.time(11,59)
    # Test case of failure
    with pytest.raises(ValidationError):
        time_format.validate("11:59-")
    # Test case of failure
    with pytest.raises(ValidationError):
        time_format.validate("11:60")

# Generated at 2022-06-14 14:30:48.622036
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    result = date.validate("2019-05-16")
    assert result == datetime.date(2019, 5, 16)



# Generated at 2022-06-14 14:30:51.251025
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    format = DateFormat()
    assert format.validate("2019-01-01") == datetime.date(2019, 1, 1)
    assert format.validate("2019-01-01") == datetime.date(2019, 1, 1)
    assert format.validate("2019-10-10") == datetime.date(2019, 10, 10)



# Generated at 2022-06-14 14:31:06.339011
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate('2014-02-13') == datetime.date(2014, 2, 13)


# Generated at 2022-06-14 14:31:11.264815
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    assert tf.validate("20:10:10") == datetime.time(20, 10, 10)
    assert tf.validate("20:10:10.123456") == datetime.time(20, 10, 10, 123456)
    assert tf.validate("20:10") == datetime.time(20, 10)

# Generated at 2022-06-14 14:31:13.918531
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    value = "2000-01-31"
    expected_result = datetime.date(2000, 1, 31)
    assert expected_result == DateFormat().validate(value)


# Generated at 2022-06-14 14:31:16.161587
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    c = TimeFormat()
    # c.validate('23:59:59.999999')
    c.validate('23:59:59')


# Generated at 2022-06-14 14:31:27.220585
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    timeformat = TimeFormat()
    # test normal format
    time = timeformat.validate('15:59:59.000001')
    assert time.hour == 15
    assert time.minute == 59
    assert time.second == 59
    assert time.microsecond == 1

    # test without microsecond
    time = timeformat.validate('15:59:59')
    assert time.hour == 15
    assert time.minute == 59
    assert time.second == 59
    assert time.microsecond == 0
    
    # test without second
    time = timeformat.validate('15:59')
    assert time.hour == 15
    assert time.minute == 59
    assert time.second == 0
    assert time.microsecond == 0
    
    # test without minute

# Generated at 2022-06-14 14:31:30.627556
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date = date_format.validate("2020-05-09")
    assert date.year == 2020
    assert date.month == 5
    assert date.day == 9


# Generated at 2022-06-14 14:31:40.884226
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat()
    date.validate('2020-05-22')
    date.validate('9999-12-31')
    bad_date1 = '200-05-22'
    bad_date2 = '2020-5-22'
    bad_date3 = '2020-05-222'
    bad_date4 = '2020-13-22'
    bad_date5 = '2020-12-32'
    with pytest.raises(ValidationError):
        date.validate(bad_date1)
    with pytest.raises(ValidationError):
        date.validate(bad_date2)
    with pytest.raises(ValidationError):
        date.validate(bad_date3)

# Generated at 2022-06-14 14:31:44.072241
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    a = TimeFormat()

# Generated at 2022-06-14 14:31:50.783457
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time1 = TimeFormat()
    time1.validate("12:00:00")
    time1.validate("12:00:00.000000")
    time1.validate("12:00:00.123456")
    time1.validate("12:00")
    time1.validate("00:00:00.000000")
    time1.validate("00:00:00")


# Generated at 2022-06-14 14:31:53.151343
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    """
    Test method validate of DateFormat class.
    """
    date = "2020-07-14"
    date_format = DateFormat()
    new_date = date_format.validate(date)
    assert new_date == datetime.date(2020, 7, 14)

# Generated at 2022-06-14 14:32:26.092185
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dateTimeFormat = DateTimeFormat()
    dateTimeFormat.validate("2020-08-03T03:28:41Z") # datetime.datetime(2020, 8, 3, 3, 28, 41, tzinfo=datetime.timezone.utc)
    dateTimeFormat.validate("2020-08-03T03:28:41.1235+00:00") # datetime.datetime(2020, 8, 3, 3, 28, 41, 123000, tzinfo=datetime.timezone.utc)
    dateTimeFormat.validate("2020-08-03T03:28:41.01+09:00") # datetime.datetime(2020, 8, 3, 3, 28, 41, 10000, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))


#

# Generated at 2022-06-14 14:32:31.101138
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    value = '2020-01-01T00:00:00+00:00'
    result = DateTimeFormat().validate(value)
    assert result == datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z')


# Generated at 2022-06-14 14:32:39.704530
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    time_format = TimeFormat()
    assert time_format.validate("12:34:56") == datetime.time(12, 34, 56)
    assert time_format.validate("12:34") == datetime.time(12, 34)
    assert time_format.validate("12:34:56.123") == datetime.time(12, 34, 56, 123000)
    assert time_format.validate("12:34:56.123456") == datetime.time(12, 34, 56, 123456)
    assert time_format.validate("00:59:00") == datetime.time(0, 59)
    assert time_format.validate("23:59:59:123456") == datetime.time(23, 59, 59, 123456)

# Generated at 2022-06-14 14:32:46.551881
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    d1 = datetime.date(2019, 2, 28)
    d2 = datetime.date(1991, 2, 28)
    test_cases = {
        "2019-02-28": d1,
        "1991-02-28": d2,
    }

    for value, expected_result in test_cases.items():
        fmt = DateFormat()
        assert fmt.validate(value) == expected_result


# Generated at 2022-06-14 14:32:49.487474
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    test_value = "10:01:14.01"
    a = TimeFormat()
    assert a.validate(test_value) == datetime.time(10,1,14, 10000)


# Generated at 2022-06-14 14:32:57.194949
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.base import Format
    from datetime import time
    t1 = TimeFormat()
    t2 = TimeFormat(required=True)
    t3 = TimeFormat(description="Work time", error_messages={
                'format': "Must be a valid time format.",
                'invalid': "Must be a real time.",
            }, required=True)

    try:
        t1.validate("00:00:00:00")
    except ValidationError as e:
        assert e.code == 'format'
        assert e.text == 'Must be a valid time format.'
    else:
        assert False

    try:
        t1.validate("25:00:00:00")
    except ValidationError as e:
        assert e.code == 'invalid'

# Generated at 2022-06-14 14:33:00.156563
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date = DateFormat().validate('2020-09-01')
    assert date == datetime.date(2020, 9, 1)



# Generated at 2022-06-14 14:33:02.999277
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    for time in ['00:00:00', '13:45:00']:
        assert TimeFormat().validate(time) is not None


# Generated at 2022-06-14 14:33:04.884883
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    with pytest.raises(ValidationError):
        date_format.validate("20-02-20")



# Generated at 2022-06-14 14:33:08.031014
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    # Test regular case
    dateFormat = DateFormat()
    assert dateFormat.validate("2020-09-12") == datetime.date(2020, 9, 12)

