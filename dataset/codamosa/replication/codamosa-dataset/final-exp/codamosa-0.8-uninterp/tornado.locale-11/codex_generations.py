

# Generated at 2022-06-14 12:16:38.645073
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    locale = Locale.get("ja")
    assert locale.pgettext("law", "right") == "権利"
    assert locale.pgettext("good", "right") == "正しい"
    assert locale.pgettext("organization", "club", "clubs", 2) == "部"
    assert locale.pgettext("stick", "club", "clubs", 2) == "棒"


# Generated at 2022-06-14 12:16:40.481533
# Unit test for function load_translations
def test_load_translations():
    directory="./test"
    encoding="utf-8-sig"
    load_translations(directory,encoding)
    gen_log.debug(_translations)


# Generated at 2022-06-14 12:16:50.128325
# Unit test for method format_day of class Locale

# Generated at 2022-06-14 12:16:59.975361
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import os
    import locale

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    dir = os.path.join(os.path.dirname(__file__), 'translations')
    domain = 'messages'

    load_gettext_translations(dir, domain)

    LANGUAGE = os.environ.get('LANGUAGE')

    # Available languages
    assert 'pt_BR' in _translations
    assert 'en_US' in _translations
    assert 'fr_FR' in _translations

    # Default language
    assert _default_locale == 'en_US'

    # Test translation with gettext
    assert _translations['pt_BR'].gettext('dog') == 'cachorro'

# Generated at 2022-06-14 12:17:04.160516
# Unit test for function load_translations
def test_load_translations():
    load_translations('/root/data/workplace/tornado/lib/python3.7/site-packages/tornado/_locale_data/')

    assert _translations['en_US'] == _translations[_default_locale]


# Generated at 2022-06-14 12:17:06.925680
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    test_directory = "."
    test_domain = "tornado"
    load_gettext_translations(test_directory, test_domain)



# Generated at 2022-06-14 12:17:18.194655
# Unit test for constructor of class Locale
def test_Locale():
    assert isinstance(Locale.get("en_US"), Locale)
    assert isinstance(Locale.get("en_US"), CSVLocale)
    assert isinstance(Locale.get("en"), Locale)
    assert isinstance(Locale.get("en"), CSVLocale)
    assert isinstance(Locale.get("fa"), Locale)
    assert isinstance(Locale.get("fa"), CSVLocale)
    assert isinstance(Locale.get("fa_IR"), Locale)
    assert isinstance(Locale.get("fa_IR"), CSVLocale)
    assert Locale.get("en").rtl is False
    assert Locale.get("fa").rtl is True
    assert Locale.get("fa_IR").rtl is True



# Generated at 2022-06-14 12:17:21.733740
# Unit test for function load_translations
def test_load_translations():
    load_translations('locale/')
    print("test_load_translations: ", _translations['es_LA'])



# Generated at 2022-06-14 12:17:26.470248
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    loc = Locale.get("fa")
    now = datetime.datetime.utcnow()
    day1 = loc.format_day(now, dow=False)
    day2 = loc.format_day(now)
    print (day1)
    print (day2)


# Generated at 2022-06-14 12:17:31.361094
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # Test 1
    Locale._cache = {}
    _translations = {"en": {"plural": {}, "singular": {"g": "G"}}}
    code = "en"
    translations = _translations.get(code, None)
    _use_gettext = False
    locale = CSVLocale(code, translations)
    _default_locale = "en"
    _supported_locales = frozenset(list(_translations.keys()) + [_default_locale])

    context = "c"
    message = "m"
    plural_message = "pm"
    count = 10

    result = locale.pgettext(context, message, plural_message, count)
    assert result is None

    # Test 2
    Locale._cache = {}

# Generated at 2022-06-14 12:18:09.349122
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    l = Locale.get("en_US")
    assert l.friendly_number(0) == "0"
    assert l.friendly_number(1) == "1"
    assert l.friendly_number(999) == "999"
    assert l.friendly_number(1000) == "1,000"
    assert l.friendly_number(1001) == "1,001"
    assert l.friendly_number(1000000) == "1,000,000"
    assert l.friendly_number(123456789) == "123,456,789"
    assert l.friendly_number(1234567890) == "1,234,567,890"
    l = Locale.get("fa")
    assert l.friendly_number(0) == "0"

