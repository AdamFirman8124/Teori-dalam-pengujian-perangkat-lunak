

# Generated at 2022-06-13 22:12:15.010004
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment(stdout_isatty=False)
    formatting = Formatting(["colors"], env=env)
    formatted = formatting.format_headers("content")
    assert formatted == "content"


# Generated at 2022-06-13 22:12:25.271609
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter.mime == "application/json"
    assert converter.supports("application/json")
    assert not converter.supports("application/xml")
    assert not converter.supports("application")
    assert not converter.supports("json")
    assert not converter.supports("")
    assert not converter.supports(None)
    assert not Conversion.get_converter("json")
    assert not Conversion.get_converter("")
    assert not Conversion.get_converter(None)

# Generated at 2022-06-13 22:12:29.816635
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():

    class fm(Formatting):
        def __init__(self, **kwargs):
            pass
        def format_headers(self, headers):
            return headers

    ff = fm()
    assert ff.format_headers("Content-Type: application/json") == "Content-Type: application/json"

# Generated at 2022-06-13 22:12:39.197929
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Test on converter plugin
    class TestConverterPlugin(ConverterPlugin):
        def __init__(self, mimetype):
            super().__init__(mimetype)

        @classmethod
        def convert(cls, content: str, mimetype: str) -> Optional[str]:
            return f'{content} - {mimetype}'

    # Register plugin
    plugin_manager.register_plugin(TestConverterPlugin)

    # test instance
    c = Conversion()

    # test on mimetype 'text/html'
    assert c.get_converter('text/html').convert('hello', 'text/html') == 'hello - text/html'

    # test on mimetype 'text/plain'

# Generated at 2022-06-13 22:12:46.703606
# Unit test for constructor of class Formatting
def test_Formatting():
    testHeader = "HTTP/1.1 200 OK\nContent-Length: 0\n\n"
    testBody = "1"
    testMIME = "text/html"
    groups = ["highlighting", "colors"]
    formatter = Formatting(groups)
    testHeader = formatter.format_headers(testHeader)
    testBody = formatter.format_body(testBody, testMIME)

# Generated at 2022-06-13 22:13:00.554592
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Expected output:
    # {
    #     "Profile": "https://url.to.json.schema/user_profile_schema.json",
    #     "User-Agent": "HTTPie/1.0.0"
    # }

    input_str = """\
HTTP/1.1 200 OK
Content-Type: application/json
Profile: https://url.to.json.schema/user_profile_schema.json
User-Agent: HTTPie/1.0.0
"""
    output_str = Formatting(['headers'], indent=4).format_headers(input_str)

# Generated at 2022-06-13 22:13:12.059308
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    """
    @author: Yukun
    :return:
    """
    # arrange
    parameters = ["HTTP headers"]
    groups = ["HTTP headers"]
    env = Environment(colors=True, stdin=sys.stdin, stdout=sys.stdout,
                      stdin_isatty=True, stdout_isatty=True)

# Generated at 2022-06-13 22:13:15.753421
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('application/json')
    assert not Conversion.get_converter('abc/abc')
    assert not Conversion.get_converter('')


# Generated at 2022-06-13 22:13:27.861951
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    '''
    Create a Formatting object with no arguments
    '''
    f = Formatting()

    '''
    Pass 1 header line.
    Expect 1 line returned.
    The value should be unchanged (it's already formatted)
    '''
    assert f.format_headers('Content-Type: text/plain') == 'Content-Type: text/plain'

    '''
    Pass 2 header lines.
    Expect the 2 lines returned, with no change to each value
    '''
    assert f.format_headers('Content-Type: text/plain\nContent-Disposition: attachment') \
           == 'Content-Type: text/plain\nContent-Disposition: attachment'

    '''
    Pass 3 header lines.
    Expect the 3 lines returned, with no change to each value
    '''

# Generated at 2022-06-13 22:13:38.118137
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ["format", "colors"]
    env = Environment()
    from httpie.plugins.builtin import Formatter
    from httpie.plugins.builtin import Colors
    Formatter(env=env, **{})
    Colors(env=env, **{})
    f = Formatting(groups, env)
    f.format_body("{}", "application/json") == "{}"
    f.format_body("{}", "text/html") == "{}"
    f.format_body("{}", "text/plain") == "{}"
    f.format_body("{}", "text/javascript") == "{}"

