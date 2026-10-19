

# Generated at 2022-06-14 12:16:19.510851
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    from tornado.options import options

    import zerver.lib.test_classes

    backup_locale = options.pytest_locale
    options.pytest_locale = "en_US"
    locale = Locale.get(options.pytest_locale)


# Generated at 2022-06-14 12:16:29.243570
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    #test format_date
    assert(Locale("en_US").format_date(datetime.datetime(2011, 1, 1), 0) == "January 1, 2011")
    assert(Locale("en_US").format_date(datetime.datetime(2011, 1, 1), 0, False) == "January 1, 2011")
    assert(Locale("en_US").format_date(datetime.datetime(2011, 1, 2), 0) == "yesterday")
    assert(Locale("en_US").format_date(datetime.datetime(2011, 1, 3), 0) == "Monday")
    assert(Locale("en_US").format_date(datetime.datetime(2011, 1, 4), 0) == "Tuesday")

# Generated at 2022-06-14 12:16:38.470932
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    local_path = os.path.join(os.path.dirname(__file__), "locale")
    load_gettext_translations(local_path, "tornado")
    trans1 = _translations["en_US"](
        "Tornado is a Python web framework and asynchronous networking library.")
    trans2 = _translations["zh_CN"]("Tornado is a Python web framework and asynchronous networking library.")
    assert trans1 == "Tornado is a Python web framework and asynchronous networking library."
    assert trans2 == "Tornado 是一个 Python 的 Web 框架和异步网络库。"

_date_format_cache = {}  # type: Dict[str, Any]



# Generated at 2022-06-14 12:16:42.262876
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations("/tmp/tornado_locale", "tornado")



# Generated at 2022-06-14 12:16:45.912170
# Unit test for function load_gettext_translations
def test_load_gettext_translations():

    load_gettext_translations("locale","my_proj")
    global _translations
    global _supported_locales
    global _use_gettext
    assert(_use_gettext)
    assert(_translations)
    assert(_supported_locales)
    

# Generated at 2022-06-14 12:16:50.623956
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    assert Locale('fa_IR').format_date(datetime.datetime(2020,9,30), 0, False, False) == 'سپتامبر 30, 2020 در 00:00'
    assert Locale('fa').format_date(datetime.datetime(2020,9,30), 0, False, False) == 'سپتامبر 30, 2020 در 00:00'
    assert Locale('fa_42').format_date(datetime.datetime(2020,9,30), 0, False, False) == 'سپتامبر 30, 2020 در 00:00'
    assert Locale('fa_IR').format_date(datetime.datetime(2020,9,30), 0, False, True) == 'سپتامبر 30, 2020'

# Generated at 2022-06-14 12:16:54.794578
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale("en").friendly_number(1000) == "1,000"
    assert Locale("en").friendly_number(1001) == "1,001"
    assert Locale("en").friendly_number(1) == "1"
    assert Locale("en").friendly_number(0) == "0"
    assert Locale("en").friendly_number(10000) == "10,000"
    assert Locale("en").friendly_number(1111111) == "1,111,111"




# Generated at 2022-06-14 12:16:57.629184
# Unit test for function load_translations
def test_load_translations():
    set_default_locale("fr_FR")
    load_translations("/Users/alex/Documents/Projets/tornado/locale")
    print(_translations)


# Generated at 2022-06-14 12:17:00.980372
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    assert GettextLocale.pgettext('pgettext', 'pgettext') == 'pgettext'

# Generated at 2022-06-14 12:17:04.612210
# Unit test for function load_translations
def test_load_translations():
    directory = "./"
    encoding = None
    load_translations(directory, encoding)
    print(_supported_locales)
    print(list(_translations.keys()))



# Generated at 2022-06-14 12:17:55.933816
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import datetime
    from zulip_bots.zulip_bots.bots.converter.lib.timezone import GMT
    """
    This function tests if format_date of Locale class behaves correctly
    """
    gmt = GMT()
    gmt_offset_pst = -8 * 60
    gmt_offset_utc = 0
    gmt_time = datetime.datetime.utcnow()
    pst_time = gmt.fromutc(gmt_time, gmt_offset_pst)
    utc_time = gmt.fromutc(gmt_time, gmt_offset_utc)


