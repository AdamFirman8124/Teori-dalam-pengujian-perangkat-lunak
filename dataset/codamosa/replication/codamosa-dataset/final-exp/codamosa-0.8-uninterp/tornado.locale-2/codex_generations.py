

# Generated at 2022-06-14 12:16:29.273367
# Unit test for function load_translations
def test_load_translations():
    dir = "../data/translations/"
    encoding = "utf-8-sig"
    for path in os.listdir(dir):
        if not path.endswith(".csv"):
            continue
        locale, extension = path.split(".")
        if not re.match("[a-z]+(_[A-Z]+)?$", locale):
            gen_log.error(
                "Unrecognized locale %r (path: %s)",
                locale,
                os.path.join(dir, path),
            )
            continue
        full_path = os.path.join(dir, path)
        # Try to autodetect encoding based on the BOM.

# Generated at 2022-06-14 12:16:33.837974
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import inspect
    import os
    import sys

    path = os.path.dirname(inspect.getfile(get))
    path = os.path.join(path, "locale")
    load_gettext_translations(path, "tornado")
    for lang in os.listdir(path):
        if lang.startswith("."):
            continue  # skip .svn, etc
        if os.path.isfile(os.path.join(path, lang)):
            continue
        try:
            os.stat(os.path.join(path, lang, "LC_MESSAGES", "tornado.mo"))
            _translations[lang] = gettext.translation(
                "tornado", path, languages=[lang]
            )
        except Exception as e:
            print(e)
            continue

# Generated at 2022-06-14 12:16:39.051250
# Unit test for function load_translations
def test_load_translations():
    import os
    import sys

    try:
        directory = os.path.dirname(sys.modules[__name__].__file__)
    except (AttributeError, KeyError):
        directory = os.path.dirname(__file__)
    directory = os.path.join(directory, "translations")
    print(directory)
    load_translations(directory)
    return _translations



# Generated at 2022-06-14 12:16:49.882527
# Unit test for method translate of class CSVLocale

# Generated at 2022-06-14 12:16:52.559143
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations('tests/test_locale_gettext_translations', 'test')


# Generated at 2022-06-14 12:17:01.243142
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    from tornado import testing
    import tempfile
    import shutil
    import gettext
    import os

# Generated at 2022-06-14 12:17:11.848829
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    l = Locale('en')
    d = datetime.datetime(1986, 10, 22,14, 35)
    r = l.format_date(d)
    e = 'October 22, 1986 at 2:35 pm'
    assert r == e
    d = datetime.datetime(2019, 1, 6, 14, 34)
    r = l.format_date(d)
    e = '1 minute ago'
    assert r == e
    d = datetime.datetime(2019, 1, 6, 14, 7)
    r = l.format_date(d)
    e = '27 minutes ago'
    assert r == e
    d = datetime.datetime(2019, 1, 6, 11, 40)
    r = l.format_date(d)
    e = '2 hours ago'

# Generated at 2022-06-14 12:17:17.530483
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get_closest(['fa_IR'])
    date = datetime.datetime.now()
    print(locale.format_day(date, 0, False))
    # print(locale.code)

if __name__ == "__main__":
    test_Locale_format_day()

# Generated at 2022-06-14 12:17:26.470322
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    with mock.patch("pytz.timezone") as timezone:
        timezone_instance = timezone.return_value
        timezone_instance.localize.return_value = datetime.datetime(2020, 5, 22)
        locale = Locale.get("en_US")
        fmt = locale.format_day(datetime.datetime(2020, 5, 22), 0)
        assert fmt == "Friday, May 22"



# Generated at 2022-06-14 12:17:29.775169
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get("en")
    date = datetime.datetime.utcnow()
    date_str = locale.format_day(date, 0, True)
    assert date_str == datetime.datetime.strftime(date,
            '%A, %B %-d')

    date_str = locale.format_day(date, 0, False)
    assert date_str == datetime.datetime.strftime(date,
            '%B %-d')


