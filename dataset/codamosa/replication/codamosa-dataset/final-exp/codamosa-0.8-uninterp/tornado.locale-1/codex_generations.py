

# Generated at 2022-06-14 12:16:24.318760
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    print(Locale.get("en").format_day(datetime.datetime(year=2018, month=5, day=4)))

test_Locale_format_day()


# Generated at 2022-06-14 12:16:27.020716
# Unit test for function load_translations
def test_load_translations():
    directory = './locale_data'
    language = [
        'en_US',
        'es_LA',
        'fr_FR',
        'de_DE',
        'it_IT',
        'zh_CN'
    ]
    for lang in language:
        load_translations(directory, lang)


# Generated at 2022-06-14 12:16:32.944622
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get("en_US")
    assert locale.format_day(datetime.datetime(2019, 9, 8, 23, 56, 48)) == "Sunday, September 8" # test for a normal day
    assert locale.format_day(datetime.datetime(2019, 9, 8, 23, 56, 48), dow=False) == "September 8" # test for a day without dow
    assert locale.format_day(datetime.datetime(2019, 1, 1, 23, 56, 48)) == "Tuesday, January 1" # test for new year's day
    assert locale.format_day(datetime.datetime(2019, 1, 1, 23, 56, 48), dow=False) == "January 1" # test for new year's day without dow

# Generated at 2022-06-14 12:16:34.263163
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    #  TODO: write the test
    pass


# Generated at 2022-06-14 12:16:42.210090
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """
    To test format_day, we created a test case where we compare the
    format_day method's generated date to one manually written.
    We have also provided 2 test cases, one with the dow and one without.
    """

    date = datetime.datetime(2020, 5, 2, 19, 2, 4, 7)
    gmt_offset = 0
    dow = True
    assert Locale("en").format_day(date, gmt_offset, dow) == "Saturday, May 2"

    dow = False
    assert Locale("en").format_day(date, gmt_offset, dow) == "May 2"


# Generated at 2022-06-14 12:16:45.870931
# Unit test for function load_translations
def test_load_translations():
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)),'template')
    load_translations(d)
    print(_translations)
    assert _translations != {}
# test_load_translations()



# Generated at 2022-06-14 12:16:49.013977
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    l = Locale('en-US')
    date = datetime.datetime.utcnow()
    dow = l.format_day(date)
    assert dow == l._weekdays[date.weekday()] + ", " + l._months[date.month - 1] + " " + str(date.day)
    dow = l.format_day(date, dow=False)
    assert dow == l._months[date.month - 1] + " " + str(date.day)



# Generated at 2022-06-14 12:16:55.948310
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    for t in [
        (datetime.datetime(2010, 8, 15, 12, 30), 'Sunday, August 15'),
        (datetime.datetime(2010, 8, 16, 12, 30), 'Monday, August 16'),
        (datetime.datetime(2010, 8, 17, 12, 30), 'Tuesday, August 17'),
        (datetime.datetime(2010, 8, 18, 12, 30), 'Wednesday, August 18'),
        (datetime.datetime(2010, 8, 19, 12, 30), 'Thursday, August 19'),
        (datetime.datetime(2010, 8, 20, 12, 30), 'Friday, August 20'),
        (datetime.datetime(2010, 8, 21, 12, 30), 'Saturday, August 21')
    ]:
        assert Locale.get('fa_IR').format_day

# Generated at 2022-06-14 12:17:01.209330
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    try:
        _ = Locale.get("en")
        _.pgettext("test context", "message")
        _.pgettext("test context", "singular message", "plural message")
        _.pgettext("test context", "singular message", "plural message", 1)
        _.pgettext("test context", "singular message", "plural message", 2)
    except Exception as err:
        print(err)


# Generated at 2022-06-14 12:17:05.241583
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert type(_translations) == dict
    assert type(_supported_locales) == frozenset
    assert type(_use_gettext) == bool
    #TODO: Exception case