# Generated at 2022-06-14 12:18:09.349170
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    from typing import Dict
    """
    The following unit test verifies that the friendly_number method of the
    Locale class will return the correct string for the following cases:
    1.  The value is not an integer
    2.  The value does not have a comma
    3.  The value has one comma
    4.  The value has many commas
    """
    # Test method in a dict along with the expected output

# Generated at 2022-06-14 12:18:10.090769
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    pass

# Generated at 2022-06-14 12:18:13.637751
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import doctest
    doctest.run_docstring_examples(load_gettext_translations, globals(), verbose=True)

# -------------------------------------------------------------------------------------------------
# Class Locale
# -------------------------------------------------------------------------------------------------



# Generated at 2022-06-14 12:18:15.633063
# Unit test for function load_translations
def test_load_translations():
    load_translations("i18n/locale")
    LOCALE_NAMES.update(_translations)



# Generated at 2022-06-14 12:18:22.834106
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    _Locale_obj = Locale.get("en_US")
    assert _Locale_obj.friendly_number(value=1000) == "1,000"
    _Locale_obj = Locale.get("en")
    assert _Locale_obj.friendly_number(value=1000) == "1,000"
    _Locale_obj = Locale.get("en_UK")
    assert _Locale_obj.friendly_number(value=1000) == "1000"
    return



# Generated at 2022-06-14 12:18:27.258682
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    directory = '/home/tuhuynh/envs/tornado/lib/python3.6/site-packages/tornado/_locale_data/locale'
    domain ='tornado'
    test = load_gettext_translations(directory,domain )
    assert type(test) == None


# Generated at 2022-06-14 12:18:29.368812
# Unit test for function load_translations
def test_load_translations():
    assert _translations == {}
    assert _supported_locales == frozenset([_default_locale])
    load_translations("/")

# Generated at 2022-06-14 12:18:41.542258
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    def format_date(locale_code, date, gmt_offset):
        """Test date format for a given locale.
        """
        loc = Locale.get(locale_code)
        return loc.format_date(date=date, gmt_offset=gmt_offset)

    # Current time is 2019-07-22 12:26:00+00:00
    # See https://stackoverflow.com/a/13694166/1405289
    class UTCDateTime(datetime.tzinfo):
        def utcoffset(self, dt):
            return datetime.timedelta(0)

        def tzname(self, dt):
            return "UTC"

        def dst(self, dt):
            return datetime.timedelta(0)

    utc_date_time = datetime

# Generated at 2022-06-14 12:18:51.204758
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get('en').friendly_number(1) == '1'
    assert Locale.get('en').friendly_number(10) == '10'
    assert Locale.get('en').friendly_number(100) == '100'
    assert Locale.get('en').friendly_number(1000) == '1,000'
    assert Locale.get('en').friendly_number(10000) == '10,000'
    assert Locale.get('en').friendly_number(100000) == '100,000'
    assert Locale.get('en').friendly_number(1000000) == '1,000,000'
    assert Locale.get('en').friendly_number(10000000) == '10,000,000'

# Generated at 2022-06-14 12:19:30.532159
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # Parameter default values
    gmt_offset = 0
    dow = True
    
    for locale, date_instance in locale_date_tuples:
        locale = Locale.get(locale)
        result = locale.format_day(date_instance, gmt_offset, dow)
        make_assertion_and_print(result, date_instance, locale.code)
# Tests method format_day of class Locale
test_Locale_format_day()

# Unit tests for method format_date of class Locale

# Generated at 2022-06-14 12:19:41.292339
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get("en").friendly_number(1000) == "1,000"
    assert Locale.get("en").friendly_number(1299) == "1,299"
    assert Locale.get("en").friendly_number(2320) == "2,320"
    assert Locale.get("en").friendly_number(2000000) == "2,000,000"
    assert Locale.get("en").friendly_number(2000059) == "2,000,059"
    assert Locale.get("en_US").friendly_number(1000) == "1,000"
    assert Locale.get("en_US").friendly_number(1299) == "1,299"
    assert Locale.get("en_US").friendly_number(2320) == "2,320"
    assert Locale.get

