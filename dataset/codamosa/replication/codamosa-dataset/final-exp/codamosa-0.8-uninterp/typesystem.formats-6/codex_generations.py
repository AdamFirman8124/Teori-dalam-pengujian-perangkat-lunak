

# Generated at 2022-06-14 14:23:42.917493
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.base import ValidationError
    
    pattern = "Must be a real time."
    
    try:
        TimeFormat().validate('02:75')
    except ValidationError as e:
        assert e.text == pattern
    
    

# Generated at 2022-06-14 14:23:54.669154
# Unit test for method serialize of class TimeFormat
def test_TimeFormat_serialize():
	# assert TimeFormat().serialize(None) == None
	assert TimeFormat().is_native_type(datetime.datetime(2018, 6, 16, 11, 58, 50)) == True
	assert TimeFormat().is_native_type(datetime.datetime(2018, 6, 16, 11, 58, 50, 1)) == True
	assert TimeFormat().is_native_type(2018) == False
	assert TimeFormat().serialize(datetime.datetime(2018, 6, 16, 11, 58, 50)) == "11:58:50"
	assert TimeFormat().serialize(datetime.datetime(2018, 6, 16, 11, 58, 50, 1)) == "11:58:50.000001"
	assert TimeFormat().validate("11:58:50") == datetime.time(11, 58, 50)
	

# Generated at 2022-06-14 14:24:03.566273
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(1910, 8, 3, )) == '1910-08-03T00:00:00'
    assert DateTimeFormat().serialize(datetime.datetime(2019, 6, 24, 8, 45, 0, 0 )) == '2019-06-24T08:45:00'
    assert DateTimeFormat().serialize(datetime.datetime(1989, 12, 27, 6, 56, 57, 123456, tzinfo=datetime.timezone.utc )) == '1989-12-27T06:56:57.123456Z'
    assert DateTimeFormat().serialize(datetime.datetime(2001, 4, 2, 4, 2, 3, 4, tzinfo=datetime.timezone(datetime.timedelta(hours=-8, minutes=0))))

# Generated at 2022-06-14 14:24:08.754468
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    dtf = DateTimeFormat()
    ret = dtf.validate("2018-07-14T15:23:01+08:00")
    #print(type(ret))
    assert ret == "2018-07-14T15:23:01+08:00"

test_DateTimeFormat_validate()


# Generated at 2022-06-14 14:24:17.417781
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    f = TimeFormat()
    t1 = f.validate("01:02:03")
    assert(t1.hour == 1)
    assert(t1.minute == 2)
    assert(t1.second == 3)
    assert(t1.strftime("%H:%M:%S") == "01:02:03")

    t2 = f.validate("01:02")
    assert(t2.hour == 1)
    assert(t2.minute == 2)
    assert(t2.strftime("%H:%M:%S") == "01:02:00")

    t3 = f.validate("01:02:03.456")
    assert(t3.hour == 1)
    assert(t3.minute == 2)
    assert(t3.second == 3)

# Generated at 2022-06-14 14:24:24.174452
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    formatter = DateFormat()

    invalid_date = "2018-02-30"
    try:
        formatter.validate(invalid_date)
    except ValidationError as e:
        assert e.code == "invalid"

    invalid_format = "13:13:13:13"
    try:
        formatter.validate(invalid_format)
    except ValidationError as e:
        assert e.code == "format"



# Generated at 2022-06-14 14:24:26.638662
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    formatter = DateTimeFormat()
    date = formatter.validate("2019-11-28T10:15:45Z")
    assert date



# Generated at 2022-06-14 14:24:29.807019
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    assert DateFormat().validate("1996-09-15") == datetime.date(year=1996, month=9, day=15)
    assert DateFormat().validate("1996-09-15") == '1996-09-15'

# Generated at 2022-06-14 14:24:39.459258
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    from typesystem.date import TimeFormat
    from datetime import timedelta
    tf = TimeFormat()
    # examples from https://www.ietf.org/rfc/rfc3339.txt :
    assert tf.validate('00:30:15') == timedelta(hours=0, minutes=30, seconds=15)
    assert tf.validate('23:59:60') == timedelta(hours=23, minutes=59, seconds=60)
    assert tf.validate('23:59:59.1') == timedelta(hours=23, minutes=59, seconds=59, microseconds=100000)
    assert tf.validate('23:59:59.123456') == timedelta(hours=23, minutes=59, seconds=59, microseconds=123456)