# Generated at 2022-06-14 12:17:33.231364
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    os.system(r"python ./test_tornado_locale.py")



# Generated at 2022-06-14 12:17:35.073108
# Unit test for function load_translations
def test_load_translations():
    load_translations('locale')
    assert _translations != {}

# Generated at 2022-06-14 12:17:44.500998
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale("en").format_day(datetime.datetime(2016, 4, 5)) == "Tuesday, April 5"
    assert Locale("en").format_day(datetime.datetime(2016, 4, 5), dow=False) == "April 5"
    assert Locale("fa").format_day(datetime.datetime(2016, 4, 5)) == "دوشنبه، آوریل 5"
    assert Locale("fa").format_day(datetime.datetime(2016, 4, 5), dow=False) == "آوریل 5"
    # Check for specific language codes that are not in LOCALE_NAMES

# Generated at 2022-06-14 12:17:49.473596
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    test_list = [
        {
            "input_value": [123456789],
            "expected_value": "123,456,789",
            "comment": "",
        },
        {
            "input_value": [0],
            "expected_value": "0",
            "comment": "",
        },
    ]
    for test in test_list:
        result = Locale("en_US").friendly_number(test["input_value"][0])
        assert result == test["expected_value"]


# Generated at 2022-06-14 12:17:59.183077
# Unit test for function load_translations
def test_load_translations():
    import tempfile
    import os
    import csv
    import shutil
    tmpdirname = tempfile.mkdtemp()

# Generated at 2022-06-14 12:18:02.682548
# Unit test for function load_translations
def test_load_translations():
	#from tornado.locale import load_translations
	load_translations("D:\\Homework\\Projects\\nailgun\\test_data\\test_locale_data")
	print(_translations)


# Generated at 2022-06-14 12:18:05.233501
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    assert False, "Need to write Unit test for method pgettext of class Locale"



# Generated at 2022-06-14 12:18:16.989216
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    # Test the case of english and english_US non-friendly number
    assert Locale('en').friendly_number(12345) == "12345"
    assert Locale('en_US').friendly_number(12345) == "12345"
    # Test the case of english and english_US friendly number
    assert Locale('en').friendly_number(1234567) == "1,234,567"
    assert Locale('en_US').friendly_number(1234567) == "1,234,567"
    # Test the case of non-english and non-english_US friendly number
    assert Locale('fa').friendly_number(12345) == "12345"
    assert Locale('fa').friendly_number(1234567) == "1234567"



# Generated at 2022-06-14 12:18:17.649161
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    pass

# Generated at 2022-06-14 12:18:28.548387
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """
    Asserts that format_day method works correctly on a real example
    """
    import time
    import datetime
    import pytz

    def convert(date, timezone):
        tz = timezone(timezone)
        date = tz.localize(date)
        return date.astimezone(pytz.UTC)

    def year_month_day(date):
        return date.strftime("%Y-%m-%d")

    def convert_to_year_month_day(date, timezone):
        return year_month_day(convert(date, timezone))

    UTC = pytz.utc
    EDT = pytz.timezone("US/Eastern")
    IST = pytz.timezone("Asia/Kolkata")


# Generated at 2022-06-14 12:18:51.358427
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    print(GettextLocale.pgettext(context = "mycontext", message = "mymessage", plural_message = "mypluralmessage", count = 10))



# Generated at 2022-06-14 12:18:56.736300
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    test_code = "en"
    test_translations = {"singular": {"singular_message": "singular_message_output"},
                         "plural": {"plural_message": "plural_message_output"}}
    test_message = "singular_message"
    test_plural_message = "plural_message"
    test_count = 1
    test_locale = CSVLocale(test_code, test_translations)
    assert test_locale.translate(test_message, test_plural_message, test_count) == "singular_message_output"


# Generated at 2022-06-14 12:18:58.459468
# Unit test for function load_gettext_translations

