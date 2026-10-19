

# Generated at 2022-06-13 22:12:28.510835
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():

    # ----------------- Test with pprint.pformat(object, indent=indent, width=width) --------------- #
    # 'pprint' is a built-in Python module
    # object: object to be pformatted
    # indent: integer, can be 0 or not, default is 4
    # width: integer, can be 0 or not, default is 80
    # pprint.pformat(object, indent=indent, width=width) returns a string
    # Each line of the string will be printed with the indent X spaces before it; one exception is the first line of
    # the string, which is printed starting from the left edge. It is also called pretty-printing.

    my_dict = {'key 1': 'value 1', 'key 2': 'value 2', 'key 3': 'value 3'}

# Generated at 2022-06-13 22:12:32.093084
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)
    # application/json is not a valid mime type
    assert Conversion.get_converter('application/json') is None

# Generated at 2022-06-13 22:12:35.953918
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(['colors'])
    assert f.format_headers("HTTP/1.1 200 OK\r\n") == "HTTP/1.1 200 OK\r\n"


# Generated at 2022-06-13 22:12:39.487122
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatting = Formatting(['colors'])
    headers = formatting.format_headers('{"greeting":"Hello, world!"}\n')
    assert headers == '{"greeting":"Hello, world!"}\n'

# Generated at 2022-06-13 22:12:49.413234
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    '''
    Test for method format_headers of class Formatting.
    This testcase uses a test response obtained from pypi.org as input.
    The expected output is obtained from Postman.
    '''

    # Set up test response
    request_headers = '''GET /pypi/ HTTP/1.1\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nHost: pypi.org\r\nUser-Agent: HTTPie/0.9.9\r\n\r\n'''

    # Set up expected result

# Generated at 2022-06-13 22:12:59.312577
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.compat import is_windows
    from httpie.plugins import FormatterPlugin

    class UpperCaseFormatter(FormatterPlugin):
        def format_headers(self, headers: str) -> str:
            return headers.upper()

    plugin_manager.register(UpperCaseFormatter)
    # Make sure that the formatter plugin was registered on windows too.
    if is_windows:
        plugin_manager._get_formatters_grouped()

    fs = Formatting(['all'])
    assert fs.format_headers('Content-Type: application/json') == \
        'CONTENT-TYPE: APPLICATION/JSON'



# Generated at 2022-06-13 22:13:00.860825
# Unit test for constructor of class Formatting
def test_Formatting():
    f=Formatting(['colors'])
    assert type(f.enabled_plugins) == list


# Generated at 2022-06-13 22:13:04.579278
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import HTTPieHighlight
    f = Formatting(['colors', 'formatters'])
    assert isinstance(f.enabled_plugins[0], HTTPieHighlight)

# Generated at 2022-06-13 22:13:18.003811
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # If no plugins are in use, it should return the same content
    formatting = Formatting([])
    body = "{\"test\":\"value\"}"
    mime = "application/json"
    assert formatting.format_body(body, mime) == body
    # If no plugins are in use and MIME is not valid, it should return
    # the same content
    mime = "application/xml"
    assert formatting.format_body(body, mime) == body
    # If a valid plugin is in use, it should return the content formatted
    from httpie.plugins.builtin import PrettyFormatPlugin
    formatting = Formatting(["pretty"])
    body = "{\"test\":\"value\"}"
    mime = "application/json"
    expected_body = """\
{
    "test": "value"
}"""
   

# Generated at 2022-06-13 22:13:29.449511
# Unit test for constructor of class Formatting
def test_Formatting():
    import sys
    import os

    sys.path.append(os.path.dirname(__file__) + "/../")
    from httpie.plugins.builtin import HTTPHeadersFormatPlugin
    from httpie.plugins.builtin import JSONformatPlugin
    from httpie.plugins import FormatterPlugin


    def enabled(self):
        return True

    def format_headers(self, headers):
        return "format_headers"

    FormatterPlugin.enabled = enabled
    FormatterPlugin.format_headers = format_headers
    JSONformatPlugin.enabled = enabled
    JSONformatPlugin.format_body = format_headers
    HTTPHeadersFormatPlugin.enabled = enabled
    f = Formatting(groups=["format"])
    assert f.enabled_plugins[0].__class__.__name__ == 'HTTPHeadersFormatPlugin'