# Generated at 2022-06-13 22:13:52.945410
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = 'date: 2018-10-29 18:40:53\nserver: Werkzeug/0.14.1 Python/3.6.6\ncontent-type: text/html; charset=utf-8\ncontent-length: 4242\n\n';

# Generated at 2022-06-13 22:14:00.617998
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter(
        'application/vnd.docker.distribution.manifest.v2+json') is not None
    assert Conversion.get_converter('application/vnd.docker.image.rootfs.diff') is not None
    assert Conversion.get_converter('application/vnd.docker.image.rootfs.diff.tar.gzip') is not None
    assert Conversion.get_converter('application/vnd.docker.image.rootfs.foreign.diff.tar.gzip') is not None
    assert Conversion.get_converter('application/vnd.docker.image.rootfs.layer.tar.gzip') is not None

# Generated at 2022-06-13 22:14:04.823414
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # test case 1
    a = Conversion.get_converter('a/b')
    assert a is None
    # test case 2
    b = Conversion.get_converter('application/json')
    assert b is not None


# Generated at 2022-06-13 22:14:10.110459
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    assert Formatting(groups=["highlight"]).format_headers("headers") == "headers"
    assert Formatting(groups=["highlight"], headers_theme="base16").format_headers("headers") == "headers"



# Generated at 2022-06-13 22:14:20.608065
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    c = Conversion()
    assert c.get_converter('application/json')
    assert c.get_converter('text/plain')
    assert c.get_converter('text/html')
    assert c.get_converter('text/xml')
    assert c.get_converter('text/csv')
    assert c.get_converter('text/javascript')
    assert c.get_converter('application/javascript')
    assert c.get_converter('application/vnd.api+json')
    assert c.get_converter('application/vnd.hal+json')
    assert not c.get_converter('xxx')
    assert not c.get_converter('text')
    assert not c.get_converter('application')

# Generated at 2022-06-13 22:14:29.833541
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_plugin1 = 'httpie.plugins.builtin.format.JSONPrettyFormatPlugin'
    test_plugin2 = ('httpie.plugins.builtin.format.JsonBodyHighlightFormatPlugin')
    test_env = 'httpie.context.Environment'
    test_headers = "['Content-Type', 'Content-Range', 'Content-Encoding']"
    test_groups = ['json']
    test_kwargs = {'sort': '0'}

    test_formatting = Formatting(groups=test_groups, env=test_env, **test_kwargs)
    test_formatting.enabled_plugins.append(test_plugin1)
    test_formatting.enabled_plugins.append(test_plugin2)

    assert(test_formatting.format_headers(headers=test_headers) == test_headers)


# Generated at 2022-06-13 22:14:41.917496
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    header = {'status_line': 'HTTP/1.1 200 OK', 'headers': [('Connection', 'keep-alive'), ('Content-Type', 'application/json; charset=utf-8'), ('ETag', 'W/"3e3b3a2a1bb71c8a047a33d21a6dcb52"'), ('X-Powered-By', 'Express'), ('Content-Length', '29')], 'body': '{"success":true,"message":""}'}
    # header = 'status_line: HTTP/1.1 200 OK\nConnection: keep-alive\nContent-Type: application/json; charset=utf-8\nETag: W/"3e3b3a2a1bb71c8a047a33d21a6dcb52"\nX-Powered-By: Express\

# Generated at 2022-06-13 22:14:43.669237
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter("application/json") is not None

# Generated at 2022-06-13 22:14:55.337946
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors']
    env = Environment()
    kwargs = {}
    f = Formatting(groups, env, **kwargs)
    assert f.format_body('test', 'application/json') == 'test'
    assert f.format_body('test', 'text/html') == 'test'
    assert f.format_body('test', 'text/xml') == 'test'
    assert f.format_body('test', 'text/plain') != 'test'
    assert f.format_body('test', 'text/plain') == '\x1b[39mtest\x1b[39m'
    assert f.format_body('test', 'text/css') != 'test'

