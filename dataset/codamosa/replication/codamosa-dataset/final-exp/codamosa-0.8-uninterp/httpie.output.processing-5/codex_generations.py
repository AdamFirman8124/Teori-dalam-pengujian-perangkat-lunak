

# Generated at 2022-06-13 22:12:17.469966
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('test/test'), ConverterPlugin)


# Generated at 2022-06-13 22:12:23.025386
# Unit test for constructor of class Formatting
def test_Formatting():
    """
    Test constructor of class Formatting
    :return:
    """
    available_plugins = plugin_manager.get_formatters_grouped()
    Formatting(["body"])
    Formatting(["headers"])
    Formatting(["body", "headers"])

# Generated at 2022-06-13 22:12:25.058523
# Unit test for constructor of class Formatting
def test_Formatting():
    formatting = Formatting(['colors'])
    assert len(formatting.enabled_plugins) == 2

# Generated at 2022-06-13 22:12:27.875839
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    result = Conversion.get_converter("application/json")
    assert isinstance(result, ConverterPlugin)


# Generated at 2022-06-13 22:12:33.791172
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    # Execute the command scoped for this function
    result = run('echo "GET http://httpbin.org HTTP/1.1\nAccept: */*\nUser-Agent: HTTPie/0.9.5\n\n" | HTTPie -f')

    # Verifies the output it is correct
    assert result.output == """\
GET http://httpbin.org HTTP/1.1
Accept: */*
User-Agent: HTTPie/0.9.5


"""

# Generated at 2022-06-13 22:12:46.910566
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """
    The unit test for method get_converter of class Conversion,
    verify the ConverterPlugin can be retrieved in different conditions.

    """
    # Case 1: Content-Type Header is not specified
    content_type_header = None
    converter = Conversion.get_converter(content_type_header)
    assert converter is None

    # Case 2: Content-Type Header is invalid
    content_type_header = "invalid"
    converter = Conversion.get_converter(content_type_header)
    assert converter is None

    # Case 3: Content-Type Header is not supported
    content_type_header = "unsupported/content-type"
    converter = Conversion.get_converter(content_type_header)
    assert converter is None

    # Case 4: Content-Type Header is supported, with registered converter


# Generated at 2022-06-13 22:13:00.836241
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # arrange
    headers = str("Date: Mon, 27 Jul 2009 12:28:53 GMT\n"
                  "Server: Apache/2.2.14 (Win32)\n"
                  "Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\n")
    formatting = Formatting(groups=['colors'])

    # act
    result = formatting.format_headers(headers)

    # assert
    assert result == str("\x1b[94mDate:\x1b[0m Mon, 27 Jul 2009 12:28:53 GMT\n"
                         "\x1b[94mServer:\x1b[0m Apache/2.2.14 (Win32)\n"
                         "\x1b[94mLast-Modified:\x1b[0m Wed, 22 Jul 2009 19:15:56 GMT\n")

# Generated at 2022-06-13 22:13:12.247506
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(['colors'])
    headers = f.format_headers("date: Mon, 27 Jul 2009 12:28:53 GMT\nserver: Apache\nx-powered-by: PHP/5.2.6-1+lenny9\nlast-modified: Mon, 27 Jul 2009 12:28:53 GMT\ntransfer-encoding: chunked\ncontent-type: application/json; charset=UTF-8\n\n")

# Generated at 2022-06-13 22:13:14.786477
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins.builtin import JSONConverter
    c=Conversion.get_converter("application/json")
    assert isinstance(c,JSONConverter)



# Generated at 2022-06-13 22:13:19.695116
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    p = Formatting(groups=['format', 'colors'])
    content = '{"a": "b"}'
    mime = 'application/json'
    assert (p.format_body(content, mime)) == '{\n    "a": "b"\x1b[0m\n}\x1b[0m\n'

# Generated at 2022-06-13 22:13:24.518077
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    p = Conversion.get_converter('application/json')
    assert p is not None



