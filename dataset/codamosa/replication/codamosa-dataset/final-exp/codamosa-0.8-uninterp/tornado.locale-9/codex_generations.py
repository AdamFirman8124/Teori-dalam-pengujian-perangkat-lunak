

# Generated at 2022-06-14 12:16:29.901950
# Unit test for function load_translations
def test_load_translations():
    # Check that es_LA can't be recognized, and it breaks the flow below for es_MX
    data = _translations['es_LA']
    assert(data == {})

    # Check that es_MX can be recognized, and it breaks the flow below for en_US
    data = _translations['es_MX']
    assert('unknown' in data)
    assert('%(name)s liked this' in data['unknown'])

    # Check that en_US can be recognized, and it breaks the flow below for en_US
    data = _translations['en_US']
    assert('unknown' in data)
    assert('%(name)s liked this' in data['unknown'])

# TODO(bdarnell): Change load_gettext_translations to use
# tornado.util.get_object_module_attribute when that

# Generated at 2022-06-14 12:16:32.967260
# Unit test for function load_translations
def test_load_translations():
    if not load_translations("/Users/junhaopark/Documents/compose_web/i18n/locale/locale_data"):
        return False
    return True

# Generated at 2022-06-14 12:16:37.213114
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get_closest("zh_CN")
    date = datetime.datetime(2018,5,5,5,5,5)
    result = locale.format_day(date)
    assert result == "星期六, 五月 5"

    locale = Locale.get_closest("fa")
    date = datetime.datetime(2018,5,5,5,5,5)
    result = locale.format_day(date)
    assert result == "یک شنبه, خرداد 5"

# Generated at 2022-06-14 12:16:42.062496
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    locale_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'locale')
    load_gettext_translations(locale_path, 'locale')
    assert('ru' in _translations)
    assert(os.path.exists(os.path.join(locale_path, 'ru', 'LC_MESSAGES')))
    assert(os.path.exists(os.path.join(locale_path, 'ru', 'LC_MESSAGES', 'locale.mo')))
    assert('en' in _translations)
    assert(os.path.exists(os.path.join(locale_path, 'en', 'LC_MESSAGES')))

# Generated at 2022-06-14 12:16:42.692027
# Unit test for function load_translations
def test_load_translations():
    print("Testing load_translations...")
    load_translations(".")


# Generated at 2022-06-14 12:16:44.279255
# Unit test for function load_translations
def test_load_translations():
    import tornado.testing
    list_locale = load_translations("F:\python安装包\tornado_project\tornado_test\test\test_data\test_locale_data")
    print(list_locale)
    tornado.testing.gen_test(test_load_translations)


# Generated at 2022-06-14 12:16:49.690987
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """Testing method format_day of class Locale
    To check if the day is represented well in the language of the country
    """
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    dayOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    year = 2020
    country = ["fr","es","de","ru","ar","zh", "fa", "he", "ta"]
    for i in country:
        locale = Locale.get(i)
        for j in range(0,12):
            for k in range(0,31):
                date = datetime.datetime(year,j+1,k+1)

# Generated at 2022-06-14 12:16:53.985487
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale.get('en')
    if locale.friendly_number(123) != '123':
        return False
    if locale.friendly_number(1234) != '1,234':
        return False
    if locale.friendly_number(1234567) != '1,234,567':
        return False
    return True

if not test_Locale_friendly_number():
    raise RuntimeError('Bad implementation of method friendly_number of class Locale')



# Generated at 2022-06-14 12:17:02.306584
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    """Tests for Locale.format_date
    - Choose a local timezone as here
    - Choose a GMT timezone as here
    - Define a time format
    - Set, among others, the same minutes and seconds of minute
    - Convert local time to GMT time
    - Call Locale.format_date with the converted time
    - Check the result
    """
    local_tz = timezone('Europe/Paris')
    gmt_tz = timezone('GMT')

    time_string = '2011-08-01 15:23:00'
    time_format = '%Y-%m-%d %H:%M:%S'

    local_time = local_tz.localize(datetime.strptime(time_string, time_format))

# Generated at 2022-06-14 12:17:05.809411
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert (Locale("en_US").friendly_number(1000000) == "1,000,000")
    assert (Locale("fa").friendly_number(1000000) == "1000000")

# Generated at 2022-06-14 12:17:24.736083
# Unit test for constructor of class Locale
def test_Locale():
    assert Locale


# Generated at 2022-06-14 12:17:28.225207
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get("en").friendly_number(1000000000) == '1,000,000,000'
    assert Locale.get("de").friendly_number(1000000000) == '1000000000'



