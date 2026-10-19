

# Generated at 2022-06-13 22:12:21.268389
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.context import Environment
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import PrettyFormatter
    from httpie.plugins.builtin import FormatControlFormatter
    env = Environment()

    groups = ['formatters']
    kwargs = {}
    #test_groups = ['formatters']
    test_groups = ['formatters', 'format_control']
    formatting = Formatting(test_groups, env, **kwargs)
    enabled_plugins = formatting.enabled_plugins
    # If the class is instantiated correctly, the enabled_plugins should contain
    # JSONFormatter, PrettyFormatter and FormatControlFormatter
    assert FormatControlFormatter in enabled_plugins
    assert JSONFormatter in enabled_plugins
    assert PrettyFormatter in enabled_plugins


# Generated at 2022-06-13 22:12:24.906919
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    assert Formatting(['colors']).format_body('<p>i am \n a paragraph</p>',"text/html")=='\u001b[96m<p\u001b[0m\u001b[91m>\u001b[0mi am \u001b[91m\n\u001b[0m a paragraph\u001b[96m</p\u001b[0m\u001b[91m>\u001b[0m'

# Generated at 2022-06-13 22:12:34.707542
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    fm = Formatting(groups=['all'])
    assert isinstance(fm, Formatting)


# Generated at 2022-06-13 22:12:43.085173
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    result = Formatting(groups=['colors']).format_body(content="{'a' : 'b'}", mime='application/json')
    assert result == '{\n    \x1b[1;37m\x1b[40m"a"\x1b[0m\x1b[39m: \x1b[1;37m\x1b[40m"b"\x1b[0m\x1b[39m\n}'

# Generated at 2022-06-13 22:12:49.339596
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = """
    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 12
    """
    fmt = Formatting(["colors"])
    assert "HTTP/1.1 200 OK" in fmt.format_headers(headers)
    assert "Content-Type" not in fmt.format_headers(headers)
    assert "Content-Length" not in fmt.format_headers(headers)


# Generated at 2022-06-13 22:12:57.273155
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = 'HTTP/1.1 200 OK\r\ncontent-type: application/json\r\nserver: example.com\r\n'
    fmt = Formatting(['json'])
    assert fmt.format_headers(headers)[:8] == '\x1b['



# Generated at 2022-06-13 22:13:02.299635
# Unit test for constructor of class Formatting
def test_Formatting():
    http_formatter_grp = ["colors", "formatters"]
    env = Environment()
    f = Formatting(http_formatter_grp, env)
    # print(f.enabled_plugins)
    assert f.enabled_plugins

# Generated at 2022-06-13 22:13:08.761505
# Unit test for constructor of class Formatting
def test_Formatting():

    # case1
    group = [
        'pretty',
    ]
    env = Environment()
    formatting = Formatting(group, env)

    assert formatting.enabled_plugins
    assert formatting.enabled_plugins[0].__class__.__name__ == 'PrettyFormatter'

    # case2
    group = [
        'colors',
    ]
    env = Environment(colors=False)
    formatting = Formatting(group, env)

    assert formatting.enabled_plugins == []



# Generated at 2022-06-13 22:13:09.932407
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting([], env=Environment(), **{})

# Generated at 2022-06-13 22:13:20.504065
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    class f1_plugin(FormattingPlugin):
        def format_headers(self, headers: str) -> str:
            return headers + 'h11'

    class f2_plugin(FormattingPlugin):
        def format_headers(self, headers: str) -> str:
            return headers + 'h22'
    
    plugin_manager.register(f1_plugin)
    plugin_manager.register(f2_plugin)

    headers = 'abc'

    groups = ['f1', 'f2']
    formatting = Formatting(groups)
    h = formatting.format_headers(headers)

    assert h == 'abch11h22'


# Generated at 2022-06-13 22:13:24.108026
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    pass

# Generated at 2022-06-13 22:13:30.866121
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["JSON", "HTML"]
    obj = Formatting(groups) # Environment should be given explicitly
    assert obj.enabled_plugins
    assert obj.format_headers("{\"key\": \"value\"}") == "{\"key\": \"value\"}"
    assert obj.format_body("{\"key\": \"value\"}", "application/json") == "{\"key\": \"value\"}"