# Generated at 2022-06-14 12:19:09.814307
# Unit test for function load_translations
def test_load_translations():
    import os
    os.chdir('/Users/JoJo/OneDrive/Coding/Python/tornado-localization/')
    global _translations
    global _supported_locales
    load_translations('./')
    print(_supported_locales)
    print(_translations)
    # print(_translations['en_US']['unknown']['I'])
    # print(_translations['zh_CN']['unknown']['我的名字'])
    # print(_translations['es']['unknown']['Mi nombre es'])
    # print(_translations['en_US']['unknown']['My name is'])



# Generated at 2022-06-14 12:19:21.790367
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get('en').friendly_number(1) == '1'
    assert Locale.get('en_US').friendly_number(1) == '1'
    assert Locale.get('es').friendly_number(1) == '1'
    assert Locale.get('en').friendly_number(10) == '10'
    assert Locale.get('en_US').friendly_number(10) == '10'
    assert Locale.get('es').friendly_number(10) == '10'
    assert Locale.get('en').friendly_number(100) == '100'
    assert Locale.get('en_US').friendly_number(100) == '100'
    assert Locale.get('es').friendly_number(100) == '100'

# Generated at 2022-06-14 12:19:29.160742
# Unit test for function load_translations
def test_load_translations():
    import tornado
    import sys
    test_directory = os.getcwd()
    sys.path.append(test_directory)
    tornado.locale.load_translations(test_directory)
    assert len(_translations) == 1
    assert _translations["es_GT"] == {'unknown': {'"I love you"': '"Te amo"'}}
    assert len(_supported_locales) == 2

test_load_translations()



# Generated at 2022-06-14 12:19:34.216817
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get("en_US").friendly_number(123) == "123"
    assert Locale.get("en_US").friendly_number(1234) == "1,234"
    assert Locale.get("en_US").friendly_number(12345) == "12,345"
    assert Locale.get("en_US").friendly_number(123456) == "123,456"
    assert Locale.get("en_US").friendly_number(1234567) == "1,234,567"



# Generated at 2022-06-14 12:19:44.993810
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    _months_pt_BR = [
        u"Janeiro",
        u"Fevereiro",
        u"Mar\xe7o",
        u"Abril",
        u"Maio",
        u"Junho",
        u"Julho",
        u"Agosto",
        u"Setembro",
        u"Outubro",
        u"Novembro",
        u"Dezembro",
    ]
    _weekdays_pt_BR = [
        u"Segunda",
        u"Ter\xe7a",
        u"Quarta",
        u"Quinta",
        u"Sexta",
        u"S\xe1bado",
        u"Domingo",
    ]

# Generated at 2022-06-14 12:19:50.248764
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations("./locale","tornado-hello-world")
    par = "introduction"
    result = _translations["fr_FR"].gettext(par)
    assert result == "Il s'agit d'un programme Hello World fonctionnant sur le port 8080", "Fonction error"



# Generated at 2022-06-14 12:19:59.174402
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale("en").friendly_number(1000) == "1,000"
    assert Locale("en").friendly_number(1000000) == "1,000,000"
    assert Locale("en").friendly_number(10000000) == "10,000,000"
    assert Locale("en").friendly_number(12345) == "12,345"
    assert Locale("fr_FR").friendly_number(1000) == "1000"
    assert Locale("fr_FR").friendly_number(1000000) == "1000000"
    assert Locale("fr_FR").friendly_number(10000000) == "10000000"
    assert Locale("fr_FR").friendly_number(12345) == "12345"



# Generated at 2022-06-14 12:20:48.155824
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    # 测试参数为空
    try:
        load_gettext_translations('','')
    except Exception as e:
        print(e)
    # 测试参数存在重复 
    try:
        load_gettext_translations('/tornado/locale/cldr','/tornado/locale/cldr')
    except Exception as e:
        print(e)
    # 测试参数存在不同路径
    try: 
        load_gettext_translations('/tornado/locale/cldr','/tornado/locale')
    except Exception as e:
        print(e)
    # 测试参数

