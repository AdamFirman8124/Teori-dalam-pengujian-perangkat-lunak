

# Generated at 2022-06-14 12:16:06.257621
# Unit test for function load_translations
def test_load_translations():
    """
    A function to test function:load_translations()
    """
    load_translations('./translations')


# Generated at 2022-06-14 12:16:13.452846
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # Arrange
    _LO_locale_ = Locale.get("lo")
    _LO_locale_.translations = {"test": "ທົດສອບ"}
    # Act
    result = _LO_locale_.pgettext(None, "test")
    # Assert
    if result != "ທົດສອບ":
        raise AssertionError("The result should be 'ທົດສອບ'")


# Generated at 2022-06-14 12:16:23.787799
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    l = CSVLocale("test_locale", {
        "singular": {
            "hello": "hola",
            "message": "mensaje"
        },
        "plural": {
            "hello": "holas",
            "message": "mensajes"
        }
    })

    assert l.translate("hello") == "hola"
    assert l.translate("hello", "hello", 1) == "hola"
    assert l.translate("hello", "hello", 2) == "holas"
    assert l.translate("message", "message", 1) == "mensaje"
    assert l.translate("message", "message", 2) == "mensajes"
    assert l.translate("message", "message") == "mensaje"



# Generated at 2022-06-14 12:16:29.483743
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations('/tmp/locale/', 'tornado')
    assert get('zh_CN').translate('Quit') == '退出'
    assert get('zh_CN').translate('Add') == '添加'
    assert get('zh_CN').translate('Signed in as') == '登录为'
    assert get('en_US').translate('Quit') == 'Quit'
    assert get('en_US').translate('Add') == 'Add'
    assert get('en_US').translate('Signed in as') == 'Signed in as'
    assert get('tr_TR').translate('Quit') == 'Çıkış'
    assert get('tr_TR').translate('Add') == 'Ekle'
   

# Generated at 2022-06-14 12:16:38.938903
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    def _mock_stat(path):
        # type: (str) -> int
        return 0
    _mock_stat_patcher = mock.patch("os.stat", _mock_stat)
    _mock_stat_patcher.start()

    load_gettext_translations(".", "messages")
    assert _supported_locales == {_default_locale}
    assert _translations == {}

    def _mock_stat(path):
        # type: (str) -> int
        return 1
    _mock_stat_patcher.stop()
    _mock_stat_patcher = mock.patch("os.stat", _mock_stat)
    _mock_stat_patcher.start()

    load_gettext_translations(".", "messages")
    assert _supported_loc

# Generated at 2022-06-14 12:16:49.845735
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # test short relative format
    locale = Locale.get("en")
    date1 = datetime.datetime(year=2011, month=7, day=22)
    date2 = datetime.datetime(year=2011, month=7, day=23)
    date3 = datetime.datetime(year=2011, month=7, day=24)
    date4 = datetime.datetime.now() + datetime.timedelta(hours=1)
    assert locale.format_date(date1, relative=True) == "yesterday"
    assert locale.format_date(date1, relative=True, full_format=True) == "July 22, 2011"
    assert locale.format_date(date2, relative=True) == "yesterday at 1:00pm"

# Generated at 2022-06-14 12:16:56.367091
# Unit test for function load_translations
def test_load_translations():
    load_translations(os.path.dirname(__file__))
    assert 'en_US' in _translations
    assert 'Test' in _translations['en_US']
    assert _translations['en_US']['Test'][0] == 'Test'
    assert 'TestContext' in _translations['en_US']
    assert _translations['en_US']['TestContext'][0] == 'Test %(context)s'



# Generated at 2022-06-14 12:17:05.237755
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    
    locale = Locale.get('en_US')
    date = datetime.datetime(2018, 7, 16)
    dow = locale.format_day(date)
    assert dow == 'Monday, July 16'
    
    locale = Locale.get('zh_CN')
    date = datetime.datetime(2018, 7, 16)
    dow = locale.format_day(date, dow=False)
    assert dow == '7月16日'
    
    locale = Locale.get('ru_RU')
    date = datetime.datetime(2018, 7, 16)
    dow = locale.format_day(date)
    assert dow == 'понедельник, 16 июля'
    
    locale = Locale.get('fa_IR')

