

# Generated at 2022-06-14 12:16:36.176710
# Unit test for function load_translations
def test_load_translations():
    # 加载本地语言文件
    load_translations("/Users/jianzhuang/Desktop/Tornado/locale", encoding=None)
    # 获取中文简体翻译
    zh = get("zh_CN")
    assert zh.translate("Sign in") == "登录"
    assert zh.translate("Sign out") == "注销"



# Generated at 2022-06-14 12:16:37.742394
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    print("[TEST] hello")
    load_gettext_translations("locale", "spam")


# Generated at 2022-06-14 12:16:42.299066
# Unit test for function load_translations
def test_load_translations():
    test_csv = 'my_test.csv'
    open(test_csv,"a").close()
    f = open(test_csv,'w')
    f.write("\"I love you\",\"Te amo\"\n")
    f.write("\"%(name)s liked this\",\"A %(name)s les gustó esto\",\"plural\"\n")
    f.write("\"%(name)s liked this\",\"A %(name)s le gustó esto\",\"singular\"")
    f.close()
    load_translations(os.path.dirname(os.path.realpath(__file__)), "utf-8")

# Generated at 2022-06-14 12:16:47.389331
# Unit test for function load_translations
def test_load_translations():
    import _locale_data
    _locale_data._translations = _locale_data._translations_default.copy()
    _locale_data.load_translations("/home/sfw/Users/sharif/work/tornado_test/tornado/locale/locale")
    print(_locale_data._translations)
    # test_load_translations()



# Generated at 2022-06-14 12:16:51.320731
# Unit test for function load_translations
def test_load_translations():
    directory = 'translations'
    for path in os.listdir(directory):
        print (path)

test_load_translations()


# Generated at 2022-06-14 12:16:52.336606
# Unit test for function load_translations
def test_load_translations():
    file = 'test.csv'
    load_translations(file)


# Generated at 2022-06-14 12:16:53.202634
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert 1==1


# Generated at 2022-06-14 12:16:58.122643
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations(os.getcwd()+"/tornado/_locale/", "tornado")
    assert _translations == {}
    assert _support_locales == {'en_US'}
    assert _use_gettext
    assert gen_log.debug("Supported locales: %s", sorted(_supported_locales)) == None

test_load_gettext_translations()


# Generated at 2022-06-14 12:17:01.790061
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    assert Locale.get('pt_BR').format_date(datetime.datetime.utcnow()) == str(datetime.datetime.today())



# Generated at 2022-06-14 12:17:06.309649
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    try:
        os.stat("/usr/share/locale")
    except OSError:
        return True
    load_gettext_translations("/usr/share/locale", "tornado")
    return len(_translations) > 0



# Generated at 2022-06-14 12:17:27.443706
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    from pytest import raises
    from tornado.util import u
    from . import translate
    import unittest
    if not (hasattr(unittest.TestCase, "assertRegex")):
        unittest.TestCase.assertRegex = unittest.TestCase.assertRegexpMatches

    with raises(NotImplementedError):
        (Locale(code="af")).pgettext(
            context="af",
            message="af",
            plural_message="af",
            count=1,
        )



# Generated at 2022-06-14 12:17:30.140776
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    test_model = Locale.pgettext
    assert test_model == None, "The test case has not been implemented."



# Generated at 2022-06-14 12:17:38.361472
# Unit test for function load_translations
def test_load_translations():
    directory = "/Users/tingyuanwang/Documents/GitHub/autotest/tornado_autotest/test_tornado/test_locale.py"
    load_translations(directory)
    _translations1 = {}
    _translations1["en_US"] = {}
    _translations1["en_US"]["singular"] = {"Hello,": "yoyo"}
    _translations1["en_US"]["plural"] = {"Hello,": "yoyo"}
    assert _translations == _translations1


# Generated at 2022-06-14 12:17:46.625201
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    date = datetime.datetime(2012, 5, 9, 18, 40)
    now = datetime.datetime(2012, 5, 9, 21, 23)
    yesterday = datetime.datetime(2012, 5, 8, 9, 27)
    assert Locale("en").format_date(now, now) == "just now"
    assert Locale("en").format_date(yesterday, now) == "yesterday"
    assert Locale("en").format_date(date, now) == "Wednesday"
    assert Locale("en").format_date(date, now, full_format=True) == "Wednesday at 6:40pm"
    assert Locale("en").format_date(date, now, relative=False) == "May 9, 2012 at 6:40pm"