# Generated at 2022-06-13 22:13:33.406828
# Unit test for constructor of class Formatting
def test_Formatting():
    Formatting(groups=['colors'])

# Generated at 2022-06-13 22:13:38.803578
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json")  is not None
    assert Conversion.get_converter("application/json; charset=utf-8")  is not None
    assert Conversion.get_converter("application/xml")  is None
    assert Conversion.get_converter("application/xml; charset=utf-8")  is None

# Generated at 2022-06-13 22:13:45.322678
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert is_valid_mime('application/json') == True
    assert is_valid_mime('application/xml') == True
    assert is_valid_mime('application/html') == True
    assert is_valid_mime('application/pdf') == True
    assert is_valid_mime('text/html') == True
    assert is_valid_mime('text/csv') == True
    assert is_valid_mime('text/plain') == True

    assert is_valid_mime('./html') == False
    assert is_valid_mime('abc') == False
    assert is_valid_mime('/pdf') == False
    assert is_valid_mime('a/') == False
    assert is_valid_mime('/a') == False

# Generated at 2022-06-13 22:13:49.242980
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    body = '{"hello": "world", "foo": "bar"}'
    mime = 'application/json'
    f = Formatting(groups=['pjson'])
    print(f.format_body(body, mime))


# Generated at 2022-06-13 22:13:59.370148
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    test_string = '{"test": "test"}'
    test_mime = 'application/json'

    # Apply only default formatting
    test_group = ['default']
    fmt = Formatting(test_group)
    result_without_json = fmt.format_body(test_string, test_mime)

    # Apply json formatting
    test_group = ['default', 'json']
    fmt = Formatting(test_group)
    result_with_json = fmt.format_body(test_string, test_mime)

    assert result_without_json == test_string
    assert result_with_json != test_string

# Generated at 2022-06-13 22:14:07.508358
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    # case 1: not enabled
    groups = []
    env = Environment()
    fmt = Formatting(groups, env)
    headers = "hello world"
    formatted_headers = fmt.format_headers(headers)
    assert formatted_headers == headers

    # case 2: enabled
    groups = ["nocolor"]
    fmt = Formatting(groups, env)
    formatted_headers = fmt.format_headers(headers)
    assert formatted_headers == '{0:>20} {1}\n'.format('hello', 'world')


# Generated at 2022-06-13 22:14:10.006534
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter("text/html"),ConverterPlugin)

# Generated at 2022-06-13 22:14:23.026514
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()
    groups = ['colors', 'format', 'pretty']
    env = Environment()
    kwargs = {}
    enabled_plugins = []
    for group in groups:
        for cls in available_plugins[group]:
            p = cls(env=env, **kwargs)
            if p.enabled:
                enabled_plugins.append(p)
    f = Formatting(groups=groups)
    assert f.format_body(content="{'hello': 'world'}", mime="application/json") == """\
{\033[94m\033[1m'hello'\033[0m: \033[92m'world'\033[0m}"""
    assert f.format_body(content="hello world", mime="text/plain")

# Generated at 2022-06-13 22:14:26.114610
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """Test method get_converter of class Conversion."""
    



# Generated at 2022-06-13 22:14:30.950019
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    class TestFormatterPlugin(FormattingPlugin):
        def format_body(self, content, mime):
            return 'test'
    plugin_manager.register(TestFormatterPlugin)
    formatter = Formatting()
    assert formatter.format_body('test', 'test/test') == 'test'

# Generated at 2022-06-13 22:14:42.916124
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    xml = '<?xml version="1.0"?><note><to>Tove</to></note>'
    sample_mime = "text/xml"
    converter = Conversion.get_converter(sample_mime)
    converted = converter.apply(xml)
    existed_tree = ['note', 'to', 'Tove']
    for element in existed_tree:
        assert element in converted
    html = '<!DOCTYPE html><html><head></head><body><div id="content"></div></body></html>'
    sample_mime = "text/html"
    converter = Conversion.get_converter(sample_mime)
    converted = converter.apply(html)
    existed_tree = ['html', 'head', 'body', 'div']