# Generated at 2022-06-13 22:13:40.769908
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert is_valid_mime("application/json") == True
    assert is_valid_mime("application/xml") == True
    assert is_valid_mime("application/soap+xml") == True
    assert is_valid_mime("application/javasccript") == False
    assert is_valid_mime("application/") == False
    assert is_valid_mime("") == False

    env = Environment()
    env.config['request']['formatters_grouped'] = ['json']

    f = Formatting(['json'], env)
    formatter = f.enabled_plugins[0]
    converter = formatter.converter
    assert converter.enabled == True

    # test mime which is not supported by any converter
    converter = Conversion.get_converter("application/javascript")
   

# Generated at 2022-06-13 22:13:47.952474
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import HTTPPrettyPrinter
    from httpie.core import parser

    env = Environment()
    env.stdout = io.StringIO()

    f = Formatting(['pretty'], env=env)
    assert len(f.enabled_plugins) == 1
    assert isinstance(f.enabled_plugins[0], HTTPPrettyPrinter)

    args = parser.parse_args(args=[], env=env)
    f = Formatting(args.prettify, env=env)
    assert len(f.enabled_plugins) == 1
    assert isinstance(f.enabled_plugins[0], HTTPPrettyPrinter)


# Generated at 2022-06-13 22:13:48.377363
# Unit test for constructor of class Formatting
def test_Formatting():
    pass

# Generated at 2022-06-13 22:13:53.107127
# Unit test for constructor of class Formatting
def test_Formatting():
    groups: List[str] = ['color']
    env = Environment()

    fmt = Formatting(groups, env)
    try:
        assert fmt.enabled_plugins[0].__class__.__name__ == 'Colorful'
    except AssertionError:
        print('False: Case1')
    else:
        print('True: Case1')

    fmt = Formatting(groups, env, always=True)
    try:
        assert fmt.enabled_plugins[0].__class__.__name__ == 'Colorful'
        assert fmt.enabled_plugins[0].always
    except AssertionError:
        print('False: Case2')
    else:
        print('True: Case2')



# Generated at 2022-06-13 22:13:57.114171
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors', 'format']
    env = Environment()
    obj = Formatting(groups, env, style='monokai')
    assert obj.enabled_plugins[0].STYLE == 'monokai'
    assert obj.enabled_plugins[1].STYLE == 'monokai'


# Generated at 2022-06-13 22:14:01.048880
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print("Test function: get_converter")
    c = Conversion.get_converter("text/html")
    assert c.__class__.__name__ == "HTMLConverter"



# Generated at 2022-06-13 22:14:09.134305
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import HTTPHeadersProcessor
    from httpie.plugins.builtin import JSONProcessor
    from httpie.plugins.builtin import PrettyJsonProcessor
    from httpie.plugins.builtin import XMLProcessor
    from httpie.plugins.builtin import PrettyXmlProcessor

    sample = Formatting(['headers', 'format', 'pretty'])
    sample_plugins = [HTTPHeadersProcessor, JSONProcessor, PrettyJsonProcessor, XMLProcessor, PrettyXmlProcessor]
    assert sample.enabled_plugins == sample_plugins

# Generated at 2022-06-13 22:14:16.688895
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """
    Test if method get_converter of class Conversion returns a converter class
    if valid mime type is passed as argument and None otherwise.
    """
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)
    # Pass invalid mime type and expect None
    assert Conversion.get_converter('test') is None


# Generated at 2022-06-13 22:14:24.043147
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting([('colors',)])
    x = f.format_body(
        '{"foo": "bar"}',
        'application/json')
    assert b'"foo":\x1b[34m "bar"\x1b[0m' in x



# Generated at 2022-06-13 22:14:31.198373
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # does not support
    assert Conversion.get_converter('application/tar') is None
    assert Conversion.get_converter('application/xml') is None
    assert Conversion.get_converter('image/png') is None
    assert Conversion.get_converter(None) is None

    # supports
    assert Conversion.get_converter('application/json')
    assert Conversion.get_converter('application/json; charset=utf-8')
    assert Conversion.get_converter('application/x-www-form-urlencoded')
    assert Conversion.get_converter('application/xml; charset=UTF-8')
    assert Conversion.get_converter('text/html')
    assert Conversion.get_converter('text/html; charset=UTF-8')