# Generated at 2022-06-14 12:17:52.846244
# Unit test for function load_translations
def test_load_translations():
    print ("Test load_translations")
    directory = '.'
    encoding = 'utf-8'
    load_translations(directory,encoding)
    for path in os.listdir(directory):
        if not path.endswith(".csv"):
            continue
        locale, extension = path.split(".")
        print ("locale: %s, extension: %s" % (locale, extension))


# Generated at 2022-06-14 12:18:03.268911
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # Test 1: Check if gmt offset is implemented properly
    locale = Locale.get("en_US")
    date1 = datetime.datetime(2011, 1, 1, 0, 0, 0)
    date2 = datetime.datetime(2011, 1, 1, 0, 0, 0)
    assert locale.format_day(date1, 0) == locale.format_day(date2, 120)
    assert locale.format_day(date1, 0) == "Saturday, January 1"

    # Test 2: Check if parameter dow is properly implemented
    locale = Locale.get("en_US")
    assert locale.format_day(date1, 0, False) == "January 1"

    # Test 3: Check if Day of Week and Month name is correct
    locale = Locale.get("fa_IR")
    date1

# Generated at 2022-06-14 12:18:15.633536
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    def test_date(shorter: bool = False, full_format: bool = False) -> bool:
        """
        Will be run for each supported locale
        """
        assert isinstance(shorter,bool)
        assert isinstance(full_format,bool)
        date = datetime.datetime.utcnow()
        formatted = get_closest_locale("en").format_date(date, relative=True, shorter=shorter, full_format=full_format)
        n = datetime.datetime.strptime("%s/12/1994 %d:%d" % (date.day, date.hour, date.minute), "%m/%d/%Y %H:%M")

# Generated at 2022-06-14 12:18:26.701917
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """
    Unit test for method Locale.format_day
    """
    import test_utils as t
    import test_utils as t
    
    t.set_up_locale()
    en_locale = Locale.get_closest("en")
    date1 = datetime.datetime(2019, 1, 1)
    date2 = datetime.datetime(2019, 1, 2)
    date3 = datetime.datetime(2019, 1, 3)
    date4 = datetime.datetime(2019, 1, 4)
    date5 = datetime.datetime(2019, 1, 5)
    date6 = datetime.datetime(2019, 1, 6)
    date7 = datetime.datetime(2019, 1, 7)

# Generated at 2022-06-14 12:18:34.959531
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get("en").friendly_number(1234567) == "1,234,567"
    assert Locale.get("en").friendly_number(1234) == "1,234"
    assert Locale.get("en").friendly_number(1000) == "1,000"
    assert Locale.get("en").friendly_number(100) == "100"
    assert Locale.get("en").friendly_number(1) == "1"

    assert Locale.get("en").friendly_number(0) == "0"
    assert Locale.get("en").friendly_number(-1) == "-1"
    assert Locale.get("en").friendly_number(-1234) == "-1,234"

    assert Locale.get("en").friendly_number(123.456) == "123.456"


# Generated at 2022-06-14 12:18:37.705001
# Unit test for method list of class Locale
def test_Locale_list():
    """Test for the Locale method list"""
    list_arg = [1,2,3]
    assert Locale.list(list_arg) == '1, 2, and 3'

# Generated at 2022-06-14 12:18:55.589299
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import datetime

    test_date_list = [0, 0.001, 0.9, 1.0, 2, 59, 60, 61, 120, 121, 1199, 1200, 3600, 7200]

    print("Testing  format_date  of class Locale")
    print("Tested date list is as follows: ")
    print(test_date_list)
    today = datetime.datetime.now()
    en_locale = Locale.get("en")
    zh_locale = Locale.get("zh_CN")
    for date in test_date_list:
        str_1 = en_locale.format_date(date)
        str_2 = en_locale.format_date(date, relative=False)

# Generated at 2022-06-14 12:18:58.952058
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    l = Locale.get("en_US")
    now = datetime.datetime.utcnow()
    print(l.format_day(now, 0, True))
    print(l.format_day(now, 0, False))