# Generated at 2022-06-13 22:13:34.229535
# Unit test for constructor of class Formatting
def test_Formatting():
    formats = Formatting(['highlight', 'format'])
    # There are four formatters.
    # But two of them are disabled by default,
    # because the windows console does not support ANSI escape code.
    assert len(formats.enabled_plugins) == 2
    # The plugin manager will return the first formatter
    # with the same name in different groups.
    # So we can only expect the first element of enabled_plugins list.
    assert formats.enabled_plugins[0].name == 'highlight'
    assert formats.enabled_plugins[1].name == 'format'

# Generated at 2022-06-13 22:13:41.247847
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    assert Formatting([]).format_body("<h1>Good</h1>","text/html") == "<h1>Good</h1>"
    assert Formatting(["colors"]).format_body("{\"id\": 1, \"goodbye\": false}", "application/json") == '{\x1b[92m"id"\x1b[39m: \x1b[94m1\x1b[39m, \x1b[91m"goodbye"\x1b[39m: \x1b[94mfalse\x1b[39m}'

# Generated at 2022-06-13 22:13:50.471638
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    cvt = Conversion.get_converter('text/csv')
    assert cvt.__class__.__name__ == 'CSVConverter'
    cvt = Conversion.get_converter('application/json')
    assert cvt.__class__.__name__ == 'JSONConverter'
    cvt = Conversion.get_converter('application/xml')
    assert cvt.__class__.__name__ == 'XMLConverter'
    cvt = Conversion.get_converter('test/test')
    assert cvt is None


# Generated at 2022-06-13 22:13:54.310707
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter.mime == "application/json"

# Generated at 2022-06-13 22:13:56.614937
# Unit test for constructor of class Formatting
def test_Formatting():
    formatter = Formatting(['color', 'format'])
    assert formatter.enabled_plugins

# Generated at 2022-06-13 22:14:00.119395
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins.builtin import HTMLConverter

    assert isinstance(Conversion.get_converter('text/html'), HTMLConverter)


# Generated at 2022-06-13 22:14:05.730200
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment(colors=256)
    formating = Formatting(groups=["format", "colors"], env=env)
    assert formating.enabled_plugins[0].__class__.__name__ == 'Colors'
    assert formating.enabled_plugins[1].__class__.__name__ == 'Formatting'


# Generated at 2022-06-13 22:14:19.330253
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    ff = Formatting('color')
    headers = '''HTTP/1.1 200 OK\r
server: nginx/1.10.3 (Ubuntu)\r
date: Wed, 29 May 2019 00:52:34 GMT\r
content-type: application/json; charset=UTF-8\r
content-length: 160\r
x-ratelimit-limit: 60\r
x-ratelimit-remaining: 59\r
x-ratelimit-reset: 1559179898\r
strict-transport-security: max-age=15768000\r
vary: Origin, Accept-Encoding\r
x-frame-options: SAMEORIGIN\r
x-content-type-options: nosniff\r
x-xss-protection: 1; mode=block\r
\r
'''
   

# Generated at 2022-06-13 22:14:22.949734
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import Formatter
    availability = {'form': [Formatter]}
    formatting = Formatting(['form'], availability)
    assert formatting.enabled_plugins[0].name == 'Formatter'

# Generated at 2022-06-13 22:14:34.894542
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    f = Formatting(groups=['colors'], style='solarized', scheme='http',
                   auth=False, auto_json=True, body_style=False, pretty=True,
                   print_body=True, verify=True)
    headers = '''HTTP/1.1 200 OK
Content-Type: text/plain
Date: Mon, 10 Sep 2018 14:58:21 GMT
Server: WSGIServer/0.1 Python/2.7.9
X-Frame-Options: SAMEORIGIN

'''
    result = f.format_headers(headers)


# Generated at 2022-06-13 22:14:41.358485
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    H = "Host: localhost:80\r\nConnection: keep-alive\r\nContent-Length: 7\r\n"
    f = Formatting(['colors'], warn_color='yellow', notify_color='yellow')
    assert f.format_headers( H ) == 'Host:\x1b[33mlocalhost:80\x1b[0m\r\nConnection: keep-alive\r\nContent-Length: 7\r\n'