# Generated at 2022-06-13 22:15:08.049002
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import HeadersFormatter
    fmt = Formatting(groups=['json'], env=Environment())
    assert len(fmt.enabled_plugins) == 1
    assert fmt.enabled_plugins[0].__class__ is JSONFormatter
    fmt = Formatting(groups=['headers'], env=Environment())
    assert len(fmt.enabled_plugins) == 1
    assert fmt.enabled_plugins[0].__class__ is HeadersFormatter
    fmt = Formatting(groups=['json', 'headers'], env=Environment())
    assert len(fmt.enabled_plugins) == 2
    assert fmt.enabled_plugins[0].__class__ is JSONFormatter
    assert fmt.enabled_plugins[1].__class__ is HeadersFormatter



# Generated at 2022-06-13 22:15:20.946545
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in ["format"]:
        for cls in available_plugins[group]:
            p = cls(env=Environment(), **{})
            if p.enabled:
                enabled_plugins.append(p)

    content = '{"a": "b"}'
    for p in enabled_plugins:
        content = p.format_body(content, "application/json")
    print(content)
    assert content == '{\n  "a": "b"\n}'

if __name__ == "__main__":
    test_Formatting_format_body()

# Generated at 2022-06-13 22:15:22.271119
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    pass


# Generated at 2022-06-13 22:15:24.915576
# Unit test for constructor of class Formatting
def test_Formatting():
    assert isinstance(Formatting([]), Formatting)
    assert isinstance(Formatting(["colors"]), Formatting)


# Generated at 2022-06-13 22:15:28.947355
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    assert Conversion.get_converter(mime).convert(b'{"a":"b"}').decode() == '{"a": "b"}'


# Generated at 2022-06-13 22:15:32.896851
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter.__class__.__name__ == 'JSONConverter'


# Generated at 2022-06-13 22:15:35.246395
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert converter == "JsonConverterPlugin"

# Generated at 2022-06-13 22:15:42.719225
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter('text/plain').__class__.__name__ == "PlainTextConverter"
    assert Conversion.get_converter('application/json').__class__.__name__ == "JsonConverter"
    assert isinstance(Conversion.get_converter('application/yaml'), ConverterPlugin)
    assert isinstance(Conversion.get_converter('test/test'), type(None))
    assert isinstance(Conversion.get_converter(None), type(None))
    assert isinstance(Conversion.get_converter(' '), type(None))
    assert isinstance(Conversion.get_converter('text/plain-test'), type(None))


# Generated at 2022-06-13 22:15:51.118433
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    ConverterPlugin.supported_mimes = ['text/plain']
    ConverterPlugin.supported_mimes.append('text/html')
    c = Conversion.get_converter('text/html')
    assert c is not None
    assert c.mime == 'text/html'
    c = Conversion.get_converter('text/plain')
    assert c is not None
    assert c.mime == 'text/plain'
    c = Conversion.get_converter('text/json')
    assert c is None

# Generated at 2022-06-13 22:15:58.780645
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert is_valid_mime(None) == False
    assert is_valid_mime('asdsad') == False
    assert is_valid_mime('application/json') == True

    assert Conversion.get_converter(None) == None
    assert Conversion.get_converter('asdsad') == None
    c = Conversion.get_converter('application/json')
    assert c.supports('application/json')
    assert c.supports('application/geo+json')
    assert c.supports('application/ld+json')
    assert not c.supports('asdsad')


# Generated at 2022-06-13 22:16:05.413292
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter_json_1 = Conversion.get_converter('application/json')
    assert converter_json_1
    assert converter_json_1.mime == 'application/json'

    converter_json_2 = Conversion.get_converter('application/json; charset=utf-8')
    assert converter_json_2
    assert converter_json_2.mime == 'application/json'

    converter_xml = Conversion.get_converter('application/xml')
    assert converter_xml


if __name__ == '__main__':
    test_Conversion_get_converter()

# Generated at 2022-06-13 22:16:09.514844
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    assert Formatting().format_headers(b"{'test': 'test'}") == "{'test': 'test'}"


