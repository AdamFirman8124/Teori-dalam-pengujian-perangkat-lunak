

# Generated at 2022-06-13 22:12:29.210122
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    json_str = '''{
      "name": "httpie",
      "description": "HTTPie is a command line HTTP client, a user-friendly cURL replacement.\n",
      "home_page": "https://httpie.org/",
      "keywords": [
        "curl",
        "cli",
        "http",
        "wget"
      ],
      "license": "BSD"
    }
    '''
    groups = ['highlight']
    env=Environment()
    formatting_class = Formatting(groups, env)
    colorized_json_str = formatting_class.format_body(json_str, "application/json")
    print(colorized_json_str)

if __name__ == "__main__":
    test_Formatting_format_body()

# Generated at 2022-06-13 22:12:32.905517
# Unit test for constructor of class Formatting
def test_Formatting():
    print("=====test for constructor of class Formatting=====")
    groups = ["colors"]
    env = Environment()
    ft = Formatting(groups, env)
    print(ft.enabled_plugins)
    print(ft.format_headers("Content-Length:10"))

# Generated at 2022-06-13 22:12:46.251814
# Unit test for constructor of class Formatting
def test_Formatting():
    # Create environment
    env = Environment()
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    env.stdin = sys.stdin
    env.config.config_dir = Path('/tmp/.httpie')
    env.config.default_options = [
        '--ignore-stdin',
        '--print=B',
        '--verify=no',
        '--all'
    ]
    env.config.config_path = Path('/tmp/.httpie/config.json')


# Generated at 2022-06-13 22:12:52.536581
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'text/plain'
    assert isinstance(Conversion.get_converter(mime), ConverterPlugin)
    mime = 'text/plain; charset=utf-8'
    assert isinstance(Conversion.get_converter(mime), ConverterPlugin)
    mime = 'application/json'
    assert isinstance(Conversion.get_converter(mime), ConverterPlugin)
    mime = 'bogus'
    assert not isinstance(Conversion.get_converter(mime), ConverterPlugin)
    mime = ''
    assert not isinstance(Conversion.get_converter(mime), ConverterPlugin)
    mime = None
    assert not isinstance(Conversion.get_converter(mime), ConverterPlugin)

# Generated at 2022-06-13 22:13:04.924796
# Unit test for constructor of class Formatting
def test_Formatting():
    import json
    formatter = Formatting(['colors'])
    assert formatter.enabled_plugins[0].__class__.__name__ == 'Colors'
    data = {'status': 200,
            'headers': {'X-Foo': 'foo', 'X-Bar': 'bar', 'X-Baz': 'baz'},
            'content': json.dumps({'foo': 'bar'}, indent=4)
            }
    formatter.format_headers(**data)
    formatter.format_body(**data)
    formatter = Formatting(['colors'], True, sort_headers=True)
    formatter.format_headers(**data)
    formatter.format_body(**data)
    formatter = Formatting(['colors'], True, sort_headers=False)


# Generated at 2022-06-13 22:13:11.479524
# Unit test for constructor of class Formatting
def test_Formatting():
    assert len(Formatting.__init__.__annotations__) == 4
    assert Formatting.__init__.__annotations__['groups'] == List[str]
    assert Formatting.__init__.__annotations__['env'] == Environment
    assert Formatting.__init__.__annotations__['return'] == None


# Generated at 2022-06-13 22:13:13.652361
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting(mime='application/json', groups=['colors'], env=Environment())

# Generated at 2022-06-13 22:13:20.759408
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(['colors', 'format'], write_stream=sys.stdout)
    # Check that plugin with params are enabled
    assert(plugin_manager.get_colors_grouped()[0](write_stream=sys.stdout).enabled)
    assert(plugin_manager.get_formatters_grouped()[0](write_stream=sys.stdout).enabled)


# Generated at 2022-06-13 22:13:30.559813
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    environment = Environment(colors=256, stdin_isatty=True,
                              stdout_isatty=True, is_windows=False,
                              read_cli_bool=(lambda: True),
                              configuration_dir=None,
                              styles=OrderedDict(), default_options={})
    environment.configure_logging()

    assert Formatting(['format'], env=environment, max_cols=None).format_body("<p>abc</p>", 'text/html') == '<p>abc</p>\n'
    assert Formatting(['format'], env=environment, max_cols=None).format_body("{\n  \"a\": 1\n}", 'application/json') == '{\n  "a": 1\n}\n'