# Generated at 2022-06-14 12:18:20.734211
# Unit test for method list of class Locale
def test_Locale_list():
    L = Locale("fa_IR")
    parts = ["A", "B", "C"]
    assert L.list(parts) == "A \u0648 B \u0648 C"
    parts = ["A", "B", "C", "D"]
    assert L.list(parts) == "A \u0648 B \u0648 C \u0648 D"
    parts = ["A", "B", "C", "D", "E"]
    assert L.list(parts) == "A, B, C, D \u0648 E"
    parts = ["A", "B", "C", "D", "E", "F"]
    assert L.list(parts) == "A, B, C, D, E \u0648 F"


# Generated at 2022-06-14 12:18:27.069950
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    gen_log.info('Hello')
    gen_log.info(Locale.friendly_number(1000))
    gen_log.info(Locale.friendly_number(10000))
    gen_log.info(Locale.friendly_number(100000))
    gen_log.info(Locale.friendly_number(1000000))
    gen_log.info(Locale.friendly_number(10000000))
    gen_log.info(Locale.friendly_number(100000000))



# Generated at 2022-06-14 12:18:29.547979
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    code = 'en_US'
    locale_for_test = Locale(code)
    assert locale_for_test.friendly_number(1) == "1"



# Generated at 2022-06-14 12:18:41.567357
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    def _test(locale_code, date_str, gmt_offset, relative, shorter, full_format):
        date = datetime.datetime(*[int(x) for x in date_str.split(" ")[0].split("-")])
        locale = Locale.get(locale_code)
        return locale.format_date(date, gmt_offset, relative, shorter, full_format)

    # TODO: tests to check that strings containing non-ASCII characters
    # are actually returned in Unicode. Right now this is only true for
    # the Russian translation.

    # "0 seconds ago" in all languages
    assert _test("cs", "2013-08-13 20:00:30", 0, True, False, False) == "před vteřinou"

# Generated at 2022-06-14 12:18:51.205844
# Unit test for method format_day of class Locale

# Generated at 2022-06-14 12:19:01.023833
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    from datetime import datetime

# Generated at 2022-06-14 12:19:11.222228
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    ignore = Locale.get("en_US")
    ignore = GettextLocale("en_US", gettext.NullTranslations())

    def get_context_and_message(msg: str) -> Tuple[str, str]:
        """Returns tuple (context, message)

        where message is translated message without context,
        and context is message context if message was translated,
        or '' if message was not translated.
        """
        result = msg.split(CONTEXT_SEPARATOR)
        if len(result) == 1:
            # Not translated
            return ("", msg)
        else:
            return (result[0], CONTEXT_SEPARATOR.join(result[1:]))


# Generated at 2022-06-14 12:19:23.713444
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    Locale.get('es').format_date(date=datetime.datetime(2019, 1, 1, 16, 30),gmt_offset=0)
    Locale.get('zh_CN').format_date(date=datetime.datetime(2019, 1, 1, 16, 30),gmt_offset=0)
    Locale.get('es').format_date(date=1487422700.0,gmt_offset=0)
    Locale.get('es').format_date(date=1487422700.0,gmt_offset=0,relative=False)
    Locale.get('es').format_date(date=1487422700.0,gmt_offset=0,shorter=True)

# Generated at 2022-06-14 12:19:31.124007
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # get_supported_locales()
    locales = get_supported_locales()
    for x in locales:
        if x == "fa":
            L = Locale.get(x)
        # print(x)
    date = datetime.datetime(2019, 5, 20)
    print(L.format_day(date))
    # print(date)
    # print(L.format_day(date, dow=False)) #this is what I want
    return
test_Locale_format_day()


# Generated at 2022-06-14 12:20:07.017723
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    class TestingLocale(Locale):
        def pgettext(
            self,
            context: str,
            message: str,
            plural_message: Optional[str] = None,
            count: Optional[int] = None,
        ) -> str:
            pass

