

# Generated at 2022-06-14 12:16:12.941659
# Unit test for function load_translations
def test_load_translations():
    load_translations('./translations')
    # print(_translations)
    '''
    {'en_US': {'unknown': {'Test string': 'Test string'}}, 'fr_FR': {'unknown': {'Test string': 'Chaîne de test'}}, 'de_DE': {'unknown': {'Test string': 'Testzeichenkette'}}, 'es_ES': {'unknown': {'Test string': 'Cadena de prueba'}}, 'it_IT': {'unknown': {'Test string': 'Stringa di prova'}}}

    '''
    # print(_supported_locales)
    '''
    frozenset({'en_US', 'fr_FR', 'it_IT', 'es_ES', 'de_DE'})

    '''
    set_default_

# Generated at 2022-06-14 12:16:19.702792
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # Create a datetime object and a Locale object
    test_date = datetime.datetime(2018, 2, 14, 14, 37)
    test_local = Locale.get('en')
    test_local_tow = Locale.get('en')
    # Test for case of True, should return 'Wednesday, February 14'
    # and test for case of False, should return 'February 14'
    assert test_local.format_day(test_date, gmt_offset=6, dow=True) == 'Wednesday, February 14'
    assert test_local_tow.format_day(test_date, gmt_offset=6, dow=False) == 'February 14'

# Generated at 2022-06-14 12:16:29.269923
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """
    [Unit test for method format_day of class Locale]
    """
    from datetime import datetime
    import unittest
    import logging
    import inspect
    import sys
    from unittest.mock import patch
    
    # Loading the logging configuration
    logging.basicConfig(level=logging.INFO)

    # logging the start of test
    current_test = inspect.stack()[0][3]
    logging.info("\n\n >> Starting unit test:  %s", current_test)

    # list of tests

# Generated at 2022-06-14 12:16:30.079937
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    pass

# Generated at 2022-06-14 12:16:39.016760
# Unit test for method list of class Locale
def test_Locale_list():
    from .translation import load_translations

    load_translations()

    Locale.get("en").list(["1", "2", "3"])
    Locale.get("en").list(["1", "2"])
    Locale.get("en").list(["1"])
    Locale.get("zh_CN").list(["1", "2", "3"])
    Locale.get("zh_CN").list(["1", "2"])
    Locale.get("zh_CN").list(["1"])
    Locale.get("fa").list(["1", "2", "3"])
    Locale.get("fa").list(["1", "2"])
    Locale.get("fa").list(["1"])



# Generated at 2022-06-14 12:16:44.616794
# Unit test for function load_translations
def test_load_translations():
    load_translations("tornado/_test/test_locale.csv")
    assert _translations["test_locale"]["plural"]["one"] == "Test string"
    assert _translations["test_locale"]["plural"]["two"] == "Test string two"


# Generated at 2022-06-14 12:16:50.011545
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert (
        _translations
        == {}  # type: ignore # mypy thinks _translations is Optional[Dict[str, Any]]
    )
    assert _supported_locales == frozenset([_default_locale])
    assert _use_gettext is False
    load_gettext_translations(directory="/path/to/directory", domain="mydomain")
    assert (
        _translations
        != {}  # type: ignore # mypy thinks _translations is Optional[Dict[str, Any]]
    )
    assert (
        _supported_locales
        != frozenset([_default_locale])  # type: ignore # mypy thinks _supported_locales is Optional[frozenset[str]]
    )
    assert _use_gettext is True



# Generated at 2022-06-14 12:16:54.970219
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    l = Locale("")
    assert l.friendly_number(1) == "1"
    assert l.friendly_number(1000) == "1,000"
    assert l.friendly_number(1000000) == "1,000,000"
    assert l.friendly_number(1000000000) == "1,000,000,000"



# Generated at 2022-06-14 12:16:58.912883
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    from .util_test import _do_test
    from .locale_data import _suppress_locale_warnings
    with _suppress_locale_warnings(), _do_test(Locale):
        Locale.get_closest("ko", "en")



# Generated at 2022-06-14 12:17:05.416394
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale.get("en")
    assert locale.friendly_number(1000) == '1,000'
    assert locale.friendly_number(-1000) == '-1,000'
    assert locale.friendly_number(1000579) == '1,000,579'
    assert locale.friendly_number(-1000579) == '-1,000,579'
    assert locale.friendly_number(0) == '0'