# Generated at 2022-06-13 22:14:50.056308
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    class Converter1(ConverterPlugin):
        pass

    class Converter2(ConverterPlugin):
        pass

    plugin_manager.register(Converter1)
    plugin_manager.register(Converter2)

    assert Conversion.get_converter('') is None
    assert Conversion.get_converter('text/html') is None

    assert isinstance(Conversion.get_converter('application/json'), Converter2)

# Generated at 2022-06-13 22:14:52.697948
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    
    # Setup
    testF = Formatting(['colors'])

    # Test
    assert testF.format_headers("test") == "test"



# Generated at 2022-06-13 22:15:01.102931
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'html'
    assert is_valid_mime(mime) == True
    converter = Conversion.get_converter(mime)
    assert converter.content_type == 'text/html'

    mime = 'text/html'
    assert is_valid_mime(mime) == True
    converter = Conversion.get_converter(mime)
    assert converter.content_type == 'text/html'

    mime = 'text/'
    assert is_valid_mime(mime) == False
    converter = Conversion.get_converter(mime)
    assert converter == None

    mime = '/html'
    assert is_valid_mime(mime) == False
    converter = Conversion.get_converter(mime)
    assert converter == None


# Generated at 2022-06-13 22:15:04.446561
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter_class = Conversion.get_converter('audio/wav')
    assert converter_class.mime == 'audio/wav'


# Generated at 2022-06-13 22:15:04.989443
# Unit test for constructor of class Formatting
def test_Formatting():
    pass

# Generated at 2022-06-13 22:15:11.037536
# Unit test for constructor of class Formatting
def test_Formatting():
    # When class Formatting is created with argument in right type, 
    # the value of self.enabled_plugins is expected to be a list.
    assert isinstance(Formatting(groups=['Formatter']).enabled_plugins, list) 
    # When class Formatting is created with argument in incorrect type, 
    # the value of self.enabled_plugins is expected to be a list.
    assert isinstance(Formatting(groups=None).enabled_plugins, list)

# Generated at 2022-06-13 22:15:17.694351
# Unit test for constructor of class Formatting
def test_Formatting():
    data = {'headers': 'a: 1\nb: 2', 'mime': 'test/test'}
    formatting = Formatting(['headers', 'body'])
    assert formatting.format_headers(data['headers']) == data['headers']
    assert formatting.format_body(data['headers'], data['mime']) == data['headers']



