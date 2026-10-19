

# Generated at 2022-06-13 22:12:19.796993
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    groups: List[str] = ["format", "colors"]
    formatting = Formatting(groups=groups, env=env)
    print(formatting.enabled_plugins)
    print(formatting.format_body("abc", ""))


# Generated at 2022-06-13 22:12:26.105048
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json")
    assert Conversion.get_converter("text/html")
    assert not Conversion.get_converter("image/jpeg")
    assert not Conversion.get_converter("test")
    assert not Conversion.get_converter("test/test")
    assert not Conversion.get_converter("test/test/test")

# Generated at 2022-06-13 22:12:33.548733
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # 测试json转换器
    json_converter = Conversion.get_converter('application/json')
    assert isinstance(json_converter, ConverterPlugin)
    assert json_converter.mime == 'application/json'

    # 测试xml转换器
    xml_converter = Conversion.get_converter('application/xml')
    assert isinstance(xml_converter, ConverterPlugin)
    assert xml_converter.mime == 'application/xml'

# Generated at 2022-06-13 22:12:39.647359
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["json", "xml", "html"]
    env = Environment()
    available_plugins = plugin_manager.get_formatters_grouped()
    assert len(env.format_options) == 0
    assert available_plugins.keys() == {'colors', 'colors-light', 'colors-256', 'colors-16', 'json', 'xml', 'html'}
    a = Formatting(groups, env)
    assert len(a.enabled_plugins) == 3
    assert len(a.enabled_plugins[2].env.format_options) == 0
    assert a.enabled_plugins[2].enabled == True
    assert a.enabled_plugins[2].env == env


# Generated at 2022-06-13 22:12:41.478132
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("image")



# Generated at 2022-06-13 22:12:46.478731
# Unit test for constructor of class Formatting
def test_Formatting():
    # Unit test for empty groups
    formatting = Formatting([])
    assert formatting._enabled_plugins == []

    # Unit test for not empty groups
    formatting = Formatting(["json", "colors"])
    assert len(formatting._enabled_plugins) > 0

# Generated at 2022-06-13 22:12:48.221306
# Unit test for constructor of class Formatting
def test_Formatting():
    # construct object
    fmt = Formatting(['colors'])
    assert fmt.enabled_plugins

# Formatting.format_headers test case

# Generated at 2022-06-13 22:12:50.907749
# Unit test for constructor of class Formatting
def test_Formatting():
    json_groups = ["json"]
    env = Environment()
    formatting = Formatting(json_groups, env)
    assert formatting.enabled_plugins == [], "enabled_plugins should be empty"
    assert formatting.enabled_plugins != None, "enabled_plugins should not be None"



# Generated at 2022-06-13 22:12:53.256103
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors']
    f = Formatting(groups)
    assert  f.format_body('', 'application/json') == ''

# Generated at 2022-06-13 22:13:04.198989
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = 'HTTP/1.1 200 OK\r\nServer: nginx\r\nDate: Thu, 18 Feb\
            2016 05:42:51 GMT\r\nContent-Type: application/json\r\n\
            Content-Length: 24\r\nConnection: keep-alive'
    #test for group all
    f = Formatting(groups=['all'],
                   prefs={'format': 'all', 'colors': False, 'style': 'friendly'})
    assert(f.format_headers(headers) == 'HTTP/1.1 200 OK\nServer: nginx\nDate: Thu, 18 Feb 2016 05:42:51 GMT\n\
Content-Type: application/json\nContent-Length: 24\nConnection: keep-alive')
    #test for group headers
    f = Formatting

# Generated at 2022-06-13 22:13:12.328811
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting([])
    assert Formatting(['isatty'])
    assert Formatting(['isatty', 'colors'])
    assert Formatting(['isatty', 'colors', 'format'])
    assert Formatting(['isatty', 'colors', 'format', 'pretty'])