# Generated at 2022-06-13 22:14:34.698740
# Unit test for constructor of class Formatting
def test_Formatting():
    pg = Formatting(groups=['colors'], env=Environment(), color=True)
    print(pg.enabled_plugins)



# Generated at 2022-06-13 22:14:41.521431
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    input = b"""POST / HTTP/1.1\r\nContent-Type: application/json\r\n
Content-Length: 15\r\n\r\n""".decode('utf-8')
    expected_output = b"""POST / HTTP/1.1\r\nContent-Type: application/json\r\n
Content-Length: 15\r\n\r\n""".decode('utf-8')
    formatter = Formatting(['colors'])
    assert formatter.format_headers(input) == expected_output

# Generated at 2022-06-13 22:14:42.660917
# Unit test for constructor of class Formatting
def test_Formatting():
    assert 1 == 1

# Generated at 2022-06-13 22:14:54.120658
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins import FormatterPlugin
    from httpie.pretty import ConsoleCodes, get_lexer

    class TestFormatterPlugin(FormatterPlugin):

        def format_body(self, body, mime):
            try:
                lexer = get_lexer(mime)
                return ConsoleCodes.colorize(body, lexer)
            except ValueError:
                return body

    groups = ['test']
    format_string = "a=b"
    mime = "text/plain; charset=utf-8"

    testing = Formatting(groups, Format="colors")
    testing.enabled_plugins = [TestFormatterPlugin()]

    result = testing.format_body(format_string, mime)
    assert result != ''

# Generated at 2022-06-13 22:15:01.840550
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    formatting = Formatting(["HttpieProcessors"])

    headers_list = [
        ("Content-type: text/html"),
        ("Date: January 1st, 1970"),
        ("Content-type: text-html"),
        ("Content-type: text/plain"),
        ("Date: January 1st, 1970"),
        ("Date: January 1st, 1971"),
        ("Date: January 1st, 1972"),
        ("Date: January 1st, 1973"),
        ("Date: January 1st, 1974"),
        ("Date: January 1st, 1975"),
        ("Content-type: application/pdf"),
        ("Content-type: application/json")
    ]

    # get original headers
    headers = ""
    for header in headers_list:
        headers += header + "\n"

    # get expected headers
    expected_headers = ""
   

# Generated at 2022-06-13 22:15:12.496558
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    import requests
    from httpie import ExitStatus
    from plugins.highlight import SolarizedStyle
    available_plugins = plugin_manager.get_formatters_grouped()
    for group in available_plugins:
        for cls in available_plugins[group]:
            p = cls(style=SolarizedStyle)
            if p.enabled:
                enabled_plugins.append(p)
    try:
        s = requests.Session()
        s.get("http://httpbin.org/")
        r = s.get("http://httpbin.org/get")
        mime = Formatting.format_headers(r.headers)
    except requests.exceptions.ConnectionError:
        print('Network is unreachable, skip tests involving network accesses')
        exit(ExitStatus.ERROR_CONNECT)

# Generated at 2022-06-13 22:15:17.634878
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter.mime == 'application/json'
    assert converter.supports('application/json')
    assert not converter.supports('application/vnd.api+json')


# Generated at 2022-06-13 22:15:24.799226
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatter = Formatting(['colors'], use_colors=True)
    headers = 'HTTP/1.1 200 OK\r\n\r\n'
    assert formatter.format_headers(headers) == '\x1b[1m\x1b[32mHTTP/1.1 200 OK\x1b[39m\x1b[0m\r\n\r\n'



# Generated at 2022-06-13 22:15:29.412180
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    l = Formatting(['colors'],env)
    assert l.enabled_plugins[0].__class__.__name__ == 'ColorsFormatter'



# Generated at 2022-06-13 22:15:35.185308
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('a/b') == None
    assert Conversion.get_converter('application/json') != None
    assert Conversion.get_converter('application/xml') != None
    assert Conversion.get_converter('text/csv') != None


# Generated at 2022-06-13 22:15:45.916905
# Unit test for method format_body of class Formatting

# Generated at 2022-06-13 22:15:52.461473
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in ["format_body"]:
        for cls in available_plugins[group]:
            p = cls(env=Environment())
            if p.enabled:
                enabled_plugins.append(p)
    assert (enabled_plugins[0].format_body("hehe", "application/json") is not None)