# Generated at 2022-06-13 22:14:53.832251
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.context import Environment

    available_plugins = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in ['json']:
        for cls in available_plugins[group]:
            p = cls(env=Environment(), color=True)
            if p.enabled:
                enabled_plugins.append(p)

    json_content = '{"foo": 12345}'
    mime = 'application/json'

    for p in enabled_plugins:
        json_content = p.format_body(json_content, mime)


# Generated at 2022-06-13 22:15:01.744188
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    data = '''HTTP/1.1 200 OK
Content-Length: 22
Content-Type: application/json; charset=UTF-8
Date: Wed, 09 Jan 2019 01:43:13 GMT

{
    "x": "y"
}
'''
    response_headers = data[:data.find('\n\n')]
    formatting = Formatting(groups=['colors'])

# Generated at 2022-06-13 22:15:06.470122
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fmt = Formatting(['colors'])
    headers = fmt.format_headers('HTTP/1.1 200 OK\nHost:localhost\nContent-Type:application/json\n')
    assert headers == 'HTTP/1.1 200 OK\nHost:localhost\nContent-Type:application/json\n'

# Generated at 2022-06-13 22:15:15.401632
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json") is not None
    assert Conversion.get_converter("application/xml") is not None
    assert Conversion.get_converter("application/x-www-form-urlencoded") is not None
    assert Conversion.get_converter("image/jpeg") is not None
    assert Conversion.get_converter("text/plain") is not None
    assert Conversion.get_converter("application/json") is not None
    assert Conversion.get_converter("application/json;charset=ISO-8859-1") is not None
    assert Conversion.get_converter("text/csv") is not None
    assert Conversion.get_converter("text/x-whatever") is not None

# Generated at 2022-06-13 22:15:27.042602
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Test case 1
    print ('Test case 1:')
    mime = 'text/plain'
    converter = Conversion.get_converter(mime)
    assert converter.supports('text/plain') is True
    # Test case 2
    print ('Test case 2:')
    mime = 'text/javascript'
    converter = Conversion.get_converter(mime)
    assert converter.supports('text/javascript') is True
    # Test case 3
    print ('Test case 3:')
    mime = 'text/c++'
    converter = Conversion.get_converter(mime)
    assert converter is None
    # Test case 4
    print ('Test case 4:')
    mime = ''
    converter = Conversion.get_converter(mime)
    assert converter is None


#

# Generated at 2022-06-13 22:15:29.500938
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter("text/plain")
    assert(c.supports("text/plain"))


# Generated at 2022-06-13 22:15:32.728237
# Unit test for constructor of class Formatting
def test_Formatting():
    fmt = Formatting(['colors'], env=Environment(),**{})
    assert len(fmt.enabled_plugins) == 1

# Generated at 2022-06-13 22:15:40.097944
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin, builtin_plugins
    env = Environment()
    fmt = Formatting(['colors'], env)
    for p in fmt.enabled_plugins:
        assert isinstance(p, FormatterPlugin)
        assert p in builtin_plugins()
    with pytest.raises(KeyError):
        Formatting(['no_such_group'], env)



# Generated at 2022-06-13 22:15:45.831659
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    plugins = plugin_manager.get_formatters_grouped()
    available_plugins = [cls() for cls in plugins['color']]

    assert isinstance(available_plugins, list)

# Generated at 2022-06-13 22:15:48.002685
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['colors'])
    # print(f.enabled_plugins)



# Generated at 2022-06-13 22:15:51.701601
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    fm = Formatting(groups=['colors'])
    headers = 'Connection:close\n'
    assert fm.format_headers(headers) == 'Connection:close'