# Generated at 2022-06-14 14:24:47.686449
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():

    tf = TimeFormat()
    assert str(tf.validate("12:34:56+02")) == "12:34:56+02:00"
    assert str(tf.validate("12:34:56+02:00")) == "12:34:56+02:00"
    assert str(tf.validate("12:34:56+0200")) == "12:34:56+02:00"
    assert str(tf.validate("12:34:56")) == "12:34:56"
    assert str(tf.validate("12:34")) == "12:34:00"



# Generated at 2022-06-14 14:25:03.496016
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 12, 15)) == "2020-01-01T12:15:00"
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 12, 15, tzinfo=datetime.timezone.utc)) == "2020-01-01T12:15:00Z"
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 12, 15, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))) == "2020-01-01T12:15:00+02:00"

# Generated at 2022-06-14 14:25:05.584581
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()
    date_format.validate("2020-01-01")



# Generated at 2022-06-14 14:25:13.468794
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    a = DateTimeFormat()
    b = DateTimeFormat()
    obj1 = datetime.datetime(2016, 10, 4, 14, 54, 14, 28, tzinfo=datetime.timezone.utc)
    obj2 = datetime.datetime(2016, 10, 4, 14, 54, 14, 28)
    assert a.serialize(obj1) == "2016-10-04T14:54:14.000028Z"
    assert b.serialize(obj2) == "2016-10-04T14:54:14.000028"

# Generated at 2022-06-14 14:25:20.644368
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime(2019, 12, 31, 22, 30, tzinfo=datetime.timezone.utc)
    res = DateTimeFormat().serialize(dt)
    assert res == "2019-12-31T22:30:00Z"
    dt = datetime.datetime(2019, 12, 31, 22, 30)
    res = DateTimeFormat().serialize(dt)
    assert res == "2019-12-31T22:30:00"

# Generated at 2022-06-14 14:25:26.375290
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    """
    Test that serialize method in DateTimeFormat class
    """
    obj = datetime.datetime.now()
    obj2 = datetime.datetime(2019, 12, 1, 12, 0, 0)
    assert isinstance(DateTimeFormat().serialize(obj), str)
    assert DateTimeFormat().serialize(obj2) == "2019-12-01T12:00:00"

# Generated at 2022-06-14 14:25:28.305537
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date = datetime.date(2018, 4, 26)
    assert DateFormat().serialize(date) == "2018-04-26"


# Generated at 2022-06-14 14:25:32.400280
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    #GIVEN
    date = "2018-04-01"
    #WHEN
    date = DateTimeFormat().validate(date)
    #THEN
    assert date == datetime.datetime(2018,4,1)
    return date


# Generated at 2022-06-14 14:25:40.237778
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # check that year, month, day are a valid datetime
    datetime_format = DateTimeFormat()
    try:
        time = datetime_format.validate('2010-01-01T00:00:00Z')
    except ValidationError as e:
        assert e.code == 'invalid'
    else:
        assert time.isoformat() == '2010-01-01T00:00:00+00:00'

    # check that year, month, day are a valid datetime with minutes and hours offset
    datetime_format = DateTimeFormat()
    try:
        time = datetime_format.validate('2010-01-01T08:30+03:30')
    except ValidationError as e:
        assert e.code == 'invalid'

# Generated at 2022-06-14 14:25:44.043355
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2019, 11, 28, 13, 56, 10, 303501)) == "2019-11-28T13:56:10.303501"

# Generated at 2022-06-14 14:25:56.098812
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    datetimef = DateTimeFormat()
    dt_UTC = datetime.datetime(1,2,3,4,5,6,7,datetime.timezone.utc)
    assert datetimef.serialize(dt_UTC) == "0001-02-03T04:05:06.000007+00:00"
    dt = datetime.datetime(1,2,3,4,5,6,7)
    assert datetimef.serialize(dt) == "0001-02-03T04:05:06.000007"
    dt = datetime.datetime(1,2,3,4,5,6,7,datetime.timezone(datetime.timedelta(hours=5,minutes=30)))