# Generated at 2022-06-13 22:13:32.883514
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)


# Generated at 2022-06-13 22:13:43.713238
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:13:46.741115
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(["jjson","json"])
    s = '{"text": "hello world"}'
    assert f.format_body(s, "application/json") == """{
    "text": "hello world"
}"""


# Generated at 2022-06-13 22:13:52.991785
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    formatting = Formatting(groups=["colors"])

    actual_result = formatting.format_body('{"k1": "v1"}', 'application/json')
    assert actual_result == '{\n    "k1": "v1"\n}\n'

    actual_result = formatting.format_body('{"k1": "v1"}', 'none')
    assert actual_result == '{"k1": "v1"}'


# Generated at 2022-06-13 22:13:55.645990
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting([])
    Formatting(['colors', 'colors'])
    Formatting(['colors', 'colors', 'colors'])

# Generated at 2022-06-13 22:14:08.041465
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """
    Test method format_headers.
    """
    before = """
    HTTP/1.1 200 OK
    Accept-Ranges: bytes
    Cache-Control: public, max-age=120
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Length: 543
    Content-Type: text/html; charset=utf-8
    Date: Mon, 20 Jun 2016 12:26:40 GMT
    ETag: "1466393017"
    Expires: Mon, 20 Jun 2016 12:28:40 GMT
    Last-Modified: Mon, 20 Jun 2016 12:26:37 GMT
    Server: nginx
    X-Content-Type-Options: nosniff
    X-Frame-Options: DENY
    X-XSS-Protection: 1; mode=block
    """

   

# Generated at 2022-06-13 22:14:16.752865
# Unit test for constructor of class Formatting
def test_Formatting():
    # Create a testing environment
    test_env = Environment()
    test_env.output_options.format = 'colors'
    test_env.output_options.colors = 'Windows'
    # Create a Formatting object
    test_formatting = Formatting(['colors'], test_env)
    # Check the length of enabled processors
    assert len(test_formatting.enabled_plugins) == 2


# Generated at 2022-06-13 22:14:22.404867
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['colors'], env=Environment())
    assert(len(f.enabled_plugins) == 1)
    assert(f.enabled_plugins[0].__class__.__name__ == 'ColorsFormatter')


# Generated at 2022-06-13 22:14:31.038003
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.config import Config
    from httpie.context import Environment
    f = Formatting(groups=['colors'], env=Environment(config=Config()), request_headers=True)
    assert 0 == len(f.enabled_plugins)
    f = Formatting(groups=['colors'], env=Environment(config=Config(colors=True)), request_headers=True)
    assert 1 == len(f.enabled_plugins)



# Generated at 2022-06-13 22:14:39.560367
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    # Test1: return converter of a given mime
    mime = "application/json"
    converter = Conversion.get_converter(mime)

    if not isinstance(converter, ConverterPlugin):
        raise AssertionError("ConverterPlugin is not found")

    # Test2: return converter of a given mime
    mime = "application/xml"
    converter = Conversion.get_converter(mime)

    if converter is None:
        raise AssertionError("ConverterPlugin is not found")


# Generated at 2022-06-13 22:14:46.343683
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    x = Formatting(groups = ["colors"])
    assert(x.format_headers("Test case") == HTTPIE_OUTPUT_OF_FORMATTING)

HTTPIE_OUTPUT_OF_FORMATTING = '\x1b[0m\x1b[34mTest case\x1b[0m'

# Test for method format_body of class Formatting

# Generated at 2022-06-13 22:14:49.714534
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter_class = Conversion.get_converter('application/json')
    assert str(converter_class) == "Converter<application/json>"

# Generated at 2022-06-13 22:14:51.310543
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)

# Generated at 2022-06-13 22:15:00.189884
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_headers = """HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Fri, 07 Feb 2020 18:50:26 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
X-Content-Type-Options: nosniff
Alternate-Protected-Resource-Location: https://www.google.com/
X-XSS-Protection: 1; mode=block
Referrer-Policy: no-referrer
Content-Encoding: gzip

"""
    groups = ['browsable']
    f = Formatting(groups)

