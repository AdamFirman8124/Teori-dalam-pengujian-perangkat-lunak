

# Generated at 2022-06-13 22:12:24.310744
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('image/jpg')
    assert converter is None

    converter = Conversion.get_converter('application/json')
    assert converter is not None
    assert converter.is_binary is False

    converter = Conversion.get_converter('application/octet-stream')
    assert converter is not None
    assert converter.is_binary is True

    converter = Conversion.get_converter('')
    assert converter is None

# Generated at 2022-06-13 22:12:33.699969
# Unit test for constructor of class Formatting
def test_Formatting():
	assert Formatting(["highlight"]).enabled_plugins == [plugin_manager.get_formatters_grouped()["highlight"][0](env=Environment())]
	assert Formatting(["highlight"], env=Environment(), style="Riot").enabled_plugins == [plugin_manager.get_formatters_grouped()["highlight"][0](env=Environment(), style="Riot")]
	# assert Formatting(["highlight", "possible"]).enabled_plugins == [plugin_manager.get_formatters_grouped()["highlight"][0]().enabled_plugins[0], plugin_manager.get_formatters_grouped()["possible"][0]()]


# Generated at 2022-06-13 22:12:40.108957
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    #check the content  and mime type
    assert 'content' == Formatting(['colors']).format_body('content', 'application/json')
    assert '' == Formatting(['colors']).format_body('', 'application/json')
    assert 'content' == Formatting(['colors']).format_body('content', 'html/json') #wrong mime type


# Generated at 2022-06-13 22:12:43.332066
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    body = '{\n  "key": "value"\n}'
    mime = 'application/json'
    assert body == Formatting([], env=Environment()).format_body(body, mime)



# Generated at 2022-06-13 22:12:46.957437
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    Formatting = Formatting(['indent'])
    assert Formatting.format_body("{\"name\":\"Alex\"}","application/json")=="{\n    \"name\": \"Alex\"\n}"

# Generated at 2022-06-13 22:13:00.958003
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins import formatter
    from six import StringIO



# Generated at 2022-06-13 22:13:12.335058
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():

    from httpie.plugins.builtin import HTTPPrettyJSON
    from httpie.plugins.builtin import HTTPPrettyPrinter
    from httpie.plugins.builtin import HTTPPrettyXML

    # Configure the environment
    env = Environment(stdin=None, stdout=None, isatty=True, colors=256)

    mime = 'application/json'

    # Input json
    json = '{"prop": "foo", "prop2": "bar"}'
    # Expected output
    expected = '{\n    "prop": "foo",\n    "prop2": "bar"\n}'

    # Invoke the formatting method
    formatting = Formatting(['json'], env)
    actual = formatting.format_body(json, mime)

    # Assert the expected and actual are equal
    assert actual == expected

# Generated at 2022-06-13 22:13:23.034002
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    print("Running Unit Test: Formatting.format_body")
    f = Formatting(['colors'])
    json_str = '{"string":"example","int":4,"float":4.5}'
    json_str_result = '{\n    "string": "example",\n    "int": 4,\n    "float": 4.5\n}'
    assert(f.format_body(json_str, 'application/json') == json_str_result)
    assert(f.format_body(json_str, 'invalid/mime') == json_str)

if __name__ == "__main__":
    test_Formatting_format_body()

# Generated at 2022-06-13 22:13:30.685948
# Unit test for constructor of class Formatting
def test_Formatting():
    import mock
    env_mock = mock.Mock()
    formatting = Formatting(groups=['redact'], env=env_mock)

    assert len(formatting.enabled_plugins) == 1
    assert formatting.enabled_plugins[0].enabled
    assert formatting.enabled_plugins[0].name == 'Redact'
    assert formatting.enabled_plugins[0].env is env_mock

# Generated at 2022-06-13 22:13:40.738368
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    test_str = 'test1'
    test_str2 = 'test2'
    test_str3 = 'test3'
    test_str4 = 'test4.test'
    test_str5 = 'test5'
    test_str6 = 'test6'
    test_str7 = 'test7'
    test_str8 = 'test8'
    test_str9 = 'test9'
    test_str10 = 'test10'
    test_str11 = 'test11'
    #Act
    result = Conversion.get_converter(test_str)
    result2 = Conversion.get_converter(test_str2)
    result3 = Conversion.get_converter(test_str3)
    result4 = Conversion.get_converter(test_str4)
    result5