# Generated at 2022-06-14 14:26:04.667288
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # testing standard serialize
    testDate = '2020-05-10T19:18:00Z'
    assert DateTimeFormat().serialize(datetime.datetime.fromisoformat(testDate)) == testDate, f"Returned value {DateTimeFormat().serialize(datetime.datetime.fromisoformat(testDate))} was not equal to {testDate}."
    # testing no serialize
    testDate = None 
    assert DateTimeFormat().serialize(testDate) == testDate, f"Returned value {DateTimeFormat().serialize(testDate)} was not equal to {testDate}."


# Generated at 2022-06-14 14:26:16.476449
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # test_DateTimeFormat_validate_1
    date_time_format = DateTimeFormat()
    # value: "2018-12-15T16:34:05"
    date_time = date_time_format.validate("2018-12-15T16:34:05")
    assert date_time.year == 2018
    assert date_time.month == 12
    assert date_time.day == 15
    assert date_time.hour == 16
    assert date_time.minute == 34
    assert date_time.second == 5
    assert date_time.microsecond == 0
    assert date_time.tzinfo is None
    # value: "2018-12-15T16:34:05.1234"

# Generated at 2022-06-14 14:26:19.832280
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    date_format = DateFormat()
    date = datetime.date(2019, 1, 12)
    assert date_format.serialize(date) == "2019-01-12"


# Generated at 2022-06-14 14:26:22.826893
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    date_format = DateFormat()

    date_format.validate("2002-12-25")


# Generated at 2022-06-14 14:26:30.977273
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from typesystem.base import (instanceof, Integer, String)
    from typesystem.fields import DateTime, UUID

    class BlogPost(typesystem.Schema):
        id = UUID()
        title = String()
        created_at = DateTime()
        updated_at = DateTime()
        num_comments = Integer()

    post = BlogPost().load(
        {"id": "bd2c9b13-e2ab-47e2-b53e-03b0b27f0c75",
         "title": "First Blog Post",
         "created_at": "2018-05-17T16:30:20.861643+00:00",
         "num_comments": 0}
    )

# Generated at 2022-06-14 14:26:33.496911
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from datetime import datetime, timezone
    obj = datetime(2020, 3, 6, 12, 33, 58, tzinfo=timezone(datetime.timedelta(hours=5, minutes=30)))
    serialize_value = DateTimeFormat().serialize(obj)
    assert serialize_value == "2020-03-06T12:33:58+05:30"

# Generated at 2022-06-14 14:26:36.019773
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    uuid_string = "a6d47792-2cf1-4cd8-a99a-126c9e64cde8"

    uuid_format = UUIDFormat()

    assert uuid_format.validate(uuid_string) == uuid.UUID(uuid_string)

# Generated at 2022-06-14 14:26:42.681352
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    test_uuid = 'df7dc2bc-07a8-48a1-b448-fbc9f1b8d7b3'
    assert UUIDFormat().validate(test_uuid) == uuid.UUID(test_uuid)
    assert UUIDFormat().validate(test_uuid) == uuid.UUID(test_uuid)


# Generated at 2022-06-14 14:26:45.099663
# Unit test for method validate of class UUIDFormat
def test_UUIDFormat_validate():
    assert UUIDFormat().validate("37b5ebff-3f0b-41b7-b5e9-22d8b66f30fb")


# Generated at 2022-06-14 14:26:47.809332
# Unit test for method serialize of class DateFormat
def test_DateFormat_serialize():
    # given
    df = DateFormat()
    value = datetime.date(2015, 11, 9)

    # when
    actual = df.serialize(value)

    # then
    assert actual == "2015-11-09"


# Generated at 2022-06-14 14:27:00.582818
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2020, 12, 12, 12, 12, 12, tzinfo=datetime.timezone.utc)) == '2020-12-12T12:12:12+00:00'
    assert DateTimeFormat().serialize(datetime.datetime(2020, 12, 12, 12, 12, 12, tzinfo=datetime.timezone(datetime.timedelta(hours=2)))) == '2020-12-12T12:12:12+02:00'
    assert DateTimeFormat().serialize(datetime.datetime(2020, 12, 12, 12, 12, 12, tzinfo=datetime.timezone(datetime.timedelta(hours=2, minutes=15)))) == '2020-12-12T12:12:12+02:15'