# Generated at 2022-06-14 12:20:18.343397
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import os
    import shutil
    import tempfile
    import unittest

    from tornado.util import PYTHON3

    if PYTHON3:
        # gettext is built in, so there is no egg to install
        skip_if = None  # type: Optional[unittest.SkipTest]
    else:
        try:
            import pkg_resources
        except ImportError:
            skip_if = unittest.skip("pkg_resources not imported")
        else:
            try:
                pkg_resources.require("Babel >=0.9.6")
            except pkg_resources.DistributionNotFound:
                skip_if = unittest.skip("gettext not installed")
            else:
                skip_if = None


# Generated at 2022-06-14 12:20:25.493904
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale(code='fr_FR')
    locale_ = {
        'day': '24',
        'month_name': 'avril',
        'weekday': 'mardi'
    }
    assert locale.format_day(date=datetime.datetime(2020, 4, 24, 12, 8, 52, 543341), dow=False) == 'avril 24'
    assert locale.format_day(date=datetime.datetime(2020, 4, 24, 12, 8, 52, 543341)) == 'mardi, avril 24'
    locale_ = {
        'day': '26',
        'month_name': 'avril',
        'weekday': 'jeudi'
    }

# Generated at 2022-06-14 12:20:32.294617
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    def test_Locale_format_date_scenario(code, date, gmt_offset, relative, shorter, full_format, result):
        # Arrange
        load_gettext_translations("/tmp/translations", "zulip")
        locale = Locale.get(code)
        # Act
        actual_result = locale.format_date(date, gmt_offset, relative, shorter, full_format)
        # Assert
        if actual_result != result:
            raise AssertionError("Actual result: %s is not equal to expected result: %s" % (actual_result, result))
    # Should return a relative time

# Generated at 2022-06-14 12:20:43.880614
# Unit test for function load_translations
def test_load_translations():
    translation_test = {}
    translation_test['en_US'] = {
        '':{
            'test': 'test'
        }
    }
    translation_test['zh_CN'] = {
        '':{
            'test': '测试'
        }
    }
    global _translations
    global _supported_locales
    global _default_locale
    _default_locale = 'en_US'
    _supported_locales = frozenset([_default_locale])
    _translations = translation_test
    assert translation_test == _translations
    assert _supported_locales == frozenset(['en_US'])
    set_default_locale('zh_CN')
    assert _default_locale == 'zh_CN'
    assert _supported_locales == frozenset

# Generated at 2022-06-14 12:20:53.482105
# Unit test for function load_translations
def test_load_translations():
    # Enforce known encoding behavior
    os.environ["LANG"] = "en_US.UTF-8"

    def translate(locale_codes, english, expected=None):
        locale = Locale.get_closest(*locale_codes)
        if expected is None:
            expected = english
        translation = locale.translate(english, plural=None)
        assert translation == expected, "%s for %s -> %s" % (
            english,
            locale_codes,
            translation,
        )

    # Empty translation directory
    load_translations("/does/not/exist")
    translate(["en_US"], "hi")

    from tempfile import mkdtemp

    # BOM-less UTF8
    tempdir = mkdtemp()

# Generated at 2022-06-14 12:21:04.071284
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    # Locale.code is en
    l = Locale("en")
    assert l.friendly_number(0) == '0'
    assert l.friendly_number(11) == '11'
    assert l.friendly_number(1234) == '1,234'
    assert l.friendly_number(-123) == '-123'
    assert l.friendly_number(-1234) == '-1,234'
    # Locale.code is not en
    l = Locale("zh-CN")
    assert l.friendly_number(0) == '0'
    assert l.friendly_number(11) == '11'
    assert l.friendly_number(1234) == '1234'
    assert l.friendly_number(-123) == '-123'

# Generated at 2022-06-14 12:21:13.609377
# Unit test for function load_translations
def test_load_translations():
    def test_func():
        set_default_locale("en_US")
        load_translations("tests/i18n")
        user_locale = Locale.get_closest("es_LA")
        print(user_locale.translate("Sign out"))
        people = ["Ben Darnell", "Guido van Rossum", "Andrew Gerrand"]
        message = user_locale.translate(
            "%(list)s is online", "%(list)s are online", len(people))
        print(message % {"list": user_locale.list(people)})

    test_func()