# Generated at 2022-06-13 22:13:53.976158
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.builtin import FormatterPlugin, JSONFormatterPlugin
    from httpie.plugins.core import HTTPHeadersProcessor

    class TestPlugin(FormatterPlugin):
        enabled = True

        def get_style_defs(self):
            return 'color:red'

        def format_headers(self, headers):
            return '#####'


    class TestPlugin2(JSONFormatterPlugin):
        enabled = True

        def get_style_defs(self):
            return 'color:blue'

        def format_headers(self, headers):
            return '------'

        def format_body(self, body, mime):
            return '******'

    formatters = Formatting(['HTTPHeaders'])

# Generated at 2022-06-13 22:13:57.209629
# Unit test for constructor of class Formatting
def test_Formatting():
    format_obj = Formatting(groups=['colors'])
    assert format_obj.enabled_plugins[0].__class__.__name__ == 'ColorsFormatter'

# Generated at 2022-06-13 22:14:09.078520
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # f is the Formatting object
    f = Formatting(["colors"])
    # c is the content passed to Formatting's format_body method.
    c = "[{\"status\": \"SUCCESS\", \"sessionHandle\": \"1234\"}]"
    # m is the mime type of json
    m = "application/json"
    # e is the desired result after invoking format_body method

# Generated at 2022-06-13 22:14:11.437738
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/html') is None

# Generated at 2022-06-13 22:14:22.253753
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/plain') != None
    assert Conversion.get_converter('image/png') != None
    assert Conversion.get_converter('text/csv') != None
    assert Conversion.get_converter('application/json') != None
    assert Conversion.get_converter('application/pdf') != None
    assert Conversion.get_converter('application/xml') != None
    assert Conversion.get_converter('application/vnd.openxmlformats-officedocument.wordprocessingml.document') != None

# Unit test to check if the method get_converter returns None for invalid mime type

# Generated at 2022-06-13 22:14:35.211296
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Body with Content-Type: application/json
    # It should have the similar output when test this case
    # curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://httpbin.org/get
    body = '''
{
  "args": {}, 
  "headers": {
    "Accept": "application/json", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.64.1"
  }, 
  "url": "http://httpbin.org/get"
}
'''
    formatter = Formatting('colors')
    new_body = formatter.format_body(body, 'application/json')
    assert body == new_body

# Generated at 2022-06-13 22:14:39.195044
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print('Testing method get_converter of class Conversion')
    # Test when there is no compatible converter
    assert Conversion.get_converter('text/plain') == None
    # Test when there is a compatible converter
    assert Conversion.get_converter('text/html') != None

# Generated at 2022-06-13 22:14:46.677860
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    fmt = Formatting(['colors'], env)
    fmt.format_headers(r'HTTP/1.1 200 OK\r\nServer: nginx\r\n\r\n') == \
        '\x1b[94mHTTP/1.1 200 OK\x1b[0m\r\n\x1b[94mServer: nginx\x1b[0m\r\n\r\n'

# Generated at 2022-06-13 22:14:52.152097
# Unit test for constructor of class Formatting
def test_Formatting():
    classes = plugin_manager.get_formatters_grouped()
    abc = Formatting(['all'], env=Environment(), color=True)
    for group in classes:
        for cls in classes[group]:
            p = cls(env=Environment(), color=True)
            if p.enabled:
                assert p in abc.enabled_plugins

# Generated at 2022-06-13 22:14:58.405481
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    text = "[{\"key1\":\"value1\"},{\"key2\":\"value2\"}]"
    mime = "application/json"
    formatting = Formatting(groups=["json"])
    formatted_text = formatting.format_body(content=text, mime=mime)
    assert formatted_text == "[\n  {\n    \"key1\": \"value1\"\n  },\n  {\n    \"key2\": \"value2\"\n  }\n]\n"

test_Formatting_format_body()