# Generated at 2022-06-13 22:13:24.905665
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import httpie.plugins.builtin

    available_plugins = plugin_manager.get_formatters_grouped()
    f = Formatting(["formatting"])

    # Test case where formatting plugins are enabled
    headers = "HTTP/1.1 200 OK\r\nAccept-Encoding: gzip\r\nUser-Agent: HTTPie/0.9.9\r\nConnection: keep-alive\r\nServer: gunicorn/19.9.0\r\nDate: Sun, 04 Nov 2018 02:56:04 GMT\r\n\r\n"

# Generated at 2022-06-13 22:13:34.169194
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Test for Base16Processor
    f = Formatting(groups=['b16'])
    headers = 'Content-Type:application/json'
    formatted_headers = f.format_headers(headers)
    assert 'Content-Type:application/json' == formatted_headers

    # Test for PrettyPrint
    f = Formatting(groups=['pretty'])
    headers = 'Content-Type:application/json'
    formatted_headers = f.format_headers(headers)
    assert 'Content-Type: application/json' == formatted_headers


# Generated at 2022-06-13 22:13:39.524760
# Unit test for constructor of class Formatting
def test_Formatting():
    mime = "text/plain"
    groups = ["formatters"]
    env = Environment()
    f = Formatting(groups=groups,env=env)
    assert f
    assert f.enabled_plugins
    assert not f.enabled_plugins.is_empty()
    for p in f.enabled_plugins:
        assert isinstance(p,Plugin)
        assert p.enabled

# Generated at 2022-06-13 22:13:52.540236
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    import httpie.formatters.json

    class Formatting_for_testing(Formatting):
        def __init__(self, groups: List[str], env=Environment(), **kwargs):
            super().__init__(groups=groups, env=env, **kwargs)
            self.enabled_plugins = [httpie.formatters.json.JSONFormatter]

    url = 'http://httpbin.org/get'

    import requests

    headers = requests.get(url).json()['headers']
    # print(headers)

    format_headers = Formatting_for_testing(groups=['headers']).format_headers(headers)
    # print(format_headers)

    format_body = Formatting_for_testing(groups=['body']).format_body(format_headers, 'application/json')
    # print(format_

# Generated at 2022-06-13 22:13:57.311166
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    # when mime is supported
    test_result1 = Conversion.get_converter('text/html')

    # when mime is not supported
    test_result2 = Conversion.get_converter('text/')

    assert test_result1 is not None and isinstance(test_result1, ConverterPlugin)
    assert test_result2 is None


# Generated at 2022-06-13 22:14:03.452761
# Unit test for constructor of class Formatting
def test_Formatting():
    f1 = Formatting(groups=['colors'], env=Environment(), **{})
    f2 = Formatting(groups=['colors', 'formatters'], env=Environment(), **{})
    assert(len(f1.enabled_plugins) == 1)
    assert(len(f2.enabled_plugins) == 2)


# Generated at 2022-06-13 22:14:10.815944
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env=Environment()
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    f = Formatting(groups=['headers'], env=env)
    headers = "HTTP/1.1 200 OK\r\nContent-type: application/json; charset=utf-8"
    print(f.format_headers(headers))

# Generated at 2022-06-13 22:14:14.212052
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    Formatting('colors').format_headers('HTTP/1.1 200 OK') == '\x1b[32mHTTP/1.1 200 OK'

# Generated at 2022-06-13 22:14:21.805445
# Unit test for constructor of class Formatting
def test_Formatting():
    # Test instantiates a Formatting class with valid inputs
    try:
        Formatting(['colors'], Environment(), color_scheme='paraiso')
        assert True
    except:
        assert False
    # Test instantiates a Formatting class with invalid inputs
    try:
        Formatting(0, ['colors'], Environment(), color_scheme='paraiso')
        assert False
    except:
        assert True


# Generated at 2022-06-13 22:14:24.954526
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting is not None

# Generated at 2022-06-13 22:14:27.080943
# Unit test for constructor of class Formatting
def test_Formatting():
    h = Formatting(['colors'])
    assert len(h.enabled_plugins) == 1
    assert h.enabled_plugins[0]

# Generated at 2022-06-13 22:14:34.295487
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """Test for method format_headers"""
    # Verify if the headers are properly formatted
    f = Formatting(['colors'])
    result = f.format_headers(
        "HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8")
    assert result == "\x1b[0m\x1b[37m\x1b[1mHTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\x1b[0m"

