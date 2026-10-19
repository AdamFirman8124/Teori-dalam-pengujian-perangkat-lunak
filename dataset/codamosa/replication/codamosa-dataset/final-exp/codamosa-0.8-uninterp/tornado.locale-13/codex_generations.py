

# Generated at 2022-06-14 12:16:12.303854
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert '1,234' == Locale.get('en').friendly_number(1234)
    assert '234' == Locale.get('en').friendly_number(234)
    assert '23' == Locale.get('en').friendly_number(23)



# Generated at 2022-06-14 12:16:22.427431
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    # Test for basic case
    test_locale = GettextLocale('en', None)
    test_result = test_locale.pgettext('law', 'right')
    assert test_result == 'right',\
    'pgettext is missing the basic case of one message'
    # Test for plural message case
    test_result = test_locale.pgettext('sticks', 'stick', 'sticks', 5)
    assert test_result == 'sticks',\
    'pgettext is missing the plural message case of two messages'
    # Test for the case that pgettext will fall back to normal gettext
    test_result = test_locale.pgettext('organization', 'club', 'clubs', 5)

# Generated at 2022-06-14 12:16:28.027875
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import tempfile
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.escape import utf8
    basedir = tempfile.mkdtemp()
    # Step 1: generate POT file
    pot = b"""
    #: test.py:1
    msgid "Hello, world!"
    msgstr ""
    """
    open(os.path.join(basedir, "messages.pot"), "wb").write(pot)
    # Step 2: Generate MO file

# Generated at 2022-06-14 12:16:28.930768
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    pass


# Generated at 2022-06-14 12:16:32.631081
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # test1
    now = datetime.datetime.utcnow()
    now2 = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    later = datetime.datetime.utcnow() + datetime.timedelta(hours=25,minutes=1)
    assert now == now2
    # test2
    sign = now < later
    assert sign
    # test3
    sign = later >= now
    assert sign


# Generated at 2022-06-14 12:16:35.317735
# Unit test for function load_translations
def test_load_translations():
    directory = 'locale'
    encoding = 'utf-8'
    load_translations(directory,encoding)
    print(_supported_locales)
    print(_translations)


# Generated at 2022-06-14 12:16:38.446302
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    test_format_date(Locale("en"), 0)
    test_format_date(Locale("pt_BR"), -60)
    test_format_date(Locale("zh_CN"), 360)


# Generated at 2022-06-14 12:16:49.806383
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    load_translations(
        os.path.join(os.path.dirname(__file__), "..", "..", "translations")
    )
    zh_CN = Locale("zh-CN")
    now = time.time()
    assert zh_CN.format_date(now) == "1 秒前"
    assert zh_CN.format_date(now - 50) == "1 秒前"
    assert zh_CN.format_date(now - 50.1) == "1 分钟前"
    assert zh_CN.format_date(now - 9 * 60) == "9 分钟前"
    assert zh_CN.format_date(now - 15 * 60) == "15 分钟前"


# Generated at 2022-06-14 12:16:59.938704
# Unit test for function load_translations
def test_load_translations():
    global _translations

    _translations = {}

    full_path = "./locale/zh_CN.csv"
    encoding = "utf-8-sig"
    with open(full_path, encoding=encoding) as f:
        _translations['zh_CN'] = {}
        for i, row in enumerate(csv.reader(f)):
            if not row or len(row) < 2:
                continue
            row = [escape.to_unicode(c).strip() for c in row]
            english, translation = row[:2]
            if len(row) > 2:
                plural = row[2] or "unknown"
            else:
                plural = "unknown"

# Generated at 2022-06-14 12:17:10.503220
# Unit test for function load_translations
def test_load_translations():
    import pytest
    from io import StringIO
    from os import path
    from tempfile import mkdtemp
    encoding = 'utf-8'
    dirpath = mkdtemp(suffix='_test')
    csvpath = path.join(dirpath, 'es_LA.csv')
    csvfile = StringIO()
    csvfile.write(
        '"I love you","Te amo"\n'
        '"%(name)s liked this","A %(name)s le gusto esto","singular"\n'
        '"%(name)s liked this","A %(name)s les gusto esto","plural"\n'
        '"Hello!","Hola!"\n'
        )
    csvfile.seek(0)