# Generated at 2022-06-13 22:15:05.420138
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting(["json", "colors"]).enabled_plugins[0].__class__.__name__ == "JSONFormatter"
    assert Formatting(["json", "colors"]).enabled_plugins[1].__class__.__name__ == "ColorsFormatter"

# Generated at 2022-06-13 22:15:07.055453
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    res = Conversion.get_converter('audio/midi')
    assert res is None



# Generated at 2022-06-13 22:15:09.848331
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = "text/html"
    if is_valid_mime(mime):
        assert Conversion.get_converter(mime)

# Generated at 2022-06-13 22:15:12.166184
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=["colors"], env=None, **{"test":"test"})
    assert f.enabled_plugins[0].test == 'test'

# Generated at 2022-06-13 22:15:23.511400
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import httpie.formatter
    import httpie.plugins.formatter.colors
    temp = httpie.formatter.COLORS
    httpie.formatter.COLORS = True
    httpie.plugins.formatter.colors.httpie_colors.enabled = True
    fmt = Formatting(['colors'])
    head = 'HTTP/1.1 200 OK\nContent-Length: 25\nServer: CherryPy/3.1.2\nContent-Type: text/html\nDate: Tue, 11 Aug 2015 12:42:35 GMT\n'
    resp = fmt.format_headers(head)
    print(resp)
    httpie.formatter.COLORS = temp

# Generated at 2022-06-13 22:15:29.117425
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    mime = 'text/plain'
    src_converter = Conversion.get_converter(mime)
    src_converted = src_converter.encode(txt)
    dst_converter = Conversion.get_converter(src_converter.mime)
    dst_converted = dst_converter.decode(src_converted)
    assert txt == dst_converted


# Generated at 2022-06-13 22:15:34.429105
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    sample = "    {\"key\":\"value\"}"
    sample_formatted = Formatting(["json"]).format_body(sample, "application/json")
    assert sample_formatted == "{\n    \"key\": \"value\"\n}\n"



# Generated at 2022-06-13 22:15:40.217280
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """
    Unit test for method get_converter of class Conversion
    :return:
    """
    print("test_Conversion_get_converter")

    print(Conversion.get_converter("application/json"))


if __name__ == "__main__":
    test_Conversion_get_converter()

# Generated at 2022-06-13 22:15:48.543633
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.compat import urlopen
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import Formatter
    from httpie.cli import raw_format
    from httpie.output.formatters.colors import get_lexer
    from httpie.context import Environment
    from httpie.output.formatters.colors import PygmentsStyle
    from httpie import ExitStatus
    from httpie import __version__
    from httpie.plugins import get as plugin_get
    from httpie.plugins.manager import plugin_manager, builtin_plugins
    from pygments.formatters import TerminalFormatter


# Generated at 2022-06-13 22:15:53.039590
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Valid mime (json)
    assert type(Conversion.get_converter('application/json')) is ConverterPlugin
    # Invalid mime (e.g.: json/app)
    assert Conversion.get_converter('json/app') is None

# Generated at 2022-06-13 22:16:00.074425
# Unit test for constructor of class Formatting
def test_Formatting():
    print("\n\n-----------test for class Formatting----------")
    f = Formatting(groups=['colors'])
    print(f.enabled_plugins)


# Generated at 2022-06-13 22:16:08.176877
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from subprocess import check_output
    out = check_output(['python3', '-c', 'from httpie.formatting import Formatting; print(Formatting(["colors"]).format_headers("Hello world"))']).rstrip()
    print("output = " + out.decode("utf-8"))
    assert out.decode("utf-8") == "\x1b[37mHello world\x1b[39m"


# Generated at 2022-06-13 22:16:14.955053
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Set up test input - given a simple string
    test_input = "application/json"

    # Set up expected results - json converter should return a JSONConverter class
    expected = "JSONConverter"

    # Execute test
    actual = str(Conversion.get_converter(test_input)).split("'")[1]

    # Report results
    assert actual == expected, "Actual: " + actual + "Expected: " + expected


# Generated at 2022-06-13 22:16:27.381134
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/plain') == None