# Generated at 2022-06-13 22:16:00.038207
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    class PlainTextConverter(ConverterPlugin):  # a sample converter
        def supports(self):
            return 'text/plain'

        def convert(self,
                    body: Optional[str],
                    headers_mapping: Optional[Headers]) -> str:
            return body  # just return the same input

    test_env = Environment()
    test_env.formatter.enabled_plugins = []  # to make sure no other plugins are affecting the test
    test_env.formatter.enabled_plugins.append(PlainTextConverter('text/plain'))
    test_env.formatter.enabled_plugins.append(PlainTextConverter('text/plain'))
    test_env.formatter.enabled_plugins.append(PlainTextConverter('text/plain'))
    result = test_env.formatter

# Generated at 2022-06-13 22:16:09.101176
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    import pytest 
    assert not is_valid_mime("*/*")
    assert is_valid_mime("application/json")
    assert not is_valid_mime(".json")
    assert not is_valid_mime("/json")
    assert not is_valid_mime("application/")
    assert not is_valid_mime("application")
    assert not is_valid_mime("")
    assert not is_valid_mime(None)
    assert not is_valid_mime("json")

# Generated at 2022-06-13 22:16:16.955700
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    body = "some body"
    mime = 'application/json'
    expected = "{\n  \"test\": \"value\"\n}"

    available_plugins  = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for cls in available_plugins['colors']:
        p = cls(env=Environment())
        if p.enabled:
            enabled_plugins.append(p)

    for p in enabled_plugins:
        body = p.format_body(body, mime)
    assert body == expected

# Generated at 2022-06-13 22:16:28.726966
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    assert Formatting(groups=['colors']).format_headers(headers='') == ''

if __name__ == "__main__":
    test_Formatting_format_headers()

# Generated at 2022-06-13 22:16:34.527912
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']
    kwargs = {'theme': 'Solarized'}
    env_kwargs = {'colors': True}
    env = Environment(**env_kwargs)
    formatting = Formatting(groups, env, **kwargs)
    print(formatting.enabled_plugins)