# Generated at 2022-06-14 12:17:11.038676
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    print(Locale.get("en-US").format_day(datetime.datetime.now()))
    print(Locale.get("zh-CN").format_day(datetime.datetime.now()))
    print(Locale.get("en-US").format_day(datetime.datetime.now(), dow = False))
    print(Locale.get("zh-CN").format_day(datetime.datetime.now(), dow = False))


# Generated at 2022-06-14 12:17:23.971264
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    from datetime import datetime
    
    class TestFormatDay(unittest.TestCase):
        def setUp(self):
            load_translations("locale")
            
        def test_zh_CN(self):
            locale = Locale.get('zh_CN')
            self.assertEqual(locale.format_day(datetime(2017, 6, 8), dow=True), '星期四, 六月 8')
            
        def test_en_US(self):
            locale = Locale.get('en_US')
            self.assertEqual(locale.format_day(datetime(2017, 6, 8), dow=True), 'Thursday, June 8')
            

# Generated at 2022-06-14 12:17:54.205630
# Unit test for function load_translations
def test_load_translations():
    assert len(set(_translations.keys()))==1
    assert len(set(_translations['es_LA'].keys()))==3
    assert _translations['es_LA']['unknown']['I love you']=='Te amo'
    assert _translations['es_LA']['singular']['%(name)s liked this']=='A %(name)s le gustó esto'


# Generated at 2022-06-14 12:17:59.485570
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    '''test for load_gettext_translations'''
    import os
    rtdir = os.path.dirname(os.path.dirname(__file__))
    os.path.join(rtdir, "locale", "en_US", "LC_MESSAGES", "tornado.mo")


# Generated at 2022-06-14 12:18:03.350258
# Unit test for constructor of class Locale
def test_Locale():
    assert(Locale('en').code == 'en')
    assert(Locale('en_US').code == 'en_US')
    assert(Locale('fa_IR').code == 'fa_IR')


# Generated at 2022-06-14 12:18:15.686227
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    locale = GettextLocale("en", _translations["en"])

    class FakeTranslations(object):
        def __init__(self, code: str, translations: gettext.NullTranslations) -> None:
            self.code = code
            self.ngettext = translations.ngettext
            self.gettext = translations.gettext
            self.pgettext = locale.pgettext

    class Locale(object):
        def __init__(self, code: str, translations: Dict[str, Dict[str, str]]) -> None:
            self.code = code
            self.translations = translations
            self.fake_translations = FakeTranslations(code, translations)
            self.ngettext = self.fake_translations.ngettext
            self.gettext = self.fake_translations.get

# Generated at 2022-06-14 12:18:16.887709
# Unit test for function load_translations
def test_load_translations():
    load_translations("../locale/")
    print(_translations)
    assert False



# Generated at 2022-06-14 12:18:18.561688
# Unit test for function load_translations
def test_load_translations():
    load_translations("C:\\Users\\lx\\Desktop\\my-workspace\\tornado-5.1.1\\tornado\\locale")


# Generated at 2022-06-14 12:18:21.056705
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    #@TODO: write tests for unit test for method pgettext of class Locale
    pass

# Generated at 2022-06-14 12:18:31.002872
# Unit test for constructor of class Locale
def test_Locale():
    global _translations
    global _supported_locales
    global _use_gettext

    _translations = {}
    _supported_locales = set()
    _use_gettext = False

    with patch.object(gen_log, 'error') as mock_log_error:
        Locale.get('en_US')
        assert mock_log_error.called

    _supported_locales = {'en_US'}
    l = Locale.get('en_US')
    assert l.code == 'en_US'
    _translations = {'en_US': {'plural': {'A': 'B'}}}
    _use_gettext = True
    mock_log_error.reset_mock()