# Generated at 2022-06-13 22:15:56.825227
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    J = lambda **kwargs: json.loads(Formatting('body', **kwargs).format_body(json.dumps(kwargs), 'application/json'))
    assert J(hello='world', xyz=123) == {"hello": "world", "xyz": 123}
    assert J(items=[1, 2, 3]) == {"items": [1, 2, 3]}

    assert '\n'.join(Formatting().format_body("""{
"hello": "world!",
"xyz": 123
}""", 'application/json').splitlines()) == """{
    "hello": "world!",
    "xyz": 123
}"""

# Generated at 2022-06-13 22:15:59.909904
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()
    print("available_plugins: " + str(available_plugins))


# Generated at 2022-06-13 22:16:04.980395
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # if the mimetype is invalid, return None
    mime = "invalid mimetype"
    assert not is_valid_mime(mime)
    assert not Conversion.get_converter(mime)

    # if the mimetype is valid, return a converter object
    mime = "application/json"
    converter = Conversion.get_converter(mime)
    assert is_valid_mime(mime)
    assert converter


# Generated at 2022-06-13 22:16:15.894558
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    try:
        from httpie.formatters.colors import ColorsFormatter
    except ImportError:
        pytest.skip("colors formatter not available")

    # Arrange
    groups = ["colors"]
    env = Environment()
    kwargs = {}
    formatting = Formatting(groups, env, **kwargs)

# Generated at 2022-06-13 22:16:30.369925
# Unit test for constructor of class Formatting
def test_Formatting():
    params = {
        'groups': ['highlight'],
        'env': Environment(),
        'prettify': True
    }
    test_class = Formatting(**params)
    assert test_class.enabled_plugins[0].prettify
    params['prettify'] = False
    test_class = Formatting(**params)
    assert not test_class.enabled_plugins[0].prettify

# Generated at 2022-06-13 22:16:41.326370
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatted = Formatting(["pretty"]).format_headers("Accept:text/html\r\nOrigin: file://\r\n")
    assert formatted == "Accept: text/html\nOrigin: file://\n"
    formatted = Formatting(["pretty"]).format_headers("Accept:text/html\n")
    assert formatted == "Accept: text/html\n"
    formatted = Formatting(["pretty"]).format_headers("Accept:text/html\r")
    assert formatted == "Accept: text/html\r"
    formatted = Formatting(["pretty"]).format_headers("Accept:text/html\r\n")
    assert formatted == "Accept: text/html\r\n"
    formatted = Formatting(["pretty"]).format_headers("Accept:text/html\n\n")

# Generated at 2022-06-13 22:16:44.164327
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    env = Environment()
    f = Formatting(['colors'], env)
    assert '#ffffff' == f.format_body('#ffffff', 'text/html')

# Generated at 2022-06-13 22:16:53.392791
# Unit test for constructor of class Formatting
def test_Formatting():
    F = Formatting(["foo", "bar"], use_colors=False)
    assert len(F.enabled_plugins) == 2
    assert F.enabled_plugins[0].__class__.__name__ == "FooProcessor"
    assert F.enabled_plugins[0].use_colors is False
    assert F.enabled_plugins[1].__class__.__name__ == "BarProcessor"
    assert F.enabled_plugins[1].use_colors is False

# Generated at 2022-06-13 22:17:07.223313
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    group = ["color"]
    environment = Environment()
    formatting = Formatting(group, environment)
    headers = "HTTP/1.1 200 OK\r\nDate: Wed, 25 Mar 2020 13:54:23 GMT\r\nServer: Apache\r\nExpires: Thu, 19 Nov 1981 08:52:00 GMT\r\nCache-Control: no-store, no-cache, must-revalidate\r\nPragma: no-cache\r\nContent-Length: 10\r\nSet-Cookie: sess=932000; path=/\r\nSet-Cookie: nocache=1; path=/\r\nContent-Type: text/html\r\n"

# Generated at 2022-06-13 22:17:08.647371
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter != None
    assert converter.supports('application/json')


# Generated at 2022-06-13 22:17:12.467663
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert isinstance(Conversion.get_converter('application/json'), ConverterPlugin)
    assert Conversion.get_converter('text') is None
    assert Conversion.get_converter('') is None



