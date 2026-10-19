

# Generated at 2022-06-14 12:16:26.983414
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    _ = GettextLocale("en_US", gettext.NullTranslations()).pgettext

    assert _("law", "right") == "right"
    assert _("good", "right") == "right"

    clubs = []
    assert _("stick", "club", "clubs", len(clubs)) == "club"
    clubs = ["one"]
    assert _("stick", "club", "clubs", len(clubs)) == "club"
    clubs = ["one", "two"]
    assert _("stick", "club", "clubs", len(clubs)) == "clubs"



# Generated at 2022-06-14 12:16:37.498106
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    for code in tuple(_supported_locales):
        if code in ('vi'):
            print('\n{} tests skipped (https://github.com/tornadoweb/tornado/issues/3708)'.format(code))
            continue
        locale = get_closest(code)
        print('\n{}'.format(code))
        print(locale.format_date(datetime.datetime.utcnow() - datetime.timedelta(minutes=2)))
        print(locale.format_date(datetime.datetime.utcnow() - datetime.timedelta(hours=2)))
        print(locale.format_date(datetime.datetime.utcnow() - datetime.timedelta(days=2)))

test_Locale_format_date()


# Generated at 2022-06-14 12:16:46.091425
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    '''
    >>> Locale.get('en').friendly_number(10)
    '10'
    >>> Locale.get('en').friendly_number(10000)
    '10,000'
    >>> Locale.get('en').friendly_number(1000000)
    '1,000,000'
    >>> Locale.get('es').friendly_number(10)
    '10'
    >>> Locale.get('ja').friendly_number(10)
    '10'
    '''
    pass



# Generated at 2022-06-14 12:16:48.292716
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    directory = "languages"
    domain = "tornado"
    load_gettext_translations(directory, domain)
    print(_translations)
    assert _translations != {}
    assert _use_gettext == True
    assert _supported_locales == frozenset(list(_translations.keys()) + [_default_locale])


# Generated at 2022-06-14 12:16:50.624653
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    local = Locale.get("fa_IR")
    assert local.format_day(datetime.datetime(2020, 6, 22)) == "شنبه، ژوئن 22"
    assert local.format_day(datetime.datetime(2020, 6, 22), dow=False) == "ژوئن 22"



# Generated at 2022-06-14 12:16:56.997979
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    class MyLocale(Locale):
        def translate(
            self,
            message: str,
            plural_message: Optional[str] = None,
            count: Optional[int] = None,
        ) -> str:
            if message == '1 new friend request':
                return '1 nieuw vriendschapsverzoek'
            elif message == '%(num)d new friend requests':
                return '%(num)d nieuwe vriendschapsverzoeken'
            elif message == 'You have %(num)d new friend requests':
                return 'U hebt %(num)d nieuwe vriendschapsverzoeken'
            else:
                return '???'


# Generated at 2022-06-14 12:17:03.813033
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get("es_MX")
    date = datetime.datetime(2020, 1, 21)
    assert locale.format_day(date, dow=False) == '21 de enero'
    assert locale.format_day(date) == 'martes, 21 de enero'
    locale = Locale.get("en_US")
    assert locale.format_day(date) == 'Tuesday, January 21'
    assert locale.format_day(date, dow=False) == 'January 21'
    locale = Locale.get("fa_IR")

# Generated at 2022-06-14 12:17:12.957511
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import datetime
    
    # make sure we have a log for the unit test
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    current_time = datetime.datetime.now()
    just_now = current_time - datetime.timedelta(seconds=15)
    one_minute_ago = current_time - datetime.timedelta(minutes=1)
    two_minutes_ago = current_time - datetime.timedelta(minutes=2)
    one_hour_ago = current_time - datetime.timedelta(hours=1)
    one_day_ago = current_time - datetime.timedelta(days=1)
    two_days_ago = current_time - datetime.timedelta(days=2)
    one_year_ago

# Generated at 2022-06-14 12:17:25.562903
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    date = datetime.datetime(2020, 3, 4, 16, 25)
    assert Locale("en").format_date(date) == "yesterday at 4:25 pm"
    assert Locale("en").format_date(date, gmt_offset=240) == "yesterday at 8:25 pm"
    assert Locale("en").format_date(date, gmt_offset=-120) == "yesterday at 2:25 pm"
    assert Locale("en").format_date(date, gmt_offset=-480) == "yesterday at 12:25 pm"
    assert Locale("en").format_date(date, gmt_offset=540) == "yesterday at 11:25 am"
    assert Locale("en").format_date(date, gmt_offset=-540) == "yesterday at 6:25 am"