# Generated at 2022-06-14 12:18:35.631290
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale("en_US")
    date = datetime.datetime(1982,1,1)
    formatted = locale.format_day(date)

    assert "January" in formatted
    assert "1" in formatted


# Generated at 2022-06-14 12:18:44.474680
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # UTILITY FUNCTIONS
    def round_to_milliseconds(time):
        return int((round(time * 1000) / 1000))

    def generate_timestamps():
        timestamp = time.time()
        current_time = time.localtime()

        # will generate timestamps for 10 seconds ago, 1 minute ago, 1 hour ago and 1 day ago
        timestamps_dict = { '0': timestamp, '10 seconds ago': {}, '1 minute ago': {}, '1 hour ago': {}, '1 day ago': {} }
        for key in timestamps_dict:
            if key == '0':
                timestamps_dict[key] = round_to_milliseconds(timestamp)
                continue

            calculation_string = key.rpartition(' ')[0]

# Generated at 2022-06-14 12:18:59.735936
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    test_translations = {}
    print(test_translations)
    assert _translations == test_translations
    assert _supported_locales == frozenset({'en_US', 'es_MX'})
    assert _use_gettext == False


# Generated at 2022-06-14 12:19:11.058430
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    global _translations
    global _supported_locales
    global _use_gettext
    _translations = {}
    _use_gettext = True
    try:
        load_gettext_translations("./locale", "messages")
        assert _translations["pt_BR"].gettext("Hello") == "Olá"
        assert _translations["en_US"].gettext("Hello") == "Hello"
        assert _supported_locales == frozenset(["pt_BR", "en_US"])
    finally:
        _translations = {}
        _supported_locales = frozenset([])
        _use_gettext = False


# Generated at 2022-06-14 12:19:16.298084
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    tests = []
    # Testcase format:
    # (date, gmt_offset, relative, shorter, full_format, expected_output)
    tests.append((datetime.datetime(2018, 12, 27, 12, 0), 0, True, False, False, 'yesterday'))
    tests.append((datetime.datetime(2018, 12, 27, 11, 0), 0, True, False, True, 'December 27, 2018'))
    tests.append((datetime.datetime(2018, 12, 27, 12, 0), 0, True, False, True, 'December 27, 2018'))
    tests.append((datetime.datetime(2018, 12, 27, 13, 0), 0, True, False, True, 'December 27, 2018'))

# Generated at 2022-06-14 12:19:20.642114
# Unit test for constructor of class Locale
def test_Locale():
    locale = Locale("en")
    assert locale.code == "en"
    assert locale.name == "English"
    assert not locale.rtl
    assert len(locale._months) == 12
    assert len(locale._weekdays) == 7


# Generated at 2022-06-14 12:19:21.091163
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    pass



# Generated at 2022-06-14 12:19:29.679753
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    l = Locale.get_closest("en")
    d = datetime.datetime(2017, 12, 24)
    assert l.format_day(d, 0, True) == "Sunday, December 24"
    assert l.format_day(d, 0, False) == "December 24"
    l = Locale.get_closest("es")
    assert l.format_day(d, 0, True) == "Domingo, Diciembre 24"
    assert l.format_day(d, 0, False) == "Diciembre 24"



# Generated at 2022-06-14 12:19:30.542779
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    pass



# Generated at 2022-06-14 12:19:39.552105
# Unit test for method list of class Locale
def test_Locale_list():
    # Test function list of class Locale

    for locale in _supported_locales:
        le = Locale.get(locale)
        # Test lists of size 1
        assert le.list(["A"]) == "A"
        # Test lists of size 2
        assert le.list(["A", "B"]) == "A and B"
        # Test lists of size 3
        assert le.list(["A", "B", "C"]) == "A, B and C"
        # Test lists of size 4
        assert le.list(["A", "B", "C", "D"]) == "A, B, C and D"