# Generated at 2022-06-13 22:14:43.445514
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from json import dumps
    from httpie.plugins.builtin import Formatter, JSONStreamFormatter, JSONLinesFormatter, PrettyJsonFormatter, PygmentsFormatter,\
        FormattingPlugin

    # Test for character '\n'
    def my_format_headers(headers):
        return '\n'.join('{}: {}'.format(k, v) for k, v in sorted(headers.items()))

    # Test for character '\r'
    def my_format_headers2(headers):
        return '\r'.join('{}: {}'.format(k, v) for k, v in sorted(headers.items()))

    # Test for character '\t'

# Generated at 2022-06-13 22:14:51.085735
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter_example = Conversion.get_converter('text/html')
    if converter_example is None:
        assert False, 'Test failed because converter_example was None.'
    if not isinstance(converter_example, ConverterPlugin):
        assert False, 'Test failed because converter_example was not of type ConverterPlugin.'
    if converter_example.mime != 'text/html':
        assert False, 'Test failed because mime of converter_example was not text/html.'

# Generated at 2022-06-13 22:14:57.852744
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import pytest
    f = Formatting(groups=['colors'])
    assert f.format_headers("200 OK\nX-Header: some value\n\n") == "\x1b[37m200 OK\n\x1b[0mX-Header: \x1b[33msome value\n\x1b[0m\n"
    f = Formatting(groups=[])
    assert f.format_headers("200 OK\nX-Header: some value\n\n") == "200 OK\nX-Header: some value\n\n"


# Generated at 2022-06-13 22:15:09.553734
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie import environment
    from httpie.plugins.builtin import PrettyOptionsPlugin
    format_options = PrettyOptionsPlugin(env=environment.Environment())
    fmt = Formatting(groups=["headers"])
    # Without pretty options enabled
    fmt.enabled_plugins = []
    assert fmt.format_headers("HTTP/1.1 200 OK\r\nServer: nginx\r\nContent-Type: text/html; charset=utf-8\r\n") == \
           "HTTP/1.1 200 OK\r\nServer: nginx\r\nContent-Type: text/html; charset=utf-8\r\n"
    # With pretty options enabled
    fmt.enabled_plugins = [format_options]

# Generated at 2022-06-13 22:15:12.895036
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter_class = Conversion.get_converter("application/json")
    assert converter_class.supports("application/json")
    assert converter_class.supports("application/hal+json")
    assert converter_class.supports("application/schema+json")
    assert not converter_class.supports("application/xml")
    assert not converter_class.supports("text/html+json")
    assert not converter_class.supports("json")

# Generated at 2022-06-13 22:15:18.002763
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    groups = []
    env = Environment()
    content = 'Content-Type: application/json\nAccept: application/xml\n'
    f = Formatting(groups, env)
    actual_content = f.format_headers(content)
    assert content == actual_content


# Generated at 2022-06-13 22:15:21.651192
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("text/html")
    assert converter is not None
    assert converter.mime == 'text/html'
    assert converter.supports("text/html")


# Generated at 2022-06-13 22:15:25.357860
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("text/plain"), ConverterPlugin)

# Generated at 2022-06-13 22:15:33.384867
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = """HTTP/1.1 200 OK
Server: nginx
Date: Tue, 26 May 2020 10:39:40 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Mon, 11 May 2020 10:13:44 GMT
Connection: close
ETag: "5eb92720-264"
Accept-Ranges: bytes

"""
    groups = ["colors", "format"]
    formatting = Formatting(groups)
    new_headers = formatting.format_headers(headers)

# Generated at 2022-06-13 22:15:35.245205
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting([])
    assert Formatting(['application/json'])

# Generated at 2022-06-13 22:15:37.170865
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert None is Conversion.get_converter('text/html')


# Generated at 2022-06-13 22:15:43.045889
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors', 'formatters'];
    env = Environment()
    kwargs = {};
    f = Formatting(groups, env, **kwargs);
    content = '[{"name": "Test"}]'
    mime = "application/json"
    val = f.format_body(content, mime)
    print (val);
    assert val == '[{name: Test}]';