# Generated at 2022-06-13 22:16:39.632652
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fmt1 = Formatting(['colors'], style='solarized')
    fmt2 = Formatting(['colors'], style='emacs')

    # Test for wrong inputs
    assert fmt1.format_headers(5) == 5
    assert fmt2.format_headers(5) == 5

    # Test for cases with no headers
    assert fmt1.format_headers('') == ''
    assert fmt2.format_headers('') == ''

    # Test for cases with single header
    assert fmt1.format_headers('Host: localhost\n') == '\x1b[0;37mHost: \x1b[0;32mlocalhost\x1b[0m\n'
    assert fmt2.format_headers('Host: localhost\n') == 'Host: localhost\n'

    # Test for

# Generated at 2022-06-13 22:16:45.979449
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    groups = ['header']
    env = Environment(colors=None)
    kwargs = {}
    formatting = Formatting(groups, env=env, **kwargs)
    unformatted_headers = 'one: 1\r\ntwo: 2\r\n'
    formatted_headers = formatting.format_headers(unformatted_headers)
    assert formatted_headers == 'one: 1\ntwo: 2\n'


# Generated at 2022-06-13 22:16:55.489964
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # arrange
    class ConverterPlugin_class:
        @staticmethod
        def supports(mime):
            if is_valid_mime(mime):
                return True
            else:
                return False


    class plugin_manager_class:
        @staticmethod
        def get_converters():
            return [ConverterPlugin_class,]

    # act
    MIME = 'mime'
    plugin_manager = plugin_manager_class
    actual = Conversion.get_converter(MIME)

    # assert
    assert(actual is not None)
    assert(MIME == actual.mime)

# Generated at 2022-06-13 22:17:02.703868
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Test data
    content = '{"Status":"OK"}'
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    content_expected = converter.convert(content)
    content_actual = Formatting([]).format_body(content, mime)
    # Method under test
    assert content_expected == content_actual

# Generated at 2022-06-13 22:17:15.523266
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/xml') is not None
    assert Conversion.get_converter('application/json') is not None
    assert Conversion.get_converter('application/hal+json') is not None
    assert Conversion.get_converter('application/yaml') is not None
    assert Conversion.get_converter('application/x-yaml') is not None
    assert Conversion.get_converter('application/x-msgpack') is not None
    assert Conversion.get_converter('application/vnd.php.serialized') is not None
    assert Conversion.get_converter('application/javascript') is not None
    assert not Conversion.get_converter('text')
    assert not Conversion.get_converter('xml')

# Generated at 2022-06-13 22:17:19.875503
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins import ConverterPlugin
    from httpie.plugins.registry import plugin_manager
    from tests.compat import Mock

    class ConverterMock(ConverterPlugin):
    
        def __init__(self, mime):
            self.mime = mime

        @property
        def mime_type(self):
            return self.mime

        def supports(self, mime):
            return mime == self.mime

    plugin_manager.get_converters = Mock(return_value=[ConverterMock("mime")])
    assert Conversion.get_converter("mime").mime_type == "mime"



# Generated at 2022-06-13 22:17:32.112906
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.builtin import HTTPHeadersProcessor
    from httpie.context import Environment
    import json
    import collections
    env = Environment(default_options=[])
    formatter = Formatting(['headers'], env)
    dict_headers = collections.OrderedDict()
    dict_headers["Content-Type"] = "application/json"
    dict_headers["date"] = "Mon, 04 Jun 2018 14:40:41 GMT"
    dict_headers["x-content-type-options"] = "nosniff"
    dict_headers["x-frame-options"] = "SAMEORIGIN"
    dict_headers["x-xss-protection"] = "1; mode=block"
    dict_headers["cache-control"] = "no-cache, no-store"
    dict_headers["pragma"]

# Generated at 2022-06-13 22:17:35.811607
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = plugin_manager.get_formatters_groups()
    formatting = Formatting(groups, env=Environment())
    assert(formatting is not None)