# Generated at 2022-06-13 22:15:07.055696
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.builtin import FormatterPlugin
    class Plugin(FormatterPlugin):
      def format_headers(self, headers):
        return headers.replace(': ',':')
    plugin_manager.register(Plugin)

    f = Formatting([])
    assert f.format_headers('Connection: test') == 'Connection:test'

    plugin_manager._instantiated_plugins = {}
    plugin_manager.deregister(Plugin)

# Generated at 2022-06-13 22:15:10.992275
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(["html"], env=Environment())
    content = "<p>this is a test</p>"
    mime = "text/html"
    assert f.format_body(content, mime) == "<p>this is a test</p>"

# Generated at 2022-06-13 22:15:18.564925
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.native import PythonHTTPClientsEmulatorPlugin
    env = Environment(plugins=[PythonHTTPClientsEmulatorPlugin()])
    f = Formatting(['browsable'], env)
    assert f.format_headers('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n') == 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n'

# Generated at 2022-06-13 22:15:28.732053
# Unit test for constructor of class Formatting
def test_Formatting():
    environment = Environment()
    formatter = Formatting(groups=["transform"], env=environment,
                           options={'suppress': False, 'pretty': True})

# Generated at 2022-06-13 22:15:33.071174
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fmt = Formatting(['colors'])
    test_string = 'a: b\nc: d'
    assert test_string == fmt.format_headers(test_string)


# Generated at 2022-06-13 22:15:41.946565
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # I
    groups = ['colors']
    env = Environment()
    expected = b'Content-Type: text/html; charset=utf-8'
    content = b'Content-Type: text/html; charset=utf-8'
    mime = 'Content-Type: text/html; charset=utf-8'
    
    # M
    formatter = Formatting(groups, env)
    result = formatter.format_headers(content)
    
    # O
    assert expected == result.encode()
    

# Generated at 2022-06-13 22:15:45.068415
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    print(converter)


# Generated at 2022-06-13 22:15:58.086715
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # test case 1
    # input
    expected_result = "HTTP/1.1 200 OK\n" \
                      "Access-Control-Allow-Origin: *\n" \
                      "Cache-Control: no-cache\n" \
                      "Content-Length: 67\n" \
                      "Content-Type: application/json\n" \
                      "Date: Sun, 25 Apr 2021 18:43:09 GMT\n" \
                      "X-Ratelimit-Limit: 120\n" \
                      "X-Ratelimit-Remaining: 120"


# Generated at 2022-06-13 22:16:01.340154
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('application/json')
    assert str(c) == 'httpie.plugins.builtin.converters.JSONConverter(mime=application/json)'

# Generated at 2022-06-13 22:16:14.427381
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins.builtin import JSONConverter, HTMLConverter
    from httpie.plugins.builtin import ImageConverter, BinaryConverter
    from httpie.plugins.builtin import XMLConverter, URLEncodedConverter

    assert type(Conversion.get_converter(JSONConverter.supported_mime)) == JSONConverter
    assert type(Conversion.get_converter(HTMLConverter.supported_mime)) == HTMLConverter
    assert type(Conversion.get_converter(ImageConverter.supported_mime)) == ImageConverter
    assert type(Conversion.get_converter(BinaryConverter.supported_mime)) == BinaryConverter

# Generated at 2022-06-13 22:16:28.600921
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    formatting = Formatting(
        ['colors', 'colors256'],
        env=env,
        kind='auto'
    )
    assert env.formatter == formatting

# Generated at 2022-06-13 22:16:40.341248
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Case when no conversion plugins are available
    formatting = Formatting([""])
    formatted_headers = formatting.format_body("", "test_format/test_header")
    assert_that(formatted_headers).is_equal_to("")

    # Case when no conversion plugins support the given mime type
    formatting = Formatting([""])
    formatted_headers = formatting.format_body("", "test_format/test_body")
    assert_that(formatted_headers).is_equal_to("")

    # Case when no valid mime type is passed
    formatting = Formatting([""])
    formatted_headers = formatting.format_body("", None)
    assert_that(formatted_headers).is_equal_to("")

    # Case when a conversion plugin is available and supports the mime type
    formatting = Format

# Generated at 2022-06-13 22:16:45.836325
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fs = Formatting(groups=['colors'])
    content = fs.format_headers('GET / HTTP/1.1')
    assert content == '\x1b[90mGET\x1b[39m \x1b[36m/\x1b[39m \x1b[90mHTTP/1.1\x1b[39m\n'