# Generated at 2022-06-13 22:15:55.469360
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import PrettyJsonFormatter
    from httpie.plugins.builtin import JsonLinesFormatter
    from httpie.plugins.builtin import PrettyJsonLinesFormatter
    from httpie.plugins.builtin import CommonLogFormatterPlugin
    from httpie.plugins.builtin import VerboseLogFormatterPlugin
    from httpie.plugins.builtin import CSVFormatterPlugin

    groups = ['format', 'json', 'log', 'csv']
    formatting = Formatting(groups)
    assert len(formatting.enabled_plugins) == 3
    assert isinstance(formatting.enabled_plugins[0], JSONFormatter)
    assert isinstance(formatting.enabled_plugins[1], PrettyJsonFormatter)

# Generated at 2022-06-13 22:16:00.181984
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = "application/json"
    obj = Conversion.get_converter(mime)
    assert obj.supports(mime) == True



# Generated at 2022-06-13 22:16:13.745768
# Unit test for constructor of class Formatting
def test_Formatting():
    # Sample input/output values
    header_string = 'HTTP/1.1 200 OK\r\nServer: nginx/1.10.3 (Ubuntu)\r\nDate: Thur, 24 May 2018 21:40:33 GMT\r\nContent-Type: application/json\r\nContent-Length: 18\r\nConnection: close\r\n\r\n'
    formatted_header_string = 'HTTP/1.1 200 OK\nServer: nginx/1.10.3 (Ubuntu)\nDate: Thur, 24 May 2018 21:40:33 GMT\nContent-Type: application/json\nContent-Length: 18\nConnection: close\n\n'
    json_string = '{"Hello": "World!"}\n'

# Generated at 2022-06-13 22:16:14.585343
# Unit test for constructor of class Formatting
def test_Formatting():
    Formatting(groups = [])

# Generated at 2022-06-13 22:16:29.718323
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert(Conversion.get_converter('json') is not None)
    assert(Conversion.get_converter('html') is not None)
    assert(Conversion.get_converter('xml') is not None)
    assert(Conversion.get_converter('xml/xxx') is None)    


# Generated at 2022-06-13 22:16:35.244946
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion()
    assert c.get_converter('application/json')

# Generated at 2022-06-13 22:16:50.666871
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    with open('tests/data/headers_large.txt', 'r') as headers_file:
        headers_with_many_lines = headers_file.read()
    formatting = Formatting(['colors'])
    formatted_headers = formatting.format_headers(headers_with_many_lines)

    with open('tests/data/headers_large_formatted.txt', 'r') as headers_file:
        expected_formatted_headers = headers_file.read()

    assert formatted_headers[0] == expected_formatted_headers[0]
    assert formatted_headers[1:6] == expected_formatted_headers[1:6]
    assert formatted_headers[-1] == expected_formatted_headers[-1]
    assert formatted_headers.endswith("\n")

# Generated at 2022-06-13 22:17:04.632209
# Unit test for constructor of class Formatting
def test_Formatting():
    import unittest
    from httpie.plugins import FormatterPlugin
    class Mock1_Plugin(FormatterPlugin):
        enabled = True
        def format_headers(self, headers):
            return headers
        def format_body(self, content, mime):
            return content
    class Mock2_Plugin(FormatterPlugin):
        enabled = True
        def format_headers(self, headers):
            return headers
        def format_body(self, content, mime):
            return content
    class Mock3_Plugin(FormatterPlugin):
        enabled = True
        def format_headers(self, headers):
            return headers
        def format_body(self, content, mime):
            return content
    class Mock4_Plugin(FormatterPlugin):
        enabled = True
        def format_headers(self, headers):
            return headers


# Generated at 2022-06-13 22:17:14.051911
# Unit test for constructor of class Formatting
def test_Formatting():
    with pytest.raises(TypeError):
        Formatting('testFormat', 123)

    with pytest.raises(ValueError):
        Formatting('testFormat', [1, 2, 3, 'a', 'b', None])

    with pytest.raises(ValueError):
        Formatting('testFormat', [1, 'Not a String', 2])

    try:
        Formatting('testFormat', ['Valid String'])
    except ValueError:
        pytest.fail("Formatting is giving ValueError when it should not")