# Generated at 2022-06-14 12:19:42.517831
# Unit test for function load_translations
def test_load_translations():
    load_translations('translations')

# Test the jinja2 filter

# Generated at 2022-06-14 12:19:50.599513
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import sys
    from os.path import dirname as parentdir
    sys.path.insert(0, parentdir(parentdir(parentdir(__file__))))
    from webapp.apps.hello.translations import load_translations
    load_translations(parentdir(__file__))
    locale = Locale.get("fa")
    date = datetime.datetime.utcnow()
    date += datetime.timedelta(seconds=25)
    print(locale.format_date(date))
    date += datetime.timedelta(minutes=25)
    print(locale.format_date(date))
    date += datetime.timedelta(hours=25)
    print(locale.format_date(date))
    date += datetime.timedelta(days=25)

# Generated at 2022-06-14 12:19:59.985951
# Unit test for function load_translations
def test_load_translations():
    set_default_locale("zh")
    load_translations("internal/cloud/src/tornado/locale")
    assert _default_locale == 'zh'
    assert _translations['zh']['unknown']['%(name)s liked this'] == '%(name)s 喜欢这个'
    assert _translations['zh']['singular']['%(name)s liked this'] == '%(name)s 喜欢这个'
    assert _translations['zh']['plural']['%(name)s liked this'] == '%(name)s 喜欢这个'
    assert _supported_locales == frozenset(['zh', 'en_US'])



# Generated at 2022-06-14 12:20:01.951615
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert load_gettext_translations('/home/thongpb/Documents/DjangoTest/tornado/translations', 'messages')



# Generated at 2022-06-14 12:20:03.200531
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations("../data/locale", "test")

# Generated at 2022-06-14 12:20:10.890691
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # Setup
    locale = Locale("en")
    context = "context"
    message = "message"
    plural_message = "plural_message"
    count = 1
    # Exercise
    result = locale.pgettext(context, message, plural_message, count)
    # Verify
    assert result == "message", "Expected \"message\" but got {0} instead".format(
        result
    )



# Generated at 2022-06-14 12:20:18.122832
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    with MainLoop(make_options=None) as loop:
        # 测试时间格式
        def t(locale_code, timestamp_or_datetime, gmt_offset=0, relative=True,
            shorter=False, full_format=False):
            locale = Locale.get(locale_code)
            str_date = locale.format_date(timestamp_or_datetime,
                gmt_offset, relative, shorter, full_format)
            # print(lo

# Generated at 2022-06-14 12:20:23.900837
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    test_cases = [
        (0, "0"),
        (1, "1"),
        (177, "177"),
        (1234, "1,234"),
        (123456, "123,456"),
        (123456789, "123,456,789"),
        ]
    for v, r in test_cases:
        assert Locale("en").friendly_number(v) == r
        assert Locale("en_US").friendly_number(v) == r
        assert Locale("fr").friendly_number(v) == str(v)



# Generated at 2022-06-14 12:20:42.310589
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale.get("en_US")
    if locale.friendly_number(1000) != "1,000":
        raise ValueError("Wrong comma seperation")
    
    

# Generated at 2022-06-14 12:20:52.425172
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    from datetime import datetime
    from pytz import timezone
    from datetime import timedelta
    
    gmt13_tz = timezone('Asia/Kuala_Lumpur')
    gmt2_tz = timezone('Etc/GMT+2')
    gmt_tz = timezone('Etc/UTC')
    gmt3_tz = timezone('Etc/GMT+3')
    ams_tz = timezone('Europe/Amsterdam')
    
    now = datetime.now(gmt13_tz)
    
    # Case 1
    # current time in KL
    dt = datetime.now(gmt13_tz)
    locale = Locale.get('en')
    result = locale.format_date(dt, 13, True)
    expected = 'now'