# Generated at 2022-06-14 12:18:26.493662
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    try:
        path = os.path.join( os.path.dirname(__file__), "testdata", "locale")
        load_gettext_translations(path, "test")
    except Exception as e:
        gen_log.warning("Cannot load translation: %s", str(e))



# Generated at 2022-06-14 12:18:37.171237
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    import sys
    import random

    if '--help' in sys.argv or '-h' in sys.argv:
        print('usage: LocaleTest')
        sys.exit(1)

    # Set up supported locales
    locale_codes = ["en", "ja", "ko", "zh_CN", "en_US", "fa_IR"]
    # Check if pytest uses SysLogHandler to send logging message to syslog
    for handler in gen_log.handlers:
        if isinstance(handler, logging.handlers.SysLogHandler):
            break
    else:
        gen_log.addHandler(logging.handlers.SysLogHandler(address='/dev/log'))
    gen_log.info('testing tornado.locale.Locale')
    locale_names = {}

# Generated at 2022-06-14 12:18:42.901176
# Unit test for function load_translations
def test_load_translations():
    """
    def test_load_translations():
        path_o = 'E://Projects/python/tornado-5.0.2/tornado/locale/sp_SP.csv'
        with open(path_o, encoding='utf-8') as f:
            a = [x for x in csv.reader(f)]
        #print(a)
        print(len(a[0]))
        print(a[2])

    test_load_translations()
    """



# Generated at 2022-06-14 12:18:45.199637
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    """Unit tests for Locale.friendly_number"""
    locale = Locale('en')
    assert locale.friendly_number(1000000) == "1,000,000"



# Generated at 2022-06-14 12:18:53.768678
# Unit test for function load_translations
def test_load_translations():
    import unittest
    from unittest import mock
    from tornado.testing import AsyncTestCase, gen_test

    class FakeFile():
        def __init__(self, **kwargs):
            self.kwargs = kwargs
        def read(self):
            return "someting"
        def __enter__(self):
            return self
        def __exit__(self):
            return self

    class FakeOpen():
        def __init__(self, **kwargs):
            self.kwargs = kwargs
            return self
        def __enter__(self):
            return self
        def __exit__(self):
            return self

# Generated at 2022-06-14 12:19:03.044942
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    locale = Locale("fa")
    timezone = pytz.timezone("Asia/Tehran")
    date = timezone.localize(datetime.datetime(2019,8,20))
    date2 = timezone.localize(datetime.datetime(2019,7,20))
    date3 = timezone.localize(datetime.datetime(2020,8,20))
    date4 = timezone.localize(datetime.datetime(2019,7,11))
    date5 = timezone.localize(datetime.datetime(2019,7,9))
    assert(locale.format_date(date,relative=True) == "1398/6/29 ساعت 7:00:00")

# Generated at 2022-06-14 12:19:11.919489
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    test_date = datetime.datetime.utcnow()
    test_date_str = str(test_date.year)+"-"+str(test_date.month)+"-"+str(test_date.day)
    test_date_day = test_date.day
    test_date_month = test_date.month
    test_date_year = test_date.year
    test_date_weekday = test_date.weekday()
    test_date_str_expected = "Monday"
    test_date_day_expected = 22
    test_date_month_expected = 1
    test_date_year_expected = 2020
    test_date_weekday_expected = 0

    test_date = datetime.datetime.strptime(test_date_str, "%Y-%m-%d")
   

# Generated at 2022-06-14 12:19:16.849003
# Unit test for method format_date of class Locale

# Generated at 2022-06-14 12:19:21.711520
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import time

    t_now = time.time()
    t_yesterday = t_now - 24 * 3600
    t_two_days_ago = t_now - 2 * 24 * 3600
    t_in_2007 = time.mktime(time.strptime("2007-01-01", "%Y-%m-%d"))
    
    def check_result(result, expres):
        assert result == expres, \
                "invalid result: %s, expres: %s" % (result, expres)
    
    locale = Locale.get("en_US")
    check_result(locale.format_date(0, 0, False),
                    "1/1/1970 at 12:00am")

# Generated at 2022-06-14 12:19:23.511607
# Unit test for function load_translations
def test_load_translations():
    directory = "./blob"
    load_translations(directory)