#

# Generated at 2022-06-14 14:27:03.643201
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj_type = DateTimeFormat()
    datetime_val = datetime.datetime(2015, 1, 1, 12, 10, 10, tzinfo=datetime.timezone.utc)
    assert obj_type.serialize(datetime_val) == "2015-01-01T12:10:10Z"
    return True

# Generated at 2022-06-14 14:27:08.216285
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime(2018, 7, 18, 16, 44, 31, tzinfo=None)
    serialized_obj = DateTimeFormat().serialize(obj)
    assert serialized_obj == "2018-07-18T16:44:31"

# Generated at 2022-06-14 14:27:11.136079
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    time = datetime.datetime.now().time()
    time_string = time.isoformat()
    assert time == tf.validate(time_string)

# Generated at 2022-06-14 14:27:15.250191
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # Arrange
    sut = DateTimeFormat()
    obj = datetime.datetime(2019, 12, 31, 23, 59, 59)
    expected = "2019-12-31T23:59:59"

    # Act
    actual = sut.serialize(obj)

    # Assert
    assert expected == actual

# Generated at 2022-06-14 14:27:23.354548
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date4 = datetime.datetime(2019, 7, 8, 16, 8, 7, tzinfo=datetime.timezone.utc)
    date3 = datetime.datetime(2019, 7, 8, 16, 8, tzinfo=datetime.timezone.utc)
    date2 = datetime.datetime(2019, 7, 8, 16, tzinfo=datetime.timezone.utc)
    date1 = datetime.datetime(2019, 7, 8, tzinfo=datetime.timezone.utc)
    date = datetime.datetime(2019, 7, 8)


# Generated at 2022-06-14 14:27:28.624347
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_time_format = DateTimeFormat()
    obj = datetime.datetime(2020, 2, 1, 15, 20, 45, tzinfo=datetime.timezone.utc)

    assert date_time_format.serialize(obj) == "2020-02-01T15:20:45Z"

# Generated at 2022-06-14 14:27:37.446337
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():

    dt1 = datetime.datetime(2010, 1, 1)
    dt2 = datetime.datetime(2010, 1, 1, tzinfo=datetime.timezone.utc)
    dt3 = datetime.datetime(2010, 1, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=3)))

    assert "2010-01-01T00:00:00" == DateTimeFormat().serialize(dt1)
    assert "2010-01-01T00:00:00Z" == DateTimeFormat().serialize(dt2)
    assert "2010-01-01T00:00:00+03:00" == DateTimeFormat().serialize(dt3)

# Generated at 2022-06-14 14:27:44.798185
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    assert DateTimeFormat().validate("2020-01-01T01:01") == datetime.datetime(2020, 1, 1, 1, 1)
    assert DateTimeFormat().validate("2020-01-01T01:01Z") == datetime.datetime(2020, 1, 1, 1, 1, tzinfo=datetime.timezone.utc)
    assert DateTimeFormat().validate("2020-01-01T01:01+01:00") == datetime.datetime(2020, 1, 1, 1, 1, tzinfo=datetime.timezone(datetime.timedelta(hours=1)))

# Generated at 2022-06-14 14:27:57.305987
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    fmt = DateTimeFormat()
    assert fmt.validate("2020-05-17T11:25:36.2Z") == datetime.datetime(2020, 5, 17, 11, 25, 36, 200000, datetime.timezone.utc)
    assert fmt.validate("2020-05-17T11:25:36.200Z") == datetime.datetime(2020, 5, 17, 11, 25, 36, 200000, datetime.timezone.utc)
    assert fmt.validate("2020-05-17T11:25:00.123Z") == datetime.datetime(2020, 5, 17, 11, 25, 0, 123000, datetime.timezone.utc)
    assert fmt.validate("2020-05-17T11:25:00.1230Z") == datetime.datetime