# Generated at 2022-06-14 12:17:34.506076
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert load_gettext_translations(
        directory = "/Users/wangyiming/Desktop/xgettext",
        domain = "test_domain"
    ) == None


# Generated at 2022-06-14 12:17:37.500984
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    l = Locale.get("de_DE")
    print(l.format_date(datetime.datetime.now()))

test_Locale_format_date()


# Generated at 2022-06-14 12:17:39.380226
# Unit test for function load_translations
def test_load_translations():
    return load_translations('test_data')
# EOF function test_load_translations



# Generated at 2022-06-14 12:17:45.408996
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    locale = Locale.get('en')
    date = datetime.datetime(2016, 12, 1, 10, 0, 0)
    result = locale.format_date(date)
    print(result)
    result = locale.format_date(date, relative = False)
    print(result)

test_Locale_format_date()


# Generated at 2022-06-14 12:17:50.647753
# Unit test for function load_translations
def test_load_translations():
    try:
        load_translations("../locale")
    except FileNotFoundError:
        gen_log.info(
            "Unable to test load_translations, no file to test it with.")
    except Exception as e:
        gen_log.error("Test failed: load_translations")
        raise e



# Generated at 2022-06-14 12:18:00.033165
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    import pytest
    locale = Locale("en", "")
    local_date = datetime.datetime.utcnow()
    dow = locale.format_day(local_date, gmt_offset=0, dow=True)
    assert dow[:len(locale._weekdays[local_date.weekday()])] == locale._weekdays[local_date.weekday()]
    assert dow[-8:] == "%s %s" % (locale._months[local_date.month - 1], str(local_date.day))
    with pytest.raises(Exception):
        dow = locale.format_day(local_date, gmt_offset=10, dow=True)
    dow = locale.format_day(local_date, gmt_offset=0, dow=False)
    assert dow[-3:]

# Generated at 2022-06-14 12:18:01.110504
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    set_up_function()
    load_gettext_translations('/home/vagrant/tornado/tornado/locale/', 'tornado')
    test_get()


# Generated at 2022-06-14 12:18:13.691766
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale1 = Locale.get("en")
    assert locale1.friendly_number(0) == "0"
    assert locale1.friendly_number(1) == "1"
    assert locale1.friendly_number(2) == "2"
    assert locale1.friendly_number(10) == "10"
    assert locale1.friendly_number(100) == "100"
    assert locale1.friendly_number(1000) == "1,000"
    assert locale1.friendly_number(10000) == "10,000"
    assert locale1.friendly_number(100000) == "100,000"
    assert locale1.friendly_number(1000000) == "1,000,000"
    assert locale1.friendly_number(10000000) == "10,000,000"

# Generated at 2022-06-14 12:18:24.851481
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    test_date = datetime.datetime(2019, 1, 1, 0, 0)
    # print("{}".format(test_date))
    locale = Locale.get("en")
    assert locale._months[test_date.month-1] == "January"
    assert locale._weekdays[test_date.weekday()] == "Tuesday"
    assert locale.format_day(test_date) == "Tuesday, January 1"
    assert locale.format_day(test_date, dow=False) == "January 1"
    locale = Locale.get("zh_CN")
    assert locale._months[test_date.month-1] == u"\u4e00\u6708"

# Generated at 2022-06-14 12:18:25.229906
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    pass



# Generated at 2022-06-14 12:19:12.867853
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # check format() function
    # set timezone to japan
    os.environ["TZ"] = "Asia/Tokyo"
    time.tzset()
    cur_time = datetime.datetime.now()
    ja_locale = Locale.get("ja")
    assert ja_locale.format_day(cur_time, dow=True) == '月曜日, {} {}'.format(ja_locale._months[cur_time.month - 1], cur_time.day)
    assert ja_locale.format_day(cur_time, dow=False) == '{} {}'.format(ja_locale._months[cur_time.month - 1], cur_time.day)
    # set timezone to US
    os.environ["TZ"] = "America/New_York"