# Generated at 2022-06-13 22:16:16.681626
# Unit test for constructor of class Formatting
def test_Formatting():
    class Environment:
        def get_headers(self, req):
            return 'headers'
        def get_body(self, req):
            return 'body'
        def __init__(self, charset=None):
            self.charset = charset
    env = Environment()
    f = Formatting(['headers', 'body'], env)
    assert f.enabled_plugins[0].env == env
    assert f.enabled_plugins[0].format_headers('headers') == 'headers-headers'
    assert f.enabled_plugins[1].env == env
    assert f.enabled_plugins[1].format_body('body', 'mime') == 'body-mime-body'

# Generated at 2022-06-13 22:16:28.477792
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert(converter.supported_mime == 'application/json')


# Generated at 2022-06-13 22:16:37.501762
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    s = Formatting(['colors'], env=Environment())
    assert s.format_body('{"answer": 42}', 'application/json') == '\x1b[36m{\x1b[39;49;00m\n   \x1b[33m"answer"\x1b[39;49;00m \x1b[33m:\x1b[39;49;00m \x1b[34m42\x1b[39;49;00m\n\x1b[36m}\x1b[39;49;00m\n'

# Generated at 2022-06-13 22:16:51.409719
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    # Unit test for method format_headers of class Formatting
    import json
    from httpie.compat import is_py26

    class FormatterStub(object):
        def __init__(self, *args, **kwargs):
            pass

        def format_headers(self, headers):
            return json.dumps(headers)

    f = Formatting(['stub'], formatter=FormatterStub)

    headers_str = '''HTTP/1.1 200 OK
Content-Length: 0
Content-Type: text/html
Date: Sat, 09 Sep 2017 11:25:10 GMT
Server: nginx

'''

# Generated at 2022-06-13 22:17:05.178377
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    assert Formatting(groups=['colors'], colors=True).format_headers('HTTP/1.1 200 OK\nETag: "bcc2bcad7929ea9c902a9eabacf2d340"') == 'HTTP/1.1 200 OK\nETag: "bcc2bcad7929ea9c902a9eabacf2d340"'
    assert Formatting(groups=['colors'], colors=True, style='solarized').format_headers('HTTP/1.1 200 OK\nETag: "bcc2bcad7929ea9c902a9eabacf2d340"') == 'HTTP/1.1 200 OK\nETag: "bcc2bcad7929ea9c902a9eabacf2d340"'

# Generated at 2022-06-13 22:17:08.465924
# Unit test for constructor of class Formatting
def test_Formatting():
    assert Formatting(['colors'])
    assert Formatting(['colors', 'format'])

# Generated at 2022-06-13 22:17:11.398545
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    test_mime = 'text/html'
    res = Conversion.get_converter(test_mime)
    assert res
    assert res.mime == 'text/html'

# Generated at 2022-06-13 22:17:13.797623
# Unit test for constructor of class Formatting
def test_Formatting():
    F = Formatting(["json"])
    assert F.enabled_plugins[0].__class__.__name__ == "JSONFormatter"



# Generated at 2022-06-13 22:17:15.072245
# Unit test for constructor of class Formatting
def test_Formatting():
    emtpy_group = []
    assert Formatting(emtpy_group)

# Generated at 2022-06-13 22:17:28.491599
# Unit test for method get_converter of class Conversion

# Generated at 2022-06-13 22:17:37.307062
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Test with a specific case
    env = Environment()
    f = Formatting(groups=['colors'], env=env)
    content = '{"a": "b"}'
    mime = 'application/json'
    assert f.format_body(content, mime) == '\x1b[37m{\x1b[39;49;00m\n  \x1b[37m"a"\x1b[39;49;00m: \x1b[37m"b"\x1b[39;49;00m\n\x1b[37m}\x1b[39;49;00m'
    # Test with multiple formatters
    f = Formatting(groups=['colors', 'json'], env=env)

# Generated at 2022-06-13 22:17:40.455752
# Unit test for constructor of class Formatting
def test_Formatting():
    groups = ['colors']
    env = Environment()
    formatter = Formatting(groups, env=env)
    assert formatter

# Generated at 2022-06-13 22:17:42.357835
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    env.config["format"] = ["all", "colors", "formatters", "formatters_ordered"]
    fmt = Formatting(groups=env.config["format"], env=env)
    assert fmt is not None