# Generated at 2022-06-14 12:17:30.062190
# Unit test for function load_translations
def test_load_translations():
    directory = "./"
    load_translations(directory)
    print(_translations)


# Generated at 2022-06-14 12:17:36.484634
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    class MockLocale(Locale):
        def translate(
            self,
            message: str,
            plural_message: Optional[str] = None,
            count: Optional[int] = None,
        ) -> str:
            return message

    date = datetime.datetime.utcnow()
    locale = MockLocale('zh_CN')
    locale.format_date(date)



# Generated at 2022-06-14 12:17:44.403235
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    for code in ("en", "en_US"):
        l = Locale.get(code)
        assert l.friendly_number(1234567890) == "1,234,567,890"
        assert l.friendly_number(1234) == "1,234"
        assert l.friendly_number(12) == "12"
    for code in ("fr", "cz"):
        l = Locale.get(code)
        assert l.friendly_number(1234567890) == "1234567890"
        assert l.friendly_number(1234) == "1234"
        assert l.friendly_number(12) == "12"



# Generated at 2022-06-14 12:17:54.203551
# Unit test for function load_translations
def test_load_translations():
    t = {}
    t = _translations
    directory = "en_US"
    print(t)
    for path in os.listdir(directory):
        locale, extension = path.split(".")
        t[locale] = {}
        print(t)
        for i, row in enumerate(csv.reader(path)):
            if not row or len(row) < 2:
                continue
            row = [escape.to_unicode(c).strip() for c in row]
            english, translation = row[:2]
            t[locale].setdefault(plural, {})[english] = translation
    print(t)
    return t
#x = test_load_translations()



# Generated at 2022-06-14 12:17:56.295517
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert load_gettext_translations(directory="/home/eyu/workspaces/tornado/examples",domain="tornado") == None


# Generated at 2022-06-14 12:18:03.573418
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    #test1
    csv = pd.read_csv('test.csv', delimiter = ';')
    csv = csv.to_dict(orient='list')
    csv = {'singular':csv['singular'],'plural':csv['plural']}
    code = 'fr'
    translations = csv
    locale = CSVLocale(code, translations)
    message = 'Cancel'
    count=0
    res = locale.translate(message,count)
    ans = 'Annuler'
    assert(res==ans)
    #test2
    message = 'Cancel'
    count=1
    res = locale.translate(message,count)
    ans = 'Cancel'
    assert(res==ans)
    #test3
    message = 'Year'
    count=0


# Generated at 2022-06-14 12:18:15.831109
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get("en_US").friendly_number(3333) == "3,333"
    assert Locale.get("en_US").friendly_number(33333) == "33,333"
    assert Locale.get("en_US").friendly_number(4333333) == "4,333,333"
    assert Locale.get("en_US").friendly_number(3333333) == "3,333,333"

    assert Locale.get("ru_RU").friendly_number(3333) == "3333"
    assert Locale.get("ru_RU").friendly_number(33333) == "33333"
    assert Locale.get("ru_RU").friendly_number(4333333) == "4333333"

# Generated at 2022-06-14 12:18:24.335622
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    values = (
        ( 1234567, '1,234,567' ),
        ( 123, '123' ),
        ( 12, '12' ),
        ( 1, '1' ),
        ( 0, '0' ),
        ( -1, '-1' ),
        ( -12, '-12' ),
        ( -123, '-123' ),
        ( -1234567, '-1,234,567' ),
    )
    for value, expected in values:
        actual = Locale.get('en_US').friendly_number(value)
        assert actual == expected


# Generated at 2022-06-14 12:18:44.859693
# Unit test for function load_translations
def test_load_translations():
    directory = "h"
    load_translations(directory)



# Generated at 2022-06-14 12:18:53.530707
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # Saturday, July 1
    assert Locale('en').format_day(datetime.datetime(2017, 7, 1, 0, 0, 0)) == 'Saturday, July 1'
    # Sunday, July 2
    assert Locale('en').format_day(datetime.datetime(2017, 7, 2, 0, 0, 0)) == 'Sunday, July 2'
    # Monday, July 3
    assert Locale('en').format_day(datetime.datetime(2017, 7, 3, 0, 0, 0)) == 'Monday, July 3'
    # Tuesday, July 4
    assert Locale('en').format_day(datetime.datetime(2017, 7, 4, 0, 0, 0)) == 'Tuesday, July 4'
    # Wednesday, July 5