# Generated at 2022-06-14 12:17:28.085604
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale.get('en').format_day(datetime.datetime(2018, 1, 22)) == 'Monday, January 22'


# Generated at 2022-06-14 12:17:29.803169
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    pass
load_translations("app/translations")

# Generated at 2022-06-14 12:17:32.635327
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale(code='es')
    locale.format_day(date=datetime.datetime(2020, 4, 1), dow=True)

# Generated at 2022-06-14 12:17:41.722431
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    global _translations
    global _supported_locales
    global _use_gettext
    # Make sure that gettext uses our mock, not whatever is installed in
    # the system.
    assert gettext._installed_translation_function == gettext.translation
    assert gettext._default_localedir == "foo/locale"
    assert _translations == {"de_DE": "foo", "ru": "bar", "ru_RU": "baz"}
    assert _supported_locales == frozenset(["en_US"])
    assert _use_gettext is False
    gettext._installed_translation_function = None
    gettext._default_localedir = "/usr/share/locale"


# Generated at 2022-06-14 12:17:42.990239
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations('./', 'tornado')



# Generated at 2022-06-14 12:17:53.966884
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """Test format_day"""

    # create a timestamp
    now = datetime.datetime.now()
    today = now.date()

    # create two Locale objects
    en_locale = Locale.get("en_US")
    ar_locale = Locale.get("ar")

    # change the day of the timestamp
    delta = datetime.timedelta(days=10)
    then = today + delta

    # format in en_locale
    assert en_locale.format_day(now) == \
        '%s, %s %d' % (en_locale._weekdays[now.weekday()],
                       en_locale._months[now.month - 1],
                       now.day)

# Generated at 2022-06-14 12:17:57.138472
# Unit test for function load_translations
def test_load_translations():
    directory = r"C:\Dev\tornado\demos\blog\content\locale"
    load_translations(directory)
    print(_translations)
    print(_supported_locales)
# test_load_translations()


# Generated at 2022-06-14 12:18:02.376881
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale.get('en').format_day(datetime.datetime(2018,1,22),0)=='Monday, January 22'
    assert Locale.get('en').format_day(datetime.datetime(2018,1,22),0,False)=='January 22'


# Generated at 2022-06-14 12:18:14.982970
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    def _test_Locale_format_date(locale_id, date, gmt_offset, expected):
        assert Locale.get(locale_id).format_date(date, gmt_offset) == expected
    now = time.time()    
    # relative
    _test_Locale_format_date("en", now - 1, 0, "1 second ago")
    _test_Locale_format_date("en", now - 121, 0, "1 minute ago")
    _test_Locale_format_date("en", now - 3122, 0, "1 hour ago")
    _test_Locale_format_date("en", now - 3122, 0, "1 hour ago")
    _test_Locale_format_date("en", now - (24 * 3600 * 1), 0, "yesterday")
   

# Generated at 2022-06-14 12:18:23.677212
# Unit test for function load_translations
def test_load_translations():
    load_translations("./test/translations")
    locale = get("zh_CN")
    assert locale.translate("My name is %(name)s", name="小李子") == "我的名字叫小李子"
    assert locale.translate(
        "%(name)s liked this",
        plural="%(name)s liked this",
        name=locale.list(["小李子", "小智"])) == "小李子和小智喜欢这个"

# Generated at 2022-06-14 12:18:55.979884
# Unit test for function load_translations
def test_load_translations():
    test_dir = os.path.join(os.getcwd(), "unit_tests", "test_locale_data")
    load_translations(test_dir)
    assert _translations=={"en": {"unknown": {"test": "test"}}, "es": {"unknown": {"test": "test_es"}}}



# Generated at 2022-06-14 12:19:04.502673
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # Case 1:
    # Given:
    #       The year, month and day of now
    # When:
    #       we build a datetime
    #       we set gmt_offset = 0
    #       we set dow = True
    # Then:
    #       The format of day of week should be "Monday, January 22"
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    dt = datetime.datetime(year, month, day)

    # Case 2:
    # Given:
    #       A datetime
    #       gmt_offset = 0
    #       dow = True
    # When:
    #       we call format_day
    # Then:
    #       The format of day of week should be "Monday,