# Generated at 2022-06-14 12:20:54.903469
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import tornado
    tornado.locale.load_gettext_translations(r'test/data', 'tornado')
    loc = tornado.locale.get('zh_CN')
    assert (loc.translate('Hello') == '你好')
    tornado.locale.set_default_locale('zh_CN')
    assert (loc.translate('Hello') == '你好')
    tornado.locale.set_default_locale('en_US')
    assert (loc.translate('Hello') == '你好')
    assert (len(tornado.locale.get_supported_locales()) > 0)



# Generated at 2022-06-14 12:20:57.909297
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert(Locale("en_US").format_day(datetime.datetime(2019, 10, 22), dow=True) == "Tuesday, October 22")

# Generated at 2022-06-14 12:21:00.625035
# Unit test for function load_gettext_translations

# Generated at 2022-06-14 12:21:02.345658
# Unit test for function load_translations
def test_load_translations():
    directory = ""
    encoding = "utf-8"
    return load_translations(directory, encoding)


# Generated at 2022-06-14 12:21:12.115253
# Unit test for method list of class Locale
def test_Locale_list():
    assert Locale.get('en').list(['A']) == 'A'
    assert Locale.get('en').list(['A', 'B']) == 'A and B'
    assert Locale.get('en').list(['A', 'B', 'C']) == 'A, B and C'
    assert Locale.get('fa').list(['A']) == 'A'
    assert Locale.get('fa').list(['A', 'B']) == 'A و B'
    assert Locale.get('fa').list(['A', 'B', 'C']) == 'A و B و C'
test_Locale_list()



# Generated at 2022-06-14 12:21:19.814681
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations("/not/exists","not_found")
    assert _translations=={}
    load_gettext_translations("/usr/share/locale","tornado")
    assert sorted(_translations)==sorted(_supported_locales)==['en_US']
    load_gettext_translations("test/translations","tornado")

# Generated at 2022-06-14 12:21:25.818624
# Unit test for function load_translations
def test_load_translations():
    directory = './test_locale'
    load_translations(directory)
    locale = 'en_US'
    expected = "Hello, world!"
    if locale in _translations:
        actual = _translations[locale]['unknown']['Hello, world!']
    else:
        actual = 'Hello, world!'
    assert(expected == actual)



# Generated at 2022-06-14 12:21:33.907759
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    """
    To manually test this function, first, create a directory of the form
    {directory}/{lang}/LC_MESSAGES/{domain}.mo, e.g.
    load_translation_test/es_ES/LC_MESSAGES/tornado.mo
    Then call this function with load_gettext_translations(
    "load_translation_test", "tornado")
    This will result in a printed message, "Supported locales: ['es_ES']"
    """
    load_gettext_translations("load_translation_test", "tornado")



# Generated at 2022-06-14 12:21:46.199570
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    try:
        import polib
    except ImportError:
        print("You need to install polib to run this unit test")
        return
    import tempfile
    import shutil
    import os.path
    import subprocess
    # create base translations
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 12:22:14.857229
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale("fa_IR").friendly_number(1) == "1"
    assert Locale("fa_IR").friendly_number(12) == "12"
    assert Locale("fa_IR").friendly_number(123) == "123"
    assert Locale("fa_IR").friendly_number(1234) == "1,234"
    assert Locale("fa_IR").friendly_number(12345) == "12,345"
    assert Locale("fa_IR").friendly_number(123456) == "123,456"
    assert Locale("fa_IR").friendly_number(1234567) == "1,234,567"
    assert Locale("fa_IR").friendly_number(12345678) == "12,345,678"

# Generated at 2022-06-14 12:22:26.261403
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from datetime import datetime
    from mock import patch
    from random import randint
    from copy import copy

    locale = Locale(code = _default_locale)

    # Test with dow = True
    expectedDate = datetime(year = randint(1, 9999),
            month = randint(1,12), day = randint(1,28),
            hour = randint(0, 23), minute = randint(0, 59),
            second = randint(0, 59))
    with patch("datetime.datetime.utcnow") as patched_datetime:
        patched_datetime.return_value = expectedDate
        actualDate = locale.format_day(date = copy(expectedDate), dow = True, gmt_offset = 0)
        # Compare if actualDate is equal to expectedDate, _months and _week