# Generated at 2022-06-13 22:16:53.854670
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json').mime == 'application/json'
    assert Conversion.get_converter('image/jpeg').mime == 'image/jpeg'
    assert isinstance(Conversion.get_converter('image/jpeg'), ConverterPlugin)
    assert Conversion.get_converter('image/jpeg+json') == None
    assert Conversion.get_converter('') == None
    assert Conversion.get_converter('jpeg/jpg') == None


# Generated at 2022-06-13 22:17:07.161963
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    content = "abc"
    mime = "a/b"
    available_groups = plugin_manager.get_formatters_grouped()
    env = Environment()
    f = Formatting(["colors", "format"], env=env)
    assert f.format_body(content, mime) == "abc"
    f = Formatting(["colors", "format"], env=env)
    for group in available_groups:
        for cls in available_groups[group]:
            p = cls(env=env)
            if p.enabled:
                p.format_body = lambda content, mime: content + "d"
                p.format_headers = lambda headers: headers + "d"
                return
    assert f.format_body(content, mime) == "abcd"

# Generated at 2022-06-13 22:17:07.886767
# Unit test for constructor of class Formatting
def test_Formatting():
    a = Formatting([])

# Generated at 2022-06-13 22:17:17.199417
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import copy
    f = Formatting(groups=['colors'], env=Environment(), colors={'headers': 'on'})
    input_headers = copy.deepcopy(headers_with_color_on)
    assert f.format_headers(input_headers) == expected_headers_result
    assert input_headers == headers_with_color_on
    assert f.format_headers(headers_without_color) == expected_headers_result
    assert f.format_headers(headers_with_color_off) == expected_headers_result
    f = Formatting(groups=['colors'], env=Environment(), colors={'headers': 'off'})
    assert f.format_headers(headers_with_color_off) == headers_with_color_off
    assert f.format_headers(headers_without_color) == headers_without_color

# Generated at 2022-06-13 22:17:30.468380
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    input = "HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nServer: gunicorn/19.9.0\r\nDate: Tue, 27 Nov 2018 19:53:05 GMT\r\nContent-Type: application/json; charset=utf-8\r\nContent-Length: 2\r\nAccess-Control-Allow-Origin: *\r\nAccess-Control-Allow-Credentials: true\r\nVia: 1.1 vegur\r\n\r\n{}"

# Generated at 2022-06-13 22:17:31.570006
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(["HTTPie"])
    assert f.enabled_plugins == []

# Generated at 2022-06-13 22:17:35.878256
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("application/json"), ConverterPlugin)
    assert not isinstance(Conversion.get_converter("application/jons"), ConverterPlugin)


# Generated at 2022-06-13 22:17:37.853844
# Unit test for constructor of class Formatting
def test_Formatting():
    res = Formatting(["colors"])
    assert res.enabled_plugins == []

# Generated at 2022-06-13 22:17:46.163865
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    Formatting(["colors", "format", "format_json", "format_html"], Environment())

    print(available_plugins["colors"])
    print(available_plugins["format"])
    print(available_plugins["format_json"])
    print(available_plugins["format_html"])
    print(dir(available_plugins["colors"][0]))


if __name__ == '__main__':
    test_Formatting()

# Generated at 2022-06-13 22:17:48.446590
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not Conversion.get_converter('text/plain')
    assert Conversion.get_converter('application/json').mime == 'application/json'


# Generated at 2022-06-13 22:17:59.900691
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Test with no formatter
    f = Formatting([])
    assert f.format_headers("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n") == "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

    # Test with only pretty formatter
    f = Formatting(['pretty'])
    assert f.format_headers("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n") == "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"


# Generated at 2022-06-13 22:18:04.622414
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    groups = ['colors']
    env = Environment()
    enabled_plugins = []
    for group in groups:
        for cls in available_plugins[group]:
            p = cls(env=env)
            if p.enabled:
                enabled_plugins.append(p)


# Generated at 2022-06-13 22:18:08.579047
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins.converter.js import JSONConverter
    assert Conversion.get_converter('application/json').__class__ == JSONConverter


# Generated at 2022-06-13 22:18:12.848889
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["colors", "colors_16"]
    env = Environment()
    kwargs = {}
    fmt = Formatting(groups, env, **kwargs)
    assert fmt.enabled_plugins != []

# Generated at 2022-06-13 22:18:16.663303
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    assert converter.mime == mime

