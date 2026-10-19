

# Generated at 2022-06-14 12:16:28.455880
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    print("test_Locale_friendly_number start")
    locale = Locale.get("en")
    assert locale.friendly_number(999) == "999"
    assert locale.friendly_number(0) == "0"
    assert locale.friendly_number(123456789) == "123,456,789"
    assert locale.friendly_number(3) == "3"
    assert locale.friendly_number(100000) == "100,000"
    print("test_Locale_friendly_number end")



# Generated at 2022-06-14 12:16:33.058597
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale('fa_IR').friendly_number(1234567) == '1234567'
    assert Locale('en').friendly_number(1234567) == '1,234,567'
    assert Locale('en_US').friendly_number(1234567) == '1,234,567'



# Generated at 2022-06-14 12:16:34.353669
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations("locale","dummy")



# Generated at 2022-06-14 12:16:44.299246
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import datetime
    
    # sort out the supported_locales
    supported_locales_ = ["en","zh_CN","zh_TW"]
    supported_locales = set()
    for l in supported_locales_:
        supported_locales.add(l)
    supported_locales.add("en_US")
    supported_locales.add("en_GB")
    supported_locales.add("zh_HK")
    print(supported_locales)
    
    # get the local timezone
    local_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
    
    # make sure the date is right
    date_ = datetime.datetime(2020, 6, 16, 8, 0, 0)
    date = date_ - datetime.tim

# Generated at 2022-06-14 12:16:46.471215
# Unit test for function load_translations
def test_load_translations():
    return  load_translations("./locale/test","UTF-8")

test_load_translations()


# Generated at 2022-06-14 12:16:54.016515
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import os.path
    import tempfile
    import tornado
    import subprocess

    tornado.locale.load_gettext_translations('./locale', 'test')
    # tornado.locale.load_gettext_translations(os.path.join(os.path.dirname(__file__), 'locale'), 'test')
    d = tornado.locale.get("de_DE")
    assert d._("Hello, world") == "Hallo, Welt"

    d = tornado.locale.get("de_DE")
    assert d._("Hello, world") == "Hallo, Welt"

    d = tornado.locale.get("de_DE")
    assert d._("Hello, world") == "Hallo, Welt"
    # os.remove('./locale/de_DE/LC_

# Generated at 2022-06-14 12:17:02.112169
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    def test_helper(date_text, locale_shortname, dow, expected):
        sdate = datetime.datetime.strptime(date_text,"%Y-%m-%d")
        locale = Locale.get(locale_shortname)
        assert locale.format_day(sdate,dow=dow) == expected

    test_helper("2020-01-22","en_US",True,"Wednesday, January 22")
    test_helper("2020-01-22","en_US",False,"January 22")
    test_helper("2020-01-22","fr_FR",True,"mercredi, 22 janvier")
    test_helper("2020-01-22","fr_FR",False,"22 janvier")


# Generated at 2022-06-14 12:17:04.256648
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    ###
    # Only available when the code is written
    ###
    pass

# Generated at 2022-06-14 12:17:09.376915
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """Unit test for method format_day of class Locale"""
    assert (Locale.get("en").format_day(
        datetime.datetime(2019, 9, 19), 0, True) == "Thursday, September 19")
    assert (Locale.get("en").format_day(
        datetime.datetime(2019, 9, 19), 0, False) == "September 19")



# Generated at 2022-06-14 12:17:15.851232
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations(directory="/home/zhxy/github/Python-Web-Server/tornado/locale",domain="tornado")
    _trans = _translations['en_US']
    assert _trans == gettext.NullTranslations(), "Translation for en_US is NullTranslations"
    assert len(_supported_locales) == 3, "Supported locales have 3 languages"