# Generated at 2022-06-13 22:17:22.863564
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    class Highlighter(httpie.plugins.FormatterPlugin):
        name = 'highlighter'

        def format_body(self_, body, mime):
            if mime == 'text/plain':
                return body.upper()
            return body

    plugin_manager.register(Highlighter)

    fmt = Formatting(env=httpie.Environment(), print_body=True, json_indent=None)

    assert fmt.format_body("test", 'text/plain') == 'TEST'
    assert fmt.format_body("test", 'application/json') == 'test'

    plugin_manager.unregister(Highlighter)

# Generated at 2022-06-13 22:17:32.887476
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
	assert Conversion.get_converter("image/jpeg") == None
	assert Conversion.get_converter("image/jpeg") != "image/jpeg"
	assert Conversion.get_converter("image/jpeg") != "jpeg"
	assert Conversion.get_converter("image/jpeg") != None
	assert Conversion.get_converter("image/jpeg") == "image/jpeg"
	assert Conversion.get_converter("image/jpeg") != "image"
	assert Conversion.get_converter("image/jpeg") != "jpeg"
	assert Conversion.get_converter("image/jpeg") != "image/jpeg"
	assert Conversion.get_converter("image/jpeg") != "jpeg"

# Generated at 2022-06-13 22:17:40.136634
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatter = Formatting("colors", env=Environment())
    headers = formatter.format_headers("""HTTP/1.1 200 OK\r\nServer: nginx""")
    assert headers == """\033[90mHTTP/1.1 200 OK\033[0m\r\n\033[90mServer: nginx\033[0m"""


# Generated at 2022-06-13 22:17:42.868004
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("text/html")
    assert converter.__class__.__name__ == 'HTMLConverter'

# Generated at 2022-06-13 22:17:45.933550
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter.__class__.__name__ == 'JSONConverter'


# Generated at 2022-06-13 22:17:49.093739
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    res = Conversion.get_converter('text/html')
    assert res.__str__() == 'Converter(text/html)'
    with pytest.raises(Exception):
        res = Conversion.get_converter('text/text')


# Generated at 2022-06-13 22:17:59.190828
# Unit test for constructor of class Formatting
def test_Formatting():
    p = Formatting(['url', 'headers', 'body'], env=Environment(), )
    assert p.enabled_plugins[2].__class__.__name__ == 'BodyURLHighlight'
    p = Formatting(['body', ], env=Environment(),
                   request_as_curl=True)
    assert p.enabled_plugins[0].__class__.__name__ == 'PipeRequestAsCurlCommand'

# Generated at 2022-06-13 22:18:01.418257
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(['curl'])
    assert(True == True)


if __name__ == "__main__":
    test_Formatting()

# Generated at 2022-06-13 22:18:02.915569
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(['colors'])
    assert f


# Generated at 2022-06-13 22:18:14.426320
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatting = Formatting(['color'], env=Environment(), color_scheme='solarized')
    formatted_headers = formatting.format_headers("HTTP/1.1 200 OK\r\nDate: Thu, 18 Jun 2020 14:13:17 GMT\r\nServer: Apache\r\nLast-Modified: Thu, 18 Jun 2020 14:00:03 GMT\r\nETag: \"4e6-5a5e5ccb21b80\"\r\nAccept-Ranges: bytes\r\nContent-Length: 1262\r\nKeep-Alive: timeout=5, max=100\r\nConnection: Keep-Alive\r\nContent-Type: text/html; charset=UTF-8\r\n")

# Generated at 2022-06-13 22:18:15.776800
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert (Conversion.get_converter(
                "application/json") is not None)

# Generated at 2022-06-13 22:18:18.121199
# Unit test for constructor of class Formatting
def test_Formatting():
    with pytest.raises(KeyError):
        Formatting(['foo'], ) # noqa