# Generated at 2022-06-14 14:28:07.505103
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    value = "23:59"
    time_parser = TimeFormat()
    assert time_parser.validate(value) == datetime.time(hour=23, minute=59)

    value = "23:59:59"
    time_parser = TimeFormat()
    assert time_parser.validate(value) == datetime.time(hour=23, minute=59, second=59)

    value = "23:59:59.123456"
    time_parser = TimeFormat()
    assert time_parser.validate(value) == datetime.time(hour=23, minute=59, second=59, microsecond=123456)

    value = "23:59:59."
    time_parser = TimeFormat()

# Generated at 2022-06-14 14:28:11.214324
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime(2020,9,1,21,30,10)
    assert DateTimeFormat().serialize(None) == None
    assert DateTimeFormat().serialize(dt) == "2020-09-01T21:30:10"


# Generated at 2022-06-14 14:28:13.933274
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    """
        Test for verifying serialize method in class DateTimeFormat
    """
    dt = None
    output = DateTimeFormat().serialize(dt)
    assert output == None


# Generated at 2022-06-14 14:28:19.960261
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    base_format = DateTimeFormat()
    assert base_format.serialize(datetime.datetime.fromtimestamp(
        timestamp=1595774040, tz=datetime.timezone.utc)) == "2020-07-27T19:07:20Z"
    assert base_format.serialize(datetime.datetime.fromtimestamp(
        timestamp=1595774040, tz=datetime.timezone(datetime.timedelta(hours=-4)))) == "2020-07-27T19:07:20-04:00"

# Generated at 2022-06-14 14:28:23.419020
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2020,7,1,13,55,0,0,datetime.timezone.utc))=="2020-07-01T13:55:00Z"

# Generated at 2022-06-14 14:28:27.912805
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    obj = datetime.datetime.strptime("2019-02-05T09:23Z", "%Y-%m-%dT%H:%MZ")
    output = DateTimeFormat().serialize(obj)
    assert output == "2019-02-05T09:23Z"


# Generated at 2022-06-14 14:28:32.858377
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    format = DateTimeFormat()
    assert('2019-01-01T01:01:01Z' == format.serialize(datetime.datetime(2019, 1, 1, 1, 1, 1, tzinfo=datetime.timezone.utc)))

# Generated at 2022-06-14 14:28:41.391477
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    #positive test cases
    dtf = DateTimeFormat()
    assert dtf.validate("2000-01-01T00:00:00Z") == datetime.datetime(2000, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
    assert dtf.validate("2000-01-01T00:00:00+10:00") == datetime.datetime(2000, 1, 1, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=10)))
    assert dtf.validate("2000-01-01T00:00:00-10:00") == datetime.datetime(2000, 1, 1, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-10)))


# Generated at 2022-06-14 14:28:47.428607
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    t = DateFormat()
    assert t.validate('2019-12-31') == datetime.date(2019,12,31)
    try: 
        t.validate('2019-13-31')
        assert False
    except ValidationError as e:
        assert e.code == 'invalid' and e.text == 'Must be a real date.'


# Generated at 2022-06-14 14:28:51.902814
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    pass
    #date_time_format = DateTimeFormat()
    #assert date_time_format.validate("2019-01-01 12:00:00") == datetime.datetime(2019, 1, 1, 12, 0, 0)


# Generated at 2022-06-14 14:29:03.688954
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    value = DateTimeFormat().serialize(datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0, tzinfo=datetime.timezone.utc))
    assert value == "2020-01-01T00:00:00Z"

    value = DateTimeFormat().serialize(datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0, tzinfo=datetime.timezone(datetime.timedelta(hours=8))))
    assert value == "2020-01-01T00:00:00+08:00"

# Generated at 2022-06-14 14:29:06.578943
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt = datetime.datetime(2015, 1, 1)
    assert DateTimeFormat().serialize(dt) == '2015-01-01T00:00:00'

# Generated at 2022-06-14 14:29:12.295108
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    t1 = TimeFormat()
    res = t1.validate('00:01:02')
    res1 = t1.validate('00:01:02.55')
    res2 = t1.validate('00:01:02.5304')
    res3 = t1.validate('00:01:02.556678')
    res4 = t1.validate('00:01:02.556678554')


# Generated at 2022-06-14 14:29:16.611640
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from typesystem.format import DateTimeFormat

    dt = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
    test_dt = dt.isoformat().replace('Z', '')
    assert DateTimeFormat().serialize(dt) == test_dt