# Generated at 2022-06-14 12:19:26.019170
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    from datetime import datetime
    from base64 import b64encode
    from hashlib import sha1
    from hashlib import sha3_256

    def sha1_digest(s):
        return b64encode(sha1(s.encode()).digest()).decode()

    def sha3_digest(s):
        return b64encode(sha3_256(s.encode()).digest()).decode()

    import pytz
    utc = pytz.utc

    def utc_from(date):
        return utc.localize(date)

    def gmt_from(date):
        return date.replace(tzinfo=utc)

    def test(locale, date, gmt_offset, relative, full_format, expected):
        locale = Locale

# Generated at 2022-06-14 12:19:34.162403
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get("en")
    now = datetime.datetime.utcnow()
    gmt_offset = 4
    date1 = now - datetime.timedelta(minutes=gmt_offset)
    assert locale.format_day(date1, gmt_offset, dow=True) == 'Today, %s %d'%(locale._months[date1.month-1],date1.day)    
    date2 = now - datetime.timedelta(minutes=gmt_offset,hours=90)
    assert locale.format_day(date2, gmt_offset, dow=True) == '%s, %s %d'%(locale._weekdays[date2.weekday()],locale._months[date2.month-1],date2.day)
    date3 = now

# Generated at 2022-06-14 12:19:44.965892
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    def get_translate_function(msg_list):
        def translate_function(message, plural_message=None, count=None):
            if message not in msg_list:
                return 'msg not in list'
            return msg_list[message]
        return translate_function

    from unittest.mock import Mock

    # test if message not in msg_list
    mock_translate_function = Mock(side_effect=get_translate_function({'A':'B'}))
    locale = Locale(code='EN')
    locale.translate = mock_translate_function
    assert locale.pgettext('C', 'X') == 'msg not in list'

    # test if message in msg_list

# Generated at 2022-06-14 12:19:56.030383
# Unit test for function load_translations
def test_load_translations():
    class Test:
        def __init__(self):
            self.log = []
            self.file_path = ""
    test = Test()

    test_data_file = os.path.join(os.path.dirname(__file__), 'test_data_file')
    test.file_path = os.path.join(test_data_file, 'en_US.csv')
    load_translations(test_data_file)
    # check the translation of "I love you"
    en_us = get("en_US")
    assert en_us.translate("I love you") == "I love you"
    en_ca = get("en_CA")
    assert en_ca.translate("I love you") == "I love you"
    es_la = get("es_LA")
    assert es

# Generated at 2022-06-14 12:20:06.107336
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import tornado.testing
    import tornado.web
    import tornado.ioloop
    import os
    import gettext

    class TestHandler(tornado.web.RequestHandler):
        def get(self):
            return self.write(self.locale.translate('This is a test'))

    class TestTornadoLocale(tornado.testing.AsyncHTTPTestCase):
        def get_app(self):
            return tornado.web.Application([(r'/', TestHandler)])


# Generated at 2022-06-14 12:20:09.069947
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    devs = []
    devs.append(UnitTestDev('locale_class', "test_Locale_format_day", "get", True))
    return devs


# Generated at 2022-06-14 12:20:20.167352
# Unit test for function load_translations
def test_load_translations():
    load_translations("./locale")

#def load_translations(directory):
#    """Loads translations from CSV files in a directory.
#
#    Translations are strings with optional Python-style named placeholders
#    (e.g., ``My name is %(name)s``) and their associated translations.
#
#    The directory should have translation files of the form ``LOCALE.csv``,
#    e.g. ``es_GT.csv``. The CSV files should have two or three columns: string,
#    translation, and an optional plural indicator. Plural indicators should
#    be one of "plural" or "singular". A given string can have both singular
#    and plural forms. For example ``%(name)s liked this`` may have a
#    different verb conjugation depending on whether %(name)s

# Generated at 2022-06-14 12:20:28.217042
# Unit test for function load_translations
def test_load_translations():
    root_folder = os.path.abspath(os.path.dirname(__file__))
    test_dir_path = os.path.join(root_folder,'tornado/test/locale/')
    test_file_name = 'zh_CN.csv'
    load_translations(test_dir_path)
    #print(list(_translations.keys()))
    #print(_translations['zh_CN'])

# Generated at 2022-06-14 12:20:29.640721
# Unit test for function load_translations
def test_load_translations():
    directory = "./data"
    load_translations(directory)