# Generated at 2022-06-14 12:21:19.758879
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale(code="en")
    # Test 1
    n = locale.friendly_number(1234567890)
    assert n == '1,234,567,890'
    # Test 2
    n = locale.friendly_number(123)
    assert n == '123'
    # Test 3
    n = locale.friendly_number(12345)
    assert n == '12,345'
    # Test 4
    n = locale.friendly_number(1234567)
    assert n == '1,234,567'
    # Test 5
    n = locale.friendly_number(1)
    assert n == '1'



# Generated at 2022-06-14 12:21:29.475634
# Unit test for function load_translations
def test_load_translations():
    directory = "./translations"
    encoding = "UTF-8"
    load_translations(directory, encoding)
    assert _default_locale == "en_US"
    assert _translations != {}
    assert _supported_locales == frozenset({'en_US', 'en_UK', 'fr_FR'})

_month_names = {"long": [], "short": []}  # type: Dict[str, List[str]]
_day_names = {"long": [], "short": []}  # type: Dict[str, List[str]]
_first_week_day = 0



# Generated at 2022-06-14 12:22:06.277281
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert(Locale("en_US").format_day(datetime.datetime(2018,3,14), dow=False) == "March 14")
    assert(Locale("en_US").format_day(datetime.datetime(2018,3,14), dow=True) == "Wednesday, March 14")
    assert(Locale("zh_CN").format_day(datetime.datetime(2018,3,14), dow=False) == "3\u670814\u65e5")
    assert(Locale("zh_CN").format_day(datetime.datetime(2018,3,14), dow=True) == "3\u670814\u5468\u4e8c")

# Generated at 2022-06-14 12:22:14.963072
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    d = os.path.join(os.path.dirname(__file__), 'test', 'gettext')
    x = load_gettext_translations(d, "mydomain")
    _translation = load_gettext_translations
    assert d == os.path.join(os.path.dirname(__file__), 'test', 'gettext')
    assert os.path.isfile(os.path.join(d, x))
    if _translation is False:
        print("This Function is not working, sorry")
    else:
        print("gettext_translations is working")
#test_load_gettext_translations()



# Generated at 2022-06-14 12:22:24.197866
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale('en')
    t_date = datetime.datetime(2016, 1, 25, 11, 11, 11)
    t_dow = datetime.datetime(2016, 1, 25, 11, 11, 11).weekday()
    t_res = locale.format_day(t_date)
    t_exp = datetime.datetime(2016, 1, 25, 11, 11, 11).strftime("%A, %B %d")
    if (t_res != t_exp):
        print("Locale.format_day() could not format date correctly.")
test_Locale_format_day()


# Generated at 2022-06-14 12:22:27.072934
# Unit test for function load_translations
def test_load_translations():
    load_translations('C:/Users/HP/PycharmProjects/tornado/tornado/locale')
    print(_translations)


# Generated at 2022-06-14 12:22:29.278568
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale("en_US").format_day(datetime.datetime(2016, 1, 1)) == "Friday, January 1"



# Generated at 2022-06-14 12:22:32.105083
# Unit test for function load_translations
def test_load_translations():
    import os
    import locale
    directory = os.path.dirname(__file__)
    load_translations(directory + '/locale/')
    user_locale = get(locale.getdefaultlocale()[0])
    trans_msg = user_locale.translate("Hello world")



# Generated at 2022-06-14 12:22:44.209400
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import pytest
    def test_relative_date(locale, date, expected):
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        got = locale.format_date(date, 0, True)
        assert got == expected
    def test_full_date(locale, date, expected):
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        got = locale.format_date(date, 0, False)
        assert got == expected

# Generated at 2022-06-14 12:22:48.952621
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    locale = Locale('en')
    assert locale.friendly_number(1000) == '1,000'
    assert locale.friendly_number(1000000) == '1,000,000'
    assert locale.friendly_number(1234567) == '1,234,567'
    assert locale.friendly_number(100100100) == '100,100,100'



# Generated at 2022-06-14 12:22:54.341587
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    directory = os.path.join(os.path.dirname(__file__), "locale")
    domain = "tornado"
    load_gettext_translations(directory, domain)
    assert _supported_locales == frozenset(["ru_RU", "zh_CN", "en_US"])



