

# Generated at 2022-06-13 22:12:22.618926
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(['colors'])
    body_bytes = b'{"test": 1}'
    formatted = f.format_body(body_bytes, 'application/json')
    assert formatted == body_bytes

# Generated at 2022-06-13 22:12:31.297264
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    try:
        environment = Environment(colors=256, stdin=sys.stdin, stdout=sys.stdout,
                                  is_windows=(os.name == 'nt'), config_dir=os.path.join(os.path.dirname(__file__), ".."))
        formatting = Formatting(["json"], env=environment, pretty=True)
        jsonString = '{"algorithm":[["algorithm","PATH"],["algorithm","TEXT"]]}'
        formattedString = formatting.format_body(jsonString, "application/json")
        print(formattedString)
    except AttributeError as e:
        pass

# Generated at 2022-06-13 22:12:37.328148
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins.builtin import FormatterPlugin
    import json

    class MyFormatter(FormatterPlugin):
        def format_body(self, body, mime):
            return json.loads(body)["name"]

    fmt = Formatting(["MyFormatter"])
    fmt.enabled_plugins = [MyFormatter()]

    body = """
    {
        "name": "Richard"
    }
    """

    body = fmt.format_body(body, "None")
    assert body == "Richard"

# Generated at 2022-06-13 22:12:42.988788
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    g = Formatting(["pretty"])
    headers = "\n".join(["Content-Length: 10", "Content-Type: text/plain"])
    assert (g.format_headers(headers) ==
            "\n".join(["Content-Length: 10", "Content-Type: text/plain"]))



# Generated at 2022-06-13 22:12:51.437699
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """
    Test method format_body of class Formatting
    :return:
    """
    environment = Environment()
    available_plugins = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in ['colors']:
        for cls in available_plugins[group]:
            p = cls(env=environment, **{})
            if p.enabled:
                enabled_plugins.append(p)

    # print('enabled plugins: ', enabled_plugins)

    content = "{\n  " + "\"foo\": \"bar\"" + "\n}"
    mime = "application/json"

    for p in enabled_plugins:
        content = p.format_body(content, mime)

    print(content)



# Generated at 2022-06-13 22:12:54.421538
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("") == None
    assert type(Conversion.get_converter("application/json")) == ConverterPlugin

# Generated at 2022-06-13 22:13:06.117217
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Without plugins
    test_group = []
    env = Environment()
    test_formatting = Formatting(test_group, env=env)
    test_headers = '''Content-Type: application/json
    Cache-Control: no-cache'''
    test_output_headers = test_formatting.format_headers(test_headers)
    assert test_headers == test_output_headers

    # With plugins
    test_group = ['pretty']
    env = Environment()
    test_formatting = Formatting(test_group, env=env)
    test_headers = '''Content-Type: application/json
    Cache-Control: no-cache'''
    test_output_headers = test_formatting.format_headers(test_headers)

# Generated at 2022-06-13 22:13:19.458313
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fmt = Formatting(['colors'])
    raw_headers = '''
HTTP/1.1 200 OK
Date: Fri, 31 Dec 1999 23:59:59 GMT
Content-Type: text/html
Content-Length: 1354
Last-Modified: Wed, 06 Jan 2016 08:29:53 GMT

'''

# Generated at 2022-06-13 22:13:30.124693
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('text/html'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('application/json'), ConversionPlugin)
    assert isinstance(Conversion.get_converter('text/plain'), ConversionPlugin)
    assert isinstance(Conversion.get_converter('text/xml'), ConversionPlugin)
    assert Conversion.get_converter('text/html').convert('{}') == '{\n    \n}'
    assert Conversion.get_converter('text/html').convert('<html><body><h1>Hello World!</h1></body></html>') == '<html>\n    <body>\n        <h1>\n            Hello World!\n        </h1>\n    </body>\n</html>'

# Generated at 2022-06-13 22:13:32.464128
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    res = Formatting(groups = ["colors"]).format_headers("Content-Type: application/json\n")

# Generated at 2022-06-13 22:13:43.714079
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """Unit test for method format_body() of class Formatting.
    
    :return: None
    """

# Generated at 2022-06-13 22:13:46.986675
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('e')
    assert converter is None

    converter = Conversion.get_converter('application/json')
    assert converter is not None
    assert converter.__class__.__name__ == 'JSONConverter'