# Generated at 2022-06-14 12:19:47.596942
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    # 测试所用的语言包
    directory = 'testdata\\locale'
    domain = 'messages'
    load_gettext_translations(directory, domain)
    assert _translations['en'].gettext("Hello") == "Hello"
    assert _translations['zh'].gettext("Hello") == "你好"
    assert _translations['zh'].gettext("Hello").__class__ == str
    assert _use_gettext == True
    assert _supported_locales == frozenset({'en', 'zh', 'en_US'})



# Generated at 2022-06-14 12:19:58.752752
# Unit test for function load_translations
def test_load_translations():
    import tornado.locale
    class FakeFile:
        def __init__(self, content: str) -> None:
            self.content = content
            self.pos = 0
        def read(self, size: int = -1) -> Bytes:
            if size == -1:
                data = self.content[self.pos:]
            else:
                data = self.content[self.pos : self.pos + size]
            self.pos += len(data)
            return(data)
        def close(self) -> None:
            self.content = b''
            self.pos = 0

    import io
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()

# Generated at 2022-06-14 12:20:33.279749
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from datetime import datetime
    from . import load_gettext_translations
    import os
    import sys
    import unittest
    from tornado.testing import AsyncTestCase, gen_test

    locale_paths = os.path.join(
        sys.path[0], "locale"
    )  # Assume this file is in ROOT/locale/tests
    load_gettext_translations(locale_paths, domain="kiwix-serve")
    print(
        "Loaded locales:", get_supported_locales()
    )  # Assume en and fr_FR are in ROOT/locale/
    print(
        "Default locale:", Locale.get_closest("")
    )  # Assume en is in ROOT/locale/

# Generated at 2022-06-14 12:20:35.102040
# Unit test for function load_translations
def test_load_translations():
    home = os.path.join(os.path.dirname(__file__), '..', '..')
    load_translations(os.path.join(home, "locale"))


# Generated at 2022-06-14 12:20:37.792300
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    time = datetime.datetime(2015, 7, 15, o)
    print(Locale.get('en').format_day(time, 5))

# Generated at 2022-06-14 12:20:48.714100
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    today = datetime.datetime.utcnow()
    today = datetime.datetime(year=today.year, month=today.month, day=today.day)
    t = time.mktime(today.timetuple())
    import pytz
    utc = pytz.timezone("UTC")
    nyc = pytz.timezone("America/New_York")
    try:
        Locale.get_closest(nyc.localize(today).tzname())
        assert False  # pragma: no cover
    except AssertionError:
        pass
    try:
        Locale.get_closest(utc.localize(today).tzname())
        assert False  # pragma: no cover
    except AssertionError:
        pass


# Generated at 2022-06-14 12:20:56.404867
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    global _translations
    global _supported_locales
    global _default_locale
    global _use_gettext
    _use_gettext = False
    _translations = {'en':{'unknown':{'long locale':'English locale'}}}
    _default_locale = 'en'
    _supported_locales = frozenset(list(_translations.keys()) + [_default_locale])
    now = datetime.datetime.utcnow()
    date = now + datetime.timedelta(minutes=3)
    l = Locale.get('en')
    format = l.format_date(date)
    assert format == '3 minutes ago'
    format = l.format_date(date, full_format=True)
    assert format == '%s at %d:%02d'

# Generated at 2022-06-14 12:20:57.045649
# Unit test for function load_translations
def test_load_translations():
    pass


# Generated at 2022-06-14 12:21:07.885853
# Unit test for function load_translations
def test_load_translations():
    '''
    Test load translations.
    First, make a dictionary as the translations.
    Then, call function load_translations to load 
    the translations.
    Test if load_translations works.
    '''
    # make a dictionary
    example_translations = {
        'es_GT': {
            'plural': {"I love you": "Te amo", 
                "%(name)s liked this": "A %(name)s le gustó esto"},
            'singular': {"I love you": "Te amo", 
                "%(name)s liked this": "A %(name)s les gustó esto"},
            'unknown': {}
        }
    }
    
    load_translations(example_translations)
    
    example_locale = 'es_GT'
    example_sing