# Generated at 2022-06-13 22:15:26.978517
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('text/html'), ConverterPlugin)
    assert Conversion.get_converter('image/svg') is None
    assert isinstance(
        Conversion.get_converter('application/json'), ConverterPlugin)
    assert Conversion.get_converter('application/yaml') is None
    assert isinstance(Conversion.get_converter('text/css'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('text/xml'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('text/markdown'), ConverterPlugin)


# Generated at 2022-06-13 22:15:28.665576
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ["headers"]
    env = Environment()
    f = Formatting(groups, env)
    assert f

# Generated at 2022-06-13 22:15:41.634966
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import json
    from httpie.plugins.builtin import HTTPHeadersProcessor

    processor = HTTPHeadersProcessor()
    available_plugins = plugin_manager.get_formatters_grouped()
    headers = "Content-Type: application/json\r\nContent-Length: 35\r\n\r\n"
    actual = processor.format_headers(headers)
    expected = json.dumps(dict(
        [(pair.split(": ", 1)[0], ": ".join(pair.split(": ", 1)[1:])) for pair in headers.strip().split("\n")],
        indent=4
    ))

    assert expected == actual

# Generated at 2022-06-13 22:15:54.574605
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Arrange
    grouplst = ['colors']
    env = Environment()
    kwargs = {"style": "solarized"}
    obj = Formatting(grouplst, env, **kwargs)
    # Act
    result = obj.format_body('{"key1": "value1", "key2": "value2"}', 'application/json')
    # Assert

# Generated at 2022-06-13 22:16:00.064228
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("txt/plain") is None
    assert isinstance(Conversion.get_converter("image/png"), ConverterPlugin)


# Generated at 2022-06-13 22:16:02.612280
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = "text/html"
    assert Conversion.get_converter(mime)

# Generated at 2022-06-13 22:16:06.360000
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    f = Formatting(["colors"], env)

# Generated at 2022-06-13 22:16:14.542068
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    formatter = Formatting(['colors'], env)
    assert formatter.format_headers('Connection: keep-alive\nContent-Type: application/json') == '\x1b[36mConnection\x1b[39;49;00m: \x1b[39;49;00mkeep-alive\r', '\n\x1b[36mContent-Type\x1b[39;49;00m: \x1b[39;49;00mapplication/json'


# Generated at 2022-06-13 22:16:29.717928
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['colors'], env=Environment(), force_colors=True)
    print(f.enabled_plugins[0].__class__)
    print(f.enabled_plugins[0].__class__.__name__)
    assert f.enabled_plugins[0].__class__.__name__ == 'JSONFormatter'

# Generated at 2022-06-13 22:16:41.009702
# Unit test for constructor of class Formatting
def test_Formatting():
    requirements = [
        "https://github.com/jakubroztocil/httpie/blob/master/httpie/plugins/builtin.py",
        "https://github.com/jakubroztocil/httpie/blob/master/httpie/plugins/manager.py",
        'https://github.com/jakubroztocil/httpie/blob/master/httpie/context.py#L39',
        'https://github.com/jakubroztocil/httpie/blob/master/httpie/plugins/registry.py',
        'https://github.com/jakubroztocil/httpie/blob/master/tests/test_default_plugins.py#L58'
    ]

    # Construct an instance of class Formatting

# Generated at 2022-06-13 22:16:47.499244
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """
    Test Formatting.format_headers method
    """
    formatting = Formatting(['colors'])
    headers = 'Content-Type: application/json\r\nHost: example.com\r\n\r\n'
    assert formatting.format_headers(headers) == '\x1b[92mContent-Type\x1b[0m: application/json\r\n\x1b[92mHost\x1b[0m: example.com\r\n\r\n'


# Generated at 2022-06-13 22:16:49.308729
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json").mime == "application/json"


# Generated at 2022-06-13 22:16:52.577165
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    pass

# Generated at 2022-06-13 22:17:06.235807
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_headers = '''
    HTTP/1.1 200 Ok
    Date: Sat, 17 Nov 2018 19:37:37 GMT
    Server: Apache
    Last-Modified: Fri, 08 Oct 2010 20:27:00 GMT
    ETag: "381026-141d-48d4558b7ea40"
    Accept-Ranges: bytes
    Content-Length: 5336
    Cache-Control: max-age=86400
    Expires: Sun, 18 Nov 2018 19:37:37 GMT
    Content-Type: text/html
    '''
    a=Formatting(['colors'])
    b=a.format_headers(test_headers)
    print(b)
    assert b.count('\n') == 13, "The number of lines should be 13."

# Generated at 2022-06-13 22:17:09.428893
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.builtin import PrettyOptionsPlugin
    # Test for a simple header like 'name: value'
    s = 'name: value'
    # Test for a header like 'name: value\nother_name: other_value'
    p = PrettyOptionsPlugin(None)
    assert p.format_headers(s) == 'name: value'



# Generated at 2022-06-13 22:17:16.418054
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import subprocess
    res = subprocess.run(["hget", 'https://httpbin.org/post', '-d', 'color=blue'],
            encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    headers = res.stdout.splitlines()[0]
    f = Formatting(['colors'])
    f.format_headers(headers)



# Generated at 2022-06-13 22:17:19.352383
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    assert is_valid_mime(mime)
    converter = Conversion.get_converter(mime)
    assert not (converter is None)
    mime = 'application/foobar'
    assert is_valid_mime(mime)
    converter = Conversion.get_converter(mime)
    assert converter is None


# Generated at 2022-06-13 22:17:30.876157
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(groups=['colors'])
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Foo: Bar\r\n'
        'X-Bar: Baz\r\n'
        '\r\n'
    )

# Generated at 2022-06-13 22:17:44.352268
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.context import Environment


# Generated at 2022-06-13 22:17:48.073221
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    test_mime = 'application/foo'
    assert is_valid_mime(test_mime) == True
    assert Conversion.get_converter(test_mime) == None
    


# Generated at 2022-06-13 22:17:59.200372
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json").mime == "application/json"
    assert Conversion.get_converter("application/x-json").mime == "application/json"
    assert Conversion.get_converter("application/json; charset=utf-8") == None
    assert Conversion.get_converter("application/json123") == None
    assert Conversion.get_converter("json") == None
    assert Conversion.get_converter("application/json") != None
    assert Conversion.get_converter("application/json; charset=utf-8") != None
    assert Conversion.get_converter("application/json123") != None

# Generated at 2022-06-13 22:18:04.867524
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # -------------- Valid mime type test -------------
    # Asks for a converter for a valid mime type, then expects the returned
    # converter to be able to convert the mime type
    converter = Conversion.get_converter("text/html")
    assert converter.supports("text/html")
    # -------------- Invalid mime type test -------------
    # Asks for a converter for an invalid mime type, then expects the returned
    # converter to be None
    assert Conversion.get_converter("asd") is None

# Generated at 2022-06-13 22:18:16.583087
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formater = Formatting(groups = ['colors'])
    header = "HTTP/1.1 200 OK\r\n" \
             "Content-Type: text/html; charset=utf-8\r\n" \
             "Content-Length: 9\r\n" \
             "\r\n" \
             "<h1>Hello</h1>"
    result = formater.format_headers(header)

# Generated at 2022-06-13 22:18:18.587748
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('text/plain')
    assert c.content_type == 'text/plain'

# Generated at 2022-06-13 22:18:25.416149
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = """
HTTP/1.1 200 OK
Server: gunicorn/19.9.0
Date: Thu, 18 Jul 2019 01:28:17 GMT
Connection: close
Content-type: application/json

"""
    groups = ['colors']
    formatting = Formatting(groups)
    formatted = formatting.format_headers(headers)

    assert formatted != headers


# Generated at 2022-06-13 22:18:34.139186
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import textwrap
    # format_headers method only deals with colored section and HTTP method

# Generated at 2022-06-13 22:18:41.939456
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()

    groups = ['colors']
    enabled_plugins = []
    for group in groups:
        for cls in available_plugins[group]:
            p = cls()
            if p.enabled:
                enabled_plugins.append(p)

    for p in enabled_plugins:
        content = p.format_body('{}', 'application/json')
        assert content == '{}'



# Generated at 2022-06-13 22:18:46.186097
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    converter = Conversion.get_converter('application/json')
    formatting = Formatting(groups=['colors'])
    assert formatting.format_body('{"test": 1}', 'application/json') == converter.to_terminal('{"test": 1}')

# Generated at 2022-06-13 22:18:49.906855
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # test for json-to-hcl
    print(Conversion.get_converter("application/json"))
    # test for hcl-to-json
    print(Conversion.get_converter("application/hcl"))



# Generated at 2022-06-13 22:18:53.053744
# Unit test for constructor of class Formatting
def test_Formatting():
    group_list = ['colors', 'format']
    env = Environment()
    Formatting(group_list, env)

# Generated at 2022-06-13 22:19:01.047602
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    content = 'foo'
    mime = 'application/json'
    env = Environment()
    kwargs = ''
    groups = ['json']
    formatting = Formatting(groups, env, kwargs)
    assert formatting.format_body(content, mime) == 'foo'
    groups = ['json', 'colors']
    formatting = Formatting(groups, env, kwargs)
    assert formatting.format_body(content, mime) == '\x1b[39mfoo\x1b[0m'

# Generated at 2022-06-13 22:19:12.337388
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:19:19.720856
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(['colors'])
    assert f


# Generated at 2022-06-13 22:19:22.979991
# Unit test for constructor of class Formatting
def test_Formatting():
    environment = Environment()
    formatting = Formatting(['colors'], env=environment)
    assert formatting.enabled_plugins != []

# Generated at 2022-06-13 22:19:26.039173
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Prepare
    mime = "application/json"
    # Execute
    converter = Conversion.get_converter(mime)
    # Verify
    assert converter is not None


# Generated at 2022-06-13 22:19:33.829583
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()
    plugin_list = [cls(env=Environment(), ) for cls in available_plugins['colors']]
    test_Formatting = Formatting(['colors'],env=Environment())
    test_Formatting.enabled_plugins = plugin_list
    content = test_Formatting.format_body('{"name":"dongzhi","age"1}','application/json')
    print(content)


# Generated at 2022-06-13 22:19:36.561131
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter is not None
    converter = Converte

# Generated at 2022-06-13 22:19:41.502809
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("text/html")
    assert converter.__class__.__name__ == "HTMLConverter"

    converter = Conversion.get_converter("application/xml")
    assert converter.__class__.__name__ == "XMLConverter"


# Generated at 2022-06-13 22:19:46.514179
# Unit test for constructor of class Formatting
def test_Formatting():
    formatting = Formatting([])
    assert formatting.enabled_plugins == []
    formatting = Formatting(["test"])
    assert formatting.enabled_plugins == []
    formatting = Formatting(["json"])
    assert len(formatting.enabled_plugins) == 1
    assert formatting.enabled_plugins[0]._name == "json"

# Generated at 2022-06-13 22:19:53.796396
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = """HTTP/1.1 200 OK
Connection: keep-alive
Content-Type: application/json
Date: Tue, 23 Oct 2018 14:14:58 GMT
Server: nginx
Via: 1.1 varnish
X-Cache: HIT
X-Cache-Hits: 1
Transfer-Encoding: chunked
"""
    groups = ['colors', 'formatters', 'formatters_aliases']
    formatting = Formatting(groups, groups=groups)
    assert 'HTTP/1.1 200 OK' in formatting.format_headers(headers)

# Generated at 2022-06-13 22:20:04.299568
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    def converter(mime):
        return Conversion.get_converter(mime)

    assert not converter('text')
    assert converter('text/plain')
    assert converter('text/plain; charset=UTF-8')
    assert not converter('text/plain;charset=UTF-8')
    assert converter('application/json')
    assert converter('application/json; charset=UTF-8')
    assert not converter('application/json;charset=UTF-8')
    assert not converter('application/json; charset="UTF-8"')
    assert not converter('application/json; charset="UTF-8"')



# Generated at 2022-06-13 22:20:06.028881
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json')



# Generated at 2022-06-13 22:20:18.667232
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not is_valid_mime('app/octet-stream')
    assert Conversion.get_converter('application/json')



# Generated at 2022-06-13 22:20:20.947138
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    assert Formatting(['format']).format_body('{}', 'application/json') == '{}'

# Generated at 2022-06-13 22:20:26.636200
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('text/html')
    assert converter == None

    converter = Conversion.get_converter('application/json')
    assert converter.mime == 'application/json'
    assert converter.supports('application/json')
    assert not converter.supports('text/html')


# Generated at 2022-06-13 22:20:29.329928
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting(["colors"])
    assert Formatting(["colors"], debug=True)



# Generated at 2022-06-13 22:20:32.587879
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """Tests method get_converter of class Conversion"""
    converter_class = Conversion.get_converter('application/json')
    converter = converter_class('application/json')
    assert converter.mime == 'application/json'


# Generated at 2022-06-13 22:20:41.921813
# Unit test for constructor of class Formatting
def test_Formatting():
    def side_effect_cls(env=Environment(), arg='value'):
        return arg

    con = Formatting(groups=['colors'])
    # test enabled plugins
    assert con.enabled_plugins == []
    # test color plugin
    plugin = mock.Mock()
    plugin.get_colors = side_effect_cls
    plugin.get_style = side_effect_cls
    plugin.supports_color = side_effect_cls
    plugin.enabled = True

    with mock.patch('httpie.plugins.registry.plugin_manager.get_formatters') as get_formatters:
        get_formatters.return_value = [plugin]
        con = Formatting(groups=['colors'])
        # test enabled plugins

# Generated at 2022-06-13 22:20:50.654768
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    import json
    import sys

    sys.stdout = open('formatting_output.txt', 'w', encoding='utf-8')
    output = Formatting(groups=['json']).format_body(body, 'application/json')
    print(output)

    with open('formatting_output.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(output), f, indent=4)


if __name__ == '__main__':
    test_Formatting_format_body()

# Generated at 2022-06-13 22:20:54.236881
# Unit test for constructor of class Formatting
def test_Formatting():
    formatting_groups, formatting_kwargs = {}, {}
    formatting_groups = ['colors', 'colors']
    formatting_kwargs = {'style': 'foo'}
    x = Formatting(formatting_groups, formatting_kwargs)

# Generated at 2022-06-13 22:21:00.186637
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(['colors'])
    assert f.format_body('{"a": "b"}', 'application/json') == '\x1b[36m{\x1b[39m\x1b[92m"a"\x1b[39m\x1b[93m:\x1b[39m\x1b[92m"b"\x1b[39m\x1b[36m}\x1b[39m'

# Generated at 2022-06-13 22:21:03.512790
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    text = "this is a message"
    f = Formatting(["headers"])
    res = f.format_body(text, "text/plain")
    assert res == text

# Generated at 2022-06-13 22:21:35.699241
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("text/html").mime == "text/html"
    assert Conversion.get_converter("text/html").name == "html"
    assert Conversion.get_converter("application/json").mime == "application/json"
    assert Conversion.get_converter("application/json").name == "json"
    assert Conversion.get_converter("text/plain").mime == "text/plain"
    assert Conversion.get_converter("text/plain").name == "raw"
    assert Conversion.get_converter("text/plain").supports("text/plain") == True
    assert Conversion.get_converter("text/plain").supports("application/json") == False
    assert Conversion.get_converter("unknown").name is None

# Generated at 2022-06-13 22:21:39.651740
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    result = Conversion.get_converter("application/json")
    print(result)
    assert isinstance(result, ConverterPlugin)


# Generated at 2022-06-13 22:21:47.689865
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    groups = ["colors"]
    h_list = ['content-type: text/html', 'content-encoding: gzip']
    h_list_expected = ['\033[34mcontent-type\033[39m: text/html', '\033[34mcontent-encoding\033[39m: gzip']
    f = Formatting(groups, pretty=True)
    h_list_res = f.format_headers(h_list)
    assert h_list_res == h_list_expected


# Generated at 2022-06-13 22:21:56.078956
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """Test cases for method get_converter() of class Conversion"""
    # an instance of class ConverterPlugin
    converter = Conversion.get_converter('application/json')
    assert(converter.__class__.__name__ == 'JSONConverter')
    # None
    assert(Conversion.get_converter('junk/abcd') == None)



# Generated at 2022-06-13 22:21:59.987771
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    assert converter



# Generated at 2022-06-13 22:22:06.696045
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # when
    output_headers = Formatting(groups=["headers"]).format_headers("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")

    # then
    assert output_headers == '🔬HTTP/1.1 200 OK\r\n🔬Content-Type: text/html\r\n\r\n'


# Generated at 2022-06-13 22:22:16.114964
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    available_plugins = plugin_manager.get_formatters_grouped()
    group = "colors"
    for cls in available_plugins[group]:
        if cls.supports(env=Environment()):
            p = cls(env=Environment())
            break
    headers = """HTTP/1.1 200 OK
Server: gunicorn/19.8.1
Date: Tue, 04 Dec 2018 05:23:04 GMT
Connection: close
Content-Type: application/json; charset=utf-8
Content-Length: 225
Access-Control-Allow-Origin: http://127.0.0.1:8080
Access-Control-Allow-Credentials: true
Vary: Accept, Cookie
Allow: GET, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN

"""
    assert p.format_