# Generated at 2022-06-14 12:17:44.530711
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    # Test the 'en' friendly number
    mylocale = Locale("en")
    assert mylocale.friendly_number(10000) == "10,000"
    assert mylocale.friendly_number(100000) == "100,000"
    assert mylocale.friendly_number(1000000) == "1,000,000"

    # Test the 'en_US' friendly number
    mylocale = Locale("en_US")
    assert mylocale.friendly_number(10000) == "10,000"
    assert mylocale.friendly_number(100000) == "100,000"
    assert mylocale.friendly_number(1000000) == "1,000,000"

    # Test the non-friendly number
    mylocale = Locale("en_GB")
    assert mylocale.friendly_number

# Generated at 2022-06-14 12:17:45.452051
# Unit test for function load_translations
def test_load_translations():
    test_load_translations_1()



# Generated at 2022-06-14 12:17:56.474222
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    import unittest

    def get_test_class():
        try:
            # noinspection PyCompatibility
            import unittest.mock as mock
        except ImportError:
            import mock

        class LocaleTester(unittest.TestCase):
            def setUp(self):
                self.mock_loc = mock.Mock(spec=Locale)
                self.mock_loc.code = 'en'

                self.mock_loc.format_date.return_value = 'mock_date'
                self.mock_loc._weekdays = ["Monday", "Tuesday", "Wednesday",
                                           "Thursday", "Friday", "Saturday",
                                           "Sunday"]

# Generated at 2022-06-14 12:18:00.056335
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale.get("en").friendly_number(1000) == "1,000"
    assert Locale.get("fr").friendly_number(1000) == "1000"



# Generated at 2022-06-14 12:18:01.599775
# Unit test for function load_translations
def test_load_translations():
    load_translations("local")
    print(_translations['en_US'])
    print(_supported_locales)



# Generated at 2022-06-14 12:18:02.630112
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    pass


# Generated at 2022-06-14 12:18:07.404823
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    test_cases = [
        (0, "0"),
        (1, "1"),
        (10, "10"),
        (100, "100"),
        (999, "999"),
        (1000, "1,000"),
        (1001, "1,001"),
        (1010, "1,010"),
        (1234, "1,234"),
        (12345, "12,345"),
        (123456, "123,456"),
        (1234567, "1,234,567"),
    ]
    for value, expected in test_cases:
        assert Locale.get("en").friendly_number(value) == expected



# Generated at 2022-06-14 12:18:18.738857
# Unit test for function load_translations
def test_load_translations():
    def _test_translations_filename(locale_code: str) -> str:
        return '{}.csv'.format(locale_code)

    def _test_translations_csv_content(
        locale_code: str,
        translations_dict: Dict[str, Dict[str, str]],
    ) -> str:
        return '\n'.join(
            [
                '"{}","{}"'.format(
                    k,
                    v,
                )
                for k, v in translations_dict.items()
            ],
        )