# Generated at 2022-06-14 12:17:37.092934
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import glob
    import tempfile
    import shutil
    import subprocess
    import sys
    import os

    # Temporary output directory
    outdir = tempfile.mkdtemp("tornado_test_locale")

    # Create POT file from dummy Python code
    tmp_source = os.path.join(outdir, "file.py")
    with open(tmp_source, "w") as f:
        f.write("""
            #!/usr/bin/env python
            # -*- coding: utf-8 -*-

            def foo():
                print("bar")
                print("bar")

            foo()
        """)
    # Create PO file from POT file
    tmp_template = os.path.join(outdir, "file.pot")

# Generated at 2022-06-14 12:18:22.693373
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
	# get-text translation output
	assert Locale('en_US').pgettext('en_US', 'this is', 'this are') == 'this are'
	# CSV translates only the first argument
	assert Locale('en_US').pgettext('en_US', 'this is', 'this are') == 'this is'

# Generated at 2022-06-14 12:18:25.964688
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    # print("load_gettext_translations test start")
    load_gettext_translations("locale", "mydomain")
    # print("load_gettext_translations test complete")



# Generated at 2022-06-14 12:18:34.466892
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    import datetime
    locale = Locale.get("zh_CN")
    print( locale.format_day(datetime.datetime.utcnow(), gmt_offset=0))

# test_Locale_format_day()

#@classmethod
#def get_closest(cls, *locale_codes: str) -> "Locale":
#    """Returns the closest match for the given locale code."""
#    for code in locale_codes:
#        if not code:
#            continue
#        code = code.replace("-", "_")
#        parts = code.split("_")
#        if len(parts) > 2:
#            continue
#        elif len(parts) == 2:
#            code = parts[0].lower() + "_" + parts[1].upper()
#        if

# Generated at 2022-06-14 12:18:37.753250
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get("en")
    date = datetime.datetime(2019, 7, 31)
    assert locale.format_date(date) == "July 31, 2019"



# Generated at 2022-06-14 12:18:46.485559
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from datetime import datetime
    locale_codes = ["en", "fr", "fa"]
    for locale_code in locale_codes:
        if locale_code == "en":
            assert(
                Locale.get(locale_code).format_day(datetime(2018, 1, 2))
                == "Tuesday, January 2")
            assert(
                Locale.get(locale_code).format_day(datetime(2018, 1, 2), dow=False)
                == "January 2")
        if locale_code == "fr":
            assert(
                Locale.get(locale_code).format_day(datetime(2018, 1, 2))
                == "mardi 2 janvier")

# Generated at 2022-06-14 12:18:50.356330
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    import random
    import string
    random_string = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(6))
    assert len(Locale.get(random_string).pgettext(random_string, None))>0


# Generated at 2022-06-14 12:19:00.246262
# Unit test for method list of class Locale
def test_Locale_list():
    translator_instance_1 = CSVLocale("ar", {})
    translator_instance_2 = CSVLocale("ar_EG", {})
    translator_instance_3 = CSVLocale("ar_SA", {})
    translator_instance_4 = CSVLocale("de", {})
    translator_instance_5 = CSVLocale("de_AT", {})
    translator_instance_6 = CSVLocale("de_DE", {})
    translator_instance_7 = CSVLocale("en", {})
    translator_instance_8 = CSVLocale("en_US", {})
    
    assert translator_instance_1.list(["A","B","C"]) == 'A, B و C'
    assert translator_instance_2.list(["A","B","C"]) == 'A, B و C'
    assert translator_instance

# Generated at 2022-06-14 12:19:03.640213
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations(__path__[0],"tornado.locale")
    pass


# Generated at 2022-06-14 12:19:12.315171
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import os
    os.environ["LC_CTYPE"] = "zh_CN.UTF-8"
    #判断默认语言是否为‘zh_CN’
    #locale.getpreferredencoding(False)
    os.environ["LANG"] = "zh_CN.UTF8"
    os.environ["LC_TIME"] = "zh_CN.UTF-8"
    #print(os.environ.get('LANG'))
    #print(locale.getpreferredencoding(False))

    #判断默认语言是否为‘zh_CN’
    #print('./pt_BR/LC_MESSAGES/mydomain.mo')

    #print