# Generated at 2022-06-13 22:18:30.618593
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(['colors'])
    h = '''
    HTTP/1.1 200 OK
    Date: Wed, 18 Apr 2018 14:57:04 GMT
    X-Powered-By: Express
    Content-Type: application/json; charset=utf-8
    Content-Length: 7
    Connection: keep-alive
    ETag: W/"7-5ee5d5bdb6acbe0a46cacd95"
    '''

    # Expected results
    e1 = 'HTTP/1.1 200 OK'
    e2 = 'Content-Type: application/json; charset=utf-8'
    e3 = 'Content-Length: 7'
    # Actual results
    a = f.format_headers(h)
    a1 = a.split('\n')[1]


# Generated at 2022-06-13 22:18:37.595405
# Unit test for constructor of class Formatting
def test_Formatting():
    # Unit test for constructor of class Formatting
    available_plugins = plugin_manager.get_formatters_grouped()
    kwargs = {}
    env = Environment()
    groups = ['colors', 'format', 'formatvars']
    f = Formatting(groups, env, **kwargs)
    for group in groups:
        for cls in available_plugins[group]:
            p = cls(env=env, **kwargs)
            if p.enabled:
                assert p in f.enabled_plugins

# Generated at 2022-06-13 22:18:41.832828
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # try to get an invalid mime
    assert not Conversion.get_converter("some-stuff")
    # try to get a valid mime
    assert Conversion.get_converter("image/jpeg")


# Generated at 2022-06-13 22:18:47.758676
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    assert Conversion.get_converter("application/json").__class__.__name__ == "JSONConverter"
    assert Conversion.get_converter("application/xml").__class__.__name__ == "XMLConverter"
    assert Conversion.get_converter("application/x-yaml").__class__.__name__ == "YAMLConverter"


# Generated at 2022-06-13 22:18:53.855925
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("application/json"),ConverterPlugin)


# Generated at 2022-06-13 22:18:58.775199
# Unit test for constructor of class Formatting
def test_Formatting():
	groups = ['json', 'colors']
	env = Environment()
	env.colors = {}
	env.config = {}
	formatting = Formatting(groups, env, max_json_pprint_depth=2)
	assert formatting.enabled_plugins[0].name == 'colors'


# Generated at 2022-06-13 22:19:10.294281
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import pytest
    from httpie.plugins import FormatterPlugin
    
    class MockFormatterPlugin(FormatterPlugin):
        def format_headers(self, headers):
            return headers + '\nfoo: bar'

    class MockFormatterPlugin2(FormatterPlugin):
        def format_headers(self, headers):
            return headers + '\nhello: world'

    input_headers = 'HTTP/1.1 200 OK\nAccept: */*\nContent-Type: application/json'
    output_headers = Formatting(
        ['all'],
        env = Environment(),
        plugins = [MockFormatterPlugin, MockFormatterPlugin2]
    ).format_headers(input_headers)
    
    # Checks that the output headers contains all the headers from input_headers and from plugins.
    # "foo: bar" and "

# Generated at 2022-06-13 22:19:17.490019
# Unit test for constructor of class Formatting
def test_Formatting():
    # Test with no parameters (instead of env)
    try:
        Formatting(groups=[])
    except KeyError:
        print("Constructor for Formatting need a env parameter")

    fmt = Formatting(groups=[], env=Environment())
    # Test with empty groups
    if len(fmt.enabled_plugins) != 0:
        print("Expected to have 0 plugins, but got " + len(fmt.enabled_plugins))
    # Test with one plugin
    fmt = Formatting(groups=["colors"], env=Environment())
    if len(fmt.enabled_plugins) != 1:
        print("Expected to have 1 plugin, but got " + len(fmt.enabled_plugins))
    # Test with two plugins
    fmt = Formatting(groups=["colors", "colors"], env=Environment())

# Generated at 2022-06-13 22:19:27.193752
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Case 1: pass one mime type, which is not supported
    mime = "unknown/unknown"
    assert is_valid_mime(mime) == True
    assert Conversion.get_converter(mime) is None

    # Case 2: pass one of the mime types supported
    mime = "application/json"
    assert is_valid_mime(mime) == True
    assert Conversion.get_converter(mime).mime == "application/json"

    # Case 3: pass one mime type, which is supported but not currently loaded
    # Therefore, no converter is assigned
    mime = "application/xml"
    assert is_valid_mime(mime) == True
    assert Conversion.get_converter(mime) is None