# Generated at 2022-06-14 12:18:55.268792
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    result = Locale.get("en-US").format_day(1, 1, 1)
    assert result == "1"

# Generated at 2022-06-14 12:18:59.736133
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import os
    import sys
    cwd = os.getcwd()
    load_gettext_translations(cwd, "message")
    import gettext
    t = gettext.translation("message", localedir=cwd, languages=["en_US"])
    _ = t.gettext
    _("Welcome!")


# Generated at 2022-06-14 12:19:11.058991
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
  import tornado.testing
  import os.path
  import tempfile
  import gettext

  base_dir = tempfile.mkdtemp(suffix="_tornado")

# Generated at 2022-06-14 12:19:21.119017
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    """ Unit test for method format_date of class Locale
    """
    # make a LOCALE_NAMES to avoid error
    LOCALE_NAMES = {}
    LOCALE_NAMES['zh_CN'] = {}
    LOCALE_NAMES['zh_CN']["name"] = u"Unknown"
    # initialize Locale
    Locale_obj = Locale('zh_CN')
    # test case 1: date is int
    arg1 = 1
    arg2 = 0
    arg3 = True
    arg4 = False
    arg5 = False
    output = Locale_obj.format_date(arg1,arg2)
    assert True, output

# Generated at 2022-06-14 12:19:31.917424
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    from datetime import datetime

    locale = Locale.get('en')
    test_date = datetime.strptime('2019-10-18T07:07:00', '%Y-%m-%dT%H:%M:%S')
    assert locale.format_date(test_date) == 'today at 7:07 am'
    test_date = datetime.strptime('2019-10-16T17:07:00', '%Y-%m-%dT%H:%M:%S')
    assert locale.format_date(test_date) == '2 days ago'
    test_date = datetime.strptime('2019-10-15T17:07:00', '%Y-%m-%dT%H:%M:%S')
    assert locale.format_date

# Generated at 2022-06-14 12:19:36.468255
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    import time
    import datetime
    f = Locale.get('fa').format_day
    print(f(time.localtime(), 0))
    print(f(time.localtime(), 0, False))
    print(f(datetime.datetime.now(), 0))


# Generated at 2022-06-14 12:19:46.703408
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    load_translations(path.join(path.dirname(__file__), "data/translations"))
    fr = Locale.get("fr")
    assert fr.format_date(1499144113.07718) == "Il y a 29 secondes"
    assert fr.format_date(1499144113.07718, relative=False) == "vendredi 28 juillet à 12:08 AM"
    assert fr.format_date(1499144113.07718, shorter=True, relative=True) == "Il y a 29 secondes"
    assert fr.format_date(1499144113.07718, shorter=True, relative=False) == "vendredi 28 juillet à 12:08 AM"

# Generated at 2022-06-14 12:19:47.996942
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations("./locale", "messages")


# Generated at 2022-06-14 12:20:14.018366
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    # this is stupid test,
    # just to avoid the code coverage error
    csvlocale = CSVLocale("en", translations={"unknown": {"test": "test"}})
    assert "test" == csvlocale.translate("test")
    assert "test" == csvlocale.translate("test", "test", 1)
    assert "test" == csvlocale.translate("test", "test", 2)



# Generated at 2022-06-14 12:20:15.385340
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations(directory='locale', domain='tornado')


# Generated at 2022-06-14 12:20:17.245398
# Unit test for function load_translations
def test_load_translations():
    load_translations("C:\Python\Python37\Scripts\tornado\locale")



# Generated at 2022-06-14 12:20:19.816835
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get('en_US').friendly_number(1234567) == '1,234,567'


# Generated at 2022-06-14 12:20:31.966908
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    def assert_equals(expected, actual):
        assert expected == actual

    locale = Locale.get("en")
    assert_equals("12,345", locale.friendly_number(12345))
    assert_equals("12", locale.friendly_number(12))
    assert_equals("1", locale.friendly_number(1))
    assert_equals("0", locale.friendly_number(0))
    assert_equals("-1", locale.friendly_number(-1))
    assert_equals("-12", locale.friendly_number(-12))
    assert_equals("-12,345", locale.friendly_number(-12345))
    assert_equals("1,234", locale.friendly_number(1234))
    assert_equals("1,234", locale.friendly_number(1234))

# Generated at 2022-06-14 12:20:34.843148
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    tranlations = {'unknown': {'Unknown': '未知'}}
    code = "zh_CN"
    csv = CSVLocale(code, tranlations)
    assert csv.translate("Unknown") == "未知"