# Generated at 2022-06-14 12:19:12.764046
# Unit test for function load_translations
def test_load_translations():
    import sys
    import tornado.escape
    import tornado.locale
    class TestLocale:
        def setup_method(self, method):
            self.save_translations = tornado.locale._translations
            tornado.locale._translations = {}
        
        def teardown_method(self, method):
            tornado.locale._translations = self.save_translations
            
        def test_load_translations(self):
            directory = os.path.join(os.path.dirname(__file__), "test", "translations")
            tornado.locale.load_translations(directory)
            locale = tornado.locale.get("es_LA")
            self.assertTrue(locale.translate("I love you") == "Te amo")

    return TestLocale()



# Generated at 2022-06-14 12:19:19.069207
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # When there is no dow variable
    assert Locale.get("en_US").format_day(datetime.datetime(2004, 1, 2)) == 'January 2'
    # When there is dow variable
    assert Locale.get("en_US").format_day(datetime.datetime(2004, 1, 2), dow = False) == 'January 2'

# Generated at 2022-06-14 12:19:29.585119
# Unit test for function load_translations
def test_load_translations():
    import tornado
    import os
    os.chdir('test')
    tornado.locale.load_translations("test_locale/")
    locale = tornado.locale.get("en_US")
    assert locale.translate("%(name)s liked this", name="Xingyu") == "Xingyu liked this"
    assert locale.translate("%(name)s liked this", name=["Xingyu", "Yingyu"]) == "Xingyu, Yingyu liked this"
    assert locale.translate("%(name)s liked this", name=["Xingyu", "Yingyu", "Zingyu"]) == "Xingyu, Yingyu, Zingyu liked this"



# Generated at 2022-06-14 12:19:40.713676
# Unit test for function load_translations
def test_load_translations():
    directory = "../../tornado"
    path = "../../tornado/_locale_data.py"
    encoding = "utf-8"
    test_path = os.path.join(directory, path)
    if encoding is None:
            # Try to autodetect encoding based on the BOM.
            with open(test_path, "rb") as bf:
                data = bf.read(len(codecs.BOM_UTF16_LE))
            if data in (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE):
                encoding = "utf-16"

# Generated at 2022-06-14 12:19:49.545079
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """Test method format_day of class Locale"""
    test_date = datetime(2017, 8, 7)
    # gmt_offset = 0, dow = True
    result = Locale.get("en").format_day(test_date)
    assert result == "Monday, August 7", "Expected 'Monday, August 7', got " + result
    # gmt_offset = 0, dow = False
    result = Locale.get("en").format_day(test_date, dow = False)
    assert result == "August 7", "Expected 'August 7', got " + result
    # gmt_offset = 1, dow = True
    result = Locale.get("en").format_day(test_date, gmt_offset = 1)

# Generated at 2022-06-14 12:19:56.384576
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    '''Unit test for method format_day of class Locale
    '''
    locale = Locale.get('en')
    date = datetime.datetime(2015, 8, 1, 0, 0, 0, 0)
    gmt_offset = 1
    dow = True
    assert locale.format_day(date, gmt_offset, dow) == 'Saturday, August 1'
    dow = False
    assert locale.format_day(date, gmt_offset, dow) == 'August 1'



# Generated at 2022-06-14 12:20:06.642026
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import unittest
    import os
    import sys

    class LoadGettextTranslationsTest(unittest.TestCase):
        def setUp(self):
            self._dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self._domain = 'tornado'
            self.domain = os.path.join(self._dir, 'locale', self._domain)
            if not os.path.exists(self.domain):
                os.makedirs(self.domain)

        def tearDown(self):
            import shutil
            if os.path.exists(self.domain):
                shutil.rmtree(self.domain)


# Generated at 2022-06-14 12:20:16.158800
# Unit test for function load_translations
def test_load_translations():
    dic = {}
    dic["en_US"] = {}
    dic["en_US"]["plural"] = {}
    dic["en_US"]["plural"]["%(name)s liked this"] = "A %(name)s les gustó esto"
    dic["en_US"]["singular"] = {}
    dic["en_US"]["singular"]["I love you"] = "Te amo"
    load_translations("D:/Users/Administrator/PycharmProjects/tornado_test/tornado/locale/")
    assert sorted(dic.items()) == sorted(_translations.items())