# Generated at 2022-06-13 22:17:49.246750
# Unit test for constructor of class Formatting
def test_Formatting():
    # 1.1
    groups = ['colors']
    env = Environment()
    kwargs = {}
    fmt = Formatting(groups, env, **kwargs)
    print('Test for constructor of class Formatting')
    print('Test for groups = \'colors\'')
    print('Test for env = Environment()')
    print('Test for kwargs = {}')
    print('Test for fmt = Formatting(groups, env, **kwargs)')
    print('Test finished')
    # 1.2
    # Missing test cases


# Generated at 2022-06-13 22:17:56.510220
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert Conversion.get_converter(mime='application/json').mime == 'application/json'
    assert Conversion.get_converter(mime='application/xml').mime == 'application/xml'
    assert Conversion.get_converter(mime='application/yaml').mime == 'application/yaml'
    assert not Conversion.get_converter(mime='application/unknown')

# Generated at 2022-06-13 22:18:06.876854
# Unit test for constructor of class Formatting
def test_Formatting():
    header = (
        'HTTP/1.1 200 OK\r\n'
        'Date: Fri, 31 Dec 1999 23:59:59 GMT\r\n'
        'Content-Type: text/plain\r\n'
        'Content-Length: 2\r\n'
        '\r\n'
    )
    body = 'OK'
    
    # Default initialization
    formatter = Formatting()
    assert formatter.enabled_plugins == []
    
    # Formatters are enabled by default
    env = Environment(formatter='colors')
    formatter = Formatting(env=env)
    assert formatter.enabled_plugins[0].name == 'colors'
    
    # Formatters are disabled by setting 'formatter' env to 'off'
    env = Environment(formatter='off')
    form

# Generated at 2022-06-13 22:18:14.305122
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    headers = [
        '# comment',
        'Foo: bar',
        'Content-Type: application/json'
    ]
    headers_str = '\n'.join(headers)
    groups = ['colors', 'headers']
    f = Formatting(groups)
    assert '\x1b[32m# comment\x1b[39m' in f.format_headers(headers_str)
    assert '\x1b[33mContent-Type: application/json\x1b[39m' in f.format_headers(headers_str)



# Generated at 2022-06-13 22:18:17.419393
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'
    print("Testing conversion of '" + mime + "'...")
    print("Converter plugin: ")
    converter = Conversion.get_converter(mime)
    print(converter)
    assert converter is not None
    assert converter.mime == mime
    print("OK")



# Generated at 2022-06-13 22:18:28.982193
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'text/html'
    converter = Conversion.get_converter(mime)
    assert converter.__class__.__name__ == 'JSONConverter'
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    assert converter.__class__.__name__ == 'JSONConverter'
    mime = 'invalid/json'
    converter = Conversion.get_converter(mime)
    assert converter == None

if __name__ == '__main__':
    test1 = test_Conversion_get_converter()
    print("Test case 1 of function get_converter() in class Conversion : Passed")

# Generated at 2022-06-13 22:18:41.070426
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    available_plugins = plugin_manager.get_formatters_grouped()
    enabled_plugins = []
    for group in ["color"]:
        for cls in available_plugins[group]:
            enabled_plugins.append(cls)

    for plugin in enabled_plugins:
        p = plugin(env=Environment(),)
        formatted_content = p.format_body("some content", "application/json")
        assert formatted_content == "some content"

# Generated at 2022-06-13 22:18:42.674585
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    print(Conversion.get_converter("text/html"))


# Generated at 2022-06-13 22:18:44.987023
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Test case 1: get_converter is None
    assert Conversion.get_converter(None) is None
    # Test case 2: get a converter
    assert isinstance(Conversion.get_converter('text/html'), ConverterPlugin)


# Generated at 2022-06-13 22:18:56.103221
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    env = Environment()
    headers = """Content-Type: application/json
Date: Thu, 09 Nov 2017 01:24:28 GMT
Server: Werkzeug/0.12.2 Python/2.7.13

"""
    formatting_object = Formatting(groups=['colors'],env=env)
    formatted_headers = formatting_object.format_headers(headers)
    assert formatted_headers == """\x1b[36mContent-Type: application/json\x1b[0m
\x1b[36mDate: Thu, 09 Nov 2017 01:24:28 GMT\x1b[0m
\x1b[36mServer: Werkzeug/0.12.2 Python/2.7.13\x1b[0m

"""