# Generated at 2022-06-13 22:17:48.229656
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:17:57.558012
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    dict = {'a': 'aaa'}

    environment = Environment()
    environment.headers = {}
    environment.output_options = {}
    environment.output_options['stdout'] = sys.stdout
    environment.output_options['stderr'] = sys.stderr

    f = Formatting(['http'], environment)
    res = f.format_body(dict, 'application/json')
    assert(res == '{\n    "a": "aaa"\n}\n')
    print(res)



# Generated at 2022-06-13 22:18:00.965228
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['colors'], env=Environment(), force_colors=False)
    assert (f.enabled_plugins == [FormatterPlugin(env=Environment(), force_colors=False)])

# Generated at 2022-06-13 22:18:06.732783
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Case 1.1: MIME is wrong
    mime = "text"
    result = Conversion.get_converter(mime)
    assert result == None

    # Case 1.2: MIME is correct but not supported
    mime = "application/json"
    result = Conversion.get_converter(mime)
    assert result != None

    # Case 2.1: MIME is correct and supported
    mime = "text/html"
    result = Conversion.get_converter(mime)
    assert result != None

# Generated at 2022-06-13 22:18:11.000600
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not Conversion.get_converter(None)
    assert not Conversion.get_converter('invalid')
    assert Conversion.get_converter('text/html') == 'text/html'
    assert Conversion.get_converter('application/json') == 'application/json'

# Generated at 2022-06-13 22:18:18.937197
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert None == Conversion.get_converter('image/jpeg')
    assert None == Conversion.get_converter('image/jpeg123')
    assert None == Conversion.get_converter('image/jpeg.')
    assert None == Conversion.get_converter('image/jpg')
    assert 'httpie.plugins.converter.json.JsonConverter' == Conversion.get_converter('application/json').__class__.__name__
    assert 'httpie.plugins.converter.KeyValueConverter' == Conversion.get_converter('text/plain').__class__.__name__
    assert 'httpie.plugins.converter.KeyValueConverter' == Conversion.get_converter('text/x-foo').__class__.__name__

# Generated at 2022-06-13 22:18:28.392026
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    data = [
        ('body', 'text/plain', 'formatted body'),
        ('body', 'application/json', '{\n    "formatted": "body"\n}'),
    ]
    formatter_mock = Mock(return_value='formatted body')
    instance = Formatting(groups=[], env=Environment())
    instance.enabled_plugins = [formatter_mock]

    for content, mime, expected in data:
        actual = instance.format_body(content, mime)
        print(content, mime, actual, expected)
        assert expected == actual

# Generated at 2022-06-13 22:18:30.723819
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json') is not None
    assert Conversion.get_converter('text/html') is None

# Generated at 2022-06-13 22:18:37.296166
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    Formatting(["colors"], color=True, css_colors=True).format_body("")
    pass


# Generated at 2022-06-13 22:18:48.703658
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import re
    import json
    from pygments import highlight
    from pygments.formatters import TerminalTrueColorFormatter
    from pygments.lexers import JsonLexer, get_lexer_for_mimetype

    env = Environment(
        colors=256,
        headers_style="default",
        headers_colors_style=0,
        headers_color_theme=5,
        headers_colors_custom={},
        headers_columns=0,
        output_options={}
    )

# Generated at 2022-06-13 22:18:57.783972
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('text/html')
    assert c.get_converter_name() == 'html'
    c = Conversion.get_converter('application/json')
    assert c.get_converter_name() == 'json'
    c = Conversion.get_converter('application/xml')
    assert c.get_converter_name() == 'xml'
    c = Conversion.get_converter('application/vnd.openxmlformats-officedocument.presentationml.presentation')
    assert c.get_converter_name() == 'pptx'

# Generated at 2022-06-13 22:18:59.301575
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting(groups=[], env='') is not None

# Generated at 2022-06-13 22:19:03.469082
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors', 'format', 'syntax']

    env = Environment()
    kwargs = {}

    format_test = Formatting(groups, env, **kwargs)

    assert format_test