# Generated at 2022-06-14 12:20:49.118853
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale.get("en_US")
    assert locale.friendly_number(1000) == "1,000"
    assert locale.friendly_number(1) == "1"
    assert locale.friendly_number(1234) == "1,234"
    assert locale.friendly_number(123456789) == "123,456,789"



# Generated at 2022-06-14 12:20:56.003800
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from datetime import datetime
    from tornado.testing import AsyncTestCase
    locale = Locale("en")
    # check for day of week
    gmt_offset = 0
    dow = True
    date = datetime(2017, 9, 20, 12, 0, 0)
    assert locale.format_day(date, gmt_offset=gmt_offset, dow=dow) == "Wednesday, September 20"
    # check for day of week
    gmt_offset = 0
    dow = False
    date = datetime(2017, 9, 20, 12, 0, 0)
    assert locale.format_day(date, gmt_offset=gmt_offset, dow=dow) == "September 20"

# Generated at 2022-06-14 12:21:03.085003
# Unit test for function load_translations
def test_load_translations():
    import os
    os.chdir(os.path.dirname(__file__))
    load_translations('locale')
    assert _translations['en']['unknown']['Sign out']=='Sign out'
    assert _translations['zh_CN']['unknown']['Sign out']=='登出'
    assert _translations['zh_CN']['unknown']['Sign in']=='登陆'
    os.chdir(os.path.dirname(__file__))



# Generated at 2022-06-14 12:21:06.435307
# Unit test for function load_translations
def test_load_translations():
    global _translations
    load_translations("./translations")
    assert _translations != {}, "load_translations properly loaded translations"

# Generated at 2022-06-14 12:21:14.979098
# Unit test for function load_translations
def test_load_translations():
    directory = "test_dir"
    f = open(os.path.join(directory, "zh_CN.csv"), "w") 
    f.write("\"链接\",\"link\",\"plural\"\n")
    f.write("\"登出\",\"logout\",\"singular\"\n")
    load_translations(directory)
    assert _translations["zh_CN"] == {'plural': {'链接': 'link'}, 'singular': {'登出': 'logout'}}

# path is the directory which contains .mo file

# Generated at 2022-06-14 12:21:18.373559
# Unit test for function load_translations
def test_load_translations():
    load_translations(".")
    # test_load_translations to load spanish
    assert _translations["es_LA"]["Sign out"] == "Salir"
    assert _translations["es_LA"]["Sign in"] == "Entrar"
    assert _translations["es_LA"]["Sign In"] == "Entrar"



# Generated at 2022-06-14 12:21:24.819252
# Unit test for function load_translations
def test_load_translations():
    #directory = "../locale/ja_JP.csv"
    directory = "../locale"
    load_translations(directory)
    print(get("ja_JP").translate("This is a test") + "\n")
    print(get("en_US").translate("This is a test"))
# Example use
#test_load_translations()

# This function is copied from gettext.py in the standard library.

# Generated at 2022-06-14 12:21:29.367591
# Unit test for function load_translations
def test_load_translations():
    from tornado.testing import AsyncTestCase, gen_test

    # No need to actually load translations for test
    def load_translations(d, e=None):
        pass
    load_translations("testdata/locale")



# Generated at 2022-06-14 12:21:37.478963
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    for lang, lang_names in LOCALE_NAMES.items():
        # GMT+8
        date_fmt = lang_names.get('date_fmt', '%a, %b %d')
        locale = Locale.get(lang)
        assert locale.format_day(datetime.datetime(2017, 7, 3, 8, 0, 0), 8, True) == time.strftime(date_fmt, time.struct_time((2017, 7, 3, 0, 0, 0, 0, 0, 0)))
        assert locale.format_day(datetime.datetime(2017, 7, 3, 8, 0, 0), 8, False) == time.strftime(date_fmt[4:].strip(), time.struct_time((2017, 7, 3, 0, 0, 0, 0, 0, 0)))