# Generated at 2022-06-14 14:29:21.417774
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    data = "2014-10-30T09:12:00.000000Z"
    date = DateTimeFormat().validate(data)
    expected = datetime.datetime(2014, 10, 30, 9, 12, 0, tzinfo=datetime.timezone.utc)
    assert date == expected

# Unit test data for testing class DateTimeFormat

# Generated at 2022-06-14 14:29:22.077184
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    return

# Generated at 2022-06-14 14:29:26.348254
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dt_format = DateTimeFormat()
    date = datetime.datetime(2020, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    assert dt_format.serialize(date) == "2020-01-01T12:00:00Z"

# Generated at 2022-06-14 14:29:28.653346
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    data = '2019-03-25'
    df = DateFormat()
    assert df.is_native_type(df.validate(data)) is True


# Generated at 2022-06-14 14:29:33.615254
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    print(DateTimeFormat().validate("2019-04-01T09:00:00"))
    print(DateTimeFormat().validate("2019-04-01T09:00:00.000"))
    print(DateTimeFormat().validate("2019-04-01T09:00:00.000000"))
    print(DateTimeFormat().validate("2019-04-01T09:00:00.123456"))
    print(DateTimeFormat().validate("2019-04-01T09:00:00Z"))
    print(DateTimeFormat().validate("2019-04-01T09:00:00+00:00"))
    print(DateTimeFormat().validate("2019-04-01T09:00:00+01:00"))

# Generated at 2022-06-14 14:29:42.268661
# Unit test for method serialize of class DateTimeFormat

# Generated at 2022-06-14 14:29:49.416430
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # Test DateTimeFormat with Z
    assert DateTimeFormat().serialize(datetime.datetime(2017, 12, 12, 12, 12, 12, 121212, datetime.timezone.utc)) == '2017-12-12T12:12:12.121212Z'
    # Test DateTimeFormat without Z
    assert DateTimeFormat().serialize(datetime.datetime(2017, 12, 12, 12, 12, 12, 121212)) == '2017-12-12T12:12:12.121212'

# Generated at 2022-06-14 14:29:54.613332
# Unit test for method validate of class DateTimeFormat
def test_DateTimeFormat_validate():
    # test datetime with Z in the end
    assert DateTimeFormat().validate('2019-10-24T15:06:11Z') == datetime.datetime(year=2019, month=10, day=24, hour=15, minute=6, second=11, tzinfo=datetime.timezone.utc)
    
    # test datetime with +00:00 in the end
    assert DateTimeFormat().validate('2019-10-24T15:06:11+00:00') == datetime.datetime(year=2019, month=10, day=24, hour=15, minute=6, second=11, tzinfo=datetime.timezone.utc)
    
    # test datetime with +01:00 in the end

# Generated at 2022-06-14 14:29:58.405799
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    tz = pytz.timezone('America/Montreal')
    dt = datetime.datetime.now(tz)
    df = DateTimeFormat()
    assert df.serialize(dt) == dt.isoformat().replace('+00:00', 'Z')

# Generated at 2022-06-14 14:30:11.838568
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 12, 0, 0, 0)) == '2020-01-01T12:00:00'
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 12, 0, 0, 123456)) == '2020-01-01T12:00:00.123456'
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 12, 0, 0, 723456)) == '2020-01-01T12:00:00.723456'
    assert DateTimeFormat().serialize(datetime.datetime(2020, 1, 1, 12, 0, 0, 723456, datetime.timezone.utc)) == '2020-01-01T12:00:00Z'
   

# Generated at 2022-06-14 14:30:15.030388
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2000, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)) == '2000-01-01T00:00:00Z'

# Generated at 2022-06-14 14:30:23.561510
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2018, 8, 7, 15, 11, 3)) == '2018-08-07T15:11:03'
    assert DateTimeFormat().serialize(datetime.datetime(2018, 8, 7, 15, 11, 3, 0)) == '2018-08-07T15:11:03'
    assert DateTimeFormat().serialize(datetime.datetime(2018, 8, 7, 15, 11, 3, 1)) == '2018-08-07T15:11:03.000001'