# Generated at 2022-06-13 22:19:01.953843
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    test_env = Environment(colors=False, stdin=None, stdout=None, stderr=None,
                           stdin_isatty=False, stdout_isatty=False,
                           stderr_isatty=False)

    test_str = "Content-Type: application/json\nServer: nginx"
    test_formatting = Formatting(groups=[], env=test_env)
    assert test_formatting.format_headers(test_str) == test_str

    test_formatting = Formatting(groups=["headers"], env=test_env)
    assert test_formatting.format_headers(test_str) == """\
Server: nginx
Content-Type: application/json"""


# Generated at 2022-06-13 22:19:12.825328
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    groups = ["colors", "formatters", "syntax_highlighters"]
    env = Environment()
    kwargs = {}
    fmt = Formatting(groups, env, **kwargs)
    assert fmt.enabled_plugins == []

    group = "colors"
    for cls in available_plugins[group]:
        p = cls(env, **kwargs)
        if p.enabled:
            fmt.enabled_plugins.append(p)

    assert fmt.enabled_plugins != []
    for p in fmt.enabled_plugins:
        assert p.enabled
    assert fmt.format_headers("testing format_headers") == "testing format_headers"
    assert fmt.format_body("test", "") == "test"

# Generated at 2022-06-13 22:19:14.109750
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter.mime == 'application/json'

# Generated at 2022-06-13 22:19:18.162817
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter("application/json")
    assert(converter.mime == "application/json")
    converter = Conversion.get_converter("application/xml")
    assert(converter.mime == "application/xml")

# Generated at 2022-06-13 22:19:21.077213
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():

    mime = 'text/html'
    expected = Conversion.get_converter(mime)
    assert expected


# Generated at 2022-06-13 22:19:36.714237
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    f = Formatting(["testing"])
    expected_json_output = """\n{
    "name": "Joy",
    "age": 23
}\n"""
    assert f.format_body("""{"name": "Joy", "age": 23}""", "application/json") == expected_json_output
    expected_html_output = """\n<html>
    <head>
        <title>HTML</title>
    </head>
    <body>
        <p>This is test.</p>
    </body>
</html>\n"""
    assert f.format_body("""<html>
    <head>
        <title>HTML</title>
    </head>
    <body>
        <p>This is test.</p>
    </body>
</html>""", "text/html")

# Generated at 2022-06-13 22:19:55.370417
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    # Initialize class
    Formatting_object = Formatting(["highlighting"])
    # Have a file to read
    content_file_name = "data.json"
    # Open file
    content_file = open(content_file_name)
    # Read file
    content = content_file.read()
    # Close file
    content_file.close()
    # Get formatted version of content
    formatted_content = Formatting_object.format_body(content, "application/json")
    # Check if the formatted content is colored
    if formatted_content.find("\x1b[") >= 0:
        print("Formatting.format_body works properly")
    else:
        print("Formatting.format_body doesn't work properly")
    # Have a file to write the new formatted content

# Generated at 2022-06-13 22:20:05.362951
# Unit test for constructor of class Formatting

# Generated at 2022-06-13 22:20:16.902783
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    if __name__ == '__main__':
        try:
            env = Environment(colors=256)
        except AttributeError:
            env = Environment()
        env.config['style'] = 'paraiso-light'
        obj = Formatting(groups=['colors'], env=env, colors=256)
        mime = "application/json"
        content = "{\"test\":\"123\"}"

# Generated at 2022-06-13 22:20:19.635396
# Unit test for constructor of class Formatting
def test_Formatting():
    f = Formatting(groups=['default'], env=Environment())
    assert f.enabled_plugins is not None


# Generated at 2022-06-13 22:20:28.143271
# Unit test for constructor of class Formatting
def test_Formatting():
    available_plugins = plugin_manager.get_formatters_grouped()
    collected_names = [c.name for c in available_plugins['highlighting']]
    expected_names = ['colors', 'colors_256', 'colors_16m']
    assert collected_names == expected_names, "Names of highlighting plugins were not collected correctly"
    formatting = Formatting(['highlighting'])
    highlighted_plugins = [p.name for p in formatting.enabled_plugins]
    assert highlighted_plugins == expected_names, "Enabled plugins were not selected correctly"