# Generated at 2022-06-14 12:23:04.942163
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import datetime

    d = datetime.date.today()
    
    # Test 1
    print("Testing today at 00:00h, format: relative")
    print(f"{d}")
    l = Locale('pt_BR')
    print(l.format_date(d))
    
    # Test 2
    print("Testing today at 00:00h, format: full")
    print(f"{d}")
    l = Locale('pt_BR')
    print(l.format_date(d, full_format = True))
    
    # Test 3
    print("Testing now, format: relative")
    print(f"{datetime.datetime.now()}")
    l = Locale('pt_BR')
    print(l.format_date(datetime.datetime.now()))


# Generated at 2022-06-14 12:24:13.561512
# Unit test for function load_translations
def test_load_translations():
    load_translations('./locale')
    print(Locale.get_closest('./locale/'))
    print(Locale.get_closest('ko_KR'))
    import os
    print(os.path.basename('ko_KR'))
# test_load_translations()

# Generated at 2022-06-14 12:24:20.676051
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    test_format_day = Locale.format_day
    assert (
        test_format_day(
            datetime.datetime(2020, 2, 15, 8, 21, 3, 867963),
            gmt_offset=0,
            dow=True
        )
        == "Saturday, February 15"
    )
    assert (
        test_format_day(
            datetime.datetime(2020, 2, 15, 8, 21, 3, 867963),
            gmt_offset=0,
            dow=False
        )
        == "February 15"
    )

# Generated at 2022-06-14 12:24:23.810168
# Unit test for function load_translations
def test_load_translations():
    load_translations('./locale_data')
    assert get('en_US').translate('%(name)s liked this') == '%(name)s liked this'


# Generated at 2022-06-14 12:24:34.999971
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from datetime import datetime

    def format_day_with_class_locale(date, gmt_offset, dow):
        return _locale.format_day(date, gmt_offset, dow)

    date = datetime.strptime('2019-01-22 12:40:01', '%Y-%m-%d %H:%M:%S')
    _locale = Locale.get_closest('en')
    assert format_day_with_class_locale(date, 0, True) == "Tuesday, January 22"
    _locale = Locale.get_closest('en_US')
    assert format_day_with_class_locale(date, 0, True) == "Tuesday, January 22"
    _locale = Locale.get_closest('fa')
   

# Generated at 2022-06-14 12:24:45.373668
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # parse time
    import time
    # time is the number of seconds since epoch (1 Jan 1970)
    current_time = time.time()
    date_time = datetime.datetime.fromtimestamp(current_time)
    print(date_time)

    # format time
    now = datetime.datetime.utcnow()
    #print(now)
    current_time = now.timestamp()
    print(current_time)
    print(datetime.datetime.fromtimestamp(current_time))

    # Set supported locales
    load_translations(os.path.join(os.path.dirname(__file__), "locale"))
    supported = get_supported_locales()
    #print(supported)

    print("Locale:")
    print("format date:")

# Generated at 2022-06-14 12:24:47.061653
# Unit test for function load_translations
def test_load_translations():
    # load_translations("../locale")
    pass


# Generated at 2022-06-14 12:24:58.707242
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    test_directory = "test/test_directory"
    test_domain = "mydomain.po"

# Generated at 2022-06-14 12:25:01.031153
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert(load_gettext_translations("locale", "tornado"))
    assert(_supported_locales == "en_US")


# Generated at 2022-06-14 12:25:12.407449
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    print(load_gettext_translations.__doc__)
    print("")
    print("run this test by executing this command:")
    print("python -m tornado.locale.test_load_gettext_translations")
    class Dummy():
        def __init__(self, name: str) -> None:
            self.name = name
        def __repr__(self) -> str:
            return "<Dummy {0}, {1}>".format(self.name, id(self))
    dummies = [Dummy(name) for name in ('Johnny', 'Jane', 'Juanita', 'John')]
    print("\nThe following list will be output:")
    print(dummies)
    print("\nYou should see three variants of the first line.")

# Generated at 2022-06-14 12:25:15.306868
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # Setup the test
    locale = Locale.get('ar')
    # Execute the test
    result = locale.pgettext('context', 'message')
    # Verify the result
    assert result == 'message'