# Generated at 2022-06-14 12:22:29.814742
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale('en_US')
    assert locale.friendly_number(10) == '10'
    assert locale.friendly_number(1000000) == '1,000,000'


# Generated at 2022-06-14 12:22:30.357985
# Unit test for function load_translations
def test_load_translations():
    assert True


# Generated at 2022-06-14 12:22:40.943431
# Unit test for function load_translations
def test_load_translations():
    from tornado.locale import load_translations
    # It's difficult to unit test load_translations directly since it
    # reads a filesystem directory. Use a closure to test it indirectly.
    def test_translations(locale, english, localized):
        assert get(locale).translate(english) == localized
    load_translations(os.path.join(os.path.dirname(__file__), "locale"))
    test_translations('en_US', 'hello', 'hello')
    test_translations('es_MX', 'hello', 'hola')
    test_translations('es_MX', 'hello %(name)s', 'hola %(name)s')



# Generated at 2022-06-14 12:22:51.522597
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert(Locale("en").format_day(datetime.datetime(2020, 1, 21))) == 'Tuesday, January 21'
    assert(Locale("en_US").format_day(datetime.datetime(2020, 1, 21))) == 'Tuesday, January 21'
    assert(Locale("en").format_day(datetime.datetime(2020, 1, 21), dow=False)) == 'January 21'
    assert(Locale("en_US").format_day(datetime.datetime(2020, 1, 21), dow=False)) == 'January 21'
    assert(Locale("it").format_day(datetime.datetime(2020, 1, 21))) == 'martedì, 21 gennaio'

# Generated at 2022-06-14 12:22:59.426981
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale("en_US")
    t = datetime.datetime(2019, 4, 1,0,0,0)
    assert locale.format_day(t) == "Monday, April 1"
    assert locale.format_day(t,gmt_offset=AMSTERDAM_OFFSET) == "Monday, April 1"
    assert locale.format_day(t,dow=False) == "April 1"
    assert locale.format_day(t,gmt_offset=AMSTERDAM_OFFSET,dow=False) == "April 1"
    try:
        locale.format_day(t,gmt_offset=37)
    except TypeError as e:
        assert str(e) == "gmt_offset should be an integer"
    else:
        assert False



# Generated at 2022-06-14 12:23:02.524232
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    print(Locale.get("en_US").format_day(datetime.datetime(2019,1,20)))

# Generated at 2022-06-14 12:23:10.572173
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale.get("en")
    assert locale.friendly_number(1) == '1'
    assert locale.friendly_number(1000) == '1,000'
    assert locale.friendly_number(1234567) == '1,234,567'
    assert locale.friendly_number(12345678901234567890) == '12,345,678,901,234,567,890'
    # Test the reversed() call with a list with no elements
    locale.friendly_number(0)



# Generated at 2022-06-14 12:23:18.902693
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    import doctest
    from zulip_bots.bots.zulip_message_sender import ZulipMessageSender
    import zulip_bots.bots.converter.locale as locale

    locale.load_translations("locale")

    localeObj = Locale.get("en")
    print("Input: 1000")
    print("Output: " + localeObj.friendly_number(1000))
    print("Expected: 1,000")
    print("Input: 10")
    print("Output: " + localeObj.friendly_number(10))
    print("Expected: 10")
    assert(localeObj.friendly_number(1000) == '1,000')
    assert(localeObj.friendly_number(10) == '10')