# Generated at 2022-06-14 12:19:11.022276
# Unit test for function load_translations
def test_load_translations():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.httpclient import AsyncHTTPClient
    from tornado.web import Application, RequestHandler
    from tornado import gen

    def _translations_callback(response):
        assert response.error is None
        assert response.code == 200
        assert "text/csv" in response.headers["Content-Type"]
        assert response.body == b"\"Hello, world!\",\"Bonjour tout le monde!\"\r\n"

    def _locale_callback(response):
        assert response.error is None
        assert response.code == 200
        assert response.body == b"Bonjour tout le monde!"


# Generated at 2022-06-14 12:19:23.405232
# Unit test for function load_translations
def test_load_translations():
  import locale
  import tornado.testing
  from tornado.platform.asyncio import AsyncIOMainLoop
  AsyncIOMainLoop().install()
  from tornado.platform.asyncio import to_asyncio_future
  import asyncio
  import tornado.ioloop
  import tornado.web
  import tornado.gen
  import time
  import re
  import tempfile

  @tornado.gen.coroutine
  def test_locale():
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    with tempfile.TemporaryDirectory() as tempdir:
      with open(os.path.join(tempdir, "es_LA.csv"), "w") as f:
        f.write(u'"I love you","Te amo"\n')
        f.write

# Generated at 2022-06-14 12:19:28.794108
# Unit test for function load_translations
def test_load_translations():
    print("testing load_translations")
    class Dummy:
        pass
    dum = Dummy()
    dum.listdir = lambda x: ["en_US.csv"]
    dum.open = lambda x: ["Singular,Singular", "Plural,Plural", "Unknown,Unknown"]
    load_translations("./", dum)  # type: ignore
    if _translations["en_US"]["plural"]["Plural"] == "Plural" and _translations["en_US"]["singular"]["Singular"] == "Singular" and _translations["en_US"]["unknown"]["Unknown"] == "Unknown":
        print("PASS")
    else:
        print("FAIL")



# Generated at 2022-06-14 12:19:36.266057
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # test Locale format_date
    # testcase 1
    locale = get_closest_locale('en')
    date = datetime.datetime(2018, 4, 1, 20, 15, 0)
    print(locale.format_date(date))
    # testcase 2
    date = datetime.datetime(2018, 3, 31, 9, 0, 0)
    print(locale.format_date(date))
    # testcase 3
    date = datetime.datetime(2018, 3, 30, 9, 0, 0)
    print(locale.format_date(date))
    # testcase 4
    date = datetime.datetime(2018, 3, 29, 19, 15, 0)
    print(locale.format_date(date))
    # testcase 5
    date = datetime

# Generated at 2022-06-14 12:19:40.303396
# Unit test for function load_translations
def test_load_translations():
    def setUp():
        pass

    def test_load_translations():

        # test load_translations()
        input_csv_dir = "translations_dir/es_LA.csv"
        load_translations(input_csv_dir)

    test_load_translations()



# Generated at 2022-06-14 12:19:52.229114
# Unit test for method translate of class CSVLocale

# Generated at 2022-06-14 12:19:57.158529
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    # 当前目录
    i = os.path.dirname(os.path.abspath(__file__))
    # 测试文件夹
    files = os.path.join(i, "locale")
    # 域
    domain = "test_domain"
    load_gettext_translations(files, domain)
    _test_gettext_lang = _translations



# Generated at 2022-06-14 12:20:07.834551
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    from datetime import date
    from dateutil.tz import tzoffset
    loc = Locale.get('en_US')
    dt = date(2015, 4, 3)
    assert loc.format_day(dt) == 'Friday, April 3'
    dt = date(2015, 4, 4)
    assert loc.format_day(dt) == 'Saturday, April 4'
    loc = Locale.get('fr')
    assert loc.format_day(dt) == 'samedi 4 avril'
    dt = date(2015, 4, 5)
    assert loc.format_day(dt) == 'dimanche 5 avril'
    dt = date(2015, 4, 6)
    assert loc.format_day(dt) == 'lundi 6 avril'