# Generated at 2022-06-13 22:13:54.094052
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    environment = Environment()
    mime = 'xml'
    headers = ''
    groups = ['formatting']
    content = '<book><title>test</title><author>test1</author></book>'
    formatter = Formatting(groups, environment, headers=headers)
    formatted_content = formatter.format_body(content, mime)
    expected_content = '<book>\n  <title>test</title>\n  <author>test1</author>\n</book>\n'
    assert formatted_content == expected_content

# Generated at 2022-06-13 22:14:02.768826
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json').mime == 'application/json'
    assert Conversion.get_converter('image/gif').mime == 'image/gif'
    assert not Conversion.get_converter('application/json1')
    assert not Conversion.get_converter('image/gif1')
    assert not Conversion.get_converter('')
    assert not Conversion.get_converter('test')
    assert not Conversion.get_converter(None)

# Generated at 2022-06-13 22:14:06.873526
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    result=Formatting(['colors']).format_headers('HTTP/1.1 200 OK\ncontent-type: application/json')
    assert result=='\x1b[37m\x1b[1mHTTP/1.1\x1b[22m \x1b[32m\x1b[1m200\x1b[22m\x1b[39m \x1b[32m\x1b[1mOK\x1b[22m\x1b[39m\n\x1b[37m\x1b[1mcontent-type:\x1b[22m\x1b[39m \x1b[33m\x1b[1mapplication/json\x1b[22m\x1b[39m\n'


# Generated at 2022-06-13 22:14:09.939808
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(['json', 'colors'])
    print(f.format_body('{"a": "b"}', 'application/json'))

# Generated at 2022-06-13 22:14:19.098442
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """Testing method 'format_body' of class 'Formatting'."""
    input_str = '{"key":"value", "key2":"value2"}'
    expected = '{\n  "key": "value",\n  "key2": "value2"\n}'
    result = Formatting(groups=['format']).format_body(content=input_str, mime='application/json')
    assert result == expected



# Generated at 2022-06-13 22:14:23.579090
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    env = Environment()
    formatting = Formatting(groups=['formatters'], env=env, prettify=True)
    content = formatting.format_body(content='[{"val": 1}, {"val": 2}]', mime='application/json')
    assert content == '[\n  {\n    "val": 1\n  },\n  {\n    "val": 2\n  }\n]'

# Generated at 2022-06-13 22:14:31.867834
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("text/plain"), ConverterPlugin)
    assert not isinstance(Conversion.get_converter("text/plainblah"), ConverterPlugin)
    assert not isinstance(Conversion.get_converter("text/plainblah"), ConverterPlugin)
    assert not isinstance(Conversion.get_converter(""), ConverterPlugin)
    assert not isinstance(Conversion.get_converter("plainblah"), ConverterPlugin)



# Generated at 2022-06-13 22:14:36.993607
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    expected = 'text/html'
    actual = None
    mime = 'text/html'
    converter = Conversion.get_converter(mime)
    if converter is not None:
        actual = converter.mime_type
    assert expected == actual


# Generated at 2022-06-13 22:14:41.070415
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('text/html')
    assert converter.mime == 'text/html'

# Generated at 2022-06-13 22:14:49.294151
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """Test method format_body of class Formatting"""
    formatter_groups = ['colors']
    env = Environment()
    formatting = Formatting(formatter_groups, env=env)
    formatter_mimetypes = [
        'application/json',
        'application/xml',
        'text/html',
        'text/css',
        'text/javascript',
    ]
    for mime in formatter_mimetypes:
        assert formatting.format_body(mime, mime) == mime

# Generated at 2022-06-13 22:14:54.617331
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import HTTPHeadersProcessor, HTTPBodyProcessor
    groups = ['headers', 'body']
    formatting = Formatting(groups)
    assert any(type(x) is HTTPHeadersProcessor for x in formatting.enabled_plugins)
    assert any(type(x) is HTTPBodyProcessor for x in formatting.enabled_plugins)