# Generated at 2022-06-14 14:30:33.192143
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2000,1,1,1,1)) == "2000-01-01T01:01:00"
    assert DateTimeFormat().serialize(datetime.datetime(2000,1,1,1,1,0,10)) == "2000-01-01T01:01:00.000010"
    assert DateTimeFormat().serialize(datetime.datetime(2000,1,1,1,1,0,1000010)) == "2000-01-01T01:01:00.100001"
    assert DateTimeFormat().serialize(datetime.datetime(2000,1,1,1,1,0,1000000)) == "2000-01-01T01:01:00.100000"

# Generated at 2022-06-14 14:30:39.086587
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # Given
    value = '2016-12-15T21:17:09.0Z'
    obj = '2016-12-15T21:17:09.0Z'
    assert_result = obj
    # When
    datetime_format = DateTimeFormat()
    result = datetime_format.serialize(value)
    # Then
    assert result == assert_result

# Generated at 2022-06-14 14:30:43.000426
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    format = DateTimeFormat()
    date_time_obj = datetime.datetime(2018, 7, 27, 14, 15, 16, 17000)
    assert format.serialize(date_time_obj) == '2018-07-27T14:15:16.0170Z'


# Generated at 2022-06-14 14:30:45.531316
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2019, 6, 11, 12, 31, 0, 0)) == "2019-06-11T12:31:00Z"

# Generated at 2022-06-14 14:31:02.781176
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    from typesystem.base import BaseType

    class TestType(BaseType):
        # One format can be optional
        format = "date-time"

    date = datetime.datetime(2019, 1, 1, 1, 1, 1)
    assert TestType.serialize(date) == "2019-01-01T01:01:01Z"

    date = datetime.datetime(2019, 1, 1, 1, 1, 1, tzinfo=datetime.timezone.utc)
    assert TestType.serialize(date) == "2019-01-01T01:01:01Z"



# Generated at 2022-06-14 14:31:05.711233
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime.now(tz=datetime.timezone.utc)) == '2020-04-01T13:15:23.372817+00:00'

# Generated at 2022-06-14 14:31:08.514720
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2019, 12, 31, 14, 58, 20)) == '2019-12-31T14:58:20'

# Generated at 2022-06-14 14:31:15.207328
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    test_obj_1 = datetime.datetime(2019, 10, 11, 4, 25, 26, tzinfo=datetime.timezone.utc)
    test_obj_2 = datetime.datetime(2019, 10, 11, 4, 25, 26)
    assert DateTimeFormat().serialize(obj = test_obj_1) == "2019-10-11T04:25:26Z"
    assert DateTimeFormat().serialize(obj = test_obj_2) == "2019-10-11T04:25:26"


# Generated at 2022-06-14 14:31:21.555126
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    fmt = DateTimeFormat()
    try:
        fmt.serialize(None)
    except: 
        assert False
    try:
        fmt.serialize(1)
    except:
        assert not False
    # Had to remove try block because assert will not work with it for some reason
    # There is no error anyways



# Generated at 2022-06-14 14:31:23.536976
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    value = datetime.datetime(2019, 6, 22, 13, 2, 30)
    assert DateTimeFormat().serialize(value) == "2019-06-22T13:02:30"



# Generated at 2022-06-14 14:31:31.751026
# Unit test for method validate of class DateFormat
def test_DateFormat_validate():
    #test case 1
    data1 = datetime.date(2020,6,13)
    d1 = DateFormat()
    assert d1.validate(data1.isoformat()) == data1
    #test case 2
    data2 = datetime.date(2020,6,13)
    d2 = DateFormat()
    assert d2.validate(data2.isoformat()) == data2
    #test case 3
    data3 = datetime.date(2020,6,13)
    d3 = DateFormat()
    assert d3.validate(data3.isoformat()) == data3
    #test case 4
    data4 = datetime.date(2020,6,13)
    d4 = DateFormat()
    assert d4.validate(data4.isoformat()) == data4
    #test case 5
   

# Generated at 2022-06-14 14:31:36.022856
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date = datetime.datetime.utcnow()
    date = date.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=0)))
    datetimeformat = DateTimeFormat()
    assert datetimeformat.serialize(date) == date.isoformat()