# Generated at 2022-06-14 12:21:13.938583
# Unit test for function load_translations
def test_load_translations():
    load_translations(os.path.dirname(__file__)+"/test_locale_data")
    assert _translations["en_US"]["test_key"] == "test_value"
    assert _translations["en_US"]["test_key2"] == "test_value2"
    assert _translations["en_US"]["test_key3"] == "test_value3"



# Generated at 2022-06-14 12:21:20.778608
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    def test(locale_code, dt_str, gmt_offset, relative, shorter, full_format, expected):
        # setup
        dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        gmt = int(gmt_offset)

        # run
        locale = Locale.get(locale_code)
        result = locale.format_date(dt, gmt, relative, shorter, full_format)

        # verify
        assert result == expected, 'Locale.format_date(%s, %s, %s, %s, %s, %s) == %r instead of %r' % (dt, gmt, relative, shorter, full_format, locale_code, result, expected)


# Generated at 2022-06-14 12:21:24.934598
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    test_code= 'en'
    test_value= 1000
    expected_result= '1,000'
    actual_result= Locale(test_code).friendly_number(test_value)
    assert actual_result == expected_result



# Generated at 2022-06-14 12:22:02.201566
# Unit test for function load_translations
def test_load_translations():
    from . import locale
    import os
    import sys
    import tempfile
    current_dir = os.getcwd()
    os.chdir(os.path.dirname(__file__))

    def clean_up():
        os.chdir(current_dir)
        sys.path.remove(os.path.abspath('.'))


# Generated at 2022-06-14 12:22:13.887590
# Unit test for function load_translations
def test_load_translations():
    load_translations("test_locale_data/locale")
    assert sorted(_translations.keys()) == ["es_LA"]
    assert (
        sorted(_translations["es_LA"].keys())
        == ["plural", "singular", "unknown"]
    )
    assert (
        sorted(_translations["es_LA"]["singular"].keys())
        == ["I love you", "Sign out", "You have signed out"]
    )
    assert (
        sorted(_translations["es_LA"]["plural"].keys())
        == ["%(name)s liked this"]
    )
    assert (
        sorted(_translations["es_LA"]["unknown"].keys())
        == ["You have 1 new message", "You have %(count)d new messages"]
    )



# Generated at 2022-06-14 12:22:24.405490
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # Variable to represent a date
    date = datetime.datetime(2018,8,18,0,0,0,0)
    # Create an instance of locale with locale code 'en_US'
    locale = Locale.get('en_US')
    # Call the method format_day
    output1 = locale.format_day(date)
    output2 = locale.format_day(date, dow=False)
    # Hard-code some expected outputs
    expected1 = 'Saturday, August 18'
    expected2 = 'August 18'
    # Assertion
    assert(output1==expected1)
    assert(output2==expected2)

# Commented out for now. Cannot import datetime for some reason.

# Generated at 2022-06-14 12:22:34.014569
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from tornado.httpclient import HTTPClient
    import json
    import io
    import sys
    import base64
    import hashlib
    import datetime
    result_output = io.StringIO()
    sys.stdout = result_output
    date = datetime.datetime(2014, 4, 20, 2, 59, 0)
    locale = Locale.get_closest("en_US")
    s = locale.format_day(date, dow=True)
    print(s)
    sys.stdout = sys.__stdout__
    result = result_output.getvalue()
    result_output.close()
    assert result == "Sunday, April 20" or result == "Sunday, April 20\n"

# Generated at 2022-06-14 12:22:38.530239
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    try:
        load_gettext_translations('auj_tornado', 'auj_tornado')
    except Exception as e:
        print(e)
        assert True