# Generated at 2022-06-13 22:18:19.214479
# Unit test for constructor of class Formatting
def test_Formatting():
    # Enable only plugins for pretty, syntax.
    F = Formatting(['pretty'])
    F_ = Formatting(['pretty', 'syntax'])



# Generated at 2022-06-13 22:18:31.380249
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    conversion = Conversion()
    assert Conversion.get_converter('image/png') is not None  # Coverage 100%
    assert Conversion.get_converter('text/plain') is not None  # Coverage 100%
    assert Conversion.get_converter('text/html') is not None  # Coverage 100%
    assert Conversion.get_converter('text/xml') is not None  # Coverage 100%
    assert Conversion.get_converter('application/javascript') is not None  # Coverage 100%
    assert Conversion.get_converter('application/json') is not None  # Coverage 100%
    assert Conversion.get_converter('application/xml') is not None  # Coverage 100%
    assert Conversion.get_converter('text/xml') is not None  # Coverage 100%
    assert Conversion.get_converter

# Generated at 2022-06-13 22:18:33.338913
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion()
    assert converter.get_converter('application/json')

# Generated at 2022-06-13 22:18:43.079714
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    content_str = '''<!DOCTYPE html>
    <html>
    <head>
        <title>HTTPie</title>
    </head>
    <body>
        <h1>HTTPie</h1>
    </body>
    </html>'''
    mime_str = 'text/html'
    formatter = Formatting(['format'])
    content = formatter.format_body(content_str, mime_str)
    assert '\n    ' not in content
    assert content == content_str.replace('\n    ', '')

# Generated at 2022-06-13 22:18:46.462199
# Unit test for constructor of class Formatting
def test_Formatting():
    result = Formatting(['colors', 'formatters'],
                        scheme='http', auth=('username', 'password'),
                        verify=True, verbose=True)
    assert result
    assert result.enabled_plugins

# Generated at 2022-06-13 22:18:48.700830
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    f = Formatting(groups=["JSON", "HTML"], env=env)



# Generated at 2022-06-13 22:18:50.014340
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/javascript")
    

# Generated at 2022-06-13 22:19:02.619141
# Unit test for constructor of class Formatting
def test_Formatting():
    """Test if the constructor of class Formatting works as expected."""

    # create environment
    env = Environment(colors=256, stdin_isatty=False)  # does not matter

    # case 1: if no parameters are passed to formatting
    fmt = Formatting([], env)
    assert fmt.enabled_plugins == []

    # create a new environment with some parameters set
    env2 = Environment(colors=256, stdin_isatty=True)

    # case 2: no parameters are passed to the formatting
    fmt2 = Formatting([], env2)

    # get the Formatting class
    _fmt_c = plugin_manager.get_formatters_grouped()['Formatting']
    _fmt_c = _fmt_c[0]  # take the first one
    _fmt_obj = _f

# Generated at 2022-06-13 22:19:07.423926
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    # test mime type supported
    mime = 'application/json'
    assert Conversion.get_converter(mime) is not None

    # test mime type not supported
    mime = 'audio/mp3'
    assert Conversion.get_converter(mime) is None



# Generated at 2022-06-13 22:19:11.955872
# Unit test for constructor of class Formatting
def test_Formatting():
    """
    Unit test for constructor of class Formatting
    """
    groups = ['colors']
    assert Formatting(groups)

# Generated at 2022-06-13 22:19:21.746809
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['syntax', 'colors']

    encoding = 'utf8'
    env = Environment(stdin_isatty=False, stdout_isatty=False)
    formatting = Formatting(groups, env, encoding=encoding)

    raw = b'{"foo": "bar"}'
    content = raw.decode(encoding=encoding)
    assert content == '{"foo": "bar"}'

    formatted = formatting.format_body(content=content, mime="application/json")
    assert formatting.format_body(content='', mime="application/json") == ""

    assert formatted == '{\n    "foo": "bar"\n}'


if __name__ == '__main__':
    test_Formatting_format_body()

# Generated at 2022-06-13 22:19:35.648499
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = "HTTP/1.1 200 OK\r\n" \
              "Access-Control-Allow-Credentials: true\r\n" \
              "Access-Control-Allow-Origin: http://localhost:8080\r\n" \
              "Content-Type: application/json;charset=UTF-8\r\n" \
              "Date: Wed, 10 Jul 2019 10:14:39 +0000\r\n" \
              "Server: HttpComponents/1.1\r\n" \
              "Transfer-Encoding: chunked\r\n" \
              "\r\n"
    print(Formatting(['format', 'colors']).format_headers(headers))