# Generated at 2022-06-14 12:19:21.307733
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations(directory="/tmp/locale", domain="b_tornado_test")
    set_default_locale("en_US")
    assert get("en_US").translate("hello") == "hello"
    assert get("en_US").translate("hello world") == "hello world"
    set_default_locale("zh_CN")
    assert get("zh_CN").translate("hello") == "你好"
    assert get("zh_CN").translate("hello world") == "大家好"



# Generated at 2022-06-14 12:20:24.856438
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations("E:\PythonWorkSpace\locale", "tornado")

# Generated at 2022-06-14 12:20:34.913367
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    """Test the method pgettext of class Locale"""
    context = random.choice(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"])
    message = random.choice(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"])
    plural_message = random.choice(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"])
    count = random.randint(1,100)
    # Create the object
    obj = Locale("en")
    # Call the method
    result = obj.pgettext(context, message, plural_message, count)

# Generated at 2022-06-14 12:20:42.072984
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    class DummyLocale(Locale):
        def __init__(self, code):
            self.code = code
            self.months = ["jan", "feb", "march", "april", "may", "june", "july", "aug", "sept", "oct", "nov", "dec"]
            self.weekdays = ["mon", "tue", "wed", "th", "fri", "sat", "sun"]

        def translate(self, message, plural_message=None, count=None):
            if message == "%(month_name)s %(day)s":
                idx = int(count) - 1
                return self.months[idx] + " " + str(count)
            elif message == "%(month_name)s":
                idx = int(count) - 1
               

# Generated at 2022-06-14 12:20:52.213278
# Unit test for function load_translations
def test_load_translations():
    print('test_load_translations')
    directory_name = 'test_locale_data'
    def check_spanish(data):
        assert data == {
        'plural': {
            'I love you': 'Te amo',
            '%(name)s liked this': 'A %(name)s les gustó esto'
        },
        'singular': {
            'I love you': 'Te amo un montón',
            '%(name)s liked this': 'A %(name)s le gusta esto'
        },
        'unknown': {
            'I love you': 'Te quiero',
            '%(name)s liked this': 'A %(name)s le gusta, vamos'
        }
        }
    load_translations(directory_name)
   

# Generated at 2022-06-14 12:20:56.886337
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get("en_US")
    assert locale.format_day(datetime.datetime(2012, 7, 27)) == "Friday, July 27"
    assert locale.format_day(datetime.datetime(2012, 7, 27), dow=False) == "July 27"



# Generated at 2022-06-14 12:21:07.710582
# Unit test for function load_translations
def test_load_translations():
    import os
    import tempfile
    from tornado.util import b
    from tornado.locale import load_translations
    from tornado.testing import AsyncTestCase
    from tornado.util import raise_exc_info
    from tornado.testing import bind_unused_port
    def test_async(self):
        def handle_request(response):
            self.assertIn(b("A Christophe le gust\xc3\xb3 esto"), response.body)
        # Make sure that load_translations doesn't die if it's called twice
        # (since this used to cause a null-pointer exception with
        # Python's CSV module).
        with (tempfile.NamedTemporaryFile() if os.name == "nt" else
                  tempfile.NamedTemporaryFile(delete=False)) as f:
            name = f.name


# Generated at 2022-06-14 12:21:13.897491
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale.get("fr").format_day(datetime.datetime(2017, 5, 28)) == "dimanche, mai 28"
    assert Locale.get("fr").format_day(datetime.datetime(2017, 5, 28), dow=False) == "mai 28"
    print("method Locale.format_day(): OK")

test_Locale_format_day()


# Generated at 2022-06-14 12:21:25.765666
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    from datetime import datetime
    date = datetime.now()
    Locale.get('en').format_date(date)
    Locale.get('de').format_date(date)
    Locale.get('zh_CN').format_date(date)
    Locale.get('zh_CN').format_date(date, 1, False)
    Locale.get('zh_CN').format_date(date, 1, True, False, True)
    Locale.get('en').format_date(date, 1, False)
    Locale.get('en').format_date(date)
    Locale.get('en').format_date(date, 1, True)
    Locale.get('en').format_date(date, 1, True, False, True)

# Generated at 2022-06-14 12:21:35.950757
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    test_Locale = Locale("en")
    # Test if the code runs
    test_Locale.friendly_number(123456789)
    # Test if the method has no bugs
    assert test_Locale.friendly_number(123456789) == "123,456,789"
    # Test if the method handles small number
    assert test_Locale.friendly_number(1) == "1"
    # Test if the method handles zero
    assert test_Locale.friendly_number(0) == "0"
    # Test if the method handles negative numbers
    assert test_Locale.friendly_number(-123456789) == "-123,456,789"
    # Test if the method returns a string, also if the input is not a string

# Generated at 2022-06-14 12:21:39.686223
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale("es")
    date = datetime.datetime(2020, 8, 14)
    result = locale.format_day(date, dow=False)
    assert result == "14 de agosto"


# Generated at 2022-06-14 12:22:30.514010
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    import datetime
    l = Locale("en_US")
    date = datetime.datetime(2017,1,1)
    assert l.format_day(date) == "Sunday, January 1"
    assert l.format_day(date, dow=False) == "January 1"



# Generated at 2022-06-14 12:22:34.848468
# Unit test for function load_translations
def test_load_translations():
    translations = {
        "es_LA": {
            "plural": {
                "I love you": "Te amo",
                "%(name)s liked this": "A %(name)s les gustó esto",
            },
            "singular": {
                "%(name)s liked this": "A %(name)s le gustó esto",
            },
        }
    }
    load_translations("examples\\translation")
    assert _supported_locales == frozenset(list(translations.keys()) + [_default_locale])
    assert _translations == translations



# Generated at 2022-06-14 12:22:39.314596
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    from io import StringIO
    from tornado.escape import utf8
    from tornado.util import unicode_type
    def t(message, plural_message=None, count=None):
        return unicode_type (message)
    def load_translations(translations):
        for k, v in translations.items():
            translations[k] = dict(((k, utf8(v)) for k, v in v.items()))
        return translations

# Generated at 2022-06-14 12:22:49.789204
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    assert CSVLocale('en').format_date(0.0) == u"1 second ago"
    assert CSVLocale('en').format_date(time.time()) == u"1 second ago"
    assert CSVLocale('en').format_date(1507390591.0) == u"yesterday"
    assert CSVLocale('en').format_date(1516473791.0) == u"Monday, January 22, 2018 at 3:46 pm"
    assert CSVLocale('zh_CN').format_date(1507390591.0, full_format=True) == u"2017\u5e7404\u670829\u65e5"

# Generated at 2022-06-14 12:23:00.146425
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    """ This function tests the method format_date for class Locale for the following input(s):
            test_set_1 - accepts a single argument and calls the function with that argument.
            test_set_2 - accepts 3 arguments and calls the function with all 3 of them.
            test_set_3 - accepts 4 arguments and calls the function with all 4 of them.
            test_set_4 - accepts 4 arguments and calls the function with all 4 of them.
            test_set_5 - accepts 4 arguments and calls the function with all 4 of them.
            test_set_6 - accepts 4 arguments and calls the function with all 4 of them.
    """
    def test_set_1(test_set_1_arg_1):
        # Load the CSVTranslations files
        load_translations(os.path.join(DATA_PATH, "translations"))


# Generated at 2022-06-14 12:23:12.316339
# Unit test for function load_translations
def test_load_translations():
    directory = '.'
    encoding = 'utf-8'

    _translations = {}
    for path in os.listdir(directory):
        if not path.endswith(".csv"):
            continue
        locale, extension = path.split(".")
        if not re.match("[a-z]+(_[A-Z]+)?$", locale):
            gen_log.error(
                "Unrecognized locale %r (path: %s)",
                locale,
                os.path.join(directory, path),
            )
            continue
        full_path = os.path.join(directory, path)

# Generated at 2022-06-14 12:23:13.222882
# Unit test for function load_translations
def test_load_translations():
    assert _translations
    return True


# Generated at 2022-06-14 12:23:22.278459
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    """Unit tests of the method format_date of the class Locale """

    assert Locale("en_US").format_date(
        datetime.datetime.utcnow() + datetime.timedelta(minutes=10), relative=False
    ) == "Tuesday, January 1, 2019 at 12:00 AM"
    assert Locale("zh_CN").format_date(
        datetime.datetime.utcnow() + datetime.timedelta(minutes=10), relative=False
    ) == "2019\u5e741\u67081\u65e5\u51c0\u65f6"
    assert Locale("en_US").format_date(
        datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
        full_format=True
    )

# Generated at 2022-06-14 12:23:24.117503
# Unit test for function load_translations
def test_load_translations():
    load_translations('test_locale_data')
test_load_translations()



# Generated at 2022-06-14 12:23:31.723327
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import tempfile
    import os
    import shutil
    import tornado.testing
    import tornado.locale
    import tornado.httputil

    import tornado.httpserver

    # where is the test file
    current_path = os.path.dirname(__file__)
    test_path = os.path.split(current_path)[0]

    # remove the test directory
    tmp_path = test_path + '/tmp'
    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)

    # set up the test directory
    # tornado.locale.load_gettext_translations() looks for files in this directory
    # with this format:
    # {directory}/{lang}/LC_MESSAGES/{domain}.mo

# Generated at 2022-06-14 12:24:16.204870
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    #test
    en = Locale.get("en")
    german = Locale.get("de")
    
    d = datetime.datetime(2018,3,14,12,30)
    assert en.format_day(d,dow=False) == "March 14"
    assert german.format_day(d,dow=False) == "14. März"
    
    assert en.format_day(d) == "Wednesday, March 14"
    assert german.format_day(d) == "Mittwoch, 14. März"

# Generated at 2022-06-14 12:24:28.092100
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import time

    def translate(message:str, plural_message:Optional[str]=None, count:Optional[int]=None)->str:
        return message
    
    loc_obj = Locale('en')
    loc_obj.translate = translate
    date_string_actual = loc_obj.format_date(time.time())
    date_string_expected = '2 hours ago'
    assert date_string_actual == date_string_expected, "test_Locale_format_date 1"

    date = datetime.datetime.utcnow()
    date_string_actual = loc_obj.format_date(date)
    date_string_expected = '1 second ago'
    assert date_string_actual == date_string_expected, "test_Locale_format_date 2"

    date_string_actual = loc

# Generated at 2022-06-14 12:24:32.138054
# Unit test for function load_translations
def test_load_translations():
    assert(_supported_locales == frozenset([_default_locale]))
    set_default_locale("en_US")
    load_translations(".")
    results = get("en_US")
    assert(isinstance(results, Locale))



# Generated at 2022-06-14 12:24:43.104482
# Unit test for function load_gettext_translations

# Generated at 2022-06-14 12:24:47.523010
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    base_dir = os.path.dirname(__file__)
    test_files_dir = os.path.join(base_dir, "testfiles")
    load_gettext_translations(test_files_dir, "tornado")

    assert _use_gettext == True
    assert _translations
    assert _supported_locales


# type: (str, str) -> None # No support for typing recursive types in py3

# Generated at 2022-06-14 12:24:59.214341
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from datetime import datetime
    # Test Locale class in english language
    locale = Locale.get("en_US")
    date = datetime.now()
    # Test day of week with GMT plus 5:30
    dow = locale.format_day(date, 330, True)
    assert dow != None
    # Test day of week without day of week
    dow = locale.format_day(date, 330, False)
    assert dow != None
    # Test day of week with GMT plus 6:30
    dow = locale.format_day(date, 390, True)
    assert dow != None
    # Test day of week without day of week
    dow = locale.format_day(date, 390, False)
    assert dow != None
    # Test day of week with GMT plus 13

# Generated at 2022-06-14 12:25:04.295309
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    from zulip.tests import stubs

    with stubs.attrs_override(locale.getdefaultlocale, lambda: ('en', 'UTF-8')):
        l = Locale.get('en')
        assert l.friendly_number(123) == "123"
        assert l.friendly_number(12345) == "12,345"
        assert l.friendly_number(123456) == "123,456"



# Generated at 2022-06-14 12:25:13.234117
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert (Locale.get("de").format_day(datetime.datetime(2012, 7, 10)) == u"Dienstag, Juli 10")
    assert (Locale.get("en").format_day(datetime.datetime(2012, 7, 10)) == u"Tuesday, July 10")
    assert (Locale.get("en").format_day(datetime.datetime(2012, 7, 10),dow=False) == u"July 10")
    assert (Locale.get("en").format_day(datetime.datetime(2012, 7, 10),dow=True) == u"Tuesday, July 10")



# Generated at 2022-06-14 12:25:23.811580
# Unit test for method list of class Locale
def test_Locale_list():
    # get_closest()
    assert Locale.get_closest("zh_CN") == Locale("zh_CN")
    assert Locale.get_closest("es") == Locale("es")

    # list()
    assert (
        Locale("en").list(["A", "B", "C"])
        == Locale("en").list(["A", "B", "C"])
        == "A, B, and C"
    )
    assert Locale("en").list(["A", "B"]) == "A and B"
    assert Locale("en").list(["A"]) == "A"
    assert Locale("en").list([]) == ""

# Generated at 2022-06-14 12:25:24.755817
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    pass

import unittest