# Generated at 2022-06-13 22:16:48.217532
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("image/jpeg"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("image/png"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("image/gif"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("text/html"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("text/xml"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("application/json"), ConverterPlugin)
    assert isinstance(Conversion.get_converter("application/atom+xml"), ConverterPlugin)


# Generated at 2022-06-13 22:17:04.616330
# Unit test for constructor of class Formatting

# Generated at 2022-06-13 22:17:10.566935
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["color"]
    env = Environment()
    # formatting = Formatting(groups, env, **kwargs)
    #
    # assert formatting.enabled_plugins == []
    # assert formatting.group == "colors"
    # assert formatting.kwargs == kwargs

# Generated at 2022-06-13 22:17:20.081551
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.compat import json

    class Formatting_Tester:

        def __init__(self):
           self.groups = ["pretty"]
           self.headers = {'Content-Type': 'application/json', 'ETag': 'foobar'} 

        def test_format_headers(self):
            h = Formatting(self.groups)
            headers = json.dumps(self.headers, separators=(',', ':'))
            headers = h.format_headers(headers)
            headers = json.loads(headers)
            assert isinstance(headers, dict)

    Formatting_Tester().test_format_headers()

# Generated at 2022-06-13 22:17:30.808612
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Best match
    converter_class = Conversion.get_converter('application/json')
    assert converter_class
    assert converter_class.mime == 'application/json'

    # Exact match
    converter_class = Conversion.get_converter('application/json;q=1.0')
    assert converter_class
    assert converter_class.mime == 'application/json'

    # Inexact match
    converter_class = Conversion.get_converter('application/json;q=0.9')
    assert converter_class
    assert converter_class.mime == 'application/json'

    # Inexact match with charset
    converter_cla

# Generated at 2022-06-13 22:17:44.238651
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Test for Formatting instance
    class FormattingMock(Formatting):
        def __init__(self, *args, **kwargs):
        # remove __init__ method from superclass
            pass
    # Test for class in plugin_manager.get_formatters_grouped()
    class GroupMock:
        def __init__(self, *args, **kwargs):
        # remove __init__ method from superclass
            pass
    # Test for GroupMock.format_body
    def format_body_rs(self, content: str, mime: str) -> str:
        return content
    GroupMock.format_body = format_body_rs
    # Test env
    env = Environment()
    # Test content
    content = b'{"test_key" : "test_value"}'
    # Test mime


# Generated at 2022-06-13 22:17:49.670876
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins import FormatterPlugin
    class test_plugin(FormatterPlugin):
        def __init__(self, *args, **kwargs):
            self.enabled = True
    assert Conversion.get_converter("test_plugin") == None
    plugin_manager.register(test_plugin)
    assert Conversion.get_converter("test_plugin").__class__ == test_plugin
    plugin_manager.unregister(test_plugin)


# Generated at 2022-06-13 22:17:59.634077
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """Test for method format_body of class Formatting"""
    env = Environment()
    env.colors = True
    h = Formatting(groups=['colors'], env=env)
    assert h.format_body('{"foo": "bar"}', "application/json") == '\x1b[32m{\x1b[39m\n    \x1b[32m"foo"\x1b[39m\x1b[37m: \x1b[39m\x1b[33m"bar"\x1b[39m\n\x1b[32m}\x1b[39m\n'

# Generated at 2022-06-13 22:18:08.684939
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import io
    import sys
    # io.StringIO: https://docs.python.org/3/library/io.html
    # This class supports the context manager protocol.
    # Use a StringIO object to imitate the behaviour of sys.stdout
    # https://stackoverflow.com/questions/7617605/python-output-buffering
    stdout = sys.stdout
    sys.stdout = io.StringIO()

# Generated at 2022-06-13 22:18:17.800931
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie import ExitStatus
    from httpie.context import Environment
    from httpie.plugins.builtin import Formatter
    import pytest

    class FormatterA(Formatter):
        def format_headers(self, headers):
            return 'headers A'

    class FormatterB(Formatter):
        def format_headers(self, headers):
            return 'headers B'

    FormatterA.name = 'A'
    FormatterB.name = 'B'

    pm = plugin_manager.PluginManager()
    pm.register_plugin_class(FormatterA)
    pm.register_plugin_class(FormatterB)


# Generated at 2022-06-13 22:18:22.822203
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Case: non-existing converter
    assert not Conversion.get_converter("NON_EXISTING/NON_EXISTING")

    # Case: existing converter
    assert Conversion.get_converter("text/html")


# Generated at 2022-06-13 22:18:31.331960
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("application/json"), ConverterPlugin)
    assert not Conversion.get_converter("json")
    assert not Conversion.get_converter("")
    assert not Conversion.get_converter(None)

# Generated at 2022-06-13 22:18:40.379034
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors']
    fm = Formatting(groups)
    content = '{"a":1}'
    mime = 'application/json'
    assert fm.format_body(content, mime) == '\x1b[38;5;244m{\x1b[39m\n' \
                                            '    \x1b[38;5;244m"a"\x1b[39m: ' \
                                            '\x1b[38;5;39m1\x1b[39m\n' \
                                            '\x1b[38;5;244m}\x1b[39m\n'

# Generated at 2022-06-13 22:18:41.999103
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter



# Generated at 2022-06-13 22:18:46.654853
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'text/html'
    converter_class = Conversion.get_converter(mime)
    assert converter_class.supports(mime)
    assert converter_class.output_mime == 'application/json'
    assert converter_class.convert('<html></html>') == '{}'

# Generated at 2022-06-13 22:18:58.376987
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors']
    kwargs = {'colors': 'always'}
    f = Formatting(groups, **kwargs)
    content = f.format_body('abc\ndef', 'text/html')
    assert content == '<span style="color:cyan">abc</span>\n<span style="color:cyan">def</span>'
    content = f.format_body('abc\ndef', 'text/plain')
    assert content == 'abc\ndef'
    content = f.format_body('{"a": 0.5, "b": "abc"}', 'application/json')

# Generated at 2022-06-13 22:19:13.169347
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie import ExitStatus
    from httpie.core import main
    from httpie.context import Environment

    env = Environment(stdin=six.StringIO())
    output = main(['https://api.github.com/users/jakubroztocil'], env=env)
    assert output
    assert output.exit_status == ExitStatus.OK

# Generated at 2022-06-13 22:19:26.163796
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()

    f = Formatting(groups=('colors', 'formatters'), env=env,
                   color_scheme='Solarized')

    h = '''Content-Type: application/json; charset=utf-8
Cache-Control: max-age=0, private, must-revalidate
Content-Length: 335
Vary: Origin
X-Frame-Options: SAMEORIGIN
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Runtime: 0.007426
X-Request-Id: 8a3aa3e3-2b21-4d36-a207-ee1bbb768c83
Strict-Transport-Security: max-age=31536000
'''.encode('utf8')  # type: bytes
    f

# Generated at 2022-06-13 22:19:36.903484
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    text = "bla bla bla"
    mime = "text/html"
    format = Formatting([], env=Environment(colors=True))
    assert format.format_body(text, mime) == text
    mime = "text/plain"
    format = Formatting(["colors"], env=Environment())
    assert format.format_body(text, mime) == text
    mime = "text/html"
    format = Formatting(["colors"], env=Environment())
    assert format.format_body(text, mime) == text
    mime = "text/html"
    format = Formatting(["colors"], env=Environment(colors=True))
    assert format.format_body(text, mime) == text

# Generated at 2022-06-13 22:19:40.737611
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Step 1. Data
    converter = Conversion.get_converter('text/json')
    assert converter.text == '{"test": "value"}'
    assert converter.mime == 'application/json'

# Generated at 2022-06-13 22:19:46.067837
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    group_list = ['colors']
    formatting_obj = Formatting(group_list, env)

# Generated at 2022-06-13 22:20:01.982138
# Unit test for constructor of class Formatting
def test_Formatting():
    """
    For unit test of Formatting class, I need to create a instance of class
    Formatting.
    """
    formater = Formatting(['color', 'colors']).format_body('{color: red}', 'text/json')
    assert formater.find('\033[') != -1
    formater = Formatting(['color', 'colors']).format_body('{color: red}', 'format')
    assert formater.find('\033[') != -1
    formater = Formatting(['color', 'colors']).format_body('{color: red}', 'application/json')
    assert formater.find('\033[') == -1

# Generated at 2022-06-13 22:20:05.521325
# Unit test for constructor of class Formatting
def test_Formatting():
    #array of strings
    a = Formatting(groups=['colors'])
    assert a.enabled_plugins is not None
    assert type(a.enabled_plugins) == list



# Generated at 2022-06-13 22:20:15.183174
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not Conversion.get_converter('text/html;')
    assert not Conversion.get_converter('text/plain')
    assert not Conversion.get_converter('unknown;')
    assert Conversion.get_converter('json')
    assert Conversion.get_converter('JSON')
    assert Conversion.get_converter('json;')
    assert Conversion.get_converter('json;charset=UTF-8')
    assert Conversion.get_converter('application/json;charset=UTF-8')
    assert Conversion.get_converter('application/vnd.github.v3+json;charset=UTF-8')

# Generated at 2022-06-13 22:20:22.437076
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    class TestPlugin:
        def __init__(self, env=Environment(), **kwargs):
            self.enabled = True
        def format_headers(self, headers: str) -> str:
            return headers
    available_plugins = {'color': [TestPlugin]}
    formatting = Formatting(['color'], available_plugins=available_plugins)
    assert formatting.format_headers("\n") == '\n'


# Generated at 2022-06-13 22:20:35.470966
# Unit test for constructor of class Formatting
def test_Formatting():
    from mock import MagicMock
    from httpie.plugins import FormatterPlugin
    http = Formatting(['default'])
    assert http.enabled_plugins == []
    http1 = Formatting(['default', 'highlight'], c='abc')
    assert http1.enabled_plugins[0].env.colors == 'abc'

# Generated at 2022-06-13 22:20:41.857328
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    class ConverterPluginMock(ConverterPlugin):
        @staticmethod
        def supports(mime):
            return mime.startswith("mime_to_be_tested")

        def decode(self, body):
            return body

    plugin_manager.converters["test_Conversion_get_converter"] = ConverterPluginMock

    plugin_manager.load_converters()

    mime = "mime_to_be_tested_abc"

    assert Conversion.get_converter(mime).name == "test_Conversion_get_converter"



# Generated at 2022-06-13 22:20:44.884332
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('media/image')
    assert isinstance(Conversion.get_converter('media/image'), ConverterPlugin)


# Generated at 2022-06-13 22:20:55.743410
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_cases = [
        # no params, output is the same as input
        (
            'a=1',
            {},
            {},
            'a=1'
        ),
        (
            '',
            {},
            {},
            ''
        ),
        # pretty
        (
            'a=1&b=2',
            {'pretty': 'all'},
            {},
            'a = 1\nb = 2'
        ),
        (
            'a=1&b=2',
            {'pretty': 'colors'},
            {},
            '[36ma[0m = [32m1[0m\n[36mb[0m = [32m2[0m'
        )
    ]

# Generated at 2022-06-13 22:20:57.582882
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json")



# Generated at 2022-06-13 22:21:07.557878
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    html_content = """
<html><body>
<h1>Welcome to the minimal HTTP server!</h1>
<p>You are requesting: /</p>
<p>The system has the following commands:</p>
<p>
<ul>
<li><a href="/switchOn">switchOn</a>
<li><a href="/switchOff">switchOff</a>
<li><a href="/getStatus">getStatus</a>
</ul>
</p>
</body></html>"""
    p = Conversion.get_converter("text/html")
    assert p is not None
    assert p.prettify(html_content)


if __name__ == '__main__':
    test_Conversion_get_converter()

# Generated at 2022-06-13 22:21:15.931138
# Unit test for constructor of class Formatting
def test_Formatting():
    """
    Test if constructor of class Formatting is correct.
    """
    x = Formatting(["group1", "group2"])

# Unit tests for function format_headers of class Formatting

# Generated at 2022-06-13 22:21:17.568124
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(['colors'], False)
    assert f.enabled_plugins

# Generated at 2022-06-13 22:21:23.955221
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(["colors"])
    assert f.format_body("ciao", "text") == "ciao"
    assert f.format_body("ciao", "application/json") == '\x1b[94mciao\x1b[0m'
    f = Formatting(["colors", "format", "format_options"])
    assert f.format_body("ciao", "application/json") == '\x1b[94mciao\x1b[0m'

# Generated at 2022-06-13 22:21:30.257362
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('txt') is None
    assert Conversion.get_converter('text/plain') is not None
    assert Conversion.get_converter('application/json') is not None
    assert Conversion.get_converter('apgli/json') is None
    assert Conversion.get_converter('application/json;charset=utf-8') is not None

test_Conversion_get_converter()

# Generated at 2022-06-13 22:21:32.788450
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter is not None
    assert converter.name == 'json'



# Generated at 2022-06-13 22:21:36.402969
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.core import main
    from httpie.compat import is_windows
    try:
        main(['https://httpbin.org/json'])
    except SystemExit as e:
        assert str(e) == '0'

# Generated at 2022-06-13 22:21:44.122161
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:21:51.467381
# Unit test for constructor of class Formatting
def test_Formatting():
    import httpie.plugins.builtin.__main__
    env = Environment()
    httpie.plugins.builtin.__main__.configure(env)
    formatting = Formatting(groups=["colors", "formatting", "syntax_highlighting"], env=env)
    assert len(formatting.enabled_plugins) == 3
    assert formatting.enabled_plugins[0].name == "Colors"
    assert formatting.enabled_plugins[1].name == "Formatted JSON"
    assert formatting.enabled_plugins[2].name == "Solarized"
    assert formatting.format_body("Test", "text/plain") == "Test"

# Generated at 2022-06-13 22:21:53.867030
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    Conversion.get_converter('application/json')


# Generated at 2022-06-13 22:22:06.686303
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import os
    import json

    # build the environment
    env = Environment()
    env.config.colors.headers = False
    env.config.colors.body = False

    # build the Formatting object
    formatting = Formatting(groups=['colors'], env=env)

    # setup the input headers
    s = json.dumps({'Headers': ["HTTP/1.1 200 OK\r", "Server: nginx/1.12.2\r"]})

    # call the method
    result = formatting.format_headers(s)

    # assert the result
    expected = json.dumps({'Headers': "HTTP/1.1 200 OK\nServer: nginx/1.12.2\n"})
    assert result == expected