# Generated at 2022-06-13 22:19:40.737891
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']
    env = Environment()
    test_obj = Formatting(groups, env = env, headers = None, style = True)
    assert test_obj.enabled_plugins[0].__class__.__name__ == 'ColorsFormatter'


# Generated at 2022-06-13 22:19:46.365483
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    headers = {
        'Content-Type': 'application/xml',
    }
    content = '<responses><response><status>200</status><title>OK</title></response></responses>'

    # Test
    formatter = Formatting([])
    new_content = formatter.format_body(content, headers['Content-Type'])

    # Assert
    assert content == new_content

# Generated at 2022-06-13 22:19:51.691276
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    input_formatting_instance = Formatting(["default"])
    actual_result = input_formatting_instance.format_headers('Content-Type: application/x-www-form-urlencoded')
    expected_result = 'Content-Type: application/x-www-form-urlencoded'
    assert expected_result == actual_result



# Generated at 2022-06-13 22:20:00.424847
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["colors", "colors"]
    env = Environment()
    fmt = Formatting(groups, env)
    plugins = fmt.enabled_plugins

    assert len(plugins) == 2

    assert plugins[0].__class__.__name__ == "ColorsFormatter"
    assert plugins[0].enabled == True

    assert plugins[1].__class__.__name__ == "ColorsFormatter"
    assert plugins[1].enabled == True



# Generated at 2022-06-13 22:20:05.656704
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    test_cases = [
        ('text/html', 'HTML'),
        ('text/tab-separated-values', 'CSV'),
        ('text/plain', 'None'),
    ]
    for mime, expected_result in test_cases:
        converter = Conversion.get_converter(mime)
        result = None
        if converter:
            result = converter.__class__.__name__

        print(mime, result, expected_result)
        assert result == expected_result

# Generated at 2022-06-13 22:20:10.409607
# Unit test for constructor of class Formatting
def test_Formatting():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pretty', action='append', default=[])
    args = parser.parse_args(['--pretty', 'all'])
    fmt = Formatting(groups=args.pretty)

    assert fmt is not None

# Generated at 2022-06-13 22:20:14.124552
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print(Conversion.get_converter('application/json'))
    print(Conversion.get_converter('text/html'))



# Generated at 2022-06-13 22:20:29.072791
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins.builtin import JSONFormatter, HTMLFormatter, XMLFormatter
    plugin_manager.get_formatters_grouped()['json'] = (JSONFormatter,)
    plugin_manager.get_formatters_grouped()['html'] = (HTMLFormatter,)
    plugin_manager.get_formatters_grouped()['xml'] = (XMLFormatter,)
    f = Formatting(['json', 'html'], prettify=True)
    assert f.format_body('[{},{"a":1}]', 'application/json') == '''[
    {},
    {
        "a": 1
    }
]'''

# Generated at 2022-06-13 22:20:31.243976
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('text/html')
    assert converter.mime == 'text/html'

# Generated at 2022-06-13 22:20:36.006306
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()
    p = available_plugins["styles"][0]
    print(p)
    content = p.format_body('{"test": "1","test": "2"}', "application/json")
    print(content)


# Generated at 2022-06-13 22:20:42.626970
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    frm = Formatting(['colors', 'formatting'])
    headers = frm.format_headers("HTTP/1.1 200 OK\r\nDate: Sat, 12 Jan 2019 23:02:17 GMT\r\nServer: Apache\r\n")
    assert headers == "\u001b[1mHTTP/1.1 200 OK\u001b[22m\r\n\u001b[1mDate\u001b[22m: Sat, 12 Jan 2019 23:02:17 GMT\r\n\u001b[1mServer\u001b[22m: Apache\r\n"


# Generated at 2022-06-13 22:20:47.543729
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert(Conversion.get_converter(mime="application/json") is not None)
    assert(Conversion.get_converter(mime="application/jso") is None)
    assert(Conversion.get_converter(mime="application") is None)


# Generated at 2022-06-13 22:20:49.125268
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/html')