# Generated at 2022-06-14 12:24:43.618735
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # Create Locale instance
    locale = Locale.get('de')
    assert isinstance(locale, Locale)
    
    # Test for relative=False
    date = datetime.datetime(2020, 6, 14, 2, 28, 2)
    assert locale.format_date(date, False) == '14. Juni 2020 um 2:28'
    
    # Test for relative=True
    now = datetime.datetime.utcnow()
    assert isinstance(locale.format_date(now), str)
    assert isinstance(locale.format_date(now), str)
    # Test for full_format=True
    date2 = datetime.datetime(2019, 12, 12, 12, 1, 25)

# Generated at 2022-06-14 12:24:54.503455
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    directory='./'
    domain = 'mydomain'
    load_gettext_translations(directory, domain)
    print('Supported locales: %s' % sorted(_supported_locales))
    print('gettext: %s' % _use_gettext)
    for lang in os.listdir(directory):
        if lang.startswith("."):
            print('skip .svn, etc')
        elif os.path.isfile(os.path.join(directory, lang)):
            print('is file')

# Generated at 2022-06-14 12:25:04.291269
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import os
    import tempfile
    import shutil
    import subprocess
    import tornado.locale
    from tornado._locale_data import LOCALE_NAMES
    from tornado.testing import AsyncHTTPTestCase, ExpectLog

    class TranslationTests(AsyncHTTPTestCase):

        def setUp(self):
            super(TranslationTests, self).setUp()
            # create temporary translation directory
            obj = tempfile.mkdtemp(prefix=__name__)
            self.addCleanup(shutil.rmtree, obj)
            self.translation_dir = obj
            # create gettext .po file
            obj = tempfile.NamedTemporaryFile(prefix=__name__, suffix=".po", mode="wt")
            self.addCleanup(obj.close)
            self.translation_po = obj.name


# Generated at 2022-06-14 12:25:14.548222
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    a = Locale.get("en")
    assert a.friendly_number(1234) == "1,234"
    assert a.friendly_number(12345678) == "12,345,678"
    assert a.friendly_number(1) == "1"
    assert a.friendly_number(0) == "0"
    assert a.friendly_number(12) == "12"
    assert a.friendly_number(123) == "123"

    b = Locale.get("fa")
    assert b.friendly_number(1) == "1"
    assert b.friendly_number(0) == "0"
    assert b.friendly_number(1234) == "1234"
    assert b.friendly_number(12345678) == "12345678"



# Generated at 2022-06-14 12:25:17.955815
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get("fa_IR").friendly_number(1000) == '۱,۰۰۰'
    assert Locale.get("en_US").friendly_number(1000) == '1,000'



# Generated at 2022-06-14 12:25:28.221402
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    result = Locale.get('en_US').format_day(datetime.datetime.now(), dow = False)
    print(result)

test_Locale_format_day()

### test code
# load translations
load_translations(os.path.join(os.path.dirname(__file__), 'translations'))

# test
# print(get_closest_locale('zh-CN'))
# print('Supported Locales:', get_supported_locales())

# en_US_locale = get_closest_locale('en_US')
# print(en_US_locale.translate('January'))
# print(en_US_locale.format_date(datetime.datetime.now()))
# print(en_US_locale.format_day(

# Generated at 2022-06-14 12:25:33.071250
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    gen_log.debug("start test_load_gettext_translations")
    directory = "./test_data"
    domain = "test"
    load_gettext_translations(directory, domain)
    if not _use_gettext:
        gen_log.error("Cannot load gettext file")
# test
if __name__ == "__main__":
    test_load_gettext_translations()



# Generated at 2022-06-14 12:25:41.253126
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    l = Locale.get("en")
    # These two dates are far enough apart to test that the year doesn't appear
    d1 = datetime.datetime(2016, 1, 1)
    d2 = datetime.datetime(2016, 1, 2)
    d3 = datetime.datetime(2016, 1, 3)
    d4 = datetime.datetime(2016, 1, 4)
    d5 = datetime.datetime(2016, 1, 5)
    d6 = datetime.datetime(2016, 1, 6)
    d7 = datetime.datetime(2016, 1, 7)
    d8 = datetime.datetime(2016, 1, 8)
    assert l.format_day(d1, dow=False) == "January 1"