# Generated at 2022-06-14 12:20:37.980915
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # Test that format_day work for different locales
    assert (Locale('en').format_day(datetime.datetime(2014, 12, 27)) == "Saturday, December 27")
    assert (Locale('fr').format_day(datetime.datetime(2014, 12, 27)) == "Samedi 27 D\u00e9cembre")
    # Test that the dow argument works
    assert (Locale('en').format_day(datetime.datetime(2014, 12, 27), dow=False) == "December 27")
    assert (Locale('fr').format_day(datetime.datetime(2014, 12, 27), dow=False) == "27 D\u00e9cembre")


# Generated at 2022-06-14 12:20:48.894021
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    t = tornado.escape.to_unicode
    l = Locale.get("ja_JP")
    assert l.format_day(datetime.datetime(2012, 1, 1), gmt_offset=0, dow=True) == t("2012\u5e741\u6708 1\u65e5\u91d1\u66dc\u65e5, 1\u6708 1\u65e5")
    assert l.format_day(datetime.datetime(2012, 1, 1), gmt_offset=0, dow=False) == t("1\u6708 1\u65e5")
    l = Locale.get("en_US")

# Generated at 2022-06-14 12:20:56.502018
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    l = Locale.get('en')
    assert l.format_date(datetime.datetime.utcnow() - datetime.timedelta(days=0, hours=0, minutes=2, seconds=24)) == "2 minutes ago"
    assert l.format_date(datetime.datetime.utcnow() - datetime.timedelta(days=0, hours=0, minutes=2)) == "2 minutes ago"
    assert l.format_date(datetime.datetime.utcnow() - datetime.timedelta(days=0, hours=2, minutes=0, seconds=0)) == "2 hours ago"

# Generated at 2022-06-14 12:21:01.026184
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    msg = 'saudi arabia'
    ctx = 'female'
    c_msg = ctx + '\x04' + msg
    c = Locale()
    assert c._pgettext(c_msg) == msg
    assert c._pgettext(c_msg, ctx) == msg

# Generated at 2022-06-14 12:21:02.045590
# Unit test for function load_translations
def test_load_translations():
    load_translations(".")


# Generated at 2022-06-14 12:21:08.806345
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    # Note: The file we used is a bit different from the one in test/system,
    # as we have updated that one to be compatible with the new version of
    # tornado's CSV translation format, so we would need to use the old
    # version of the CSV translation code (using
    # tornado.locale.load_translations).

    from django.utils.translation import activate, deactivate
    activate("en")
    import string  # type: ignore
    transformations = string.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")


# Generated at 2022-06-14 12:21:18.184729
# Unit test for method format_day of class Locale
def test_Locale_format_day():

    locale_data = ['en', 'zh_CN']
    locale_obj = []
    locale_obj.append(Locale.get(locale_data[0]))
    locale_obj.append(Locale.get(locale_data[1]))

    now = datetime.datetime.utcnow()
    result = []
    result.append(locale_obj[0].format_day(now))
    result.append(locale_obj[1].format_day(now))

    now = datetime.datetime.utcnow()
    result = []
    result.append(locale_obj[0].format_day(now))
    result.append(locale_obj[1].format_day(now))

    now = datetime.datetime.utcnow()
    result = []

# Generated at 2022-06-14 12:21:20.251767
# Unit test for function load_translations
def test_load_translations():
    assert _translations == {}
    #assert _supported_locales == ()
    # assert load_translations() == None



# Generated at 2022-06-14 12:21:32.547257
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """Test for method format_day of class Locale"""
    print("\n*** Testing for method format_day of class Locale ***")
    sample_date = datetime.datetime(2019, 9, 30, 13, 30, 0, 0)
    test_cases = [
        # test case        expected result
        # input parameters # -
        [(sample_date, 0,  True),  "Monday, September 30"],
        [(sample_date, 0,  False), "September 30"],
        [(sample_date, 240, True), "Sunday, September 29"],
        [(sample_date, 240, False), "September 29"],
        [(sample_date, -240, True), "Tuesday, October 1"],
        [(sample_date, -240, False), "October 1"],
    ]