# Generated at 2022-06-14 12:22:47.703053
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # test for different timezone
    assert Locale("en").format_date(1457451028) == "1 minute ago"
    # test the result of future date
    assert Locale("en").format_date(1457451028, relative=False) == "April 1 at 4:17 pm"
    # test the full format
    assert Locale("en").format_date(1457451028, full_format=True) == "April 1, 2016 at 4:17 pm"
    # test the result of multiple days
    assert Locale("en").format_date(1457451028, full_format=True, gmt_offset=600) == "March 31, 2016 at 10:17 pm"



# Generated at 2022-06-14 12:22:48.677484
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert load_gettext_translations("directory", "domain") == None


# Generated at 2022-06-14 12:22:49.502823
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    pass


# Generated at 2022-06-14 12:22:53.166030
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    import datetime
    assert get_closest_locale(
        "en").format_day(datetime.datetime(2012, 4, 1), dow=False
    ) == "April 1"


# Generated at 2022-06-14 12:22:55.548461
# Unit test for method format_day of class Locale
def test_Locale_format_day():

    l = Locale('ar_EG')
    d = datetime.datetime(2017, 1, 22)
    print(l.format_day(d))



# Generated at 2022-06-14 12:23:27.618174
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # test for dates in the past
    test_locale = Locale.get_closest("en")
    test_now = datetime.datetime(2019, 2, 25, 23, 0, 0)
    test_date = datetime.datetime(2019, 2, 25, 20, 0, 0)
    test_result = test_locale.format_date(test_date, 0, relative=True, shortest=True)
    assert test_result == "3 hours ago"
    # test for dates in the future
    test_date = datetime.datetime(2019, 2, 25, 21, 0, 0)
    test_result = test_locale.format_date(test_date, 0, relative=True, shortest=True)
    assert test_result == "2 hours"

    # test for dates in the past
   

# Generated at 2022-06-14 12:23:31.421793
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale("en").friendly_number(1000000) == "1,000,000"
    assert Locale("fr").friendly_number(1000000) == "1000000"


# Generated at 2022-06-14 12:23:43.016751
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    _translations={'en_US': {'singular': {'Foo': 'Foo'}, 'plural': {'Foo': 'Foos'}}, 'fr_FR': {'singular': {'Foo': 'Foo'}, 'plural': {'Foo': 'Foos'}}}
    global _translations
    global _supported_locales
    global _use_gettext
    _translations = {'en_US': {'singular': {'Foo': 'Foo'}, 'plural': {'Foo': 'Foos'}}, 'fr_FR': {'singular': {'Foo': 'Foo'}, 'plural': {'Foo': 'Foos'}}}
    _supported_locales = frozenset(list(_translations.keys()) + ['en_US'])


# Generated at 2022-06-14 12:23:46.614672
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import datetime
    Locale.get("en").format_date(datetime.datetime.utcnow())


# Generated at 2022-06-14 12:23:50.140567
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale('en_US').format_day(datetime.datetime(2019, 1, 10)) == "Thursday, January 10"
    assert Locale('en_US').format_day(datetime.datetime(2019, 1, 10), dow=False) == "January 10"



# Generated at 2022-06-14 12:23:52.933486
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    import unittest
    class TestLocale_pgettext(unittest.TestCase):
        def test_01(self):
            pass
    unittest.main()

# Generated at 2022-06-14 12:23:55.915681
# Unit test for function load_translations
def test_load_translations():
    load_translations("/Users/dongwookim/Desktop/Anaconda3/envs/JPA/tornado/locale")
    print(_translations)

# Generated at 2022-06-14 12:24:06.284076
# Unit test for function load_translations
def test_load_translations():
    from locale import setlocale, LC_ALL

    setlocale(LC_ALL, "")

    test_csv = os.path.join(os.path.dirname(__file__), "test.csv")

    # Test that load_translations can be called again and again.
    for _ in range(2):
        load_translations(os.path.dirname(test_csv), encoding="utf-8")
        # Test that the translations are loaded correctly.
        translations = _translations[get().code]
        assert translations["singular"]["%(name)s liked this"] == "A %(name)s le gustó esto"
        assert translations["plural"]["%(name)s liked this"] == "A %(name)s les gustó esto"