# Generated at 2022-06-13 22:15:07.457018
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Setup env
    env = Environment(auto_json=False)
    env.stdout = StringIO()
    f = Formatting([], env=env, printer_class=None, display_body_max_len=None)

    # Construct the list of plugin
    available_plugins = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in []:
        for cls in available_plugins[group]:
            p = cls(env=env, stdout=env.stdout,
                display_body_max_len=None, printer_class=None)
            if p.enabled:
                enabled_plugins.append(p)
    f.enabled_plugins = enabled_plugins

    # Run test
    content = "Hello"
    mime = "text/plain"
    assert f.format

# Generated at 2022-06-13 22:15:09.476019
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("application/json"), ConverterPlugin)

# Generated at 2022-06-13 22:15:13.382875
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('text/html'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('text'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('text/a'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('a/text'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('a/b'), ConverterPlugin)


# Generated at 2022-06-13 22:15:19.418852
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    env.config.default_options['output'] = ['format_headers']
    groups_list = ['headers']
    formatting = Formatting(groups_list, env=env)
    headers = formatting.format_headers('Content-Type: application/json')
    assert headers == 'Content-Type: application/json'

# Generated at 2022-06-13 22:15:29.074170
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    f = Formatting(groups=['SyntaxHighlight'])
    print("test_Formatting_format_headers: " + repr(f))


# Generated at 2022-06-13 22:15:42.307614
# Unit test for constructor of class Formatting
def test_Formatting():
    global available_plugins
    available_plugins = plugin_manager.get_formatters_grouped()
    f = Formatting(groups=['matrix', 'space'], env=Environment(),
        indent_size=2, sort_by=('headers', 'columns'), table_format='psql',
        colors = 'always')
    assert len(f.enabled_plugins) == 2
    assert (isinstance(f.enabled_plugins[0], available_plugins['matrix'][0]))
    assert (f.enabled_plugins[0].indent_size == 2)
    assert (f.enabled_plugins[0].sort_by == ('headers', 'columns'))
    assert (f.enabled_plugins[0].table_format == 'psql')
    assert (f.enabled_plugins[0].colors == 'always')
   

# Generated at 2022-06-13 22:15:47.767467
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    env = Environment()
    test_Conversion_get_converter_instance = Conversion.get_converter(env.default_options['format'])

    assert(test_Conversion_get_converter_instance.supports(env.default_options['format']))



# Generated at 2022-06-13 22:15:59.348864
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    e = Environment()
    e.colors = False
    e.headers = False

    f = Formatting(groups=['colors'], env=e)
    # Test the header printed by the plugin Highlight
    expected_result = 'HTTP/1.1 200 OK\r\n'
    result = f.format_headers('HTTP/1.1 200 OK\r\n')
    assert (result == expected_result)

    # Test the case of the environment variables
    # colors and headers set to False
    e.colors = False
    e.headers = False
    f = Formatting(groups=['colors'], env=e)
    expected_result = 'HTTP/1.1 200 OK\r\n'
    result = f.format_headers('HTTP/1.1 200 OK\r\n')

# Generated at 2022-06-13 22:16:03.977684
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins import FormatterPlugin
    from pytest import raises

    class TestPlugin(FormatterPlugin):
        enabled = True
        def format_headers(self, headers: str) -> str:
            return "test"

    plugins = [TestPlugin()]
    formatter = Formatting(groups=[], plugins=plugins)
    assert formatter.format_headers("") == "test"

# Generated at 2022-06-13 22:16:07.500953
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print("\nUnit test for method get_converter of class Conversion\n")
    assert Conversion.get_converter("application/json") is not None



# Generated at 2022-06-13 22:16:10.562844
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fmt = Formatting(groups=['colors'])
    assert fmt.format_headers('HTTP/1.1 200 OK') == '\x1b[92mHTTP/1.1 200 OK\x1b[0m\n'


# Generated at 2022-06-13 22:16:19.899801
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    formatting = Formatting(groups=['colors'], env=env)

# Generated at 2022-06-13 22:16:28.728130
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not Conversion.get_converter('123')
    assert not Conversion.get_converter('test/test')
    assert Conversion.get_converter('application/json')

# Generated at 2022-06-13 22:16:34.073652
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["color", "colors", "compact", "format", "formatters", "json", "pretty",
              "pygments", "solarized", "style", "table", "unix"]
    env = Environment()
    obj = Formatting(groups, env)
    obj.enabled_plugins


# Generated at 2022-06-13 22:16:50.097586
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie import context
    import httpie.output.formatter
    import httpie.output.formatters.default
    import httpie.output.formatters.colors

    context.default_options.colors = True
    groups = {'headers'}
    status_code = None

# Generated at 2022-06-13 22:16:54.649170
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('json')
    assert converter.mime == 'application/json'
    converter = Conversion.get_converter('html')
    assert converter.mime == 'text/html'

# Generated at 2022-06-13 22:17:07.764076
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test = Formatting(['colors'],
                    colors = 'on',
                    style = 'solarized')
    headers = 'HTTP/1.1 200 OK\r\n'\
            'content-type: text/html; charset=utf-8\r\n'\
            'content-length: 13\r\n'\
            'connection: keep-alive\r\n'\
            'server: gunicorn/19.9.0\r\n'\
            'date: Sun, 28 Feb 2016 01:51:29 GMT\r\n'\
            '\r\n'
    result = test.format_headers(headers)

# Generated at 2022-06-13 22:17:14.667916
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert str(converter) == "<ConverterPlugin 'application/json'>"

    converter = Conversion.get_converter("")
    assert converter == None

# Generated at 2022-06-13 22:17:20.666719
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import Formatter
    from httpie.plugins.builtin import COLOR

    available_plugins = {COLOR: [Formatter]}
    f = Formatting([COLOR], 
                   env=Environment(), 
                   available_plugins=available_plugins)
    assert len(f.enabled_plugins) == 1
    assert f.enabled_plugins[0].__class__.__name__ == 'Formatter'

# Generated at 2022-06-13 22:17:31.253322
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # preparing
    f = Formatting(['colors'], headers_extra_style='', headers_prefix='')

    # testing basic tag
    assert f.format_body("<script>", 'text/xml') == "\x1b[31m<script>\x1b[0m"

    # testing tag with attribute
    assert f.format_body("<script type='text/javascript'>", 'text/xml') == "\x1b[31m<script\x1b[0m type='text/javascript'>"

    # testing self-closed tag
    assert f.format_body("<script />", 'text/xml') == "\x1b[31m<script />\x1b[0m"

    # testing multi tags

# Generated at 2022-06-13 22:17:44.896119
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie import cli
    from httpie.context import Environment
    from httpie.output.formatter.colors import CssStyle
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.registry import plugin_manager
    class DefaultFormatting(FormatterPlugin):
        enabled = True
        def format_headers(self, headers: str) -> str:
            return headers
    class TestFormatterPlugin(FormatterPlugin):
        enabled = True
        def format_headers(self, headers: str) -> str:
            return headers + '\n[' + ']'
    plugin_manager.register(TestFormatterPlugin)

    args = cli.parser.parse_args([])
    env = Environment(args)
    f = Formatting(groups=['DefaultFormatting'], env=env)
    assert f.format

# Generated at 2022-06-13 22:17:51.224633
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = 'HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nContent-Length: 11\r\nContent-Type: \r\n\r\n'
    result = Formatting(['HTTP']).format_headers(headers)
    assert 'HTTP/1.1 200 OK\nConnection: keep-alive\nContent-Length: 11\nContent-Type: \n\n' == result

# Generated at 2022-06-13 22:17:54.148727
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json')



# Generated at 2022-06-13 22:18:01.143173
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    class ColorfulPlugin(FormattingPlugin):
        def format_headers(self, headers):
            return '\033[0;36m%s\033[0m' % headers

    plugin_manager.register(ColorfulPlugin)
    formatters = Formatting('color')
    assert formatters.format_headers('X-bla: bla') == '\033[0;36mX-bla: bla\033[0m'



# Generated at 2022-06-13 22:18:03.478130
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    headers = ""
    expected = ""
    assert Formatting(["simple"]).format_body(headers, "text/plain") == expected

# Generated at 2022-06-13 22:18:14.688335
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """
    This function helps to unit test the method format_headers of class Formatting
    :return: None
    """
    # Create a environment object
    env = Environment()

    # Create a Formatting object
    formatting = Formatting(groups=['colors'], env=env)

    # Initialize headers

# Generated at 2022-06-13 22:18:19.013472
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    fmt=Formatting([], **dict(pretty='all', colors='16'))
    assert fmt.format_body('{"test": "hello"}', 'application/json') == '{\n    "test": "hello"\n}'
    assert fmt.format_body('{"test": "hello"}', 'text') is None
    assert fmt.format_body('{"test": "hello"}', 'application/hello') is None
    assert fmt.format_body('{"test": "hello"}', 'application/json; charset=utf-8') == '{\n    "test": "hello"\n}'

# Generated at 2022-06-13 22:18:32.725318
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Non-empty header string
    assert Formatting([]).format_headers("HTTP/1.1 200 OK\n\
Date: 2017-11-26 19:45:23\n\
Content-Type: application/json; charset=UTF-8\n\
Content-Length: 1341\n\
Connection: keep-alive\n\
Server: nginx/1.11.10\n\
\n\
") == "HTTP/1.1 200 OK\n\
Date: 2017-11-26 19:45:23\n\
Content-Type: application/json; charset=UTF-8\n\
Content-Length: 1341\n\
Connection: keep-alive\n\
Server: nginx/1.11.10\n\
\n\
"
    # Empty header string
    assert Format

# Generated at 2022-06-13 22:18:45.236258
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    print("######## Testing method format_body of class Formatting ########")
    body = '{"age": 34, "first_name": "Kaitlin", "friends": ["Dianne", "Tracy", "Carla"], "gender": "F"}'
    content = Formatting(['pretty']).format_body(body, 'application/json')
    if content == '{\n    "age": 34,\n    "first_name": "Kaitlin",\n    "friends": [\n        "Dianne",\n        "Tracy",\n        "Carla"\n    ],\n    "gender": "F"\n}':
        print("Test method format_body of class Formatting successful!")
    else: print("Test method format_body of class Formatting failed!")

# Generated at 2022-06-13 22:18:51.333559
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = """HTTP/1.1 200 OK
    Date: Tue, 20 Mar 2018 11:31:21 GMT
    Server: Apache/2.2.15 (CentOS)
    Last-Modified: Mon, 07 Mar 2016 14:31:20 GMT
    ETag: "2bc44-5276c9775d180"
    Accept-Ranges: bytes
    Content-Length: 110244
    Connection: close
    Content-Type: text/html; charset=UTF-8"""
    formatting = Formatting(['format'])
    formatted_headers = formatting.format_headers(headers)

# Generated at 2022-06-13 22:19:00.497177
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    formatting = Formatting(['colors'], env, style='par')
    headers = "Content-Type: application/json\nDate: Mon, 19 Feb 2018 11:31:36 GMT\nContent-Length: 173"
    formatted_headers = "Content-Type:\x1b[32m application/json\x1b[39m\nDate:\x1b[32m Mon, 19 Feb 2018 11:31:36 GMT\x1b[39m\nContent-Length:\x1b[32m 173\x1b[39m"
    assert formatting.format_headers(headers) == formatted_headers

# Generated at 2022-06-13 22:19:04.301844
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/csv')
    assert not (Conversion.get_converter('aaaa/csv'))
    assert not (Conversion.get_converter('aaaa/bbbb'))

# Generated at 2022-06-13 22:19:10.900290
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatted_string = Formatting(['format']).format_headers('{"X-Request-Id": "d3d3e3a2-b1cf-4dd6-ae52-a665e2b9a1b4"}')
    print("Formatting.format_headers() Result: ", formatted_string)


# Generated at 2022-06-13 22:19:14.878159
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(groups=["format"])
    print(f.format_body(content="[{\"status\": \"success\"}, {\"status\": \"success\"}]", mime="application/json"))

# test_Formatting_format_body()

# Generated at 2022-06-13 22:19:24.761447
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """Test the formatting of headers"""
    input_format = "Content-Length: 4\r\nContent-Type: text/plain; charset=utf-8\r\nServer: CherryPy/18.1.1\r\n"
    expected = "content-length: 4\ncontent-type: text/plain; charset=utf-8\nserver: CherryPy/18.1.1\n"
    returned_value = Formatting("headers").format_headers(input_format)
    assert(expected == returned_value)


# Generated at 2022-06-13 22:19:31.383080
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors']
    kwargs = {'colors':True}
    env = Environment()
    formatting = Formatting(groups, env, **kwargs)
    content = '{"foo": "bar", "baz": [1, 2, 3, 4]}'
    mime = 'application/json'
    content = formatting.format_body(content, mime)

# Generated at 2022-06-13 22:19:33.561623
# Unit test for constructor of class Formatting
def test_Formatting():
    fr = Formatting(["csv"])
    assert fr is not None

# Generated at 2022-06-13 22:19:39.470319
# Unit test for constructor of class Formatting
def test_Formatting():
    pass

# Generated at 2022-06-13 22:19:48.642226
# Unit test for constructor of class Formatting
def test_Formatting():
    with open('./test/fixture/json.txt', 'r') as f_json:
        json_str = f_json.read()
    with open('./test/fixture/html.txt', 'r') as f_html:
        html_str = f_html.read()
    with open('./test/fixture/css.txt', 'r') as f_css:
        css_str = f_css.read()
    with open('./test/fixture/xml.txt', 'r') as f_xml:
        xml_str = f_xml.read()
    with open('./test/fixture/text.txt', 'r') as f_text:
        text_str = f_text.read()
    # Groups are: ['pprint', 'colors', 'format']
   

# Generated at 2022-06-13 22:19:54.259940
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    grp = ['colors']
    hdr = 'HTTP/1.1 200 OK\r\nServer: nginx/1.12.2\r\nDate: Mon, 19 Nov 2018 16:25:20 GMT'
    fmt = Formatting(grp)
    # no color
    print(fmt.format_headers(hdr))
    # color
    print(fmt.format_headers(hdr))


# Generated at 2022-06-13 22:19:56.317401
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    Formatting().format_headers("a b c")


# Generated at 2022-06-13 22:20:04.524908
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    text = '{"name":"Josie","age":23}'
    print("\nHello from method test_Formatting_format_body()")
    print("\nHere's the text before formatting: " + text)
    groups = [Color(env).name]
    fmt = Formatting(groups, env=Environment())
    mime = 'application/json'
    text = fmt.format_body(text, mime)
    print("\nHere's the text after formatting: ")
    print(text)

# Generated at 2022-06-13 22:20:09.047161
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    if converter is not None:
        if converter.mime_type == mime:
            assert True
        else:
            assert False

# Generated at 2022-06-13 22:20:16.095091
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    content = '{a:1, b:2}'
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    if converter == None:
        assert False
    body = converter.encode(content)
    assert body == content
    content = converter.decode(body)
    assert content == body
    assert converter.mime == mime

# Generated at 2022-06-13 22:20:27.642214
# Unit test for constructor of class Formatting
def test_Formatting():
    # Test case 1:
    groups = []
    env = Environment()
    assert isinstance(Formatting(groups, env), Formatting) == True

    # Test case 2:
    groups = ["format", "colors"]
    env = Environment()
    assert isinstance(Formatting(groups, env), Formatting) == True

    # Test case 3:
    groups = ["format", "colors", "styles"]
    env = Environment()
    assert isinstance(Formatting(groups, env), Formatting) == True

    # Test case 4:
    env = Environment()
    try:
        Formatting("format", env)
    except AssertionError:
        assert True
    else:
        assert False

    # Test case 5:
    env = Environment()

# Generated at 2022-06-13 22:20:39.785934
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatter = Formatting(groups=[], env=Environment())
    assert formatter.format_headers("") == ""
    assert formatter.format_headers("Host: abc") == "Host: abc"
    assert formatter.format_headers("Date: Thu, 04 Jun 2020 09:34:16 GMT") == "Date: Thu, 04 Jun 2020 09:34:16 GMT"
    assert formatter.format_headers("Date: Thu, 04 Jun 2020 09:34:16 GMT\nDate: Thu, 04 Jun 2020 09:34:16 GMT") == "Date: Thu, 04 Jun 2020 09:34:16 GMT\nDate: Thu, 04 Jun 2020 09:34:16 GMT"
    assert formatter.format_headers("status: 301") == "status: 301"

# Generated at 2022-06-13 22:20:41.808158
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    Formatting(["JSON"], env)

# https://github.com/jkbrzt/httpie/blob/master/httpie/formatting.py#L67

# Generated at 2022-06-13 22:20:56.039040
# Unit test for constructor of class Formatting
def test_Formatting():
    
    available_plugins = plugin_manager.get_formatters_grouped()
    
    groups = ["formatters_meta"]
    env = Environment()
    kwargs = {"--json": "", "--json-pp": False, "--debug": False}

    F = Formatting(groups, env, **kwargs)
    assert F.enabled_plugins == []

    groups = ["formatters_meta"]
    env = Environment()
    kwargs = {"--json": "", "--json-pp": True, "--debug": False}
    F = Formatting(groups, env, **kwargs)
    assert F.enabled_plugins == [plugin_manager.instantiate(
                                    available_plugins["formatters_meta"][0],
                                    env = env,
                                    **kwargs)]


# Generated at 2022-06-13 22:20:58.245794
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter
    


# Generated at 2022-06-13 22:21:03.571022
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    for group in available_plugins:
        for p in available_plugins[group]:
            x = p(env=Environment())
            assert x.enabled == True
            #print(x)

# Generated at 2022-06-13 22:21:07.683885
# Unit test for constructor of class Formatting
def test_Formatting():
    input = "HTTP/1.1 200 OK\n\n{\"key\": \"value\"}"
    Formatting(['JSON'], None).format_body(input, 'application/json')

# Generated at 2022-06-13 22:21:16.680502
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime1 = "application/json"
    mime2 = "application/xml"
    mime3 = "application/xml;"
    mime4 = "text/html"

    assert Conversion.get_converter(mime1).__class__.__name__ == "JSONConverter"
    assert Conversion.get_converter(mime2).__class__.__name__ == "XMLConverter"
    assert Conversion.get_converter(mime3).__class__.__name__ == "XMLConverter"
    assert Conversion.get_converter(mime4) == None

# Generated at 2022-06-13 22:21:24.176561
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    import pytest
    fmt = Formatting(['url'])
    assert fmt.format_body('http://www.baidu.com', 'text/html') == '\x1b[32m\x1b[1mhttp://www.baidu.com\x1b[0m'
    assert fmt.format_body('http://www.baidu.com', 'application/json') == 'http://www.baidu.com'
    with pytest.raises(ValueError):
        fmt.format_body('http://www.baidu.com', '')


# Generated at 2022-06-13 22:21:34.767679
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Test the format_body method of class Formatting
    import json
    from httpie.plugins.builtin import JSONPrettyPrint
    from httpie.context import Environment
    env = Environment()
    env.stdout_isatty = False
    format_groups = ['pretty']
    content = '{"test": "format_body_of_class_Formatting"}'
    mime = 'application/json'
    data_json_obj = json.loads(content)
    expected_format_body_result = '\n'.join(['{',
        '    "test": "format_body_of_class_Formatting"',
        '}'])
    result = Formatting(format_groups, env).format_body(content, mime)
    assert expected_format_body_result == result

# Generated at 2022-06-13 22:21:42.922433
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ["format"]
    env = Environment()
    formatter = Formatting(groups, env)

# Generated at 2022-06-13 22:21:46.978683
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    success = 0
    for mime in ["application/x-www-form-urlencoded", "text/html"]:
        instance = Conversion.get_converter(mime)
        if instance:
            success += 1
    assert success == 2



# Generated at 2022-06-13 22:21:50.609476
# Unit test for constructor of class Formatting
def test_Formatting():
    p = Formatting(groups=['highlight', 'colors'])
    assert p.enabled_plugins[0].__class__.__name__ == 'HighlightFormatter'

# Generated at 2022-06-13 22:22:06.974617
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    p1 = plugin_manager.get_formatters_grouped()["colors"]
    processor1 = p1[0]("json", env=Environment())
    p2 = plugin_manager.get_formatters_grouped()["compact"]
    processor2 = p2[0]("json", env=Environment())
    f = Formatting(["colors", "compact"], env=Environment(), colors=True, indent=True)
    headers = u'Content-Type: application/json\r\nContent-Length: 9\r\n\r\n'
    output = f.format_headers(headers)
    assert output == processor1.format_headers(processor2.format_headers(headers))


# Generated at 2022-06-13 22:22:10.923455
# Unit test for constructor of class Formatting
def test_Formatting():
    test_groups = ["JSON"]
    test_env = Environment()
    test_kwargs = {"indent":""}
    test = Formatting(test_groups, test_env, test_kwargs)
    assert test != None
    

# Generated at 2022-06-13 22:22:12.977788
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    fmt = Formatting(['colors'], env, 'pretty')