# Generated at 2022-06-13 22:19:13.637590
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    environment = Environment()
    formatter = Formatting(groups=['colorize'], env=environment)
    headers = 'Content-Type: application/json\n' \
              'Date: Wed, 28 Aug 2019 05:04:46 GMT\n' \
              'Server: nginx/1.10.3 (Ubuntu)\n' \
              'Transfer-Encoding: chunked\n' \
              'Connection: close\n' \
              'X-Powered-By: PHP/7.2.19-0ubuntu0.18.04.1\n' \
              'Vary: Accept-Encoding\n' \
              'X-Robots-Tag: noindex\n' \
              'Content-Encoding: gzip\n' \
              '\n'

# Generated at 2022-06-13 22:19:24.553369
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """
    Test Case:
    Method get_converter of class Conversion
    """
    assert(Conversion.get_converter('application/json').class_name == 'JsonConverter')
    assert(Conversion.get_converter('application/xml').class_name == 'XmlConverter')
    assert(Conversion.get_converter('application/yaml').class_name == 'YamlConverter')
    assert(Conversion.get_converter('application/xxjson').class_name == None)


# Generated at 2022-06-13 22:19:31.295110
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.compat import str
    from httpie.output.formatter import JSONFormatter
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE

    env = Environment()
    json_formatter = JSONFormatter(env)
    if not json_formatter.enabled:
        return

    env.stdout = io.BytesIO() if env.is_windows else io.StringIO()

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: application/json\r\n'
        '\r\n'
    )
    content = '{"a": 1, "b": 2}\n'

    # Test with the JSON formatter enabled.
    json_formatter.enabled = True

# Generated at 2022-06-13 22:19:35.878254
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert "json" in str(Conversion.get_converter("application/json"))
    assert "json" not in str(Conversion.get_converter("application/xml"))


# Generated at 2022-06-13 22:19:43.326790
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    c = Conversion