# Generated at 2022-06-13 22:20:53.799098
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']
    env = Environment(colors=True)
    f = Formatting(groups, env)
    assert len(f.enabled_plugins) == 1
    assert f.enabled_plugins[0].__class__.__name__ == 'Colors'

# Generated at 2022-06-13 22:20:59.700547
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(['highlight', 'format', 'colors'],
                   highlight_lines=[1, 2, 3],
                   sort_headers=False,
                   body_style='httpie',
                   color_scheme='<color_scheme>',
                   stream=None,
                   pretty=None)

    assert f.enabled_plugins == '[]'
    assert f.enabled_plugins == []

# Generated at 2022-06-13 22:21:05.245491
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Given
    env = Environment()
    # It looks like the "available_plugins" list is always empty
    # Then the enabled_plugins list is also always empty
    # When
    formatting = Formatting(['headers'], env=env)
    # Then
    assert len(formatting.enabled_plugins) == 0

# Generated at 2022-06-13 22:21:13.565227
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Define data for testing
    message = "Hello world!"
    expected = "HELLO WORLD!"
    # Initialize class Formatting
    formatting = Formatting([])
    # Invoke method format_body of class Formatting
    actual = formatting.format_body(message, "text/plain")
    assert actual == expected,\
        "The actual result is " + actual + " but the expected result is " + expected



# Generated at 2022-06-13 22:21:19.202353
# Unit test for constructor of class Formatting
def test_Formatting():    
    format_obj = Formatting(groups=['web-preview'])
    assert isinstance(format_obj, Formatting)


# Generated at 2022-06-13 22:21:28.993383
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_string = 'aaa\nbbb\nccc\n'
    format_test = Formatting(groups=['colors'])
    assert format_test.format_headers(test_string)==('\x1b[38;5;241maaa\x1b[39m\n'
                                                     '\x1b[38;5;241mbbb\x1b[39m\n'
                                                     '\x1b[38;5;241mccc\x1b[39m\n')

# Generated at 2022-06-13 22:21:39.318356
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """
    Makes a simple test of the method format_headers of the class Formatting.
    The test will check whether the output of the method is as expected.
    :return:
    """
    print("\nFunction test_Formatting_format_headers")
    print("\n")
    print("Testing the method format_headers of the class Formatting")
    print("\n")
    print("Remarks:")
    print("\t1. This test is a basic test that makes sure that the output\n"
          "\tof the method is as expected.")
    print("\n")

# Generated at 2022-06-13 22:21:47.491083
# Unit test for constructor of class Formatting
def test_Formatting():
    # arrange
    env = Environment()
    env.stdout = open('Test.txt','w')
    available_plugins = plugin_manager.get_formatters_grouped()
    groups = ['all']
    expected = "Available formatters:\ncolors, colors_extended, format,\n"+\
                "json, html, prettyjson, prettyxml, table,\npygments,\n\n"
    # act
    f = Formatting(groups, env)
    # assert
    assert expected == env.stdout.read()

# Generated at 2022-06-13 22:21:53.141095
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    '''
    Function to test get_converter method of class Conversion
    :return: Nothing
    '''
    assert type(Conversion.get_converter("application/json")) == type(Conversion.get_converter("text/html"))


# Generated at 2022-06-13 22:21:55.975544
# Unit test for constructor of class Formatting
def test_Formatting():
    instances = Formatting('colors,format')
    assert instances.enabled_plugins[1].__class__.__name__ == 'ColorsFormatter'
    assert instances.enabled_plugins[0].__class__.__name__ == 'FormatFormatter'


# Generated at 2022-06-13 22:22:08.583242
# Unit test for constructor of class Formatting
def test_Formatting():
    class Mock:
        def __init__(self, env=Environment(), **kwargs):
            self.env = env
            self.kwargs = kwargs
            self.enabled = True
            self.__class__.called = True
        @staticmethod
        def format_headers(headers: str):
            return ''
        @staticmethod
        def format_body(content, mime):
            return ''
        def __repr__(self):
            return f'{self.__class__.__name__}({self.env}, {self.kwargs})'
    plugin_manager.get_formatters_grouped = lambda: {'group': [Mock,]}
    env = Environment()
    f = Formatting(['group'], env)
    assert Mock.called

# Generated at 2022-06-13 22:22:10.772696
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    print(available_plugins)

#test_Formatting()

# Generated at 2022-06-13 22:22:13.384788
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("text/html"), ConverterPlugin)