# Generated at 2022-06-14 12:20:41.755857
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    assert(Locale.get("en").format_date(datetime.datetime.utcnow()) == \
           'now')
    assert(Locale.get("en").format_date(0) == \
          'Dec 31, 1969')
    assert(Locale.get("en").format_date(86400) == \
          'Jan 1, 1970')
    assert(Locale.get("en").format_date(86400,relative=False) == \
          'Jan 1, 1970')
    assert(Locale.get("en").format_date(86400,full_format=True) == \
          'Jan 1, 1970 at 12:00 am')
    assert(Locale.get("en").format_date(86400,shorter=True) == \
          'Jan 1')

# Generated at 2022-06-14 12:20:51.999163
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    domain = 'mydomain'
    directory = 'locale'
    if not os.path.exists(directory):
        os.mkdir(directory)
    lang = 'zh_CN'
    locale_dir = os.path.join(directory, lang, 'LC_MESSAGES')
    if not os.path.exists(locale_dir):
        os.makedirs(locale_dir)
    mo_file = os.path.join(locale_dir, domain+'.mo')

# Generated at 2022-06-14 12:20:55.588713
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    expected = "2 minutes ago"
    actual = Locale.get("en").pgettext("pgettext", u"%(seconds)d seconds ago", count = 2)
    assert actual == expected



# Generated at 2022-06-14 12:20:57.470614
# Unit test for function load_translations
def test_load_translations():
    load_translations("./locale",encoding='utf-8')
    
    

# Generated at 2022-06-14 12:21:08.445648
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():
    class TestTranslations(gettext.NullTranslations):
        def gettext(self_, message):
            translations = {
                "right": "право",
                "club": "клуб",
                "stick": "палка",
                "organization": "организация",
            }
            return translations.get(message, message)


# Generated at 2022-06-14 12:21:17.990848
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    global _translations
    _translations = {}
    global _supported_locales
    _supported_locales = frozenset([_default_locale])
    global _use_gettext
    _use_gettext = False
    my_translation_locale = {"plural": {"message": "messages"}, "singular": {}}
    my_translation_locale["singular"]["\u0420\u0443\u0441\u0441\u043a\u0438\u0439"] = (
        "russian"
    )
    my_translation_locale["singular"]["English"] = "english"
    my_translation_locale["singular"]["\u0627\u0644\u0639\u0631\u0628\u064a\u0629"]

# Generated at 2022-06-14 12:21:20.373449
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    dir = "locale"
    domain = "mydomain"
    load_gettext_translations(dir, domain)
    assert _translations != None



# Generated at 2022-06-14 12:21:26.496285
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """
    Uses the date - March 22, 2013 to test against.
    """
    date = datetime.datetime(2013, 3, 22)
    time_zone = time.timezone
    locale = Locale.get_closest(time_zone)
    result = locale.format_day(date)
    assert result == "Friday, March 22"
    

# Generated at 2022-06-14 12:21:28.253322
# Unit test for function load_translations
def test_load_translations():
    # TODO: implement me.
    pass



# Generated at 2022-06-14 12:21:30.265941
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    gen_log.warning("TESTING: load_gettext_translations in the DIRECTORY")


# Generated at 2022-06-14 12:22:02.883525
# Unit test for function load_translations
def test_load_translations():

    import tempfile
    import os
    import shutil

    dir_path = tempfile.mkdtemp()

    csvfile = os.path.join(dir_path, "testcsv.csv")
    with open(csvfile, "w") as f:
        f.write('"I love you","Ich habe dich lieb"\n')
        f.write('"%(name)s liked this","%(name)s mochte das","plural"\n')
        f.write('"%(name)s liked this","%(name)s mochte das","singular"\n')

    load_translations(dir_path)

    shutil.rmtree(dir_path)


_eol_message_re = re.compile(r"\r?\n")



# Generated at 2022-06-14 12:22:06.798924
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    assert CSVLocale.translate("This is a test!") == "This is a test!"
    assert CSVLocale.translate("This is a test!", count=1) == "This is a test!"
    assert CSVLocale.translate("This is a test!", plural_message="These are tests!", count=2) == "These are tests!"
    assert CSVLocale.translate("This is a test!", plural_message="These are tests!", count=1) == "This is a test!"
    assert CSVLocale.translate("This is a test!", plural_message="These are tests!", count=0) == "These are tests!"