# Generated at 2022-06-13 22:17:19.241761
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    import random
    import string
    import json

    def random_string(length):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

    def random_choice(lst):
        i = random.randint(0, len(lst) - 1)
        return lst[i]

    def random_json():
        lst = []
        for _ in range(4):
            lst.append((random_string(4), random_string(4)))
        return json.dumps(lst)

    def random_raw():
        lst = []
        for _ in range(4):
            lst.append('{}: {}'.format(random_string(4), random_string(4)))

# Generated at 2022-06-13 22:17:31.190351
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import PrettyOptions
    env = Environment()
    options = PrettyOptions(
        indent=4,
        sort_keys=True,
        colors=False,
        ssl_verify=True,
        default_options=True,
        print_body_only=False
    )
    jf = JSONFormatter(env=env, options=options)
    groups = ["json"]
    f = Formatting(groups, env=env, options=options)
    assert f.format_body('{"text": "test", "number": 0}', "application/json") == jf.format_body('{"text": "test", "number": 0}', "application/json")


# Generated at 2022-06-13 22:17:36.910664
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(['colors'], env=Environment(), max_colors=30)
    expected = [plugin_manager.get_formatters_grouped()['colors'][0](env=Environment(), max_colors=30)]
    assert f.enabled_plugins == expected



# Generated at 2022-06-13 22:17:40.576560
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    """
    Get any converter
    """
    conv = Conversion.get_converter("application/json")
    assert conv is not None

test_Conversion_get_converter()

# Generated at 2022-06-13 22:17:44.777099
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    pairs = Formatting([], env=Environment())
    print(pairs.format_headers(headers='HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nabcabc'))



# Generated at 2022-06-13 22:17:54.172853
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Given
    import json
    import pygments # type: ignore

    class PygmentsFormatter(pygments.formatters.TerminalFormatter):
        pass
    class CustomFormatter(ConverterPlugin):
        def format_body(self, content, mime):
            return pygments.highlight(json.dumps(content, indent=2), pygments.lexers.JsonLexer(), PygmentsFormatter())
    
    env = Environment()
    kwargs = {}
    groups = ["json"]
    f = Formatting(groups=groups, env=env, **kwargs)
    mime = "json"
    content = { "key": "value"}
    expected_result = json.dumps(content, indent=2)

# Generated at 2022-06-13 22:18:02.571267
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    assert not is_valid_mime(None)
    assert not is_valid_mime('')
    assert not is_valid_mime('/')
    assert not is_valid_mime('foo')
    assert not is_valid_mime('foo/bar/baz')

    assert is_valid_mime('foo/bar')
    assert is_valid_mime('foo-bar/baz-qux')



# Generated at 2022-06-13 22:18:14.425974
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    available_plugins = plugin_manager.get_formatters_grouped()
    f = Formatting(['colors'], env=Environment(), **{})
    # normal case
    headers = "HTTP/1.1 200 OK\r\nDate: Tue, 28 May 2019 15:26:16 GMT\r\nLast-Modified: Tue, 28 May 2019 15:20:03 GMT\r\nEtag: " \
              "\"5cee0d7b-44\"\r\nServer: Apache/2.4.25 (Debian)\r\nVary: Accept-Encoding\r\nContent-Length: 68\r\nContent-Type: " \
              "application/json; charset=utf-8\r\n\r\n"
    res = f.format_headers(headers)

# Generated at 2022-06-13 22:18:18.676284
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    test_class = Formatting(groups=['colors'],
                            theme='solarized-light',
                            colors=True)
    mime = "application/json"
    content = '{"key": "value"}'
    result = test_class.format_body(content, mime)
    assert result == '{\x1b[38;5;246m"key"\x1b[39m: \x1b[38;5;40m"value"\x1b[39m}'