# Generated at 2022-06-13 22:19:41.610814
# Unit test for constructor of class Formatting
def test_Formatting():
    headers = 'App-Name: httpie\nApp-Version: 1.0.2\nContent-Length: 20\nConnection: Keep-Alive\nHeader: Value'
    body = '<html>\n<header>\n<title>Something</title>\n</header>\n<body>\n<h1>haha</h1>\n</body>\n</html>'
    body_mime = 'text/html'
    # Test for format_headers
    f = Formatting(['headers'])
    result1 = f.format_headers(headers)
    if result1 != headers:
        print('Formatting.format_headers() has a bug!')
        exit(1)
    # Test for format_body
    f = Formatting(['body'])
    result2 = f.format_

# Generated at 2022-06-13 22:19:53.299349
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['formatters', ]
    kwargs = {'output_options': {'style': 'monokai', 'colors': True, 'format': 'html', 'all': True, 'follow': False, 'indent': 2, 'traverse': False}, 'output_file': None, 'output_encoding': None, 'output_stream': None, 'output_redirected': False, 'explain': False, 'debug': False}
    env = Environment()
    mime = 'text/xml'
    content = '<?xml version="1.0" encoding="UTF-8"?><note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don\'t forget me this weekend!</body></note>'
    f = Formatting(groups, env, **kwargs)

# Generated at 2022-06-13 22:20:05.966037
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    input_str = b'HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nDate: Mon, 16 Apr 2018 13:02:43 GMT\r\nContent-Type: application/json; charset=utf-8\r\nContent-Length: 41\r\nConnection: keep-alive\r\n\r\n{"status": "ok"}'
    f = Formatting(['colorized'], style='solarized')
    output_str = f.format_headers(input_str)
    assert b'HTTP/1.1' not in output_str
    assert b'Server' in output_str
    assert b'Date' in output_str
    assert b'Content-Type' in output_str
    assert b'Content-Length' in output_str


# Generated at 2022-06-13 22:20:09.946900
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    assert converter is not None
    assert converter.__class__.__name__ == 'JSONConverter'


# Generated at 2022-06-13 22:20:23.178250
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Test with application/json
    converter = Conversion.get_converter("application/json")
    assert str(converter) == "JSONConverter"

    # Test with application/xml
    converter = Conversion.get_converter("application/xml")
    assert str(converter) == "XMLConverter"

    # Test with application/x-www-form-urlencoded
    converter = Conversion.get_converter("application/x-www-form-urlencoded")
    assert str(converter) == "URLEncodedFormConverter"

    # Test with application/xml;charset=UTF-8
    converter = Conversion.get_converter("application/xml;charset=UTF-8")
    assert str(converter) == "XMLConverter"

   

# Generated at 2022-06-13 22:20:41.029402
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    input = {'a': '1', 'b': '2', 'c': '3'}
    output = Formatting(['json']).format_headers(input)
    assert output == {'a': '1', 'b': '2', 'c': '3'}

    input = {'a': '1', 'b': '2', 'c': '3'}
    output = Formatting(['json', 'colors']).format_headers(input)
    assert output == {'a': '1', 'b': '2', 'c': '3'}

    input = {'a': '1', 'b': '2', 'c': '3'}
    output = Formatting(['colors']).format_headers(input)

# Generated at 2022-06-13 22:20:45.106104
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f1 = Formatting(groups=['headers'])
    print(f1.format_headers('Date: Mon, 08 Oct 2018 05:57:34 GMT\nContent-Type: text/html; charset=utf-8'))



# Generated at 2022-06-13 22:20:48.160507
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/html') == plugin_manager.get_converters()[2]
    assert Conversion.get_converter('text/markdown') == None