# Generated at 2022-06-14 12:21:03.045659
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    tests = [
        (0, "0"),
        (1, "1"),
        (10, "10"),
        (100, "100"),
        (999, "999"),
        (1000, "1,000"),
        (1001, "1,001"),
        (9999, "9,999"),
        (10000, "10,000"),
        (10001, "10,001"),
        (10101, "10,101"),
        (1010101, "1,010,101"),
        (101010100, "101,010,100"),
        (1000000000, "1,000,000,000"),
        (1000000001, "1,000,000,001"),
    ]

    for value, expected in tests:
        assert Locale.get("en_US").friendly_number(value) == expected


# Generated at 2022-06-14 12:21:14.384931
# Unit test for function load_translations
def test_load_translations():
    import tornado.testing
    import tornado.web
    app = tornado.web.Application()
    # there is no English translation, so this should make a missing
    # string error when we try to run the app:
    app.add_handlers(
        r".*",
        [tornado.web.url("/", MainHandler, name="main")],
    )
    request = tornado.testing.AsyncHTTPTestCase.fetch(
        app.get_request("/"),
        raise_error=False,
    )
    assert request.code == 500
    tornado.locale.load_translations("tests/locale_data")
    request = tornado.testing.AsyncHTTPTestCase.fetch(
        app.get_request("/"),
        raise_error=False,
    )
    assert request.code == 200

# Generated at 2022-06-14 12:21:17.118485
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    assert(Locale("de").format_date(0) == "01.01.1970 um 01:00")
    assert(Locale("de").format_date(1527865227) == "03.06.2018 um 14:27")

# Generated at 2022-06-14 12:21:27.059023
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale.get('en_US').format_day(datetime.datetime(2020, 5, 15), 0, True) == "Friday, May 15"
    assert Locale.get('en_US').format_day(datetime.datetime(2020, 5, 15), 0, False) == "May 15"
    assert Locale.get('fa_IR').format_day(datetime.datetime(2020, 5, 15), 0, True) == "جمعه، 2 مرداد 1399"
    assert Locale.get('fa_IR').format_day(datetime.datetime(2020, 5, 15), 0, False) == "2 مرداد 1399"

# Generated at 2022-06-14 12:21:35.950836
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # no relative
    now = datetime.datetime.utcnow()
    # test timestamp
    ts = now.timestamp()
    assert Locale.get("en").format_date(ts, relative = False) == now.strftime("%B %d, %Y at %I:%M %p")
    assert Locale.get("en").format_date(now, relative = False) == now.strftime("%B %d, %Y at %I:%M %p")
    # test relative

# Generated at 2022-06-14 12:21:44.135515
# Unit test for function load_translations
def test_load_translations():
    set_default_locale("es_LA")
    assert _default_locale == "es_LA"
    assert list(_translations.keys()) == []
    assert _supported_locales == frozenset(["es_LA"])
    load_translations("C:/Users/Sahba/Desktop/Veracitor/tornado-5.0.2/tornado/locale")
    assert _translations["es_LA"]["unknown"]["Error"] == "Error"



# Generated at 2022-06-14 12:21:52.196977
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    from .constants import LOCALE_NAMES
    from .i18n import _translations, _default_locale
    from .i18n import load_gettext_translations
    from .i18n import load_translations
    from .i18n import Locale
    from .i18n import get_closest_locale, get_locale
    from .i18n import set_supported_locales, supported_locales
    from .i18n import set_translations, translate

    # Arrange
    directory = '/home/mbarbu/dev/zulip/locale'
    domain = 'messages'

    # Act
    Locale.load_gettext_translations(directory, domain)

    # Assert
    assert _translations != {}

    # reset everything
    _translations = {}


# Generated at 2022-06-14 12:21:54.600647
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    dir='./'
    domain='gettext'
    load_gettext_translations(dir,domain)



# Generated at 2022-06-14 12:22:28.048380
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # pgettext is not implemented on base class, this should throw an error
    
    try:
        Locale.get("fa_IR").pgettext("context", "text")
    except NotImplementedError:
        print("not implemented")
    else:
        raise Exception("expected NotImplementedError")

test_Locale_pgettext()