# Generated at 2022-06-14 12:21:49.278190
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    now = time.time()
    assert Locale.get("en").format_date(now - 60) == "1 minute ago"
    assert Locale.get("en").format_date(now - 61) == "2 minutes ago"
    assert Locale.get("en").format_date(now - 61, full_format=True) == "2 minutes ago"
    assert Locale.get("en").format_date(now - 61, relative=False) == "Jan 1, 1970 at 12:00 am"
    assert Locale.get("en").format_date(now - 61, relative=False, full_format=True) == "Jan 1, 1970 at 12:00 am"
    assert Locale.get("en").format_date(now - 60 * 60) == "1 hour ago"

# Generated at 2022-06-14 12:22:24.354971
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    test_loc = "E:/Project/tornado/tornado/_locale_data/zh_CN"
    domain = 'tornado.locale'
    load_gettext_translations(test_loc, domain)


# Generated at 2022-06-14 12:22:32.931725
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale('en_US')
    assert locale.format_day(datetime.datetime(2017, 6, 14), 2) == 'Wednesday, June 14'
    assert locale.format_day(datetime.datetime(2018, 6, 15), 2, True) == 'Friday, June 15'
    assert locale.format_day(datetime.datetime(2018, 6, 15), 2, False) == 'June 15'


_translations: Dict[str, Any] = {}
_default_locale = "en_US"
_supported_locales = {_default_locale}
_use_gettext = False

# Generated at 2022-06-14 12:22:41.877005
# Unit test for function load_translations
def test_load_translations():
    # Test load_translations function in tornado/util.py
    # It needs a directory with CSV files,
    # try to run this test in a unit test environment
    load_translations(".")
    # Results:
    # If a CSV file is found, it should be read
    # If no CSV file is found, nothing should be loaded
    print("Unit test for function load_translations in tornado/util.py")
    print("Supported locales:")
    for locale in _supported_locales:
        print(locale)
    return



# Generated at 2022-06-14 12:22:52.686274
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale.get("en").format_day(datetime.datetime(2019, 12, 20)) == "Friday, December 20"
    assert Locale.get("en").format_day(datetime.datetime(2019, 12, 21)) == "Saturday, December 21"
    assert Locale.get("en").format_day(datetime.datetime(2019, 12, 22)) == "Sunday, December 22"
    assert Locale.get("en").format_day(datetime.datetime(2019, 12, 23)) == "Monday, December 23"
    assert Locale.get("en").format_day(datetime.datetime(2019, 12, 24)) == "Tuesday, December 24"
    assert Locale.get("en").format_day(datetime.datetime(2019, 12, 25)) == "Wednesday, December 25"
   

# Generated at 2022-06-14 12:23:03.201832
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    g = GettextLocale('zh_CN', _translations['zh_CN'])
    assert g.pgettext('law', 'right') == '权利'
    assert g.pgettext('good', 'right') == '对'
    assert g.pgettext('organization', 'club', 'clubs', len(['a', 'b', 'c'])) == '俱乐部'
    assert g.pgettext('stick', 'club', 'clubs', len(['a', 'b', 'c'])) == '棒球棒'
    assert g.pgettext('law', 'right') == '权利'
    assert g.pgettext('good', 'right') == '对'

# Generated at 2022-06-14 12:23:14.474138
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import tempfile
    import shutil
    import os
    import re
    import gettext

    domain = 'messages'
    directory = os.path.join(tempfile.gettempdir(), 'tornado_locale_test')

    # Generate POT translation file
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Generate .po file
    os.system("xgettext --language=Python --keyword=_:1,2 -d %s %s "
              "--from-code=UTF-8 -o %s" % (
                  domain, os.path.join(os.path.dirname(__file__), 'test_locale.py'),
                  os.path.join(directory, domain + '.pot')))

# Generated at 2022-06-14 12:23:17.993183
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations(
        directory="./locale",
        domain = "mydomain"
    )
    msg = _translations['pt_BR'].gettext("hello")
    assert msg == "Olá"
    msg = _translations['en_US'].gettext("hello")
    assert msg == "olá"


# Generated at 2022-06-14 12:23:21.087100
# Unit test for function load_translations
def test_load_translations():
    load_translations("locale")