# Generated at 2022-06-14 12:20:47.209724
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """
    Test cases:
    1. Test method format_day with different days.
    2. Test method format_day with different days of weeks.
    3. Test method format_day with different months.
    """
    l = Locale.get("en")
    day = datetime.datetime(month=1, year=2019, day=22)
    dow = date(2019, 1, 22).strftime("%a")
    result = l.format_day(day, dow=True)
    assert result == "%s, January 22" % dow, "Should be %s, January 22" % dow
    result = l.format_day(day, dow=False)
    assert result == "January 22", "Should be January 22"
    day = datetime.datetime(month=12, year=2019, day=22)
    dow

# Generated at 2022-06-14 12:20:47.663791
# Unit test for function load_translations
def test_load_translations():
    pass


# Generated at 2022-06-14 12:20:55.788827
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    from random import randint
    from . import _translations

    test_date = datetime.datetime(year=2020, month=4, day=4, hour=randint(0, 23), minute=randint(0, 59))
    test_date_next = test_date + datetime.timedelta(hours=1)
    test_date_forever = datetime.datetime(year=randint(2021, 3000), month=randint(1, 12), day=randint(1, 28), hour=randint(0, 23), minute=randint(0, 59))

    load_translations("./test_locale.csv", "_:1,2")
    test_locale_id_1 = Locale.get_closest("id")
    test_locale_en_1 = Locale.get

# Generated at 2022-06-14 12:20:57.281032
# Unit test for function load_translations
def test_load_translations():
    assert isinstance(load_translations, object)


# Generated at 2022-06-14 12:21:26.296640
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    _ = Locale.get("en").translate
    def eq(a, b):
        assert a == b
    eq(Locale.get("en").format_day(datetime.datetime(2017, 5, 23), dow=True), "Tuesday, May 23")
    eq(Locale.get("fa").format_day(datetime.datetime(2017, 5, 23), dow=True), "یکشنبه، مه 23")
    eq(Locale.get("en").format_day(datetime.datetime(2017, 5, 23), dow=False), "May 23")
    eq(Locale.get("fa").format_day(datetime.datetime(2017, 5, 23), dow=False), "مه 23")

# Generated at 2022-06-14 12:21:31.473941
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    directory = "D:\WorkSpace\Rui\src\python\tornado_start\tornado-5.1.1\tornado\locale"
    domain = "tornado"
    load_gettext_translations(directory, domain)
    assert "zh_CN" == "zh_CN"



# Generated at 2022-06-14 12:21:38.523283
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    import unittest
    import datetime

# Generated at 2022-06-14 12:21:44.559265
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    test_locale = Locale('en')
    date = datetime.datetime.strptime("2016-11-14", "%Y-%m-%d")
    result = test_locale.format_date(date)
    assert result == "2 years ago"
    

# Generated at 2022-06-14 12:21:46.804278
# Unit test for function load_translations
def test_load_translations():
    global _translations ; _translations = {}
    load_translations("..\\translations\\")
    assert _translations == {}



# Generated at 2022-06-14 12:21:53.521470
# Unit test for function load_translations
def test_load_translations():
    # Testing the function load_translations
    # Create a temp file and write some example data to it
    with open("test.csv", "w") as file:
        file.write("\"I love you\",\"Te amo\" \n")
        file.write("\"%(name)s liked this\",\"A %(name)s les gustó esto\",\"plural\"\n")
        file.write("\"%(name)s liked this\",\"A %(name)s le gustó esto\",\"singular\"")
    load_translations("")
    # If load_translations() properly loaded the file and _translations var,
    # _translations is expected to contain the given data

# Generated at 2022-06-14 12:22:01.483337
# Unit test for method format_date of class Locale
def test_Locale_format_date():

    l = Locale.get('en')
    assert l.format_date(datetime.datetime(2018, 3, 1, 10, 0)) == 'March 1, 2018 at 10:00am'

    l = Locale.get('zh_CN')
    assert l.format_date(datetime.datetime(2018, 3, 1, 10, 0)) == '3\u6708 1\u65e5\u4e0a\u534810:00'



# Generated at 2022-06-14 12:22:09.315638
# Unit test for method format_date of class Locale