# Generated at 2022-06-13 22:18:31.130436
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.core import main
    from httpie.output.streams import STDOUT

    import json
    from json import JSONDecodeError
    from typing import Dict
    from io import TextIO

    @plugin_manager.transform_stdout
    def transform_stdout(stdout: TextIO, is_terminal: bool,
                         force_colors: bool) -> TextIO:
        return stdout

    def get_json_response(args: list, env: Environment) -> Dict:
        """
        Execute http request and return the decoded json content
            :param args: arguments to be passed to the request
            :param env: Environment() object
            :return: json dictionary of the response
        """
        response_data = main(args, stdout=STDOUT, env=env)

# Generated at 2022-06-13 22:18:35.569715
# Unit test for constructor of class Formatting
def test_Formatting():
    fmt = Formatting(['colors'])
    assert len(fmt.enabled_plugins) == 1

    # Empty group list
    fmt = Formatting([])
    assert not fmt.enabled_plugins

    # Invalid group name
    fmt = Formatting(['invalid group name'])
    assert not fmt.enabled_plugins

# Generated at 2022-06-13 22:18:42.618138
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    assert converter is not None
    assert converter.supports(mime) is True
    assert converter.to_string('{"name": "Find out who you are"}') == \
           '{\n    "name": "Find out who you are"\n}'
    assert converter.to_string('"quote"') == '"quote"'



# Generated at 2022-06-13 22:18:49.987498
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins import FormatterPlugin

    class TestFormatterPlugin(FormatterPlugin):

        def format_body(self, body: str, mime: str):
            return "foobar"

    class TestConverterPlugin(ConverterPlugin):

        def supports(self, mime_type):
            return mime_type == "application/json"

        def convert(self, content: str):
            return '{}'

    plugin_manager.register(TestConverterPlugin)
    plugin_manager.register(TestFormatterPlugin)
    tested = Formatting(["test"])

    assert tested.format_body("test", "application/json") == "foobar"

# Generated at 2022-06-13 22:18:54.016080
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from httpie.plugins.builtin import JSONPointer
    converter = Conversion.get_converter('application/json')
    assert(converter == JSONPointer)

# Generated at 2022-06-13 22:18:57.155532
# Unit test for constructor of class Formatting
def test_Formatting():
    test = Formatting(groups=['uglyjson'])
    assert test.enabled_plugins[0].__class__.__name__ == 'PrettyJsonFormat'

# Generated at 2022-06-13 22:19:05.700252
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    groups = ['colors']
    env = Environment(colors='off')
    f = Formatting(groups, env)
    headers = '''Content-Length: 390\nContent-Type: application/json; charset=utf-8\nDate: Wed, 27 Feb 2019 12:36:09 GMT\nETag: W/"194-sE4Q4xN/RuJW/9XFv/3OgSbAx0pk"\nVary: Accept-Encoding\nX-Powered-By: Express'''
    result = f.format_headers(headers)

# Generated at 2022-06-13 22:19:20.251566
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    formatter = Formatting(groups=['colors'], colors=False)
    assert formatter.format_headers('HTTP/1.1 200 OK\r\nCache-Control: no-cache\r\nDate: Fri, 24 May 2019 19:41:39 GMT\r\n\r\n') == 'HTTP/1.1 200 OK\r\nCache-Control: no-cache\r\nDate: Fri, 24 May 2019 19:41:39 GMT\r\n\r\n'

# Generated at 2022-06-13 22:19:27.880235
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    """
    Test cases for method format_body of class Formatting
    """
    # Test case: Input: mime = 'text/plain'
    #             Expected output: content
    assert Formatting([], env=Environment()).format_body(
        content = 'hello',
        mime = 'text/plain'
    ) == 'hello'

    # Test case: Input: mime = 'application/json'
    #             Expected output: content
    assert Formatting([], env=Environment()).format_body(
        content = 'hello',
        mime = 'application/json'
    ) == 'hello'

    # Test case: Input: mime = ''
    #             Expected output: content

# Generated at 2022-06-13 22:19:31.444863
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert (issubclass(converter.__class__, ConverterPlugin))


# Generated at 2022-06-13 22:19:37.029998
# Unit test for method format_headers of class Formatting