test_Formatting()

# Generated at 2022-06-13 22:20:39.858553
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    import sys
    import os
    import io
    import json
    import logging

    def test_logging(test_string):
        logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
        logging.info(test_string)


# Generated at 2022-06-13 22:20:45.931995
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = ['colors']
    env = Environment()
    kwargs = {}
    f = Formatting(groups, env, **kwargs)

    content = '{"key1": "val1", "key2": "val2"}'
    mime = 'application/json'
    assert '\033[34m' in f.format_body(content, mime)

# Generated at 2022-06-13 22:20:55.151463
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    converter = Conversion.get_converter('application/json')
    assert converter != None
    converter = Conversion.get_converter('application/xml')
    assert converter != None
    converter = Conversion.get_converter('text/html')
    assert converter != None
    converter = Conversion.get_converter('text/plain')
    assert converter != None
    converter = Conversion.get_converter('text/css')
    assert converter != None
    converter = Conversion.get_converter('application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    assert converter != None


# Generated at 2022-06-13 22:21:05.544695
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    input_test_cases = ((1, "test from format_body"), (2, """test2 from format_body"""),
                        (3, """test3 from format_body"""))
    specific_formatters = Formatting(["colors", "formatters-specific"])
    for i, test_case in input_test_cases:
        actual = specific_formatters.format_body(test_case, "text/html; charset=utf-8")
        if i == 1:
            assert actual == "\u001b[32mtest from format_body\u001b[39m"
        if i == 2:
            assert actual == "\u001b[33mtest2 from format_body\u001b[39m"

# Generated at 2022-06-13 22:21:08.266357
# Unit test for constructor of class Formatting
def test_Formatting():
    Formatting([], **{})
    Formatting([], Environment(), **{})


# Generated at 2022-06-13 22:21:37.114688
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.output import BINARY_SUPPRESSED_NOTICE

    env = Environment()
    env.stdout = io.StringIO()

    fmt = Formatting(['colors'], env=env)
    assert fmt.format_headers('') == ''

    fmt = Formatting(['colors'], env=env)
    assert fmt.format_headers('key') == '\033[37mkey\033[0m'

    fmt = Formatting(['colors'], env=env)
    assert fmt.format_headers('key: value') == '\033[37mkey:\033[0m \033[36mvalue\033[0m'

    fmt = Formatting(['colors'], env=env)

# Generated at 2022-06-13 22:21:48.961147
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    assert not is_valid_mime("/")
    assert not is_valid_mime("/text")
    assert not is_valid_mime("text/")
    assert not is_valid_mime("text")
    assert not is_valid_mime(".")
    assert not is_valid_mime(".text")
    assert not is_valid_mime(".txt")
    assert not is_valid_mime("text/.")
    assert not is_valid_mime("text/txt")
    assert is_valid_mime("text/plain")
    assert is_valid_mime("text/PLAIN")
    assert is_valid_mime("text/plain+json")
    assert is_valid_mime("text/PLAIN+json")

# Generated at 2022-06-13 22:21:55.240696
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'text/plain'
    status = 1
    if is_valid_mime(mime):
        for converter_class in plugin_manager.get_converters():
            if converter_class.supports(mime):
                status = 0
                assert (status == 0)
    else:
        status = -1
        assert (status == -1)

# Test for method format_headers of class Formatting

# Generated at 2022-06-13 22:22:07.312825
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Test with mime type 'text/html'
    mime = 'text/html'
    converter = Conversion.get_converter(mime)
    assert converter.mime == mime

    # Test with mime type 'text/xml'
    mime = 'text/xml'
    converter = Conversion.get_converter(mime)
    assert converter.mime == mime

    # Test with mime type 'application/xml'
    mime = 'application/xml'
    converter = Conversion.get_converter(mime)
    assert converter.mime == mime

    # Test with mime type 'application/json'
    mime = 'application/json'
    converter = Conversion.get_converter(mime)
    assert converter.mime == mime

    # Test with mime type