# Generated at 2022-06-14 12:21:47.357022
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # Assume that the zh_CN dictionary contains 'hi' with translation '哈哈'
    # and 'bye' with context and translation '再见', '再见，世界' respectively
    pass

# Generated at 2022-06-14 12:21:48.841975
# Unit test for function load_translations
def test_load_translations():
    load_translations("/Users/saurabh/Desktop/Tornado")


# Generated at 2022-06-14 12:22:01.575210
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    global _translations
    global _supported_locales
    global _use_gettext
    # Setup
    _translations = {}
    _supported_locales = {}
    _use_gettext = False
    directory = "/usr/share/locale"
    domain = "tornado"
    for lang in os.listdir(directory):
        if lang.startswith("."):
            continue  # skip .svn, etc
        if os.path.isfile(os.path.join(directory, lang)):
            continue
        try:
            os.stat(os.path.join(directory, lang, "LC_MESSAGES", domain + ".mo"))
            _translations[lang] = gettext.translation(
                domain, directory, languages=[lang]
            )
        except Exception as e:
            gen_

# Generated at 2022-06-14 12:22:03.317812
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    now = datetime.datetime.utcnow()
    format=locale_module.Locale.get("en").format_day(now)
    assert format==now.strftime("%A, %B %d")

# Generated at 2022-06-14 12:22:15.800939
# Unit test for function load_translations
def test_load_translations():
    import tornado.locale
    from tornado.locale import load_translations
    from tornado._locale_data import LOCALE_NAMES

    tornado.locale.LOCALE_NAMES = {'en_US': 'English (United States)',
                                   'zh_CN': 'Chinese (China)',
                                   'es_ES': 'Spanish (Spain)',
                                   'fr_FR': 'French (France)',
                                   'de_DE': 'German (Germany)',
                                   'ja_JP': 'Japanese (Japan)',
                                   'ko_KR': 'Korean (Korea)',
                                   'zh_TW': 'Chinese (Taiwan)'}

    # TODO(julienr): Avoid using __file__ in tests and provide a get_datadir
    # function.

# Generated at 2022-06-14 12:22:28.050081
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from tornado_yarl import Locale
    import datetime
    # Test for a time zone in the same time zone as the local time zone
    a = datetime.datetime(2018, 5, 10, 17, 00)
    print(Locale.get("en-US").format_day(a))
    print(Locale.get("en-GB").format_day(a))
    print(Locale.get("fr-FR").format_day(a))
    print(Locale.get("zh-CN").format_day(a))
    print(Locale.get("fa-FA").format_day(a))
    # Test for a time zone in a different time zone than the local time zone
    print(Locale.get("en-US").format_day(a, 330))

# Generated at 2022-06-14 12:22:39.316206
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """
        Test the Locale.format_day method
    """
    # Test the format of the date
    load_translations("LOCALE_DATA_DIR")
    print(Locale.get_closest("en_US").format_day(datetime.datetime.strptime("01-04-1989", "%m-%d-%Y"), dow=True))
    print(Locale.get_closest("fr_FR").format_day(datetime.datetime.strptime("01-04-1989", "%m-%d-%Y"), dow=True))
    print(Locale.get_closest("de_DE").format_day(datetime.datetime.strptime("01-04-1989", "%m-%d-%Y"), dow=True))

# Generated at 2022-06-14 12:22:46.328039
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    test_locale = GettextLocale('en', None)
    assert test_locale.pgettext("law", "right") is 'right'
    assert test_locale.pgettext("good", "right") is 'right'
    assert test_locale.pgettext("organization", "club", "clubs", len(1)) is 'club'
    assert test_locale.pgettext("stick", "club", "clubs", len(1)) is 'club'



# Generated at 2022-06-14 12:22:54.265478
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    print("Method format_day of class Locale:")
    # Use a date of 2019-03-21 because in this case, the default locale is 'en'
    date = datetime.datetime(2019, 3, 21)
    gmt_offset = 0
    dow = True
    for code in get_supported_locales():
        locale = Locale.get(code)
        day_string = locale.format_day(date, gmt_offset, dow)
        print(f"    code: {code}, day_string: {day_string}")

# Generated at 2022-06-14 12:22:56.359401
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    if __name__ == "__main__":
        import doctest
        doctest.testmod()