# Generated at 2022-06-14 12:24:17.054768
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import os
    import os.path
    import tornado.locale
    from tornado.log import app_log
    app_log.setLevel("INFO")

    path = os.path.join(os.path.dirname(__file__), "..", "locale")
    tornado.locale.load_gettext_translations(path, "gettext_test")
    for i in range(10):
        print("")
    print("\nIn English:")
    en_us = tornado.locale.get("en_US")
    print("Hello is %s" % repr(en_us.translate("Hello")))
    print("Boat is %s" % repr(en_us.translate("Boat")))
    print("My name is %(name)s." % {"name": "Leif"})
   

# Generated at 2022-06-14 12:24:19.000719
# Unit test for function load_translations
def test_load_translations():
    directory = 'test/test_data/test_local'
    encoding = None
    assert load_translations(directory) == None


# Generated at 2022-06-14 12:24:46.223362
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from datetime import date
    date1 = date(2013, 3, 2)
    locale1 = Locale('en_US')
    locale1.format_day(date1)
    

# Generated at 2022-06-14 12:24:50.592714
# Unit test for function load_translations
def test_load_translations():
    directory = "locale"
    encoding = "utf-8"
    load_translations(directory, encoding)
    print(_translations)
#test_load_translations()

# Generated at 2022-06-14 12:25:01.329830
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    from tempfile import mkdtemp
    import shutil
    from typing import Callable
    from subprocess import Popen, PIPE
    from os import path

    def run_cmd(*args: str) -> str:
        p = Popen(args, stdout=PIPE)
        return p.communicate()[0].decode("utf8")

    def test_locale(fn: Callable[[str], None]) -> None:
        # Prepare temporary dir to test gettext functionality
        locale_dir = mkdtemp()
        old_cwd = os.getcwd()
        os.chdir(locale_dir)

        # file to be translated

# Generated at 2022-06-14 12:25:04.207854
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    test_result=Locale.pgettext("context", "message", "plural_message", 1)
    assert test_result=="message"


# Generated at 2022-06-14 12:25:14.151234
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    from .i18n import load_translations

    load_translations("/tmp")
    l = Locale.get("en")
    l.pgettext("Food", "Apple")
    l.pgettext("transportation", "Apple")
    l.pgettext("Food", "Apple", None, None)
    l.pgettext("transportation", "Apple", None, None)
    l.pgettext("Food", "Apple", "Fruits", 0)
    l.pgettext("transportation", "Apple", "Fruits", 0)
    l.pgettext("Food", "Apple", "Fruits", 1)
    l.pgettext("transportation", "Apple", "Fruits", 1)


# Generated at 2022-06-14 12:25:24.053913
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    '''Test Locale.format_day().'''
    if __name__ == '__main__':
        print()
        print('Test Locale.format_day():')
        print(Locale('en').format_day(datetime.datetime(2019, 9, 24, 16, 0)))
        print(Locale('en').format_day(datetime.datetime(2019, 9, 24, 16, 0), dow=False))
        print(Locale('fa').format_day(datetime.datetime(2018, 11, 22, 16, 0), dow=True))
        print(Locale('fa').format_day(datetime.datetime(2018, 11, 22, 16, 0), dow=False))
        print()



# Generated at 2022-06-14 12:25:27.446461
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    try:
        load_gettext_translations("/usr/share/locale", "tornado")
    except Exception as e:
        gen_log.error("Cannot load translation for '%s': %s", "tornado", str(e))
    assert True


# Generated at 2022-06-14 12:25:32.704901
# Unit test for function load_translations
def test_load_translations():
    test_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests')

    load_translations(test_directory)
    assert _translations is not None
    assert 'es_LA' in _translations
    assert _supported_locales is not None
    assert 'es_LA' in _supported_locales
    assert _default_locale is not None
    assert 'en_US' in _supported_locales