# Generated at 2022-06-13 22:19:45.327607
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    assert isinstance(Conversion.get_converter(mime), ConverterPlugin)

    mime = 'application/xml'
    assert Conversion.get_converter(mime) is None

    mime = 'application/x-www-form-urlencoded'
    assert isinstance(Conversion.get_converter(mime), ConverterPlugin)

    mime = 'plain/text'
    assert isinstance(Conversion.get_converter(mime), ConverterPlugin)

# Generated at 2022-06-13 22:19:50.577208
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    class formatter(object):
        def __init__(self, env=Environment(), **kwargs):
            self.enabled = True
        def format_body(self, content: str, mime: str) -> str:
            return mime
    converter = formatter()
    assert converter.format_body('this', 'application/json') == 'this'

# Generated at 2022-06-13 22:19:55.296881
# Unit test for constructor of class Formatting
def test_Formatting():
    import json
    json_data = json.dumps({'foo': 'bar'}, indent=4)
    fmt = Formatting(['json'])
    assert fmt.format_body(json_data, 'application/json') == json_data

    fmt = Formatting(['json', 'colors'])
    assert fmt.format_body(json_data, 'application/json') != json_data

# Generated at 2022-06-13 22:19:56.937898
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    pass


# Generated at 2022-06-13 22:19:58.573187
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print(Conversion.get_converter('application/json'))


# Generated at 2022-06-13 22:20:00.953737
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(groups=['json'])
    print(f.format_body('{"username":"test"}', 'application/json'))

# Generated at 2022-06-13 22:20:19.105120
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    case1 = 'application/json'
    case2 = 'application/xml'
    case3 = 'application/wml'
    case4 = 'application/jsonxml'
    answer1 = Conversion.get_converter(case1)
    answer2 = Conversion.get_converter(case2)
    answer3 = Conversion.get_converter(case3)
    answer4 = Conversion.get_converter(case4)
    print(answer1)
    print(answer2)
    print(answer3)
    print(answer4)


# Generated at 2022-06-13 22:20:25.360848
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['format.json']
    env = Environment(stdin=BytesIO(b'{"b": "c"}'),
                      stdin_isatty=True)
    result = Formatting(groups, env).format_body('{"b": "c"}',
                                                 'application/json')
    assert result == '{\n  "b": "c"\n}'

# Generated at 2022-06-13 22:20:32.135837
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    format_body_result = Formatting(['colors']).format_body("{ \"name\": \"Tom\" }", "application/json")
    assert format_body_result == "{ \x1b[32m\"name\"\x1b[39m: \x1b[34m\"Tom\"\x1b[39m }\n"

# Generated at 2022-06-13 22:20:35.089485
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("text/html") is None
    assert isinstance(Conversion.get_converter("application/json"), ConverterPlugin)

# Generated at 2022-06-13 22:20:43.082389
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    json_str = '{"foo": "bar" }'
    formatted_str = '[b]foo: bar[/b]'

    from httpie.plugins.builtin import HTTPieJSONOutput
    from httpie.plugins.builtin import HTTPieBoldOutput
    from httpie.utils import get_response_writer

    class TestHTTPieJSONOutput(HTTPieJSONOutput):
        def format_body(self, body, mime):
            return json_str

    class TestHTTPieBoldOutput(HTTPieBoldOutput):
        def format_headers(self, headers):
            return formatted_str

    # First, create a list of Formatting plugins

# Generated at 2022-06-13 22:20:49.367992
# Unit test for constructor of class Formatting
def test_Formatting():
    import tempfile
    temp = tempfile.NamedTemporaryFile()
    environment = Environment(stdout_isatty=temp.fileno() != 0,
                              stdin_isatty=temp.fileno() != 0,
                              stdin=temp,
                              stdout=temp)
    testFormatter = Formatting(['default'], env=environment)
    assert testFormatter != None