# Generated at 2022-06-13 22:20:50.813028
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = "content-length: 2\n"
    headers_expected = "Content-Length: 2\r\n"
    env = Environment(stdout=io.StringIO(), stderr=io.StringIO())
    f = Formatting(["headers"], env=env)
    headers_actual = f.format_headers(headers)
    assert headers_actual == headers_expected

# Generated at 2022-06-13 22:20:53.589263
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['colors'])
    assert f.enabled_plugins != []
    for p in f.enabled_plugins:
        assert p.enabled


# Generated at 2022-06-13 22:21:02.380223
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # test for empty input string
    f = Formatting(['colors'])
    assert f.format_body("", "application/json") == ""
    # test for JSON response
    f = Formatting(['colors'])
    assert f.format_body('{"a": ["b", "c"]}', "application/json") == '{\n    "a": [\n        "b", \n        "c"\n    ]\n}\n'
    # test for XML response
    f = Formatting(['colors'])
    assert f.format_body('<a><b>b</b><b>c</b></a>', "application/xml") == '<a>\n  <b>b</b>\n  <b>c</b>\n</a>\n'
    # test for

# Generated at 2022-06-13 22:21:06.152035
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """Test method get_converter of class Conversion,
    with an invalid MIME as input"""
    converter = Conversion.get_converter("nothing")
    assert converter is None

# Generated at 2022-06-13 22:21:10.855314
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('application/json')
    assert c

    c = Conversion.get_converter('NOT-A-MIME-TYPE')
    assert c is None

    c = Conversion.get_converter('NOT_APPLICATION/JSON-TYPE')
    assert c is None

# Generated at 2022-06-13 22:21:22.289498
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # json converter
    s = Conversion.get_converter('application/json')
    assert isinstance(s, ConverterPlugin)
    assert(s.mime == 'application/json')
    assert(s.converts('application/json'))
    assert(not s.converts('application/xml'))

    # xml converter
    s = Conversion.get_converter('application/xml')
    assert isinstance(s, ConverterPlugin)
    assert(s.mime == 'application/xml')
    assert(s.converts('application/xml'))
    assert(not s.converts('application/json'))

    # html converter
    s = Conversion.get_converter('text/html')
    assert isinstance(s, ConverterPlugin)
    assert(s.mime == 'text/html')


# Generated at 2022-06-13 22:21:29.870713
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter != None
    converter = Conversion.get_converter("application/xml")
    assert converter != None
    converter = Conversion.get_converter("application/x1")
    assert converter == None
    converter = Conversion.get_converter("text/plain")
    assert converter == None
    converter = Conversion.get_converter("application/a+b")
    assert converter == None


# Generated at 2022-06-13 22:21:49.237964
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = [
        "json",
        "colors",
        "format"
    ]
    env = Environment()

    formatting = Formatting(
        groups=groups,
        env=env,
        table_fields=None
    )

    assert formatting.enabled_plugins != None

# Generated at 2022-06-13 22:21:50.954529
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('json')
    assert not Conversion.get_converter('text/plain')



# Generated at 2022-06-13 22:21:54.049986
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    for group in ['colors']:
        for cls in available_plugins[group]:
            p = cls(env=Environment())
            if p.enabled:
                print(p)

if __name__ == '__main__':
    test_Formatting()

# Generated at 2022-06-13 22:21:58.557940
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime="text/plain"
    expected_converter=None
    obtained_converter=Conversion.get_converter(mime)

    assert obtained_converter == expected_converter


# Generated at 2022-06-13 22:22:02.345971
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json')
    assert not Conversion.get_converter('application/json1')

# Generated at 2022-06-13 22:22:14.031342
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """Unit test for method format_body of class Formatting"""

    # Create the object to test
    formatter = Formatting(["colors"])

    # Test the function
    assert formatter.format_body("") == ""
    assert formatter.format_body("test") == "test"
    assert formatter.format_body("test {}", "text/plain") == "test {}"
    assert formatter.format_body("{} test", "text/plain") == "{} test"
    assert formatter.format_body("{test}", "text/plain") == "{test}"
    assert formatter.format_body("test {body}", "text/plain") == "test {body}"
    assert formatter.format_body("test", "application/json") == "test"