# Generated at 2022-06-14 12:18:24.137213
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    gen_log.debug("start test_Locale_friendly_number")
    l = CSVLocale.get('en')
    list_unit_test = [0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    list_unit_test_result = ['0', '1', '10', '100', '1,000', '10,000', '100,000', '1,000,000', '10,000,000', '100,000,000']
    for i in range(0, len(list_unit_test)):
        assert(l.friendly_number(list_unit_test[i]) == list_unit_test_result[i])
    gen_log.debug("end test_Locale_friendly_number")


# Generated at 2022-06-14 12:18:26.567943
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    load_gettext_translations(directory='tornado/locale', domain='tornado')
    print(get('en_US'))
    print(get('zh_CN'))
    print(get('zh_TW'))
    print(get('zh_HK'))
    print(get('zh_SG'))


# Generated at 2022-06-14 12:19:02.903782
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    assert Locale.get("de").format_day(datetime.datetime(2018,7,26)) == "Donnerstag, 26. Juli"
    assert Locale.get("de").format_day(datetime.datetime(2018,7,26), dow=False) == "26. Juli"
    assert Locale.get("en").format_day(datetime.datetime(2018,7,26)) == "Thursday, July 26"
    assert Locale.get("en").format_day(datetime.datetime(2018,7,26), dow=False) == "July 26"
    assert Locale.get("is").format_day(datetime.datetime(2018,7,26)) == "Fimmtudagur, 26. júl"

# Generated at 2022-06-14 12:19:05.065148
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    directory = "./locale/"
    domain = "locale"
    assert load_gettext_translations(directory, domain) == None


# Generated at 2022-06-14 12:19:09.776238
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    try:
        load_gettext_translations("/home/damien/Téléchargements/tornado-master-test/tornado/locale", "tornado")
    except Exception as e:
        print(e)
test_load_gettext_translations()


# Generated at 2022-06-14 12:19:13.280287
# Unit test for function load_translations
def test_load_translations():
    load_translations("/Users/jian/Desktop/tornado-4.5.3/tornado/locale")
    print(_translations["es_LA"])
    get("es_LA").translate("I love you")


# Generated at 2022-06-14 12:19:26.446746
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """Unit test for method format_day of class Locale
    """
    date = datetime.datetime(year=2020, month=1, day=1)
    locale = Locale.get("en")
    s = locale.format_day(date)
    assert s == u"Wednesday, January 1"
    s = locale.format_day(date, dow=False)
    assert s == "January 1"
    locale = Locale.get("zh_CN")
    s = locale.format_day(date)
    assert s == u"\u661f\u671f\u4e09, 1\u6708 1\u65e5"
    s = locale.format_day(date, dow=False)
    assert s == "1\u6708 1\u65e5"

# Generated at 2022-06-14 12:19:34.429231
# Unit test for method format_day of class Locale
def test_Locale_format_day():
    """Test method format_day of class Locale"""
    initialized = False
    if initialized:
        return
    else:
        initialized = True

    import __main__ as main
    import inspect

    import dateutil.parser

    # Set up context
    release_path = Path(__file__).parent.parent.resolve()
    main.gen_log = logging.getLogger("gen.log")
    main.gen_log.setLevel(logging.DEBUG)
    main.gen_log.addHandler(logging.StreamHandler())
    module_path = Path(inspect.getfile(inspect.currentframe())).resolve()
    gen_log.info("Running tests in {}".format(module_path))
    gen_log.info("Running tests in release: {}".format(release_path))
    os.chdir

# Generated at 2022-06-14 12:19:45.488362
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # Generate test cases
    def case(self, context, message, plural_message=None, count=None, expected=None):
        _ = self.translate
        _p = self.pgettext
        if count is None:
            if expected is None:
                expected = _(message)
            actual = _p(context, message)
        else:
            if expected is None:
                expected = _(message, plural_message, count)
            actual = _p(context, message, plural_message, count)
        assert actual == expected

    # Run test cases

# Generated at 2022-06-14 12:19:56.619024
# Unit test for method list of class Locale
def test_Locale_list():
    result = list(map(str, range(1, 20)))
    assert Locale.get('zh_CN').list(result) == '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \u4e0b\u534811, \u4e0a\u534812, \u4e0b\u534813, \u4e0a\u534814, \u4e0b\u534815, \u4e0a\u534816, \u4e0b\u534817, \u4e0a\u534818, \u4e0b\u534819'

# Generated at 2022-06-14 12:20:07.017256
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():
    csl_name_v1 = CSVLocale(code="en", translations={"unknown": {"Hello, World!": "Hello, world"}})
    csl_name_v2 = CSVLocale(code="en", translations={"unknown": {"Hello, World!": "Hello, world"}})
    csl_name_v3 = CSVLocale(code="en", translations={"unknown": {"Hello, World!": "Hello world"}})
    csl_name_v4 = CSVLocale(code="en", translations={"unknown": {"Hello, World!": "Hello", "world": "world"}})
    csl_name_v5 = CSVLocale(code="en", translations={"unknown": {"Hello, World!": "Hello", "world": "world."}})

# Generated at 2022-06-14 12:20:14.513059
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    locale = Locale.get("en_US")
    assert locale.pgettext("Now") == "Now"
    assert locale.pgettext("This is the best") == "This is the best"
    assert locale.pgettext("One") == "One"
    assert locale.pgettext("One", "Two", 1) == "One"
    assert locale.pgettext("One", "Two", 2) == "Two"
    assert locale.pgettext("One", "Two", 10) == "Two"



# Generated at 2022-06-14 12:21:22.972085
# Unit test for function load_translations
def test_load_translations():
    load_translations("translations")


# Generated at 2022-06-14 12:21:26.137173
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # TODO: It is an error if the implementation does not match the docstring
    assert False, "TODO: Implement"


# Generated at 2022-06-14 12:21:36.203808
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    '''
        Test format_date(date, gmt_offset, relative, shorter, full_format)
    '''
    # Test cases:
    # Test case 1
    # Input:
    #   date = datetime.datetime.utcnow() - datetime.timedelta(seconds=27)
    #   gmt_offset = 0
    #   relative = True
    #   shorter = False
    #   full_format = False
    # Expected output:
    #   27 seconds ago
    print("Unit test for method format_date of class Locale start...")
    test_case_1 = True
    date_1 = datetime.datetime.utcnow() - datetime.timedelta(seconds=27)
    gmt_offset_1 = 0
    relative_1 = True

# Generated at 2022-06-14 12:21:48.315013
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    _translations = {}
    directory=os.path.join(os.path.dirname(__file__),'_locale_data')
    domain='tornado'
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
            gen_log.error("Cannot load translation for '%s': %s", lang, str(e))
            continue
    _supported

# Generated at 2022-06-14 12:22:01.137099
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    # Set up test data
    test_values = [
        (1, "1"),
        (10, "10"),
        (100, "100"),
        (1000, "1,000"),
        (10000, "10,000"),
        (100000, "100,000"),
        (1000000, "1,000,000"),
        (1000000000000000, "100,000,000,000,000"),
    ]
    # Run the test(s)
    for value, expected_friendly_number in test_values:
        test_locale = Locale("en")
        friendly_number = test_locale.friendly_number(value)
        assert friendly_number == expected_friendly_number
test_Locale_friendly_number()


# Generated at 2022-06-14 12:22:09.118266
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():
    # should return the same result for transaltions for same context
    assert Locale.get_closest("en").pgettext("email", "Email") == Locale.get_closest("en").pgettext("email", "Email")
    assert Locale.get_closest("en").pgettext("profile", "Profile") == Locale.get_closest("en").pgettext("profile", "Profile")

    # should return the same result in singular and plural cases
    assert Locale.get_closest("en").pgettext("plural", "zero") == Locale.get_closest("en").pgettext("plural", "zero", "one", 1)

    # should return the same result in singular and plural cases

# Generated at 2022-06-14 12:22:11.010055
# Unit test for function load_translations
def test_load_translations():
    directory = "app/user/locale"
    encoding = "utf-8"
    load_translations(directory, encoding)

# Generated at 2022-06-14 12:22:15.230982
# Unit test for function load_gettext_translations

# Generated at 2022-06-14 12:22:17.973410
# Unit test for function load_translations
def test_load_translations():
    load_translations(os.getcwd()+'/translations')
    assert type(_translations) == type({})
    assert _translations != {}
    assert _supported_locales != None


# Generated at 2022-06-14 12:22:23.644835
# Unit test for function load_translations
def test_load_translations():
    test_data1 = "./test_csvdata1"
    test_data2 = "./test_csvdata2"
    test_data3 = "./test_csvdata3"
    load_translations(test_data1)
    load_translations(test_data2)
    load_translations(test_data3)



# Generated at 2022-06-14 12:23:43.779572
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    # Test for English locale
    locale = Locale.get('en')
    date = datetime.datetime(2011, 1, 2, 14, 29, 42, 735000)
    assert locale.format_date(date) == '3 years, 6 months ago'

    # Test for German locale
    locale = Locale.get('de')
    date = datetime.datetime(2011, 1, 2, 14, 29, 42, 735000)
    assert locale.format_date(date) == 'vor 3 Jahren'

    # Test with gmt_offset
    locale = Locale.get('en')
    date = datetime.datetime(2011, 1, 2, 14, 29, 42, 735000)
    assert locale.format_date(date, gmt_offset=5) == '3 years, 6 months ago'


# Generated at 2022-06-14 12:23:54.731197
# Unit test for method format_date of class Locale
def test_Locale_format_date():
    import datetime

# Generated at 2022-06-14 12:23:56.770985
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    assert load_gettext_translations("./locale/", "test") == None



# Generated at 2022-06-14 12:24:06.284047
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    # Test for locales which does not use comma
    l = Locale("fa")
    assert l.friendly_number(0) == "0"
    assert l.friendly_number(1) == "1"
    assert l.friendly_number(10) == "10"
    # Test for English (default)
    l = Locale("en")
    assert l.friendly_number(0) == "0"
    assert l.friendly_number(1) == "1"
    assert l.friendly_number(10) == "10"
    assert l.friendly_number(100) == "100"
    assert l.friendly_number(1000) == "1,000"
    assert l.friendly_number(10000) == "10,000"



# Generated at 2022-06-14 12:24:11.608308
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    assert Locale("en").friendly_number(1000) == "1,000"
    assert Locale("en").friendly_number(10000) == "10,000"
    assert Locale("en").friendly_number(100000) == "100,000"



# Generated at 2022-06-14 12:24:18.837067
# Unit test for function load_gettext_translations
def test_load_gettext_translations():
    import tempfile
    import os
    import shutil
    import gettext

    tmp = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmp, "zh_CN"))
    os.mkdir(os.path.join(tmp, "zh_CN", "LC_MESSAGES"))
    with open(os.path.join(tmp, "zh_CN", "LC_MESSAGES", "test1.mo"), "wb") as f:
        f.write(gettext.GNUTranslations(f)._catalog[""])

    load_gettext_translations(tmp, "test1")
    shutil.rmtree(tmp)