# Generated at 2022-06-13 22:20:54.976293
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    formatting = Formatting(['highlight'])
    print(formatting.format_body('{"foo": "bar"}', 'application/json'))
    print(formatting.format_body('{"foo": "bar"}', ''))
    print(formatting.format_body('', ''))


if __name__ == '__main__':
    test_Formatting_format_body()

# Generated at 2022-06-13 22:21:02.440411
# Unit test for constructor of class Formatting
def test_Formatting():
    import sys
    import os
    import tempfile
    from textwrap import dedent

    from httpie.plugins.builtin import HTTPieJSONFormatter
    from httpie.plugins.builtin import HTTPiePrettyFormatter
    from httpie.plugins.builtin import HTTPiePrettyStreamFormatter

    stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    tmp = tempfile.mkdtemp()
    os.environ['HTTPIE_JSON_PRETTY_NO_COLOR'] = '1'
    os.environ['HTTPIE_TEMPLATE_DIR'] = tmp
    os.environ['HTTPIE_JSON_FILE_TEMPLATES'] = 'default.j2'

# Generated at 2022-06-13 22:21:04.752665
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion.get_converter('image/png')
    assert isinstance(c, ConverterPlugin)

# Generated at 2022-06-13 22:21:13.685098
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    class JsonConverter(ConverterPlugin):
        type = "json"
        extensions = ("json",)
        media_type = "application/json"
        media_type_params = {
            "charset": "utf-8",
        }

        @staticmethod
        def supports(mime):
            return mime == "application/json"

        def convert_from(self, data, mime):
            return "change"

    class JsonConverter2(ConverterPlugin):
        type = "json"
        extensions = ("json",)
        media_type = "application/json"
        media_type_params = {
            "charset": "utf-8",
        }

        @staticmethod
        def supports(mime):
            return mime == "application/json"


# Generated at 2022-06-13 22:21:41.307319
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    groups = ["colors", "formatters"]
    env = Environment()
    kwargs = {"style": "solarized"}
    format = Formatting(groups, env, **kwargs)
    headers = "HTTP/1.1 200 OK\nDate: Fri, 12 Oct 2018 04:10:12 GMT\n" \
              "Server: Apache/2.4.29 (Ubuntu)\nLast-Modified: Fri, 25 Jan 2019 13:56:31 GMT\n" \
              "ETag: \"2c6-5845cdcb29400\"\nAccept-Ranges: bytes\nContent-Length: 710\n" \
              "Content-Type: text/html\n\n"

# Generated at 2022-06-13 22:21:43.927151
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    print(Formatting(["colors"]).format_headers("HTTP/1.1 200 OK\r\n"))


# Generated at 2022-06-13 22:21:48.211384
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    # Expected group names
    group = ['JSON','XML','HTML','Markdown','Text','Style','Colors','Other']
    for i in group:
        available_plugins[i] = []

    Formatting(group, env=Environment())

# Generated at 2022-06-13 22:21:50.623972
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']
    environment = Environment()
    formatting = Formatting(groups, env=environment)
    assert formatting
    assert formatting.enabled_plugins

# Unit tests for methods of class Formatting

# Generated at 2022-06-13 22:21:53.711522
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not Conversion.get_converter("text/html")
    assert Conversion.get_converter("application/json").supports("application/json")

# Generated at 2022-06-13 22:22:06.838439
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    format_headers_test = Formatting(['colors'], headers_color='red')

# Generated at 2022-06-13 22:22:10.525953
# Unit test for constructor of class Formatting
def test_Formatting():
    fmt = Formatting(['colors'])
    assert len(fmt.enabled_plugins) == 1
    assert fmt.enabled_plugins[0]._name == 'colors'



# Generated at 2022-06-13 22:22:19.638814
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins.builtin import Arguments
    from httpie.context import Environment
    env = Environment(arguments=Arguments())
    header = "Content-Type: application/json"
    headers = Formatting(['headers'], env=env).format_headers(header)
    assert headers == header
    headers = Formatting(['headers'], env=env).format_headers('Content-Type: text/html')
    assert headers == 'Content-Type: text/html'