# Generated at 2022-06-14 12:21:43.161216
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    test_cases = [
        (
            (datetime.datetime(year=2018, month=3, day=19), 60, True),
            'Monday, March 19',
        ),
        (
            (datetime.datetime(year=2018, month=3, day=19), 0, False),
            'March 19',
        ),
    ]
    for (test_case, expected) in test_cases:
        actual = Locale.get('en_US').format_day(*test_case)
        assert (actual == expected), 'FAILED test_Locale_format_day({0}, {1}) '\
            'expected {2}, actual {3}'.format(test_case, expected, actual)

# Generated at 2022-06-14 12:22:58.570222
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations('.', 'hello')
    assert('zh_CN'==_default_locale)
    assert(True==('zh_CN' in _supported_locales))
    assert(True==('zh_TW' in _supported_locales))
    assert(True==_use_gettext)



# Generated at 2022-06-14 12:23:10.658250
# Unit test for function load_translations
def test_load_translations():
    global _default_locale
    global _translations
    global _supported_locales
    _default_locale = "en_US"
    _translations = {}
    _supported_locales = frozenset([_default_locale])
    load_translations("./locale/")
    print(_translations)
    print("_default_locale:", _default_locale)
    print("_supported_locales:")
    for locale in _supported_locales:
        print(locale, end=" ")
    print("\n")
    i18n = get("es")
    print(i18n.translate("Sign out"))
    i18n = get("zh_CN")
    print(i18n.translate("Sign out"))
    i18n = get("en_US")


# Generated at 2022-06-14 12:23:14.902424
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    try:
        # TODO: make it possible to test this on systems that don't have French
        load_gettext_translations("locale", "tornado_test")
        assert get("fr_FR").translate("month-of-year") == "mois"
    finally:
        _translations = {}



# Generated at 2022-06-14 12:23:19.608612
# Unit test for function load_translations
def test_load_translations():
    locale = ["es_LA.csv"]
    directory = "test"
    load_translations(directory)
    assert(locale == ["es_LA.csv"])



# Generated at 2022-06-14 12:23:21.735431
# Unit test for function load_translations
def test_load_translations():
    load_translations(".")
    assert ("fr_FR" in _translations)



# Generated at 2022-06-14 12:23:26.307100
# Unit test for function load_translations
def test_load_translations():
    
    set_default_locale("en_us")
    #locale = "es_LA"
    #print(locale)
    output = load_translations("/home/phm/Documents/softwares/tornado-5.1.1/tornado/locale_test")
    print(output)
#test_load_translations()


# Generated at 2022-06-14 12:23:27.666913
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    '''
    test case of GettextLocale method pgettext
    '''

# Generated at 2022-06-14 12:23:40.532618
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    _translations = {
        'en': {
            'plural': {
                '%(hours)d hours ago': lambda hours: '%(hours)d hours ago' % {'hours': hours},
                '%(minutes)d minutes ago': lambda minutes: '%(minutes)d minutes ago' % {'minutes': minutes},
                '%(seconds)d seconds ago': lambda seconds: '%(seconds)d seconds ago' % {'seconds': seconds},
            }
        }
    }
    cur_locale = Locale.get('en')
    t0 = time.time()
    t1 = t0 - 19
    # t1 is 5s ago, %(time)s should not be added.
    assert cur_locale.format_date(t1) == '19 seconds ago'

# Generated at 2022-06-14 12:23:45.003516
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    import unittest
    import types
    import random
    import functools
    class Test_get(unittest.TestCase):
        def test_(self):
            pass
    def run_test(test):
        suite = unittest.TestSuite()
        suite.addTest(Test_get(test))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    run_test("test_")

# Generated at 2022-06-14 12:23:50.734995
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    l = Locale('en')
    t = datetime.datetime.utcnow()
    assert l.format_day(t) == "%s, %s %d" % (l._weekdays[t.weekday()], l._months[t.month - 1], t.day)
    assert l.format_day(t, dow=False) == "%s %d" % (l._months[t.month - 1], t.day)