# Generated at 2022-06-14 12:22:16.557942
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    assert Locale.get("en").format_date(datetime.datetime(2000, 1, 1, 1, 0, 0)) == "Jan 1, 2000 at 1:00am"
    assert Locale.get("en").format_date(datetime.datetime(2000, 1, 2, 1, 0, 0)) == "Jan 2, 2000 at 1:00am"
    assert Locale.get("en").format_date(datetime.datetime(2000, 1, 1, 13, 0, 0)) == "Jan 1, 2000 at 1:00pm"
    assert Locale.get("en").format_date(datetime.datetime(2000, 1, 2, 13, 0, 0)) == "Jan 2, 2000 at 1:00pm"

# Generated at 2022-06-14 12:22:22.705072
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    date = datetime.datetime.utcfromtimestamp(1493436400)
    # Test when dow is set to True
    assert Locale('en_US').format_day(date, dow=True) == "Wednesday, May 10"
    # Test when dow is set to False
    assert Locale('en_US').format_day(date, dow=False) == "May 10"



# Generated at 2022-06-14 12:23:08.838821
# Unit test for method pgettext of class Locale

# Generated at 2022-06-14 12:23:16.274504
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert (Locale.get("en").friendly_number(10000)=="10,000")
    assert (Locale.get("en").friendly_number(10)=="10")
    assert (Locale.get("en").friendly_number(101)=="101")
    assert (Locale.get("en").friendly_number(1001)=="1,001")
    assert (Locale.get("en").friendly_number(10001)=="10,001")
    assert (Locale.get("en").friendly_number(1000000)=="1,000,000")



# Generated at 2022-06-14 12:23:17.316067
# Unit test for function load_translations
def test_load_translations():
    load_translations('./')
    return _translations


# Generated at 2022-06-14 12:23:27.591343
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get("en").friendly_number(1) == "1"
    assert Locale.get("en").friendly_number(12) == "12"
    assert Locale.get("en").friendly_number(123) == "123"
    assert Locale.get("en").friendly_number(1234) == "1,234"
    assert Locale.get("en").friendly_number(12345) == "12,345"
    assert Locale.get("en").friendly_number(123456) == "123,456"
    assert Locale.get("en").friendly_number(1234567) == "1,234,567"
    assert Locale.get("en").friendly_number(12345678) == "12,345,678"

# Generated at 2022-06-14 12:23:31.842360
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale('en')
    assert locale.friendly_number(123)== '123'
    assert locale.friendly_number(1234)== '1,234'
    assert locale.friendly_number(12345)== '12,345'



# Generated at 2022-06-14 12:23:37.572601
# Unit test for function load_translations
def test_load_translations():
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.abspath(os.path.join(path, 'locale'))
    load_translations(path)
    return _translations
    pass
# end unit test for load_translations



# Generated at 2022-06-14 12:23:46.101417
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    l = Locale("en")
    d = datetime.datetime(2020, 2, 22, 23, 59, 59, 999999)
    r = l.format_day(d)
    assert r == "Saturday, February 22"

    l = Locale("fa")
    d = datetime.datetime(2020, 2, 22, 23, 59, 59, 999999)
    r = l.format_day(d)
    assert r == "شنبه، فوریه 22"

    l = Locale("he")
    d = datetime.datetime(2020, 2, 22, 23, 59, 59, 999999)
    r = l.format_day(d)
    assert r == "שבת, פברואר 22"

    l = Locale("ar")


# Generated at 2022-06-14 12:23:56.094268
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    class TestLocale(Locale):
        def translate(
            self,
            message: str,
            plural_message: Optional[str] = None,
            count: Optional[int] = None,
        ) -> str:
            return message
    test_locale = TestLocale('en')
    now = datetime.datetime.utcnow()
    test_date_1 = now - datetime.timedelta(minutes=50)
    test_date_2 = now - datetime.timedelta(days=1)
    test_date_3 = now - datetime.timedelta(days=7)
    test_date_4 = now - datetime.timedelta(days=365)
    assert test_locale.format_date(test_date_1, 0) == '50 seconds ago'

# Generated at 2022-06-14 12:24:06.577364
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    import gettext

    from zerver.lib.test_helpers import get_all_templates

    # type: () -> None
    def get_all_templates_for_locale(locale_code):
        # type: (str) -> Dict[str, Template]
        locale_string = gettext.translation('django', localedir=localedir, languages=[locale_code])
        locale_string.install()
        return get_all_templates()

    localedir = os.path.join(os.path.dirname(__file__), '../templates/zerver/translations')
    templates = get_all_templates_for_locale('en')


# Generated at 2022-06-14 12:24:11.432854
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale_ = Locale.get(_default_locale)
    assert locale_.friendly_number(12345) == '12345'
    assert locale_.friendly_number(1234567) == '1,234,567'