# Generated at 2022-06-14 12:22:09.450673
# Unit test for method format_day of class Locale
def test_Locale_format_day(): 
    x = Locale.get("en")
    x.format_day(datetime.datetime(2018, 10, 1))

# Generated at 2022-06-14 12:22:14.639394
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    locale = Locale.get("fa_IR")
    date = datetime.datetime(2020, 8, 12, 23, 59, 59, tzinfo=pytz.UTC)
    formatted_day = locale.format_day(date)
    assert formatted_day == "اسفند، آگوست 12"



# Generated at 2022-06-14 12:22:22.081832
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # case 1 (day of week not specified):
    # expected result:
    # "January 22"
    assert Locale("en").format_day(datetime.datetime(2016, 1, 22), dow=False) == \
        "January 22"
    # case 2 (day of week specified):
    # expected result:
    # "Thursday, January 22"
    assert Locale("en").format_day(datetime.datetime(2016, 1, 22), dow=True) == \
        "Thursday, January 22"



# Generated at 2022-06-14 12:22:33.231031
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    """
    This function helps in verifying the case of function format_date
    """
    try:
        # To test the case when input datetime is in past
        locale_obj = Locale('en')
        assert locale_obj.format_date(datetime.datetime(2020,5,5,5,5)) == "yesterday"
        
        # To test the case when input datetime is in future
        assert locale_obj.format_date(datetime.datetime(2021,5,5,5,5),relative = False) == "May 5, 2021 at 5:05 pm"

        #To test the case when input datetime is same as current datetime
        assert locale_obj.format_date(datetime.datetime.now()) == "1 second ago"
    except Exception:
        print("One of the test cases failed")


# Generated at 2022-06-14 12:22:45.528994
# Unit test for function load_translations
def test_load_translations():
    if not os.path.exists("tests/locale"):
        os.makedirs("tests/locale")
    # Note, there is no BOM
    with open("tests/locale/en_US.csv", "w") as fd:
        fd.write('"I love you","Te amo"\n')
        fd.write('"%(name)s liked this","A %(name)s les gustó esto","plural"\n')
        fd.write('"%(name)s liked this","A %(name)s le gustó esto","singular"\n')
        fd.flush()

    load_translations("tests/locale", encoding="utf-8")
    assert len(_translations) == 1
    print(repr(_translations))
    assert _trans

# Generated at 2022-06-14 12:22:55.902916
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    l = Locale.get_closest("en_US")
    l.format_date(-2) == "2 seconds ago"
    l.format_date(-25) == "25 seconds ago"
    l.format_date(-500) == "8 minutes ago"
    l.format_date(-5000) == "1 hour ago"
    l.format_date(-35000) == "9 hours ago"
    l.format_date(-40000) == "yesterday"
    l.format_date(-50000) == "yesterday"
    l.format_date(-60 * 60 * 24) == "yesterday"
    l.format_date(-60 * 60 * 24 * 2) == "yesterday"
    l.format_date(-60 * 60 * 24 * 3) == "yesterday"

# Generated at 2022-06-14 12:22:57.744064
# Unit test for function load_translations
def test_load_translations():
    load_translations('./tornado/locale/')
    print(_translations)
    print(_supported_locales)


# Generated at 2022-06-14 12:23:07.062346
# Unit test for function load_translations
def test_load_translations():
	load_translations("test/test_loadtranslations.csv")
	assert Locale.get_closest("me").translate("I love you") == "我爱你"
	assert Locale.get_closest("me").translate("%(name)s liked this") == "喜欢这个"
	assert Locale.get_closest("me").translate("%(name)s liked this", "%(name)s liked this", 2) == "喜欢这个"

# test_load_translations()


# Generated at 2022-06-14 12:24:04.948783
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    translation = {
        "trans1": _("This is a translation: %(var)s"),
        "trans2": _("This is another translation: %(var)s"),
    }
    locale = CSVLocale("en_US", translation)
    assert locale.pgettext("Trans1", "trans1") == "This is a translation: %(var)s"
    assert locale.pgettext("Trans2", "trans2") == "This is another translation: %(var)s"