# Generated at 2022-06-14 12:23:28.292291
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    expected = "10"
    actual = Locale.get("en_US").friendly_number(10)
    assert expected == actual

    expected = "1,000"
    actual = Locale.get("en_US").friendly_number(1000)
    assert expected == actual

    expected = "1,000,000"
    actual = Locale.get("en_US").friendly_number(1000000)
    assert expected == actual

    expected = "1,000,000,000"
    actual = Locale.get("en_US").friendly_number(1000000000)
    assert expected == actual



# Generated at 2022-06-14 12:23:30.486686
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    directory = ""
    domain = ""
    return load_gettext_translations(directory, domain)



# Generated at 2022-06-14 12:24:46.073896
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    from babel.support import Translations
    from functools import partial
    import random
    from unittest.mock import MagicMock
    """
    Unit test for method pgettext of class Locale
    """

    def dumb_translate(singular, plural=None, count=None):
        if count is None:
            return singular
        return plural if count == 1 else singular

    def dumb_pgettext(context, singular, plural=None, count=None):
        return '{0}:{1}'.format(context, dumb_translate(singular, plural, count))

    # print("Test Cases")
    # print("-----------")

# Generated at 2022-06-14 12:24:58.217692
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    assert Locale("en_US").format_date(datetime.datetime.fromtimestamp(1528365272)) == "2 minutes ago"
    assert Locale("en_US").format_date(datetime.datetime.fromtimestamp(1528365272), full_format=True) == "May 29, 2018 at 7:04 pm"
    assert Locale("en_US").format_date(datetime.datetime.fromtimestamp(1528365272), gmt_offset=600) == "2 minutes ago"
    assert Locale("en_US").format_date(datetime.datetime.fromtimestamp(1528365272), relative=False) == "May 29, 2018 at 5:04 pm"

# Generated at 2022-06-14 12:25:06.709446
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    from .test_utils import get_test_data
    code = "he"
    translations = {}
    data = get_test_data("locale.csv", "translations.csv", "untranslated.csv")
    for r in data:
        if r["lang"] == code:
            translations[r["key"]] = r["translation"]
    locale = CSVLocale(code, translations)
    assert locale.pgettext("law", "right") == "זכות"
    assert locale.pgettext("good", "right") == "נכון"
    assert locale.pgettext("organization", "club","clubs", len(["a"])) == "כנסת"

# Generated at 2022-06-14 12:25:17.291512
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    code = "pt_BR"
    locale = Locale.get(code)
    time1 = 1530108715
    time2 = 1530108715 - 60
    time3 = 1530108715 - 60 - 60
    time4 = 1530108715 - 60 - 60*24
    time5 = 1530108715 - 60 - 60*24*34
    time6 = 1530108715 - 60 - 60*24*365
    assert locale.format_date(time1) == "Agora"
    assert locale.format_date(time2) == "1 minuto atrás"
    assert locale.format_date(time3) == "1 hora atrás"
    assert locale.format_date(time4) == "ontem às 19:15"

# Generated at 2022-06-14 12:25:20.001495
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # Locale.pgettext
    assert GettextLocale("en_US", None).pgettext("context", "hello") == "hello"

# Generated at 2022-06-14 12:25:21.263598
# Unit test for function load_translations
def test_load_translations():
    os.chdir('../tests')
    load_translations('locale')



# Generated at 2022-06-14 12:25:30.852348
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    assert Locale("en_US").pgettext("x1", "y1", "z1", 1) == "y1"
    assert Locale("en_US").pgettext("x1", "y1", "z1", 2) == "z1"
    assert Locale("en_US").pgettext("x1", "y1", "z1") == "y1"

    assert Locale("en_GB").pgettext("x1", "y1", "z1", 1) == "y1"
    assert Locale("en_GB").pgettext("x1", "y1", "z1", 2) == "z1"
    assert Locale("en_GB").pgettext("x1", "y1", "z1") == "y1"



# Generated at 2022-06-14 12:25:35.599033
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    locale = Locale.get_closest("en_US")
    assert locale.pgettext('w', 'word') == 'word'
    assert locale.pgettext('w', 'word', count = 1) == 'word'
    assert locale.pgettext('w', 'word', plural_message = 'words') == 'word'
    assert locale.pgettext('w', 'word', count = 2, plural_message = 'words') == 'words'