# Generated at 2022-06-14 12:22:33.272983
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    response = _translation.pgettext('context', 'Test')
    assert response == 'عنوان تست'
    response = _translation.pgettext('context', 'Test', count=2)
    assert response == 'عنوان تست'
    response = _translation.pgettext('context', 'Test', context='routing')
    assert response == 'عنوان تست'
    

# Generated at 2022-06-14 12:22:34.514355
# Unit test for function load_translations
def test_load_translations():
    load_translations("/Users/lixingyu/Desktop/Python/tornado-5.1.1/tornado/locale/_translations")



# Generated at 2022-06-14 12:22:46.728734
# Unit test for function load_translations
def test_load_translations():
    load_translations('../translations')
    assert _translations['vi']
    assert _translations['vi']["plural"]["%(list)s is online"] == "%(list)s đang tham gia"
    assert _translations['vi']["plural"]["%(list)s and %(another)s are online"] == "%(list)s và %(another)s đang trực tuyến"
    assert _translations['vi']["plural"]["%(name)s liked this"] == "%(name)s thích điều này"

# Generated at 2022-06-14 12:22:52.847988
# Unit test for function load_translations
def test_load_translations():
    set_default_locale('en_US')
    assert _default_locale == 'en_US'
    load_translations('/home/lievendoclo/PycharmProjects/Tornado_Server/tornado/locale/data')
    assert _translations == {'en_US': {}}
    assert _supported_locales == frozenset(['en_US'])


# Generated at 2022-06-14 12:22:54.208125
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations("../", "messages")



# Generated at 2022-06-14 12:23:04.798789
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    l = Locale('pt_BR')
    assert l.code == "pt_BR"
    assert l.format_date(datetime.datetime.now()) == "hoje"
    assert l.format_date(datetime.datetime.now() - datetime.timedelta(hours=1, minutes=1), gmt_offset=1) == "1 hora, 1 minuto atrás"
    assert l.format_date(datetime.datetime.now() - datetime.timedelta(hours=23, minutes=59, seconds=59), gmt_offset=1) == "hoje"
    assert l.format_date(datetime.datetime.now() + datetime.timedelta(hours=23, minutes=59, seconds=59), gmt_offset=1) == "hoje"
    assert l

# Generated at 2022-06-14 12:23:15.815953
# Unit test for function load_translations
def test_load_translations():
    """
    This is the unit test for the load_translation function.
    """
    import random
    import shutil
    import tempfile
    import csv
    import os

    # Create a temporary directory
    test_dir = tempfile.mkdtemp(prefix="tornado_test_locale_")
    csv_path = os.path.join(test_dir, "en_US.csv")
    csv_file = open(csv_path, 'w', encoding="utf-8")
    test_string = '"I love you","Te amo"'
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow([test_string])
    load_translations(test_dir)
    locale = _translations.get("en_US", None)
   

# Generated at 2022-06-14 12:23:26.823626
# Unit test for method friendly_number of class Locale

# Generated at 2022-06-14 12:23:30.693047
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    l = CSVLocale("en", translations={
            "unknown": {"a": "b"}
        })
    assert l.translate("c") == "c"
    assert l.translate("a") == "b"
    l = CSVLocale("en", translations={
            "plural": {"a": "b"},
            "singular": {"a": "c"}
        })
    assert l.translate("c") == "c"
    assert l.translate("a", "" , 1) == "c"
    assert l.translate("a", "" , 2) == "b"
test_CSVLocale_translate()



# Generated at 2022-06-14 12:24:33.139839
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    class Translations(object):
        def ugettext(self, message):
            return message

        def ungettext(self, singular, plural, n):
            return singular

        def upgettext(self, context, singular):
            return singular

        def upgettext_lazy(self, context, singular):
            return singular

        def ungettext_lazy(self, singular, plural, n):
            return singular

        def ugettext_lazy(self, message):
            return message

    def _test_gettext(locale, context, msgid, plural=None, n=None):
        # type: (Locale, str, str, Optional[str], Optional[int]) -> str
        return locale.pgettext(context, msgid, plural, n)