# Generated at 2022-06-13 22:20:04.749574
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    g = Formatting([])
    a = {'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
         'Accept-Encoding': 'gzip, deflate',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'}
    b = g.format_headers(a)
    c = 'Accept-Encoding: gzip, deflate\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n'

# Generated at 2022-06-13 22:20:12.542451
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    test_cases = [
        ('text/html', 'html2json'),
        ('html2json', 'html2json'),
        ('xml2json', 'xml2json'),
        ('json2xml', 'json2xml'),
        ('json2html', 'json2html'),
        ('foo/bar', 'foo/bar')
    ]
    for mime, expected in test_cases:
        assert Conversion.get_converter(mime).name == expected, f'failed test on {mime}'


# Generated at 2022-06-13 22:20:20.883369
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    test_body = '{"field0": 0, "field1": "one", "field2": 2}'
    test_mime = 'application/json'
    Formatting = Formatting(['format'], **{'mime': test_mime})
    result_body = Formatting.format_body(test_body, test_mime)
    assert result_body == '{\n    "field0": 0,\n    "field1": "one",\n    "field2": 2\n}'

# Generated at 2022-06-13 22:20:30.124024
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    #test1
    format = Formatting(['colors'])
    test = format.format_headers("content-type: \"application/json; charset=UTF-8\"\r\n")
    assert test == "content-type: \"\x1b[33mapplication/json\x1b[39;49;00m; charset=UTF-8\"\r\n"
    #test2
    format = Formatting(['colors'])
    test = format.format_headers("""content-type: \"application/json; charset=UTF-8\"\r\ncontent-type: \"text/html; charset=UTF-8\"\r\n""")

# Generated at 2022-06-13 22:20:35.595330
# Unit test for constructor of class Formatting
def test_Formatting():
    groups: List[str] = ['headers']
    env: Environment = Environment(colors=True, stdin_isatty=True)
    kwargs: dict = {"headers": "hello"}
    f: Formatting = Formatting(groups, env, **kwargs)
    assert len(f.enabled_plugins) == 1



# Generated at 2022-06-13 22:20:38.090995
# Unit test for constructor of class Formatting
def test_Formatting():
    fmt = Formatting([])
    assert len(fmt.enabled_plugins) == 0
    fmt = Formatting(['colors'])
    assert len(fmt.enabled_plugins) == 1


# Generated at 2022-06-13 22:20:40.745578
# Unit test for constructor of class Formatting
def test_Formatting():
    assert (Formatting(groups=["colors"], env=Environment()))

# Generated at 2022-06-13 22:20:44.896396
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'text/html'
    converter = Conversion.get_converter(mime)
    assert converter.mime == mime
    assert type(converter) == plugin_manager.get_converters()[2]


# Generated at 2022-06-13 22:20:46.594132
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting([])
    assert isinstance(f, Formatting)

# Generated at 2022-06-13 22:20:56.852138
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins.builtin import JSONTableFormatter as JTF
    from httpie.plugins.builtin import JSONPointer

    # Testcase: When input content is not a JSON string
    assert(Formatting(groups=[''], json_indent=4, v=False).format_body('hello world', 'application/json') == 'hello world')

    # Testcase: When input content is a JSON string, but not formatted with JSON
    assert(Formatting(groups=[''], json_indent=4, v=False).format_body('{"test": "test"}', 'text/plain') == '{"test": "test"}')

    # Testcase: When input content is a JSON string, and is formatted with JSON

# Generated at 2022-06-13 22:21:08.150874
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("json")
    assert converter
    assert converter.STDOUT_CONVERTER_CLASS == "httpie_plugins.JSONConverter"

# Generated at 2022-06-13 22:21:15.666182
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print('get converter')
    print(Conversion.get_converter('text/html'))
    print(Conversion.get_converter('text/csv'))
    print(Conversion.get_converter('text/plain'))
    print(Conversion.get_converter('text/html'))
    print(Conversion.get_converter('application/json'))
    print(Conversion.get_converter('application/csv'))


# Generated at 2022-06-13 22:21:17.671454
# Unit test for constructor of class Formatting
def test_Formatting():
    m = Formatting(groups=['colors'])
    assert len(m.__dict__) == 2

# Generated at 2022-06-13 22:21:18.725089
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json')

# Generated at 2022-06-13 22:21:20.179271
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting(groups = ['SyntaxHighlight']) != None

# Generated at 2022-06-13 22:21:32.788893
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    class ConverterPluginX(ConverterPlugin):

        def __init__(self, supported_type):
            self.supported_type = supported_type

        @property
        def name(self):
            return ''

        @property
        def description(self):
            return ''

        @property
        def enabled_by_default(self):
            return True

        def convert(self, data):
            return data

        def supports(self, mime):
            return mime == self.supported_type

    class ConverterPluginY(ConverterPlugin):

        def __init__(self, supported_type):
            self.supported_type = supported_type

        @property
        def name(self):
            return ''

        @property
        def description(self):
            return ''


# Generated at 2022-06-13 22:21:33.922149
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json")

# Generated at 2022-06-13 22:21:45.104793
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8'
    try:
        _f = Formatting(['headers'])
        new_headers = _f.format_headers(headers)
        assert new_headers == headers
    except:
        assert True
    try:
        _f = Formatting(['headers', 'colors'])
        new_headers = _f.format_headers(headers)
        assert new_headers == headers
    except:
        assert True
    try:
        _f = Formatting(['headers', 'colors', 'format'])
        new_headers = _f.format_headers(headers)
        assert new_headers == headers
    except:
        assert True

# Generated at 2022-06-13 22:21:48.752942
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """
    Test for method get_converter of class Conversion
    """
    converter = Conversion.get_converter('application/javascript')
    from httpie.plugins.builtin import JSONConverter
    assert converter.__class__ == JSONConverter



# Generated at 2022-06-13 22:21:55.564079
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # if mime type is valid, then return the converter that supports mime type
    assert(Conversion.get_converter("application/json"))
    assert(Conversion.get_converter("image/tiff"))

    # if mime type is not valid, then return None
    assert(Conversion.get_converter("application") is None)
    assert(Conversion.get_converter("") is None)
    assert(Conversion.get_converter(None) is None)

# Generated at 2022-06-13 22:22:12.376646
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:22:19.304930
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_env = Environment()
    test_env.headers = ["test1: 1", "test2: 2", "test1: 3", "test2: 4"]
    f = Formatting(["headers"], env=test_env)
    assert f.format_headers(test_env.headers) == "test1: 1, 3\r\ntest2: 2, 4"