# Generated at 2022-06-14 14:31:43.944736
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    def test(obj, result):
        t = DateTimeFormat().serialize(obj)
        assert t == result
    test(datetime.datetime(1990, 5, 1, 12, 0, 0), '1990-05-01T12:00:00')
    test(datetime.datetime(1990, 5, 1, 12, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=2))), '1990-05-01T12:00:00+02:00')
    test(datetime.datetime(1990, 5, 1, 12, 0, 0, tzinfo=datetime.timezone.utc), '1990-05-01T12:00:00Z')
    test(None, None)

# Generated at 2022-06-14 14:31:55.343463
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    # setup
    from typesystem.datetime import DateTimeFormat
    utc_datetime = datetime.datetime(2020, 8, 13, 13, 10, 41, 553000)
    local_datetime = datetime.datetime(2020, 8, 13, 13, 10, 41, 553000, tzinfo=datetime.timezone(datetime.timedelta(hours=2, minutes=0)))
    
    # given
    serialize_utc_datetime = DateTimeFormat().serialize(utc_datetime)
    serialize_local_datetime = DateTimeFormat().serialize(local_datetime)

    # when
    expected_utc_datetime = "2020-08-13T13:10:41.553000Z"

# Generated at 2022-06-14 14:32:26.286448
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    datetimeFormat = DateTimeFormat()
    assert datetimeFormat.serialize(datetime.datetime(2019, 1, 1, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)) == '2019-01-01T00:00:00+00:00'
    assert datetimeFormat.serialize(datetime.datetime(2019, 1, 1, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)) == '2019-01-01T00:00:00+00:00'

# Generated at 2022-06-14 14:32:30.089835
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dateTimeFormat = DateTimeFormat()
    assert dateTimeFormat.serialize(datetime.datetime(2000, 1, 1, 12, 0, 0, 0)) == '2000-01-01T12:00:00'

# Generated at 2022-06-14 14:32:31.493381
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
	assert DateTimeFormat().serialize(datetime.datetime.now())

# Generated at 2022-06-14 14:32:39.035714
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    import typesystem
    from typesystem import DateTime, Struct, String

    class Event(Struct):
        title = String()
        description = String(required=False)
        start_datetime = DateTime()

    event = Event(
        title="Test Event",
        description="This is a test event.",
        start_datetime="2019-06-04T16:00:00-06:00",
    )
    assert event.serialize() == {
        "title": "Test Event",
        "description": "This is a test event.",
        "start_datetime": "2019-06-04T22:00:00Z",  # UTC time
    }



# Generated at 2022-06-14 14:32:41.208962
# Unit test for method validate of class TimeFormat
def test_TimeFormat_validate():
    tf = TimeFormat()
    tf.validate(datetime.datetime.now().time().isoformat())

# Generated at 2022-06-14 14:32:44.800344
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert DateTimeFormat().serialize(datetime.datetime(2018, 5, 9, tzinfo=datetime.timezone.utc)) == '2018-05-09T00:00:00+00:00'

# Generated at 2022-06-14 14:32:54.326516
# Unit test for method validate of class DateTimeFormat

# Generated at 2022-06-14 14:32:59.024599
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    dtf = DateTimeFormat()
    test = datetime.datetime(2020,8,2,19,20,15,25)
    test = dtf.serialize(test)
    assert test == "2020-08-02T19:20:15.000025"

# Generated at 2022-06-14 14:33:11.557427
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    assert '2020-04-30T14:25+02:00' == DateTimeFormat().serialize(datetime.datetime(2020, 4, 30, 14, 25, tzinfo = datetime.timezone(datetime.timedelta(hours=2, minutes=0))))
    assert '2020-04-30T12:25Z' == DateTimeFormat().serialize(datetime.datetime(2020, 4, 30, 12, 25, tzinfo = datetime.timezone.utc))
    assert '2020-04-30T08:25' == DateTimeFormat().serialize(datetime.datetime(2020, 4, 30, 8, 25))

# Generated at 2022-06-14 14:33:16.748692
# Unit test for method serialize of class DateTimeFormat
def test_DateTimeFormat_serialize():
    date_obj = datetime.datetime(2020, 6, 1, tzinfo=datetime.timezone.utc)
    date_time = DateTimeFormat()
    assert date_time.serialize(date_obj) == '2020-06-01T00:00:00+00:00'