# Generated at 2022-06-14 12:24:16.011357
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    import pytest
    messages = {"context|msg": "plural_msg"}
    Locale._cache['en'] = CSVLocale('en', messages)
    assert Locale.get('en').translate('msg', 'plural_msg') == 'msg'
    assert Locale.get('en').translate('msg', 'plural_msg', 5) == 'plural_msg'
    assert Locale.get('en').pgettext('context', 'msg', 'plural_msg') == 'plural_msg'
    assert Locale.get('en').pgettext('context', 'msg', 'plural_msg', 5) == 'plural_msg'
    assert Locale.get('en').pgettext('another_context', 'msg', 'plural_msg') == 'msg'

# Generated at 2022-06-14 12:24:25.245425
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    #1. load from a test folder that contains a file named mydomain.mo.
    #2. load from a file.
    #3. load from a non-existing folder.
    #4. load from a folder that does not contain any .mo files.
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    load_gettext_translations(os.path.join(basedir, 'testing', 'tornado'), 'mydomain')
    # print(current_locale._catalog)



# Generated at 2022-06-14 12:24:29.554106
# Unit test for function load_translations
def test_load_translations():
	from tornado.locale import load_translations
	load_translations("/home/nelson/Documents/IOT/web_tornado_safety_monitor/")
	locale = Locale.get_closest("fr_CA")
	print(locale.translate("Emergency contact"))
	




# Generated at 2022-06-14 12:24:40.644177
# Unit test for function load_translations
def test_load_translations():
    def load_translations_helper(encoding):
        dir = os.path.join(_current_path, 'test_csv')
        load_translations(dir, encoding)
        gen_log.debug('Got translations %r', _translations)
        assert 'es_LA' in _translations
        assert 'unknown' in _translations['es_LA']
        assert 'I love you' in _translations['es_LA']['unknown']
        assert 'Te amo' == _translations['es_LA']['unknown']['I love you']
        assert 'plural' in _translations['es_LA']
        assert '%(name)s liked this' in _translations['es_LA']['plural']

# Generated at 2022-06-14 12:24:48.619705
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    from datetime import datetime
    
    locales = [
        # 'en_US',
        # 'es',
        # 'fr',
        # 'ko',
        # 'ru',
        # 'zh_CN',
        # 'zh_HK',
        'zh_TW'
    ]

    for locale_code in locales:
        locale = Locale.get(locale_code)
        print("{} (relative mode):".format(locale_code))

        print("    format_date({}, relative=True):".format(datetime.utcnow()))
        print("    " + locale.format_date(datetime.utcnow(), relative=True))

# Generated at 2022-06-14 12:24:52.073757
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    locale = Locale.get("en")
    date = datetime.datetime(2017, 3, 6, 0, 0, 0)
    result = locale.format_date(date)
    assert result == "1 hour ago"



# Generated at 2022-06-14 12:24:57.146636
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    # Test for method format_day(self, date, gmt_offset, dow) of class Locale
    class TestLocale:
        def format_day(self, date, gmt_offset, dow):
            return date, gmt_offset, dow

    test_locale = TestLocale()
    d = Locale.format_day(test_locale, datetime.datetime.now(), 0, True)
    assert d == (datetime.datetime.now(), 0, True)
    d = Locale.format_day(test_locale, datetime.datetime.now(), 0)
    assert d == (datetime.datetime.now(), 0, True)



# Generated at 2022-06-14 12:25:05.962636
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    class TestClass:
        def setUp(self):
            self.obj = Locale('zh_CN')

    class TestTranslate:
        def test_correct_arguments(self):
            context = "Account"
            message = "Preferences saved."
            expect = "账户" + '\u0004' + "Preferences saved."
            actual = self.obj.pgettext(context, message)
            assert_equals(expect, actual)
        def test_incorrect_context(self):
            context = "1"
            message = "Preferences saved."
            expect = "账户" + '\u0004' + "Preferences saved."
            actual = self.obj.pgettext(context, message)
            assert_equals(expect, actual)

# Generated at 2022-06-14 12:25:07.761562
# Unit test for function load_translations
def test_load_translations():
    import tornado.locale
    tornado.locale.load_translations('./locale')