# Generated at 2022-06-14 12:24:31.101469
# Unit test for function load_translations
def test_load_translations():
    #Load data
    dataset = load_translations("/home/lili/Documents/Proyecto/tornado-5.1/tornado/locale")
    with open("/home/lili/Documents/Proyecto/tornado-5.1/tornado/locale/es_LA.csv", "r") as csvfile:
        #Read csv file
        data = list(csv.reader(csvfile))
    for d in data:
        for i in range(1,3):
            d[i] = d[i].replace('"','')
    for i in range(len(data)):
        #Compare functions output with expected result
        assert _translations["es_LA"]["unknown"][data[i][0]] == data[i][1]


# Generated at 2022-06-14 12:24:35.448986
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():
    test_locale_code = "en"
    test_locale = Locale(test_locale_code)
    test_value_1 = 1
    test_value_1000 = 1000
    test_value_10000 = 10000
    test_value_1000000 = 1000000
    assert test_locale.friendly_number(test_value_1) == "1"
    assert test_locale.friendly_number(test_value_1000) == "1,000"
    assert test_locale.friendly_number(test_value_10000) == "10,000"
    assert test_locale.friendly_number(test_value_1000000) == "1,000,000"

    test_locale_code_2 = "en_US"

# Generated at 2022-06-14 12:24:39.349576
# Unit test for function load_translations
def test_load_translations():
    # Normalized to "en_US"
    load_translations("example/locale")
    user_locale = Locale.get_closest("es_LA")
    print(user_locale.translate("Sign out"))



# Generated at 2022-06-14 12:24:44.234379
# Unit test for function load_translations
def test_load_translations():
    load_translations(os.path.dirname(__file__))
    print(_translations)
    # print(get('de_DE').translate('dog'))
    print(get('de_DE').translate('dog', 'dogs', 2))
    print(get('de_DE').translate('dog', 'dogs', 4))

    # test_load_translations()