# Generated at 2022-06-14 12:24:43.698343
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    import unittest
    class test_locale(unittest.TestCase):
        def test_single_digit(self):
            self.assertEqual(Locale.get('').friendly_number(1), '1')
        def test_double_digit(self):
            self.assertEqual(Locale.get('').friendly_number(10), '10')
        def test_three_digits(self):
            self.assertEqual(Locale.get('').friendly_number(100), '100')
        def test_four_digits(self):
            self.assertEqual(Locale.get('').friendly_number(1000), '1,000')

# Generated at 2022-06-14 12:24:51.023046
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    test_cases = [
        (datetime.datetime(2019, 11, 9), "Saturday, November 9"),
        (datetime.datetime(2019, 11, 9), "Saturday, November 9", True),
        (datetime.datetime(2019, 11, 9), "November 9", False)
    ]

    for test_case in test_cases:
        assert Locale.get("en_US").format_day(test_case[0], dow=test_case[2]) == test_case[1]

# Generated at 2022-06-14 12:24:57.208266
# Unit test for function load_translations
def test_load_translations():
    import os
    import json
    import tempfile

    _translations = {}

    def _check_translation(expected_translation, actual_translation):
        assert sorted(expected_translation) == sorted(actual_translation)
        for key in expected_translation:
            assert expected_translation[key] == actual_translation[key]

    # create temp directory
    temp_dir = tempfile.mkdtemp()

    # create temp file of locale data
    temp_file = tempfile.NamedTemporaryFile(mode='w', dir=temp_dir, delete=False)

# Generated at 2022-06-14 12:24:58.855060
# Unit test for function load_translations
def test_load_translations():
    directory = "./locale/"
    locale = "en_US"
    encoding = "utf-8"
    load_translations(directory, encoding)



# Generated at 2022-06-14 12:25:07.068303
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # Test with simple string
    L = Locale.get("en")
    date = datetime.datetime(2017, 12, 4, 17, 34, 0)
    date_str = L.format_date(date, gmt_offset=0, relative=True, shorter=False, full_format=False)
    assert date_str == "December 4, 2017, at 12:34 pm"
    date_str = L.format_date(date, gmt_offset=0, relative=False, shorter=False, full_format=False)
    assert date_str == "December 4, 2017, at 12:34 pm"
    date_str = L.format_date(date, gmt_offset=0, relative=True, shorter=True, full_format=False)
    assert date_str == "December 4, 2017"
    date_

# Generated at 2022-06-14 12:25:17.664332
# Unit test for function load_translations
def test_load_translations():
    from tornado import testing
    import os
    import shutil
    from tornado.testing import AsyncTestCase, gen_test
    class TestLoadTranslations(AsyncTestCase):
        def setUp(self):
            self.path = os.path.dirname(__file__) + '/translations'
            self.locales_path = os.path.join(self.path, 'locales')
            #if os.path.isdir(self.path):
            #    shutil.rmtree(self.path)
            #os.mkdir(self.path)
            #os.mkdir(self.locales_path)
            #with open(os.path.join(self.locales_path, 'es_LA.csv'), 'wb') as f:
            #    f.write(tornado.escape.utf8(

# Generated at 2022-06-14 12:25:27.880523
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # Test if it works with datetime objects
    now = datetime.datetime.now()
    assert Locale.get("en").format_date(now) == \
        Locale.get("en").format_date(time.mktime(now.timetuple()))
    assert Locale.get("en").format_date(now) == \
        Locale.get("en").format_date(now.timestamp())
    # Test if it works with date string
    date = '1988-10-15'
    assert Locale.get("en").format_date(date) == \
        Locale.get("en").format_date(time.mktime(time.strptime(date, '%Y-%m-%d')))
    assert Locale.get("en").format_date(date) == \
        Locale

# Generated at 2022-06-14 12:25:36.027559
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # create set of mocked assertions
    mock_code = "en"
    mock_name = "Localized name"
    mock_rtl = True
    mock_months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    mock_weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    mock_context = "mock_context"
    mock_message = "mock_message"
    mock_plural_message = "mock_plural_message"